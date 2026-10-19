# INVARIANT_ATOM_OUTPUT_PURITY_V0

Architectural Invariant

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: capability_transforms
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the runtime's CT executor, which treats anything an atom raises other than CTExecutionError
    as a fault that ends the run, and transform conformance, which fails a case on a fault
assert_projection:
  applies_to_kinds:
  - CT
```

## Summary

An atom answers in one of two ways. It returns a dict of its declared outputs, or it raises
`CTExecutionError`, which the contract reads as VIOLATION. Anything else it raises is a fault, not an
answer.

## What this realizes
For every CT atom:
1. `execute()` returns a dict of its declared outputs, or raises `CTExecutionError`
2. Every atom raises `CTExecutionError` on missing or malformed input
3. `core.refusal` declares how it judges its subject (`SCHEMA_CAPABILITY_TRANSFORM_V0`): `raises`
   refuses by raising `CTExecutionError`; `returns` yields the judgement as an output, so the step
   succeeds whatever it found; `never` makes no judgement
4. A judgement that is not a refusal is an output (e.g., `{"is_eligible": false}`)
5. Any other exception, or a `None` result, is a fault: the run ends, it is never routed, and a
   conformance case fails on it whatever the case expected

The refusal is recognised by its class name, `CTExecutionError`, so an atom may define its own class
of that name without importing the runtime.

## Where it applies
- **Artifact Types**: CT
- **Enforcement**:
  - the CT executor at every run (`CTFault`);
  - conformance at every build.

## Examples

### ✅ VALID - A finding as an output

```python
def execute(inputs: dict, context=None) -> dict:
    return {"is_eligible": inputs["training_completed"]}
```

### ✅ VALID - A declared refusal (`refusal: raises`)

```python
class CTExecutionError(RuntimeError):
    """The inputs do not form a book identity."""

def execute(inputs: dict, context=None) -> dict:
    title = " ".join(inputs["title"].split())
    if not title:
        raise CTExecutionError("a book carries a title")
    return {"identity_key": title.casefold()}
```

### ❌ INVALID - A fault where an answer belongs

```python
def execute(inputs: dict, context=None) -> dict:
    if inputs["assigned_count"] >= inputs["quota"]:
        raise ValueError("Quota exhausted")  # ❌ fault: not a refusal, and not an output
    return {"quota_available": True}
```

## Rationale

Two answers keep execution explicit:
- every outcome a workflow routes on is declared: SUCCESS, or VIOLATION from `CTExecutionError`;
- a defect is never mistaken for a judgement, because a fault is refused rather than routed;
- a run or a build names the atom that broke instead of answering.

## Related Artifacts

- `capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0` - Defines pure transform behavior
- `capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0` - Every vector case states its outcome

---

## What this realizes
```yaml
core:
  rule: A CT atom returns its declared outputs or raises CTExecutionError; anything else it raises is a
    fault
  summary: An atom answers with outputs or CTExecutionError, never with an exception of another kind
```
