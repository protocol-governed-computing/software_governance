# CONSTITUTION_WORKFLOW_V0

## Machine
```yaml
fqdn: fb.workflow::CONSTITUTION_WORKFLOW_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: fb.governance::CONSTITUTION_GOVERNANCE_V0
core:
  enforcement_model: compiler_enforced
  governs:
  - WF
rules:
- applies_to: WF
  enforced_by: fb.workflow::INVARIANT_WF_EXECUTION_PATH_VALID_V0
- applies_to: WF
  enforced_by: fb.workflow::INVARIANT_WF_CC_ONLY_NODES_V0
- applies_to: WF
  enforced_by: fb.workflow::INVARIANT_WF_EXECUTION_PATH_VALID_V0
- applies_to: WF
  enforced_by: fb.workflow::INVARIANT_WF_ENTRY_INTENT_V0
- applies_to: WF
  enforced_by: fb.artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0
```

---

## 1. Purpose

This constitution defines the governance and enforcement rules for Workflow (WF) artifacts.

Workflows declare directed acyclic graphs of capability contract invocations. They define the sequencing and routing of execution within a protocol — not the logic itself.

---

## 2. Core Principles

- **DAG Structure:** Workflows MUST form valid directed acyclic graphs. Cycles are constitutional violations.
- **CC-Only Nodes:** Workflow steps invoke capability contracts. CT and CS artifacts are never referenced directly from a workflow.
- **Explicit Transitions:** All routing between nodes MUST be declared. No implicit defaults, no fallthrough.
- **Entry Intent:** Every workflow requires exactly one declared entry intent that gates admission.
- **FQDN References:** All artifact references within a workflow MUST use fully-qualified names.

---

## 3. Required Fields

- `wf_code`: Unique identifier for the workflow.
- `version`: Version of the workflow artifact.
- `governed_by`: The constitution governing this workflow.
- `core`: Metadata including summary, start node, and node graph.
- `runtime_binding`: FQDN reference to the RB artifact providing CS bindings.

---

## 4. Validation Rules

- Workflow node graph MUST be acyclic.
- All node references MUST resolve to declared CC artifacts via FQDN.
- All result status transitions from each node MUST be explicitly declared.

---

## End of Constitution

---

## Rule Statement

```yaml
core:
  description: Governs workflow DAG structure and execution sequencing
rules:
- rule_id: WF_DAG_STRUCTURE
  constraint: workflow steps MUST form a valid directed acyclic graph
- rule_id: WF_CC_ONLY_NODES
  constraint: workflow steps MUST reference CC artifacts only; no direct CT or CS invocation
- rule_id: WF_NO_IMPLICIT_FLOW
  constraint: all transitions MUST be explicitly declared; no implicit default routing
- rule_id: WF_ENTRY_INTENT_REQUIRED
  constraint: every workflow MUST declare exactly one entry intent
- rule_id: WF_FQDN_REFERENCES
  constraint: all artifact references in workflow MUST use FQDN
```
