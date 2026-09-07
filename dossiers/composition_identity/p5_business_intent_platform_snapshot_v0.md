# Stage 5 — Business Intent: platform / snapshot
**Stage:** 5 — Business Intent
**CR:** composition_identity
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The snapshot subdomain governs what a built composition is: the files it carries, the identity that
names it, and what a reader may conclude from two identities being the same or different. Its
authority is to decide what belongs to a composition's identity and what merely accompanies it. It
decides nothing about what any composition contains.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| snapshot | Governs what a built composition is, and decides what belongs to its identity and what merely accompanies it. | S1 cr_type #1 |
| cryptographic_trust | Governs what may be trusted and how it is attested. It owns the attestation whose fields this change divides between constituting and accompanying, and states that division. | S4 gap_register GAP-2 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Excluding at the grain of a field | IN_SCOPE | The attestation carries a binding the runtime enforces, so the file stays and the field goes. | S4 authoring_scope #1 |
| Stating what an attestation contributes to identity | IN_SCOPE | Stated by the subdomain that owns the attestation, consumed by the one that computes the identity. | S4 authoring_scope #2 |
| Requiring a rebuild to reproduce an identity | IN_SCOPE | Nothing requires it, which is why twenty failing pins went unreported. | S4 authoring_scope #3 |
| Making the signature real | DEFERRED | Its own change, with its own subject; this one makes the identity stable whether the signature is a placeholder or not. | S4 authoring_scope deferred #1 |
| Establishing reproducibility across machines | DEFERRED | Not measured anywhere, and requiring it would demand what nobody has established. | S4 authoring_scope deferred #2 |
| Ruling on the approvals recorded against expired pins | DEFERRED | A human ruling reaching every completed change, and not one a mechanism makes. | S4 authoring_scope deferred #3 |
| Re-pinning the twenty expired dossiers | DEFERRED | Follows the ruling, and each is its own dossier's act. | S4 authoring_scope deferred #4 |

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
| A composition's identity is a function of what it contains and of nothing else. | An identity that counts when a build ran answers a different question from the one a reader asks it, and the reader cannot tell which question was answered. | S4 constraint_register #1 |
| Building unchanged source twice produces one identity. | A pin records the composition a change was validated against so a later reader may re-check it. If a rebuild produces a different composition, the record names something nobody can produce, and every claim resting on it becomes unverifiable. | S4 constraint_register #1 |
| Two identities differing means the compositions differ. | The identity exists to make an alteration after sealing, or a relocation, detectable. A field that changes on every build makes a genuine alteration and a rebuild indistinguishable, so a reader who sees identities differ learns nothing. | S4 constraint_register #2 |
| A composition altered after sealing is refused. | The composition a reader relies on must be the one that was constituted, or the reliance is on something no longer there. | S4 constraint_register #2 |
| A composition moved somewhere it was not built for is refused. | A composition that answers correctly in a place it was never constituted for is a composition nobody can locate. | S4 constraint_register #3 |
| What accompanies a composition is excluded from its identity by declaration. | Two files are already excluded, each naming its ground where the exclusion is made. An exclusion inferred from a directory or a suffix would move whenever a file moved. | S4 constraint_register #5 |
| An attestation's determinative fields stay in the identity. | The runtime refuses a composition whose projection does not match what its attestation binds. Excluding the file would drop an enforced binding, which is the opposite of what this change wants. | S4 constraint_register #6 |
| The record of when a composition was signed is kept. | It is what an attestation is for, once the signature is real. What is wrong is counting it as part of what the composition is, not writing it. | S4 constraint_register #4 |
| The change claims stability, not reproducibility. | Two builds on one machine minutes apart is what was measured. Claiming more would assert a property nobody has established, and a further instability would be a further change. | S4 constraint_register #7 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Exclude a field that records rather than constitutes | Constituent | A composition being constituted. | IN_SCOPE | S4 capability_graph #1 |
| State which of an attestation's fields constitute the composition | Attestation | An attestation being declared. | IN_SCOPE | S4 capability_graph #2 |
| Refuse a rebuild that does not reproduce the identity of unchanged source | Composition | A composition being built from source that has not changed. | IN_SCOPE | S4 capability_graph #3 |
| Refuse a composition altered after it was sealed | Composition | A composition being verified. | IN_SCOPE | S1 operation_refusals #1 |
| Refuse a composition read where it was not built for | Composition | A composition being verified. | IN_SCOPE | S1 operation_refusals #2 |

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
| Stage 6 — Governance Intent | Pending | — |
