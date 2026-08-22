# CONSTITUTION_CAPABILITY_CONTRACT_V0

## Machine
```yaml
fqdn: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: capability_contracts
core:
  enforcement_model: compiler_enforced
  governs:
  - CC
rules:
- applies_to: CC
  enforced_by: capability_contracts::INVARIANT_CC_INPUTS_SATISFIED_V0
- applies_to: CC
  enforced_by: capability_contracts::INVARIANT_CC_CAPABILITY_BINDING_VALID_V0
- applies_to: CC
  enforced_by: capability_contracts::INVARIANT_CC_NO_IMPLICIT_CHAINING_V0
- applies_to: CC
  enforced_by: capability_contracts::INVARIANT_CC_NO_MISSING_DEPENDENCIES_V0
- applies_to: CC
  enforced_by: capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0
- applies_to: CC
  enforced_by: artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0
```

---

## 1. Purpose

This constitution defines the governance and enforcement rules for Capability Contract (CC) artifacts.

Capability Contracts bind pure Capability Transforms (CTs) and authorized Capability Side Effects (CSs) into governed executable units. They are the execution nodes within a workflow — declarative, deterministic, and auditable.

---

## 2. Core Principles

- **Input Completeness:** All inputs required by a CC MUST be satisfied by declared bindings before execution begins. Unsatisfied inputs are constitutional violations.
- **Valid Capability Bindings:** Every capability referenced in a CC MUST resolve to a declared CT or CS artifact. Unresolved references fail the build.
- **No Implicit Chaining:** All dataflow between capabilities MUST be explicitly declared. Implicit chaining or ambient state is forbidden.
- **No Missing Dependencies:** A CC MUST NOT reference inputs or capabilities not declared in scope.
- **No Unused Outputs:** All declared outputs MUST be consumed or emitted. Dead outputs are governance noise.
- **FQDN References:** All artifact references within a CC MUST use fully-qualified names.

---

## 3. Required Fields

- `cc_code`: Unique identifier for the capability contract.
- `version`: Version of the capability contract artifact.
- `governed_by`: The constitution governing this capability contract.
- `core`: Metadata including summary, inputs, outputs, result_status_contract, and pipeline.

**Schema**: `SCHEMA_CAPABILITY_CONTRACT_V0.json` — canonical JSON Schema for CC artifact structure.
**Pipeline step schema**: `SCHEMA_CC_PIPELINE_STEP_V0.json` — canonical JSON Schema for a single execution topology step.

---

## 4. Validation Rules

- All input fields declared in `core.inputs` MUST be bound before execution.
- All capability references in `core.pipeline` MUST resolve to declared CT or CS artifacts.
- No output declared in `core.outputs` may remain unconsumed across the pipeline.

---

## End of Constitution

---

## Rule Statement

```yaml
core:
  description: Governs Capability Contract (CC) artifacts — explicit binding, determinism, and governed
    denial
rules:
- rule_id: CC_INPUTS_SATISFIED
  constraint: all CC inputs MUST be satisfied by declared bindings before execution
- rule_id: CC_CAPABILITY_BINDING_VALID
  constraint: every capability reference in CC MUST resolve to a declared CT or CS artifact
- rule_id: CC_NO_IMPLICIT_CHAINING
  constraint: CC MUST NOT implicitly chain capabilities; all dataflow MUST be explicitly declared
- rule_id: CC_NO_MISSING_DEPENDENCIES
  constraint: CC MUST NOT reference undeclared inputs or capabilities
- rule_id: CC_NO_UNUSED_OUTPUTS
  constraint: CC MUST NOT declare outputs that are never consumed or emitted
- rule_id: CC_FQDN_REFERENCES
  constraint: all artifact references in CC MUST use FQDN
```
