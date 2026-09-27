# Stage 1 — Change Request: Clarification & Fact Capture: platform / conformance
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** platform_test_data
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
| conformance | MODIFY | The platform supplies twelve transforms and proves none of them. Its build runs no conformance, on a reason that holds for a domain's transforms and not for its own. No domain proves them, correctly, because no domain supplies them. Vectors for eleven exist in the reference implementation and are not used, in a format nothing now reads. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Transform | A unit of computation a governed act performs, whose implementation lives outside the composition. | CR seed §2 Business Vocabulary #1 |
| Platform transform | A transform the platform declares and implements once, which any domain may carry. | CR seed §2 Business Vocabulary #2 |
| Supplier | Whoever implements a transform; its vectors belong to the supplier. | CR seed §2 Business Vocabulary #3 |
| Carried transform | A platform transform a domain uses; the domain's build names it and does not test it. | CR seed §2 Business Vocabulary #4 |
| Test vector | Stated inputs and the outputs a transform must produce from them. | CR seed §2 Business Vocabulary #5 |
| Case | One set of inputs in a vector, with the outcome and outputs it must produce. | CR seed §2 Business Vocabulary #6 |
| Inherited case | A case brought across from the reference implementation. | CR seed §2 Business Vocabulary #7 |
| Reference implementation | The implementation this platform was derived from, which carried hand-written vectors. | CR seed §2 Business Vocabulary #8 |
| Conformance | Proof that a transform does what its declaration says, carried in the composition. | CR seed §2 Business Vocabulary #9 |
| Proven | A transform whose vectors all ran and passed. | CR seed §2 Business Vocabulary #10 |
| Unproven | A transform no vector tests; never counted as passing. | CR seed §2 Business Vocabulary #11 |
| Domain build | The build in which a domain's own declarations and implementations are compiled. | CR seed §2 Business Vocabulary #12 |
| Platform build | The build in which the platform's declarations are compiled. | CR seed §2 Business Vocabulary #13 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The reference implementation's vectors for eleven platform transforms are declarations of the platform, with their cases in the Machine block and their targets named by current identity. | CR seed §3 Requested Outcomes #1 |
| Every inherited case is re-judged against the current declaration and implementation, and a case that no longer holds is corrected or dropped with the reason recorded. | CR seed §3 Requested Outcomes #2 |
| The platform's vectors run in the platform's own build, after its compile succeeds, and the platform is refused if any fails, exactly as a domain's build does. | CR seed §3 Requested Outcomes #3 |
| Each of the eleven platform transforms is reported proven by name, and the twelfth unproven. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| The platform supplies capability transforms that any domain may carry. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Each platform transform is declared and implemented in the platform, once, and every domain that uses one runs the same code. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Every domain build proves its transforms against their test vectors once its compile succeeds. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A domain build names each transform the domain owns as proven, unproven or refused, and names separately each platform transform the domain carries. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A domain build's conformance result is part of the snapshot. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The change that delivered that mechanism deliberately wrote no vectors, leaving each existing transform unproven until a change gave it vectors. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The platform governs every vector: its constitution states what a vector is, what counts as proven, and that a transform's vectors run in the build of the domain that supplies it. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| Each vector belongs to whoever supplies the transform it tests, because what a vector proves is that supplier's code. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| The platform supplies its own transforms, so their vectors are the platform's. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| The platform supplies twelve transforms and proves none of them. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| Conformance was taken out of the platform's build because the platform does not own a domain's implementations. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| That reason holds for a domain's transforms and says nothing about the platform's own; the decision was applied more broadly than its reason. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| The platform's vectors are run in the platform's own build. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| A domain that carries a platform transform names it as carried and does not test it, correctly, because it does not supply it. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| Three of the platform's transforms are carried by no domain. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| The reference implementation carried hand-written vectors for eleven platform transforms the composition still carries under the same codes. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| A read-only run of the inherited cases against the current implementations found ten of the eleven transforms matching on every case. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| The passthrough transform returns its value bare, and whether the runner yields what its vectors expect is confirmed only when it is built. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| The inherited vectors state their cases in prose, under numbered headings, and name their targets by identities that no longer exist. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| The platform reads cases from the Machine block only, and the human-block fidelity check refuses a declaration made in prose. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| Proving each platform transform in every domain that carries it was rejected: the vector would be stated up to three times, a transform carried by no domain would be proven nowhere, and each domain would prove code it does not supply. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| Proving the platform's transforms in a workload built to carry them was rejected: it needs acts that exist only to carry transforms, vectors imported into domains, and a runner proving what a build carries rather than supplies. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| Lifting the vectors without running them would leave eleven declarations judged by nothing. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| An inherited case is corrected where the current behaviour is the intended one, dropped where it tested something no longer declared, and never kept as written only because it was inherited. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| A domain that carries a platform transform still reports it as carried once the platform proves it; the platform's proof is in the platform's result, and the snapshot carries both. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| The platform has a reference build and two placement builds, a federated and a multi-worker one, and all three seal the same transforms. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| All three of the platform's builds prove its transforms: each composition is sealed on its own and states what it proved, and none relies on another build's evidence. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| Any failed case refuses the build that ran it, whoever supplies the transform it tests. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| Today the runner judges only a build's own transforms, so a failed case for a carried transform would run and be ignored; no domain declares one, and this change adds none. | HIGH | CR seed §4 Known Facts — Business Truths #29 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| No platform transform has a vector in the composition. | Decides whether all twelve are unproven today. | Confirm what vectors the composition carries, and for which transforms. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The eleven platform transforms keep the codes the reference implementation's vectors name. | Decides whether each inherited vector has a target. | Establish the current identity of each platform transform an inherited vector names. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The platform's build does not discover vectors and declares no place for runnable cases. | Decides what the platform's build declaration must newly state. | Establish which kinds the platform's build discovers and what places it declares. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The platform's build step does not run conformance. | Decides whether the build step changes. | Establish what the platform's build step runs after its compile. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The runner takes a transform as a build's own only when its namespace is the build's scope. | Decides whether the platform's transforms, which are not named for the platform, would be judged at all. | Establish how the runner tells a build's own transforms from carried ones. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| The platform's conformance result would be carried into the snapshot as a domain's is. | Decides whether the assembler changes. | Establish how the assembler finds and carries a build's conformance result. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

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
| The platform governs every vector. | Business policy | CR seed §7 Constraints #1 |
| A vector belongs to whoever supplies the transform it tests. | Business policy | CR seed §7 Constraints #2 |
| The platform's vectors are declared with the platform and run in the platform's own build. | Business policy | CR seed §7 Constraints #3 |
| The platform's build never proves a domain's transforms. | Business policy | CR seed §7 Constraints #4 |
| Every build of the platform proves the platform's transforms. | Business policy | CR seed §7 Constraints #5 |
| A build with a failed case is never admitted, whoever supplies the transform the case tests. | Business policy | CR seed §7 Constraints #6 |
| An inherited case is re-judged against the current declaration and implementation, never trusted. | Business policy | CR seed §7 Constraints #7 |
| An inherited case that no longer holds is corrected or dropped, and the reason is recorded. | Business policy | CR seed §7 Constraints #8 |
| No vector is invented for a platform transform the reference implementation never tested. | Business policy | CR seed §7 Constraints #9 |
| Lifting the vectors without running them is not an acceptable partial change. | Business policy | CR seed §7 Constraints #10 |
| A domain that carries a platform transform reports it as carried, unchanged. | Business policy | CR seed §7 Constraints #11 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every platform vector tests a platform transform the composition declares. | CR seed §8 Business Invariants #1 |
| Every platform vector runs on every build of the platform. | CR seed §8 Business Invariants #2 |
| No build with a failed case is admitted. | CR seed §8 Business Invariants #3 |
| A transform's vectors run in the build of its supplier and nowhere else. | CR seed §8 Business Invariants #4 |
| No inherited case is kept as written only because it was inherited. | CR seed §8 Business Invariants #5 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Platform transform | Unproven | No vector tests it; it is named, never counted as passing. | CR seed §9 Lifecycle States #1 |
| Platform transform | Proven | Every vector that tests it ran against it as sealed and passed. | CR seed §9 Lifecycle States #2 |
| Platform transform | Refused | A vector that tests it failed; the platform is not admitted. | CR seed §9 Lifecycle States #3 |
| Inherited case | Kept | It holds against the current declaration and implementation as written. | CR seed §9 Lifecycle States #4 |
| Inherited case | Corrected | It tested current, intended behaviour and was restated to match it, with the reason recorded. | CR seed §9 Lifecycle States #5 |
| Inherited case | Dropped | It tested something no longer declared, and was removed with the reason recorded. | CR seed §9 Lifecycle States #6 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| The platform's transforms were proven | When the platform's build runs its vectors and all pass | What each platform transform does is evidence in the composition, proven by the build that supplies it. | CR seed §10 Business Events #1 |
| The platform was refused for a failed vector | When a platform vector fails in the platform's build | A platform transform that does not do what it says never enters a composition. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a vector is and what counts as proven | The platform | CR seed §11 Authority Boundaries #1 |
| A platform transform's vectors | The platform | CR seed §11 Authority Boundaries #2 |
| A domain transform's vectors | The domain that supplies it | CR seed §11 Authority Boundaries #3 |
| Running the platform's vectors | The platform's build | CR seed §11 Authority Boundaries #4 |
| What a domain reports about the transforms it carries | That domain's build | CR seed §11 Authority Boundaries #5 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Vectors for any domain's own transforms | Three of ai_governance's transforms have inherited vectors that disagree with the current implementations, where the reference implementation answered "no" and the current one refuses; that is ai_governance's question, in its own change. | CR seed §12 Out of Scope #1 |
| Vectors for the platform transform the reference implementation never tested | None is invented here. | CR seed §12 Out of Scope #2 |
| How much proof is enough | The inherited cases are the floor they were. | CR seed §12 Out of Scope #3 |
| Proving a domain's transforms in the platform's build | The platform does not own a domain's implementations. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| conformance | EXTENDED | CR seed §13 Governance Scope #1 |
| structure | MODIFIED | CR seed §13 Governance Scope #2 |
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
| Each of the eleven platform transforms has one vector, declared with the platform, with its cases in the Machine block and its target named by current identity. | CR seed §15 Acceptance Criteria #1 |
| Every inherited case is kept, corrected or dropped, and every correction and drop records its reason. | CR seed §15 Acceptance Criteria #2 |
| Each of the platform's three builds runs every platform vector after its compile succeeds, and reports each of the eleven proven and the twelfth unproven by name. | CR seed §15 Acceptance Criteria #3 |
| A platform vector whose result does not match refuses the platform's build. | CR seed §15 Acceptance Criteria #4 |
| The platform's build proves no domain's transform. | CR seed §15 Acceptance Criteria #5 |
| Each domain that carries a platform transform still reports it as carried. | CR seed §15 Acceptance Criteria #6 |
| A build whose case for a carried transform fails is refused. | CR seed §15 Acceptance Criteria #7 |
| The platform's conformance result is carried into the snapshot. | CR seed §15 Acceptance Criteria #8 |

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
| Platform transform | Unproven | Proven | Its vector is declared and passes in the platform's build. | None. | CR seed §17 Lifecycle Transitions #1 |
| Platform transform | Proven | Refused | A later platform build runs a vector that now fails. | The platform is not admitted. | CR seed §17 Lifecycle Transitions #2 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Build the platform | A platform vector fails against its transform as sealed. | A platform transform that does not do what it says never enters a composition. | CR seed §18 Operation Refusals #1 |
| Build any domain or the platform | A case fails for a transform the build carries rather than supplies. | A failed case never admits its build. | CR seed §18 Operation Refusals #2 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Vectors for ai_governance's own transforms | The ai_governance domain | Its own change | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
