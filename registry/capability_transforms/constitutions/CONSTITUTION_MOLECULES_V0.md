# CONSTITUTION_MOLECULES_V0

## Machine
```yaml
fqdn: capability_transforms::CONSTITUTION_MOLECULES_V0
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
  enforced_by: capability_transforms::INVARIANT_MOLECULE_RUNNABLE_V0
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_MOLECULE_PURITY_CONSISTENT_V0
```

---

## 1. Purpose

This constitution governs the **molecule**: a capability transform composed of other transforms and
run as a stated sequence of steps. A molecule exists so that a computation made of several decisions
is declared as those decisions, each visible in the composition, rather than hidden inside a single
implementation.

It governs molecules only. Deterministic atoms are governed by
`capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0`, and atoms that declare their result
is not determined by their inputs by `capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0`.
Each transform is governed by exactly one of the three, decided by its kind and declared purity.

---

## 2. What a molecule is

- A molecule declares `ct_kind: molecule`, an ordered **atom stream** of steps, and the one value it
  **emits**.
- A step is an **atom**, a **molecule**, or a **loop**.
- A **loop** runs a body — an atom or a molecule — once for each member of a stated collection, and
  carries values from one pass to the next.
- A molecule declares no implementation of its own. Its steps are its specification.

---

## 3. How a molecule runs

- **Declared order.** A molecule's steps run in the order they are declared, and in no other.
- **Every pass runs.** A loop runs its body exactly once per member of its collection, every time. A
  loop whose work is finished carries that fact forward in the values it passes, and the passes that
  remain change nothing. A loop's length never depends on the data it computes.
- **Bounded.** No molecule contains itself, directly or through others. A molecule that did would be
  repetition with no stated bound.
- **Runnable.** Every step and every loop body resolves to a transform the runtime can run.
- **Observable.** Every step a molecule runs leaves one evidence record, naming its results and not
  their values, in the same form as the step of a governed operation.

---

## 4. Purity

A molecule declares its purity, and the declaration is checked against its steps. A molecule declared
deterministic contains only deterministic steps. A molecule containing a step that is not
deterministic declares itself so, and is then subject to what
`capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0` requires of that step's results.

No molecule has side effects, whatever its purity. Side effects are the business of capability side
effects.

---

## 5. Acts stay acyclic

An act — a workflow — is acyclic under `workflow::CONSTITUTION_WORKFLOW_V0`. Repetition belongs in a
molecule's loop, where it is bounded by a collection the composition can see.

---

## What this realizes
```yaml
core:
  description: Governs molecules — composed capability transforms, their steps, loops and purity
rules:
- rule_id: MOLECULE_GOVERNED_HERE
  constraint: a transform declaring ct_kind molecule MUST be governed by this constitution
- rule_id: MOLECULE_DECLARED_ORDER
  constraint: a molecule's steps MUST run in their declared order
- rule_id: MOLECULE_EVERY_PASS
  constraint: a loop MUST run its body exactly once per member of its stated collection
- rule_id: MOLECULE_NO_SELF_CONTAINMENT
  constraint: no molecule MAY contain itself, directly or through others
- rule_id: MOLECULE_RUNNABLE
  constraint: every step and loop body MUST resolve to a transform the runtime can run
- rule_id: MOLECULE_PURITY_CONSISTENT
  constraint: a molecule declared deterministic MUST contain only deterministic steps
- rule_id: MOLECULE_STEP_EVIDENCE
  constraint: every step a molecule runs MUST leave one evidence record naming its results
- rule_id: MOLECULE_NO_SIDE_EFFECTS
  constraint: a molecule MUST NOT produce side effects
```
