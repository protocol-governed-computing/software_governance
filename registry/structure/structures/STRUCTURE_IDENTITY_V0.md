# STRUCTURE_IDENTITY_V0

**Artifact Type**: STRUCTURE
**Version**: V0
**Status**: CANONICAL
**Authority**: CONSTITUTIONAL

---

## Purpose

Single source of truth for artifact identity. Defines FQDN composition, normalization rules from short names to fully qualified IDs, and identity uniqueness constraints.

---

## Machine

```yaml
fqdn: structure::STRUCTURE_IDENTITY_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
core:
  summary: Consolidated artifact identity and FQDN configuration
  description: 'Defines the canonical identity system for all protocol artifacts. Namespace identity is
    federation-boundary-scoped under the fb.* scheme.

    '
identity:
  fqdn:
    format: '{namespace}::{artifact_code}'
    namespace:
      derivation:
        rules:
        - namespace: capability_side_effects
        - namespace: capability_transforms
        - namespace: actor
        - namespace: artifact
        - namespace: authority
        - namespace: capability_contracts
        - namespace: compiler
        - namespace: conformance
        - namespace: cryptographic_trust
        - namespace: event
        - namespace: execution
        - namespace: execution_placement
        - namespace: execution_scheduling
        - namespace: execution_topology
        - namespace: federation
        - namespace: governance
        - namespace: intent
        - namespace: lifecycle
        - namespace: runtime_binding
        - namespace: security_domain
        - namespace: structure
        - namespace: surface_contract
        - namespace: trace
        - namespace: transport
        - namespace: vocabulary
        - namespace: workflow
    uniqueness:
      scope: global
      constraint: no_duplicate_fqdn
normalization:
  short_name_resolution:
    allowed: true
    resolution_phase: compile_time
    rules:
    - local_scope_first
    - global_search
    on_ambiguity: FAIL
```
