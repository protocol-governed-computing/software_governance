# TEST_DATA_CT_PURE_GENERATE_ID_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_GENERATE_ID_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_GENERATE_ID_V0
target: capability_transforms::CT_PURE_GENERATE_ID_V0
cases:
- case_id: generate_id_string_data
  expected_outcome: SUCCESS
  bindings:
    prefix: AC
    data: test_account
  expected:
    id: AC_ac8cc683f338b84f
- case_id: generate_id_object_data
  expected_outcome: SUCCESS
  bindings:
    prefix: WF
    data:
      workflow: build
      version: v1
  expected:
    id: WF_75382b9a6ab93c66
- case_id: generate_id_numeric_data
  expected_outcome: SUCCESS
  bindings:
    prefix: TX
    data: 12345
  expected:
    id: TX_d3ff95909dfb2231
- case_id: generate_id_deterministic
  expected_outcome: SUCCESS
  bindings:
    prefix: IN
    data: consistent
  expected:
    id: IN_c918e775137f8254
```

## Intent

Test deterministic ID generation using Keccak-256 hashing.
