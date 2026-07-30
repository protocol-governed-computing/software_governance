# STRUCTURE_CONFORMANCE_POLICY_V0

## Machine

```yaml
fqdn: fb.conformance::STRUCTURE_CONFORMANCE_POLICY_V0
artifact_kind: STRUCTURE
version: V0
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0

core:
  description: Defines CONFORMANCE_POLICY artifact rules

conformance:
  scope:
    - CT

  execution:
    mode: runtime

  expectations:
    default: NOT_NONE

  failure:
    behavior: FAIL_BUILD
```
