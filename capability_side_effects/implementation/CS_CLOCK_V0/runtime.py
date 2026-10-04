"""Execution-only host for CS_CLOCK_V0.

Answers the current instant. The whole capability is one call the runtime is not allowed to make
itself — a workflow node reading a clock directly would be reaching outside the composition, which
is what a declared side effect exists to prevent.
"""

from datetime import datetime, timezone
from typing import Any, Dict


class ClockRuntime:
    """Execution-only host for CS_CLOCK_V0."""

    capability_kind = "CS"
    _default_capability_code = "CS_CLOCK_V0"

    def __init__(self, config: Dict[str, Any] | None = None,
                 metadata: Dict[str, Any] | None = None,
                 capability_code: str | None = None):
        self._config = config or {}
        self._metadata = metadata or {}
        self.capability_code = capability_code or self._default_capability_code

    def execute(self, *, op: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a validated CS operation."""
        if op != "NOW":
            return {"result_status": "BACKEND_ERROR",
                    "message": f"No backend handler for op: {op}"}
        try:
            now = datetime.now(timezone.utc)
        except Exception:  # a runtime with no clock is a backend failure, not a violation
            return {"result_status": "BACKEND_ERROR", "message": "no clock available"}

        # Seconds by default: a trail's times must advance, and finer resolution than the business
        # asked for invites comparing two records that differ by nothing it cares about.
        if str(self._config.get("precision", "seconds")).lower() == "milliseconds":
            stamp = now.isoformat(timespec="milliseconds").replace("+00:00", "Z")
        else:
            stamp = now.isoformat(timespec="seconds").replace("+00:00", "Z")
        return {"result_status": "SUCCESS", "timestamp": stamp}
