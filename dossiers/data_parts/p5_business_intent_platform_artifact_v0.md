# Stage 5 — Business Intent: platform / artifact
**Stage:** 5 — Business Intent
**CR:** data_parts
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The artifact subdomain governs how a declaration is read: which parts name another artifact, which
parts only explain, which lists are read as sets, and which parts record history. Its authority is
to state, once, how every reader of a declaration tells a name from a value, and it decides nothing
about what any declaration says.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| artifact | Governs how a declaration is read, and how every reader tells a name from a value. | S1 cr_type #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Declaring a part whose contents are values | IN_SCOPE | A data part is declared by name, as a reference part is. | S4 authoring_scope #1 |
| Passing over a data part when finding references | IN_SCOPE | One walk decides what a reference is for every reader. | S4 authoring_scope #2 |
| Reading the new version wherever the vocabulary is read | IN_SCOPE | A reader of the old version reads a declaration that no longer stands. | S4 authoring_scope #3 |
| Declaring any other part data | DEFERRED | Nothing needs it today; each is declared when it is needed. | S4 authoring_scope deferred #1 |
| What any vector states | DEFERRED | Each domain's business. | S4 authoring_scope deferred #2 |

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
| Every reference is in a part declared to hold references. | What names another artifact is declared, never inferred. | S4 constraint_register #1 |
| Nothing inside a data part is read as a reference. | A value that looks like a name is still a value; reading it as a reference refuses data no transform can be proven without. | S4 constraint_register #2 |
| A name outside every declared part is still refused. | Otherwise a misspelled reference passes as a value, and the rule that a reference is declared stops catching anything. | S4 constraint_register #3 |
| A part's name means the same thing in every kind. | A part is declared by its name, so a name read two ways would make a declaration mean what its kind says rather than what it states. | S4 constraint_register #4 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Declare a part whose contents are values | Data part | The platform declaring how a vector's cases are read. | IN_SCOPE | S4 capability_graph #1 |
| Pass over a data part when finding references | Data part | The platform reading a declaration. | IN_SCOPE | S4 capability_graph #2 |
| Read the vocabulary's new version | Declaration | The vocabulary gaining a group. | IN_SCOPE | S4 capability_graph #3 |

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
