# Stage 5 — Business Intent: platform / routing closure

**Stage:** 5 — Business Intent

**CR:** routing_closure

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
| execution_topology | Holds every step to the outcomes its capability declares, at build time and at run time. | S4 actors Execution Topology |
| workflow | Holds every reachable workflow place to the outcomes of what it runs. | S4 actors Workflow |
| trace | Records each step's outcome and what happened next. | S4 actors Trace |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Refuse a narrowed step | IN_SCOPE | The step check compares with the capability. | S4 authoring_scope GAP-01 |
| Refuse an unrouted reachable place | IN_SCOPE | A new workflow obligation. | S4 authoring_scope GAP-02 |
| Refuse an unanswered step outcome | IN_SCOPE | Execution refuses where it defaulted. | S4 authoring_scope GAP-03 |
| Record each step's decision | IN_SCOPE | The step entry gains two required fields. | S4 authoring_scope GAP-04 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Run record | APPEND_ONLY_JOURNAL | Each step line now carries its outcome and what happened next. | S4 bm_entities The Step Record |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Run record | Run | Named when the run starts | One record per run; unchanged by this change. | None | S4 bm_entities The Step Record |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| No step answers fewer outcomes than its capability declares. | A missing answer is never a default. | S1 business_invariants #1 |
| No reachable workflow place leaves an outcome of its contract without a route. | A refusal at build time comes first. | S1 business_invariants #2 |
| Execution never carries on past an outcome nothing answers. | A failed step must not be treated as a successful one. | S1 business_invariants #3 |
| Every step that runs is recorded with its outcome and what happened next. | A decision that went wrong must leave a record. | S1 business_invariants #4 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Refuse | A narrowed step | A composition is built | IN_SCOPE | S4 capability_graph Refuse a narrowed step |
| Refuse | An unrouted reachable place | A composition is built | IN_SCOPE | S4 capability_graph Refuse an unrouted reachable place |
| Refuse | A request at an unanswered step outcome | A step ends with an outcome nothing answers | IN_SCOPE | S4 capability_graph Refuse an unanswered step outcome |
| Record | Each step's decision | A step runs | IN_SCOPE | S4 capability_graph Record each step's decision |

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
