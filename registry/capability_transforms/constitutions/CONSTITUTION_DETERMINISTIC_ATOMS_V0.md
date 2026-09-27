# CONSTITUTION_DETERMINISTIC_ATOMS_V0

## Machine
```yaml
fqdn: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
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
  enforced_by: capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0
- applies_to: CT
  enforced_by: execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_CT_SURFACE_CLOSED_V1
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_CT_SURFACE_DERIVED_CLOSED_V1
```

---

## 1. Purpose

This constitution governs the **deterministic atom**: a Capability Transform (CT) that names one
implementation and whose result is determined by its inputs. Deterministic atoms are the primary
mechanism for logic in the system.

It governs such atoms only. Each transform is governed by exactly one of three constitutions,
decided by its kind and declared purity (`capability_transforms::INVARIANT_CT_GOVERNED_BY_KIND_V0`):

| Transform | Constitution |
|---|---|
| an atom whose result is determined by its inputs | this one |
| an atom declaring `ct_purity: ct_impure` | `capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0` |
| a molecule, composed of steps and naming no implementation | `capability_transforms::CONSTITUTION_MOLECULES_V0` |

**It also carries rules common to every transform.** They are surface closure
(`INVARIANT_CT_SURFACE_CLOSED_V1`), closure by derivation (`INVARIANT_CT_SURFACE_DERIVED_CLOSED_V1`)
and implementation admissibility (`INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0`). They concern molecules
and non-deterministic atoms as much as the atoms named here. They sit here because this constitution
predates its two siblings, from a time when every transform was a deterministic atom. They stay here
unchanged; a home common to all three is a separate change.

---

## 2. Core Principles

- **Purity:** A deterministic atom MUST be a pure function.
- **Determinism:** Given the same input, a deterministic atom MUST always produce the same output.
- **Side-Effect Free:** No transform, of any kind, has side effects. Side effects are delegated to Capability Side Effects (CS).
- **Explicit Inputs/Outputs:** All data required by a transform must be passed as explicit inputs. All results must be returned as explicit outputs.

---

## 3. Required Fields

- `artifact_code`: Unique identifier for the transform.
- `version`: Version of the transform.
- `governed_by`: `capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0`.
- `core`: Metadata and description.
- `inputs`: Definition of input parameters.
- `outputs`: Definition of output parameters.
- `logic`: Reference to the implementation.

---

## How it is checked
- CT implementations must be discoverable.
- Input and output types must match the capability contract.
- Implementation must adhere to the purity principle.

---

## What this realizes
```yaml
core:
  description: Governs deterministic atoms — purity, determinism, and explicit IO — and carries surface rules common to every transform
rules:
- rule_id: CT_PURITY
  constraint: a deterministic atom MUST be a pure function; same inputs MUST always produce same outputs
- rule_id: CT_NO_SIDE_EFFECTS
  constraint: CT MUST NOT produce side effects; side effects belong in CS
- rule_id: CT_IMPLEMENTATION_DECLARED
  constraint: atom CT MUST declare machine.implementation with non-empty module and callable
- rule_id: CT_EXPLICIT_IO
  constraint: all CT inputs and outputs MUST be explicitly declared
```
