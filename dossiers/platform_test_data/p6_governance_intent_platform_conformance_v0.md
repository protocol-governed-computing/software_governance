# Stage 6 — Governance Intent: platform / conformance

**Stage:** 6 — Governance Intent
**CR:** platform_test_data
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `conformance` — EXISTING — extended by this CR |
| Authority class | reuse existing — the platform governs every vector and supplies its own transforms' vectors, the platform's build proves them, a domain proves its own transforms in its own build; no new actor type |
| Governing constitutions | `conformance::CONSTITUTION_TEST_DATA_V1`, succeeded by a new version this change authors |

Where a transform's vectors run, and whose they are, are conformance's concerns, so the rule belongs to
the subdomain that governs vectors. What a platform build discovers and where it writes its cases are
structure's concerns, so the platform's three build declarations gain new versions there. The
platform's vectors belong to conformance beside the constitution that governs them. The compiler's
build step and record of carried transforms, the runner, the assembler's check and the regression
realize the rule and own none of it.

**No domain artifact appears in the action registers below.** Every domain builds as it does today and
reports the same counts; only the platform's result is new.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| State that a transform's vectors run in its supplier's build | conformance | OWNED | | S4 gap_register GAP-01 |
| Compile the platform's vectors in every platform build | structure | OWNED | | S4 gap_register GAP-02 |
| Run the platform's vectors after each platform build compiles | conformance | OWNED | | S4 gap_register GAP-03 |
| Tell a build's own transforms from carried ones by what the compiler carried in | conformance | OWNED | | S4 gap_register GAP-04 |
| Refuse a build with any failed case | conformance | OWNED | | S4 gap_register GAP-05 |
| Bring the inherited vectors across, re-judged | conformance | OWNED | | S4 gap_register GAP-06 |
| Carry the platform's result into the snapshot and check it | conformance | OWNED | | S4 gap_register GAP-07 |
| Vectors for ai_governance's own transforms | conformance | DEFERRED | | S4 authoring_scope deferred #1 |
| A vector for the platform transform no inherited case tests | conformance | DEFERRED | | S4 authoring_scope deferred #2 |
| How much proof is enough beyond the inherited cases | conformance | DEFERRED | | S4 authoring_scope deferred #3 |

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
| The platform's reference build compiles its vectors | conformance -> structure | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | GAP | S4 dependency_graph #2 |
| The platform's federated build compiles its vectors | conformance -> structure | structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 | GAP | S4 dependency_graph #3 |
| The platform's multi-worker build compiles its vectors | conformance -> structure | structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 | GAP | S4 dependency_graph #4 |
| The transforms the platform's vectors test | conformance -> capability_transforms | capability_transforms::CT_PURE_LOOKUP_V0 | SATISFIED | S4 dependency_graph #5 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|------------------------------------------|----------------|
| conformance::CONSTITUTION_TEST_DATA_V1 | Places vectors in the supplying domain's build "never in the platform's own", and requires every vector to come from a design. Succeeded by a new version. | REPLACE | S3 analysis_findings #1 |
| structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | Discovers no vectors and declares no place for cases. Succeeded by a new version. | REPLACE | S3 analysis_findings #2 |
| structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 | Discovers no vectors and declares no place for cases. Succeeded by a new version. | REPLACE | S3 analysis_findings #2 |
| structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 | Discovers no vectors and declares no place for cases. Succeeded by a new version. | REPLACE | S3 analysis_findings #2 |
| capability_transforms::CT_EXEC_EMIT_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_EXTRACT_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_FILTER_RECORDS_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_GENERATE_ID_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_LOOKUP_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_MAP_RESULT_TO_HTTP_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_PASSTHROUGH_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | Tested as sealed by a platform vector; unchanged. | REUSE | S4 dependency_graph #5 |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | No inherited case; examined and left unproven. | REVIEW | S4 dependency_graph #6 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| EVERY_PLATFORM_VECTOR_TESTS_A_DECLARED_TRANSFORM | A platform vector names a platform transform the composition declares. | S4 constraint_register #1 |
| EVERY_PLATFORM_BUILD_PROVES_AGAIN | Every platform vector runs on every build of the platform. | S4 constraint_register #2 |
| NO_FAILED_CASE_ADMITS_ITS_BUILD | A build with a failed case is not admitted, whoever supplies the transform the case tests. | S4 constraint_register #3 |
| PROVEN_WHERE_SUPPLIED | A transform's vectors run in its supplier's build and nowhere else. | S4 constraint_register #4 |
| INHERITANCE_IS_NOT_EVIDENCE | No inherited case is kept as written only because it was inherited; each correction and drop is recorded with its reason. | S4 constraint_register #5 |
| THE_PLATFORM_PROVES_ONLY_ITS_OWN | The platform's build never proves a domain's transforms. | S4 constraint_register #8 |
| OWNERSHIP_IS_RECORDED_NOT_NAMED | A build's own transforms are told from carried ones by what the compiler carried in, never by name. | S4 constraint_register #13 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| State that a transform's vectors run in its supplier's build | conformance | S4 gap_register GAP-01 |
| Compile the platform's vectors in every platform build | structure | S4 gap_register GAP-02 |
| Run the platform's vectors after each platform build compiles | conformance | S4 gap_register GAP-03 |
| Tell a build's own transforms from carried ones by what the compiler carried in | conformance | S4 gap_register GAP-04 |
| Refuse a build with any failed case | conformance | S4 gap_register GAP-05 |
| Bring the inherited vectors across, re-judged | conformance | S4 gap_register GAP-06 |
| Carry the platform's result into the snapshot and check it | conformance | S4 gap_register GAP-07 |

---

## Gate 1 — Design Approval

**Gate 1 closes at this stage for this dossier.** The governance surface is authored, not
constructed, so this change is terminal at P6, and the gate that reviews a dossier as a body belongs
at the end of the dossier. Stages 0 through 6 are presented for review as a body; approval
authorizes the authoring of the new version of the constitution governing vectors, the new versions
of the platform's three build declarations, the platform's eleven vectors restated from the
reference implementation and re-judged, the platform's build step running conformance, the
compiler's record of carried transforms, the runner's classification by that record and its refusal
of any failed case, the assembler's check of the platform's result, and the regression's running of
it.

Gate 2 has no subject here: no mandate is drafted, so there is none to lock.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`d3e4fbf45009…` — the same composition every grounded register of this dossier was re-read against
and attested to in `baseline.json`. What approval authorizes is the authoring described above, and
nothing else: a clause that appears in the governance surface beyond what this dossier argues for is
an ungoverned change, and the dossier is what that statement points at.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE — APPROVED |
