# Stage 5 — Business Intent: platform / routing is a lookup

**Stage:** 5 — Business Intent

**CR:** routing_lookup

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The execution topology subdomain governs how a contract is built from steps: that each step
dispatches one capability, answers the outcomes it can produce, and says for each what happens next.
Its authority is to decide what makes a contract's steps sound. It decides nothing about what any
particular contract does.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| execution_topology | Holds every routing answer to going on or ending, at build time and at run time, so a decision is always a capability's. | S4 actors Execution topology |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Govern routing as a lookup | IN_SCOPE | A new version of the governing rule. | S4 authoring_scope GAP-01 |
| Refuse routing nothing performs | IN_SCOPE | A new version of the invariant, and execution refuses. | S4 authoring_scope GAP-02 |
| Replace the licence cap contract | DEFERRED | Its own change, in ai_governance. | S4 authoring_scope Replace the licence cap contract |
| Replace the Collatz gate contract | DEFERRED | Its own change, in the conformance workload. | S4 authoring_scope Replace the Collatz gate contract |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Every routing answer is going on or ending. | Routing is a lookup; a decision is a capability's. | S1 business_invariants #1 |
| Every outcome a contract declares is reached by a step's outcome routed to ending. | A contract's outcomes come from its steps, never from a condition. | S1 business_invariants #2 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Govern | Routing as a lookup | A contract is built | IN_SCOPE | S4 capability_graph Govern routing as a lookup |
| Refuse | Routing nothing performs | A composition is built, or a contract runs | IN_SCOPE | S4 capability_graph Refuse routing nothing performs |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|-----------|------|----------------|
| NONE IDENTIFIED | | | |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
