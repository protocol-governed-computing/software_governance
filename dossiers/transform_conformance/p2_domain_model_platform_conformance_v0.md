# Stage 2 — Domain Model Discovery: platform / conformance

**Stage:** 2 — Domain Model Discovery
**CR:** transform_conformance
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned baseline
`54412f835e6df27975d3692fb2eb09ab9ada37221129811892b12c3a335479f9` — 413 artifacts across seven
domains — read through the inspection interface, and against the compiler, runtime, assembler and
design language that build and judge it. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Transform | A unit of computation a governed act performs, whose implementation lives outside the composition. | Declared in the composition and sealed at build; twenty-eight are carried, none with a vector. | OBSERVED | S1 business_vocabulary #1 |
| Test vector | Stated inputs and the outputs a transform must produce from them. | A declaration kind the platform governs; none is carried by any composition. | OBSERVED | S1 business_vocabulary #7 |
| Runnable case | A test vector bound to the transform as the composition sealed it, ready to run. | Written by the compiler from a vector when a build declares where; no build declares where. | OBSERVED | S1 business_vocabulary #8 |
| Runner | What executes runnable cases and reports each as passed or failed. | Carried by the runtime; invoked by no build. | OBSERVED | S1 business_vocabulary #9 |
| Composition conformance evidence | The platform's record of properties checked once domains are composed. | Written into the snapshot's conformance place on every assembly. | OBSERVED | S1 business_vocabulary #14 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Test vector | Target | The transform it tests. | OBSERVED | S1 business_vocabulary #7 |
| Test vector | Cases | Each case's inputs and the outputs expected from them. | OBSERVED | S1 business_vocabulary #7 |
| Test vector | Expected outcome | Whether a case expects the transform to succeed or to refuse. | OBSERVED | S1 business_vocabulary #7 |
| Test vector | Assertions | For a field whose value cannot be stated, the form it must take instead. | OBSERVED | S1 business_vocabulary #12 |
| Runnable case | Sealed transform | The transform exactly as the composition sealed it. | OBSERVED | S1 business_vocabulary #8 |
| Transform | Conformance standing | Proven, unproven or refused, by what its vectors did. | INFERRED | S1 business_vocabulary #10 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Declare a vector | The design of a change | Nothing: the design language has no way to state one. | OBSERVED | S1 requested_outcomes #1 |
| Generate runnable cases | The compiler, in a domain's build | Cases written where the build declares; no domain build declares where. | OBSERVED | S1 requested_outcomes #2 |
| Run conformance | A domain's build | Nothing: no build step invokes the runner. | OBSERVED | S1 requested_outcomes #2 |
| Judge vectors against their transforms | The compiler | Every rule over vectors reports success, having found none to judge. | OBSERVED | S1 requested_outcomes #5 |
| Record composition conformance | The assembler | Evidence written into the snapshot's conformance place. | OBSERVED | S1 requested_outcomes #6 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Generate runnable cases | 1 | Find each vector's target transform and its sealed form | The target's sealed form | OBSERVED | S1 system_beliefs #3 |
| Generate runnable cases | 2 | Bind each case's inputs to the sealed form and write the case | One runnable case per vector case | OBSERVED | S1 system_beliefs #3 |
| Run conformance | 1 | Read every case from the snapshot's conformance place | The cases to run | OBSERVED | S1 system_beliefs #5 |
| Run conformance | 2 | Execute each case against its sealed transform and compare the result | A pass or a failure per case | OBSERVED | S1 system_beliefs #6 |
| Run conformance | 3 | Report the run as passed only if at least one case ran and none failed | The conformance result | OBSERVED | S1 system_beliefs #2 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| No transform in the composition has a vector. | VERIFIED | si.artifact.list --kind TEST_DATA answers NOT_FOUND: "no artifact of kind 'TEST_DATA' in this composition". si.artifact.list --kind CT returns twenty-eight transforms. | S1 system_beliefs #1 |
| The invariants governing vectors report success over no vectors. | VERIFIED | conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 and capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 are checked by assertions that skip every artifact not a vector and report PASSED over none. conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 declares itself enforced elsewhere, "by the VALIDATE_TEST_DATA phase of the compiler"; the compiler has no such phase, and the assertion bound to it reports PASSED unconditionally. The runner, alone, refuses to report success when no case ran — and nothing invokes it. | S1 system_beliefs #2 |
| No domain build declares conformance. | VERIFIED | Of the six domain build manifests, none declares a vector layer or a place for runnable cases; workload::STRUCTURE_BUILD_WORKLOAD_CONFIG_V0 names conformance only as the repository it lives in. structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 records that the vector layer and conformance phases were removed from the platform's build because implementations are not platform-owned and conformance is enforced where they live. Only the superseded structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V0 still declares a place for cases. No build script invokes the runner. | S1 system_beliefs #3 |
| The design language cannot state a vector. | VERIFIED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 declares twenty-two registers, none for a vector; no phase template mentions one; the vector is not among the families the design language can author, so construction has nothing to render one from. | S1 system_beliefs #4 |
| The runner and composition conformance read and write the same place. | VERIFIED | The runner reads every case from the snapshot's conformance place and fails when it is missing. The assembler writes composition evidence to the same place on every assembly; the pinned snapshot's conformance place holds only that evidence, which the runner would read as a case. | S1 system_beliefs #5 |
| The runner cannot supply recorded results to a non-deterministic step. | VERIFIED | The runner executes each case with its inputs alone. The executor accepts recorded results, and the runner never hands it any, so a molecule with a non-deterministic step would run the step. | S1 system_beliefs #6 |
| The constitution governing vectors says a transform produces its outputs deterministically. | VERIFIED | conformance::CONSTITUTION_TEST_DATA_V0 states that each case declares inputs and expected outputs "that the CT must produce deterministically", and says nothing of molecules or recorded results. | S1 system_beliefs #7 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Governs test vectors | conformance::CONSTITUTION_TEST_DATA_V0 | Declares that a vector's cases state inputs and expected outputs its transform must produce, and that its target is named by identity. | PARTIAL | Says nothing of molecules, recorded results, where vectors run, or what counts as proven. |
| Holds a vector to its transform's outputs | conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 | Refuses a vector whose expected outputs its transform does not declare. | PARTIAL | Reports success when there is no vector to judge. |
| Holds a vector's assertions to known forms | conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | Declares that an assertion names a known mode and type. | MISMATCH | Is enforced by a compiler phase that does not exist; its assertion passes unconditionally. |
| Requires each case to state its expected outcome | capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 | Refuses a case that does not say whether the transform succeeds or refuses. | PARTIAL | Reports success when there is no vector to judge. |
| Records the decision to move conformance out of the platform's build | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | Declares the platform's build without a vector layer or conformance phases, and says why. | EXACT | Nothing this change needs; the decision stands. |
| Declares a domain's build | workload::STRUCTURE_BUILD_WORKLOAD_CONFIG_V0 | Declares where a domain's artifacts are discovered and written. | PARTIAL | Declares no vector layer and no place for runnable cases. |
| Governs non-deterministic steps and their recorded results | capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | Requires every result a non-deterministic step produces to be recorded, and a replay to use the record. | EXACT | Nothing this change needs; a vector supplying recorded results is a replay by that constitution's own terms. |
| Governs molecules | capability_transforms::CONSTITUTION_MOLECULES_V0 | Declares how a molecule runs and that it is run as its declared steps. | EXACT | Nothing this change needs. |
| States a transform's binding in a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Admits a design that states a transform, its implementation or its steps. | PARTIAL | Admits no statement of a vector. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No domain build runs conformance, or declares where its vectors are read and its cases written. | CRITICAL | No transform's code is proven against its declaration anywhere. | OBSERVED | S2 belief_verification #3 |
| The design language cannot state a vector, and construction cannot render one. | CRITICAL | No change can deliver a vector through the governed path. | OBSERVED | S2 belief_verification #4 |
| Every rule over vectors reports success when there are none, and one is bound to a compiler phase that does not exist. | CRITICAL | The composition reports its transforms conformant when none has been judged. | OBSERVED | S2 belief_verification #2 |
| Nothing names a transform as unproven. | MAJOR | An unproven transform is indistinguishable from a proven one to anyone reading the composition. | OBSERVED | S1 requested_outcomes #5 |
| The runner reads the place composition conformance writes. | MAJOR | Invoked today, the runner would read composition evidence as a case. | OBSERVED | S2 belief_verification #5 |
| The runner cannot supply recorded results, and cannot confirm a supplied step was not run. | CRITICAL | A molecule with a non-deterministic step cannot be proven exactly, and replay is not proven by conformance. | OBSERVED | S2 belief_verification #6 |
| The constitution governing vectors admits only deterministic outputs and says nothing of molecules or where vectors run. | MAJOR | The rules for proving a molecule, a recorded result or a domain's build have no statement to rest on. | OBSERVED | S2 belief_verification #7 |
| No conformance result is carried into the composition as evidence. | MAJOR | What was proven is not visible to a reader of the composition. | OBSERVED | S1 requested_outcomes #2 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The platform already decided where conformance belongs; the decision was recorded and never carried out. | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | OBSERVED | S2 belief_verification #3 |
| The runner already refuses to report success when no case ran, which is the discipline the invariants lack. | conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 | OBSERVED | S2 belief_verification #2 |
| The runner already supports asserting a field's form rather than its value, which is what a non-deterministic step on its own needs. | conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | OBSERVED | S1 business_vocabulary #12 |
| The executor already accepts recorded results for non-deterministic steps; only the runner does not pass them. | capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | OBSERVED | S2 belief_verification #6 |
| The compiler already binds a vector's cases to the transform as sealed, which for a molecule is the whole inlined stream. | capability_transforms::CONSTITUTION_MOLECULES_V0 | INFERRED | S1 business_vocabulary #8 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The governance surface is immutable within a version, so the constitution governing vectors needs a new version, and every artifact naming the old one must be accounted for. | conformance::CONSTITUTION_TEST_DATA_V0 | MAJOR | INFERRED | S2 gaps #7 |
| An invariant bound to a compiler phase that does not exist is a second instance of the vacuity this change removes, and correcting it changes what the invariant claims. | conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | MAJOR | OBSERVED | S2 gaps #3 |
| Refusing a transform authored after this change without a vector requires telling an authored transform from an existing one, and nothing in the composition records when a transform was authored. | conformance::CONSTITUTION_TEST_DATA_V0 | MAJOR | INFERRED | S1 constraints #6 |
| Moving the runner's place changes where a snapshot keeps conformance, which the assembler, the runner and anything reading a sealed release must agree on. | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | MINOR | INFERRED | S2 gaps #5 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
