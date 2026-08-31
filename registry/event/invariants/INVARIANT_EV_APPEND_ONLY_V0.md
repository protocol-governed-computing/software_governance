# INVARIANT_EV_APPEND_ONLY_V0

Architectural Invariant

## Machine

```yaml
fqdn: event::INVARIANT_EV_APPEND_ONLY_V0
artifact_kind: INVARIANT
version: V0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: event
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - EV
```

## Summary

Event stores are append-only. EV artifact declarations must not express mutability semantics.
No field in an EV schema or extensions block may declare mutation intent.

## What this realizes
For every EV artifact:
1. `core.schema` MUST NOT contain mutation-signaling field names (`_update`, `_delete`, `_patch`, `_mutate`)
2. `extensions` MUST NOT declare mutation operation keys

Runtime append-only enforcement is provided by CS_APPENDONLY_JSONL_V0 and the execution engine.

## Where it applies
- **Artifact Types**: EV
- **Validation Phase**: ASSERT (Phase 5, compile-time)
- **Runtime Enforcement**: CS_APPENDONLY_JSONL_V0 (hard fail at execution time)
- **Enforced By**: ASSERT_EV_APPEND_ONLY_V0

## Rationale

Append-only event stores are the foundation of auditability and replay. Mutation operations
on event records destroy the causal chain. This invariant ensures that no EV artifact
accidentally declares mutation semantics that could be interpreted as permitting mutation.

---

## What this realizes
```yaml
core:
  rule: EV artifacts must not contain update/delete/patch/mutate field declarations
  summary: EV artifacts must not declare mutation operations
```
