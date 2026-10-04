# Change Seed — platform / routing closure

**Stage:** 0 — Change Seed
**CR:** routing_closure
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
| execution_topology | MODIFY | A step's answers are checked against what its author listed, not against what its capability declares, so a step can leave an outcome unanswered. |
| workflow | MODIFY | Nothing refuses a workflow place that leaves an outcome of its contract without a route, until a request reaches it. |
| trace | MODIFY | The record of a step names what it produced, and not the outcome it ended with or what happened next. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Step | One part of a contract, which dispatches one capability. |
| Outcome | One answer a capability can give, such as success, not found or refused. |
| Continuation | What a contract declares happens next for one outcome of one step: carry on, or end. |
| Route | What a workflow declares happens next for one outcome of a contract: another place, or an ending. |
| Reachable | A workflow place some request can arrive at. |
| Step record | The platform's account of one step that ran. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A composition in which a step answers fewer outcomes than its capability declares is refused when it is built. |
| A composition in which a reachable workflow place leaves an outcome of its contract without a route is refused when it is built. |
| A step outcome for which nothing says what happens next refuses the request, and nothing after it runs. |
| Every step record states the outcome the step ended with and what happened next. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A missing answer is never a default. | HIGH |
| A refusal at build time comes first, and a refusal at run time stays as the safeguard. | HIGH |
| A superseded workflow cannot be run and stays in the record. | HIGH |
| A step answers every outcome its capability declares, whether or not it occurs in practice. | HIGH |
| An admission check's record names its outcome, and the workflow's route decides what happens next. | HIGH |
| The three domains with gaps closed them in their own changes. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The step check compares a step's answers with what its author listed, not with what its capability declares. | A narrowed step passes the build. | Establish what the step check compares against. |
| No check closes a workflow place against what its contract can end with. | An unrouted outcome is sealed and refused only when a request reaches it. | Establish which checks govern a workflow's routes. |
| Execution carries a contract on past a step outcome nothing answers. | A failed lookup let a person be accepted. | Establish what execution does with an unanswered step outcome. |
| The step record names what a step produced and not its outcome. | The decision that went wrong left no record. | Establish what the step record carries. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every composition the domains now hold builds and runs as it does today. | Business author |
| The run-time refusal for an unrouted workflow outcome stays. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No step answers fewer outcomes than its capability declares. |
| No reachable workflow place leaves an outcome of its contract without a route. |
| Execution never carries on past an outcome nothing answers. |
| Every step that runs is recorded with its outcome and what happened next. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Composition | Built | Admitted by every check. Unchanged by this change, which adds checks. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A request was refused at an unanswered step outcome | When a step ends with an outcome nothing answers | The refusal and its reason are in the record. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Which outcomes a capability can answer | The capability's declaration |
| Which outcomes a step answers | The contract that holds it |
| Whether a step or a workflow place answers enough | The platform |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Closing the gaps in the domains | Each domain closed its own in its own change. |
| What any contract or workflow does with an outcome | Each domain's business. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| execution_topology | MODIFIED |
| workflow | MODIFIED |
| trace | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A step that answers fewer outcomes than its capability declares is refused when the composition is built. |
| A reachable workflow place that leaves an outcome of its contract without a route is refused when the composition is built. |
| A superseded workflow, and a place no request reaches, are not refused for an unanswered outcome. |
| A step outcome nothing answers refuses the request, and nothing after it runs. |
| Every step record states the outcome and what happened next. |
| Every composition the domains now hold builds and runs as it does today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| NONE IDENTIFIED | | | | |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a composition | A step answers fewer outcomes than its capability declares | A missing answer is never a default. |
| Building a composition | A reachable workflow place leaves an outcome of its contract without a route | A refusal at build time comes first. |
| Running a request | A step ends with an outcome nothing answers | Execution never carries on past an outcome nothing answers. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE IDENTIFIED | | |
