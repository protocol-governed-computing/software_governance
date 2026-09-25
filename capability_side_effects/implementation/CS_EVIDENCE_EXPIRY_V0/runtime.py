"""Execution-only host for CS_EVIDENCE_EXPIRY_V0.

Ends retention of evidence whose declared window has closed, and records that it ended.

Three things this host does not decide, because deciding them here would put the authority in the
mechanism rather than in the declarations:

**It does not decide the window.** `retention_window_days` arrives from the artifact's
configuration, which is to say from the snapshot. There is no operation that changes it and no
default that would let a missing one pass as zero or as forever — absent, it refuses.

**It does not decide the time.** `as_of` is an input, supplied by the governed clock. A host reading
its own clock would let a determination depend on something the environment supplied and nothing
declared, and an operator who moved the host clock could expire anything.

**It does not decide what is exempt.** The record of an expiry is appended to a stream that admits
no deletion. The exemption follows from where the record is kept, so no flag here grants it and
none could be cleared to withdraw it.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Tuple


class EvidenceExpiryRuntime:
    """Execution-only host for CS_EVIDENCE_EXPIRY_V0."""

    capability_kind = "CS"
    _default_capability_code = "CS_EVIDENCE_EXPIRY_V0"

    # An attestation ends with what it attests to. Recognised by suffix because an attestation names
    # its subject; a host inferring the relation some other way would be deciding what attests to
    # what, which is the artifact's business and not the host's.
    _ATTESTATION_SUFFIXES = (".attestation.json", ".sig", ".signature.json")

    def __init__(self, config: Dict[str, Any] | None = None,
                 metadata: Dict[str, Any] | None = None,
                 capability_code: str | None = None):
        self._config = config or {}
        self._metadata = metadata or {}
        self.capability_code = capability_code or self._default_capability_code

    # -- declared configuration -------------------------------------------------------------

    def _window(self) -> Tuple[int | None, str | None]:
        """The declared window in days, or a refusal.

        No default. A window that defaulted to zero would expire everything on first run, and one
        that defaulted to unbounded would retain everything while reporting success — each is a
        retention policy nobody declared.
        """
        raw = self._config.get("retention_window_days")
        if raw is None:
            return None, "retention_window_days is not declared; this capability supplies no default"
        try:
            days = int(raw)
        except (TypeError, ValueError):
            return None, f"retention_window_days is not an integer: {raw!r}"
        if days < 0:
            return None, f"retention_window_days is negative: {days}"
        return days, None

    def _deletion_stream(self) -> Tuple[str | None, str | None]:
        stream = self._config.get("deletion_record_stream")
        if not stream:
            return None, ("deletion_record_stream is not declared; an expiry that records nothing "
                          "cannot be distinguished later from evidence never written")
        return str(stream), None

    # -- operations -------------------------------------------------------------------------

    def execute(self, *, op: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a validated CS operation."""
        if op == "SURVEY":
            return self._survey(payload)
        if op == "EXPIRE":
            return self._expire(payload)
        return {"result_status": "BACKEND_ERROR",
                "message": f"No backend handler for op: {op}"}

    def _partition(self, payload: Dict[str, Any]) -> Tuple[Dict[str, Any] | None, List, List, datetime]:
        """Split a store into what is within its window and what is past it.

        Returns (refusal, within, past, as_of). A refusal is returned rather than raised: a caller
        supplying no instant is a violation the workflow routes on, not a failure of the host.
        """
        days, problem = self._window()
        if problem:
            return {"result_status": "VIOLATION", "message": problem}, [], [], None

        raw_as_of = payload.get("as_of")
        if not raw_as_of:
            return ({"result_status": "VIOLATION",
                     "message": "as_of is required and comes from the governed clock; this host "
                                "does not read one"}, [], [], None)
        try:
            as_of = datetime.fromisoformat(str(raw_as_of).replace("Z", "+00:00"))
        except ValueError as exc:
            return ({"result_status": "VIOLATION",
                     "message": f"as_of is not an ISO-8601 instant: {exc}"}, [], [], None)
        if as_of.tzinfo is None:
            as_of = as_of.replace(tzinfo=timezone.utc)

        store = payload.get("store_path")
        if not store or not os.path.isdir(store):
            return ({"result_status": "BACKEND_ERROR",
                     "message": f"evidence store is not reachable: {store!r}"}, [], [], as_of)

        cutoff = as_of - timedelta(days=days)
        within: List[Tuple[str, datetime]] = []
        past: List[Tuple[str, datetime]] = []
        for root, _dirs, files in os.walk(store):
            for name in files:
                path = os.path.join(root, name)
                closed = self._closed_at(path)
                if closed is None:
                    continue
                (past if closed < cutoff else within).append((path, closed))
        return None, within, past, as_of

    def _closed_at(self, path: str) -> datetime | None:
        """When the trace this file belongs to closed.

        Read from the record where the record states it. A file that does not say when it closed is
        left alone rather than expired on a filesystem timestamp: mtime says when bytes were last
        written, which is not when a determination was made, and expiring on it would end retention
        by a rule nobody declared.
        """
        try:
            with open(path, "r", encoding="utf-8") as handle:
                head = handle.read(65536)
        except (OSError, UnicodeDecodeError):
            return None
        for key in ("closed_at", "trace_closed_at", "completed_at"):
            marker = f'"{key}"'
            if marker not in head:
                continue
            try:
                record = json.loads(head)
            except json.JSONDecodeError:
                continue
            value = record.get(key) if isinstance(record, dict) else None
            if not value:
                continue
            try:
                stamp = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
            except ValueError:
                return None
            return stamp if stamp.tzinfo else stamp.replace(tzinfo=timezone.utc)
        return None

    def _survey(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        refusal, within, past, _ = self._partition(payload)
        if refusal:
            return refusal
        return {
            "result_status": "SUCCESS",
            "examined": len(within) + len(past),
            "within_window": len(within),
            "past_window": len(past),
            "subjects": sorted(os.path.basename(p) for p, _ in past),
        }

    def _expire(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        refusal, within, past, as_of = self._partition(payload)
        if refusal:
            return refusal

        stream, problem = self._deletion_stream()
        if problem:
            return {"result_status": "VIOLATION", "message": problem}

        ended: List[str] = []
        for path, _closed in past:
            # The attestation goes with its subject, in that order: a subject removed while its
            # attestation remained would leave a signed statement about nothing.
            for suffix in self._ATTESTATION_SUFFIXES:
                attestation = path + suffix
                if os.path.exists(attestation):
                    try:
                        os.remove(attestation)
                        ended.append(os.path.basename(attestation))
                    except OSError as exc:
                        return {"result_status": "BACKEND_ERROR",
                                "message": f"attestation could not be ended: {exc}"}
            try:
                os.remove(path)
            except OSError as exc:
                return {"result_status": "BACKEND_ERROR",
                        "message": f"evidence could not be ended: {exc}"}
            ended.append(os.path.basename(path))

        record = {
            "capability": self.capability_code,
            "as_of": as_of.isoformat().replace("+00:00", "Z"),
            "retention_window_days": self._window()[0],
            "examined": len(within) + len(past),
            "expired": len(ended),
            "subjects": sorted(ended),
        }
        try:
            os.makedirs(os.path.dirname(stream) or ".", exist_ok=True)
            with open(stream, "a", encoding="utf-8") as handle:
                handle.write(json.dumps(record, sort_keys=True) + "\n")
        except OSError as exc:
            # The record is not optional. Reporting success here would leave a platform unable to
            # distinguish evidence ended under a declared window from evidence never written, which
            # is the state this capability exists to prevent.
            return {"result_status": "BACKEND_ERROR",
                    "message": f"expiry happened and could not be recorded: {exc}"}

        return {
            "result_status": "SUCCESS",
            "examined": record["examined"],
            "expired": record["expired"],
            "subjects": record["subjects"],
            "record_id": f"{record['as_of']}:{record['expired']}",
        }
