# INVARIANT_CT_SURFACE_CLOSED_V1

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
  handler: pgs_governance.registry.handlers.assert_ct_surface_closed_v0
  scope:
    applies_to:
    - PLATFORM
  allowed_capability_transforms:
  - capability_transforms::CT_EXEC_EMIT_V0
  - capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
  - capability_transforms::CT_PURE_COMPARE_EQUAL_V0
  - capability_transforms::CT_PURE_EXTRACT_V0
  - capability_transforms::CT_PURE_FILTER_RECORDS_V0
  - capability_transforms::CT_PURE_GENERATE_ID_V0
  - capability_transforms::CT_PURE_LOOKUP_V0
  - capability_transforms::CT_PURE_MAP_RESULT_TO_HTTP_V0
  - capability_transforms::CT_PURE_PASSTHROUGH_V0
  - capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
  - capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
  - capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
  applies_to_kinds:
  - CT
```

---

## Purpose

Ensure the CT surface is closed for PGC Platform Snapshot V1.

**Core Principle**: A closed snapshot is a complete, finite, auditable executable universe
*for that snapshot*. The PGC reference platform has a deliberately small transform universe.

---

## Version History

- **V1**: Snapshot-scoped closed CT surface — the 12 neutral reference transforms of PGC
  Platform Snapshot V1. Replaces V0 (which enumerated RI-0's mixed universe, including
  blockchain/ai domain transforms). First PGC divergence for this invariant.
- **V0**: RI-0 mixed CT surface (faithful harvest). Retained in RI-0 / git history as provenance.

---

## Rule Statement

```yaml
core:
  description: 'CT surface must be closed for this platform snapshot: every executable capability transform
    is explicitly declared, every declared CT has a runtime implementation, and no undeclared CT may execute.
    This closes the CT surface of PGC Platform Snapshot V1 — it is the snapshot''s complete, enumerable
    transform universe, NOT a claim that PGC has enumerated every capability any enterprise may use. An
    enterprise extension is a new snapshot that recomputes its own closed surface.

    '
  clarification:
    closed_surface_definition: 'Closed CT surface means: Declared_CT_set == Executable_CT_set for THIS
      snapshot. No more, no less. All computation is finite, enumerable, and auditable.

      '
    snapshot_scoped: 'Closure is snapshot-scoped, not universal. Baseline closed; extension open.

      '
```
