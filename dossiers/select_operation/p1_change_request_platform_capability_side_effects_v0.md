# Stage 1 — Change Request: Clarification & Fact Capture: platform / capability_side_effects
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** select_operation
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
| capability_side_effects | MODIFY | A capability gained an operation and no dossier records it. The record is what is missing; the operation is declared, compiled and in use. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Capability | The platform's offer of something the business cannot do for itself. | CR seed §2 Business Vocabulary #1 |
| Operation | One thing a capability offers to do, named and declared. | CR seed §2 Business Vocabulary #2 |
| Offer | The whole set of operations a capability declares. | CR seed §2 Business Vocabulary #3 |
| Record | A durable statement the business keeps and addresses by a key. | CR seed §2 Business Vocabulary #4 |
| Selection | Answering a question by looking at records rather than at the keys they are filed under. | CR seed §2 Business Vocabulary #5 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The operation that reads every record is recorded as a platform change, with the reason it was added. | CR seed §3 Requested Outcomes #1 |
| A reader learns what the capability offers from the capability, not from the first domain that needed an operation. | CR seed §3 Requested Outcomes #2 |
| The record states that the change crossed an authority boundary, and that the boundary is now stated. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A domain composes what a capability offers and never decides what is on offer. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A change to one capability is a change for every domain that reaches it. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Answering a question about what is held requires seeing the records, not the keys they are filed under. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The operation is correct, declared as a read, and in use; nothing about it is being undone. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The reason a capability offers an operation belongs with the capability, not with the first caller that needed it. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A change that crossed a boundary before the boundary was stated is not a breach of a rule in force. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Recording such a change is what makes the first instance visible rather than absorbed. | HIGH | CR seed §4 Known Facts — Business Truths #7 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The capability offers an operation that reads every record it holds. | The subject of this change. | Confirm the operation is declared, what it answers with, and that it is declared a read. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The operation is reached by acts of a business domain and is running. | Establishes there is nothing to deliver, only to record. | Confirm which acts reach it and that they run. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The operation was carried into the platform by a business change request that inventoried the capability as one it extends. | The whole of why this dossier exists. | Confirm where the extension was declared and by which change. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Nothing in the composition asked whether a business change request may amend a platform capability. | Says the boundary was unenforced rather than broken. | Establish what governed the amendment at the time, and what governs it now. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The reason the capability offers this operation is written down in another domain's change request. | Says what is actually missing: the record, not the operation. | Confirm where the justification lives today. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| No other operation of this capability arrived the same way. | Only one operation was added after the capability was first declared. | CR seed §6 Assumptions #1 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| The operation stays exactly as it is; this change records it and alters nothing. | Business author | CR seed §7 Constraints #1 |
| The record is made where the capability lives, not where the caller lives. | Business author | CR seed §7 Constraints #2 |
| The change is not re-delivered through the pipeline, because there is nothing left to deliver. | Business author | CR seed §7 Constraints #3 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A capability's offer is decided by the platform, never by a domain that reaches it. | CR seed §8 Business Invariants #1 |
| Every operation a capability offers has a recorded reason for being offered. | CR seed §8 Business Invariants #2 |
| A change to a capability is recorded where the capability is declared. | CR seed §8 Business Invariants #3 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Operation | Offered | The capability declares it and any domain may compose it. | CR seed §9 Lifecycle States #1 |
| Operation | Recorded | A dossier states why the capability offers it. | CR seed §9 Lifecycle States #2 |
| Operation | Offered but unrecorded | It is reachable and its reason lives somewhere else, which is the state this change ends. | CR seed §9 Lifecycle States #3 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A capability's offer changed | When an operation is added to or withdrawn from a capability | Every domain that reaches the capability is affected, whether or not it composes the operation. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a capability offers | The platform | CR seed §11 Authority Boundaries #1 |
| Which operations an act composes | The domain performing the act | CR seed §11 Authority Boundaries #2 |
| The reason an operation is offered | The change that added it | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Whether the operation should exist | It exists, it is correct, and it is in use. | CR seed §12 Out of Scope #1 |
| Whether the caller was wrong to need it | The need was real and the operation answers it. | CR seed §12 Out of Scope #2 |
| What other capabilities should offer | Each is its own question. | CR seed §12 Out of Scope #3 |
| Re-delivering the operation through the pipeline | Nothing is left to deliver; the record is what was missing. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| capability_side_effects | MODIFIED | CR seed §13 Governance Scope #1 |

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
| The reason the capability offers an operation that reads every record can be found from the capability itself. | CR seed §15 Acceptance Criteria #1 |
| The record states which change added the operation and that it was carried by a business change request. | CR seed §15 Acceptance Criteria #2 |
| Nothing about the operation's behaviour differs before and after this record is made. | CR seed §15 Acceptance Criteria #3 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Operation | The capability that offers it and the name it is offered under | One capability offers one operation of that name. | CR seed §16 Identity and Sameness #1 |
| Offer | The capability whose offer it is | They are the same capability. | CR seed §16 Identity and Sameness #2 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Operation | Offered but unrecorded | Recorded | A dossier stating why the capability offers it. | Nothing else follows. The operation is unchanged and every act that composes it is unaffected. | CR seed §17 Lifecycle Transitions #1 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Amending a capability | The change amending it belongs to a domain that reaches the capability rather than to the platform that offers it | Every domain reaches the same capability, so a domain deciding its offer decides for all of them. | CR seed §18 Operation Refusals #1 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| What other capabilities offer | A later change | One of them needs to change. | CR seed §19 Authority Deferrals #1 |
| Whether an unused operation should be withdrawn | A later change | An operation is found that nothing composes. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
