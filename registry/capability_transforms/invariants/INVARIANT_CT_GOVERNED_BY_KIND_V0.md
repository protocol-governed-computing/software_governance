# INVARIANT_CT_GOVERNED_BY_KIND_V0

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_CT_GOVERNED_BY_KIND_V0
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

Every transform is governed by exactly one of the three constitutions that govern transforms, decided by what it declares: its kind and its purity.

## What this realizes
For every `CT` artifact:

1. An atom declaring `ct_pure` or `ct_exec` MUST be governed by
   `capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0`.
2. An atom declaring `ct_impure` MUST be governed by
   `capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0`.
3. A molecule MUST be governed by `capability_transforms::CONSTITUTION_MOLECULES_V0`.
4. A transform declaring no kind or no purity is refused: what it is cannot be placed.

## Why this is checked here rather than trusted

Three constitutions govern transforms. A transform naming the wrong one would escape the rules of the one that describes it — a non-deterministic atom claiming the deterministic constitution would never have its results recorded. Placement follows from the declaration, so it is checked against the declaration.
