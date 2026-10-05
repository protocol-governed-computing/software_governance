# Stage 6 — Governance Intent: platform / routing is a lookup

**Stage:** 6 — Governance Intent

**CR:** routing_lookup

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Both obligations stay with the subdomain that already governs routing.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Govern routing as a lookup | execution_topology | OWNED | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | S5 scope_boundary Govern routing as a lookup |
| Refuse routing nothing performs | execution_topology | OWNED | execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 | S5 scope_boundary Refuse routing nothing performs |
| Replace the licence cap contract | ai_governance | DEFERRED |  | S5 scope_boundary Replace the licence cap contract |
| Replace the Collatz gate contract | workload | DEFERRED |  | S5 scope_boundary Replace the Collatz gate contract |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED | | | |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Governing contracts | execution_topology -> capability_contracts | capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0 | SATISFIED | S4 dependency_graph capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | Present; states two routing answers in one section and three in two others | REPLACE | S4 design_decisions #1 |
| execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 | Present; admits evaluation targets and any routing answer | REPLACE | S4 design_decisions #2 |
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Present and reused unchanged; names the governing rule | REUSE | S4 dependency_graph execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| ROUTING_HAS_TWO_ANSWERS | Every routing answer is continue or exit, in every section of the governing rule. | S4 design_decisions #1 |
| NO_EVALUATION_TARGET | A routing answer other than continue or exit, or an evaluation block, refuses the build and names the step and the answer. | S4 design_decisions #2 |
| ONE_CHECK_PER_VERSION | The new invariant is enforced by a check bound to its identity. | S4 design_decisions #3 |
| NO_UNKNOWN_CONTINUATION | A routing answer execution does not know refuses the run and is recorded. | S4 design_decisions #4 |
| THE_REACH_IS_RE_POINTED | Every artifact naming the governing rule names its successor. | S4 design_decisions #5 |
| BUILT_AFTER_THE_CONTRACTS | This change is built after the licence cap and Collatz gate contracts are replaced. | S4 design_decisions #6 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Govern routing as a lookup | execution_topology | S6 ownership Govern routing as a lookup |
| Refuse routing nothing performs | execution_topology | S6 ownership Refuse routing nothing performs |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
