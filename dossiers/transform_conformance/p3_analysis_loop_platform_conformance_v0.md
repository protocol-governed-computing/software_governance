# Stage 3 — Analysis Loop: platform / conformance

**Stage:** 3 — Analysis Loop
**CR:** transform_conformance
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every decision below is grounded in the pinned baseline
`54412f835e6df27975d3692fb2eb09ab9ada37221129811892b12c3a335479f9`, re-read at this stage rather
than inherited from Stage 2. Two questions could not be settled by evidence and are put to the business
owner: how a transform authored after this change is told from one that already exists, and where the
evidence for this change comes from when the platform itself composes no molecule. The business owner
decided both at this stage.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| S2 discovery_concerns #1 | The constitution governing vectors is named by one artifact only — the invariant bound to a compiler phase that does not exist — and by no vector, because none exists. A new version supersedes it at the cost of re-pointing that one invariant, which is itself replaced. The new version states that a vector tests a transform as sealed, that a molecule is tested whole, that a vector supplies the recorded results of exactly the non-deterministic steps of what it tests, that a vector for a non-deterministic step on its own asserts shape and never values, and that a transform no vector tests is unproven rather than passing. | A new version, not a sibling: unlike the constitution governing transforms, nothing is disturbed by replacing it. | OBSERVED | HIGH | CLOSED | si.topology.impact reports conformance::CONSTITUTION_TEST_DATA_V0 reaching one artifact, conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0. |
| S2 discovery_concerns #2 | The invariant holding a vector's assertions to known forms claims enforcement by a compiler phase that does not exist, and the assertion bound to it passes unconditionally. It is replaced by a new version enforced by a compiler assertion that reads each vector's assertions and refuses an unknown mode or type. | The last rule over vectors that could not refuse can refuse. | OBSERVED | HIGH | CLOSED | The compiler declares no phase of that name; the assertion bound to the invariant returns PASSED without reading an artifact. |
| S2 discovery_concerns #3 | Nothing records when a transform was authored, so the build cannot tell a new transform from an existing one. The design can: every transform authored or amended after this change enters the composition through a design, the one path by which domain artifacts are authored. So a design authoring or amending a transform without a vector is refused at Design Intent, and at build every transform without a vector is reported unproven by name. No list of existing transforms is kept, and none is needed. | The refusal happens where the transform is authored; the build reports and never grandfathers. | INFERRED | HIGH | CLOSED | The design language already refuses a transform without an implementation binding; a vector is refused by the same kind of rule. Decided by the business owner at this stage. |
| S2 discovery_concerns #4 | The runner reads cases from each domain's own build output, at a place the domain's build manifest declares, rather than from the snapshot's conformance place. The assembler carries each domain's conformance result into the composition as evidence of its own, apart from composition conformance, whose place is unchanged. | No reader of a sealed release sees its composition evidence move. | INFERRED | HIGH | CLOSED | Carried forward to Stage 7: the places, named in the build manifest and the snapshot layout. |
| S2 gaps #1 | Conformance runs in each domain's build, after the domain compiles and before it is assembled, as a step of the build. The runner belongs to the runtime and the compiler never imports it, so the build invokes the runner as its own step, the way the reference implementation's build did. A failed vector stops the build and the domain is never assembled. | Conformance is where the platform's build manifest said it belongs, and the layer separation holds. | INFERRED | HIGH | CLOSED | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 records where conformance belongs; the reference implementation's build invoked the runner as a step after compiling. Carried forward to Stage 7: the build step. |
| S2 gaps #6 | A vector for a molecule states, for each non-deterministic step, the result it is recorded as having produced, addressed the way the runtime addresses a step inside a molecule. The runner hands them to the executor, which already substitutes a recorded result and refuses a missing one; the runner confirms every supplied step was substituted and none was run. | A molecule with a non-deterministic step is proven exactly, and every such vector is also a proof of replay. | OBSERVED | HIGH | CLOSED | The executor accepts recorded results and marks each substituted step; the runner passes none today. |
| S2 gaps #3 | A domain's conformance result names every transform proven, unproven or refused, with counts, and never reports success over nothing. The rules over vectors keep judging vectors; the claim a reader relies on is the result, which names what was not judged. A new invariant refuses a vector whose recorded results do not match the purity of the steps it tests. | "Conformant" stops being a word that can be true of a domain with no proof. | INFERRED | HIGH | CLOSED | The runner already refuses to report a run in which no case ran. Carried forward to Stage 7: the shape of the result. |
| S2 gaps #7 | The new version of the constitution states the model; the existing invariants holding a vector to its transform's outputs and to a declared outcome stand unchanged, because they are correct for every vector they judge. | Two invariants are reused as they are. | OBSERVED | HIGH | CLOSED | conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 and capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 each judge a vector correctly when one exists. |
| S2 gaps #2 | A design states vectors in a register of its own, one row per case, and construction renders each transform's vectors as one declaration. The design language refuses a transform authored or amended without one. | Vectors travel the governed path; no vector is written by hand. | INFERRED | HIGH | CLOSED | Carried forward to Stage 7: the register's shape and the renderer. |
| S1 constraints #10 | The platform composes no molecule, so the evidence that a molecule with a non-deterministic step is proven in a composition cannot come from the platform's own declarations. The platform's conformance workloads exist to prove the platform: the evidence arrives with their next change, designed through the extended language with vectors from the start, and this change's delivery proves the mechanism in the compiler's and runtime's own tests. The domain that needs non-determinism supplies none of it. | The evidence is independent of any domain that needs it, and arrives through the governed path rather than by hand. | INFERRED | HIGH | CLOSED | No conformance workload carries a molecule or a vector today. Decided by the business owner at this stage. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| No transform in the composition has a vector. | S2 belief_verification #1 | CONFIRMED | Re-read at this stage: si.artifact.list --kind TEST_DATA answers NOT_FOUND. |
| The invariants governing vectors report success over no vectors. | S2 belief_verification #2 | CONFIRMED | Two assertions skip every artifact that is not a vector; the third passes unconditionally. |
| No domain build declares conformance. | S2 belief_verification #3 | CONFIRMED | None of the six domain build manifests declares a vector layer or a place for cases. |
| The design language cannot state a vector. | S2 belief_verification #4 | CONFIRMED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 declares no register for one. |
| The runner and composition conformance read and write the same place. | S2 belief_verification #5 | CONFIRMED | The pinned snapshot's conformance place holds only composition evidence. |
| The runner cannot supply recorded results to a non-deterministic step. | S2 belief_verification #6 | CONFIRMED | The runner executes each case with its inputs alone. |
| The constitution governing vectors says a transform produces its outputs deterministically. | S2 belief_verification #7 | CONFIRMED | conformance::CONSTITUTION_TEST_DATA_V0, section 1. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| conformance::CONSTITUTION_TEST_DATA_V0 | Constitution | EXTEND | Superseded by a new version stating the model for molecules, recorded results and what counts as proven. |
| conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | Invariant | EXTEND | Superseded by a new version enforced by a compiler assertion that exists. |
| conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 | Invariant | REUSE | Correct for every vector it judges. |
| capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 | Invariant | REUSE | Correct for every vector it judges. |
| capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | Constitution | REUSE | A vector supplying recorded results is a replay on its own terms. |
| capability_transforms::CONSTITUTION_MOLECULES_V0 | Constitution | REUSE | A molecule is run as its declared steps, which is what a vector tests. |
| structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | Structure | EXISTING | The decision that conformance belongs in each domain's build stands. |
| An invariant holding a vector's recorded results to the purity of the steps it tests | Invariant | AUTHOR_NEW | Nothing checks it. |
| Each domain's build manifest | Structure | EXTEND | Declares no vector layer and no place for cases. |
| The compiler's generation of runnable cases | Platform build | EXTEND | Binds a case to the sealed transform and carries no recorded results. |
| The runtime's runner | Platform execution | EXTEND | Supplies no recorded results and reads the composition's evidence place. |
| The assembler | Platform composition | EXTEND | Carries no domain conformance result. |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 and the renderer | Design language | EXTEND | Cannot state or render a vector, and refuses no transform without one. |
| The regression | Platform process | EXTEND | Runs no domain's conformance. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| conformance::CONSTITUTION_TEST_DATA_V0 | conformance | 1 | si.topology.impact impacted_count 1 — the invariant that is itself replaced |
| conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | none | 0 | si.topology.impact impacted_count 0 |
| conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 | none | 0 | si.topology.impact impacted_count 0 — reused unchanged |
| capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 | none | 0 | si.topology.impact impacted_count 0 — reused unchanged |
| structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | none | 0 | si.topology.impact impacted_count 0 — read, never modified |
| workload::STRUCTURE_BUILD_WORKLOAD_CONFIG_V0 | none | 0 | si.topology.impact impacted_count 0 — gains a vector layer in its domain's own change |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | none | 0 | si.topology.impact impacted_count 0 — its rule set is extended and re-sealed |

