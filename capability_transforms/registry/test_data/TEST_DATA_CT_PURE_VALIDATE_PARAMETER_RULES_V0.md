# TEST_DATA_CT_PURE_VALIDATE_PARAMETER_RULES_V0

## Machine

```yaml
fqdn: capability_transforms::TEST_DATA_CT_PURE_VALIDATE_PARAMETER_RULES_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: capability_transforms
core:
  summary: Test vectors for CT_PURE_VALIDATE_PARAMETER_RULES_V0
target: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
cases:
- case_id: all_rules_pass
  expected_outcome: SUCCESS
  bindings:
    parameters:
      amount: 100
      type: deposit
    rules:
    - field: amount
      op: gt
      value: 0
  expected:
    valid: true
    failed_rule: null
- case_id: rule_fails
  expected_outcome: VIOLATION
  bindings:
    parameters:
      amount: -50
      type: deposit
    rules:
    - field: amount
      op: gt
      value: 0
  expected: {}
```

## Intent

Test parameter validation against rules.
