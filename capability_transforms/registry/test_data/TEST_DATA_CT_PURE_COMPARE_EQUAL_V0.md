# TEST_DATA_CT_PURE_COMPARE_EQUAL_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_COMPARE_EQUAL_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: capability_transforms
target: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
cases:
- case_id: equal_values
  expected_outcome: SUCCESS
  bindings:
    left: SUCCESS
    right: SUCCESS
  expected:
    is_equal: true
- case_id: different_values_return_false
  expected_outcome: SUCCESS
  bindings:
    left: SUCCESS
    right: VIOLATION
  expected:
    is_equal: false
```

## Intent

Equal values compare equal, and different values return false rather than refusing.
