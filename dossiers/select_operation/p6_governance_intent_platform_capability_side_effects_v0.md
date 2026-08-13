# Stage 6 — Governance Intent: platform / capability_side_effects
**Stage:** 6 — Governance Intent
**CR:** select_operation
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `capability_side_effects` — EXISTING — modified by this CR |
| Authority class | reuse existing — the platform decides an offer, a domain composes it; no new actor type |
| Governing constitutions | `fb.capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0`, `fb.governance::CONSTITUTION_GOVERNANCE_V0` |

What a capability offers is what this subdomain governs, so the record of why it offers an operation
belongs to it. Nothing new stands on its own, so no subdomain is declared.

**No domain artifact appears in the action registers below.** The operation has consumers, and they
are recorded at S2 and S3 as what was observed in the composition this dossier was validated against.
A consumer requires no action here, and a platform change that scheduled work inside a domain would
be claiming what it does not own.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Recording why the capability offers an operation that reads every record | capability_side_effects | OWNED | | S4 gap_register GAP-1 |
| Recording that the change crossed an authority boundary | capability_side_effects | OWNED | | S4 gap_register GAP-2 |
| The operation itself | capability_side_effects | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S4 capability_graph #3 |
| Whether every operation should carry the change that added it | capability_side_effects | DEFERRED | | S4 authoring_scope deferred #1 |
| What other capabilities offer | capability_side_effects | DEFERRED | | S4 authoring_scope deferred #2 |
| Withdrawing an operation nothing composes | capability_side_effects | DEFERRED | | S4 authoring_scope deferred #3 |

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
| NONE IDENTIFIED |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | Offers nine operations, one of which arrived with a business change request and carries no recorded reason. | REVIEW | S4 gap_register GAP-1 |
| fb.capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0 | Declares what a capability side effect is, and says nothing about who may change what an admitted one offers. | REVIEW | S4 constraint_register #1 |
| fb.capability_side_effects::INVARIANT_CS_SURFACE_CLOSED_V1 | Refuses a capability nobody admitted, and does not examine the operations an admitted one offers. | REVIEW | S4 constraint_register #1 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| THE_PLATFORM_DECIDES_ITS_OFFER | A capability's offer is decided by the platform, never by a domain that reaches it. Every domain reaches the same capability, so a domain deciding its offer decides for domains that never saw the change. | S4 constraint_register #1 |
| AN_OFFER_CARRIES_ITS_REASON | Every operation a capability offers has a recorded reason for being offered, or the next domain to reach it cannot tell the platform's decision from one caller's need. | S4 constraint_register #2 |
| THE_RECORD_LIVES_WITH_THE_CAPABILITY | A change to a capability is recorded where the capability is declared, not where the caller that needed it lives. | S4 constraint_register #3 |
| A_RECORD_CHANGES_NOTHING | Recording an operation alters neither the operation nor the acts that compose it. A record that changed behaviour would be a second change wearing the first one's name. | S4 constraint_register #4 |
| A_CROSSING_BEFORE_THE_RULE_IS_NOT_A_BREACH | A change that crossed a boundary before the boundary was stated is recorded as history rather than as a violation. What makes it worth recording is that the rule now refusing it needs something to point at. | S4 constraint_register #7 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Recording why the capability offers an operation that reads every record | capability_side_effects | S4 gap_register GAP-1 |
| Recording that the change crossed an authority boundary | capability_side_effects | S4 gap_register GAP-2 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
