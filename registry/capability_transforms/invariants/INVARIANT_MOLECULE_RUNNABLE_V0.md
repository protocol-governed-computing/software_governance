# INVARIANT_MOLECULE_RUNNABLE_V0

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_MOLECULE_RUNNABLE_V0
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
```

## Summary

Every molecule in a composition can be run: each step and each loop body resolves to a transform the runtime can run, and no molecule contains itself.

## What this realizes
For every `CT` artifact declaring `ct_kind: molecule`:

1. It MUST declare a non-empty `atom_stream` and an `emit`.
2. Every step MUST be of kind `atom`, `molecule` or `loop`.
3. An `atom` step MUST name a transform declaring `ct_kind: atom`; a `molecule` step and a `loop`
   body MUST name a transform declaring `ct_kind: molecule`.
4. A `loop` step MUST state the collection it runs over.
5. No molecule MAY reach itself through its steps, directly or through others.
6. `emit` MUST name a step the molecule declares.

## Why this is checked here rather than trusted

A molecule that cannot be run is a declaration nothing can keep, and a molecule reaching itself is repetition with no stated bound. Both are knowable when the composition is built, so neither is left to fail when an act runs.
