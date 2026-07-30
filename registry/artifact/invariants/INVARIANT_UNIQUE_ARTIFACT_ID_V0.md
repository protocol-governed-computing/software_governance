# INVARIANT_UNIQUE_ARTIFACT_ID_V0

## Machine

```yaml
fqdn: fb.artifact::INVARIANT_UNIQUE_ARTIFACT_ID_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.governance::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
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

Ensures that every artifact in the compilation graph has a globally unique identity (FQDN).
Prevents silent overwrites where multiple physical files claim the same logical identity.

---

## Rule Statement

```yaml
core:
  description: Each fqdn_id must be unique across compilation graph
  anti_patterns:
  - duplicate_fqdn: Multiple artifacts share same fqdn_id
```
