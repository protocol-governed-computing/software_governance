# INVARIANT_MOLECULE_PURITY_CONSISTENT_V0

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_MOLECULE_PURITY_CONSISTENT_V0
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

A molecule's declared purity agrees with its steps: a molecule declared deterministic contains only deterministic steps.

## What this realizes
For every `CT` artifact declaring `ct_kind: molecule` and `ct_purity: ct_pure`:

1. Every transform reachable through its steps and loop bodies MUST declare `ct_pure` or `ct_exec`.
2. A molecule reaching a step declaring `ct_impure` MUST itself declare `ct_impure`.

## Why this is checked here rather than trusted

The declaration is what a reader relies on to see where determinism ends. A molecule claiming determinism while containing a step that is not would hide the one place the reader most needs to see.
