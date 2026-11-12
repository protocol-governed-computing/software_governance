"""
CT_PURE_SELECT_RECORDS_V0

Pure Capability Transform (Atom)

Purpose:
    Select the records of an array that satisfy declared field criteria, and answer none when none
    do. It applies exactly the criteria `CT_PURE_FILTER_RECORDS_V0` applies.

    The filter refuses an empty result, which is right where the caller expected to find something.
    It is wrong for a read: "no record is in that state" is a true answer about what is held, not a
    failed lookup. Whether nothing matching is a problem is the caller's judgement, so this transform
    does not make it. The filter is kept for callers that mean "nothing matched" as a refusal.

Implementation:
    - Iterates source array, testing each record against all criteria (AND)
    - Criterion value "present" means field must exist and be non-None
    - Any other criterion value means field must equal that value exactly
    - Returns the matching records, possibly none
    - Raises CTExecutionError only when the inputs are malformed
    - Pure: no side effects, no state
"""

from typing import Any, Dict

from capability_transforms.implementation.ct_executor import CTExecutionError

_PRESENT = "present"


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Select the records of an array that satisfy declared field criteria.

    Args:
        inputs: {
            "source": list  - Array of record objects to select from
            "filter": dict  - Field criteria: {"field": value} or {"field": "present"}
        }

    Returns:
        {"extracted": list} — the records that match all criteria, possibly none

    Raises:
        CTExecutionError: if inputs are malformed
    """
    if "source" not in inputs:
        raise CTExecutionError("CT_PURE_SELECT_RECORDS_V0: missing required input 'source'")
    if "filter" not in inputs:
        raise CTExecutionError("CT_PURE_SELECT_RECORDS_V0: missing required input 'filter'")

    source = inputs["source"]
    criteria = inputs["filter"]

    if not isinstance(source, list):
        raise CTExecutionError(
            f"CT_PURE_SELECT_RECORDS_V0: 'source' must be an array, got {type(source).__name__}"
        )
    if not isinstance(criteria, dict):
        raise CTExecutionError(
            f"CT_PURE_SELECT_RECORDS_V0: 'filter' must be an object, got {type(criteria).__name__}"
        )

    def matches(record: Any) -> bool:
        if not isinstance(record, dict):
            return False
        for field, criterion in criteria.items():
            value = record.get(field)
            if criterion == _PRESENT:
                if value is None:
                    return False
            else:
                if value != criterion:
                    return False
        return True

    return {"extracted": [r for r in source if matches(r)]}
