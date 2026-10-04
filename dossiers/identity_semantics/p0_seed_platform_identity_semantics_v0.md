# Change Seed — platform / identity semantics

**Stage:** 0 — Change Seed
**CR:** identity_semantics
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The artifact subdomain governs what an artifact's identity stands for: that an identity names one
meaning, that a superseded artifact stays in the record and out of reach, and that nothing reaches
an artifact that has been stood down. Its authority is to decide what makes an identity sound. It
decides nothing about what any particular artifact means.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| artifact | EXTEND_SUBDOMAIN | Nothing declares which parts of a declaration carry meaning, so nothing can tell a change of meaning from a change of wording. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Declaration | What an artifact states about itself, in the form the platform reads. |
| Meaning | What a declaration commits the artifact to. |
| Explanation | A part of a declaration that tells a reader something and commits the artifact to nothing. |
| Unordered list | A list whose members matter and whose order does not. |
| Identity | The name an artifact is admitted and referred to under. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| One place declares which parts of a declaration are explanation. |
| The same place declares which lists carry no meaning in their order. |
| Everything else in a declaration is taken to carry meaning. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A change of meaning is a new identity; a change of how it is written is not. | HIGH |
| What carries no meaning is declared, never inferred. | HIGH |
| Adding to the declaration is itself a reviewed change. | HIGH |
| Anything the declaration does not list carries meaning. | HIGH |
| Deciding which past changes altered meaning is the next change. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Nothing in the platform declares which parts of a declaration are explanation. | Without it, a comparison of two declarations cannot ignore wording. | Establish whether any artifact declares it. |
| Some lists are written in an order that carries no meaning. | Without it, a list written in another order reads as a change of meaning. | Establish which lists are read as sets. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Nothing that is built or run changes because of this declaration. | Business author |
| A part is declared explanation only where it is explanation wherever it appears. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every part of a declaration either carries meaning or is declared not to. |
| One place declares what carries no meaning. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Declaration | Admitted | Unchanged by this change. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | | |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Which parts of a declaration carry no meaning | Artifact |
| What any part of a declaration means | The subdomain that declares the artifact |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Comparing two declarations | The next change, which reads this declaration. |
| Deciding which past changes altered meaning | The next change. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| artifact | EXTENDED |
| vocabulary | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| The composition carries one declaration naming the parts of a declaration that are explanation. |
| The same declaration names the lists whose order carries no meaning. |
| Every part it names is explanation, or an unordered list, wherever it appears in the composition. |
| Every composition the platform holds builds and runs as it does today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Declaration | The artifact's identity | They commit the artifact to the same things, whatever their wording or the order of an unordered list |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| NONE IDENTIFIED | | | | |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| NONE IDENTIFIED | | |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| How two declarations are compared | The next change | It is designed |
