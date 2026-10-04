# Stage 4 — Business Model: platform / conformance

**Stage:** 4 — Business Model
**CR:** platform_test_data
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

This document consolidates Stages 1 to 3. It re-litigates nothing and introduces no design: every
row carries the prior-stage finding it came from, and every capability Stage 3 committed appears in
the capability graph exactly as Stage 3 stated it.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The platform | Decides what a vector is and what counts as proven, and supplies its own transforms and their vectors. | Declaring — the rules of proof, and the proof of its own code, are its to state. | S1 authority_boundaries #1 |
| The platform's build | Runs the platform's vectors against its transforms as sealed, on every build of every platform composition. | Deciding — a platform build with a failed case is not admitted. | S1 authority_boundaries #4 |
| The domain that supplies a transform | Proves its own transforms in its own build. | Deciding — a domain build with a failed case is not admitted. | S1 authority_boundaries #3 |
| A domain that carries a platform transform | Names the transform as carried and does not prove it. | Observing — the proof belongs to the supplier. | S1 authority_boundaries #5 |
| A reader of the composition | Sees which platform transforms were proven, by which build, and which were not. | Observing — the party an unproven transform reported as passing misleads. | S1 business_events #1 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Platform transform | A transform the platform declares and implements once. | Declared and sealed by each platform build; proven, unproven or refused by its vectors. | S2 entities Platform transform |
| Carried transform | A platform transform a domain uses and does not supply. | Copied into the domain's build, and recorded by the compiler as carried. | S3 analysis_findings #4 |
| Test vector | Stated inputs and the outputs a transform must produce from them. | For a platform transform, declared with the platform under the dossier that gates it, and compiled by each platform build. | S3 analysis_findings #1 |
| Inherited case | A case brought across from the reference implementation. | Kept, corrected or dropped when restated, with the reason for each correction and drop recorded. | S3 analysis_findings #6 |
| Platform conformance result | Every platform transform named proven, unproven or refused, with counts. | Written by each platform build and carried into the composition beside every domain's. | S3 analysis_findings #7 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The constitution governing vectors | Its new version, placing vectors in the supplier's build | S3 analysis_findings #1 |
| The platform's three build declarations | Their new versions, compiling vectors | S3 analysis_findings #2 |
| The reference implementation's vectors | Fifty-three cases for eleven platform transforms, restated and re-judged | S3 analysis_findings #6 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| The platform's transforms were proven | A platform build runs its vectors and all pass | What each platform transform does is evidence in the composition, proven by the build that supplies it | S1 business_events #1 |
| The platform was refused for a failed vector | A platform vector fails in a platform build | A platform transform that does not do what it says never enters a composition | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Platform vector | tests | Platform transform | Declare every platform vector against a transform the composition declares | S1 business_invariants #1 |
| Platform build | runs | Platform vector | Run every platform vector on every platform build | S1 business_invariants #2 |
| Build | is refused for | A failed case | Refuse any build with a failed case | S1 business_invariants #3 |
| Transform | is proven in | Its supplier's build | Prove a transform only where it is supplied | S1 business_invariants #4 |
| Inherited case | is re-judged against | The current transform | Keep, correct or drop each inherited case | S1 business_invariants #5 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| State that a transform's vectors run in its supplier's build, the platform's for its own transforms, and that the platform's vectors are authored under the dossier that gates them | S3 authoring_decisions State that a transform's vectors run in its supplier's build, the platform's for its own transforms, and that the platform's vectors are authored under the dossier that gates them | CRITICAL | GAP-01 | The constitution excludes the platform's build. |
| Compile the platform's vectors in every platform build, and declare where their cases are written | S3 authoring_decisions Compile the platform's vectors in every platform build, and declare where their cases are written | CRITICAL | GAP-02 | No platform build discovers vectors. |
| Run the platform's vectors after each platform build compiles, and stop the build on a failure | S3 authoring_decisions Run the platform's vectors after each platform build compiles, and stop the build on a failure | CRITICAL | GAP-03 | The platform's build step ends at the compile. |
| Tell a build's own transforms from carried ones by what the compiler carried in | S3 authoring_decisions Tell a build's own transforms from carried ones by what the compiler carried in | CRITICAL | GAP-04 | The runner tells them apart by name. |
| Refuse a build with any failed case, whoever supplies the transform | S3 authoring_decisions Refuse a build with any failed case, whoever supplies the transform | MAJOR | GAP-05 | A carried transform's failed case is admitted. |
| Bring the inherited vectors across, re-judged, with every correction and drop recorded | S3 authoring_decisions Bring the inherited vectors across, re-judged, with every correction and drop recorded | MAJOR | GAP-06 | No platform transform has a vector. |
| Carry the platform's result into the snapshot and check that it names every platform transform | S3 authoring_decisions Carry the platform's result into the snapshot and check that it names every platform transform | MINOR | GAP-07 | Carried already; the check asserts the opposite. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| conformance | conformance::CONSTITUTION_TEST_DATA_V1 | governance rule | GAP | S3 dependency_discoveries #1 |
| conformance | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | build declaration | GAP | S3 dependency_discoveries #2 |
| conformance | structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 | build declaration | GAP | S3 dependency_discoveries #3 |
| conformance | structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 | build declaration | GAP | S3 dependency_discoveries #4 |
| conformance | capability_transforms | transforms under test | SATISFIED | S3 dependency_discoveries #5 |
| conformance | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | transform left unproven | SATISFIED | S3 dependency_discoveries #6 |
| conformance | compiler | platform build step | GAP | S3 dependency_discoveries #8 |
| conformance | compiler | record of carried transforms | GAP | S3 dependency_discoveries #9 |
| conformance | execution | runner | GAP | S3 dependency_discoveries #10 |
| conformance | conformance | invariants in the platform's build | GAP | S3 dependency_discoveries #11 |
| conformance | composition | evidence check | GAP | S3 dependency_discoveries #12 |
| conformance | design | rendered vectors | GAP | S3 dependency_discoveries #13 |
| conformance | process | regression | GAP | S3 dependency_discoveries #14 |

