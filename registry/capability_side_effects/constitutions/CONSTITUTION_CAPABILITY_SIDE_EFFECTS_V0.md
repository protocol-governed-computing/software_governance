# CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0

## Machine
```yaml
fqdn: capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: capability_side_effects
core:
  enforcement_model: compiler_enforced
  governs:
  - CS
rules:
- applies_to: CS
  enforced_by: capability_side_effects::INVARIANT_CS_SURFACE_CLOSED_V1
- applies_to: CS
  enforced_by: execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0
- applies_to: CS
  enforced_by: capability_side_effects::INVARIANT_CS_TRACEABLE_V0
- applies_to: CS
  enforced_by: capability_side_effects::INVARIANT_CS_ISOLATED_EXECUTION_V0
- applies_to: CS
  enforced_by: capability_side_effects::INVARIANT_INSPECTION_CAPABILITY_READ_ONLY_V0
```

---

## 1. Purpose

This constitution defines the governance and enforcement rules for Capability Side Effects (CS).

Capability Side Effects are the mechanism for interacting with the outside world, such as databases, external APIs, and filesystem.

---

## 2. Core Principles

- **Explicit Declaration:** All side effects must be explicitly declared in the protocol.
- **Isolated Execution:** Side effects must be executed through dedicated executors.
- **Traceability:** Every execution of a side effect must be recorded in the trace.
- **Limited Mutability:** Side effects should be restricted to the necessary scope of mutability.

---

## 3. Required Fields

- `cs_code`: Unique identifier for the side effect.
- `version`: Version of the side effect.
- `governed_by`: The constitution governing this side effect.
- `core`: Metadata and description.
- `inputs`: Definition of input parameters.
- `outputs`: Definition of output parameters (e.g., success status, return data).
- `logic`: Reference to the implementation executor.

---

## How it is checked
- Side effect implementations must be discoverable.
- Input and output types must match the capability contract.
- Side effects must be restricted to authorized layers.

---

## What this realizes
```yaml
core:
  description: Governs Capability Side Effect (CS) artifacts — explicit declaration, traceability, and
    isolation
rules:
- rule_id: CS_EXPLICIT_DECLARATION
  constraint: all side effects MUST be explicitly declared in protocol; no implicit side effects
- rule_id: CS_IMPLEMENTATION_DECLARED
  constraint: CS MUST declare implementation with non-empty module and callable
- rule_id: CS_TRACEABLE
  constraint: every CS execution MUST be recorded in the execution trace
- rule_id: CS_ISOLATED_EXECUTION
  constraint: CS MUST execute through dedicated executors only; not inline in CT or CC
```
