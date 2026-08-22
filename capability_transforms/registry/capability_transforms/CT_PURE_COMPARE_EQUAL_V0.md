# CT_PURE_COMPARE_EQUAL_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_COMPARE_EQUAL_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Status:** canonical

---

## 1. Summary

Compare two values for equality.

---

## 2. Inputs

| Field | Type |
|---|---|
| left | string |
| right | string |

---

## 3. Outputs

| Field | Type |
|---|---|
| is_equal | boolean |

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Compare two values for equality.
  refusal: returns
  inputs:
    left:
      type: string
      required: true
    right:
      type: string
      required: true
  outputs:
    is_equal:
      type: boolean
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: COMPUTE
  implementation:
    module: capability_transforms.implementation.ct_pure_compare_equal_v0
    callable: execute
```
