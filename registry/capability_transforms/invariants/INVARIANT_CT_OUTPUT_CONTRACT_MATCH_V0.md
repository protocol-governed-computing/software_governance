# INVARIANT_CT_OUTPUT_CONTRACT_MATCH_V0

Architectural Invariant

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_CT_OUTPUT_CONTRACT_MATCH_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: capability_transforms
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: transform conformance, which every build runs after it compiles; a completed case fails
    when the result carries a key the transform does not declare or lacks one it does
assert_projection:
  applies_to_kinds:
  - CT
```

## Summary

A Capability Transform's result carries exactly the outputs the transform declares in
`core.outputs`: no fewer, and no others.

## What this realizes
For every CT:
1. `core.outputs` declares each output by name and type
2. A completed run returns a result carrying exactly those outputs
3. A missing output or an extra key is a violation

Two checks hold this together, and neither alone is enough:
- **At compile time**, `conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0` requires every case
  that expects SUCCESS to state each declared output, and nothing else.
- **At conformance**, each case runs the implementation and fails when the result differs from the
  declared outputs in any key, before its values are compared.

The vector ties the declaration to stated values. Conformance ties the implementation to both.

## Where it applies
- **Artifact Types**: CT
- **Enforcement**: transform conformance, in every build (`runtime conformance`)

## Examples

### ✅ VALID

**CT declaration:**
```yaml
outputs:
  seed_bytes:
    type: hex_string
    required: true
```

**CT implementation:**
```python
def execute(inputs, context=None):
    return {
        "seed_bytes": "0x123abc..."
    }
```

### ❌ INVALID

**Missing key:**
```python
return {}  # ❌ Missing "seed_bytes"
```

**Extra key:**
```python
return {
    "seed_bytes": "0x123abc...",
    "result_status": "SUCCESS"  # ❌ Not declared; a CT step's outcome is SUCCESS unless it refuses
}
```

## Rationale

Output contract matching ensures:
- Predictable transform behavior
- Explicit interface contracts
- No hidden outputs
- Traceable data flow

## Related Artifacts

- `capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0` - Governs CT behavior
- `conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0` - The compile-time half

---

## What this realizes
```yaml
core:
  rule: A completed CT run returns exactly the outputs its declaration names
  summary: CT output structure must match the transform's declared outputs
```
