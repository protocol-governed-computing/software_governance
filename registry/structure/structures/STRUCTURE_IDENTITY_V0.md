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
fqdn: fb.structure::STRUCTURE_IDENTITY_V0
artifact_kind: STRUCTURE
version: V0
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0
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
        method: module_path
        rules:
        - namespace: capability_side_effects
        - namespace: capability_transforms
        - namespace: fb.actor
        - namespace: fb.artifact
        - namespace: fb.authority
        - namespace: fb.capability_contracts
        - namespace: fb.capability_side_effects
        - namespace: fb.capability_transforms
        - namespace: fb.compiler
        - namespace: fb.conformance
        - namespace: fb.cryptographic_trust
        - namespace: fb.event
        - namespace: fb.execution
        - namespace: fb.execution_placement
        - namespace: fb.execution_scheduling
        - namespace: fb.execution_topology
        - namespace: fb.federation
        - namespace: fb.governance
        - namespace: fb.intent
        - namespace: fb.lifecycle
        - namespace: fb.runtime_binding
        - namespace: fb.security_domain
        - namespace: fb.structure
        - namespace: fb.surface_contract
        - namespace: fb.trace
        - namespace: fb.transport
        - namespace: fb.vocabulary
        - namespace: fb.workflow
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
