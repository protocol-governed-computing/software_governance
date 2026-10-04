# Stage 1 — Change Request: Clarification & Fact Capture: platform / identity semantics
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** identity_semantics
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
| artifact | EXTEND_SUBDOMAIN | Nothing declares which parts of a declaration carry meaning, so nothing can tell a change of meaning from a change of wording. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Declaration | What an artifact states about itself, in the form the platform reads. | CR seed §2 Business Vocabulary #1 |
| Meaning | What a declaration commits the artifact to. | CR seed §2 Business Vocabulary #2 |
| Explanation | A part of a declaration that tells a reader something and commits the artifact to nothing. | CR seed §2 Business Vocabulary #3 |
| Unordered list | A list whose members matter and whose order does not. | CR seed §2 Business Vocabulary #4 |
| Identity | The name an artifact is admitted and referred to under. | CR seed §2 Business Vocabulary #5 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| One place declares which parts of a declaration are explanation. | CR seed §3 Requested Outcomes #1 |
| The same place declares which lists carry no meaning in their order. | CR seed §3 Requested Outcomes #2 |
| Everything else in a declaration is taken to carry meaning. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A change of meaning is a new identity; a change of how it is written is not. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| What carries no meaning is declared, never inferred. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Adding to the declaration is itself a reviewed change. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Anything the declaration does not list carries meaning. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Deciding which past changes altered meaning is the next change. | HIGH | CR seed §4 Known Facts — Business Truths #5 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Nothing in the platform declares which parts of a declaration are explanation. | Without it, a comparison of two declarations cannot ignore wording. | Establish whether any artifact declares it. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Some lists are written in an order that carries no meaning. | Without it, a list written in another order reads as a change of meaning. | Establish which lists are read as sets. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |

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
| Nothing that is built or run changes because of this declaration. | Business author | CR seed §7 Constraints #1 |
| A part is declared explanation only where it is explanation wherever it appears. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every part of a declaration either carries meaning or is declared not to. | CR seed §8 Business Invariants #1 |
| One place declares what carries no meaning. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Declaration | Admitted | Unchanged by this change. | CR seed §9 Lifecycle States #1 |

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
| Which parts of a declaration carry no meaning | Artifact | CR seed §11 Authority Boundaries #1 |
| What any part of a declaration means | The subdomain that declares the artifact | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Comparing two declarations | The next change, which reads this declaration. | CR seed §12 Out of Scope #1 |
| Deciding which past changes altered meaning | The next change. | CR seed §12 Out of Scope #2 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| artifact | EXTENDED | CR seed §13 Governance Scope #1 |
| vocabulary | ADJACENT | CR seed §13 Governance Scope #2 |

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
| The composition carries one declaration naming the parts of a declaration that are explanation. | CR seed §15 Acceptance Criteria #1 |
| The same declaration names the lists whose order carries no meaning. | CR seed §15 Acceptance Criteria #2 |
| Every part it names is explanation, or an unordered list, wherever it appears in the composition. | CR seed §15 Acceptance Criteria #3 |
| Every composition the platform holds builds and runs as it does today. | CR seed §15 Acceptance Criteria #4 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Declaration | The artifact's identity | They commit the artifact to the same things, whatever their wording or the order of an unordered list | CR seed §16 Identity and Sameness #1 |

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
| NONE IDENTIFIED |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| How two declarations are compared | The next change | It is designed | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
