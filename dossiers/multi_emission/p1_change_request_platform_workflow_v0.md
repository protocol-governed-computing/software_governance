# Stage 1 — Change Request: Clarification & Fact Capture: platform / workflow
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** multi_emission
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
| workflow | MODIFY | An act announces one moment and some acts complete several, so a declared moment goes unannounced with nobody having agreed it should. The limit is carried by implementation rather than stated by any rule, so the model is declared for the first time rather than relaxed. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Act | Something the business does as one unit, which completes or is refused. | CR seed §2 Business Vocabulary #1 |
| Moment | Something the business declared matters, recognised when it occurs. | CR seed §2 Business Vocabulary #2 |
| Announcement | An act stating that a moment occurred. | CR seed §2 Business Vocabulary #3 |
| Terminal node | Where an act ends, and what carries its announcement. | CR seed §2 Business Vocabulary #4 |
| Order | The sequence in which several announcements are made. | CR seed §2 Business Vocabulary #5 |
| Evidence record | The observable trace that a moment was announced. | CR seed §2 Business Vocabulary #6 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| One terminal node can announce more than one declared moment. | CR seed §3 Requested Outcomes #1 |
| Several moments are announced in a stated order, the same order every time. | CR seed §3 Requested Outcomes #2 |
| One distinct evidence record is produced per moment announced, so a moment announced is a moment observable. | CR seed §3 Requested Outcomes #3 |
| An announcement that cannot be made is reported rather than passed over. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| One act may complete more than one declared moment, and this is ordinary rather than exotic. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A declared moment that is never announced is a defect, because the business declared that it matters. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| An act is not split to fit a limitation of the announcement mechanism; that changes the business to suit the platform. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The order several moments are announced in is the order the design states, and that order carries meaning. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| An act whose announcement cannot be made is not refused; its work is already done and a record is immutable once written. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| An announcement that cannot be made is reported, and the moments already announced stand, because they are true. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Each moment announced produces its own evidence record. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A terminal node names each moment at most once; announcing one moment twice from one act says it occurred twice. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| Several instances of one kind of moment, about different subjects, is a different shape and not this change. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A behaviour the platform performs and no document governs is ungoverned rather than leniently governed. | HIGH | CR seed §4 Known Facts — Business Truths #10 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| A terminal node names a single moment, and the running system resolves a single moment for a given act and outcome. | The whole of this change. | Establish how many moments a terminal node carries today, and where that number is fixed. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| An act exists that completes several declared moments and can announce one. | Establishes the requirement occurred rather than being foreseen. | Confirm an instance, confirm how many moments it completes, and confirm how many it can announce. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Nothing governing states what a terminal node announces. | Decides whether this relaxes a rule or states a model for the first time. | Establish what governs announcement today, and what it says. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| A subdomain exists whose declared moments are announced by nothing at all. | Says the cost is already being paid, and paid as silence rather than as a wrong answer. | Confirm which declared moments no act announces, and whether that was a choice. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Nothing counts the moments an act announces — no rule, no published surface, no boundary declaration. | Says how much of the composition a change to the model would disturb. | Establish every consumer of an announced moment and what each relies on. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| A reader exists that takes the first announced moment it finds. | Says where several would arrive without anyone noticing. | Confirm the reader, and what it would do if an act announced more than one. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| The moments one act completes are few and known when the act is designed, rather than one per member of a collection. | The confirmed instance completes three, each a distinct kind. | CR seed §6 Assumptions #1 |
| An announcement failure is rare and caused by the same conditions that make any record fail to write. | Announcement writes evidence the same way every other record is written. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| The stated order is normative; announcing in a different order is announcing something else. | Business author | CR seed §7 Constraints #1 |
| One evidence record per moment announced, whether the act announces one moment or several. | Business author | CR seed §7 Constraints #2 |
| A terminal node names each moment at most once. | Business author | CR seed §7 Constraints #3 |
| No declared moment an act completes is passed over in silence. | Business author | CR seed §7 Constraints #4 |
| An act is never split, and no moment is dropped, to fit the announcement mechanism. | Business author | CR seed §7 Constraints #5 |
| A moment per member of a collection is not admitted by this change. | Business author | CR seed §7 Constraints #6 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every declared moment an act completes is announced by that act. | CR seed §8 Business Invariants #1 |
| Several moments are announced in the order the design states. | CR seed §8 Business Invariants #2 |
| Each moment announced has its own evidence record. | CR seed §8 Business Invariants #3 |
| An act announces each moment at most once. | CR seed §8 Business Invariants #4 |
| An announcement that cannot be made is reported, and never passed over. | CR seed §8 Business Invariants #5 |
| A moment announced is a moment that occurred. | CR seed §8 Business Invariants #6 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Moment | Declared | The business says it matters and has named it. | CR seed §9 Lifecycle States #1 |
| Moment | Announced | An act has stated that it occurred, and there is a record of the statement. | CR seed §9 Lifecycle States #2 |
| Moment | Declared and unannounceable | The act that completes it cannot say so, which is the state this change ends. | CR seed §9 Lifecycle States #3 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| An act announced its moments | When an act reaches the end and states what it completed | The business's account of the act is complete and observable. | CR seed §10 Business Events #1 |
| An announcement could not be made | When a moment an act completed cannot be stated | The account is incomplete, and the incompleteness is visible rather than silent. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Which moments an act announces | The domain that owns the act | CR seed §11 Authority Boundaries #1 |
| Whether an act may announce several | The platform | CR seed §11 Authority Boundaries #2 |
| The order several moments are announced in | The design that states them | CR seed §11 Authority Boundaries #3 |
| What counts as evidence that a moment was announced | The platform | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Which moments any act announces | Each domain's business, stated in its own change. | CR seed §12 Out of Scope #1 |
| Whether an act should complete several moments | Some do; this change follows that fact rather than judging it. | CR seed §12 Out of Scope #2 |
| A moment announced per member of a collection | A different shape, and not what the confirmed requirement needs. | CR seed §12 Out of Scope #3 |
| Anything about the lifecycle that governs change | A platform capability, distinct from the lifecycle dossiers. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| workflow | MODIFIED | CR seed §13 Governance Scope #1 |
| event | ADJACENT | CR seed §13 Governance Scope #2 |
| design | ADJACENT | CR seed §13 Governance Scope #3 |

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
| One successful traversal of an act that completes several declared moments announces every one of them. | CR seed §15 Acceptance Criteria #1 |
| The moments are announced in the order the design stated, and the same order on every traversal. | CR seed §15 Acceptance Criteria #2 |
| Each moment announced leaves its own evidence record, with no duplicate and none omitted. | CR seed §15 Acceptance Criteria #3 |
| An act that names one moment announces exactly what it announces today. | CR seed §15 Acceptance Criteria #4 |
| An act whose announcement cannot be made reports the failure, and the moments already announced remain announced. | CR seed §15 Acceptance Criteria #5 |
| A design naming the same moment twice at one terminal node is refused when the composition is built. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Moment | The declaration that names it | Two announcements name the same declaration, whatever else differs. | CR seed §16 Identity and Sameness #1 |
| Announcement | The act that made it and the moment it names | One act states one moment once. | CR seed §16 Identity and Sameness #2 |
| Evidence record | The announcement it records | They record the same announcement. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Moment | Declared | Announced | The act that completes it reaching its end. | One evidence record is written. Nothing else follows, and no other moment is announced by the same statement. | CR seed §17 Lifecycle Transitions #1 |
| Moment | Declared and unannounceable | Announced | The act gaining the ability to state every moment it completes. | Nothing else follows. The act does what it already did and now says so. | CR seed §17 Lifecycle Transitions #2 |
| Moment | Declared | Declared and unannounceable | An announcement that cannot be made. | The act reports the failure. Moments already announced stand, because they are true. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Building a composition | An act names the same moment twice at one terminal node | Announcing one moment twice from one act says it occurred twice, and a reader counting occurrences would conclude something happened that did not. | CR seed §18 Operation Refusals #1 |
| Announcing | A moment an act completed cannot be stated | The failure is reported rather than passed over, because a declared moment silently unannounced is the defect this change exists to remove. | CR seed §18 Operation Refusals #2 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| A moment announced per member of a collection | A later change | An act needs to announce one moment per member rather than a known few. | CR seed §19 Authority Deferrals #1 |
| Which moments each act announces | Each domain | That domain raises the change that needs them. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
