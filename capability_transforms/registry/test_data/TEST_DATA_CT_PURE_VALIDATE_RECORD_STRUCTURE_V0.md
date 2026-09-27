# TEST_DATA_CT_PURE_VALIDATE_RECORD_STRUCTURE_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
target: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
cases:
- case_id: valid_record
  expected_outcome: SUCCESS
  bindings:
    record:
      name: Alice
      age: 30
    schema:
      name:
        required: true
        type: string
      age:
        required: true
        type: integer
  expected:
    violations: []
- case_id: invalid_record_missing_field
  expected_outcome: SUCCESS
  bindings:
    record:
      name: Bob
    schema:
      name:
        required: true
        type: string
      age:
        required: true
        type: integer
  expected:
    violations:
    - field: age
      rule: required
      message: Field 'age' is required
```

## Intent

Test record structure validation against schema.
