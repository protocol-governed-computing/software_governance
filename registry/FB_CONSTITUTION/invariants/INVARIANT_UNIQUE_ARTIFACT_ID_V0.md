# INVARIANT_UNIQUE_ARTIFACT_ID_V0

## Machine

```yaml
artifact_kind: INVARIANT
version: V0
governed_by: fb.constitution::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
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
