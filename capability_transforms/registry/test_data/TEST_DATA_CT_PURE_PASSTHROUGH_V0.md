# TEST_DATA_CT_PURE_PASSTHROUGH_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_PASSTHROUGH_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_PASSTHROUGH_V0
target: capability_transforms::CT_PURE_PASSTHROUGH_V0
cases:
- case_id: passthrough_string
  expected_outcome: SUCCESS
  bindings:
    value: hello world
  expected:
    value: hello world
- case_id: passthrough_number
  expected_outcome: SUCCESS
  bindings:
    value: 42
  expected:
    value: 42
- case_id: passthrough_object
  expected_outcome: SUCCESS
  bindings:
    value:
      key: test
      count: 123
  expected:
    value:
      key: test
      count: 123
- case_id: passthrough_array
  expected_outcome: SUCCESS
  bindings:
    value:
    - 1
    - 2
    - 3
  expected:
    value:
    - 1
    - 2
    - 3
- case_id: passthrough_boolean
  expected_outcome: SUCCESS
  bindings:
    value: true
  expected:
    value: true
```

## Intent

Test that PASSTHROUGH returns input value unchanged for various data types.
