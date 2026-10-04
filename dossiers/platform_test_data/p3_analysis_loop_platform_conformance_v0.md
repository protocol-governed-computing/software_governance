# Stage 3 — Analysis Loop: platform / conformance

**Stage:** 3 — Analysis Loop
**CR:** platform_test_data
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every decision below is grounded in the pinned baseline
`d3e4fbf45009e0661bba3f964c1a026b41e9cbdb7d485973e74644d655ac05a8`, re-read at this stage rather
than inherited from Stage 2. Re-reading the constitution governing vectors overturned Stage 2's
judgement that it needs no change. Two questions could not be settled by evidence and were put to the
business owner: how that constitution is resolved, and how a build's own transforms are told from the
ones it carries. The business owner decided both at this stage.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| S2 architectural_observations #1 | The constitution governing vectors does not permit this change as it stands. It places a transform's vectors in the supplying domain's build and adds "never in the platform's own build"; and it says a vector is authored in the design and rendered by construction, while the platform's transforms, like the rest of the governance surface, are authored by hand under the dossier that gates them. A new version states that a transform's vectors run in its supplier's build, which for the platform's own transforms is the platform's build, and that the platform's vectors are authored under the dossier that gates them. Every other rule stands unchanged. | Stage 2's judgement that the constitution needs no change is overturned. | OBSERVED | HIGH | CLOSED | conformance::CONSTITUTION_TEST_DATA_V1, sections 4 and 5. Decided by the business owner at this stage. |
| S2 gaps #1 | Each of the platform's three build declarations gains a new version that discovers the vector kind, declares where runnable cases are written, and records that the platform proves its own transforms and never a domain's. The reason the current versions give, that implementation-layer conformance is out of scope, is narrowed to a domain's implementations. | All three platform builds compile the platform's vectors. | OBSERVED | HIGH | CLOSED | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1, structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 and structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 each list their discovered kinds without the vector kind. |
| S2 gaps #2 | The platform's build step runs the runner after its compile succeeds and stops on its failure, as a domain's build step does. A placement build writes to an output place of its own, so the runner is handed the place the build wrote rather than assuming the platform's. | The platform's vectors run on every build of every platform composition. | INFERRED | HIGH | CLOSED | A domain's build step already composes the compile and the runner. Carried forward to Stage 7: how the runner is told a placement build's output place. |
| S2 gaps #3 | A carried transform is copied into a domain's build byte for byte, and nothing in the build's output marks it as carried, so the runner can tell a build's own transforms from carried ones only by name — which names every platform transform carried in the platform's own build. The compiler already knows which transforms it carried in; it records them in the build's output, and the runner reads that record. A build's own transforms are those it declares and did not carry in. | The runner never infers ownership from a name, and every build is classified by the same fact. | OBSERVED | HIGH | CLOSED | Carried copies in ai_governance's build are identical to the platform's and bear the domain's layer. Decided by the business owner at this stage. Carried forward to Stage 7: the shape of the record. |
| S2 gaps #4 | Any failed case refuses the build that ran it, whoever supplies the transform the case tests. The runner stops classifying admission by what it judged and admits a build only when no case failed. | A failed case can no longer be run and ignored. | OBSERVED | HIGH | CLOSED | Decided by the business author at Stage 0. |
| S2 gaps #5 | Each inherited vector is restated by hand in the Machine block, named for its target by current identity, and each case is re-judged by the platform's own build: a case that fails is corrected where the current behaviour is intended, or dropped where it tests what is no longer declared, and each correction and drop is recorded with its reason in the delivery record. No case is invented, and the twelfth transform stays unproven. | The platform's vectors enter through the same judgement as any other, and what was changed from the inheritance is visible. | INFERRED | HIGH | CLOSED | Ten of the eleven transforms matched every inherited case in a read-only run. Carried forward to delivery: the record of corrections and drops. |
| S2 architectural_observations #3 | The assembler carries the platform's result with no change, under the platform's name, beside every domain's. Its evidence check, which asserts that no platform result exists, is reversed to assert that one does and names every platform transform. | The platform's proof is part of the snapshot's identity, as a domain's is. | INFERRED | HIGH | CLOSED | The assembler names no projection kind. |
| S2 discovery_concerns #2 | Recording carried transforms changes how every domain's result is classified, but not what it says: each domain's own transforms are those its namespace names today, and each carried transform is a platform transform today. | Every domain reports the same counts after the change as before it. | INFERRED | MEDIUM | CLOSED | Every carried transform in the composition is named capability_transforms, and no domain declares a transform in that namespace. |
| S3 dependency_discoveries #11 | Whether the invariants governing vectors run in the platform's own build is not settled by reading the composition: a domain build imports invariants by the kinds they apply to, and the platform's build asserts its own. | If they do not run, the platform's vectors compile unjudged by the rules written for them. | INFERRED | MEDIUM | CLOSED | Carried forward to delivery: shown by a platform vector built to trip each invariant. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| No platform transform has a vector in the composition. | S2 belief_verification #1 | CONFIRMED | Re-read at this stage: si.artifact.list --kind TEST_DATA answers NOT_FOUND. |
| The eleven platform transforms keep the codes the reference implementation's vectors name. | S2 belief_verification #2 | CONFIRMED | si.artifact.list --kind CT returns twenty-eight transforms, twelve in the capability_transforms namespace. |
| The platform's build does not discover vectors and declares no place for runnable cases. | S2 belief_verification #3 | CONFIRMED | None of the three platform build declarations names the vector kind or a conformance place. |
| The platform's build step does not run conformance. | S2 belief_verification #4 | CONFIRMED | The platform's build step ends with the compiler. |
| The runner takes a transform as a build's own only when its namespace is the build's scope. | S2 belief_verification #5 | CONFIRMED | The runner compares each transform's namespace with the build's scope, and admits a build when nothing it classified was refused. |
| The platform's conformance result would be carried into the snapshot as a domain's is. | S2 belief_verification #6 | CONFIRMED | The assembler copies every projection kind a build wrote. |
| The constitution governing vectors needs no change. | S2 pps_baseline_fqdns #1 | OVERTURNED | conformance::CONSTITUTION_TEST_DATA_V1 excludes the platform's own build and requires every vector to come from a design; resolved by S3 analysis_findings #1. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| conformance::CONSTITUTION_TEST_DATA_V1 | Constitution | EXTEND | A new version places vectors in the supplier's build and admits the platform's vectors authored under the dossier that gates them. |
| structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | Structure | EXTEND | A new version discovers vectors and declares where cases are written. |
| structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 | Structure | EXTEND | A new version discovers vectors and declares where cases are written. |
| structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 | Structure | EXTEND | A new version discovers vectors and declares where cases are written. |
| The eleven platform transforms with inherited vectors | Capability transform | REUSE | Tested as sealed; none changes. |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | Capability transform | EXISTING | No inherited vector; stays unproven. |
| Eleven vectors for the platform's transforms | Test vector | AUTHOR_NEW | None exists. |
| The platform's build step | Platform build | EXTEND | Runs the runner after the compile. |
| The compiler's record of what a build carried | Platform build | EXTEND | The compiler knows which transforms it carried in and records none of it. |
| The runtime's runner | Platform execution | EXTEND | Classifies by name and admits a build whose carried transform's case failed. |
| The invariants governing vectors in the platform's own build | Invariant | INVESTIGATE | Whether the platform's build asserts them against its own vectors is shown at delivery. |
| The assembler's evidence check | Platform composition | EXTEND | Asserts that no platform result exists. |
| The design language's rendering of a vector | Design language | EXTEND | Names the current version of the constitution in every vector it renders. |
| The regression and its runbook | Platform process | EXTEND | Record no platform result. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| conformance::CONSTITUTION_TEST_DATA_V1 | none | 0 | si.topology.impact impacted_count 0 — no vector exists to name it |
| structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | none | 0 | si.topology.impact impacted_count 0 — named by the build step, not by an artifact |
| structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 | none | 0 | si.topology.impact impacted_count 0 |
| structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 | none | 0 | si.topology.impact impacted_count 0 |

