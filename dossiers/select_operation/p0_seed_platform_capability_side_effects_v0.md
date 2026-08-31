# Change Seed — platform / capability_side_effects

**Stage:** 0 — Change Seed
**CR:** select_operation
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

Capability side effects are the platform's offer of what the business cannot do for itself: holding a
record, appending to a trail, reading a clock. A domain composes what is offered and never decides
what is on offer, because every domain reaches the same capability and a change to one is a change
for all of them. The subdomain's authority is to state that offer and to keep it closed: a capability
nobody admitted cannot be reached, and an operation nobody declared does not exist.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| capability_side_effects | MODIFY | A capability gained an operation and no dossier records it. The record is what is missing; the operation is declared, compiled and in use. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Capability | The platform's offer of something the business cannot do for itself. |
| Operation | One thing a capability offers to do, named and declared. |
| Offer | The whole set of operations a capability declares. |
| Record | A durable statement the business keeps and addresses by a key. |
| Selection | Answering a question by looking at records rather than at the keys they are filed under. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The operation that reads every record is recorded as a platform change, with the reason it was added. |
| A reader learns what the capability offers from the capability, not from the first domain that needed an operation. |
| The record states that the change crossed an authority boundary, and that the boundary is now stated. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A domain composes what a capability offers and never decides what is on offer. | HIGH |
| A change to one capability is a change for every domain that reaches it. | HIGH |
| Answering a question about what is held requires seeing the records, not the keys they are filed under. | HIGH |
| The operation is correct, declared as a read, and in use; nothing about it is being undone. | HIGH |
| The reason a capability offers an operation belongs with the capability, not with the first caller that needed it. | HIGH |
| A change that crossed a boundary before the boundary was stated is not a breach of a rule in force. | HIGH |
| Recording such a change is what makes the first instance visible rather than absorbed. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The capability offers an operation that reads every record it holds. | The subject of this change. | Confirm the operation is declared, what it answers with, and that it is declared a read. |
| The operation is reached by acts of a business domain and is running. | Establishes there is nothing to deliver, only to record. | Confirm which acts reach it and that they run. |
| The operation was carried into the platform by a business change request that inventoried the capability as one it extends. | The whole of why this dossier exists. | Confirm where the extension was declared and by which change. |
| Nothing in the composition asked whether a business change request may amend a platform capability. | Says the boundary was unenforced rather than broken. | Establish what governed the amendment at the time, and what governs it now. |
| The reason the capability offers this operation is written down in another domain's change request. | Says what is actually missing: the record, not the operation. | Confirm where the justification lives today. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| No other operation of this capability arrived the same way. | Only one operation was added after the capability was first declared. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The operation stays exactly as it is; this change records it and alters nothing. | Business author |
| The record is made where the capability lives, not where the caller lives. | Business author |
| The change is not re-delivered through the pipeline, because there is nothing left to deliver. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A capability's offer is decided by the platform, never by a domain that reaches it. |
| Every operation a capability offers has a recorded reason for being offered. |
| A change to a capability is recorded where the capability is declared. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Operation | Offered | The capability declares it and any domain may compose it. |
| Operation | Recorded | A dossier states why the capability offers it. |
| Operation | Offered but unrecorded | It is reachable and its reason lives somewhere else, which is the state this change ends. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A capability's offer changed | When an operation is added to or withdrawn from a capability | Every domain that reaches the capability is affected, whether or not it composes the operation. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a capability offers | The platform |
| Which operations an act composes | The domain performing the act |
| The reason an operation is offered | The change that added it |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Whether the operation should exist | It exists, it is correct, and it is in use. |
| Whether the caller was wrong to need it | The need was real and the operation answers it. |
| What other capabilities should offer | Each is its own question. |
| Re-delivering the operation through the pipeline | Nothing is left to deliver; the record is what was missing. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| capability_side_effects | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| The reason the capability offers an operation that reads every record can be found from the capability itself. |
| The record states which change added the operation and that it was carried by a business change request. |
| Nothing about the operation's behaviour differs before and after this record is made. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Operation | The capability that offers it and the name it is offered under | One capability offers one operation of that name. |
| Offer | The capability whose offer it is | They are the same capability. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Operation | Offered but unrecorded | Recorded | A dossier stating why the capability offers it. | Nothing else follows. The operation is unchanged and every act that composes it is unaffected. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Amending a capability | The change amending it belongs to a domain that reaches the capability rather than to the platform that offers it | Every domain reaches the same capability, so a domain deciding its offer decides for all of them. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| What other capabilities offer | A later change | One of them needs to change. |
| Whether an unused operation should be withdrawn | A later change | An operation is found that nothing composes. |
