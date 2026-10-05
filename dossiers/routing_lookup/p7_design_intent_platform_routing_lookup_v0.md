# Stage 7 — Design Intent: platform / routing is a lookup

**Stage:** 7 — Design Intent
**CR:** routing_lookup
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Read against the pinned baseline
`d880845e3b189f2589aa29bb2b53db291ff897ff0705a52f99c687bd26cf2b51`.

Nothing is rendered. The governance surface is authored rather than constructed, and the design
language has no family for a constitution or an invariant, so the new versions of the governing rule
and of the invariant are written by hand and named here. They stand the old versions down by hand.
Construction re-points the twenty artifacts that name the governing rule. The build check and the run-time
refusal are platform code, governed by the obligations they carry out.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Routing has two answers, in every section | Routing is a lookup | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1 restates its §1 and §3 so that every outcome is routed to continue or exit, and a contract's exits are the outcomes its steps exit on and the outcomes its last step continues with. Its §4 is unchanged. It names execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1 in place of execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0. Written by hand | S4 design_decisions #1 |
| Building refuses routing nothing performs | A decision is a capability's | execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1 counts exits only from exit and the last step's continue, refuses a routing answer other than continue or exit by contract, step and answer, and refuses a contract declaring an evaluation block. Written by hand | S4 design_decisions #2 |
| One check per version | A check is bound to its invariant by identity | The compiler gains the check for execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1, registered under its identity. The check for execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 stays with the stood-down invariant, which derives no assertion | S4 design_decisions #3 |
| Execution refuses an unknown answer | A continuation not declared is refused, never assumed | The runtime's step loop refuses a routing answer other than continue or exit, records the refusal and ends the run refused, as it does for an unlisted outcome | S4 design_decisions #4 |
| The reach is re-pointed | The replacement accounts for its whole reach | Every artifact that names execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 is re-pointed to execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1; each names it in a declared reference part and keeps its identity | S4 design_decisions #5 |
| Built after the contracts | No composition is refused by this change | Construction runs after ai_governance and the conformance workload replace the licence cap and Collatz gate contracts | S4 design_decisions #6 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | REVIEW |  | States three routing answers in two sections and two in a third. Its new version is written by hand and it is stood down by hand, because the governance surface is authored. | S6 pps_artifacts_requiring_action #1 |
| execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 | REVIEW |  | Admits evaluation targets and any routing answer. Its new version is written by hand and it is stood down by hand, because the governance surface is authored. | S6 pps_artifacts_requiring_action #2 |
| capability_contracts::INVARIANT_TOPOLOGY_CAPABILITY_REFERENCE_UNIQUE_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| capability_contracts::INVARIANT_TOPOLOGY_INPUT_REFERENCE_DECLARED_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| execution_topology::INVARIANT_NO_RUNTIME_TOPOLOGY_SYNTHESIS_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| execution_topology::INVARIANT_TOPOLOGY_AUTHORITY_ORTHOGONAL_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| execution_topology::INVARIANT_TOPOLOGY_IMMUTABLE_AFTER_COMPILATION_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S6 pps_artifacts_requiring_action #3 |
| execution_topology::INVARIANT_TOPOLOGY_STEP_DECLARED_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| execution_topology::INVARIANT_TOPOLOGY_STEP_ID_UNIQUE_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| execution_topology::INVARIANT_TOPOLOGY_SURFACE_CANONICAL_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| execution_topology::INVARIANT_TOPOLOGY_TRANSPORT_ORTHOGONAL_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_CT_PURE_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_REGISTRY_COUNT_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_REGISTRY_DEREGISTER_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_REGISTRY_REGISTER_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_REGISTRY_RESOLVE_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_STORAGE_APPENDONLY_APPEND_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_STORAGE_READ_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| surface_contract::SURFACE_CONTRACT_STORAGE_WRITE_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| workflow::INVARIANT_WF_NODE_KEY_BINDING_UNIQUE_V0 | REPOINT |  | Its obligation is unchanged; re-pointed to the governing rule's new version. | S4 design_decisions #5 |
| capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0 | REUSE |  | Governs the new version of the governing rule, unchanged. | S6 cross_subdomain_deps #1 |

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
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1 | supersedes | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | S4 design_decisions #1 |
| execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1 | supersedes | execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 | S4 design_decisions #2 |

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

No act, transform, policy, entrance or generator is touched. The compiler's check and the runtime's step loop change, and are named in the refusal deferrals below.

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

The business declared three refusals. The design language has no register for a compiler check or a runtime refusal, so each is deferred to what this change arms.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|
| Building a composition | A step routes to anything but going on or ending | The compiler's check for execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1 | Armed by this change, built after the two contracts are replaced, so arming it fails no build. | S0 operation_refusals #1 |
| Building a composition | A contract declares an evaluation target | The compiler's check for execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1 | Armed by this change, with the refusal above. | S0 operation_refusals #2 |
| Running a contract | A step's routing answer is neither going on nor ending | The runtime's step loop | Armed by this change. | S0 operation_refusals #3 |

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

