# Stage 6 — Governance Intent: platform / conformance

**Stage:** 6 — Governance Intent
**CR:** transform_conformance
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `conformance` — EXISTING — extended by this CR |
| Authority class | reuse existing — the platform states what a vector proves and what counts as proven, a domain proves its own transforms in its own build, a design states which vectors each transform has; no new actor type |
| Governing constitutions | `conformance::CONSTITUTION_TEST_DATA_V0`, replaced by a new version this change authors |

What a vector proves, where it runs and what counts as proven are conformance's concerns, so the
model belongs to the subdomain that governs vectors. The constitution governing them is replaced by a
new version; one artifact names it, and that artifact is itself replaced. The design language that
lets a design state a vector, and refuses a transform without one, belongs to the design subdomain.
The compiler's generation of cases, the runner, the assembler and the regression realize the model and
own no rule of it.

**No domain artifact appears in the action registers below.** A domain's build manifest gains a place
for its vectors in the domain's own change, when that change first gives a transform vectors; until
then the domain's transforms are reported unproven, which needs nothing declared. The conformance
workload that shows a molecule proven in a composition is the domain half of this change and is
scheduled by its own change once this one is delivered.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| State what a vector proves | conformance | OWNED | | S4 gap_register GAP-01 |
| Hold a vector's assertions to known forms by a check that runs | conformance | OWNED | | S4 gap_register GAP-02 |
| Refuse a vector whose recorded results do not match the purity of what it tests | conformance | OWNED | | S4 gap_register GAP-03 |
| Run every transform's vectors in its domain's build, on every build, and stop the build on a failure | conformance | OWNED | | S4 gap_register GAP-04 |
| Prove a molecule with a non-deterministic step by its recorded results | conformance | OWNED | | S4 gap_register GAP-05 |
| Report every transform proven, unproven or refused by name | conformance | OWNED | | S4 gap_register GAP-06 |
| Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | conformance | OWNED | | S4 gap_register GAP-07 |
| State vectors in a design, and refuse a transform authored or amended without one | design | OWNED | | S4 gap_register GAP-08 |
| Show a molecule with a non-deterministic step proven in a composition | conformance | OWNED | | S4 gap_register GAP-09 |
| Hold a vector's outputs to its transform, and each case to a declared outcome | conformance | SATISFIED | conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 | S4 capability_graph #3 |
| Vectors for each transform that already exists | conformance | DEFERRED | | S4 authoring_scope deferred #1 |
| What any transform does | conformance | DEFERRED | | S4 authoring_scope deferred #2 |
| How much proof is enough beyond one vector | conformance | DEFERRED | | S4 authoring_scope deferred #3 |
| Sealing the code a composition vouches for | conformance | DEFERRED | | S4 authoring_scope deferred #4 |

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
| A non-deterministic step's results are recorded, and a replay uses the record | conformance -> capability_transforms | capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | SATISFIED | S4 dependency_graph #3 |
| A molecule is run as its declared steps | conformance -> capability_transforms | capability_transforms::CONSTITUTION_MOLECULES_V0 | SATISFIED | S4 dependency_graph #4 |
| Conformance belongs in each domain's build, not the platform's | conformance -> structure | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | SATISFIED | S4 dependency_graph #5 |
| The design language that states a transform's vectors | conformance -> design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | GAP | S4 dependency_graph #10 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|------------------------------------------|----------------|
| conformance::CONSTITUTION_TEST_DATA_V0 | Admits deterministic outputs only, and says nothing of molecules, recorded results, where vectors run or what counts as proven. Replaced by a new version. | REPLACE | S3 analysis_findings #1 |
| conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | Claims enforcement by a compiler phase that does not exist; its assertion passes unconditionally. Replaced by a new version a compiler assertion enforces. | REPLACE | S3 analysis_findings #2 |
| conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 | Holds a vector's expected outputs to its transform's declared outputs. | REUSE | S4 dependency_graph #1 |
| capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 | Holds each case to a declared outcome. | REUSE | S4 dependency_graph #2 |
| capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | States that a replay uses a non-deterministic step's recorded result, which is what a molecule's vector does. | REUSE | S4 dependency_graph #3 |
| capability_transforms::CONSTITUTION_MOLECULES_V0 | States that a molecule is run as its declared steps, which is what a molecule's vector tests. | REUSE | S4 dependency_graph #4 |
| structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | Records that conformance belongs in each domain's build. Examined; unchanged. | REVIEW | S4 dependency_graph #5 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Admits a transform and no statement of its vectors. Its rule set is extended and re-sealed. | EXTEND | S4 dependency_graph #10 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| EVERY_VECTOR_TESTS_A_DECLARED_TRANSFORM | A vector names a transform the composition declares. | S4 constraint_register #1 |
| PROOF_IS_OF_WHAT_RUNS | A vector runs against the transform exactly as the composition sealed it; a molecule is run whole. | S4 constraint_register #2 |
| A_FAILED_VECTOR_STOPS_ITS_DOMAIN | A domain with a failed vector is not admitted to any composition. | S4 constraint_register #3 |
| PROVEN_OR_NAMED_UNPROVEN | Every transform is proven or named unproven; nothing is reported as passing that nothing tested. | S4 constraint_register #4 |
| RECORDED_RESULTS_MATCH_PURITY | A vector supplies recorded results for exactly the non-deterministic steps of what it tests, and none is run. | S4 constraint_register #5 |
| TWO_KINDS_OF_PROOF_KEPT_APART | Transform conformance evidence and composition conformance evidence are read and written in separate places. | S4 constraint_register #7 |
| PROVEN_WHERE_IMPLEMENTED | A domain's transforms are proven in that domain's own build, never in the platform's. | S4 constraint_register #8 |
| VECTORS_ARE_DESIGNED | Vectors are authored in the design; a transform authored or amended without one is refused at design. | S4 constraint_register #13 |
| EVERY_BUILD_PROVES_AGAIN | Every build runs every vector, and no earlier result stands for a later build. | S4 constraint_register #14 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| State what a vector proves | conformance | S4 gap_register GAP-01 |
| Hold a vector's assertions to known forms by a check that runs | conformance | S4 gap_register GAP-02 |
| Refuse a vector whose recorded results do not match the purity of what it tests | conformance | S4 gap_register GAP-03 |
| Run every transform's vectors in its domain's build, on every build, and stop the build on a failure | conformance | S4 gap_register GAP-04 |
| Prove a molecule with a non-deterministic step by its recorded results | conformance | S4 gap_register GAP-05 |
| Report every transform proven, unproven or refused by name | conformance | S4 gap_register GAP-06 |
| Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | conformance | S4 gap_register GAP-07 |
| State vectors in a design, and refuse a transform authored or amended without one | design | S4 gap_register GAP-08 |
| Show a molecule with a non-deterministic step proven in a composition | conformance | S4 gap_register GAP-09 |

---

## Gate 1 — Design Approval

**Gate 1 closes at this stage for this dossier.** The governance surface is authored, not
constructed, so this change is terminal at P6, and the gate that reviews a dossier as a body belongs
at the end of the dossier. Stages 0 through 6 are presented for review as a body; approval
authorizes the authoring of the new version of the constitution governing vectors, the replacement
of the invariant bound to a phase that does not exist, the invariant holding recorded results to
purity, the compiler's generation of cases and its assertion, the runner's recorded results and
report, the assembler's carrying of each domain's result, the regression's running of conformance on
every build, and the design language's statement of vectors and refusal of a transform without one.

Gate 2 has no subject here: no mandate is drafted, so there is none to lock.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`54412f835e6d…` — the same composition every grounded register of this dossier was re-read against
and attested to in `baseline.json`. What approval authorizes is the authoring described above, and
nothing else: a clause that appears in the governance surface beyond what this dossier argues for is
an ungoverned change, and the dossier is what that statement points at.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE — APPROVED |
