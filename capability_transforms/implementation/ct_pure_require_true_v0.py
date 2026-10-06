"""
CT_PURE_REQUIRE_TRUE_V0

Pure Capability Transform (Atom)

Purpose:
    Refuse unless a boolean is true.

Implementation:
    - Generic boolean gate — no domain words
    - Returns SUCCESS when value is true
    - Raises VIOLATION when value is false, or is not a boolean
"""

from typing import Dict, Any

from capability_transforms.implementation.ct_executor import CTExecutionError


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    if "value" not in inputs:
        raise CTExecutionError("CT_PURE_REQUIRE_TRUE_V0: missing required input 'value'")

    value = inputs["value"]

    if not isinstance(value, bool):
        raise CTExecutionError(
            f"CT_PURE_REQUIRE_TRUE_V0: value must be boolean, got {type(value).__name__}"
        )
    if not value:
        raise CTExecutionError("CT_PURE_REQUIRE_TRUE_V0: value is false")

    return {
        "result_status": "SUCCESS",
        "held": True,
    }
