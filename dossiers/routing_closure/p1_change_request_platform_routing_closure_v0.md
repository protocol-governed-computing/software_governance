# Stage 1 — Change Request: Clarification & Fact Capture: platform / routing closure
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** routing_closure
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
| execution_topology | MODIFY | A step's answers are checked against what its author listed, not against what its capability declares, so a step can leave an outcome unanswered. | CR seed §1 CR Type #1 |
| workflow | MODIFY | Nothing refuses a workflow place that leaves an outcome of its contract without a route, until a request reaches it. | CR seed §1 CR Type #2 |
| trace | MODIFY | The record of a step names what it produced, and not the outcome it ended with or what happened next. | CR seed §1 CR Type #3 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Step | One part of a contract, which dispatches one capability. | CR seed §2 Business Vocabulary #1 |
| Outcome | One answer a capability can give, such as success, not found or refused. | CR seed §2 Business Vocabulary #2 |
| Continuation | What a contract declares happens next for one outcome of one step: carry on, or end. | CR seed §2 Business Vocabulary #3 |
| Route | What a workflow declares happens next for one outcome of a contract: another place, or an ending. | CR seed §2 Business Vocabulary #4 |
| Reachable | A workflow place some request can arrive at. | CR seed §2 Business Vocabulary #5 |
| Step record | The platform's account of one step that ran. | CR seed §2 Business Vocabulary #6 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A composition in which a step answers fewer outcomes than its capability declares is refused when it is built. | CR seed §3 Requested Outcomes #1 |
| A composition in which a reachable workflow place leaves an outcome of its contract without a route is refused when it is built. | CR seed §3 Requested Outcomes #2 |
| A step outcome for which nothing says what happens next refuses the request, and nothing after it runs. | CR seed §3 Requested Outcomes #3 |
| Every step record states the outcome the step ended with and what happened next. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A missing answer is never a default. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A refusal at build time comes first, and a refusal at run time stays as the safeguard. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A superseded workflow cannot be run and stays in the record. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A step answers every outcome its capability declares, whether or not it occurs in practice. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| An admission check's record names its outcome, and the workflow's route decides what happens next. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The three domains with gaps closed them in their own changes. | HIGH | CR seed §4 Known Facts — Business Truths #6 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The step check compares a step's answers with what its author listed, not with what its capability declares. | A narrowed step passes the build. | Establish what the step check compares against. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| No check closes a workflow place against what its contract can end with. | An unrouted outcome is sealed and refused only when a request reaches it. | Establish which checks govern a workflow's routes. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Execution carries a contract on past a step outcome nothing answers. | A failed lookup let a person be accepted. | Establish what execution does with an unanswered step outcome. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The step record names what a step produced and not its outcome. | The decision that went wrong left no record. | Establish what the step record carries. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| NONE IDENTIFIED |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Every composition the domains now hold builds and runs as it does today. | Business author | CR seed §7 Constraints #1 |
| The run-time refusal for an unrouted workflow outcome stays. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No step answers fewer outcomes than its capability declares. | CR seed §8 Business Invariants #1 |
| No reachable workflow place leaves an outcome of its contract without a route. | CR seed §8 Business Invariants #2 |
| Execution never carries on past an outcome nothing answers. | CR seed §8 Business Invariants #3 |
| Every step that runs is recorded with its outcome and what happened next. | CR seed §8 Business Invariants #4 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Composition | Built | Admitted by every check. Unchanged by this change, which adds checks. | CR seed §9 Lifecycle States #1 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A request was refused at an unanswered step outcome | When a step ends with an outcome nothing answers | The refusal and its reason are in the record. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Which outcomes a capability can answer | The capability's declaration | CR seed §11 Authority Boundaries #1 |
| Which outcomes a step answers | The contract that holds it | CR seed §11 Authority Boundaries #2 |
| Whether a step or a workflow place answers enough | The platform | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Closing the gaps in the domains | Each domain closed its own in its own change. | CR seed §12 Out of Scope #1 |
| What any contract or workflow does with an outcome | Each domain's business. | CR seed §12 Out of Scope #2 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| execution_topology | MODIFIED | CR seed §13 Governance Scope #1 |
| workflow | MODIFIED | CR seed §13 Governance Scope #2 |
| trace | MODIFIED | CR seed §13 Governance Scope #3 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| A step that answers fewer outcomes than its capability declares is refused when the composition is built. | CR seed §15 Acceptance Criteria #1 |
| A reachable workflow place that leaves an outcome of its contract without a route is refused when the composition is built. | CR seed §15 Acceptance Criteria #2 |
| A superseded workflow, and a place no request reaches, are not refused for an unanswered outcome. | CR seed §15 Acceptance Criteria #3 |
| A step outcome nothing answers refuses the request, and nothing after it runs. | CR seed §15 Acceptance Criteria #4 |
| Every step record states the outcome and what happened next. | CR seed §15 Acceptance Criteria #5 |
| Every composition the domains now hold builds and runs as it does today. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| NONE IDENTIFIED |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| NONE IDENTIFIED |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Building a composition | A step answers fewer outcomes than its capability declares | A missing answer is never a default. | CR seed §18 Operation Refusals #1 |
| Building a composition | A reachable workflow place leaves an outcome of its contract without a route | A refusal at build time comes first. | CR seed §18 Operation Refusals #2 |
| Running a request | A step ends with an outcome nothing answers | Execution never carries on past an outcome nothing answers. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| NONE IDENTIFIED |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
