"""
runtime.py — Execution-only host for CS_SNAPSHOT_QUERY_V0.

Responsibilities:
- Execute read-only inspection operations against a bound snapshot
- Resolve every operation through `inspector.api.query`, never through compiled projections
- Translate inspection outcomes into CEP-visible result_status values

This host reads and never writes. There is no code path here that opens the snapshot for
modification, which is what makes an observation usable as evidence about the composition a
workflow is executing from.
"""

from typing import Any, Dict

from inspector import api


class SnapshotQueryRuntime:
    """Execution-only host for CS_SNAPSHOT_QUERY_V0."""

    capability_kind = "CS"
    _default_capability_code = "CS_SNAPSHOT_QUERY_V0"

    def __init__(
        self,
        config: Dict[str, Any],
        metadata: Dict[str, Any],
        capability_code: str | None = None,
    ):
        """
        Parameters:
            config: Runtime configuration — requires {"snapshot_root": "<path>"}
            metadata: Injected metadata (capability, operations, schema)
            capability_code: Optional override for CS identity (metadata only)
        """
        self._metadata = dict(metadata)
        assert isinstance(self._metadata, dict), "metadata must be dict"
        assert "capability" in self._metadata, "metadata must contain 'capability'"

        snapshot_root = (config or {}).get("snapshot_root")
        if not snapshot_root or not str(snapshot_root).strip():
            raise ValueError(
                "CS_SNAPSHOT_QUERY_V0 requires a non-empty 'snapshot_root' in its binding policy — "
                "the snapshot to observe is bound explicitly, never discovered"
            )
        self._snapshot_root = str(snapshot_root)
        self._capability_code = capability_code or self._default_capability_code

    # -- operations ---------------------------------------------------------

    def execute(self, op: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Dispatch a declared operation. An undeclared op is a violation, never a default."""
        if op == "QUERY":
            return self.query(payload)
        if op == "CATALOG":
            return self.catalog(payload)
        return {
            "result_status": "VIOLATION",
            "detail": f"{op!r} is not an operation CS_SNAPSHOT_QUERY_V0 declares",
        }

    def query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Execute one published inspection operation against the bound snapshot."""
        operation = (payload or {}).get("operation")
        if not operation or not isinstance(operation, str):
            return {
                "result_status": "VIOLATION",
                "detail": "'operation' is required and must name a published si.* operation",
            }

        params = (payload or {}).get("params") or {}
        if not isinstance(params, dict):
            return {
                "result_status": "VIOLATION",
                "detail": f"'params' must be an object, got {type(params).__name__}",
            }

        try:
            status, result = api.query(operation, params, self._snapshot_root)
        except (FileNotFoundError, NotADirectoryError) as exc:
            return {"result_status": "BACKEND_ERROR", "detail": str(exc)}
        except KeyError as exc:
            # An unpublished operation is a caller error, not a backend failure.
            return {"result_status": "VIOLATION", "detail": str(exc)}

        # The inspection surface already speaks the platform's result vocabulary; pass it through
        # rather than remapping, so a consumer sees what the surface actually said.
        return {"result_status": status, "result": result}

    def catalog(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """List the inspection operations the bound snapshot answers."""
        try:
            operations = api.operations(self._snapshot_root)
        except (FileNotFoundError, NotADirectoryError) as exc:
            return {"result_status": "BACKEND_ERROR", "detail": str(exc)}
        return {"result_status": "SUCCESS", "operations": list(operations)}
