# TEST_DATA_CT_PURE_LOOKUP_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_LOOKUP_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_LOOKUP_V0
target: capability_transforms::CT_PURE_LOOKUP_V0
cases:
- case_id: lookup_string_value
  expected_outcome: SUCCESS
  bindings:
    key: status
    map:
      status: active
      priority: high
  expected:
    result: active
- case_id: lookup_numeric_value
  expected_outcome: SUCCESS
  bindings:
    key: count
    map:
      count: 100
      limit: 500
  expected:
    result: 100
- case_id: lookup_object_value
  expected_outcome: SUCCESS
  bindings:
    key: config
    map:
      config:
        timeout: 30
        retries: 3
      enabled: true
  expected:
    result:
      timeout: 30
      retries: 3
- case_id: lookup_array_value
  expected_outcome: SUCCESS
  bindings:
    key: tags
    map:
      tags:
      - important
      - urgent
      archived: false
  expected:
    result:
    - important
    - urgent
```

## Intent

Test key-value lookup in mapping objects.
