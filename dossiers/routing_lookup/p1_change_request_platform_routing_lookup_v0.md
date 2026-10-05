# Stage 1 — Change Request: Clarification & Fact Capture: platform / routing is a lookup
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** routing_lookup
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
| execution_topology | MODIFY | Its two rules disagree about what routing may say, and the one the compiler follows admits an answer nothing performs. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Step | One capability a contract runs, with the outcomes it can produce. | CR seed §2 Business Vocabulary #1 |
| Routing | What a step says happens next for each outcome it can produce. | CR seed §2 Business Vocabulary #2 |
| Going on | The routing answer that runs the contract's next step. | CR seed §2 Business Vocabulary #3 |
| Ending | The routing answer that ends the contract with the step's outcome. | CR seed §2 Business Vocabulary #4 |
| Evaluation target | A named condition over a step's result, ending the contract with one outcome when it holds and another when it does not. | CR seed §2 Business Vocabulary #5 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The rule that a contract's outcomes are all reachable agrees that routing has two answers, going on and ending. | CR seed §3 Requested Outcomes #1 |
| Building a composition refuses routing to anything but going on or ending. | CR seed §3 Requested Outcomes #2 |
| Building a composition refuses a contract that declares an evaluation target. | CR seed §3 Requested Outcomes #3 |
| Running a contract refuses a routing answer it does not know, rather than go on. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| Routing is a lookup from each outcome to going on or ending. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A decision is made by a capability, which answers with an outcome. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A continuation the contract does not declare is refused, never assumed. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A change of meaning is a new identity, so the invariant is replaced by a new version. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Execution is not given a way to run conditions. | HIGH | CR seed §4 Known Facts — Business Truths #5 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The rule governing how contracts are built allows only going on and ending. | This change aligns the invariant to it rather than the reverse. | Establish what the governing rule says routing may be. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The rule that a contract's outcomes are all reachable admits evaluation targets, and the compiler follows it. | It is what this change replaces. | Establish what the invariant and its check accept. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Execution reads an unknown routing answer as going on. | It is why two contracts succeed where they should fail. | Establish what execution does with each routing answer. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Exactly two contracts route to an evaluation target: the licence cap and the Collatz gate. | Refusing evaluation targets must refuse no other contract. | Establish every routing answer in the composition. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

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
| The refusal takes effect once no composition the platform holds routes to an evaluation target; the two contracts are replaced by their own changes before this one is built. | Business author | CR seed §7 Constraints #1 |
| Every other composition builds and runs as it does today. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every routing answer is going on or ending. | CR seed §8 Business Invariants #1 |
| Every outcome a contract declares is reached by a step's outcome routed to ending. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Rule that a contract's outcomes are all reachable | In force | Checked whenever a composition is built. | CR seed §9 Lifecycle States #1 |
| Rule that a contract's outcomes are all reachable | Stood down | Replaced by the version this change adds, kept in the record and out of reach. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| NONE IDENTIFIED |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What routing may say | Execution topology | CR seed §11 Authority Boundaries #1 |
| Which outcomes a contract can reach | Execution topology | CR seed §11 Authority Boundaries #2 |
| What decision a capability makes | The subdomain that declares the capability | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Replacing the licence cap contract | Its own change, in its domain. | CR seed §12 Out of Scope #1 |
| Replacing the Collatz gate contract | Its own change, in the conformance workload. | CR seed §12 Out of Scope #2 |
| Running conditions at execution | The governing rule forbids an expression in routing. | CR seed §12 Out of Scope #3 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| execution_topology | MODIFIED | CR seed §13 Governance Scope #1 |
| capability_contracts | ADJACENT | CR seed §13 Governance Scope #2 |

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
| The new invariant states that every routing answer is going on or ending, and admits no evaluation target. | CR seed §15 Acceptance Criteria #1 |
| The old invariant is stood down, kept in the record and out of reach. | CR seed §15 Acceptance Criteria #2 |
| A contract routing to anything else is refused when the composition is built, and the refusal names the step and the answer. | CR seed §15 Acceptance Criteria #3 |
| A contract declaring an evaluation target is refused when the composition is built. | CR seed §15 Acceptance Criteria #4 |
| A routing answer execution does not know refuses the run, and the trace records where. | CR seed §15 Acceptance Criteria #5 |
| Every composition the platform holds builds and runs as it does today, once the two contracts are replaced. | CR seed §15 Acceptance Criteria #6 |

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
| Rule that a contract's outcomes are all reachable | In force | Stood down | This change adds its successor | Whatever names it is re-pointed | CR seed §17 Lifecycle Transitions #1 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Building a composition | A step routes to anything but going on or ending | Routing is a lookup; a decision is a capability's. | CR seed §18 Operation Refusals #1 |
| Building a composition | A contract declares an evaluation target | Nothing performs it. | CR seed §18 Operation Refusals #2 |
| Running a contract | A step's routing answer is neither going on nor ending | A continuation not declared is refused, never assumed. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| The licence cap decision | ai_governance | Its contract is replaced | CR seed §19 Authority Deferrals #1 |
| The Collatz termination decision | The conformance workload | Its contract is replaced | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
