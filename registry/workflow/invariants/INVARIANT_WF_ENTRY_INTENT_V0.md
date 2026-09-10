# INVARIANT_WF_ENTRY_INTENT_V0

## Machine

```yaml
fqdn: workflow::INVARIANT_WF_ENTRY_INTENT_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: workflow
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - WF
```

---

## Purpose

Enforce that every workflow has a single, unambiguous admission gate.

---

## How it is checked
### Rule: Exactly One IN Node

Count all nodes with type IN. The count must be exactly 1.

**Violation (zero)**:
```yaml
nodes:
  CC_STEP_V0:
    type: CC
    # No IN node — admission bypassed
```

**Violation (multiple)**:
```yaml
nodes:
  IN_GATE_A_V0:
    type: IN
  IN_GATE_B_V0:     # WRONG — two IN nodes
    type: IN
```

---

## Scope

**Applies to**: All WF artifacts

**Does NOT validate**: Schema of the IN artifact (see INVARIANT_IN_SCHEMA_REQUIRED_V0)

---

## What this realizes
```yaml
core:
  description: 'Every workflow must declare exactly one IN node as its entry intent. The start_node must
    reference that IN node. Zero or multiple IN nodes are constitutional violations.

    '
  anti_patterns:
  - missing_entry_intent: Workflow has no IN node — no admission gate
  - multiple_entry_intents: Workflow has more than one IN node — ambiguous admission
  - start_node_not_in: start_node does not reference the IN node
  clarification:
    single_entry: 'Exactly one IN node is required. This is the sole admission gate for the workflow.
      Multiple INs would create ambiguous entry semantics; zero would bypass admission.

      '
    start_node_alignment: The start_node field must reference the single IN node. This invariant complements
      INVARIANT_WF_EXECUTION_PATH_VALID_V0 which validates start_node existence and type — this invariant
      adds the uniqueness constraint.
```
