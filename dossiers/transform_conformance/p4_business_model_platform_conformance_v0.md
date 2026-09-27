# Stage 4 — Business Model: platform / conformance

**Stage:** 4 — Business Model
**CR:** transform_conformance
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

This document consolidates Stages 1 to 3. It re-litigates nothing and introduces no design: every
row carries the prior-stage finding it came from, and every capability Stage 3 committed appears in
the capability graph exactly as Stage 3 stated it. One question Stage 3 left implicit was settled by
the business owner here: how often a domain's vectors run.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The platform | Decides what a vector is, what it may assert, and what counts as proven. | Declaring — the rules of proof are its to state. | S1 authority_boundaries #1 |
| The domain that supplies a transform | Proves its transforms in its own build. | Deciding — a domain whose transform fails its vectors is not admitted. | S1 authority_boundaries #2 |
| The design of a change | States which vectors each transform it authors or amends has, and how much proof is enough. | Declaring — within the rules the platform states. | S1 authority_boundaries #3 |
| The design language | Decides how a design states a vector, and refuses a transform authored without one. | Declaring — the registers a design may fill are its to define. | S1 authority_boundaries #5 |
| The runner | Runs each vector against its transform as sealed and reports the result. | Executing — it runs what the domain's build hands it and nothing else. | S2 entities Runner |
| A reader of the composition | Sees which transforms were proven, which were not, and which code the composition vouches for. | Observing — the party an unproven transform reported as passing misleads. | S1 known_facts — vectors are declarations, so what a transform was proven to do is part of the composition a reader can inspect |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Transform | A unit of computation whose implementation lives outside the composition. | Declared and sealed; proven, unproven or refused by its vectors. | S2 entities Transform |
| Test vector | Stated inputs and the outputs a transform must produce from them, with recorded results for a molecule's non-deterministic steps. | Declared by a design, rendered by construction, compiled with its domain. | S2 entities Test vector |
| Runnable case | A vector bound to its transform as sealed. | Written into the domain's own build output. | S2 entities Runnable case |
| Runner | What executes runnable cases. | Invoked by each domain's build, on every build. | S2 entities Runner |
| Domain conformance result | Every transform of a domain named proven, unproven or refused, with counts. | Written by the domain's build and carried into the composition as its own evidence. | S3 analysis_findings #7 |
| Composition conformance evidence | The platform's record of properties checked once domains are composed. | Unchanged, in its own place. | S2 entities Composition conformance evidence |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The constitution governing vectors | Its new version, stating what a vector proves and what counts as proven | S3 analysis_findings #1 |
| The design language | The registers a design fills, extended to state vectors | S3 analysis_findings #9 |
| The conformance workloads | The platform's own evidence, extended with molecules and vectors in their next change | S3 analysis_findings #10 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A domain's transforms were proven | A domain's build runs its vectors and all pass | What each transform does is evidence in the composition, not a claim beside it | S1 business_events #1 |
| A domain was refused for a failed vector | A vector fails in the domain's build | A transform that does not do what it says never enters a composition | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Test vector | tests | Transform as sealed | Run every vector against its transform as sealed | S1 business_invariants #2 |
| Test vector | supplies | Recorded results | Supply recorded results for exactly the non-deterministic steps of what it tests | S1 business_invariants #5 |
| Domain | is refused for | A failed vector | Stop the domain's build on a failed vector | S1 business_invariants #3 |
| Transform | is named | Proven or unproven | Report every transform by name | S1 business_invariants #4 |
| Runnable case | is kept apart from | Composition conformance evidence | Separate the two places | S1 business_invariants #7 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| State what a vector proves: a transform as sealed, a molecule whole, recorded results for exactly its non-deterministic steps, shape alone for a non-deterministic step on its own, and unproven where nothing tests | S3 authoring_decisions State what a vector proves: a transform as sealed, a molecule whole, recorded results for exactly its non-deterministic steps, shape alone for a non-deterministic step on its own, and unproven where nothing tests | CRITICAL | GAP-01 | The constitution admits deterministic outputs only. |
| Hold a vector's assertions to known forms by a check that runs | S3 authoring_decisions Hold a vector's assertions to known forms by a check that runs | CRITICAL | GAP-02 | Bound to a compiler phase that does not exist. |
| Hold a vector's outputs to its transform, and each case to a declared outcome | S3 authoring_decisions Hold a vector's outputs to its transform, and each case to a declared outcome | SATISFIED |  | Reused as-is. |
| Refuse a vector whose recorded results do not match the purity of the steps it tests | S3 authoring_decisions Refuse a vector whose recorded results do not match the purity of the steps it tests | MAJOR | GAP-03 | Nothing checks it. |
| Run every transform's vectors in its domain's build, and stop the build on a failure | S3 authoring_decisions Run every transform's vectors in its domain's build, and stop the build on a failure | CRITICAL | GAP-04 | No build runs conformance. |
| Prove a molecule with a non-deterministic step by supplying its recorded results, and confirm the step was not run | S3 authoring_decisions Prove a molecule with a non-deterministic step by supplying its recorded results, and confirm the step was not run | CRITICAL | GAP-05 | The runner supplies no recorded results. |
| Report every transform proven, unproven or refused by name, never success over nothing | S3 authoring_decisions Report every transform proven, unproven or refused by name, never success over nothing | CRITICAL | GAP-06 | Every rule over vectors reports success over none. |
| Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | S3 authoring_decisions Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | MAJOR | GAP-07 | The two collide, and no result is carried. |
| State vectors in a design and render them, and refuse a transform authored or amended without one | S3 authoring_decisions State vectors in a design and render them, and refuse a transform authored or amended without one | CRITICAL | GAP-08 | The design language cannot state a vector. |
| Show a molecule with a non-deterministic step proven in a composition | S3 authoring_decisions Show a molecule with a non-deterministic step proven in a composition | MAJOR | GAP-09 | Arrives with the conformance workloads' next change. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| conformance | conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0 | governance read | SATISFIED | S3 dependency_discoveries #3 |
| conformance | capability_transforms::INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0 | governance read | SATISFIED | S3 dependency_discoveries #4 |
| conformance | capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | governance read | SATISFIED | S3 dependency_discoveries #5 |
| conformance | capability_transforms::CONSTITUTION_MOLECULES_V0 | governance read | SATISFIED | S3 dependency_discoveries #6 |
| conformance | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | governance read | SATISFIED | S3 dependency_discoveries #7 |
| conformance | structure | domain build manifest | GAP | S3 dependency_discoveries #9 |
| conformance | compiler | case generation | GAP | S3 dependency_discoveries #10 |
| conformance | execution | runner | GAP | S3 dependency_discoveries #11 |
| conformance | composition | carried evidence | GAP | S3 dependency_discoveries #12 |
| conformance | design | design language | GAP | S3 dependency_discoveries #13 |
| conformance | process | regression | GAP | S3 dependency_discoveries #14 |

