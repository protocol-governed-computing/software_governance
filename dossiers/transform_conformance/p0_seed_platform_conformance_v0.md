# Change Seed — platform / conformance

**Stage:** 0 — Change Seed
**CR:** transform_conformance
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the four clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The conformance subdomain governs how the platform proves that what a composition declares is what
runs. For a transform, whose implementation lives outside the composition, the proof is its test
vectors: stated inputs and the outputs the transform must produce from them, run against the transform
exactly as the composition sealed it. Its authority is to decide what a vector is, what it may assert,
where it is run and what counts as proven, and it decides nothing about what any transform computes or
how much proof a design judges enough.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| conformance | MODIFY | The platform governs transform conformance and no transform in the composition has been proven by it. Conformance was deliberately taken out of the platform's own build so that each domain would run it in its own, and no domain does; no transform has a vector, and the design language cannot state one. The rules over vectors pass on nothing. Molecules, and steps whose results are recorded and replayed, are now the transforms whose behaviour is hardest to see, and nothing proves them as part of the composition. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Transform | A unit of computation a governed act performs, whose implementation lives outside the composition. |
| Molecule | A transform composed of other transforms, run as a stated sequence of steps. |
| Non-deterministic step | A step declared as one whose result is not determined by its inputs. |
| Recorded result | A result a non-deterministic step produced, kept when it was produced. |
| Replay | Reproducing a run using recorded results in place of non-deterministic steps. |
| Conformance | Proof that a transform does what its declaration says, carried in the composition. |
| Test vector | Stated inputs and the outputs a transform must produce from them. |
| Runnable case | A test vector bound to the transform as the composition sealed it, ready to run. |
| Runner | What executes runnable cases and reports each as passed or failed. |
| Proven | A transform whose vectors all ran and passed. |
| Unproven | A transform no vector tests; never counted as passing. |
| Shape assertion | A check that a result has a stated form, without stating its value. |
| Domain build | The build in which a domain's own declarations and implementations are compiled. |
| Composition conformance | The platform's check of properties that exist only once domains are composed; a different kind of evidence from transform conformance. |
| Design | The statement of what a change will build, from which construction renders artifacts. |
| Construction | Rendering the artifacts a design determines, at full determinacy or not at all. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A design can state test vectors for the transforms it authors, and construction renders them as declarations like any other artifact. |
| Every transform's vectors run in the build of the domain that supplies it, against the transform as the composition sealed it, and the domain is refused if any vector fails. |
| A molecule is proven by its vectors, run whole, as the composition sealed it. |
| A molecule containing a non-deterministic step is proven with the step's results supplied as recorded, so the expected result is exact and the vector proves that a replay uses the record and does not run the step. |
| No transform is reported as proven when nothing proved it. |
| The runner's cases are kept apart from composition conformance evidence. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A transform's declaration says what it takes and what it yields; its implementation is code outside the composition. | HIGH |
| The composition vouches for a transform's declaration and cannot vouch for its code. | HIGH |
| A test vector states inputs and the outputs a transform must produce from them. | HIGH |
| When conformance runs, each vector is run against the transform exactly as the composition sealed it, and a transform that fails its vectors is refused. | HIGH |
| Vectors are declarations, so what a transform was proven to do is part of the composition a reader can inspect. | HIGH |
| A constitution states what a vector is, three invariants hold vectors to the transforms they test, the compiler turns vectors into runnable cases, and the runtime carries the runner. | HIGH |
| The reference implementation this platform was derived from ran conformance on every build and failed the build on any vector that failed. | HIGH |
| Conformance was deliberately taken out of the platform's own build when the platform was narrowed to its normative surface. | HIGH |
| A transform's implementation belongs to the domain that supplies it, so conformance against it belongs in that domain's build. | HIGH |
| The platform's build manifest records that decision. | HIGH |
| No domain's build declares where its vectors are read from or where its runnable cases are written. | HIGH |
| No build step invokes the runner. | HIGH |
| No transform in the composition has a vector. | HIGH |
| The vectors the reference implementation carried were not brought across when its domains were rebuilt through the governed design path. | HIGH |
| The design language has no way to state a vector, so no design could author one and no construction could render one. | HIGH |
| The three invariants governing vectors are checked on every build, find none, and report success. | HIGH |
| A rule that has never had anything to judge reports the same result as a rule that judged everything and found it sound. | HIGH |
| The runner reads its cases from a place in the snapshot that composition conformance now uses for a different kind of evidence. | HIGH |
| A molecule is composed of other transforms and may contain a non-deterministic step whose every result is recorded and replayed. | HIGH |
| Molecules and non-deterministic steps are the transforms whose behaviour is hardest to see from outside. | HIGH |
| Nothing proves a molecule outside a bespoke test written for one example. | HIGH |
| Proving transforms in hand-written tests beside the code was rejected: the proof is outside the composition and a transform can enter it unproven with nothing noticing. | HIGH |
| Restoring conformance to the platform's own build was rejected: the platform does not own a domain's implementations and cannot vouch for them. | HIGH |
| Amending the runner alone would run conformance, find no vectors, and pass. | HIGH |
| A transform that exists when this change lands and has no vector is reported by name as unproven, never counted as passing. | HIGH |
| A transform a change authors or amends after this change is refused without a vector. | HIGH |
| A vector for a non-deterministic step run on its own asserts the shape of what it yields, never its values. | HIGH |
| The runner already supports asserting a field's form rather than its content. | HIGH |
| The values a non-deterministic step yields are proven in the molecule that consumes it, with its results supplied as recorded. | HIGH |
| A failed vector stops the domain's build, and the domain is not admitted to any composition. | HIGH |
| Vectors are authored in the design, like every other declaration; a vector written by hand beside the code is proof nobody gated. | HIGH |
| The evidence for this change must not come from a domain that needs it. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| No transform in the composition has a vector. | Decides whether every existing transform is reported unproven. | Confirm what vectors the composition carries, and for which transforms. |
| The invariants governing vectors report success over no vectors. | Establishes that the rules pass on nothing today. | Establish what each invariant governing vectors checks, and what it reports with none present. |
| No domain build declares conformance. | The domain half of the change. | Establish what each domain's build manifest declares about vectors and runnable cases. |
| The design language cannot state a vector. | The design half of the change. | Establish which registers describe a transform, and whether any states a vector. |
| The runner and composition conformance read and write the same place. | Decides whether they must be separated before the runner can be used. | Establish where the runner reads its cases and where composition conformance writes its evidence. |
| The runner cannot supply recorded results to a non-deterministic step. | Decides whether proving a molecule with such a step extends the runner. | Establish how the runner executes a case and what it hands the executor. |
| The constitution governing vectors says a transform produces its outputs deterministically. | Decides whether it needs a new version to admit recorded results. | Establish what the constitution governing vectors requires of a transform and of a vector. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| A domain's transforms are proven in that domain's own build, never in the platform's. | Business policy |
| A vector is run against the transform as the composition sealed it. | Business policy |
| A molecule is proven whole. | Business policy |
| A vector for a molecule with a non-deterministic step supplies that step's recorded results. | Business policy |
| A vector for a non-deterministic step on its own asserts shape, never values. | Business policy |
| No transform is counted as passing when no vector tests it. | Business policy |
| A failed vector stops the domain's build. | Business policy |
| Vectors are authored in the design, never by hand beside the code. | Business policy |
| Amending the runner without the design, domain build and evidence halves is not an acceptable partial change. | Business policy |
| The evidence for this change comes from the platform's own conformance evidence, not from a domain that needs it. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every vector tests a transform the composition declares. |
| Every vector runs against the transform as sealed. |
| A domain with a failed vector is not admitted to a composition. |
| Every transform is either proven or named as unproven. |
| A vector supplies recorded results for exactly the non-deterministic steps of what it tests. |
| No vector's run runs a non-deterministic step whose result it supplies. |
| Transform conformance evidence and composition conformance evidence are kept apart. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Transform | Unproven | No vector tests it; it is named, never counted as passing. |
| Transform | Proven | Every vector that tests it ran against it as sealed and passed. |
| Transform | Refused | A vector that tests it failed; its domain is not admitted. |
| Test vector | Declared | A design states it and construction renders it. |
| Test vector | Passed | It ran against its transform as sealed and the result matched. |
| Test vector | Failed | It ran and the result did not match, or a step it supplies was run. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A domain's transforms were proven | When a domain's build runs its vectors and all pass | What each transform does is evidence in the composition, not a claim beside it. |
| A domain was refused for a failed vector | When a vector fails in the domain's build | A transform that does not do what it says never enters a composition. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a vector is, what it may assert, and what counts as proven | The platform |
| Where a domain's transforms are proven | The domain that supplies them |
| Which vectors a transform has | The design that states it |
| How much proof is enough beyond one vector | The design that states it |
| How a design states a vector | The design language |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What any transform does | Each domain states its transforms and their vectors in its own change. |
| Vectors for transforms that already exist | Each is named unproven until a change gives it vectors; none is written here on behalf of a domain. |
| How much proof is enough | One vector per transform is a floor, not a standard of sufficiency. |
| Returning conformance to the platform's own build | Rejected by the business author: the platform does not own a domain's implementations. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| conformance | MODIFIED |
| design | EXTENDED |
| capability_transforms | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A design states vectors for a transform, and construction renders them at full determinacy. |
| A domain's build runs every vector against its transform as sealed and reports each transform proven or unproven by name. |
| A vector whose result does not match fails, and the domain's build stops. |
| A molecule with a loop over a molecule is proven by a vector run whole. |
| A molecule containing a non-deterministic step is proven by a vector supplying that step's recorded results, and the step is not run. |
| A vector that supplies recorded results for a deterministic step, or omits them for a non-deterministic one, is refused. |
| A non-deterministic step on its own is proven by the shape of what it yields. |
| Every transform that exists when this change lands, and has no vector, is reported unproven by name. |
| A transform authored after this change without a vector is refused. |
| The invariants governing vectors no longer report success over no vectors. |
| Transform conformance evidence and composition conformance evidence are read and written in separate places. |
| The evidence is part of the platform's own conformance evidence. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Transform | Unproven | Proven | A change gives it vectors and they pass in its domain's build. | None. |
| Transform | Unproven | Refused | A change gives it vectors and one fails. | Its domain is not admitted. |
| Transform | Proven | Refused | A later build runs a vector that now fails. | Its domain is not admitted. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Build a domain | A vector fails against its transform as sealed. | A transform that does not do what it says never enters a composition. |
| Build a domain | A transform authored or amended after this change has no vector. | A new transform enters the composition proven. |
| Build a domain | A vector supplies recorded results for a deterministic step, or omits them for a non-deterministic one. | A vector that does not match what it tests proves nothing about it. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Vectors for each transform that already exists | The domain that owns it | That domain's next change to the transform |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
