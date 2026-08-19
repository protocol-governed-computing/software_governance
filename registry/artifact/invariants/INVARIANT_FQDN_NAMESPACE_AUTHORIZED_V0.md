# INVARIANT_FQDN_NAMESPACE_AUTHORIZED_V0

## Machine

```yaml
fqdn: fb.artifact::INVARIANT_FQDN_NAMESPACE_AUTHORIZED_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.governance::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  handler: pgs_governance.registry.handlers.assert_fqdn_namespace_authorized_v0
  enforcement:
    order: 6
  applies_to_kinds:
  - AC
  - CC
  - CONSTITUTION
  - CS
  - CT
  - EV
  - IN
  - INVARIANT
  - RB
  - SCHEMA
  - STRUCTURE
  - SURFACE
  - TE
  - TI
  - VOCAB
  - WF
```

---

## Purpose

Identity is declared by the artifact, not derived from its folder. The one constraint on a declared identity is that its **namespace must be authorized** — drawn from the identity authorization set (the identity rules, repurposed from derivation to authorization). A file may live anywhere in the tree; it may not mint an unauthorized namespace.

---

## Validation Rules

### Rule 1: Declared namespace is authorized

Every non-imported artifact's declared FQDN namespace MUST appear in the authorized namespace set for the build. Imported artifacts carry their origin namespace (resolved externally) and are exempt.

---

## Rationale

Decoupling identity from the filesystem removes the folder's accidental authority over identity. Authorization replaces derivation: the set of legal namespaces is declared once and enforced, so identity is free of the directory layout without becoming a free-for-all.
