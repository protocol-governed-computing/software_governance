# CT_EXEC_EMIT_V0

## Header (Mandatory)

- **Artifact Code:** CT_EXEC_EMIT_V0
- **Artifact Kind:** atom
- **Governed By:** capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Supersedes:** NONE
- **Dependencies:** NONE

---

## Machine

```yaml
fqdn: capability_transforms::CT_EXEC_EMIT_V0
artifact_kind: CAPABILITY_TRANSFORM
version: V0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Emit terminal value
  refusal: never
  description: Mark the explicit termination point of a transform pipeline and return the final result
    value.
  inputs:
    value:
      type: any
      required: true
      description: The value to emit as the result
  outputs:
    result:
      type: any
      required: true
      description: The propagated output value
machine:
  ct_kind: atom
  ct_purity: ct_exec
  operation: EMIT
  implementation:
    module: capability_transforms.implementation.ct_exec_emit_v0
    callable: execute
```
