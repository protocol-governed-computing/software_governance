# Stage 2 — Domain Model Discovery: platform / capability_transforms

**Stage:** 2 — Domain Model Discovery
**CR:** molecule_composition
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned baseline
`1b0cfbd3d094b7e93a965135c32b9f94ba8c3c43c0a1e8e8aacac8ebbdc9d010` — 407 artifacts across seven
domains — read through the inspection interface, and against the compiler, runtime and renderer that
build and run it. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Transform | A unit of computation a governed act performs. | Declared in the composition and sealed at build; twenty-eight are carried. | OBSERVED | S1 business_vocabulary #1 |
| Atom | A transform with one implementation and one result. | Twenty-eight declared, every transform the composition carries. | OBSERVED | S1 business_vocabulary #2 |
| Molecule | A transform composed of other transforms, run as a stated sequence of steps. | Its shape is declared by the platform's schema; none is carried by any composition. | OBSERVED | S1 business_vocabulary #3 |
| Loop | A step that runs a composed body once for each member of a stated collection. | Declared by the schema as a kind of step; none is carried. | OBSERVED | S1 business_vocabulary #5 |
| Evidence record | The observable trace that a step ran, naming its results and not their values. | Written as an act runs, one per step of a governed operation; nothing is written for the atoms inside a transform. | OBSERVED | S1 business_vocabulary #14 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Transform | Kind | Whether it is an atom or a molecule. | OBSERVED | S1 business_vocabulary #2 |
| Transform | Purity | Whether its result is determined by its inputs, as declared. Every carried transform declares itself pure except one, which declares that it emits a final value. | OBSERVED | S1 business_vocabulary #10 |
| Atom | Implementation | The module and callable that realize it. | OBSERVED | S1 business_vocabulary #2 |
| Molecule | Steps | Its composed transforms, in declared order. | OBSERVED | S1 business_vocabulary #4 |
| Molecule | Emission | The one value it yields. | OBSERVED | S1 business_vocabulary #9 |
| Loop | Collection | What it runs once per member of. | OBSERVED | S1 business_vocabulary #5 |
| Loop | Body | The atom or molecule it runs on each pass. | OBSERVED | S1 business_vocabulary #6 |
| Loop | Carried values | What it passes from one pass to the next. | OBSERVED | S1 business_vocabulary #8 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Design a transform | The design of a change | A transform stated with its kind, purity and implementation; for a molecule, nothing about its steps can be stated. | OBSERVED | S1 requested_outcomes #1 |
| Construct a transform | Construction | An atom's declaration rendered at full determinacy; a molecule's steps, loop and emission are never rendered. | OBSERVED | S1 requested_outcomes #1 |
| Build a composition | The compiler | Every transform lowered; a molecule's steps lowered, and a loop's body lowered as a reference with no implementation, with nothing confirming it can run. | OBSERVED | S1 requested_outcomes #3 |
| Run a transform | The runtime, within a governed act | An atom's implementation run; a composed step fails for want of an implementation. | OBSERVED | S1 requested_outcomes #4 |
| Declare a transform's purity | The design of a change | A purity value written into the declaration and read by nothing. | OBSERVED | S1 requested_outcomes #2 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Design a transform | 1 | State the transform's kind, purity, module and callable | The design's binding of the transform to its implementation | OBSERVED | S1 system_beliefs #3 |
| Design a transform | 2 | State a molecule's steps, loop and emission | Nothing: no register holds them | OBSERVED | S1 system_beliefs #3 |
| Construct a transform | 1 | Render the transform's summary, inputs, outputs, kind, purity and implementation | The transform's declaration | OBSERVED | S1 system_beliefs #3 |
| Construct a transform | 2 | Render a molecule's steps and emission | Nothing: the renderer writes neither | OBSERVED | S1 system_beliefs #3 |
| Build a composition | 1 | Lower each atom with the implementation it names | The atom's executable form | OBSERVED | S1 system_beliefs #4 |
| Build a composition | 2 | Lower each molecule step; lower a loop as a reference to its body | The molecule's executable form, with no implementation on a composed step | OBSERVED | S1 system_beliefs #4 |
| Run a transform | 1 | Dispatch each step to the implementation it carries | The step's result | OBSERVED | S1 system_beliefs #4 |
| Run a transform | 2 | For a loop, dispatch the body once per member of the collection, carrying values forward | The loop's result, or a failure where the body carries no implementation | OBSERVED | S1 system_beliefs #4 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Every transform in the composition is an atom. | VERIFIED | si.artifact.list --kind CT returns twenty-eight transforms, and si.artifact.show reports each declared ct_kind atom. | S1 system_beliefs #1 |
| Nothing governing states how a molecule runs. | VERIFIED | capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 names atoms only, in its rule that an atom declares its implementation. execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0 exempts molecules from declaring an implementation because "the atom stream provides the execution specification", and states nothing about how that stream runs. The molecule's shape is declared in SCHEMA_MOLECULE_V0, which is substrate, not a rule. | S1 system_beliefs #2 |
| The design language cannot state a molecule's steps, and the renderer cannot write them. | VERIFIED | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 declares an implementation binding with a kind of atom or molecule, and no register for a molecule's steps, loop or emission. The renderer's transform builder writes summary, refusal, inputs, outputs, kind, purity, operation and implementation, and nothing else. | S1 system_beliefs #3 |
| The runtime cannot run a composed step. | VERIFIED | The runtime's transform executor dispatches every step, and every pass of a loop, through a sealed implementation reference. The compiler lowers a loop's body and a nested molecule with none. Running the compiler's loop shape through the executor raises CTExecutionError "CT-IR step missing handler_ref". | S1 system_beliefs #4 |
| Nothing reads a transform's declared purity. | VERIFIED | No compiler, runtime or inspector source reads ct_purity. The renderer writes it and the compiler carries it into the declaration; nothing decides anything by it. | S1 system_beliefs #5 |
| The constitution governing transforms requires every transform to be pure and deterministic, and nothing enforces determinism. | VERIFIED | capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 states CT_PURITY: "CT MUST be a pure function; same inputs MUST always produce same outputs". Its enforcing invariant, capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0, is checked by an assertion that inspects an implementation for business outcomes raised rather than returned, and nothing else. | S1 system_beliefs #6 |
| A repeated computation exists that hides its decisions inside one atom. | VERIFIED | workload::CT_PURE_COLLATZ_STEP_V0 computes a whole Collatz sequence for each input inside one atom. | S1 system_beliefs #7 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Governs transforms | capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | Declares that every transform is pure, deterministic and side-effect free, with explicit inputs and outputs, and that an atom declares its implementation. | PARTIAL | Says nothing about molecules, and admits no transform that declares it is not deterministic. |
| Holds an atom to returning its outcomes | capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 | Refuses an atom whose implementation raises a business outcome instead of returning it. | PARTIAL | Checks neither determinism nor anything about a molecule. |
| Requires an atom's implementation | execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0 | Refuses an atom with no module or callable, and exempts molecules. | PARTIAL | Does not require a molecule's steps to resolve to anything runnable. |
| Closes a transform's surface | capability_transforms::INVARIANT_CT_SURFACE_CLOSED_V1 | Refuses a transform whose declared surface is open. | EXACT | Nothing this change needs. |
| Governs the act | workflow::CONSTITUTION_WORKFLOW_V0 | Declares that an act is acyclic. | EXACT | Nothing this change needs: repetition belongs in a molecule, not an act. |
| Declares which trace content is compared | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 | Declares which evidence fields are determinative and which observational. | EXACT | Nothing this change needs; a step's evidence names its results, which it already classifies. |
| States a transform's binding in a design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Admits a design whose implementation bindings state a transform's kind, purity, module and callable. | PARTIAL | Admits no statement of a molecule's steps, loop or emission. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No rule states how a molecule runs: its step order, a loop's passes, or what makes it admissible. | CRITICAL | A molecule could be admitted and run by whatever the implementation happens to do. | OBSERVED | S2 belief_verification #2 |
| The rule that every transform is pure admits no transform that declares it is not. | CRITICAL | A computation whose result is not determined by its inputs cannot be declared lawfully, and a molecule's purity cannot be checked against steps that must all be one kind. | OBSERVED | S2 belief_verification #6 |
| Nothing enforces a transform's declared purity, or checks a molecule's against its steps. | CRITICAL | A declaration nothing reads is a sentence, not a guarantee. | OBSERVED | S2 belief_verification #5 |
| The design language cannot state a molecule's steps, and construction cannot render them. | CRITICAL | No change can deliver a molecule through the governed path. | OBSERVED | S2 belief_verification #3 |
| The compiler lowers a loop's body without confirming it can be run, and refuses no molecule that contains itself. | CRITICAL | An unrunnable or unbounded molecule would be admitted. | OBSERVED | S2 belief_verification #4 |
| The runtime cannot run a composed step, at the top of a molecule or as a loop's body. | CRITICAL | No molecule runs. | OBSERVED | S2 belief_verification #4 |
| No evidence is written for the steps inside a transform. | MAJOR | A decision made inside a molecule would be declared but not observable when it is made. | OBSERVED | S1 constraints #7 |
| No conformance evidence exercises a molecule. | MAJOR | The path cannot be shown to hold, and the domain that found the gap must not supply the evidence. | OBSERVED | S1 constraints #9 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The platform already places repetition in the molecule and forbids it in the act. | workflow::CONSTITUTION_WORKFLOW_V0 | OBSERVED | S1 known_facts — the workflow constitution requires an act to be acyclic |
| The platform already exempts molecules from declaring an implementation, anticipating that their steps are the specification. | execution::INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0 | OBSERVED | S2 belief_verification #2 |
| The design language already anticipates a molecule by kind, and stops there. | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | OBSERVED | S2 belief_verification #3 |
| The purity classes a transform may declare already include one that is not deterministic, and one transform already declares a class other than pure. | capability_transforms::CT_EXEC_EMIT_V0 | OBSERVED | S2 belief_verification #5 |
| Step evidence already records a step's result names and not their values, so evidence for steps inside a molecule adds records without adding compared values. | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 | OBSERVED | S1 constraints #7 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Replacing "every transform is pure" is a change to core doctrine that other documents repeat, so a composition's rule and the guidance around it could disagree. | capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | MAJOR | OBSERVED | S2 gaps #2 |
| The governance surface is immutable within a version, so the constitution's new model must be a new version, and every artifact that names the old one must be accounted for. | capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | MAJOR | INFERRED | S2 gaps #1 |
| Evidence for every step inside a loop multiplies records by the number of passes. | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 | MINOR | INFERRED | S1 known_facts — a loop of many passes leaves a record per step per pass |
| One transform declares that it emits a final value, a purity class the new model must place: deterministic or not. | capability_transforms::CT_EXEC_EMIT_V0 | MINOR | OBSERVED | S2 architectural_observations #4 |

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
