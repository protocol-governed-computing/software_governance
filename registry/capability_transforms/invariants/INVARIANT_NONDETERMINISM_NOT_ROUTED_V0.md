# INVARIANT_NONDETERMINISM_NOT_ROUTED_V0

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_NONDETERMINISM_NOT_ROUTED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: capability_transforms
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - CT
  - CC
```

## Summary

A non-deterministic atom's results are offered, never decided: a deterministic step consumes them before anything routes on them.

## What this realizes
1. No `CC` pipeline step MAY invoke, as its transform, an atom declaring `ct_impure`.
2. For every molecule, the step named by `emit` MUST NOT be an atom declaring `ct_impure`.

## Why this is checked here rather than trusted

A capability contract routes on the outcome of its steps. If a non-deterministic atom were a step, the contract would route on what the atom said, and governance would reduce to recording it. Placing a deterministic step between the atom and every route keeps each decision where the composition can see and replay it.
