# CONSTITUTION_NONDETERMINISTIC_ATOMS_V0

## Machine
```yaml
fqdn: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: capability_transforms
core:
  enforcement_model: compiler_enforced
  governs:
  - CT
rules:
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_CT_GOVERNED_BY_KIND_V0
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_NONDETERMINISM_NOT_ROUTED_V0
```

---

## 1. Purpose

This constitution governs the **non-deterministic atom**: an atom that declares its result is not
determined by its inputs. A language model offering the words it might write next is one.

It governs such atoms only. Deterministic atoms are governed by
`capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0`, whose statement that every transform
is pure describes the transforms it governs; molecules are governed by
`capability_transforms::CONSTITUTION_MOLECULES_V0`. Each transform is governed by exactly one of the
three, decided by its kind and declared purity.

---

## 2. What a non-deterministic atom is

- An atom declaring `ct_purity: ct_impure`: given the same inputs, it may produce a different result.
- It declares its implementation, like every atom.
- It has **no side effects**. Its result is its only product; a change outside it is the business of a
  capability side effect.

---

## 3. Determinism relative to recorded outcomes

The platform's determination is deterministic: the same governed state, proposal and closure
determine the same result, and replaying a sealed composition reproduces it. A step whose result
varies would break both unless what it produced is kept. So:

- **Recorded when produced.** Every result a non-deterministic atom produces is recorded as
  determining evidence, values included, at the moment it is produced.
- **Replay substitutes.** A replay uses the recorded result in place of the atom, and never runs a
  non-deterministic atom.
- **Determinism holds** for the governed state, the proposal, the closure and the recorded outcomes
  together. The variation is observed once, recorded, and an input thereafter.

The platform already admits a value of this kind: the clock, which answers differently every time and
is recorded where it is used.

---

## 4. Offered, never decided

A non-deterministic atom's results are consumed by a deterministic step before anything routes on
them. A capability contract does not invoke a non-deterministic atom as a step of its own, and a
molecule's emission does not come from one. Otherwise governance would reduce to recording what the
atom said.

---

## What this realizes
```yaml
core:
  description: Governs atoms that declare their result is not determined by their inputs
rules:
- rule_id: NONDETERMINISTIC_ATOM_GOVERNED_HERE
  constraint: an atom declaring ct_purity ct_impure MUST be governed by this constitution
- rule_id: NONDETERMINISTIC_ATOM_NO_SIDE_EFFECTS
  constraint: a non-deterministic atom MUST NOT produce side effects
- rule_id: NONDETERMINISTIC_RESULT_RECORDED
  constraint: every result a non-deterministic atom produces MUST be recorded when produced
- rule_id: NONDETERMINISTIC_REPLAY_SUBSTITUTES
  constraint: a replay MUST use the recorded result and MUST NOT run a non-deterministic atom
- rule_id: NONDETERMINISTIC_OFFERED_NEVER_DECIDED
  constraint: nothing MAY route on a non-deterministic atom's result before a deterministic step consumes it
```
