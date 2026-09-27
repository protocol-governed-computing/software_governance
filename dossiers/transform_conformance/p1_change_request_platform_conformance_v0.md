# Stage 1 — Change Request: Clarification & Fact Capture: platform / conformance
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** transform_conformance
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
| conformance | MODIFY | The platform governs transform conformance and no transform in the composition has been proven by it. Conformance was deliberately taken out of the platform's own build so that each domain would run it in its own, and no domain does; no transform has a vector, and the design language cannot state one. The rules over vectors pass on nothing. Molecules, and steps whose results are recorded and replayed, are now the transforms whose behaviour is hardest to see, and nothing proves them as part of the composition. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Transform | A unit of computation a governed act performs, whose implementation lives outside the composition. | CR seed §2 Business Vocabulary #1 |
| Molecule | A transform composed of other transforms, run as a stated sequence of steps. | CR seed §2 Business Vocabulary #2 |
| Non-deterministic step | A step declared as one whose result is not determined by its inputs. | CR seed §2 Business Vocabulary #3 |
| Recorded result | A result a non-deterministic step produced, kept when it was produced. | CR seed §2 Business Vocabulary #4 |
| Replay | Reproducing a run using recorded results in place of non-deterministic steps. | CR seed §2 Business Vocabulary #5 |
| Conformance | Proof that a transform does what its declaration says, carried in the composition. | CR seed §2 Business Vocabulary #6 |
| Test vector | Stated inputs and the outputs a transform must produce from them. | CR seed §2 Business Vocabulary #7 |
| Runnable case | A test vector bound to the transform as the composition sealed it, ready to run. | CR seed §2 Business Vocabulary #8 |
| Runner | What executes runnable cases and reports each as passed or failed. | CR seed §2 Business Vocabulary #9 |
| Proven | A transform whose vectors all ran and passed. | CR seed §2 Business Vocabulary #10 |
| Unproven | A transform no vector tests; never counted as passing. | CR seed §2 Business Vocabulary #11 |
| Shape assertion | A check that a result has a stated form, without stating its value. | CR seed §2 Business Vocabulary #12 |
| Domain build | The build in which a domain's own declarations and implementations are compiled. | CR seed §2 Business Vocabulary #13 |
| Composition conformance | The platform's check of properties that exist only once domains are composed; a different kind of evidence from transform conformance. | CR seed §2 Business Vocabulary #14 |
| Design | The statement of what a change will build, from which construction renders artifacts. | CR seed §2 Business Vocabulary #15 |
| Construction | Rendering the artifacts a design determines, at full determinacy or not at all. | CR seed §2 Business Vocabulary #16 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A design can state test vectors for the transforms it authors, and construction renders them as declarations like any other artifact. | CR seed §3 Requested Outcomes #1 |
| Every transform's vectors run in the build of the domain that supplies it, against the transform as the composition sealed it, and the domain is refused if any vector fails. | CR seed §3 Requested Outcomes #2 |
| A molecule is proven by its vectors, run whole, as the composition sealed it. | CR seed §3 Requested Outcomes #3 |
| A molecule containing a non-deterministic step is proven with the step's results supplied as recorded, so the expected result is exact and the vector proves that a replay uses the record and does not run the step. | CR seed §3 Requested Outcomes #4 |
| No transform is reported as proven when nothing proved it. | CR seed §3 Requested Outcomes #5 |
| The runner's cases are kept apart from composition conformance evidence. | CR seed §3 Requested Outcomes #6 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A transform's declaration says what it takes and what it yields; its implementation is code outside the composition. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| The composition vouches for a transform's declaration and cannot vouch for its code. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A test vector states inputs and the outputs a transform must produce from them. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| When conformance runs, each vector is run against the transform exactly as the composition sealed it, and a transform that fails its vectors is refused. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Vectors are declarations, so what a transform was proven to do is part of the composition a reader can inspect. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A constitution states what a vector is, three invariants hold vectors to the transforms they test, the compiler turns vectors into runnable cases, and the runtime carries the runner. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The reference implementation this platform was derived from ran conformance on every build and failed the build on any vector that failed. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| Conformance was deliberately taken out of the platform's own build when the platform was narrowed to its normative surface. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A transform's implementation belongs to the domain that supplies it, so conformance against it belongs in that domain's build. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| The platform's build manifest records that decision. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| No domain's build declares where its vectors are read from or where its runnable cases are written. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| No build step invokes the runner. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| No transform in the composition has a vector. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| The vectors the reference implementation carried were not brought across when its domains were rebuilt through the governed design path. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| The design language has no way to state a vector, so no design could author one and no construction could render one. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| The three invariants governing vectors are checked on every build, find none, and report success. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| A rule that has never had anything to judge reports the same result as a rule that judged everything and found it sound. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| The runner reads its cases from a place in the snapshot that composition conformance now uses for a different kind of evidence. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| A molecule is composed of other transforms and may contain a non-deterministic step whose every result is recorded and replayed. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| Molecules and non-deterministic steps are the transforms whose behaviour is hardest to see from outside. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| Nothing proves a molecule outside a bespoke test written for one example. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| Proving transforms in hand-written tests beside the code was rejected: the proof is outside the composition and a transform can enter it unproven with nothing noticing. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| Restoring conformance to the platform's own build was rejected: the platform does not own a domain's implementations and cannot vouch for them. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| Amending the runner alone would run conformance, find no vectors, and pass. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| A transform that exists when this change lands and has no vector is reported by name as unproven, never counted as passing. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| A transform a change authors or amends after this change is refused without a vector. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| A vector for a non-deterministic step run on its own asserts the shape of what it yields, never its values. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| The runner already supports asserting a field's form rather than its content. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| The values a non-deterministic step yields are proven in the molecule that consumes it, with its results supplied as recorded. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| A failed vector stops the domain's build, and the domain is not admitted to any composition. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| Vectors are authored in the design, like every other declaration; a vector written by hand beside the code is proof nobody gated. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| The evidence for this change must not come from a domain that needs it. | HIGH | CR seed §4 Known Facts — Business Truths #32 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| No transform in the composition has a vector. | Decides whether every existing transform is reported unproven. | Confirm what vectors the composition carries, and for which transforms. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The invariants governing vectors report success over no vectors. | Establishes that the rules pass on nothing today. | Establish what each invariant governing vectors checks, and what it reports with none present. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| No domain build declares conformance. | The domain half of the change. | Establish what each domain's build manifest declares about vectors and runnable cases. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The design language cannot state a vector. | The design half of the change. | Establish which registers describe a transform, and whether any states a vector. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The runner and composition conformance read and write the same place. | Decides whether they must be separated before the runner can be used. | Establish where the runner reads its cases and where composition conformance writes its evidence. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| The runner cannot supply recorded results to a non-deterministic step. | Decides whether proving a molecule with such a step extends the runner. | Establish how the runner executes a case and what it hands the executor. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |
| The constitution governing vectors says a transform produces its outputs deterministically. | Decides whether it needs a new version to admit recorded results. | Establish what the constitution governing vectors requires of a transform and of a vector. | CR seed §5 Existing-System Beliefs — Requiring Verification #7 |

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
| A domain's transforms are proven in that domain's own build, never in the platform's. | Business policy | CR seed §7 Constraints #1 |
| A vector is run against the transform as the composition sealed it. | Business policy | CR seed §7 Constraints #2 |
| A molecule is proven whole. | Business policy | CR seed §7 Constraints #3 |
| A vector for a molecule with a non-deterministic step supplies that step's recorded results. | Business policy | CR seed §7 Constraints #4 |
| A vector for a non-deterministic step on its own asserts shape, never values. | Business policy | CR seed §7 Constraints #5 |
| No transform is counted as passing when no vector tests it. | Business policy | CR seed §7 Constraints #6 |
| A failed vector stops the domain's build. | Business policy | CR seed §7 Constraints #7 |
| Vectors are authored in the design, never by hand beside the code. | Business policy | CR seed §7 Constraints #8 |
| Amending the runner without the design, domain build and evidence halves is not an acceptable partial change. | Business policy | CR seed §7 Constraints #9 |
| The evidence for this change comes from the platform's own conformance evidence, not from a domain that needs it. | Business policy | CR seed §7 Constraints #10 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every vector tests a transform the composition declares. | CR seed §8 Business Invariants #1 |
| Every vector runs against the transform as sealed. | CR seed §8 Business Invariants #2 |
| A domain with a failed vector is not admitted to a composition. | CR seed §8 Business Invariants #3 |
| Every transform is either proven or named as unproven. | CR seed §8 Business Invariants #4 |
| A vector supplies recorded results for exactly the non-deterministic steps of what it tests. | CR seed §8 Business Invariants #5 |
| No vector's run runs a non-deterministic step whose result it supplies. | CR seed §8 Business Invariants #6 |
| Transform conformance evidence and composition conformance evidence are kept apart. | CR seed §8 Business Invariants #7 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Transform | Unproven | No vector tests it; it is named, never counted as passing. | CR seed §9 Lifecycle States #1 |
| Transform | Proven | Every vector that tests it ran against it as sealed and passed. | CR seed §9 Lifecycle States #2 |
| Transform | Refused | A vector that tests it failed; its domain is not admitted. | CR seed §9 Lifecycle States #3 |
| Test vector | Declared | A design states it and construction renders it. | CR seed §9 Lifecycle States #4 |
| Test vector | Passed | It ran against its transform as sealed and the result matched. | CR seed §9 Lifecycle States #5 |
| Test vector | Failed | It ran and the result did not match, or a step it supplies was run. | CR seed §9 Lifecycle States #6 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A domain's transforms were proven | When a domain's build runs its vectors and all pass | What each transform does is evidence in the composition, not a claim beside it. | CR seed §10 Business Events #1 |
| A domain was refused for a failed vector | When a vector fails in the domain's build | A transform that does not do what it says never enters a composition. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a vector is, what it may assert, and what counts as proven | The platform | CR seed §11 Authority Boundaries #1 |
| Where a domain's transforms are proven | The domain that supplies them | CR seed §11 Authority Boundaries #2 |
| Which vectors a transform has | The design that states it | CR seed §11 Authority Boundaries #3 |
| How much proof is enough beyond one vector | The design that states it | CR seed §11 Authority Boundaries #4 |
| How a design states a vector | The design language | CR seed §11 Authority Boundaries #5 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What any transform does | Each domain states its transforms and their vectors in its own change. | CR seed §12 Out of Scope #1 |
| Vectors for transforms that already exist | Each is named unproven until a change gives it vectors; none is written here on behalf of a domain. | CR seed §12 Out of Scope #2 |
| How much proof is enough | One vector per transform is a floor, not a standard of sufficiency. | CR seed §12 Out of Scope #3 |
| Returning conformance to the platform's own build | Rejected by the business author: the platform does not own a domain's implementations. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| conformance | MODIFIED | CR seed §13 Governance Scope #1 |
| design | EXTENDED | CR seed §13 Governance Scope #2 |
| capability_transforms | ADJACENT | CR seed §13 Governance Scope #3 |

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
| A design states vectors for a transform, and construction renders them at full determinacy. | CR seed §15 Acceptance Criteria #1 |
| A domain's build runs every vector against its transform as sealed and reports each transform proven or unproven by name. | CR seed §15 Acceptance Criteria #2 |
| A vector whose result does not match fails, and the domain's build stops. | CR seed §15 Acceptance Criteria #3 |
| A molecule with a loop over a molecule is proven by a vector run whole. | CR seed §15 Acceptance Criteria #4 |
| A molecule containing a non-deterministic step is proven by a vector supplying that step's recorded results, and the step is not run. | CR seed §15 Acceptance Criteria #5 |
| A vector that supplies recorded results for a deterministic step, or omits them for a non-deterministic one, is refused. | CR seed §15 Acceptance Criteria #6 |
| A non-deterministic step on its own is proven by the shape of what it yields. | CR seed §15 Acceptance Criteria #7 |
| Every transform that exists when this change lands, and has no vector, is reported unproven by name. | CR seed §15 Acceptance Criteria #8 |
| A transform authored after this change without a vector is refused. | CR seed §15 Acceptance Criteria #9 |
| The invariants governing vectors no longer report success over no vectors. | CR seed §15 Acceptance Criteria #10 |
| Transform conformance evidence and composition conformance evidence are read and written in separate places. | CR seed §15 Acceptance Criteria #11 |
| The evidence is part of the platform's own conformance evidence. | CR seed §15 Acceptance Criteria #12 |

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
| Transform | Unproven | Proven | A change gives it vectors and they pass in its domain's build. | None. | CR seed §17 Lifecycle Transitions #1 |
| Transform | Unproven | Refused | A change gives it vectors and one fails. | Its domain is not admitted. | CR seed §17 Lifecycle Transitions #2 |
| Transform | Proven | Refused | A later build runs a vector that now fails. | Its domain is not admitted. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Build a domain | A vector fails against its transform as sealed. | A transform that does not do what it says never enters a composition. | CR seed §18 Operation Refusals #1 |
| Build a domain | A transform authored or amended after this change has no vector. | A new transform enters the composition proven. | CR seed §18 Operation Refusals #2 |
| Build a domain | A vector supplies recorded results for a deterministic step, or omits them for a non-deterministic one. | A vector that does not match what it tests proves nothing about it. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Vectors for each transform that already exists | The domain that owns it | That domain's next change to the transform | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
