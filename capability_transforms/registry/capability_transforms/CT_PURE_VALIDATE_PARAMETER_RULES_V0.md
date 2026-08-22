# CT_PURE_VALIDATE_PARAMETER_RULES_V0

## 1. Intent

Evaluate declarative parameter constraint rules against a parameter map.

---

## 2. Rationale

Parameter rule validation is a generic governance primitive:
- Rules are declared in governance artifacts, not in code
- Supports operators: eq, neq, lte, gte, lt, gt, in, not_null
- Domain-agnostic — any parameter map can be validated against any rule set

---

## 3. Purity

| Property | Value |
|----------|-------|
| Purity | ct_pure |
| Kind | atom |

---

## 4. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| parameters | object | true | Parameter key-value map to validate |
| rules | array | true | Array of rule objects with field, op, and value/allowed |

---

## 5. Outputs

Produced only when every rule passes. A failed rule is refused rather than reported, so there is no
call in which `valid` is false or `failed_rule` is populated.

| Field | Type | Description |
|-------|------|-------------|
| valid | boolean | Always true — the transform returns only when all rules passed |
| failed_rule | object | Always null, for the same reason |

---

## 6. Result Status

This transform **refuses by raising** (`refusal: raises`): the failed rule is carried in the raised
error, not in a returned value. That is what lets a step route on the judgement — a `CT` step yields
`SUCCESS` when its transform returns and `VIOLATION` when it raises, so a transform that returned
`valid=false` would succeed on a rule that failed, and every branch declared for VIOLATION would be
unreachable.

| Status | Condition |
|--------|-----------|
| SUCCESS | All rules pass; `valid=true`, `failed_rule=null` |
| VIOLATION | The first rule that fails, named in the raised error. No outputs are returned |

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Validate parameters against rules
  refusal: raises
  description: Evaluates a set of declarative constraint rules (eq, gt, in, etc.) against a provided parameter
    map.
  inputs:
    parameters:
      type: object
      required: true
      description: Parameter key-value map to validate
    rules:
      type: array
      required: true
      description: List of constraint rule objects
  outputs:
    valid:
      type: boolean
      required: true
      description: Always true — a failed rule is raised, so the transform returns only when all
        rules passed
    failed_rule:
      type: object
      required: false
      nullable: true
      description: Always null — the rule that failed is carried in the raised error, never returned
machine:
  ct_kind: atom
  ct_purity: ct_pure
  implementation:
    module: capability_transforms.implementation.ct_pure_validate_parameter_rules_v0
    callable: execute
```
