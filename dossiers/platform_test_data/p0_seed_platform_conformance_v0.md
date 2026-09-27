# Change Seed — platform / conformance

**Stage:** 0 — Change Seed
**CR:** platform_test_data
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the six clarifications its
author answered. Human input only — nothing here was added, decided or
designed by the pipeline.

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
| conformance | MODIFY | The platform supplies twelve transforms and proves none of them. Its build runs no conformance, on a reason that holds for a domain's transforms and not for its own. No domain proves them, correctly, because no domain supplies them. Vectors for eleven exist in the reference implementation and are not used, in a format nothing now reads. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Transform | A unit of computation a governed act performs, whose implementation lives outside the composition. |
| Platform transform | A transform the platform declares and implements once, which any domain may carry. |
| Supplier | Whoever implements a transform; its vectors belong to the supplier. |
| Carried transform | A platform transform a domain uses; the domain's build names it and does not test it. |
| Test vector | Stated inputs and the outputs a transform must produce from them. |
| Case | One set of inputs in a vector, with the outcome and outputs it must produce. |
| Inherited case | A case brought across from the reference implementation. |
| Reference implementation | The implementation this platform was derived from, which carried hand-written vectors. |
| Conformance | Proof that a transform does what its declaration says, carried in the composition. |
| Proven | A transform whose vectors all ran and passed. |
| Unproven | A transform no vector tests; never counted as passing. |
| Domain build | The build in which a domain's own declarations and implementations are compiled. |
| Platform build | The build in which the platform's declarations are compiled. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The reference implementation's vectors for eleven platform transforms are declarations of the platform, with their cases in the Machine block and their targets named by current identity. |
| Every inherited case is re-judged against the current declaration and implementation, and a case that no longer holds is corrected or dropped with the reason recorded. |
| The platform's vectors run in the platform's own build, after its compile succeeds, and the platform is refused if any fails, exactly as a domain's build does. |
| Each of the eleven platform transforms is reported proven by name, and the twelfth unproven. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The platform supplies capability transforms that any domain may carry. | HIGH |
| Each platform transform is declared and implemented in the platform, once, and every domain that uses one runs the same code. | HIGH |
| Every domain build proves its transforms against their test vectors once its compile succeeds. | HIGH |
| A domain build names each transform the domain owns as proven, unproven or refused, and names separately each platform transform the domain carries. | HIGH |
| A domain build's conformance result is part of the snapshot. | HIGH |
| The change that delivered that mechanism deliberately wrote no vectors, leaving each existing transform unproven until a change gave it vectors. | HIGH |
| The platform governs every vector: its constitution states what a vector is, what counts as proven, and that a transform's vectors run in the build of the domain that supplies it. | HIGH |
| Each vector belongs to whoever supplies the transform it tests, because what a vector proves is that supplier's code. | HIGH |
| The platform supplies its own transforms, so their vectors are the platform's. | HIGH |
| The platform supplies twelve transforms and proves none of them. | HIGH |
| Conformance was taken out of the platform's build because the platform does not own a domain's implementations. | HIGH |
| That reason holds for a domain's transforms and says nothing about the platform's own; the decision was applied more broadly than its reason. | HIGH |
| The platform's vectors are run in the platform's own build. | HIGH |
| A domain that carries a platform transform names it as carried and does not test it, correctly, because it does not supply it. | HIGH |
| Three of the platform's transforms are carried by no domain. | HIGH |
| The reference implementation carried hand-written vectors for eleven platform transforms the composition still carries under the same codes. | HIGH |
| A read-only run of the inherited cases against the current implementations found ten of the eleven transforms matching on every case. | HIGH |
| The passthrough transform returns its value bare, and whether the runner yields what its vectors expect is confirmed only when it is built. | HIGH |
| The inherited vectors state their cases in prose, under numbered headings, and name their targets by identities that no longer exist. | HIGH |
| The platform reads cases from the Machine block only, and the human-block fidelity check refuses a declaration made in prose. | HIGH |
| Proving each platform transform in every domain that carries it was rejected: the vector would be stated up to three times, a transform carried by no domain would be proven nowhere, and each domain would prove code it does not supply. | HIGH |
| Proving the platform's transforms in a workload built to carry them was rejected: it needs acts that exist only to carry transforms, vectors imported into domains, and a runner proving what a build carries rather than supplies. | HIGH |
| Lifting the vectors without running them would leave eleven declarations judged by nothing. | HIGH |
| An inherited case is corrected where the current behaviour is the intended one, dropped where it tested something no longer declared, and never kept as written only because it was inherited. | HIGH |
| A domain that carries a platform transform still reports it as carried once the platform proves it; the platform's proof is in the platform's result, and the snapshot carries both. | HIGH |
| The platform has a reference build and two placement builds, a federated and a multi-worker one, and all three seal the same transforms. | HIGH |
| All three of the platform's builds prove its transforms: each composition is sealed on its own and states what it proved, and none relies on another build's evidence. | HIGH |
| Any failed case refuses the build that ran it, whoever supplies the transform it tests. | HIGH |
| Today the runner judges only a build's own transforms, so a failed case for a carried transform would run and be ignored; no domain declares one, and this change adds none. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| No platform transform has a vector in the composition. | Decides whether all twelve are unproven today. | Confirm what vectors the composition carries, and for which transforms. |
| The eleven platform transforms keep the codes the reference implementation's vectors name. | Decides whether each inherited vector has a target. | Establish the current identity of each platform transform an inherited vector names. |
| The platform's build does not discover vectors and declares no place for runnable cases. | Decides what the platform's build declaration must newly state. | Establish which kinds the platform's build discovers and what places it declares. |
| The platform's build step does not run conformance. | Decides whether the build step changes. | Establish what the platform's build step runs after its compile. |
| The runner takes a transform as a build's own only when its namespace is the build's scope. | Decides whether the platform's transforms, which are not named for the platform, would be judged at all. | Establish how the runner tells a build's own transforms from carried ones. |
| The platform's conformance result would be carried into the snapshot as a domain's is. | Decides whether the assembler changes. | Establish how the assembler finds and carries a build's conformance result. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The platform governs every vector. | Business policy |
| A vector belongs to whoever supplies the transform it tests. | Business policy |
| The platform's vectors are declared with the platform and run in the platform's own build. | Business policy |
| The platform's build never proves a domain's transforms. | Business policy |
| Every build of the platform proves the platform's transforms. | Business policy |
| A build with a failed case is never admitted, whoever supplies the transform the case tests. | Business policy |
| An inherited case is re-judged against the current declaration and implementation, never trusted. | Business policy |
| An inherited case that no longer holds is corrected or dropped, and the reason is recorded. | Business policy |
| No vector is invented for a platform transform the reference implementation never tested. | Business policy |
| Lifting the vectors without running them is not an acceptable partial change. | Business policy |
| A domain that carries a platform transform reports it as carried, unchanged. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every platform vector tests a platform transform the composition declares. |
| Every platform vector runs on every build of the platform. |
| No build with a failed case is admitted. |
| A transform's vectors run in the build of its supplier and nowhere else. |
| No inherited case is kept as written only because it was inherited. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Platform transform | Unproven | No vector tests it; it is named, never counted as passing. |
| Platform transform | Proven | Every vector that tests it ran against it as sealed and passed. |
| Platform transform | Refused | A vector that tests it failed; the platform is not admitted. |
| Inherited case | Kept | It holds against the current declaration and implementation as written. |
| Inherited case | Corrected | It tested current, intended behaviour and was restated to match it, with the reason recorded. |
| Inherited case | Dropped | It tested something no longer declared, and was removed with the reason recorded. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| The platform's transforms were proven | When the platform's build runs its vectors and all pass | What each platform transform does is evidence in the composition, proven by the build that supplies it. |
| The platform was refused for a failed vector | When a platform vector fails in the platform's build | A platform transform that does not do what it says never enters a composition. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a vector is and what counts as proven | The platform |
| A platform transform's vectors | The platform |
| A domain transform's vectors | The domain that supplies it |
| Running the platform's vectors | The platform's build |
| What a domain reports about the transforms it carries | That domain's build |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Vectors for any domain's own transforms | Three of ai_governance's transforms have inherited vectors that disagree with the current implementations, where the reference implementation answered "no" and the current one refuses; that is ai_governance's question, in its own change. |
| Vectors for the platform transform the reference implementation never tested | None is invented here. |
| How much proof is enough | The inherited cases are the floor they were. |
| Proving a domain's transforms in the platform's build | The platform does not own a domain's implementations. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| conformance | EXTENDED |
| structure | MODIFIED |
| capability_transforms | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Each of the eleven platform transforms has one vector, declared with the platform, with its cases in the Machine block and its target named by current identity. |
| Every inherited case is kept, corrected or dropped, and every correction and drop records its reason. |
| Each of the platform's three builds runs every platform vector after its compile succeeds, and reports each of the eleven proven and the twelfth unproven by name. |
| A platform vector whose result does not match refuses the platform's build. |
| The platform's build proves no domain's transform. |
| Each domain that carries a platform transform still reports it as carried. |
| A build whose case for a carried transform fails is refused. |
| The platform's conformance result is carried into the snapshot. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Platform transform | Unproven | Proven | Its vector is declared and passes in the platform's build. | None. |
| Platform transform | Proven | Refused | A later platform build runs a vector that now fails. | The platform is not admitted. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Build the platform | A platform vector fails against its transform as sealed. | A platform transform that does not do what it says never enters a composition. |
| Build any domain or the platform | A case fails for a transform the build carries rather than supplies. | A failed case never admits its build. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Vectors for ai_governance's own transforms | The ai_governance domain | Its own change |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
