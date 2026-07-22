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
ct_code: CT_PURE_COMPARE_EQUAL_V0
version: v0
governed_by: fb.topology::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Compare two values for equality.
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
    module: pgs_transforms.implementation.transforms.atoms.ct_pure_compare_equal_v0
    callable: execute
```
