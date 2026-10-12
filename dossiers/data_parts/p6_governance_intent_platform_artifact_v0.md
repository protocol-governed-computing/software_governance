# Stage 6 — Governance Intent: platform / artifact
**Stage:** 6 — Governance Intent
**CR:** data_parts
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `artifact` — EXISTING — modified by this CR |
| Authority class | reuse existing — the platform declares how a declaration is read; no new actor type |
| Governing constitutions | `vocabulary::CONSTITUTION_VOCABULARY_V0`, `conformance::CONSTITUTION_TEST_DATA_V2` |

How a declaration is read belongs to the subdomain that already declares it. Vectors are what need a
data part; the reading is not theirs to declare. Nothing new stands on its own, so no subdomain is
declared.

**No domain artifact appears in the action registers below.** What any vector states is its domain's
business, and the vectors this change makes possible are authored in their own domains.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Declaring a part whose contents are values | artifact | OWNED | | S4 gap_register GAP-1 |
| Passing over a data part when finding references | artifact | OWNED | | S4 gap_register GAP-2 |
| Reading the new version wherever the vocabulary is read | artifact | OWNED | | S4 gap_register GAP-3 |
| Declaring any other part data | artifact | DEFERRED | | S4 authoring_scope deferred #1 |
| What any vector states | artifact | DEFERRED | | S4 authoring_scope deferred #2 |

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
| How a vocabulary's group is stated | artifact -> vocabulary | vocabulary::CONSTITUTION_VOCABULARY_V0 | SATISFIED | S4 dependency_graph #1 |
| How a vector's cases are read | conformance -> artifact | conformance::CONSTITUTION_TEST_DATA_V2 | GAP | S4 dependency_graph #2 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | Declares reference, explanation, set and history parts, and no part whose contents are values. | EXTEND | S4 gap_register GAP-1 |
| vocabulary::CONSTITUTION_VOCABULARY_V0 | Declares how a vocabulary's groups are stated; a new group is stated the same way. | REUSE | S4 dependency_graph #1 |
| conformance::CONSTITUTION_TEST_DATA_V2 | Declares what a vector states, and says nothing about how its cases are read for references. | REVIEW | S4 dependency_graph #2 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_DATA_PART_IS_DECLARED | A part is data only where the platform declares it so, by name. Inferring data would let a misspelled reference pass as a value. | S4 constraint_register #1 |
| OTHER_PARTS_ARE_UNCHANGED | A part outside a vector's cases is read exactly as it is today. | S4 constraint_register #2 |
| AN_UNDECLARED_NAME_IS_REFUSED | A name outside every declared part is still refused. | S4 constraint_register #3 |
| ONE_NAME_ONE_READING | A part's name means the same thing in every kind, so a data part is chosen by a name no kind reads as references. | S4 constraint_register #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Declaring a part whose contents are values | artifact | S4 gap_register GAP-1 |
| Passing over a data part when finding references | artifact | S4 gap_register GAP-2 |
| Reading the new version wherever the vocabulary is read | artifact | S4 gap_register GAP-3 |

---

## Gate 1 — Design Approval

**Gate 1 closes at this stage for this dossier.** The governance surface is authored, not
constructed, so this change is terminal at P6. Stages 0 through 6 are presented for review as a
body; approval authorizes authoring the vocabulary's next version, which declares the vector's cases
data, and the readers that read it.

Gate 2 has no subject here: no mandate is drafted, so there is none to lock.

**Status: CLOSED.** Approved by the business author against the composition `87c838e390b2…`, the
composition every grounded register of this dossier was re-read against and attested to in
`baseline.json`. The approval authorizes the authoring described above, and nothing else.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE — APPROVED |
