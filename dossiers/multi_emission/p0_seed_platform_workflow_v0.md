# Change Seed — platform / workflow

**Stage:** 0 — Change Seed
**CR:** multi_emission
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the five clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The workflow subdomain governs the act: what an act is composed of, how it routes between the things
it performs, and where it ends. An act ends at a terminal node, and what that node announces is the
business's account of what the act completed. Its authority is to decide the shape of an act and the
account it gives of itself, and it decides nothing about what any particular act should do or which
moments a business declares matter.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| workflow | MODIFY | An act announces one moment and some acts complete several, so a declared moment goes unannounced with nobody having agreed it should. The limit is carried by implementation rather than stated by any rule, so the model is declared for the first time rather than relaxed. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Act | Something the business does as one unit, which completes or is refused. |
| Moment | Something the business declared matters, recognised when it occurs. |
| Announcement | An act stating that a moment occurred. |
| Terminal node | Where an act ends, and what carries its announcement. |
| Order | The sequence in which several announcements are made. |
| Evidence record | The observable trace that a moment was announced. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| One terminal node can announce more than one declared moment. |
| Several moments are announced in a stated order, the same order every time. |
| One distinct evidence record is produced per moment announced, so a moment announced is a moment observable. |
| An announcement that cannot be made is reported rather than passed over. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| One act may complete more than one declared moment, and this is ordinary rather than exotic. | HIGH |
| A declared moment that is never announced is a defect, because the business declared that it matters. | HIGH |
| An act is not split to fit a limitation of the announcement mechanism; that changes the business to suit the platform. | HIGH |
| The order several moments are announced in is the order the design states, and that order carries meaning. | HIGH |
| An act whose announcement cannot be made is not refused; its work is already done and a record is immutable once written. | HIGH |
| An announcement that cannot be made is reported, and the moments already announced stand, because they are true. | HIGH |
| Each moment announced produces its own evidence record. | HIGH |
| A terminal node names each moment at most once; announcing one moment twice from one act says it occurred twice. | HIGH |
| Several instances of one kind of moment, about different subjects, is a different shape and not this change. | HIGH |
| A behaviour the platform performs and no document governs is ungoverned rather than leniently governed. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| A terminal node names a single moment, and the running system resolves a single moment for a given act and outcome. | The whole of this change. | Establish how many moments a terminal node carries today, and where that number is fixed. |
| An act exists that completes several declared moments and can announce one. | Establishes the requirement occurred rather than being foreseen. | Confirm an instance, confirm how many moments it completes, and confirm how many it can announce. |
| Nothing governing states what a terminal node announces. | Decides whether this relaxes a rule or states a model for the first time. | Establish what governs announcement today, and what it says. |
| A subdomain exists whose declared moments are announced by nothing at all. | Says the cost is already being paid, and paid as silence rather than as a wrong answer. | Confirm which declared moments no act announces, and whether that was a choice. |
| Nothing counts the moments an act announces — no rule, no published surface, no boundary declaration. | Says how much of the composition a change to the model would disturb. | Establish every consumer of an announced moment and what each relies on. |
| A reader exists that takes the first announced moment it finds. | Says where several would arrive without anyone noticing. | Confirm the reader, and what it would do if an act announced more than one. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The moments one act completes are few and known when the act is designed, rather than one per member of a collection. | The confirmed instance completes three, each a distinct kind. |
| An announcement failure is rare and caused by the same conditions that make any record fail to write. | Announcement writes evidence the same way every other record is written. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The stated order is normative; announcing in a different order is announcing something else. | Business author |
| One evidence record per moment announced, whether the act announces one moment or several. | Business author |
| A terminal node names each moment at most once. | Business author |
| No declared moment an act completes is passed over in silence. | Business author |
| An act is never split, and no moment is dropped, to fit the announcement mechanism. | Business author |
| A moment per member of a collection is not admitted by this change. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every declared moment an act completes is announced by that act. |
| Several moments are announced in the order the design states. |
| Each moment announced has its own evidence record. |
| An act announces each moment at most once. |
| An announcement that cannot be made is reported, and never passed over. |
| A moment announced is a moment that occurred. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Moment | Declared | The business says it matters and has named it. |
| Moment | Announced | An act has stated that it occurred, and there is a record of the statement. |
| Moment | Declared and unannounceable | The act that completes it cannot say so, which is the state this change ends. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| An act announced its moments | When an act reaches the end and states what it completed | The business's account of the act is complete and observable. |
| An announcement could not be made | When a moment an act completed cannot be stated | The account is incomplete, and the incompleteness is visible rather than silent. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Which moments an act announces | The domain that owns the act |
| Whether an act may announce several | The platform |
| The order several moments are announced in | The design that states them |
| What counts as evidence that a moment was announced | The platform |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Which moments any act announces | Each domain's business, stated in its own change. |
| Whether an act should complete several moments | Some do; this change follows that fact rather than judging it. |
| A moment announced per member of a collection | A different shape, and not what the confirmed requirement needs. |
| Anything about the lifecycle that governs change | A platform capability, distinct from the lifecycle dossiers. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| workflow | MODIFIED |
| event | ADJACENT |
| design | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| One successful traversal of an act that completes several declared moments announces every one of them. |
| The moments are announced in the order the design stated, and the same order on every traversal. |
| Each moment announced leaves its own evidence record, with no duplicate and none omitted. |
| An act that names one moment announces exactly what it announces today. |
| An act whose announcement cannot be made reports the failure, and the moments already announced remain announced. |
| A design naming the same moment twice at one terminal node is refused when the composition is built. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Moment | The declaration that names it | Two announcements name the same declaration, whatever else differs. |
| Announcement | The act that made it and the moment it names | One act states one moment once. |
| Evidence record | The announcement it records | They record the same announcement. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Moment | Declared | Announced | The act that completes it reaching its end. | One evidence record is written. Nothing else follows, and no other moment is announced by the same statement. |
| Moment | Declared and unannounceable | Announced | The act gaining the ability to state every moment it completes. | Nothing else follows. The act does what it already did and now says so. |
| Moment | Declared | Declared and unannounceable | An announcement that cannot be made. | The act reports the failure. Moments already announced stand, because they are true. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a composition | An act names the same moment twice at one terminal node | Announcing one moment twice from one act says it occurred twice, and a reader counting occurrences would conclude something happened that did not. |
| Announcing | A moment an act completed cannot be stated | The failure is reported rather than passed over, because a declared moment silently unannounced is the defect this change exists to remove. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| A moment announced per member of a collection | A later change | An act needs to announce one moment per member rather than a known few. |
| Which moments each act announces | Each domain | That domain raises the change that needs them. |
