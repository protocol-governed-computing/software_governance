# Stage 6 — Governance Intent: platform / routing closure

**Stage:** 6 — Governance Intent

**CR:** routing_closure

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Each obligation stays with the subdomain that already governs its subject.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Refuse a narrowed step | execution_topology | OWNED | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | S5 scope_boundary Refuse a narrowed step |
| Refuse an unrouted reachable place | workflow | OWNED |  | S5 scope_boundary Refuse an unrouted reachable place |
| Refuse an unanswered step outcome | execution_topology | OWNED |  | S5 scope_boundary Refuse an unanswered step outcome |
| Record each step's decision | trace | OWNED | trace::CONSTITUTION_TRACE_EXECUTION_V0 | S5 scope_boundary Record each step's decision |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| An append-only record of each run | Each step line carries its outcome and what happened next | trace | S5 business_objects Run record |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Knowing which workflows are reachable | workflow -> artifact | artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 | SATISFIED | S4 dependency_graph artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Present; compares a step only with what its author listed | REVIEW | S4 dependency_graph execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 |
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | Present; its routing rule states the author's list only | REVIEW | S4 dependency_graph execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 |
| workflow::CONSTITUTION_WORKFLOW_V0 | Present; names no obligation closing a place against its contract | REVIEW | S4 dependency_graph workflow::CONSTITUTION_WORKFLOW_V0 |
| trace::CONSTITUTION_TRACE_EXECUTION_V0 | Present; governs a step entry carrying no outcome | REVIEW | S4 dependency_graph trace::CONSTITUTION_TRACE_EXECUTION_V0 |
| artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 | Present and reused unchanged | REUSE | S4 dependency_graph artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_STEP_ANSWERS_ITS_CAPABILITY | A step's listed outcomes hold every outcome its capability declares. | S4 design_decisions #1 |
| A_REACHABLE_PLACE_ANSWERS_WHAT_IT_RUNS | A workflow place execution can reach routes every outcome of its contract or entrance. | S4 design_decisions #2 |
| NO_DEFAULT_CONTINUATION | A step outcome with no continuation refuses the request. | S4 design_decisions #3 |
| THE_RECORD_CARRIES_THE_DECISION | A step entry carries its outcome and its continuation. | S4 design_decisions #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Refuse a narrowed step | execution_topology | S6 ownership Refuse a narrowed step |
| Refuse an unrouted reachable place | workflow | S6 ownership Refuse an unrouted reachable place |
| Refuse an unanswered step outcome | execution_topology | S6 ownership Refuse an unanswered step outcome |
| Record each step's decision | trace | S6 ownership Record each step's decision |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
