"""
CT_PURE_COMPARE_EQUAL_V0

Pure Capability Transform (Atom)

Purpose:
    Compare two values for equality. Domain-independent reusable predicate.

Inputs:
    left  — any value
    right — any value

Outputs:
    is_equal — boolean; True iff left == right
"""

from typing import Any, Dict


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    if "left" not in inputs or "right" not in inputs:
        raise ValueError("CT_PURE_COMPARE_EQUAL_V0: requires inputs 'left' and 'right'")
    return {"is_equal": inputs["left"] == inputs["right"]}