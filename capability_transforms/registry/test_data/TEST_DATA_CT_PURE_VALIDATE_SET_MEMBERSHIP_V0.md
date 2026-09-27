# TEST_DATA_CT_PURE_VALIDATE_SET_MEMBERSHIP_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
target: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
cases:
- case_id: value_in_set
  expected_outcome: SUCCESS
  bindings:
    value: active
    allowed_set:
    - active
    - pending
    - inactive
  expected:
    is_member: true
- case_id: value_not_in_set
  expected_outcome: VIOLATION
  bindings:
    value: deleted
    allowed_set:
    - active
    - pending
    - inactive
  expected: {}
```

## Intent

Test set membership validation.
