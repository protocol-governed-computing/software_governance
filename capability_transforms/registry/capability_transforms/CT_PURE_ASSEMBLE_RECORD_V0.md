# CT_PURE_ASSEMBLE_RECORD_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_ASSEMBLE_RECORD_V0
- **Artifact Kind:** atom
- **Governed By:** capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Supersedes:** NONE
- **Dependencies:** NONE

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
artifact_kind: CAPABILITY_TRANSFORM
version: V0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Assemble record object
  refusal: never
  description: Combines multiple input values into a single structured record object.
  inputs:
    fields:
      type: object
      required: true
      description: Key-value map of fields to include in the record
  outputs:
    record:
      type: object
      required: true
      description: The assembled record object
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: ASSEMBLE_RECORD
  implementation:
    module: capability_transforms.implementation.ct_pure_assemble_record_v0
    callable: execute
```
