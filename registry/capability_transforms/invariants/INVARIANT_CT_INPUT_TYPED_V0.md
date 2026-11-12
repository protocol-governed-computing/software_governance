# INVARIANT_CT_INPUT_TYPED_V0

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_CT_INPUT_TYPED_V0
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
  - CC
```

---

## Purpose

A transform is given only values of the types it declares. A contract binds each input of each
transform step to a source: a literal, an input of the contract, or an output of an earlier step.
Every source with a declared type must have the type the transform declares for that input.

## Why it is checked at build

The runtime checks the types a workflow is entered with. It does not check what one step gives
another: it resolves a step's inputs and calls the transform. A step that gives a transform a value
it does not declare runs, and a transform that compares by equality can even decide correctly. The
declaration and the use then disagree, and nothing says so.

Every type this rule compares is declared before the build, so the build refuses the disagreement and
no sealed snapshot carries one.

## How it compares

- A literal has the type of its value: a boolean, an integer, a number, a string, an array or an
  object.
- `$.inputs.<field>` has the type the contract declares for that input.
- `$.results.<step>.<name>` has the type the earlier step's transform declares for the output that
  step maps to `<name>`.
- A declaration of `any`, or a source whose type is not declared, is not compared.
- An integer satisfies `number`.

A stood-down contract is not checked: it is present and not in force, and its successor is.

---

## What this realizes
```yaml
core:
  description: Every input a contract binds to a transform step has the type the transform declares for it
```
