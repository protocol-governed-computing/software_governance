# Stage 3 — Analysis Loop: platform / capability_transforms

**Stage:** 3 — Analysis Loop
**CR:** molecule_composition
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every decision below is grounded in the pinned baseline
`1b0cfbd3d094b7e93a965135c32b9f94ba8c3c43c0a1e8e8aacac8ebbdc9d010`, re-read at this stage rather
than inherited from Stage 2. One question could not be settled by evidence and was decided by the
business owner: how the rule that every transform is pure is replaced without re-authoring the
transforms that already exist.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| S2 discovery_concerns #1 | The constitution governing transforms states that every transform is pure, and it is named as governing by every transform the composition carries. Replacing it would require every one of them to name its replacement, because a superseded artifact may not be referenced. The rule was never wrong for the transforms that exist; it was written for one kind and phrased for all. The business owner decided that the platform grows by adding, not by re-authoring what exists: the existing constitution stays unchanged and keeps governing every existing transform, and two sibling constitutions govern what it does not describe — one for molecules, one for atoms that declare their result is not determined by their inputs. | No existing artifact changes. Three constitutions govern transforms, each for one concern, and an invariant places every transform under exactly one of them. | OBSERVED | HIGH | CLOSED | si.topology.impact reports 83 artifacts reached from capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 across four namespaces; artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 applies to every transform. Decided by the business owner at this stage. |
| S2 discovery_concerns #1 | Two kinds are already governed by more than one constitution, and transforms already are by two. A sibling constitution is an established shape, not a new one. | The sibling constitutions need no change to how the compiler dispatches governance. | OBSERVED | HIGH | CLOSED | Transforms are governed by capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 and by the authority-governance constitution; workflows and capability contracts by three each. |
| S2 discovery_concerns #1 | Once siblings exist, the existing constitution's statement that every transform is pure overstates its scope. Renaming it to say what it governs would supersede it and re-point every transform, which the business owner's rule excludes. The accurate name is deferred to the constitution's next version, made for its own reasons, and each sibling states the partition explicitly in the meantime. | The overstatement is visible and explained where it is read, and corrected without a ripple. | OBSERVED | HIGH | CLOSED | Carried forward: the next version of capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 is named for deterministic atoms. |
| S2 discovery_concerns #2 | Stating molecules and declared non-determinism in sibling constitutions supersedes nothing, so no artifact must be accounted for. | The version question dissolves. | OBSERVED | HIGH | CLOSED | See S3 analysis_findings #1. |
| S2 discovery_concerns #3 | Each step a molecule runs leaves one record naming its results and not their values, as a governed operation's steps already do. The records add volume, never compared values. | Accepted by the business owner: a loop of many passes leaves a record per step per pass. | OBSERVED | HIGH | CLOSED | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 classifies step evidence; the business owner accepted the volume at P0. |
| S2 discovery_concerns #4 | The one transform declaring that it emits a final value passes its input through unchanged, so its result is determined by its input. It is a deterministic atom and stays under the existing constitution. | No existing transform changes constitution. | OBSERVED | HIGH | CLOSED | The implementation named by capability_transforms::CT_EXEC_EMIT_V0 returns its input value unchanged. |
| S2 gaps #7 | Evidence for a step inside a molecule is written by the runtime as the step runs, in the same form as a governed operation's step evidence. | The runtime extension carries it; no new evidence kind is declared. | INFERRED | HIGH | CLOSED | Carried forward to Stage 7: the runtime's evidence writer gains a record per molecule step. |
| S2 gaps #8 | The end-to-end evidence is a composed transform with a loop whose body is itself a molecule, designed through the extended design language, constructed, compiled and run, as part of the platform's own conformance workloads. It uses no language model and belongs to no business domain. | The path is shown to hold by evidence independent of the domain that found the gap. | INFERRED | HIGH | CLOSED | Carried forward to Stage 7: its placement among the conformance workloads. |
| S1 constraints #8 | The four halves land together: the governing rules, the compiler's checks, the runtime, and the design language with construction. | No partial state is delivered in which a molecule runs but cannot be designed, or can be designed but not run. | OBSERVED | HIGH | CLOSED | Stated by the business author at P0. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| Every transform in the composition is an atom. | S2 belief_verification #1 | CONFIRMED | Re-read at this stage: si.artifact.list --kind CT returns twenty-eight transforms, each declared ct_kind atom. |
| Nothing governing states how a molecule runs. | S2 belief_verification #2 | CONFIRMED | Re-read at this stage: execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0 exempts molecules and states nothing about how their steps run. |
| The design language cannot state a molecule's steps, and the renderer cannot write them. | S2 belief_verification #3 | CONFIRMED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 declares a transform's kind and no register for its steps. |
| The runtime cannot run a composed step. | S2 belief_verification #4 | CONFIRMED | The compiler's loop shape raises CTExecutionError "CT-IR step missing handler_ref" when run. |
| Nothing reads a transform's declared purity. | S2 belief_verification #5 | CONFIRMED | No compiler, runtime or inspector source reads ct_purity. |
| The constitution governing transforms requires every transform to be pure and deterministic, and nothing enforces determinism. | S2 belief_verification #6 | CONFIRMED | capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 is checked for raised business outcomes only. |
| A repeated computation exists that hides its decisions inside one atom. | S2 belief_verification #7 | CONFIRMED | workload::CT_PURE_COLLATZ_STEP_V0 computes a whole sequence inside one atom. |
| The design language already anticipates a molecule by kind. | S2 architectural_observations #3 | CONFIRMED | Its implementation binding declares a kind of atom or molecule. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | Constitution | EXISTING | Unchanged; keeps governing every existing transform. |
| capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 | Invariant | REUSE | Every atom still returns its outcomes rather than raising them, whatever its determinism. |
| execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0 | Invariant | REUSE | Already requires an atom's implementation and exempts molecules. |
| capability_transforms::INVARIANT_CT_SURFACE_CLOSED_V1 | Invariant | REUSE | Every transform's surface stays closed. |
| workflow::CONSTITUTION_WORKFLOW_V0 | Constitution | EXISTING | Acts stay acyclic. |
| A constitution for molecules | Constitution | AUTHOR_NEW | Nothing states how a molecule runs. |
| A constitution for atoms declaring they are not deterministic | Constitution | AUTHOR_NEW | Nothing admits one lawfully. |
| Invariants holding a composition to both, and placing each transform under exactly one constitution | Invariant | AUTHOR_NEW | Nothing enforces a molecule's rules, its purity against its steps, or which constitution governs a transform. |
| The compiler's checks at build | Platform build | EXTEND | Lowers molecules today and confirms nothing about them. |
| The runtime's execution of transforms and its step evidence | Platform execution | EXTEND | Dispatches only single implementations and writes no evidence inside a transform. |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 and the renderer's transform builder | Design language | EXTEND | Anticipates a molecule by kind and cannot state or render its steps. |
| A conformance workload exercising a molecule end to end | Conformance evidence | AUTHOR_NEW | No conformance evidence exercises a molecule. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | ai_governance, blockchain, book_library_mgmt, capability_transforms | 83 | si.topology.impact impacted_count 83 — left unchanged, so none is disturbed |
| capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 | none | 0 | si.topology.impact impacted_count 0 |
| execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0 | none | 0 | si.topology.impact impacted_count 0 |
| capability_transforms::INVARIANT_CT_SURFACE_CLOSED_V1 | none | 0 | si.topology.impact impacted_count 0 |
| workflow::CONSTITUTION_WORKFLOW_V0 | workflow | 1 | si.topology.impact impacted_count 1 — read, never modified |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | none | 0 | si.topology.impact impacted_count 0 — its rule set is extended and re-sealed |
| capability_transforms::CT_EXEC_EMIT_V0 | none | 0 | si.topology.impact impacted_count 0 — examined, stays deterministic |

