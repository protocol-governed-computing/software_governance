# Stage 5 — Business Intent: platform / published rules

**Stage:** 5 — Business Intent

**CR:** published_rules

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The execution topology subdomain governs how a contract is built from steps: that each step
dispatches one capability, answers the outcomes it can produce, and says for each what happens next.
The trace subdomain governs the run's record: what a trace holds and the schema every line conforms
to. Each decides what makes its subject sound, and neither decides what any particular contract does.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| execution_topology | States what a step must route, under an identity that means what it says. | S4 actors Execution topology |
| trace | States what a trace must conform to, under an identity that means what it says. | S4 actors Trace |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| State the routing rule | IN_SCOPE | A successor stating CP-13. | S4 authoring_scope GAP-01 |
| State the record rule | IN_SCOPE | A successor naming the second schema. | S4 authoring_scope GAP-02 |
| Return routes changed in place in contracts and workflows | DEFERRED | Each domain's own change. | S4 authoring_scope Return routes changed in place in contracts and workflows |

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
| A published identity means what it meant when it was published. | A release is cited for what it said. | S1 business_invariants #1 |
| Every rule in force says what its check enforces. | A check bound to a rule that says less enforces an unstated rule. | S1 business_invariants #2 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| State | The routing rule | A composition is built | IN_SCOPE | S4 capability_graph State the routing rule |
| State | The record rule | A run writes its record | IN_SCOPE | S4 capability_graph State the record rule |

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
