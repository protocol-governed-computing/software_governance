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
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - CT
```

## Summary

Every Capability Transform (CT) must produce outputs that exactly match the keys declared in its governing Capability Contract (CC).

## What this realizes
For every CT artifact:
1. CT must declare `governed_by` binding to a CC artifact
2. CC must declare `output` section with explicit keys
3. CT implementation must return dict with EXACTLY those keys
4. Extra keys, missing keys, or mismatched types are violations

## Where it applies
- **Artifact Types**: CT
- **Validation Phase**: Phase 5 (ASSERT)
- **Enforcement**: MANDATORY (build fails on violation)

## Examples

### ✅ VALID

**CC Declaration:**
```yaml
output:
  seed_bytes: hex_string
```

**CT Implementation:**
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
    "extra_field": "value"  # ❌ Not in contract
}
```

## Rationale

Output contract matching ensures:
- Predictable transform behavior
- Type safety at compilation
- Explicit interface contracts
- No hidden outputs
- Traceable data flow

## Related Artifacts

- `capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0` - Governs CT behavior
- `capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0` - Defines CC schema

---

## What this realizes
```yaml
core:
  rule: All CT artifacts must produce outputs matching their CC declaration keys and types
  summary: CT output structure must match declared capability contract
```