No existing transform, contract or workflow changes. The compiler and runtime extensions add checks and
execution for a kind of transform none of them carries, so nothing that builds or runs today behaves
differently.

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Keep governing every existing transform as deterministic | REUSE | Every existing transform is a deterministic atom, and the rule is right for them. | Superseding it with a new version, and renaming it, were examined and rejected: either forces every existing transform to name its replacement. | S3 analysis_findings #1 |
| State how a molecule runs: declared step order, one pass per member of the loop's collection, no molecule containing itself, a molecule's declared purity checked against its steps | AUTHOR_NEW | Nothing states it, and a molecule is a concern of its own. | Folding it into the existing constitution was rejected: it cannot change without a new version. One sibling for both new concerns was rejected: it repeats the conflation that caused this. | S3 analysis_findings #1 |
| Admit an atom that declares its result is not determined by its inputs, and forbid it side effects | AUTHOR_NEW | A computation such as a language model's offer of next words must be declarable lawfully, at exactly the step where determinism ends. | Treating it as a side effect was rejected at P0: a side effect cannot run inside a transform's loop. | S3 analysis_findings #1 |
| Place every transform under exactly one of the three constitutions by its kind and declared purity | AUTHOR_NEW | Three constitutions govern transforms; which one governs a given transform must be decided by what it declares, not by convention. | Leaving placement to each design was rejected: a transform could name the wrong constitution and escape its rules. | S3 analysis_findings #2 |
| Hold every atom to returning its outcomes | REUSE | Unaffected by determinism. | capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 satisfies it as-is. | S2 pps_baseline_fqdns Holds an atom to returning its outcomes |
| Require an atom's implementation and exempt a molecule | REUSE | Already stated by the invariant requiring an admissible implementation, which exempts molecules. | The existing implementation-admissibility invariant satisfies it as-is. | S2 pps_baseline_fqdns Requires an atom's implementation |
| Refuse at build a molecule whose steps or loop body cannot be run, one that contains itself, or one declared pure with a step that is not | EXTEND | The compiler already lowers molecules and must now confirm them. | Refusing at run time was rejected: a molecule that cannot keep its declaration must never enter a composition. | S2 gaps #5 |
| Run a molecule's steps in order, including a composed body once per pass of a loop, carrying values between passes | EXTEND | The runtime already runs loops over single implementations. | None: this is the only execution path the platform has. | S2 gaps #6 |
| Write one evidence record per step a molecule runs, naming its results and not their values | EXTEND | The runtime already writes step evidence for governed operations. | One record per molecule was rejected at P0: a decision inside a molecule would not be observable when made. | S3 analysis_findings #7 |
| State a molecule's steps, loop and emission in a design, and render them at full determinacy | EXTEND | The design language already anticipates a molecule by kind. | Hand-writing a molecule outside the design path was rejected: construction is the governed path. | S2 gaps #4 |
| Show the path holds with a composed transform designed, constructed, compiled and run end to end | AUTHOR_NEW | No conformance evidence exercises a molecule, and the domain that found the gap must not supply it. | Using the domain's own molecule was rejected at P0. | S3 analysis_findings #8 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | capability_transforms | Transforms are already governed here; the change adds two sibling constitutions and the invariants that place and hold transforms under them, and changes nothing that exists. | S3 analysis_findings #1 · S1 governance_scope #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All six CRITICAL gaps carried from Stage 2 have an authoring decision: the molecule constitution, the non-deterministic atom constitution, placement and enforcement, the design language and construction, the compiler's checks, and the runtime. |
| No open analyst questions | SATISFIED | Stage 2 carried none. |
| No dependency expansion in the last pass | SATISFIED | The dependency register closed at twelve entries — two existing, three reused, four extended, three authored — and re-reading the composition at this stage surfaced no further dependency. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Eight items re-verified against the composition, all CONFIRMED, none OVERTURNED. |
| Every INFERRED finding promoted, accepted or carried forward with a reason | SATISFIED | Stage 2's two INFERRED concerns are re-grounded here as OBSERVED. Two findings raised here stay INFERRED and are carried forward to Stage 7: the runtime's evidence for molecule steps, and the placement of the conformance workload. |

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
