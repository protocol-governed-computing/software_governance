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
fqdn: fb.constitution::STRUCTURE_IDENTITY_V0
artifact_kind: STRUCTURE
version: V0
governed_by: fb.constitution::CONSTITUTION_STRUCTURE_V0
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
        - namespace: fb.constitution
        - namespace: fb.topology
        - namespace: fb.transport
        - namespace: fb.authority
        - namespace: fb.vocabulary
        - namespace: fb.conformance
        - namespace: fb.identity
        - namespace: fb.blockchain
        - namespace: fb.ai_governance
        - namespace: fb.execution_placement
        - namespace: fb.execution_scheduling
        - namespace: fb.security_domain
        - namespace: fb.cryptographic_trust
        - namespace: fb.change_mgmt
        - namespace: capability_transforms
        - namespace: capability_side_effects
        - namespace: blockchain
        - namespace: ai_governance
        - namespace: structure
        - namespace: execution
        - namespace: compiler
        - namespace: ingress_gateway
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
