# Change Seed — platform / capability_transforms

**Stage:** 0 — Change Seed
**CR:** molecule_composition
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the four clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The capability transforms subdomain governs the units of computation a governed act performs: what a
transform is, what it is composed of, how it runs, and whether its result is determined by its
inputs, as each transform declares. A transform is either an atom, one implementation with one result, or a molecule, a stated
sequence of steps in which a loop may run a composed body once per member of a stated collection. Its
authority is to decide the shape of a transform and how that shape runs, and it decides nothing about
what any domain computes or whether a computation should be one step or several.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| capability_transforms | MODIFY | The platform declares composed transforms and nothing can carry one from design to execution: design cannot state one, construction cannot render one, compilation accepts one it cannot vouch for, and execution cannot run one. No rule forbids a composed transform, so its model is stated for the first time. The rule that every transform is pure becomes a declaration: determinism is required of a transform declared deterministic, and a transform may declare that it is not. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Transform | A unit of computation a governed act performs. |
| Atom | A transform with one implementation and one result. |
| Molecule | A transform composed of other transforms, run as a stated sequence of steps. |
| Step | One transform a molecule runs, in its declared place in the sequence. |
| Loop | A step that runs a composed body once for each member of a stated collection. |
| Body | What a loop runs on each pass: an atom or a molecule. |
| Pass | One run of a loop's body, for one member of its collection. |
| Carried value | A value a loop passes from one pass to the next. |
| Emission | The one value a molecule yields as its result. |
| Purity | Whether a transform's result is determined by its inputs, as declared. |
| Deterministic transform | A transform declared to produce the same output from the same inputs, and held to it. |
| Non-deterministic transform | A transform declared as one whose result is not determined by its inputs, such as a language model offering the words it might write next. |
| Side effect | A change a computation makes outside its own result; the business of capability side effects, never of transforms. |
| Evidence record | The observable trace that a step ran, naming its results and not their values. |
| Design | The statement of what a change will build, from which construction renders artifacts. |
| Construction | Rendering the artifacts a design determines, at full determinacy or not at all. |
| Recorded outcome | A result a non-deterministic atom produced, kept as evidence when it was produced. |
| Replay | Reproducing a past run from its sealed composition and inputs, using recorded outcomes in place of non-deterministic atoms. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A design can state a molecule's steps, including a loop and its body, and construction renders it at full determinacy. |
| A transform can declare that its result is not determined by its inputs, and every transform not so declared is held to determinism. |
| A molecule whose steps or loop body cannot be run is refused when the composition is built. |
| A molecule's steps run in their declared order, including a composed body once per pass of a loop. |
| A composed transform designed, constructed, compiled and run end to end shows the path holds. |
| Every result a non-deterministic atom produces is recorded, and a replay reproduces the run from the recorded results. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| Most transforms are atoms: one implementation, one result. | HIGH |
| The platform declares a second shape, the molecule, run as a stated sequence of steps. | HIGH |
| A loop runs a composed body once for each member of a stated collection and carries values from one pass to the next. | HIGH |
| A molecule exists so a computation made of several decisions can be declared as those decisions, each visible in the composition. | HIGH |
| A loop keeps repetition declared and bounded: it runs once per member of a collection the composition can see. | HIGH |
| The molecule's shape is declared: its steps, its loop, the collection a loop runs over, the values it carries, and the one value it emits. | HIGH |
| The compiler reads a molecule's declaration and lowers it. | HIGH |
| No register of the design language describes a molecule's steps. | HIGH |
| The renderer writes an atom's implementation and never a molecule's steps, its loop or its emission. | HIGH |
| A design naming a molecule leaves construction undetermined, and construction emits nothing at less than full determinacy. | HIGH |
| A loop's body is lowered as a reference to a molecule, with no implementation attached and nothing checking that it can be run. | HIGH |
| The runtime dispatches every step, including each pass of a loop, as a single implementation. | HIGH |
| Running the compiler's own loop shape fails with CTExecutionError "CT-IR step missing handler_ref", and a nested molecule fails the same way. | HIGH |
| Every transform in the composition is an atom. | HIGH |
| The only repeated computation in the composition runs its whole repetition inside one atom, where none of its decisions can be seen. | HIGH |
| A business domain needed a response written word by word with a visible rule decision on every word, and its design could not state it. | HIGH |
| The instance belongs to a domain this platform does not require; it is evidence that the shape occurs. | HIGH |
| The workflow constitution requires an act to be acyclic, and repetition belongs in molecules, not acts. | HIGH |
| No constitution or invariant forbids a composed loop body. | HIGH |
| A composed computation may include a step whose result is not determined by its inputs; a language model offering the words it might write next is one. | HIGH |
| The constitution governing transforms says every transform is pure and that the same inputs always produce the same output. | HIGH |
| The schema already lets a transform declare a different purity, and nothing reads the declaration, so a transform declared otherwise is unenforced rather than lawful. | HIGH |
| A molecule's purity cannot be checked against its steps while every step is required to be the one kind. | HIGH |
| The requirement that every transform is pure becomes a declaration: a transform declared deterministic must be, and a transform may instead declare that it is not. | HIGH |
| No transform gains a side effect by declaring that it is not deterministic; side effects remain the business of capability side effects. | HIGH |
| Treating a non-deterministic step as a side effect was rejected: a side effect runs as a step of a governed operation, never inside a transform, so it could not be repeated once per pass of a loop. | HIGH |
| Whether any domain uses a non-deterministic transform is that domain's decision, declared where it is made. | HIGH |
| Putting the whole repetition inside one atom was rejected: every decision inside it is invisible to governance. | HIGH |
| Unrolling the repetition into the act was rejected: it makes the composition unreadable where it must be read. | HIGH |
| A loop runs for every member of its collection, every time; a finished loop carries that fact forward and the remaining passes do nothing. | HIGH |
| Molecules may contain molecules to any depth, and a loop's body may contain a loop. | HIGH |
| A molecule that contains itself, directly or through others, is refused when the composition is built. | HIGH |
| A molecule's purity is declared, and a molecule declared pure is refused when any of its steps is not. | HIGH |
| Each step a molecule runs leaves its own evidence record, naming its results and not their values. | HIGH |
| A loop of many passes leaves a record per step per pass. | HIGH |
| The evidence for this change must not come from the domain that found the gap. | HIGH |
| The standard states that the same governed state, proposal and closure determine the same result, and that replay reproduces it. | HIGH |
| A step whose result varies breaks determinism and replay unless what it produced is kept. | HIGH |
| Every result a non-deterministic atom produces is recorded as evidence when it is produced. | HIGH |
| A replay uses the recorded result instead of running a non-deterministic atom again. | HIGH |
| Determinism holds for the governed state, the proposal, the closure and the recorded outcomes together. | HIGH |
| The platform already admits a value that differs every time it is asked, the clock, whose answer is recorded where it is used. | HIGH |
| A non-deterministic atom's results are consumed by a deterministic step before anything routes on them: they may be offered, never decided. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Every transform in the composition is an atom. | Establishes that no consumer depends on how molecules behave today. | Confirm the kind of every transform the composition carries. |
| Nothing governing states how a molecule runs. | Decides whether this relaxes a rule or states a model for the first time. | Establish what constitution, invariant or schema governs molecules, and what each says. |
| The design language cannot state a molecule's steps, and the renderer cannot write them. | The design half of the change. | Establish which registers describe a transform and what the renderer writes for one. |
| The runtime cannot run a composed step. | The execution half of the change. | Confirm how the runtime dispatches a step and a loop pass, and what a composed body lacks. |
| Nothing reads a transform's declared purity. | Decides whether checking purity changes the behaviour of anything that exists. | Establish every reader of a transform's purity. |
| The constitution governing transforms requires every transform to be pure and deterministic, and nothing enforces determinism. | Decides whether this relaxes an enforced rule or replaces an unenforced one with a declaration. | Establish what the constitution requires of every transform and what checks each requirement. |
| A repeated computation exists that hides its decisions inside one atom. | Establishes that the cost is already being paid. | Confirm the instance and where its repetition lives. |
| The platform already admits a value not determined by its inputs, and records it where it is used. | A precedent decides whether recorded outcomes are a new principle or an existing one applied to transforms. | Establish how the composition admits and records the clock's answer. |
| Nothing replays a run from recorded values today. | Decides whether replay from recorded outcomes extends an existing path or adds one. | Establish what replay the runtime and conformance evidence perform. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Acts stay acyclic; repetition lives in molecules. | Business policy |
| A loop runs for every member of its stated collection; its length never depends on the data it computes. | Business policy |
| No molecule contains itself, directly or through others. | Business policy |
| A molecule declared pure has no step that is not. | Business policy |
| A transform declared deterministic produces the same output from the same inputs. | Business policy |
| No transform has side effects, whatever its declared purity. | Business policy |
| Each step a molecule runs leaves an evidence record naming its results and not their values. | Business policy |
| Amending the runtime without the design and construction halves is not an acceptable partial change. | Business policy |
| The end-to-end evidence comes from the platform's own conformance evidence, not from the domain that found the gap. | Business policy |
| Every result a non-deterministic atom produces is recorded when it is produced. | Business policy |
| A replay never runs a non-deterministic atom; it uses the recorded result. | Business policy |
| Nothing routes on a non-deterministic atom's result until a deterministic step has consumed it. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every molecule in a composition can be run. |
| A molecule's steps run in their declared order. |
| A loop runs its body exactly once per member of its stated collection. |
| No molecule contains itself. |
| A molecule declared pure contains only pure steps. |
| Every transform declares whether it is deterministic. |
| No transform has side effects. |
| Every step a molecule runs leaves one evidence record. |
| Every result a non-deterministic atom produced is recorded. |
| A replay reproduces the same result from the same inputs and recorded outcomes. |
| Nothing routes directly on a non-deterministic atom's result. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Molecule | Declared and unrunnable | Its shape is declared and nothing can design, construct or run it, which is the state this change ends. |
| Molecule | Designed | A design states its steps, and construction renders it at full determinacy. |
| Molecule | Admitted | The composition was built with it, having confirmed every step and loop body can be run. |
| Molecule | Run | Its steps ran in declared order, each leaving an evidence record. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A molecule ran its steps | When a governed act runs a molecule | Each decision the molecule makes is observable when it is made. |
| A molecule was refused | When the composition is built with a molecule it cannot run, one that contains itself, or one declared pure with a step that is not | A molecule that cannot keep its declaration never enters a composition. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a molecule is and how it runs | The platform |
| What any domain composes | The domain that owns the transform |
| Whether a computation is one atom or several steps | The design that states it |
| How a design states a molecule | The design language |
| What counts as evidence that a step ran | The platform |
| Whether a transform is deterministic | The design that declares it |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What any domain composes | Each domain states its own molecules in its own change. |
| Whether a computation should be one atom or several steps | That is each design's judgement. |
| The shape of an act | Acts stay acyclic; repetition lives in molecules. |
| Whether any domain uses a non-deterministic transform | Each domain decides, and declares it where it is made. |
| A loop that stops early | Rejected by the business author: a loop's length never depends on the data it computes. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| capability_transforms | MODIFIED |
| design | EXTENDED |
| workflow | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design states a molecule with a loop whose body is itself a molecule, and construction renders it at full determinacy. |
| The composition is built with that molecule, and running it runs its steps in declared order, the body once per member of the collection. |
| A loop whose work finishes early still runs one pass per member, and the remaining passes change nothing. |
| A molecule nested inside another runs. |
| A molecule whose loop body cannot be run is refused when the composition is built. |
| A molecule that contains itself is refused when the composition is built. |
| A molecule declared pure with a step that is not pure is refused when the composition is built. |
| Each step a molecule runs leaves one evidence record naming its results and not their values. |
| A transform declared non-deterministic is admitted, and its declaration is visible to anyone reading the composition. |
| A molecule containing a non-deterministic step, and declared so, is admitted and runs. |
| Every transform that ran before this change runs as it did, and each is declared deterministic. |
| The end-to-end evidence is part of the platform's own conformance evidence. |
| Every result a non-deterministic atom produces in a run is recorded. |
| Replaying that run reproduces the same result without running the non-deterministic atom. |
| A composition in which something routes directly on a non-deterministic atom's result is refused when it is built. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Molecule | Declared and unrunnable | Designed | A design states its steps and construction renders it. | None. |
| Molecule | Designed | Admitted | The composition is built and confirms every step and loop body can be run. | None. |
| Molecule | Admitted | Run | A governed act runs it. | Each step leaves an evidence record. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Build a composition | A molecule's step or loop body cannot be run. | Every molecule in a composition can be run. |
| Build a composition | A molecule contains itself, directly or through others. | Repetition with no stated bound. |
| Build a composition | A molecule declared pure has a step that is not. | The declaration is what a reader relies on to see where determinism ends. |
| Build a composition | Something routes directly on a non-deterministic atom's result. | Its results may be offered, never decided. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