No transform, contract or workflow changes. Every domain builds as it does today, and its conformance
result names each of its transforms unproven until a change of its own gives them vectors.

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| State what a vector proves: a transform as sealed, a molecule whole, recorded results for exactly its non-deterministic steps, shape alone for a non-deterministic step on its own, and unproven where nothing tests | EXTEND | The constitution governing vectors admits deterministic outputs only, and one artifact names it. | A sibling constitution was rejected: unlike the constitution governing transforms, replacing this one disturbs nothing. | S3 analysis_findings #1 |
| Hold a vector's assertions to known forms by a check that runs | EXTEND | The invariant claims a compiler phase that does not exist. | Leaving it was rejected: a rule that cannot refuse is the defect this change removes. | S3 analysis_findings #2 |
| Hold a vector's outputs to its transform, and each case to a declared outcome | REUSE | Both are correct for every vector they judge. | None needed. | S3 analysis_findings #8 |
| Refuse a vector whose recorded results do not match the purity of the steps it tests | AUTHOR_NEW | A vector supplying a result for a deterministic step, or omitting one for a non-deterministic step, proves nothing about what it tests. | Leaving it to the runner was rejected: a mismatch is a defect in the declaration and is refused when the domain compiles. | S3 analysis_findings #7 |
| Run every transform's vectors in its domain's build, and stop the build on a failure | EXTEND | Where the platform's build manifest said conformance belongs. | Restoring it to the platform's build was rejected at P0. | S3 analysis_findings #5 |
| Prove a molecule with a non-deterministic step by supplying its recorded results, and confirm the step was not run | EXTEND | The executor already substitutes recorded results; the runner only has to pass them and check. | A separate replay test per molecule was rejected: it is the bespoke proof this change replaces. | S3 analysis_findings #6 |
| Report every transform proven, unproven or refused by name, never success over nothing | EXTEND | The runner already refuses a run in which nothing ran; the result says what was not judged. | Refusing every domain whose transforms have no vectors was rejected at P0. | S3 analysis_findings #7 |
| Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | EXTEND | The two collide today, and no result is carried. | Moving composition evidence was rejected: a sealed release's reader would see it move. | S3 analysis_findings #4 |
| State vectors in a design and render them, and refuse a transform authored or amended without one | EXTEND | Vectors must travel the governed path, and the design is where a new transform can be told from an existing one. | Refusing at build was rejected: nothing records when a transform was authored. A declared list of exempt transforms was rejected: a list kept by hand is a second record of what the composition already says. | S3 analysis_findings #3 |
| Show a molecule with a non-deterministic step proven in a composition | AUTHOR_NEW | No composition carries a molecule, and the evidence must come from no domain that needs it. | Writing the evidence by hand beside the platform was rejected: it is proof nobody gated. | S3 analysis_findings #10 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | conformance | Vectors are already governed here; the change replaces the constitution governing them and one invariant, adds one invariant, and changes no transform. | S3 analysis_findings #1 · S1 governance_scope #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All four CRITICAL gaps carried from Stage 2 have an authoring decision: the domain build, the design language, the rules that pass on nothing, and recorded results in the runner. |
| No open analyst questions | SATISFIED | The two findings put to the business owner were decided at this stage. |
| No dependency expansion in the last pass | SATISFIED | The dependency register closed at fourteen entries — one existing, four reused, eight extended, one authored — and re-reading the composition at this stage surfaced no further dependency. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Seven items re-verified against the composition, all CONFIRMED, none OVERTURNED. |
| Every INFERRED finding promoted, accepted or carried forward with a reason | SATISFIED | Six findings stay INFERRED: two were decided by the business owner, four are carried forward to Stage 7 — the places, the build step, the shape of the result, and the register. |

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
