# TEST_DATA_CT_PURE_ASSEMBLE_RECORD_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_ASSEMBLE_RECORD_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_ASSEMBLE_RECORD_V0
target: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
cases:
- case_id: assemble_simple_record
  expected_outcome: SUCCESS
  bindings:
    fields:
      name: Alice
      age: 30
      active: true
  expected:
    record:
      name: Alice
      age: 30
      active: true
- case_id: assemble_nested_record
  expected_outcome: SUCCESS
  bindings:
    fields:
      user_id: '123'
      profile:
        email: alice@example.com
        role: admin
  expected:
    record:
      user_id: '123'
      profile:
        email: alice@example.com
        role: admin
```

## Intent

Test record assembly from field values.
