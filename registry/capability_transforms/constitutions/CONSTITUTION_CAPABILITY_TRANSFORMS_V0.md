# CONSTITUTION_CAPABILITY_TRANSFORMS_V0

## Machine
```yaml
fqdn: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
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
```

---

## 1. Purpose

This constitution defines the governance and enforcement rules for Capability Transforms (CT).

Capability Transforms are pure functions that transform data within the protocol. They are the primary mechanism for logic in the system.

---

## 2. Core Principles

- **Purity:** All CTs MUST be pure functions.
- **Determinism:** Given the same input, a CT MUST always produce the same output.
- **Side-Effect Free:** CTs MUST NOT have side effects. Side effects are delegated to Capability Side Effects (CS).
- **Explicit Inputs/Outputs:** All data required by a CT must be passed as explicit inputs. All results must be returned as explicit outputs.

---

## 3. Required Fields

- `artifact_code`: Unique identifier for the transform.
- `version`: Version of the transform.
- `governed_by`: The constitution governing this transform.
- `core`: Metadata and description.
- `inputs`: Definition of input parameters.
- `outputs`: Definition of output parameters.
- `logic`: Reference to the implementation.

---

## 4. Validation Rules

- CT implementations must be discoverable.
- Input and output types must match the capability contract.
- Implementation must adhere to the purity principle.

---

## Rule Statement

```yaml
core:
  description: Governs Capability Transform (CT) artifacts — purity, determinism, and explicit IO
rules:
- rule_id: CT_PURITY
  constraint: CT MUST be a pure function; same inputs MUST always produce same outputs
- rule_id: CT_NO_SIDE_EFFECTS
  constraint: CT MUST NOT produce side effects; side effects belong in CS
- rule_id: CT_IMPLEMENTATION_DECLARED
  constraint: atom CT MUST declare machine.implementation with non-empty module and callable
- rule_id: CT_EXPLICIT_IO
  constraint: all CT inputs and outputs MUST be explicitly declared
```