No transform, contract or workflow changes. Every domain builds as it does today and reports the same
counts; the platform's result is new, and names eleven transforms proven and one unproven.

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| State that a transform's vectors run in its supplier's build, the platform's for its own transforms, and that the platform's vectors are authored under the dossier that gates them | EXTEND | The constitution governing vectors excludes the platform's build and requires a design for every vector. | Keeping the constitution and proving the platform's transforms elsewhere was rejected: it proves code in a build that does not supply it. | S3 analysis_findings #1 |
| Compile the platform's vectors in every platform build, and declare where their cases are written | EXTEND | No platform build discovers vectors. | Proving them in the reference build only was rejected by the business author: each composition states what it proved. | S3 analysis_findings #2 |
| Run the platform's vectors after each platform build compiles, and stop the build on a failure | EXTEND | The platform's build step ends at the compile. | None: a vector compiled and never run is the dormancy the platform removed. | S3 analysis_findings #3 |
| Tell a build's own transforms from carried ones by what the compiler carried in | EXTEND | Carried copies are indistinguishable from the platform's by anything but their name. | Inferring it in the runner from the platform's compiled surface was rejected: the runner would read another build's output. | S3 analysis_findings #4 |
| Refuse a build with any failed case, whoever supplies the transform | EXTEND | The runner admits a build whose carried transform's case failed. | Leaving it was rejected by the business author: a failed case that admits its build is the silence conformance exists to end. | S3 analysis_findings #5 |
| Bring the inherited vectors across, re-judged, with every correction and drop recorded | AUTHOR_NEW | No platform transform has a vector, and eleven have inherited cases. | Trusting the inherited cases as written was rejected by the business author. | S3 analysis_findings #6 |
| Carry the platform's result into the snapshot and check that it names every platform transform | EXTEND | The assembler already carries it; its evidence check asserts the opposite. | None. | S3 analysis_findings #7 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | conformance | Vectors are already governed here; the change versions the constitution governing them and the platform's build declarations, and adds the platform's vectors. | S3 analysis_findings #1 · S1 governance_scope #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All three CRITICAL gaps carried from Stage 2 have an authoring decision: the platform's build declarations, its build step, and the runner's classification. |
| No open analyst questions | SATISFIED | The two findings put to the business owner were decided at this stage. |
| No dependency expansion in the last pass | SATISFIED | The dependency register closed at fourteen entries — one existing, one reused, ten extended, one authored, one to investigate — and re-reading the composition at this stage surfaced no further dependency. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Seven items re-verified; six CONFIRMED, one OVERTURNED and resolved by a new version of the constitution. |
| Every INFERRED finding promoted, accepted or carried forward with a reason | SATISFIED | Five findings stay INFERRED: one is carried forward to Stage 7, two to delivery, and two are accepted on the evidence given. |

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
