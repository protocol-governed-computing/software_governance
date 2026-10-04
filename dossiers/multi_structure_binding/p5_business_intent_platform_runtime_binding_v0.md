# Stage 5 — Business Intent: platform / runtime_binding
**Stage:** 5 — Business Intent
**CR:** multi_structure_binding
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

Runtime binding governs where an act finds the records it works on. A subdomain owns what it holds
and says where its own records live; binding is what connects an act, when it runs, to those
descriptions. Its authority is to decide what an act may reach and whose description of a record is
authoritative, and it decides nothing about what any act should do or which records a subdomain
ought to own.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| runtime_binding | Governs where an act finds the records it works on — what it may reach, and whose description of a record is authoritative. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Naming, on an act, the bindings it operates under | IN_SCOPE | The reach itself; nothing else is reachable without it. | S4 authoring_scope #1 |
| Stating which named places an act owns and which it consults | IN_SCOPE | What a read-only reach is held to. | S4 authoring_scope #2 |
| Stating how an act resolves its records | IN_SCOPE | Nothing says it today, so the model is stated rather than widened. | S4 authoring_scope #3 |
| Refusing a composition where two subdomains describe one record | IN_SCOPE | The check that the reach is not answered by copying. | S4 authoring_scope #4 |
| Making the reach visible in the design | IN_SCOPE | Without it the next reach is discovered the same way this one was. | S4 authoring_scope #5 |
| Refusing a reach that would change what it does not own | IN_SCOPE | Holds a design today; must hold an act when it runs. | S4 authoring_scope #6 |
| Deciding which acts reach which subdomains | DEFERRED | Each domain's business, stated in its own change. | S4 authoring_scope deferred #1 |
| Declaring which readers may see which records | DEFERRED | Access control needs its own mechanism, and no act needs it. | S4 authoring_scope deferred #2 |
| Declaring how a subdomain's ownership of a record is established | DEFERRED | Ownership is settled by convention today and stating it is a separate problem. | S4 authoring_scope deferred #3 |
| Reaching records another domain holds | DEFERRED | A question about what is composed together, answered there. | S4 authoring_scope deferred #4 |

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
| A record has exactly one description, written by the subdomain that owns it. | Two descriptions of one record can disagree, and then what the business holds depends on which one a run happened to read. | S4 constraint_register #1 |
| The owner of a record is the only writer of it. | Ownership that does not include being the only writer is not ownership: two subdomains would decide what is true and neither would be answerable for the result. | S4 constraint_register #2 |
| An act that reaches records it does not own reads them and never changes them. | An act may consult what another subdomain holds because a second copy of one truth can disagree with the thing it describes; changing it makes the reader a second author. | S4 constraint_register #3 |
| An act reaches only what its own domain holds. | An act that reads across a domain boundary is correct only in the compositions that happen to include that domain, and would fail when it runs in the ones that do not. | S4 constraint_register #4 |
| A reach is declared by the act that reaches, in an artifact that act owns. | The act is the only party that knows it reads elsewhere, and a list of readers kept by the owner is a second copy nothing keeps in step. | S4 constraint_register #5 |
| An act's own records are distinguishable from those it merely consults. | A declaration that grants the reach and hides that distinction cannot be held to reading, because nothing could tell which place a write was aimed at. | S4 constraint_register #6 |
| No subdomain's artifact describes another subdomain's storage. | The maintainer of a statement would then not be the owner of what it describes, which is the second copy this change exists to prevent. | S4 constraint_register #7 |
| The reach is declared where a reviewer reads it, not inferred from what an act happens to reuse. | A reach nothing states is one no review can see, and it is discovered when the act runs. | S4 constraint_register #8 |
| An act may not gain the ability to reach records by restating another subdomain's description as its own. | That workaround works today and needs nothing from this change; leaving it available makes the wrong act the easy one. | S4 constraint_register #9 |
| Naming another subdomain's records is not the same act as being permitted to write to them. | The reach must be scoped rather than merely granted, or read-only is a sentence rather than a rule. | S4 constraint_register #10 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Name the bindings an act operates under | Binding | An act being authored that reads records another subdomain owns. | IN_SCOPE | S4 capability_graph #1 |
| State whether a named place is owned or consulted | Reach | An act naming a place where storage is described. | IN_SCOPE | S4 capability_graph #2 |
| State how an act resolves its records | Storage description | The model being declared for the first time. | IN_SCOPE | S4 capability_graph #3 |
| Refuse a composition where two subdomains describe one record | Contested description | A composition being assembled. | IN_SCOPE | S4 capability_graph #4 |
| Show the reach in the design | Reach | A design stating where an act's records live. | IN_SCOPE | S4 capability_graph #5 |
| Refuse a reach that would change what it does not own | Reach | An act attempting to write to a place it consults. | IN_SCOPE | S4 capability_graph #6 |

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
