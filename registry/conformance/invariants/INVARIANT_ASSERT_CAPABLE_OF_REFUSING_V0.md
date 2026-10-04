# INVARIANT_ASSERT_CAPABLE_OF_REFUSING_V0

## Machine

```yaml
fqdn: conformance::INVARIANT_ASSERT_CAPABLE_OF_REFUSING_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: conformance
core:
  enforcement_stage:
  - declared_not_enforced
  enforced_by: conformance::CONSTITUTION_ASSERT_V0
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - INVARIANT
```

---

## Purpose

An obligation declaring that a violation fails the build has a check with a path that produces one.

## Why this is declared and not yet enforced

**It would refuse every build today, on obligations this subdomain may not write.**

Fourteen of eighty-seven checks have no refusal-producing path. Their obligations are declared by
`authority`, `actor`, `capability_side_effects`, `execution_topology`, `surface_contract` and this
subdomain — six owners, five of them not `conformance`. Each restates its own with the stage that
matches what its check does. Arming this first would fail every build on declarations nobody here is
entitled to correct.

**So it carries `declared_not_enforced`, which is the declaration this change introduced for exactly
this case.** The obligation is stated, the debt is countable, and nothing pretends it is in force.
The alternative was leaving it unwritten — indistinguishable from nobody having thought of it, which
is the defect this change is about, performed on itself.

## What arms it

Every one of the seventeen obligations named in `enforcement_capability`'s Stage 6 carrying a stage
that matches what its check does. Then this obligation's stage moves to `compiler_assertion`, and the
count of unenforced obligations is readable from the record every build already writes.

## Capability is what can be decided

The rule is *the check has a path that produces a refusal* — a property of one artifact, decidable
from it. It is **not** *the check has a path this obligation can reach*, which is a relation between
two artifacts, established once by reading and not decidable in general. Requiring the second would
demand what no author could supply, so fourteen is a floor and is stated as one.

## What it does not reach

**Whether a check has ever been observed to refuse.** Stronger than capability, needing a case per
check, and a separate change.

**The obligations of domains other than the platform.** Each domain's own, once the platform can
express what it needs.
