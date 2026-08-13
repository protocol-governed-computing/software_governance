# Stage 6 — Governance Intent: platform / runtime_binding
**Stage:** 6 — Governance Intent
**CR:** multi_structure_binding
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `runtime_binding` — EXISTING — modified by this CR |
| Authority class | reuse existing — an act declares, a subdomain owns, assembly refuses; no new actor type |
| Governing constitutions | `fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0`, `fb.structure::CONSTITUTION_STRUCTURE_V0`, `fb.workflow::CONSTITUTION_WORKFLOW_V0` |

Where an act finds its records is what runtime binding governs, so the resolution model belongs to
it. Nothing new stands on its own, so no subdomain is declared.

**No domain artifact appears in the action registers below.** The instance that surfaced this
requirement lives in a business domain, and it is recorded at S2 and S3 as what was observed. The
domain half — an act naming the binding it consults — is a change request in that domain, raised
against the model this change states, and scheduling it here would claim work this dossier does not
own.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Naming, on an act, the bindings it operates under | runtime_binding | OWNED | | S4 gap_register GAP-1 |
| Stating which named places an act owns and which it consults | runtime_binding | OWNED | | S4 gap_register GAP-2 |
| Stating how an act resolves its records | runtime_binding | OWNED | | S4 gap_register GAP-3 |
| Refusing a composition where two subdomains describe one record | runtime_binding | OWNED | | S4 gap_register GAP-4 |
| Making the reach visible in the design | runtime_binding | OWNED | | S4 gap_register GAP-5 |
| Refusing a reach that would change what it does not own | runtime_binding | OWNED | | S4 gap_register GAP-6 |
| Telling a reading operation from a writing one | runtime_binding | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S4 capability_graph #7 |
| Deciding which acts reach which subdomains | runtime_binding | DEFERRED | | S4 authoring_scope deferred #1 |
| Declaring which readers may see which records | runtime_binding | DEFERRED | | S4 authoring_scope deferred #2 |
| Declaring how a subdomain's ownership of a record is established | runtime_binding | DEFERRED | | S4 authoring_scope deferred #3 |
| Reaching records another domain holds | runtime_binding | DEFERRED | | S4 authoring_scope deferred #4 |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| The design register that states where an act's records live | runtime_binding -> design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | GAP | S4 dependency_graph #3 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 | Governs bindings and says nothing about where storage is described or how much of it an act reaches. | EXTEND | S4 gap_register GAP-3 |
| fb.runtime_binding::INVARIANT_RB_BINDING_POLICY_CONFORMANCE_V0 | Checks the binding policy the compiler sealed, over the one description it finds. | EXTEND | S4 gap_register GAP-4 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_RECORD_IS_DESCRIBED_ONCE | A record has exactly one description, written by the subdomain that owns it. Two descriptions can disagree, and then what the business holds depends on which one a run happened to read. | S4 constraint_register #1 |
| THE_OWNER_IS_THE_ONLY_WRITER | The subdomain that owns a record is the only one that changes it. Ownership that does not include being the only writer is not ownership. | S4 constraint_register #2 |
| A_REACH_READS_AND_NEVER_WRITES | An act that reaches records it does not own reads them and never changes them. Changing them makes the reader a second author of a truth somebody else answers for. | S4 constraint_register #3 |
| A_REACH_STAYS_INSIDE_ITS_DOMAIN | An act reaches only what its own domain holds. An act reading across a domain boundary is correct only in the compositions that include that domain, and fails when it runs in the ones that do not. | S4 constraint_register #4 |
| THE_REACHER_DECLARES_THE_REACH | A reach is declared by the act that reaches, in an artifact that act owns. The act is the only party that knows it reads elsewhere. | S4 constraint_register #5 |
| OWNED_IS_DISTINGUISHABLE_FROM_CONSULTED | An act says of each place it names whether it owns it or consults it. A declaration that grants the reach and hides the distinction cannot be held to reading. | S4 constraint_register #6 |
| NO_SUBDOMAIN_DESCRIBES_ANOTHERS_STORAGE | No subdomain's artifact describes another subdomain's storage. The maintainer of the statement would not be the owner of what it describes. | S4 constraint_register #7 |
| A_COPY_IS_NOT_A_REACH | An act may not gain the ability to reach records by restating another subdomain's description as its own. That workaround works today and needs nothing from this change, which is what makes it the easy wrong act. | S4 constraint_register #9 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Naming, on an act, the bindings it operates under | runtime_binding | S4 gap_register GAP-1 |
| Stating which named places an act owns and which it consults | runtime_binding | S4 gap_register GAP-2 |
| Stating how an act resolves its records | runtime_binding | S4 gap_register GAP-3 |
| Refusing a composition where two subdomains describe one record | runtime_binding | S4 gap_register GAP-4 |
| Making the reach visible in the design | runtime_binding | S4 gap_register GAP-5 |
| Refusing a reach that would change what it does not own | runtime_binding | S4 gap_register GAP-6 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
