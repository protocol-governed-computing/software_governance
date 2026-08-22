# CT_PURE_GENERATE_ID_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_GENERATE_ID_V0
- **Artifact Kind:** atom
- **Governed By:** capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Supersedes:** NONE
- **Dependencies:** Keccak-256 (SHA-3)

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_GENERATE_ID_V0
artifact_kind: CAPABILITY_TRANSFORM
version: V0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Generate deterministic ID
  refusal: never
  description: Generates a deterministic unique identifier based on input data using Keccak-256 hashing.
  inputs:
    prefix:
      type: string
      required: true
      description: Identifier prefix (e.g., AC, WF, IN)
    data:
      type: any
      required: true
      description: Input data to hash for ID generation
  outputs:
    id:
      type: string
      required: true
      description: The generated deterministic ID
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: GENERATE_ID
  implementation:
    module: capability_transforms.implementation.ct_pure_generate_id_v0
    callable: execute
```
