# TEST_DATA_CT_PURE_SELECT_RECORDS_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_SELECT_RECORDS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_SELECT_RECORDS_V0
target: capability_transforms::CT_PURE_SELECT_RECORDS_V0
cases:
- case_id: select_by_exact_value
  expected_outcome: SUCCESS
  bindings:
    source:
    - actor_id: AC_aaa
      state: ACCEPTED
    - actor_id: AC_bbb
      state: UNVERIFIED
    - actor_id: AC_ccc
      state: ACCEPTED
    filter:
      state: ACCEPTED
  expected:
    extracted:
    - actor_id: AC_aaa
      state: ACCEPTED
    - actor_id: AC_ccc
      state: ACCEPTED
- case_id: select_by_field_presence
  expected_outcome: SUCCESS
  bindings:
    source:
    - tx_id: TX_001
      status: PENDING
    - tx_id: TX_002
    filter:
      status: present
  expected:
    extracted:
    - tx_id: TX_001
      status: PENDING
- case_id: select_multi_criteria
  expected_outcome: SUCCESS
  bindings:
    source:
    - id: R1
      type: validator
      active: true
    - id: R2
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
- case_id: select_nothing_matching_answers_empty
  expected_outcome: SUCCESS
  bindings:
    source:
    - actor_id: AC_aaa
      state: ACCEPTED
    filter:
      state: REJECTED
  expected:
    extracted: []
- case_id: select_from_nothing_answers_empty
  expected_outcome: SUCCESS
  bindings:
    source: []
    filter:
      state: ACCEPTED
  expected:
    extracted: []
- case_id: select_from_a_source_that_is_not_an_array_is_refused
  expected_outcome: VIOLATION
  bindings:
    source:
      actor_id: AC_aaa
    filter:
      state: ACCEPTED
  expected: {}
```

## Intent

Test selection by exact value, field presence and several criteria, that nothing matching answers an empty array, and that malformed input is refused.
