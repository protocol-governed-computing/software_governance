# Stage 4 — Business Model: platform / capability_transforms

**Stage:** 4 — Business Model
**CR:** molecule_composition
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
| The platform | Decides what a transform is, what a molecule is, and how each runs. | Declaring — the shape of a transform and how it runs are its to state. | S1 authority_boundaries #1 |
| The design of a change | States what a domain composes, and whether each transform it declares is deterministic. | Declaring — within the rules the platform states. | S1 authority_boundaries #6 |
| The design language | Decides how a design states a molecule. | Declaring — the registers a design may fill are its to define. | S1 authority_boundaries #4 |
| The build | Lowers every transform, and refuses a molecule it cannot vouch for. | Deciding — a molecule that cannot keep its declaration never enters a composition. | S1 operation_refusals #1 |
| The runtime | Runs a transform's steps and writes the evidence of each. | Executing — it runs what the composition declares and nothing else. | S1 requested_outcomes #4 |
| A reader of the composition | Sees where determinism ends and what each decision was. | Observing — the party a hidden decision misleads. | S1 known_facts — a molecule exists so a computation made of several decisions can be declared as those decisions |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Transform | A unit of computation a governed act performs. | Declared in the composition and sealed at build. | S2 entities Transform |
| Atom | A transform with one implementation and one result, deterministic or declared not. | Declared and sealed; every transform carried today is one, and deterministic. | S2 entities Atom |
| Molecule | A transform composed of other transforms, run as a stated sequence of steps. | Declared and sealed; none is carried today. | S2 entities Molecule |
| Loop | A step running a composed body once per member of a stated collection. | Declared within a molecule. | S2 entities Loop |
| Evidence record | The observable trace that a step ran, naming its results and not their values. | Written as the step runs, one per step, including steps inside a molecule. | S2 entities Evidence record |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The constitutions governing transforms | The existing one for deterministic atoms, and one each for molecules and for atoms declaring they are not deterministic | S3 analysis_findings #1 |
| The design language | The registers a design fills, extended to state a molecule's steps | S3 authoring_decisions State a molecule's steps, loop and emission in a design, and render them at full determinacy |
| The conformance workloads | The platform's own end-to-end evidence, extended with a molecule | S3 analysis_findings #8 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A molecule ran its steps | A governed act runs a molecule | Each decision the molecule makes is observable when it is made | S1 business_events #1 |
| A molecule was refused | The composition is built with a molecule it cannot run, one that contains itself, or one declared pure with a step that is not | A molecule that cannot keep its declaration never enters a composition | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Molecule | is composed of | Steps | Run the steps in declared order | S1 business_invariants #2 |
| Loop | runs | Body | Run the body exactly once per member of the stated collection | S1 business_invariants #3 |
| Molecule | never contains | Itself | Refuse a molecule containing itself when the composition is built | S1 business_invariants #4 |
| Transform | is governed by | Exactly one constitution | Place each transform by its kind and declared purity | S3 authoring_decisions Place every transform under exactly one of the three constitutions by its kind and declared purity |
| Step | leaves | Evidence record | Write one record per step a molecule runs | S1 business_invariants #8 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Keep governing every existing transform as deterministic | S3 authoring_decisions Keep governing every existing transform as deterministic | SATISFIED |  | The existing constitution, unchanged. |
| State how a molecule runs: declared step order, one pass per member of the loop's collection, no molecule containing itself, a molecule's declared purity checked against its steps | S3 authoring_decisions State how a molecule runs: declared step order, one pass per member of the loop's collection, no molecule containing itself, a molecule's declared purity checked against its steps | CRITICAL | GAP-01 | Nothing states it. |
| Admit an atom that declares its result is not determined by its inputs, and forbid it side effects | S3 authoring_decisions Admit an atom that declares its result is not determined by its inputs, and forbid it side effects | CRITICAL | GAP-02 | Nothing admits one lawfully. |
| Place every transform under exactly one of the three constitutions by its kind and declared purity | S3 authoring_decisions Place every transform under exactly one of the three constitutions by its kind and declared purity | CRITICAL | GAP-03 | Nothing places a transform. |
| Hold every atom to returning its outcomes | S3 authoring_decisions Hold every atom to returning its outcomes | SATISFIED |  | Reused as-is. |
| Require an atom's implementation and exempt a molecule | S3 authoring_decisions Require an atom's implementation and exempt a molecule | SATISFIED |  | Reused as-is. |
| Refuse at build a molecule whose steps or loop body cannot be run, one that contains itself, or one declared pure with a step that is not | S3 authoring_decisions Refuse at build a molecule whose steps or loop body cannot be run, one that contains itself, or one declared pure with a step that is not | CRITICAL | GAP-04 | The compiler lowers molecules and confirms nothing about them. |
| Run a molecule's steps in order, including a composed body once per pass of a loop, carrying values between passes | S3 authoring_decisions Run a molecule's steps in order, including a composed body once per pass of a loop, carrying values between passes | CRITICAL | GAP-05 | The runtime dispatches only single implementations. |
| Write one evidence record per step a molecule runs, naming its results and not their values | S3 authoring_decisions Write one evidence record per step a molecule runs, naming its results and not their values | MAJOR | GAP-06 | No evidence is written inside a transform. |
| State a molecule's steps, loop and emission in a design, and render them at full determinacy | S3 authoring_decisions State a molecule's steps, loop and emission in a design, and render them at full determinacy | CRITICAL | GAP-07 | The design language anticipates a molecule by kind only. |
| Show the path holds with a composed transform designed, constructed, compiled and run end to end | S3 authoring_decisions Show the path holds with a composed transform designed, constructed, compiled and run end to end | MAJOR | GAP-08 | No conformance evidence exercises a molecule. |
| Record every result a non-deterministic atom produces, and replay a run from the recorded results | S3 authoring_decisions Record every result a non-deterministic atom produces, and replay a run from the recorded results | CRITICAL | GAP-09 | Nothing records such results or re-executes a run. |
| Refuse at build a composition in which anything routes on a non-deterministic atom's result before a deterministic step has consumed it | S3 authoring_decisions Refuse at build a composition in which anything routes on a non-deterministic atom's result before a deterministic step has consumed it | MAJOR | GAP-10 | Nothing refuses routing on a non-deterministic result. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| capability_transforms | capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | governance read | SATISFIED | S3 dependency_discoveries #1 |
| capability_transforms | capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 | governance read | SATISFIED | S3 dependency_discoveries #2 |
| capability_transforms | capability_transforms::INVARIANT_CT_SURFACE_CLOSED_V1 | governance read | SATISFIED | S3 dependency_discoveries #4 |
| capability_transforms | workflow::CONSTITUTION_WORKFLOW_V0 | governance read | SATISFIED | S3 dependency_discoveries #5 |
| capability_transforms | compiler | build check | GAP | S3 dependency_discoveries #9 |
| capability_transforms | execution | execution | GAP | S3 dependency_discoveries #10 |
| capability_transforms | design | design language | GAP | S3 dependency_discoveries #11 |
| capability_transforms | execution | recording and replay | GAP | S3 dependency_discoveries #13 |

