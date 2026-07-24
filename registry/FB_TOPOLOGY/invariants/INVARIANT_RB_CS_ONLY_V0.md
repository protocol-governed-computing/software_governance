# INVARIANT_RB_CS_ONLY_V0

Architectural Invariant

## Machine

```yaml
artifact_kind: INVARIANT
version: V0
governed_by: fb.topology::CONSTITUTION_RUNTIME_BINDING_V0
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - RB
```

## Summary

Runtime bindings supply concrete implementations for declared CS capabilities. They must
never bind CT, WF, CC, or IN artifacts — those artifact types are resolved through
different runtime mechanisms.

## Rule

For every RB artifact, every key in `core.bindings`:
1. MUST be a valid FQDN
2. The artifact code component of the FQDN MUST start with `CS_`

## Enforcement Scope

- **Artifact Types**: RB
- **Validation Phase**: ASSERT (Phase 5, compile-time, hard fail)
- **Enforced By**: ASSERT_RB_CS_ONLY_V0

## Rationale

RB artifacts are the configuration bridge between declared CS capabilities and physical
host implementations. Binding a non-CS artifact confuses the execution model and indicates
an architectural error. The compiler must catch this before the artifact reaches runtime.

---

## Rule Statement

```yaml
core:
  rule: All binding keys in RB core.bindings must resolve to CS artifact codes (CS_ prefix)
  summary: RB bindings must reference CS artifacts only
```
