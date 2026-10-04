# Stage 7 — Design Intent: platform / routing closure

**Stage:** 7 — Design Intent
**CR:** routing_closure
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Read against the pinned baseline
`f8356d9c8938aea16ab7850d7bda964d8d16c42c64e5db9056d5fe58040ec1d0`, the composition published as
v5, whose governance surface this change amends.

Nothing is rendered. The governance surface is authored rather than constructed, so the obligation
and the three constitutions this change amends are cited here as REVIEW and written by hand, and so
is the one obligation it adds. The build check, the run-time refusal and the run's record are
platform code, governed by the obligations they carry out.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| A step answers every outcome its capability declares | A missing answer is never a default | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 compares each step's listed outcomes with what the capability declares: a side effect's operation lists them, and a transform declares success, and refusal unless it never refuses. In a domain build they are read from the platform surface the domain is built against | S4 design_decisions #1 |
| A reachable workflow place answers what it runs | A refusal at build time comes first | A new obligation, workflow::INVARIANT_WF_ROUTING_CLOSED_V0, named by workflow::CONSTITUTION_WORKFLOW_V0, refuses a place reachable from the start whose routes miss an outcome its contract or entrance declares. A workflow artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 keeps out of force is not reachable and is not checked. Written by hand, because the governance surface is authored | S4 design_decisions #2 |
| Execution refuses an unanswered step outcome | Execution never carries on past an outcome nothing answers | The runtime looks up a step's continuation with no default. Where there is none it records the refusal, ends the run refused and runs nothing after the step | S4 design_decisions #3 |
| The step record carries the decision | Every step decision is in the record | trace::CONSTITUTION_TRACE_EXECUTION_V0 governs the run's record; its step entry now requires the outcome and the continuation. An admission names the route as its continuation | S4 design_decisions #4 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | REVIEW | Requires every step to route every outcome it declares | Gains the requirement that a step's listed outcomes hold every outcome its capability declares. The governance surface is authored rather than rendered, so this amendment is written by hand and cited here, not scheduled for construction. | S6 pps_artifacts_requiring_action #1 |
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | REVIEW | Governs how a contract is built from steps | Its routing rule is restated to name the capability's declared outcomes. Written by hand. | S6 pps_artifacts_requiring_action #2 |
| workflow::CONSTITUTION_WORKFLOW_V0 | REVIEW | Governs what every workflow is held to | Names the new obligation that a reachable place answers what it runs. Written by hand, with the obligation. | S6 pps_artifacts_requiring_action #3 |
| trace::CONSTITUTION_TRACE_EXECUTION_V0 | REVIEW | Governs the run's record | The schema it governs, SCHEMA_TRACE_EVENT_V1, is restated by hand: its step entry requires the outcome and the continuation. The constitution's own text is unchanged, because it names the schema as the declaration and restates no field. | S6 pps_artifacts_requiring_action #4 |
| artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 | REUSE |  | Says which workflows are in force, and so which can be reached. Unchanged. | S6 pps_artifacts_requiring_action #5 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|

---

## 9. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|

---

## 10. Structure Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|------|------|------|----------------|

---

## 11. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NONE IDENTIFIED |

---

## 12. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 13. Unchanged Registers

No artifact is rendered, so no act, transform, vocabulary, policy, entrance or generator is touched.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|---|---|---|---|---|---|---|

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---|---|---|---|---|

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|---|---|---|---|

---

## 14. Refusal Discharge

No refusal is discharged at a step of an act: each is carried by an obligation or by execution
itself, which this change writes. The design pipeline cannot cite a rule its own change adds, so
each is recorded as handed to the obligation that carries it.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|
| Building a composition | A step answers fewer outcomes than its capability declares | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0, amended by hand in this change | Armed by this change. The three domains closed every narrowed step in their own changes first, so arming it fails no build. | S0 operation_refusals #1 |
| Building a composition | A reachable workflow place leaves an outcome of its contract without a route | workflow::INVARIANT_WF_ROUTING_CLOSED_V0, written by hand in this change | Armed by this change, after the domains closed every reachable gap. | S0 operation_refusals #2 |
| Running a request | A step ends with an outcome nothing answers | The runtime's step loop, governed by execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | Armed by this change; the step check makes it a safeguard, reached only by what the build did not see. | S0 operation_refusals #3 |

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|---|---|---|---|---|

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn.

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---|---|---|---|---|---|

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---|---|---|---|

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---|---|---|---|---|---|

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|---|---|---|---|