The three gaps are carried by this change, in the order the business author stated: the rules first,
then the compiler, the runtime and the design language, landing together.

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Every molecule in a composition can be run. | S1 business_invariants #1 | invariant |
| 2 | A molecule's steps run in their declared order. | S1 business_invariants #2 | invariant |
| 3 | A loop runs its body exactly once per member of its stated collection. | S1 business_invariants #3 | invariant |
| 4 | No molecule contains itself. | S1 business_invariants #4 | invariant |
| 5 | A molecule declared pure contains only pure steps. | S1 business_invariants #5 | invariant |
| 6 | Every step a molecule runs leaves one evidence record. | S1 business_invariants #8 | invariant |
| 7 | Every transform declares whether it is deterministic. | S1 business_invariants #6 | invariant |
| 8 | No transform has side effects. | S1 business_invariants #7 | invariant |
| 9 | Acts stay acyclic; repetition lives in molecules. | S1 constraints #1 | governance rule |
| 10 | A transform declared deterministic produces the same output from the same inputs. | S1 constraints #5 | business policy |
| 11 | Amending the runtime without the design and construction halves is not an acceptable partial change. | S1 constraints #8 | business policy |
| 12 | The end-to-end evidence comes from the platform's own conformance evidence. | S1 constraints #9 | business policy |
| 13 | No existing transform changes; the platform grows by adding. | S3 analysis_findings #1 | governance rule |
| 14 | Each transform is governed by exactly one of the three constitutions, decided by its kind and declared purity. | S3 authoring_decisions Place every transform under exactly one of the three constitutions by its kind and declared purity | governance rule |
| 15 | Every result a non-deterministic atom produced is recorded. | S1 business_invariants #9 | invariant |
| 16 | A replay reproduces the same result from the same inputs and recorded outcomes, and never runs a non-deterministic atom. | S1 business_invariants #10 | invariant |
| 17 | Nothing routes directly on a non-deterministic atom's result. | S1 business_invariants #11 | invariant |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions State how a molecule runs: declared step order, one pass per member of the loop's collection, no molecule containing itself, a molecule's declared purity checked against its steps | State how a molecule runs: declared step order, one pass per member of the loop's collection, no molecule containing itself, a molecule's declared purity checked against its steps | capability_transforms | NEW |
| GAP-02 | S3 authoring_decisions Admit an atom that declares its result is not determined by its inputs, and forbid it side effects | Admit an atom that declares its result is not determined by its inputs, and forbid it side effects | capability_transforms | NEW |
| GAP-03 | S3 authoring_decisions Place every transform under exactly one of the three constitutions by its kind and declared purity | Place every transform under exactly one of the three constitutions by its kind and declared purity | capability_transforms | NEW |
| GAP-04 | S3 authoring_decisions Refuse at build a molecule whose steps or loop body cannot be run, one that contains itself, or one declared pure with a step that is not | Refuse at build a molecule whose steps or loop body cannot be run, one that contains itself, or one declared pure with a step that is not | compiler | EXTEND |
| GAP-05 | S3 authoring_decisions Run a molecule's steps in order, including a composed body once per pass of a loop, carrying values between passes | Run a molecule's steps in order, including a composed body once per pass of a loop, carrying values between passes | execution | EXTEND |
| GAP-06 | S3 authoring_decisions Write one evidence record per step a molecule runs, naming its results and not their values | Write one evidence record per step a molecule runs, naming its results and not their values | execution | EXTEND |
| GAP-07 | S3 authoring_decisions State a molecule's steps, loop and emission in a design, and render them at full determinacy | State a molecule's steps, loop and emission in a design, and render them at full determinacy | design | EXTEND |
| GAP-08 | S3 authoring_decisions Show the path holds with a composed transform designed, constructed, compiled and run end to end | Show the path holds with a composed transform designed, constructed, compiled and run end to end | workload | NEW |
| GAP-09 | S3 authoring_decisions Record every result a non-deterministic atom produces, and replay a run from the recorded results | Record every result a non-deterministic atom produces, and replay a run from the recorded results | execution | NEW |
| GAP-10 | S3 authoring_decisions Refuse at build a composition in which anything routes on a non-deterministic atom's result before a deterministic step has consumed it | Refuse at build a composition in which anything routes on a non-deterministic atom's result before a deterministic step has consumed it | compiler | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The existing constitution stays unchanged and keeps governing every existing transform; two sibling constitutions govern molecules and atoms declaring they are not deterministic. | S3 analysis_findings #1 | The platform grows by adding, not by re-authoring what exists. Decided by the business owner. | No existing transform, contract or workflow changes. |
| 2 | Molecules and non-deterministic atoms are separate concerns in separate constitutions. | S3 authoring_decisions State how a molecule runs: declared step order, one pass per member of the loop's collection, no molecule containing itself, a molecule's declared purity checked against its steps | Kind and determinism are two axes; one constitution for both repeats the conflation that caused this. | Three constitutions govern transforms, each for one concern. |
| 3 | A transform is placed under exactly one constitution by its kind and declared purity, and an invariant enforces it. | S3 authoring_decisions Place every transform under exactly one of the three constitutions by its kind and declared purity | Placement decided by what a transform declares cannot be escaped by naming the wrong constitution. | A deterministic atom names the existing constitution; a molecule, the molecule constitution; a non-deterministic atom, the non-deterministic atom constitution. |
| 4 | The existing constitution's accurate name is deferred to its next version, made for its own reasons. | S3 analysis_findings #3 | Renaming now would supersede it and re-point every transform. Agreed by the business owner. | Each sibling states the partition explicitly until then. |
| 5 | The one transform declaring that it emits a final value is a deterministic atom. | S3 analysis_findings #6 | It passes its input through unchanged. | It stays under the existing constitution. |
| 6 | A loop runs every pass; a finished loop carries that fact forward and the remaining passes change nothing. | S1 constraints #2 | A loop's length never depends on the data it computes. Decided by the business author. | No early exit exists to design. |
| 7 | Every step a molecule runs leaves one evidence record naming its results, in the same form as a governed operation's steps. | S3 analysis_findings #7 | A decision inside a molecule is observable when made, with no new evidence kind. | Volume grows with passes; compared values do not. |
| 8 | Rules, compiler, runtime and design language land together. | S3 analysis_findings #9 | No partial state in which a molecule runs but cannot be designed, or the reverse. | One delivery. |
| 9 | The end-to-end evidence is a platform conformance workload with a loop whose body is itself a molecule, using no language model. | S3 analysis_findings #8 | Evidence independent of the domain that found the gap. | Its placement is decided at Stage 7. |
| 10 | Determinism holds relative to recorded outcomes: every non-deterministic result is recorded when produced, and replay substitutes it. | S3 analysis_findings #10 | The standard requires determinism and replay; the clock already follows this principle. Agreed by the business owner. | The runtime records values, not only result names, for non-deterministic atoms. |
| 11 | A non-deterministic atom's results may be offered, never decided. | S3 analysis_findings #11 | Governance stays in the deterministic steps. | The compiler refuses routing on such a result before a deterministic step has consumed it. |

