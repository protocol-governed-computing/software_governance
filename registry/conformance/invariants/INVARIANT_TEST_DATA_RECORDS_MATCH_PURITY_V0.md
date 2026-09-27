# INVARIANT_TEST_DATA_RECORDS_MATCH_PURITY_V0

## Machine

```yaml
fqdn: conformance::INVARIANT_TEST_DATA_RECORDS_MATCH_PURITY_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: conformance
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - TEST_DATA
```

## Summary

A case supplies a recorded result for exactly the non-deterministic steps of the transform it tests.

## What this realizes

For every case of a `TEST_DATA` artifact, with the paths of its target's steps read from the target as
sealed:

1. A case for a molecule MUST supply a recorded result for every step, at every pass, whose declared
   purity is `ct_impure`.
2. A case MUST NOT supply a recorded result for a step whose declared purity is anything else.
3. A case for an atom MUST supply no recorded result.
4. Every recorded result MUST be addressed by a path the target's steps actually have.

## Why this is checked when the domain compiles

A case supplying a result for a deterministic step asserts a replay that never happens; a case omitting
one for a non-deterministic step would run the step, and its expected result could not be exact. Either
way the case proves nothing about what it names. The mismatch is a defect in the declaration, so it is
refused where the declaration is compiled rather than discovered when the case runs.
