# INVARIANT_IDENTITY_MIGRATION_CROSSCHECK_V0

## Machine

```yaml
fqdn: fb.constitution::INVARIANT_IDENTITY_MIGRATION_CROSSCHECK_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.constitution::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  handler: pgs_governance.registry.handlers.assert_identity_migration_crosscheck_v0
  enforcement:
    phase: validation
    order: 7
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

**Temporary migration assertion.** During the transition from path-derived identity to declared identity, this proves the switch changed no FQDN value: every artifact's declared identity must equal the value the folder would have produced.

It is retired once the no-op is proven. Leaving it permanent would keep the filesystem secretly authoritative over identity, defeating the decoupling.

---

## Validation Rules

### Rule 1: Declared equals derived

For every artifact with a path-derived value, the declared FQDN MUST equal the path-derived FQDN.

---

## Rationale

The decoupling is only safe if it preserves identity exactly. This assertion is the gate that proves it, and its removal (once green) is the final step that makes the declaration — not the folder — the sole authority.
