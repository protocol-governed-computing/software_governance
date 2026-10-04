# TEST_DATA_CT_PURE_EXTRACT_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_EXTRACT_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_EXTRACT_V0
target: capability_transforms::CT_PURE_EXTRACT_V0
cases:
- case_id: extract_top_level_field
  expected_outcome: SUCCESS
  bindings:
    from:
      name: Alice
      age: 30
    path: name
    type: string
  expected:
    result: Alice
- case_id: extract_nested_field
  expected_outcome: SUCCESS
  bindings:
    from:
      user:
        id: '123'
        role: admin
    path: user.role
    type: string
  expected:
    result: admin
- case_id: extract_nested_numeric
  expected_outcome: SUCCESS
  bindings:
    from:
      config:
        timeout: 30
        retries: 3
    path: config.timeout
    type: number
  expected:
    result: 30
```

## Intent

Test JSONPath-based value extraction from structured data.
