# INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0

Architectural Invariant

## Machine

```yaml
fqdn: artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: artifact
core:
  enforcement_stage:
  - enforced_elsewhere
  enforced_by: the build's verification stage, over the dispatch it sealed and the assertions it ran
  violation_response: FAIL_IMMEDIATELY
  in_force:
    not_in_force_when: superseded_by
assert_projection:
  applies_to_kinds:
  - WF
  - IN
  - INVARIANT
  - STRUCTURE
```

---

## Purpose

Presence is not force.

A superseded artifact stays **present**. It is compiled, readable and reachable by inspection, so
the relation it declares can be read and a claim made under it can still be evaluated. It is not
**in force**. It is not enforced, not a place execution can start, not an admission gate, and not a
selection candidate.

`INVARIANT_SUPERSEDED_NOT_REFERENCED_V0` keeps live artifacts from naming a superseded one. That
covers what acquires effect by being named. It cannot cover what acquires effect by being present:
an invariant derives an assertion because it is compiled, and a workflow is dispatchable because it
has an entry. This invariant covers those.

---

## How it is checked

The predicate is one: an artifact is in force unless it declares `superseded_by`. The build asks it
wherever presence would confer effect:

| Path | What a superseded artifact loses |
|---|---|
| selection of a boundary mode | it offers no mode to a build |
| assertion derivation | an invariant derives no assertion |
| dispatch entry | a workflow is no place execution can start |
| dispatch admission | an intent is no admission gate |

The build's verification stage then checks what was produced, not the paths that produced it. A
superseded workflow with a dispatch entry, a superseded intent with an admission contract, or a
superseded invariant whose assertion ran fails the build. A path added later that does not ask the
predicate is refused there, rather than leaving a predecessor and its successor both in force.

---

## Why this is checked over outputs

The gap this closes was found by symptom. A superseded placement invariant went on being enforced
and failed a build with a message naming neither supersession nor the predecessor. A correct
reference check existed and did not cover it, because nobody had enumerated the paths on which
presence confers effect. An enumeration is only as good as its last update. A check over what the
build produced does not depend on one.

---

## What this realizes
```yaml
core:
  rule: 'A superseded artifact MUST NOT confer effect. It remains compiled and inspectable, and it is
    not enforced, not dispatchable, not admitted through and not selectable.

    '
  summary: A superseded artifact is present and not in force
```
