# CONSTITUTION_CAPABILITY_TRANSFORMS_V2

## Machine
```yaml
fqdn: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V2
supersedes: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V1
artifact_kind: CONSTITUTION
version: V2
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: capability_transforms
core:
  enforcement_model: compiler_enforced
  governs:
  - CT
rules:
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_CT_SURFACE_CLOSED_V2
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_CT_SURFACE_DERIVED_CLOSED_V1
- applies_to: CT
  enforced_by: execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_CT_INPUT_TYPED_V0
```

---

## 1. Purpose

This constitution carries the rules common to every capability transform, whatever its kind and
purity. A deterministic atom, a non-deterministic atom and a molecule are all bound by them.

No transform names this constitution as `governed_by`. Each transform is governed by exactly one of
three constitutions, decided by its kind and declared purity
(`capability_transforms::INVARIANT_CT_GOVERNED_BY_KIND_V0`):

| Transform | Constitution |
|---|---|
| an atom whose result is determined by its inputs | `capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0` |
| an atom declaring `ct_purity: ct_impure` | `capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0` |
| a molecule, composed of steps and naming no implementation | `capability_transforms::CONSTITUTION_MOLECULES_V0` |

Those three say what each kind of transform is. This one says what every transform owes the
composition it belongs to.

---

## 2. The rules

- **Surface closure** (`INVARIANT_CT_SURFACE_CLOSED_V2`). The platform's transform surface is an
  enumerated set: every executable transform is declared, every declared transform has a runtime
  implementation, and no undeclared transform executes.
- **Closure by derivation** (`INVARIANT_CT_SURFACE_DERIVED_CLOSED_V1`). A domain's surface is closed
  by derivation rather than by a list: every transform it declares is invoked by one of its
  contracts, and every transform its contracts invoke is declared where it can be resolved.
- **Implementation admissibility** (`INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0`). An atom, deterministic
  or not, declares its implementation with a non-empty module and callable. A molecule names none;
  what it runs is its steps, and each of those is held to the same rule.
- **Typed inputs** (`INVARIANT_CT_INPUT_TYPED_V0`). A transform is given only values of the types it
  declares. Each input a contract binds to a transform step has the declared type.

---

## Change from V0

`CONSTITUTION_CAPABILITY_TRANSFORMS_V0` governed every transform, from a time when every transform
was a deterministic atom. When non-deterministic atoms and molecules gained constitutions of their
own, it was renamed `CONSTITUTION_DETERMINISTIC_ATOMS_V0`, and it kept these three rules although
they concern all three kinds. This version takes the name back for what the name describes: the
rules common to every transform, and nothing else. The deterministic atom's own rules stay with
`CONSTITUTION_DETERMINISTIC_ATOMS_V0`.

---

## Change from V1

V2 closes the platform's surface with `INVARIANT_CT_SURFACE_CLOSED_V2`, whose list adds
`CT_PURE_REQUIRE_TRUE_V0`, and adds the rule that a transform is given only values of the types it
declares.

---

## What this realizes
```yaml
core:
  description: Carries the rules common to every capability transform — surface closure, closure by derivation, implementation admissibility and typed inputs
rules:
- rule_id: CT_SURFACE_CLOSED
  constraint: every executable transform MUST be declared and implemented, and no undeclared transform MAY execute
- rule_id: CT_SURFACE_DERIVED_CLOSED
  constraint: every transform a domain declares MUST be invoked by its contracts, and every transform they invoke MUST be declared
- rule_id: CT_IMPLEMENTATION_ADMISSIBLE
  constraint: every atom MUST declare an implementation with a non-empty module and callable
- rule_id: CT_INPUT_TYPED
  constraint: every input a contract binds to a transform step MUST have the type the transform declares
```
