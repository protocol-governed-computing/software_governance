# Stage 6 — Governance Intent: platform / published rules

**Stage:** 6 — Governance Intent

**CR:** published_rules

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Each rule stays with the subdomain that already governs it.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| State the routing rule | execution_topology | OWNED | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | S5 scope_boundary State the routing rule |
| State the record rule | trace | OWNED | trace::CONSTITUTION_TRACE_EXECUTION_V0 | S5 scope_boundary State the record rule |
| Return routes changed in place in contracts and workflows | execution_topology | DEFERRED |  | S5 scope_boundary Return routes changed in place in contracts and workflows |

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
| NONE IDENTIFIED | | | | |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Present; says more than v5 published | REVIEW | S4 design_decisions #1 |
| trace::CONSTITUTION_TRACE_EXECUTION_V0 | Present; names a schema v5 did not | REVIEW | S4 design_decisions #2 |
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1 | Present, unpublished; names the routing rule's published identity | REVIEW | S4 design_decisions #4 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| THE_WIDENED_RULE_HAS_ITS_OWN_IDENTITY | The routing rule's successor states CP-13, and today's check is bound to it. | S4 design_decisions #1 |
| THE_RECORD_RULE_NAMES_ITS_SCHEMA | The record rule's successor names SCHEMA_TRACE_EVENT_V2. | S4 design_decisions #2 |
| PUBLISHED_TEXT_IS_SEALED | Each published rule returns to its v5 text, gaining only its stand-down. | S4 design_decisions #3 |
| NOTHING_IN_FORCE_NAMES_THE_PAST | What is in force names each successor. | S4 design_decisions #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| State the routing rule | execution_topology | S6 ownership State the routing rule |
| State the record rule | trace | S6 ownership State the record rule |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
