# Stage 6 — Governance Intent: platform / identity semantics

**Stage:** 6 — Governance Intent

**CR:** identity_semantics

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. The declaration belongs to the subdomain that governs identity.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Declare what carries no meaning | artifact | OWNED |  | S5 scope_boundary Declare what carries no meaning |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Governing the vocabulary | artifact -> vocabulary | vocabulary::CONSTITUTION_VOCABULARY_V0 | SATISFIED | S4 dependency_graph vocabulary::CONSTITUTION_VOCABULARY_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| vocabulary::CONSTITUTION_VOCABULARY_V0 | Present and reused unchanged | REUSE | S4 dependency_graph vocabulary::CONSTITUTION_VOCABULARY_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| ONE_PLACE_SAYS_WHAT_CARRIES_NO_MEANING | Only this vocabulary declares a part or a list that carries no meaning. | S4 design_decisions #1 |
| NAMED_ONLY_WHERE_TRUE_EVERYWHERE | A part or list is named only where every occurrence qualifies. | S4 design_decisions #2 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Declare what carries no meaning | artifact | S6 ownership Declare what carries no meaning |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
