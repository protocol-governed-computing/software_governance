# Stage 6 — Governance Intent: platform / reference semantics

**Stage:** 6 — Governance Intent

**CR:** reference_semantics

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. What names another artifact belongs to the subdomain that governs identity, beside what carries no meaning.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Declare what names another artifact | artifact | OWNED | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | S5 scope_boundary Declare what names another artifact |

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
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | Present; names no reference | REPLACE | S4 design_decisions #7 |
| vocabulary::CONSTITUTION_VOCABULARY_V0 | Present and reused unchanged | REUSE | S4 dependency_graph vocabulary::CONSTITUTION_VOCABULARY_V0 |
| artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 | Present; its obligation is unchanged, and its check reads the declaration | REUSE | S4 dependency_graph artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 |
| artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0 | Present; its obligation is unchanged, and its check reads the declaration | REUSE | S4 dependency_graph artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS | Only this vocabulary declares a part that names another artifact; every check that finds a reference reads it. | S4 design_decisions #1 |
| ONE_ENFORCER_PER_RULE | A short code in a part that requires a full name is refused by one obligation, reading the declaration. | S4 design_decisions #2 |
| NAMED_ONLY_WHERE_TRUE_EVERYWHERE | A part is named a reference only where every full name beneath it names an artifact. | S4 design_decisions #3 |
| RULES_ARE_NAMED | A rule a comparison applies is a named entry, never only prose. | S4 design_decisions #6 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Declare what names another artifact | artifact | S6 ownership Declare what names another artifact |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
