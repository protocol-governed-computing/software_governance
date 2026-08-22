# INVARIANT_ASSERT_NOT_RUNTIME_REFERENCED_V0

## Machine

```yaml
fqdn: conformance::INVARIANT_ASSERT_NOT_RUNTIME_REFERENCED_V0
artifact_kind: INVARIANT
version: V0
governed_by: conformance::CONSTITUTION_ASSERT_V0
authority: pgc.platform
concern: conformance
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    level: ERROR
    order: 22
  applies_to_kinds:
  - WF
  - CC
  - CS
  - CT
  - RB
```

---

## Purpose

An ASSERT is compile-time governance. If an executable artifact can reference one, governance becomes reachable from execution — and a rule that runs during execution is no longer a property proven before it.

---

## Validation Rules

### Rule 1: No executable artifact references an ASSERT

No WF, CC, CS, CT or RB artifact may reference an `ASSERT_*` code, at any depth of its machine block.

---

## Rationale

The compile/execute boundary is only real if it is one-way. ASSERTs read the compiled graph; nothing in the compiled graph may read back.
