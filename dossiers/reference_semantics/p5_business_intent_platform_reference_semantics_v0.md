# Stage 5 — Business Intent: platform / reference semantics

**Stage:** 5 — Business Intent

**CR:** reference_semantics

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The artifact subdomain governs what an artifact's identity stands for: that an identity names one
meaning, that a superseded artifact stays in the record and out of reach, and that nothing reaches
an artifact that has been stood down. Its authority is to decide what makes an identity sound. It
decides nothing about what any particular artifact means.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| artifact | Declares which parts of a declaration carry no meaning and which name another artifact, so a change of meaning can be told from a change of wording and a replacement can learn what it reaches. | S4 actors Artifact |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Declare what names another artifact | IN_SCOPE | A new version of the declaration of what carries no meaning. | S4 authoring_scope GAP-01 |
| Declare short-code references | DEFERRED | The compiler resolves them its own way. | S4 authoring_scope Declare short-code references |

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
| One place declares which parts of a declaration are references. | Four places decided it and disagreed. | S1 business_invariants #1 |
| Every full name in a declaration sits in a part declared a reference. | What names another artifact is declared, never inferred. | S1 business_invariants #2 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Declare | What names another artifact | A part is found to hold a full name wherever it appears | IN_SCOPE | S4 capability_graph Declare what names another artifact |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| artifact | VOCAB_DECLARATION_REPRESENTATION_V1 | VOCAB | The parts of a declaration that carry no meaning, the parts that name another artifact, and the rules a comparison applies. | S4 design_decisions #1 |

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
