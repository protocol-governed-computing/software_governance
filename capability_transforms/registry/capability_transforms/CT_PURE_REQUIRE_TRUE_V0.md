# CT_PURE_REQUIRE_TRUE_V0

## 1. Intent

Refuse unless a boolean is true.

---

## 2. Rationale

A check that reports what it found does not decide. A capability decides, and answers with an
outcome. This atom turns a reported boolean into that decision:
- Succeeds when the value is true
- Refuses when the value is false
- Domain-agnostic — the value is provided as input

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
| value | boolean | true | Value that must be true |

---

## 5. Outputs

| Field | Type | Description |
|-------|------|-------------|
| held | boolean | True when the value was true |

---

## 6. Result Status

| Status | Condition |
|--------|-----------|
| SUCCESS | The value is true (held=true) |
| VIOLATION | The value is false, or is not a boolean |

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_REQUIRE_TRUE_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Refuse unless a boolean is true
  refusal: raises
  description: Succeeds when the given boolean is true and refuses when it is false.
  inputs:
    value:
      type: boolean
      required: true
      description: The value that must be true
  outputs:
    held:
      type: boolean
      required: true
      description: True when the value was true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  implementation:
    module: capability_transforms.implementation.ct_pure_require_true_v0
    callable: execute
```
