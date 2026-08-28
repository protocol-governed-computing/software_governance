# Stage 5 — Business Intent: platform / conformance
**Stage:** 5 — Business Intent
**CR:** enforcement_capability
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The conformance subdomain governs the relation between an obligation and the check that carries it:
that every obligation has one, that every check has an obligation, and that the pair can be counted.
Its authority is to decide what makes that relation sound. It decides nothing about what any
particular obligation requires.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| conformance | Governs the relation between an obligation and the check that carries it, and decides what makes that relation sound. | S1 cr_type #1 |
| capability_contracts | Governs what a capability contract is and what may be required of one. It holds the single obligation this change withdraws, which judges quality rather than admissibility. | S4 gap_register GAP-5 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Refusing a check that cannot refuse | IN_SCOPE | The mechanism that refuses the next one; without it the rest is a cleanup. | S4 authoring_scope #1 |
| Declaring whether an obligation is enforced | IN_SCOPE | A value of the place of enforcement, not a second field. | S4 authoring_scope #2 |
| Naming where a delegated obligation is carried | IN_SCOPE | A destination that can be followed, in place of a sentence in a docstring. | S4 authoring_scope #3 |
| Counting what is unenforced | IN_SCOPE | A column of the record every build already writes. | S4 authoring_scope #4 |
| Withdrawing the obligation that judges quality | IN_SCOPE | The one obligation of eighty-nine whose violation warns. | S4 authoring_scope #5 |
| Restating the parity obligation | IN_SCOPE | Superseded by derivation; restated to say so, with its dead check withdrawn. | S4 authoring_scope #6 |
| Building the enforcement the ten deferred obligations describe | DEFERRED | Each is its own change with its own subject; this one makes the deferral honest and countable. | S4 authoring_scope deferred #1 |
| Deciding whether a refusal path can be reached by its own obligation | DEFERRED | Established for one case by reading and not decidable in general; requiring it would demand what cannot be supplied. | S4 authoring_scope deferred #2 |
| Establishing that a check has ever been observed to refuse | DEFERRED | A stronger question than capability, needing a case per check. | S4 authoring_scope deferred #3 |
| The obligations of domains other than the platform | DEFERRED | Each domain's own change, once the platform can express what it needs. | S4 authoring_scope deferred #4 |

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
| An obligation declared as enforced has a check capable of refusing it. | A check that carries nothing makes its obligation a claim, and a reader counting obligations concludes the system is governed where it is not. Fourteen such obligations claim their violation fails the build immediately, and none of the fourteen can produce a violation. | S4 constraint_register #1 |
| An obligation not enforced says so, in a form a mechanism reads. | Ten authors wrote the deferral into prose because there was no field for it, and prose is why the deferral became indistinguishable from enforcement. The declaration has value and is not deleted for being unenforced. | S4 constraint_register #2 |
| Declaring an obligation unenforced does not make it optional. | An obligation stated deliberately and not yet carried is a debt the platform has taken on. Saying so honestly is what makes it a debt rather than a fiction; it does not make it a preference. | S4 constraint_register #3 |
| An obligation enforced elsewhere names where, and that place is checkable. | A delegation nobody can follow is indistinguishable from an absence, and absence is not permission. Three of the four present delegations name a mechanism that exists; the fourth names code review, which no mechanism can confirm. | S4 constraint_register #4 |
| The obligation-to-check relation gains a requirement rather than losing one. | Every obligation carried today is carried afterwards, on the same terms. The change adds what the relation must additionally require, and takes nothing away from what it already establishes. | S4 constraint_register #5 |
| Deciding admissibility and judging quality are never carried by one obligation. | An obligation whose violation produces a report leaves the violation standing, and governance that leaves the violation standing is a description. The one obligation whose subject is whether a thing is good is withdrawn rather than made to refuse. | S4 constraint_register #6 |
| The change requires what capability can be decided, and declares what cannot. | A check with no refusal path is decidable from the check alone. Whether a refusal path can be reached by its own obligation is a relation between two artifacts, established once by reading and not decidable in general. Requiring the second would demand what no author could supply. | S4 constraint_register #7 |
| Carried elsewhere is one status with a destination, not one status per kind of destination. | The three delegations point at three different kinds of place — a phase of the build, the runtime, a practice — and the difference between them is which place, not which status. A status per kind of place would multiply as new kinds appear. | S4 constraint_register #8 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Refuse a composition whose obligation claims enforcement its check cannot deliver | Obligation | A check being derived from an obligation that declares itself enforced. | IN_SCOPE | S4 capability_graph #1 |
| Declare that an obligation is not yet enforced | Obligation | An author stating a deferral they would otherwise write in prose. | IN_SCOPE | S4 capability_graph #2 |
| Name the place a delegated obligation is carried | Obligation | An obligation declaring that its check is somewhere other than the build. | IN_SCOPE | S4 capability_graph #3 |
| Refuse a delegation that names no place | Obligation | An obligation claiming to be carried elsewhere without saying where. | IN_SCOPE | S1 operation_refusals #2 |
| Count the obligations that are not enforced | Determination record | A composition being built. | IN_SCOPE | S4 capability_graph #4 |
| Withdraw the obligation that judges quality | Obligation | This change. | IN_SCOPE | S4 capability_graph #5 |
| Restate the parity obligation as carried by derivation | Obligation | This change. | IN_SCOPE | S4 capability_graph #6 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| conformance | VOCAB_ENFORCEMENT_STATUS_V0 | VOCAB | The places an obligation may be enforced, extended with one meaning declared and not yet enforced, and with what a destination must state. | S4 design_decisions #2 |

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
