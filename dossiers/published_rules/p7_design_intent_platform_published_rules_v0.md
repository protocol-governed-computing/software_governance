# Stage 7 — Design Intent: platform / published rules

**Stage:** 7 — Design Intent
**CR:** published_rules
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Read against the pinned baseline
`06dbbb2227ad019c25f3d0b7459159e3290402d322f7259e2cf2f45b3723421f`, and against v5 as
`pgc_release/snapshot` and each repository's `v5` tag hold it.

Nothing is rendered. The governance surface is authored rather than constructed, and the design
language has no family for a constitution or an invariant, so both successors are written by hand and
named here, and both published rules are returned to their v5 text by hand. Nothing is re-pointed by
construction: the only artifact in force that names either rule is unpublished and is edited by hand.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The widened routing rule has its own identity | A change of meaning is a new identity | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1 states that a step routes every outcome it lists and lists every outcome its capability declares (3d CP-13), governed by execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1. The compiler binds today's check to it as `assert_topology_routing_complete_v1`. Written by hand | S4 design_decisions #1 |
| The record rule names its schema | A change of meaning is a new identity | trace::CONSTITUTION_TRACE_EXECUTION_V1 requires every trace line to conform to SCHEMA_TRACE_EVENT_V2, and says SCHEMA_TRACE_EVENT_V1 stays the schema of traces written under it. Written by hand | S4 design_decisions #2 |
| Published text is sealed | Identity is fixed at publication | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 and trace::CONSTITUTION_TRACE_EXECUTION_V0 return to their v5 text and gain only `superseded_by`. `assert_topology_routing_complete_v0` returns to its v5 form and stays registered; a stood-down invariant derives no assertion | S4 design_decisions #3 |
| Nothing in force names the past | Nothing in force names a stood-down rule | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1, unpublished, names execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1. The compiler's scope table, the routing-closure test and the trace check's docstring name the successors | S4 design_decisions #4 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | REVIEW |  | Says more than v5 published. Returned to its v5 text and stood down by hand, because the governance surface is authored. | S6 pps_artifacts_requiring_action #1 |
| trace::CONSTITUTION_TRACE_EXECUTION_V0 | REVIEW |  | Names a schema v5 did not. Returned to its v5 text and stood down by hand. | S6 pps_artifacts_requiring_action #2 |
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1 | REVIEW |  | Unpublished; names the routing rule's successor, edited by hand. | S6 pps_artifacts_requiring_action #3 |

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
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1 | supersedes | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | S4 design_decisions #1 |
| trace::CONSTITUTION_TRACE_EXECUTION_V1 | supersedes | trace::CONSTITUTION_TRACE_EXECUTION_V0 | S4 design_decisions #2 |

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

No act, transform, policy, entrance or generator is touched. The compiler binds a check to the routing rule's successor.

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

The business declared no refusal. Every check enforces what it enforces today.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|

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

