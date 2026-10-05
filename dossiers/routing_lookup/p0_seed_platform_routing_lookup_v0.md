# Change Seed — platform / routing is a lookup

**Stage:** 0 — Change Seed
**CR:** routing_lookup
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The execution topology subdomain governs how a contract is built from steps: that each step
dispatches one capability, answers the outcomes it can produce, and says for each what happens next.
Its authority is to decide what makes a contract's steps sound. It decides nothing about what any
particular contract does.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| execution_topology | MODIFY | Its two rules disagree about what routing may say, and the one the compiler follows admits an answer nothing performs. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Step | One capability a contract runs, with the outcomes it can produce. |
| Routing | What a step says happens next for each outcome it can produce. |
| Going on | The routing answer that runs the contract's next step. |
| Ending | The routing answer that ends the contract with the step's outcome. |
| Evaluation target | A named condition over a step's result, ending the contract with one outcome when it holds and another when it does not. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The rule that a contract's outcomes are all reachable agrees that routing has two answers, going on and ending. |
| Building a composition refuses routing to anything but going on or ending. |
| Building a composition refuses a contract that declares an evaluation target. |
| Running a contract refuses a routing answer it does not know, rather than go on. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| Routing is a lookup from each outcome to going on or ending. | HIGH |
| A decision is made by a capability, which answers with an outcome. | HIGH |
| A continuation the contract does not declare is refused, never assumed. | HIGH |
| A change of meaning is a new identity, so the invariant is replaced by a new version. | HIGH |
| Execution is not given a way to run conditions. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The rule governing how contracts are built allows only going on and ending. | This change aligns the invariant to it rather than the reverse. | Establish what the governing rule says routing may be. |
| The rule that a contract's outcomes are all reachable admits evaluation targets, and the compiler follows it. | It is what this change replaces. | Establish what the invariant and its check accept. |
| Execution reads an unknown routing answer as going on. | It is why two contracts succeed where they should fail. | Establish what execution does with each routing answer. |
| Exactly two contracts route to an evaluation target: the licence cap and the Collatz gate. | Refusing evaluation targets must refuse no other contract. | Establish every routing answer in the composition. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The refusal takes effect once no composition the platform holds routes to an evaluation target; the two contracts are replaced by their own changes before this one is built. | Business author |
| Every other composition builds and runs as it does today. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every routing answer is going on or ending. |
| Every outcome a contract declares is reached by a step's outcome routed to ending. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Rule that a contract's outcomes are all reachable | In force | Checked whenever a composition is built. |
| Rule that a contract's outcomes are all reachable | Stood down | Replaced by the version this change adds, kept in the record and out of reach. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | | |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What routing may say | Execution topology |
| Which outcomes a contract can reach | Execution topology |
| What decision a capability makes | The subdomain that declares the capability |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Replacing the licence cap contract | Its own change, in its domain. |
| Replacing the Collatz gate contract | Its own change, in the conformance workload. |
| Running conditions at execution | The governing rule forbids an expression in routing. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| execution_topology | MODIFIED |
| capability_contracts | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| The new invariant states that every routing answer is going on or ending, and admits no evaluation target. |
| The old invariant is stood down, kept in the record and out of reach. |
| A contract routing to anything else is refused when the composition is built, and the refusal names the step and the answer. |
| A contract declaring an evaluation target is refused when the composition is built. |
| A routing answer execution does not know refuses the run, and the trace records where. |
| Every composition the platform holds builds and runs as it does today, once the two contracts are replaced. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Rule that a contract's outcomes are all reachable | In force | Stood down | This change adds its successor | Whatever names it is re-pointed |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a composition | A step routes to anything but going on or ending | Routing is a lookup; a decision is a capability's. |
| Building a composition | A contract declares an evaluation target | Nothing performs it. |
| Running a contract | A step's routing answer is neither going on nor ending | A continuation not declared is refused, never assumed. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| The licence cap decision | ai_governance | Its contract is replaced |
| The Collatz termination decision | The conformance workload | Its contract is replaced |
