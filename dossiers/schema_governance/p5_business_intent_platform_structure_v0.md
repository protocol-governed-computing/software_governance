# Stage 5 — Business Intent: platform / structure
**Stage:** 5 — Business Intent
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The structure subdomain governs how the platform describes itself to itself: what a declaration of
each kind may contain, which description governs which kind, and where each is found. Its authority
is to decide what makes a description binding. It decides nothing about what any particular artifact
declares.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| structure | Governs which kind is described by what, and what makes a description binding. | S1 cr_type #1 |
| transport | Governs the boundary a caller reaches the composition through. It owns the two kinds that have no description, and what those declarations may contain is its to state. | S4 gap_register GAP-4 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Reporting a description that has stopped matching | IN_SCOPE | Every drift here was found by a build refusing correct work; that method only works on a description nobody relies on. | S4 authoring_scope #1 |
| Correcting a description that has drifted | IN_SCOPE | Three descriptions, 62 artifacts, none of which changes. | S4 authoring_scope #2 |
| Stating what makes a description one | IN_SCOPE | A description requiring no field and closing no surface is dispatched and reads as governance. | S4 authoring_scope #3 |
| Describing a kind that has no description | IN_SCOPE | The two transport boundary kinds, 44 artifacts, described by the subdomain that owns them. | S4 authoring_scope #4 |
| Recording that a kind needs no description | IN_SCOPE | An exempt kind and a forgotten kind are the same absence today. | S4 authoring_scope #5 |
| Reconsidering the shape of a kind whose description drifted | DEFERRED | A claim about the kind, owned by that kind's subdomain, escalated rather than settled here. | S4 authoring_scope deferred #1 |
| Separating the runtime-data descriptions from the artifact-kind ones | DEFERRED | They describe no artifact kind and govern correctly where they are. | S4 authoring_scope deferred #2 |
| What a declaration of each kind means | DEFERRED | Each kind's own subdomain, asked when its description is written or corrected. | S4 authoring_scope deferred #3 |

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
| Every artifact kind is either described, or recorded as exempt with the ground stated. | A kind absent from the table is absent because nobody wrote a description, because one exists and nobody named it, or because the kind needs none. Three different facts and one representation, so a reader cannot tell a decision from an oversight. | S4 constraint_register #4 |
| A description matches the shape the platform currently builds. | The artifacts are what every green build produces and what the runtime executes. A description that disagrees is disagreeing with the working system, and dispatching it turns correct work away with the authority of a rule. | S4 constraint_register #7 |
| A description admits only what it names. | A description that names nothing as forbidden admits anything beside what it names, so a declaration may carry content nobody described and still pass. | S4 constraint_register #8 |
| A description states something. | One is dispatched, requires no field, closes no surface, and thereby reads as governance to any reader counting dispatched kinds. Coverage is not governance, and a count cannot tell them apart. | S4 constraint_register #8 |
| A correct declaration is never refused. | Dispatching four descriptions refused one hundred correct declarations. A wrong description refuses with the authority of a rule, which is worse than describing nothing. | S4 constraint_register #1 |
| A description that stops matching what it describes is reported. | Three divergences, none recorded when it happened, all found by a build refusing correct work. Correcting them restores today and does nothing about tomorrow. | S4 constraint_register #7 |
| No artifact is edited to satisfy a stale description. | The artifacts are current. Editing one to match a description nobody had read since writing it would change the working system to preserve a mistake. | S4 constraint_register #2 |
| A genuinely invalid declaration is still refused. | This change corrects what is checked against; it does not reduce what is checked. | S4 constraint_register #6 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Report a description that no longer matches the artifacts of its kind | Drift | A composition being built. | IN_SCOPE | S4 capability_graph #1 |
| Correct a description toward the artifacts it describes | Description | A drift being reported. | IN_SCOPE | S4 capability_graph #2 |
| Refuse a description that states nothing | Description | A kind being dispatched to it. | IN_SCOPE | S4 capability_graph #3 |
| Describe a kind that has none | Kind | This change, for the two transport boundary kinds. | IN_SCOPE | S4 capability_graph #4 |
| Record that a kind needs no description | Exemption | A decision that a kind is exempt. | IN_SCOPE | S4 capability_graph #5 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| structure | VOCAB_SCHEMA_DISPOSITION_V0 | VOCAB | The dispositions a kind may have toward description — described, exempt with a ground, or neither — and which of them the build admits | S4 gap_register GAP-5 |

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
| Stage 6 — Governance Intent | Pending | — |
