# INVARIANT_EXECUTION_PLACEMENT_DECLARED_V0

## Machine

```yaml
fqdn: execution_placement::INVARIANT_EXECUTION_PLACEMENT_DECLARED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: execution_placement
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    scope: ALL_ARTIFACTS
  applies_to_kinds:
  - SNAPSHOT
  composition_check:
    rule: exactly_one
    subject: execution placement structure carried by the composition
    selector:
      namespace: execution_placement
      artifact_type: STRUCTURE
      artifact_code_prefix: STRUCTURE_EXECUTION_PLACEMENT_
```

---

## Purpose

A composition carries exactly one execution placement structure, and therefore records exactly one
placement mode.

## Where the selection is checked, and why not here

A composition check is a cardinality rule over the artifacts a snapshot carries. It cannot reach a
build configuration, and should not: what a build named is a fact about the build, established when
the build ran, and a snapshot that carried every available mode so an invariant could pick between
them would be carrying permissions it was not granted.

So the selection is enforced where it happens. The compiler reads the mode its build configuration
names, refuses where none or more than one is named or where the named mode is unauthorized
(`CONSTITUTION_EXECUTION_PLACEMENT_V0` §3), and materializes **only the structure it selected**.

This invariant is what makes that mechanical rather than trusted: whatever the compiler intended,
a composition reaching acceptance with two placement structures, or none, is refused. The surface
may declare every authorized mode; the composition may carry one.

## What this refuses

- **No placement structure.** A composition with no placement records no mode, and an arrangement
  nobody declared is not a default.
- **More than one.** Two structures are two answers to where execution runs. It means a compiler that
  materialized more than it selected, which is dangerous because the configuration would look correct.
