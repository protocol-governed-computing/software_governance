# Stage 1 — Change Request: Clarification & Fact Capture: platform / capability_transforms
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** molecule_composition
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| capability_transforms | MODIFY | The platform declares composed transforms and nothing can carry one from design to execution: design cannot state one, construction cannot render one, compilation accepts one it cannot vouch for, and execution cannot run one. No rule forbids a composed transform, so its model is stated for the first time. The rule that every transform is pure becomes a declaration: determinism is required of a transform declared deterministic, and a transform may declare that it is not. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Transform | A unit of computation a governed act performs. | CR seed §2 Business Vocabulary #1 |
| Atom | A transform with one implementation and one result. | CR seed §2 Business Vocabulary #2 |
| Molecule | A transform composed of other transforms, run as a stated sequence of steps. | CR seed §2 Business Vocabulary #3 |
| Step | One transform a molecule runs, in its declared place in the sequence. | CR seed §2 Business Vocabulary #4 |
| Loop | A step that runs a composed body once for each member of a stated collection. | CR seed §2 Business Vocabulary #5 |
| Body | What a loop runs on each pass: an atom or a molecule. | CR seed §2 Business Vocabulary #6 |
| Pass | One run of a loop's body, for one member of its collection. | CR seed §2 Business Vocabulary #7 |
| Carried value | A value a loop passes from one pass to the next. | CR seed §2 Business Vocabulary #8 |
| Emission | The one value a molecule yields as its result. | CR seed §2 Business Vocabulary #9 |
| Purity | Whether a transform's result is determined by its inputs, as declared. | CR seed §2 Business Vocabulary #10 |
| Deterministic transform | A transform declared to produce the same output from the same inputs, and held to it. | CR seed §2 Business Vocabulary #11 |
| Non-deterministic transform | A transform declared as one whose result is not determined by its inputs, such as a language model offering the words it might write next. | CR seed §2 Business Vocabulary #12 |
| Side effect | A change a computation makes outside its own result; the business of capability side effects, never of transforms. | CR seed §2 Business Vocabulary #13 |
| Evidence record | The observable trace that a step ran, naming its results and not their values. | CR seed §2 Business Vocabulary #14 |
| Design | The statement of what a change will build, from which construction renders artifacts. | CR seed §2 Business Vocabulary #15 |
| Construction | Rendering the artifacts a design determines, at full determinacy or not at all. | CR seed §2 Business Vocabulary #16 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A design can state a molecule's steps, including a loop and its body, and construction renders it at full determinacy. | CR seed §3 Requested Outcomes #1 |
| A transform can declare that its result is not determined by its inputs, and every transform not so declared is held to determinism. | CR seed §3 Requested Outcomes #2 |
| A molecule whose steps or loop body cannot be run is refused when the composition is built. | CR seed §3 Requested Outcomes #3 |
| A molecule's steps run in their declared order, including a composed body once per pass of a loop. | CR seed §3 Requested Outcomes #4 |
| A composed transform designed, constructed, compiled and run end to end shows the path holds. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| Most transforms are atoms: one implementation, one result. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| The platform declares a second shape, the molecule, run as a stated sequence of steps. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A loop runs a composed body once for each member of a stated collection and carries values from one pass to the next. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A molecule exists so a computation made of several decisions can be declared as those decisions, each visible in the composition. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A loop keeps repetition declared and bounded: it runs once per member of a collection the composition can see. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The molecule's shape is declared: its steps, its loop, the collection a loop runs over, the values it carries, and the one value it emits. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The compiler reads a molecule's declaration and lowers it. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| No register of the design language describes a molecule's steps. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| The renderer writes an atom's implementation and never a molecule's steps, its loop or its emission. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A design naming a molecule leaves construction undetermined, and construction emits nothing at less than full determinacy. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| A loop's body is lowered as a reference to a molecule, with no implementation attached and nothing checking that it can be run. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| The runtime dispatches every step, including each pass of a loop, as a single implementation. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| Running the compiler's own loop shape fails with CTExecutionError "CT-IR step missing handler_ref", and a nested molecule fails the same way. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| Every transform in the composition is an atom. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| The only repeated computation in the composition runs its whole repetition inside one atom, where none of its decisions can be seen. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| A business domain needed a response written word by word with a visible rule decision on every word, and its design could not state it. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| The instance belongs to a domain this platform does not require; it is evidence that the shape occurs. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| The workflow constitution requires an act to be acyclic, and repetition belongs in molecules, not acts. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| No constitution or invariant forbids a composed loop body. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| A composed computation may include a step whose result is not determined by its inputs; a language model offering the words it might write next is one. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| The constitution governing transforms says every transform is pure and that the same inputs always produce the same output. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| The schema already lets a transform declare a different purity, and nothing reads the declaration, so a transform declared otherwise is unenforced rather than lawful. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| A molecule's purity cannot be checked against its steps while every step is required to be the one kind. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| The requirement that every transform is pure becomes a declaration: a transform declared deterministic must be, and a transform may instead declare that it is not. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| No transform gains a side effect by declaring that it is not deterministic; side effects remain the business of capability side effects. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| Treating a non-deterministic step as a side effect was rejected: a side effect runs as a step of a governed operation, never inside a transform, so it could not be repeated once per pass of a loop. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| Whether any domain uses a non-deterministic transform is that domain's decision, declared where it is made. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| Putting the whole repetition inside one atom was rejected: every decision inside it is invisible to governance. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| Unrolling the repetition into the act was rejected: it makes the composition unreadable where it must be read. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| A loop runs for every member of its collection, every time; a finished loop carries that fact forward and the remaining passes do nothing. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| Molecules may contain molecules to any depth, and a loop's body may contain a loop. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| A molecule that contains itself, directly or through others, is refused when the composition is built. | HIGH | CR seed §4 Known Facts — Business Truths #32 |
| A molecule's purity is declared, and a molecule declared pure is refused when any of its steps is not. | HIGH | CR seed §4 Known Facts — Business Truths #33 |
| Each step a molecule runs leaves its own evidence record, naming its results and not their values. | HIGH | CR seed §4 Known Facts — Business Truths #34 |
| A loop of many passes leaves a record per step per pass. | HIGH | CR seed §4 Known Facts — Business Truths #35 |
| The evidence for this change must not come from the domain that found the gap. | HIGH | CR seed §4 Known Facts — Business Truths #36 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Every transform in the composition is an atom. | Establishes that no consumer depends on how molecules behave today. | Confirm the kind of every transform the composition carries. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Nothing governing states how a molecule runs. | Decides whether this relaxes a rule or states a model for the first time. | Establish what constitution, invariant or schema governs molecules, and what each says. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The design language cannot state a molecule's steps, and the renderer cannot write them. | The design half of the change. | Establish which registers describe a transform and what the renderer writes for one. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The runtime cannot run a composed step. | The execution half of the change. | Confirm how the runtime dispatches a step and a loop pass, and what a composed body lacks. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Nothing reads a transform's declared purity. | Decides whether checking purity changes the behaviour of anything that exists. | Establish every reader of a transform's purity. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| The constitution governing transforms requires every transform to be pure and deterministic, and nothing enforces determinism. | Decides whether this relaxes an enforced rule or replaces an unenforced one with a declaration. | Establish what the constitution requires of every transform and what checks each requirement. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| A repeated computation exists that hides its decisions inside one atom. | Establishes that the cost is already being paid. | Confirm the instance and where its repetition lives. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Acts stay acyclic; repetition lives in molecules. | Business policy | CR seed §7 Constraints #1 |
| A loop runs for every member of its stated collection; its length never depends on the data it computes. | Business policy | CR seed §7 Constraints #2 |
| No molecule contains itself, directly or through others. | Business policy | CR seed §7 Constraints #3 |
| A molecule declared pure has no step that is not. | Business policy | CR seed §7 Constraints #4 |
| A transform declared deterministic produces the same output from the same inputs. | Business policy | CR seed §7 Constraints #5 |
| No transform has side effects, whatever its declared purity. | Business policy | CR seed §7 Constraints #6 |
| Each step a molecule runs leaves an evidence record naming its results and not their values. | Business policy | CR seed §7 Constraints #7 |
| Amending the runtime without the design and construction halves is not an acceptable partial change. | Business policy | CR seed §7 Constraints #8 |
| The end-to-end evidence comes from the platform's own conformance evidence, not from the domain that found the gap. | Business policy | CR seed §7 Constraints #9 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every molecule in a composition can be run. | CR seed §8 Business Invariants #1 |
| A molecule's steps run in their declared order. | CR seed §8 Business Invariants #2 |
| A loop runs its body exactly once per member of its stated collection. | CR seed §8 Business Invariants #3 |
| No molecule contains itself. | CR seed §8 Business Invariants #4 |
| A molecule declared pure contains only pure steps. | CR seed §8 Business Invariants #5 |
| Every transform declares whether it is deterministic. | CR seed §8 Business Invariants #6 |
| No transform has side effects. | CR seed §8 Business Invariants #7 |
| Every step a molecule runs leaves one evidence record. | CR seed §8 Business Invariants #8 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Molecule | Declared and unrunnable | Its shape is declared and nothing can design, construct or run it, which is the state this change ends. | CR seed §9 Lifecycle States #1 |
| Molecule | Designed | A design states its steps, and construction renders it at full determinacy. | CR seed §9 Lifecycle States #2 |
| Molecule | Admitted | The composition was built with it, having confirmed every step and loop body can be run. | CR seed §9 Lifecycle States #3 |
| Molecule | Run | Its steps ran in declared order, each leaving an evidence record. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A molecule ran its steps | When a governed act runs a molecule | Each decision the molecule makes is observable when it is made. | CR seed §10 Business Events #1 |
| A molecule was refused | When the composition is built with a molecule it cannot run, one that contains itself, or one declared pure with a step that is not | A molecule that cannot keep its declaration never enters a composition. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a molecule is and how it runs | The platform | CR seed §11 Authority Boundaries #1 |
| What any domain composes | The domain that owns the transform | CR seed §11 Authority Boundaries #2 |
| Whether a computation is one atom or several steps | The design that states it | CR seed §11 Authority Boundaries #3 |
| How a design states a molecule | The design language | CR seed §11 Authority Boundaries #4 |
| What counts as evidence that a step ran | The platform | CR seed §11 Authority Boundaries #5 |
| Whether a transform is deterministic | The design that declares it | CR seed §11 Authority Boundaries #6 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What any domain composes | Each domain states its own molecules in its own change. | CR seed §12 Out of Scope #1 |
| Whether a computation should be one atom or several steps | That is each design's judgement. | CR seed §12 Out of Scope #2 |
| The shape of an act | Acts stay acyclic; repetition lives in molecules. | CR seed §12 Out of Scope #3 |
| Whether any domain uses a non-deterministic transform | Each domain decides, and declares it where it is made. | CR seed §12 Out of Scope #4 |
| A loop that stops early | Rejected by the business author: a loop's length never depends on the data it computes. | CR seed §12 Out of Scope #5 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| capability_transforms | MODIFIED | CR seed §13 Governance Scope #1 |
| design | EXTENDED | CR seed §13 Governance Scope #2 |
| workflow | ADJACENT | CR seed §13 Governance Scope #3 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| A design states a molecule with a loop whose body is itself a molecule, and construction renders it at full determinacy. | CR seed §15 Acceptance Criteria #1 |
| The composition is built with that molecule, and running it runs its steps in declared order, the body once per member of the collection. | CR seed §15 Acceptance Criteria #2 |
| A loop whose work finishes early still runs one pass per member, and the remaining passes change nothing. | CR seed §15 Acceptance Criteria #3 |
| A molecule nested inside another runs. | CR seed §15 Acceptance Criteria #4 |
| A molecule whose loop body cannot be run is refused when the composition is built. | CR seed §15 Acceptance Criteria #5 |
| A molecule that contains itself is refused when the composition is built. | CR seed §15 Acceptance Criteria #6 |
| A molecule declared pure with a step that is not pure is refused when the composition is built. | CR seed §15 Acceptance Criteria #7 |
| Each step a molecule runs leaves one evidence record naming its results and not their values. | CR seed §15 Acceptance Criteria #8 |
| A transform declared non-deterministic is admitted, and its declaration is visible to anyone reading the composition. | CR seed §15 Acceptance Criteria #9 |
| A molecule containing a non-deterministic step, and declared so, is admitted and runs. | CR seed §15 Acceptance Criteria #10 |
| Every transform that ran before this change runs as it did, and each is declared deterministic. | CR seed §15 Acceptance Criteria #11 |
| The end-to-end evidence is part of the platform's own conformance evidence. | CR seed §15 Acceptance Criteria #12 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Molecule | Declared and unrunnable | Designed | A design states its steps and construction renders it. | None. | CR seed §17 Lifecycle Transitions #1 |
| Molecule | Designed | Admitted | The composition is built and confirms every step and loop body can be run. | None. | CR seed §17 Lifecycle Transitions #2 |
| Molecule | Admitted | Run | A governed act runs it. | Each step leaves an evidence record. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Build a composition | A molecule's step or loop body cannot be run. | Every molecule in a composition can be run. | CR seed §18 Operation Refusals #1 |
| Build a composition | A molecule contains itself, directly or through others. | Repetition with no stated bound. | CR seed §18 Operation Refusals #2 |
| Build a composition | A molecule declared pure has a step that is not. | The declaration is what a reader relies on to see where determinism ends. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
