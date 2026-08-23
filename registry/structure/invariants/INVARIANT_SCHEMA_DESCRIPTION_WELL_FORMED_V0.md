# INVARIANT_SCHEMA_DESCRIPTION_WELL_FORMED_V0

## Machine

```yaml
fqdn: structure::INVARIANT_SCHEMA_DESCRIPTION_WELL_FORMED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: structure
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - STRUCTURE
```

---

## Purpose

Hold three things about the descriptions the platform governs itself with: that every artifact kind
carries a disposition, that a description dispatched to a kind actually describes, and that a
description still matches the artifacts it describes.

## Every kind carries a disposition

A kind is `described` or `exempt`. A kind carrying neither is refused.

A kind absent from the dispatch table was absent for three different reasons and one representation —
nobody wrote a description, one exists and nobody named it, or the kind needs none. **A reader could
not tell a decision from an oversight**, and neither could any check. An exemption states its ground
beside it, so that the record is of a decision rather than of a silence.

## A dispatched description describes

A description names at least one required field and closes its surface. One doing neither admits every
declaration of its kind and refuses none.

This is not hypothetical. One kind was dispatched to exactly such a description and thirty-three
declarations passed it, because everything passes it. Dispatch made the kind *read* as governed while
governing nothing, which is why the count of dispatched kinds measures neither coverage nor
governance.

## A description matches what it describes

Every dispatched description is measured against every artifact of its kind. A description refusing an
artifact the composition currently carries is **reported**, and the report is the point: a stale
description refuses correct work with the authority of a rule.

Three descriptions were found to have drifted, at three separate undated divergences, and every one
was found by dispatching it and reading the hundred refusals it produced. That method works only
while nobody relies on the description. This reports the next one before a build does.

## What it does not reach

**What a declaration of a kind may contain.** That is the owning subdomain's to state. This invariant
is about a description existing, describing, and matching — never about what any description says.

**Descriptions of runtime data.** An authority state, a registry, an authenticated state and a trace
event are described beside the artifact-kind descriptions and are not artifact kinds. They are
dispatched by nothing because there is nothing to dispatch them to, and they are not this invariant's
subject.