The gaps land together: the constitution and build declarations first, then the vectors, the
compiler, the runner, the assembler's check and the design language, with the regression running them.

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Every platform vector tests a platform transform the composition declares. | S1 business_invariants #1 | invariant |
| 2 | Every platform vector runs on every build of the platform. | S1 business_invariants #2 | invariant |
| 3 | No build with a failed case is admitted. | S1 business_invariants #3 | invariant |
| 4 | A transform's vectors run in the build of its supplier and nowhere else. | S1 business_invariants #4 | invariant |
| 5 | No inherited case is kept as written only because it was inherited. | S1 business_invariants #5 | invariant |
| 6 | The platform governs every vector. | S1 constraints #1 | business policy |
| 7 | A vector belongs to whoever supplies the transform it tests. | S1 constraints #2 | business policy |
| 8 | The platform's build never proves a domain's transforms. | S1 constraints #4 | business policy |
| 9 | Each correction or drop of an inherited case is recorded with its reason. | S1 constraints #8 | business policy |
| 10 | No vector is invented for a platform transform the reference implementation never tested. | S1 constraints #9 | business policy |
| 11 | Lifting the vectors without running them is not an acceptable partial change. | S1 constraints #10 | business policy |
| 12 | A domain that carries a platform transform reports it as carried, unchanged. | S1 constraints #11 | business policy |
| 13 | A build's own transforms are told from carried ones by what the compiler carried in, never by name. | S3 analysis_findings #4 | governance rule |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions State that a transform's vectors run in its supplier's build, the platform's for its own transforms, and that the platform's vectors are authored under the dossier that gates them | State that a transform's vectors run in its supplier's build, the platform's for its own transforms, and that the platform's vectors are authored under the dossier that gates them | conformance | EXTEND |
| GAP-02 | S3 authoring_decisions Compile the platform's vectors in every platform build, and declare where their cases are written | Compile the platform's vectors in every platform build, and declare where their cases are written | structure | EXTEND |
| GAP-03 | S3 authoring_decisions Run the platform's vectors after each platform build compiles, and stop the build on a failure | Run the platform's vectors after each platform build compiles, and stop the build on a failure | execution | EXTEND |
| GAP-04 | S3 authoring_decisions Tell a build's own transforms from carried ones by what the compiler carried in | Tell a build's own transforms from carried ones by what the compiler carried in | execution | EXTEND |
| GAP-05 | S3 authoring_decisions Refuse a build with any failed case, whoever supplies the transform | Refuse a build with any failed case, whoever supplies the transform | execution | EXTEND |
| GAP-06 | S3 authoring_decisions Bring the inherited vectors across, re-judged, with every correction and drop recorded | Bring the inherited vectors across, re-judged, with every correction and drop recorded | conformance | NEW |
| GAP-07 | S3 authoring_decisions Carry the platform's result into the snapshot and check that it names every platform transform | Carry the platform's result into the snapshot and check that it names every platform transform | composition | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The constitution governing vectors gains a new version placing vectors in the supplier's build and admitting the platform's vectors authored under the dossier that gates them. | S3 analysis_findings #1 | The current version excludes the platform's build and requires every vector to come from a design. Decided by the business owner. | Every other rule stands unchanged. |
| 2 | Each of the platform's three build declarations gains a new version that compiles vectors and declares where their cases are written. | S3 analysis_findings #2 | Each composition states what it proved. Decided by the business author. | The platform's build never proves a domain's transforms. |
| 3 | Each platform build runs the runner after compiling and stops on a failure, handed the output place the build wrote. | S3 analysis_findings #3 | The same step a domain's build takes. | A placement build is proven where it wrote. |
| 4 | The compiler records which transforms a build carried in, and the runner reads that record. | S3 analysis_findings #4 | Carried copies are identical to the platform's. Decided by the business owner. | Ownership is never inferred from a name. |
| 5 | A build with any failed case is refused. | S3 analysis_findings #5 | A failed case that admits its build is the silence conformance exists to end. Decided by the business author. | Admission depends on every case, not only on what was classified. |
| 6 | The inherited vectors are restated by hand in the Machine block and re-judged by the platform's build; each correction and drop is recorded with its reason. | S3 analysis_findings #6 | Inheritance is not evidence. | No case is invented; the twelfth transform stays unproven. |
| 7 | The platform's result is carried as a domain's is, and the assembler's check requires it to name every platform transform. | S3 analysis_findings #7 | The assembler already carries it. | The platform's proof is part of the snapshot's identity. |
| 8 | Whether the invariants governing vectors run in the platform's own build is shown at delivery by a vector built to trip each. | S3 analysis_findings #9 | It is not settled by reading the composition. | A platform vector is never compiled unjudged. |

---

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| State that a transform's vectors run in its supplier's build, the platform's for its own transforms, and that the platform's vectors are authored under the dossier that gates them | GAP-01 |
| Compile the platform's vectors in every platform build, and declare where their cases are written | GAP-02 |
| Run the platform's vectors after each platform build compiles, and stop the build on a failure | GAP-03 |
| Tell a build's own transforms from carried ones by what the compiler carried in | GAP-04 |
| Refuse a build with any failed case, whoever supplies the transform | GAP-05 |
| Bring the inherited vectors across, re-judged, with every correction and drop recorded | GAP-06 |
| Carry the platform's result into the snapshot and check that it names every platform transform | GAP-07 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Vectors for ai_governance's own transforms | Their inherited cases disagree with the current implementations; that is ai_governance's question, in its own change |
| A vector for the platform transform no inherited case tests | None is invented here |
| How much proof is enough beyond the inherited cases | The inherited cases are the floor they were |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