---

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| State how a molecule runs: declared step order, one pass per member of the loop's collection, no molecule containing itself, a molecule's declared purity checked against its steps | GAP-01 |
| Admit an atom that declares its result is not determined by its inputs, and forbid it side effects | GAP-02 |
| Place every transform under exactly one of the three constitutions by its kind and declared purity | GAP-03 |
| Refuse at build a molecule whose steps or loop body cannot be run, one that contains itself, or one declared pure with a step that is not | GAP-04 |
| Run a molecule's steps in order, including a composed body once per pass of a loop, carrying values between passes | GAP-05 |
| Write one evidence record per step a molecule runs, naming its results and not their values | GAP-06 |
| State a molecule's steps, loop and emission in a design, and render them at full determinacy | GAP-07 |
| Show the path holds with a composed transform designed, constructed, compiled and run end to end | GAP-08 |
| Record every result a non-deterministic atom produces, and replay a run from the recorded results | GAP-09 |
| Refuse at build a composition in which anything routes on a non-deterministic atom's result before a deterministic step has consumed it | GAP-10 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Renaming the existing constitution for deterministic atoms | Deferred to its next version, made for its own reasons |
| What any domain composes | Each domain states its own molecules in its own change |
| Whether any domain uses a non-deterministic transform | Each domain decides, and declares it where it is made |
| A loop that stops early | Rejected by the business author |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
