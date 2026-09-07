# INVARIANT_CONCERN_NOT_AUTHORITY_V0

## Machine

```yaml
fqdn: federation::INVARIANT_CONCERN_NOT_AUTHORITY_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: federation
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  handler: pgs_governance.registry.handlers.assert_concern_not_authority_v0
  scope:
    applies_to:
    - PLATFORM
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

## A concern classification alone is refused as grounds for an authority

No value declared as a `concern` MUST also be declared as an `authority`. The two sets MUST be
disjoint.

A concern is the semantic subject an artifact is about; an authority is the entity from which
jurisdiction derives. `2e` CA-6: "A concern classification MUST NOT constitute an authority or a
jurisdiction." The ruling's clause 2 states the same, and the defect it was written for is precisely
a concern name promoted to a boundary — twenty-six of them.

This predicate is what the collapsed identifier made unwritable. While concern and authority were one
string, no check could tell an unlisted namespace from an illegitimate boundary; with separate
carriers the question is a set comparison.
