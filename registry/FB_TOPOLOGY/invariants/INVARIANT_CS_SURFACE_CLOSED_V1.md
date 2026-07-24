# INVARIANT_CS_SURFACE_CLOSED_V1

## Machine

```yaml
artifact_kind: INVARIANT
version: V1
governed_by: fb.constitution::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  handler: pgs_governance.registry.handlers.assert_cs_surface_closed_v0
  scope:
    applies_to:
    - CS
  allowed_capability_side_effects:
  - capability_side_effects::CS_APPENDONLY_JSONL_V0
  - capability_side_effects::CS_MUTABLE_JSON_V0
  - capability_side_effects::CS_REGISTRY_V0
```

---

## Purpose

Ensure the CS surface is closed for PGC Platform Snapshot V1.

**Core Principle**: A closed snapshot is a complete, finite, auditable side-effect universe
*for that snapshot*. The PGC reference platform has a deliberately small side-effect universe
(the storage-contract triple: append-only ledger, mutable JSON, registry).

---

## Version History

- **V1**: Snapshot-scoped closed CS surface — the 3 storage-contract side effects of PGC
  Platform Snapshot V1. Replaces V0 (which enumerated RI-0's wider set, including
  `name_service` and the unimplemented fuzzy workflow/email side effects).
- **V0**: RI-0 mixed CS surface (faithful harvest). Retained in RI-0 / git history as provenance.

---

## Rule Statement

```yaml
core:
  description: 'CS surface must be closed for this platform snapshot: every controlled side effect is
    explicitly declared, every declared CS has a runtime implementation, and no undeclared CS may execute.
    This closes the CS surface of PGC Platform Snapshot V1 — the snapshot''s complete, enumerable side-effect
    universe, NOT a universal catalog. An enterprise extension is a new snapshot that recomputes its own
    closed surface.

    '
  clarification:
    closed_surface_definition: 'Closed CS surface means: Declared_CS_set == Executable_CS_set for THIS
      snapshot. No more, no less. All side effects are finite, enumerable, and auditable.

      '
    snapshot_scoped: 'Closure is snapshot-scoped, not universal. Baseline closed; extension open.

      '
```
