# INVARIANT_CS_SURFACE_CLOSED_V1

## Machine

```yaml
fqdn: capability_side_effects::INVARIANT_CS_SURFACE_CLOSED_V1
artifact_kind: INVARIANT
version: V1
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: capability_side_effects
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  handler: pgs_governance.registry.handlers.assert_cs_surface_closed_v0
  scope:
    applies_to:
    - PLATFORM
  allowed_capability_side_effects:
  - capability_side_effects::CS_APPENDONLY_JSONL_V0
  - capability_side_effects::CS_CLOCK_V0
  - capability_side_effects::CS_MUTABLE_JSON_V0
  - capability_side_effects::CS_REGISTRY_V0
  - capability_side_effects::CS_SNAPSHOT_QUERY_V0
  - capability_side_effects::CS_TEXT_ARTIFACT_V0
  applies_to_kinds:
  - CS
```

---

## Purpose

Ensure the CS surface is closed for PGC Platform Snapshot V1.

**Core Principle**: A closed snapshot is a complete, finite, auditable side-effect universe
*for that snapshot*. The PGC reference platform has a deliberately small side-effect universe
(the storage-contract triple: append-only ledger, mutable JSON, registry).

---

## What this realizes
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
