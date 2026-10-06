# TEST_DATA_CT_PURE_REQUIRE_TRUE_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_REQUIRE_TRUE_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_REQUIRE_TRUE_V0
target: capability_transforms::CT_PURE_REQUIRE_TRUE_V0
cases:
- case_id: value_true
  expected_outcome: SUCCESS
  bindings:
    value: true
  expected:
    held: true
- case_id: value_false
  expected_outcome: VIOLATION
  bindings:
    value: false
  expected: {}
```

## Intent

Test the boolean gate.