The gaps are carried by this change and land together: the rules first, then the build manifest, the
compiler, the runner, the assembler and the design language, with the regression running them.

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Every vector tests a transform the composition declares. | S1 business_invariants #1 | invariant |
| 2 | Every vector runs against the transform as sealed. | S1 business_invariants #2 | invariant |
| 3 | A domain with a failed vector is not admitted to a composition. | S1 business_invariants #3 | invariant |
| 4 | Every transform is either proven or named as unproven. | S1 business_invariants #4 | invariant |
| 5 | A vector supplies recorded results for exactly the non-deterministic steps of what it tests. | S1 business_invariants #5 | invariant |
| 6 | No vector's run runs a non-deterministic step whose result it supplies. | S1 business_invariants #6 | invariant |
| 7 | Transform conformance evidence and composition conformance evidence are kept apart. | S1 business_invariants #7 | invariant |
| 8 | A domain's transforms are proven in that domain's own build, never in the platform's. | S1 constraints #1 | business policy |
| 9 | A vector for a non-deterministic step on its own asserts shape, never values. | S1 constraints #5 | business policy |
| 10 | Vectors are authored in the design, never by hand beside the code. | S1 constraints #8 | business policy |
| 11 | Amending the runner without the design, domain build and evidence halves is not an acceptable partial change. | S1 constraints #9 | business policy |
| 12 | The evidence for this change comes from the platform's own conformance evidence, not from a domain that needs it. | S1 constraints #10 | business policy |
| 13 | A transform authored or amended after this change is refused at design without a vector. | S3 analysis_findings #3 | governance rule |
| 14 | Every build runs every vector; no earlier result stands for a later build. | S3 analysis_findings #5 | business policy |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions State what a vector proves: a transform as sealed, a molecule whole, recorded results for exactly its non-deterministic steps, shape alone for a non-deterministic step on its own, and unproven where nothing tests | State what a vector proves: a transform as sealed, a molecule whole, recorded results for exactly its non-deterministic steps, shape alone for a non-deterministic step on its own, and unproven where nothing tests | conformance | EXTEND |
| GAP-02 | S3 authoring_decisions Hold a vector's assertions to known forms by a check that runs | Hold a vector's assertions to known forms by a check that runs | conformance | EXTEND |
| GAP-03 | S3 authoring_decisions Refuse a vector whose recorded results do not match the purity of the steps it tests | Refuse a vector whose recorded results do not match the purity of the steps it tests | conformance | NEW |
| GAP-04 | S3 authoring_decisions Run every transform's vectors in its domain's build, and stop the build on a failure | Run every transform's vectors in its domain's build, and stop the build on a failure | execution | EXTEND |
| GAP-05 | S3 authoring_decisions Prove a molecule with a non-deterministic step by supplying its recorded results, and confirm the step was not run | Prove a molecule with a non-deterministic step by supplying its recorded results, and confirm the step was not run | execution | EXTEND |
| GAP-06 | S3 authoring_decisions Report every transform proven, unproven or refused by name, never success over nothing | Report every transform proven, unproven or refused by name, never success over nothing | execution | EXTEND |
| GAP-07 | S3 authoring_decisions Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | composition | EXTEND |
| GAP-08 | S3 authoring_decisions State vectors in a design and render them, and refuse a transform authored or amended without one | State vectors in a design and render them, and refuse a transform authored or amended without one | design | EXTEND |
| GAP-09 | S3 authoring_decisions Show a molecule with a non-deterministic step proven in a composition | Show a molecule with a non-deterministic step proven in a composition | workload | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The constitution governing vectors is replaced by a new version. | S3 analysis_findings #1 | One artifact names it, and that artifact is itself replaced. | No transform, contract or workflow changes. |
| 2 | The invariant bound to a compiler phase that does not exist is replaced by one a compiler assertion enforces. | S3 analysis_findings #2 | A rule that cannot refuse is the defect this change removes. | Every rule over vectors can refuse. |
| 3 | A transform authored or amended without a vector is refused at Design Intent; at build, every transform without one is named unproven. | S3 analysis_findings #3 | The design is where a new transform can be told from an existing one. Decided by the business owner. | No list of exempt transforms is kept. |
| 4 | Conformance runs in each domain's build, after compiling and before assembly, as a step the build invokes; the compiler never imports the runner. | S3 analysis_findings #5 | Where the platform's build manifest said it belongs, with the layers kept apart. | A failed vector stops the build. |
| 5 | Every build runs every vector, and no result is carried from one build to the next. | S3 analysis_findings #5 | The composition seals a transform's declaration and not its code, so only running the vector shows the code still does what it says; a fingerprint deciding when to skip would itself be a check, costing what running the vectors costs, and would add a record to keep. Decided by the business owner. | Nothing is kept between builds; the result of a build is about that build. |
| 6 | A molecule's vector supplies the recorded results of its non-deterministic steps; the runner confirms each was substituted and none was run. | S3 analysis_findings #6 | Every such vector is also a proof of replay. | The runner hands the executor recorded results. |
| 7 | A domain's result names every transform proven, unproven or refused, with counts, and never reports success over nothing. | S3 analysis_findings #7 | "Conformant" cannot be true of a domain with no proof. | The result states what was not judged. |
| 8 | Runnable cases live in each domain's build output; each domain's result is carried into the composition apart from composition conformance, whose place is unchanged. | S3 analysis_findings #4 | The two collide today, and a sealed release's reader must not see its evidence move. | Two places, named at Stage 7. |
| 9 | Vectors are stated in a design, one row per case, and rendered as one declaration per transform. | S3 analysis_findings #9 | Vectors travel the governed path. | No vector is written by hand. |
| 10 | The evidence of a molecule with a non-deterministic step proven in a composition arrives with the conformance workloads' next change; this change proves the mechanism in the compiler's and runtime's own tests. | S3 analysis_findings #10 | The platform composes no molecule, and no domain that needs one may supply the evidence. Decided by the business owner. | The conformance workloads' next change carries vectors from the start. |

---

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| State what a vector proves: a transform as sealed, a molecule whole, recorded results for exactly its non-deterministic steps, shape alone for a non-deterministic step on its own, and unproven where nothing tests | GAP-01 |
| Hold a vector's assertions to known forms by a check that runs | GAP-02 |
| Refuse a vector whose recorded results do not match the purity of the steps it tests | GAP-03 |
| Run every transform's vectors in its domain's build, and stop the build on a failure | GAP-04 |
| Prove a molecule with a non-deterministic step by supplying its recorded results, and confirm the step was not run | GAP-05 |
| Report every transform proven, unproven or refused by name, never success over nothing | GAP-06 |
| Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | GAP-07 |
| State vectors in a design and render them, and refuse a transform authored or amended without one | GAP-08 |
| Show a molecule with a non-deterministic step proven in a composition | GAP-09 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Vectors for each transform that already exists | Deferred to the domain that owns it, until its next change to the transform |
| What any transform does | Each domain states its transforms and their vectors in its own change |
| How much proof is enough beyond one vector | Each design judges it |
| Sealing the code a composition vouches for | The composition seals declarations and not implementations; running every vector on every build is what binds the two until it does |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
