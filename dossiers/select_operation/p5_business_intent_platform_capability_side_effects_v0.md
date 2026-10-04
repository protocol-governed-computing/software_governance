# Stage 5 — Business Intent: platform / capability_side_effects
**Stage:** 5 — Business Intent
**CR:** select_operation
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

Capability side effects are the platform's offer of what the business cannot do for itself: holding a
record, appending to a trail, reading a clock. A domain composes what is offered and never decides
what is on offer, because every domain reaches the same capability and a change to one is a change
for all of them. The subdomain's authority is to state that offer and to keep it closed: a capability
nobody admitted cannot be reached, and an operation nobody declared does not exist.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| capability_side_effects | States what the platform offers the business, and keeps that offer closed. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Recording why the capability offers an operation that reads every record | IN_SCOPE | The reason exists and is held by the first caller that needed it. | S4 authoring_scope #1 |
| Recording that the change crossed an authority boundary | IN_SCOPE | Without it the record explains the offer and hides how it came to be unexplained. | S4 authoring_scope #2 |
| Whether every operation should carry the change that added it | DEFERRED | The general question; this change records one instance. | S4 authoring_scope deferred #1 |
| What other capabilities offer | DEFERRED | Each is its own question. | S4 authoring_scope deferred #2 |
| Withdrawing an operation nothing composes | DEFERRED | No such operation has been found. | S4 authoring_scope deferred #3 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| NONE IDENTIFIED |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| A capability's offer is decided by the platform, never by a domain that reaches it. | Every domain reaches the same capability, so a domain deciding its offer decides for domains that never saw the change. | S4 constraint_register #1 |
| Every operation a capability offers has a recorded reason for being offered. | Without one, the next domain to reach an operation cannot tell a load-bearing part of the platform from something added for a single caller. | S4 constraint_register #2 |
| A change to a capability is recorded where the capability is declared. | Every domain reads the capability and only one reads the change request that needed it; a reason held by the first caller is unfindable by the second. | S4 constraint_register #3 |
| The operation stays exactly as it is; this change records it and alters nothing. | It is declared, reached by two contracts and running against real stores. Altering it would break callers to satisfy bookkeeping. | S4 constraint_register #4 |
| The change is not re-delivered through the pipeline, because there is nothing left to deliver. | What was missing is the record, and re-delivering working behaviour to produce a record is a cost with no result. | S4 constraint_register #6 |
| A change that crossed a boundary before the boundary was stated is not a breach of a rule in force. | Recording it is what makes the first instance visible rather than absorbed, and the record is factual rather than accusatory. | S4 constraint_register #7 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Record why an operation is offered | Operation | An operation being added to a capability. | IN_SCOPE | S4 capability_graph #1 |
| Record that a change crossed an authority boundary | Offer | A change to a capability arriving from a domain that reaches it. | IN_SCOPE | S4 capability_graph #2 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|
| NONE IDENTIFIED |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
