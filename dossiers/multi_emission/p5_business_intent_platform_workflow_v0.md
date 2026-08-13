# Stage 5 — Business Intent: platform / workflow
**Stage:** 5 — Business Intent
**CR:** multi_emission
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The workflow subdomain governs the act: what an act is composed of, how it routes between the things
it performs, and where it ends. An act ends at a terminal node, and what that node announces is the
business's account of what the act completed. Its authority is to decide the shape of an act and the
account it gives of itself, and it decides nothing about what any particular act should do or which
moments a business declares matter.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| workflow | Governs the act — its composition, its routing, its ending, and the account it gives of what it completed. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Stating what a terminal node announces | IN_SCOPE | Nothing says it today; the model is declared rather than relaxed. | S4 authoring_scope #1 |
| Declaring the order normative | IN_SCOPE | A sequence is not a set with an order bolted on. | S4 authoring_scope #2 |
| Announcing an ordered sequence at one ending | IN_SCOPE | What widens is the shape a transition carries. | S4 authoring_scope #3 |
| Reporting an announcement that cannot be made | IN_SCOPE | The only choice available is loud or silent. | S4 authoring_scope #4 |
| Refusing a moment announced twice | IN_SCOPE | Twice from one act says it occurred twice. | S4 authoring_scope #5 |
| Asserting what an act announced | IN_SCOPE | The one existing reader takes the first it finds. | S4 authoring_scope #6 |
| A moment announced per member of a collection | DEFERRED | A different shape, and not what the confirmed requirement needs. | S4 authoring_scope deferred #1 |
| Deciding which moments each act announces | DEFERRED | Each domain's business, stated in its own change. | S4 authoring_scope deferred #2 |
| Checking that every declared moment is announced by something | DEFERRED | A subdomain declared six and wired none; whether that should be refused is its own question. | S4 authoring_scope deferred #3 |

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
| Every declared moment an act completes is announced by that act. | The business declared the moment matters; one that is never announced is a fact the business asked to see and cannot. | S4 constraint_register #4 |
| Several moments are announced in the order the design states. | Every serialization is ordered incidentally. Only a declaration makes the order something a reader may rely on, and a change to it a change to the account of what happened. | S4 constraint_register #1 |
| Each moment announced has its own evidence record. | Every reader asks a per-moment question, and a record naming several turns that into a substring question and a count into a different number. | S4 constraint_register #2 |
| An act announces each moment at most once. | Twice from one act says the moment occurred twice, and a reader counting occurrences would rightly conclude something happened that did not. | S4 constraint_register #3 |
| An announcement that cannot be made is reported, and never passed over. | The act's work is done and its records are immutable, so the choice is not refuse or continue — it is loud or silent, and silence is the defect. | S4 constraint_register #7 |
| An act is never split, and no moment dropped, to fit the announcement mechanism. | Splitting an act that the business performs as one thing changes the business to suit the platform. | S4 constraint_register #5 |
| A behaviour the platform performs is governed by a document that states it. | A behaviour no document governs is ungoverned rather than leniently governed, and is discovered rather than known. | S4 constraint_register #8 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Announce an ordered sequence of moments | Announcement | An act reaching an ending that announces. | IN_SCOPE | S4 capability_graph #3 |
| State what a terminal node announces | Terminal node | The model being declared for the first time. | IN_SCOPE | S4 capability_graph #1 |
| Declare the order of several announcements normative | Order | A design stating more than one moment at one ending. | IN_SCOPE | S4 capability_graph #2 |
| Report an announcement that cannot be made | Announcement | A moment an act completed that cannot be stated. | IN_SCOPE | S4 capability_graph #4 |
| Refuse a moment announced twice | Moment | A design naming one moment twice at one ending. | IN_SCOPE | S4 capability_graph #5 |
| Assert what an act announced | Evidence record | A reader checking an act's account of itself. | IN_SCOPE | S4 capability_graph #6 |

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
