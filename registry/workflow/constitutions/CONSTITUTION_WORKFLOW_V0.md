# CONSTITUTION_WORKFLOW_V0

## Machine
```yaml
fqdn: workflow::CONSTITUTION_WORKFLOW_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: workflow
core:
  enforcement_model: compiler_enforced
  governs:
  - WF
rules:
- applies_to: WF
  enforced_by: workflow::INVARIANT_WF_EXECUTION_PATH_VALID_V0
- applies_to: WF
  enforced_by: workflow::INVARIANT_WF_CC_ONLY_NODES_V0
- applies_to: WF
  enforced_by: workflow::INVARIANT_WF_EXECUTION_PATH_VALID_V0
- applies_to: WF
  enforced_by: workflow::INVARIANT_WF_ENTRY_INTENT_V0
- applies_to: WF
  enforced_by: artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0
- applies_to: WF
  enforced_by: workflow::INVARIANT_WF_ANNOUNCEMENT_DISTINCT_V0
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

## 2a. Announcement

A terminal node **announces** the moments the act completed. An announcement is the account the
business keeps of what happened; it is not how the act did it, and it is not a record a capability
step wrote. The two are different things and the composition has always treated them so — a store
holds what the business now knows, a moment states that something occurred.

**An act may complete several moments at one ending, and it announces each of them.** The singular
was never a statement about acts: twelve announcements exist across nine acts today, and four of them
already announce different moments on different endings. What was singular is the shape one
*transition* carries. A registration that admits a work, its first edition and that edition's first
copy completes three moments in one act, and there is no honest reading under which it announces one
of them.

**The order is declared and it is normative.** Moments are announced in the order the declaration
states, and that order is what a reader of the account sees. It is not an artefact of how the
composition was sealed or of the order a map happened to iterate: an account whose order varies
between runs is an account nobody can compare with another.

**A moment is announced at most once at one transition.** The same moment stated twice at one ending
is either a mistake or two different moments that were not distinguished, and neither is something a
reader can act on.

**A sequence of one is the ordinary case, and it is the case that already runs.** Every act
announcing today announces exactly what it announced before. This clause widens what may be stated;
it changes nothing that was already true.

**An announcement that cannot be made is reported, never dropped.** A moment declared for a
transition and absent when the act reaches it is a defect in what was sealed, and the act says so.
Silence is the failure this clause exists to end: a subdomain faced with announcing one of three
moments announced none, and nothing anywhere noticed.

## 3. Required Fields

- `wf_code`: Unique identifier for the workflow.
- `version`: Version of the workflow artifact.
- `governed_by`: The constitution governing this workflow.
- `core`: Metadata including summary, start node, and node graph.
- `runtime_binding`: FQDN reference to the RB artifact providing CS bindings.

---

## How it is checked
- Workflow node graph MUST be acyclic.
- All node references MUST resolve to declared CC artifacts via FQDN.
- All result status transitions from each node MUST be explicitly declared.
- A terminal node's announcement MUST be an ordered sequence of declared moments; a single moment is
  a sequence of one.
- No moment MAY appear twice in the announcement of one transition.

---

## End of Constitution

---

## What this realizes
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
- rule_id: WF_ANNOUNCEMENT_DISTINCT
  constraint: a terminal node announces each moment at most once, by FQDN, in a declared order
```
