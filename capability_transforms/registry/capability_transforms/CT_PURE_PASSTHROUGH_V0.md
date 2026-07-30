# CT_PURE_PASSTHROUGH_V0

## Header

- **Artifact Code:** CT_PURE_PASSTHROUGH_V0
- **Artifact Kind:** atom
- **Governed By:** fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Status:** draft
- **Dependencies:** NONE

---

## 1. Intent

Pass through an input value unchanged. Used for 1:1 payload mapping where no transformation is needed.

## 2. Purity

Pure. No side effects, no state mutation.

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_PASSTHROUGH_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Pass through value
  description: Returns the input value unchanged. Useful for explicit payload mapping in molecules or
    workflows.
  inputs:
    value:
      type: any
      required: true
      description: Value to pass through
  outputs:
    value:
      type: any
      required: true
      description: The identical input value
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PASSTHROUGH
  implementation:
    module: capability_transforms.implementation.ct_pure_passthrough_v0
    callable: execute
```
