# INVARIANT_WF_ANNOUNCEMENT_DISTINCT_V0

## Machine

```yaml
fqdn: workflow::INVARIANT_WF_ANNOUNCEMENT_DISTINCT_V0
artifact_kind: INVARIANT
version: V0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: workflow
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - WF
```

## Summary

A terminal node announces each moment at most once, and every moment it announces is a declared
event artifact. An announcement that names the same moment twice is either a mistake or two
different moments that were not distinguished, and a reader can act on neither.

## What this realizes
For every `WF` artifact, for every node of type `EXIT` or `EXIT_SUCCESS` declaring `emit`:

1. `emit` MUST be a moment or an ordered sequence of moments. A single moment is a sequence of one.
2. No moment MAY appear twice in one node's `emit`.
3. Every moment named MUST be a fully-qualified identity, so that what is announced resolves to a
   declared artifact rather than to a name somebody hoped existed.

## Why this is checked here rather than trusted

The order in which moments are announced is normative — it is the order a reader of the account sees
— and an ordered sequence is exactly the shape in which a repeat is easy to introduce and invisible
afterwards. A moment announced twice produces an account stating that something happened twice when
it happened once, and nothing downstream can tell the difference: the trail is append-only, so the
second entry is as permanent as the first.

The narrower reading — that a repeat is harmless because both entries name the same moment — is the
one this refuses. Two entries are two occurrences to anybody counting them, and counting them is
what an account is for.
