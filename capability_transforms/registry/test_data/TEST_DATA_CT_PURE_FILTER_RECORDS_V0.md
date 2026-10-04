# TEST_DATA_CT_PURE_FILTER_RECORDS_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_FILTER_RECORDS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_FILTER_RECORDS_V0
target: capability_transforms::CT_PURE_FILTER_RECORDS_V0
cases:
- case_id: filter_by_exact_value
  expected_outcome: SUCCESS
  bindings:
    source:
    - actor_id: AC_aaa
      enrollment_status: ACTIVE
      stake: '32000000000'
    - actor_id: AC_bbb
      enrollment_status: INACTIVE
      stake: '32000000000'
    - actor_id: AC_ccc
      enrollment_status: ACTIVE
      stake: '16000000000'
    filter:
      enrollment_status: ACTIVE
  expected:
    extracted:
    - actor_id: AC_aaa
      enrollment_status: ACTIVE
      stake: '32000000000'
    - actor_id: AC_ccc
      enrollment_status: ACTIVE
      stake: '16000000000'
- case_id: filter_by_field_presence
  expected_outcome: SUCCESS
  bindings:
    source:
    - tx_id: TX_001
      status: PENDING
    - tx_id: TX_002
    - tx_id: TX_003
      status: PENDING
    filter:
      status: present
  expected:
    extracted:
    - tx_id: TX_001
      status: PENDING
    - tx_id: TX_003
      status: PENDING
- case_id: filter_multi_criteria
  expected_outcome: SUCCESS
  bindings:
    source:
    - actor_id: AC_aaa
      enrollment_status: ACTIVE
      stake: '32000000000'
    - actor_id: AC_bbb
      enrollment_status: ACTIVE
      stake: '16000000000'
    - actor_id: AC_ccc
      enrollment_status: INACTIVE
      stake: '32000000000'
    filter:
      enrollment_status: ACTIVE
      stake: '32000000000'
  expected:
    extracted:
    - actor_id: AC_aaa
      enrollment_status: ACTIVE
      stake: '32000000000'
- case_id: filter_single_match
  expected_outcome: SUCCESS
  bindings:
    source:
    - id: R1
      type: validator
      active: true
    - id: R2
      type: observer
      active: true
    - id: R3
      type: validator
      active: false
    filter:
      type: validator
      active: true
  expected:
    extracted:
    - id: R1
      type: validator
      active: true
```

## Intent

Test array filtering by exact-value match, field-presence check, and multi-criterion AND logic.
