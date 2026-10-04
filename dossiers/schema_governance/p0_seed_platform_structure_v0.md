# Change Seed — platform / structure

**Stage:** 0 — Change Seed
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The structure subdomain governs how the platform describes itself to itself: what a declaration of
each kind may contain, which description governs which kind, and where each is found. Its authority
is to decide what makes a description binding. It decides nothing about what any particular artifact
declares.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| structure | MODIFY | A third of the composition is described by nothing, the descriptions that exist have rotted unread, two kinds have none, and five leave their surface open. Which kinds are described, by what, and how a description stays current are restated together. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Declaration | What an artifact says about itself, in the block the platform reads. |
| Description | A statement of what a declaration of one kind may contain. |
| Dispatch | The table naming which description governs which kind. |
| Closed surface | A description that admits only what it names. An open one admits anything beside it. |
| Governed kind | A kind whose declarations are checked against a description. |
| Stale description | One that describes a shape the platform has stopped building. |
| False refusal | A correct declaration turned away by a description that is wrong about it. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Every artifact kind either has a description that governs it, or a recorded reason why it needs none. |
| Whether a kind is described is a decision somebody made, readable as such. |
| A description matches the shape the platform currently builds. |
| A description admits only what it names. |
| The two boundary kinds a caller reaches the composition through are described. |
| A genuinely invalid declaration is refused, and a correct one is not. |
| A description that stops matching what it describes is reported before it turns correct work away. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| Six of fifteen artifact kinds are named by the dispatch table nowhere. | HIGH |
| Those six carry 139 of the composition's 428 artifacts. | HIGH |
| Four of the six have a description written and never named by the table. | HIGH |
| Dispatching those four refuses one hundred declarations. | HIGH |
| Not one of the hundred is a defective artifact; every one is the description being wrong. | HIGH |
| Sixty-two expect a constitution named by a bare name where every artifact now carries a qualified one. | HIGH |
| Twenty-two describe an actor with a role and no attributes, which is not the actor the platform builds. | HIGH |
| Ten forbid content an event legitimately carries, and five reject a whole number as a type. | HIGH |
| Two kinds — the transport boundary contracts, forty-four artifacts — have no description at all. | HIGH |
| Five descriptions that are dispatched do not close their surface. | HIGH |
| One of the six undispatched kinds validates cleanly against its description and is now dispatched. | HIGH |
| A description nobody reads cannot be found wrong, which is why these rotted unnoticed. | HIGH |
| Not every kind requires a description; a kind may be exempt where the ground is stated. Ruled by the business author. | HIGH |
| An exemption recorded is governed; an absence reads the same as nobody having decided, and is not. | HIGH |
| A wrong description refuses correct work with the authority of a rule, so more coverage is not automatically more governance. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The dispatch table is the sole authority for which kind is described by what. | Decides whether the fix is one table or many places. | Establish what reads the table and whether anything selects a description another way. |
| The four unnamed descriptions rotted at a namespace change and not before. | Says whether staleness is one event or continuous drift. | Establish when each description last matched what it describes. |
| Every one of the hundred refusals is the description being wrong. | The whole basis for not treating 139 artifacts as defects. | Confirm, for each of the four shapes, that the artifacts are what the platform currently builds. |
| Nothing reports a description that has stopped matching. | Says whether the fix must include a mechanism or only a correction. | Establish whether any check compares a description against the artifacts of its kind. |
| Not every artifact kind requires a description. | Decides whether the goal is total coverage or a stated policy. | Establish, for each of the fifteen kinds, whether a description is required and on what ground. |
| Closing an open surface refuses nothing that is currently built. | Decides whether closing five surfaces is a correction or a change in what is admissible. | Measure each of the five against every artifact of its kind. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| A description was correct when written. | Each matches an artifact shape the platform did build, and each stopped matching at a change nobody applied to it. |
| A kind carrying many artifacts is more likely to need describing than one carrying few. | Not established, and named here so it is argued rather than assumed. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No correct declaration is refused. A description that would turn one away is wrong and is corrected before it is dispatched. | Business author |
| No artifact is edited to satisfy a description that describes a shape the platform has stopped building. | Business author |
| A kind is dispatched only after its description has been measured against every artifact of that kind. | Business author |
| Whether a kind requires a description is decided and recorded, never left to whether one happens to exist. | Business author |
| The 139 currently undescribed artifacts are not treated as defects. | Business author |
| A genuinely invalid declaration is still refused; this change does not weaken what is checked. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every artifact kind is either described, or recorded as exempt with the ground stated. |
| An exemption states its ground. An exemption without one is an absence wearing a decision's clothes. |
| A description matches the shape the platform currently builds. |
| A description admits only what it names. |
| A correct declaration is never refused. |
| A description that stops matching what it describes is reported. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Kind | Described | A description governs it and the build reads it. |
| Kind | Exempt | Recorded as needing no description, with the ground stated. |
| Kind | Undescribed | Neither, and nobody has decided which. This is the state this change ends. |
| Description | Current | It matches what the platform builds. |
| Description | Stale | It describes a shape the platform has stopped building, and nothing reports it. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A declaration was refused | When it does not match the description of its kind | The platform caught something wrong, which is the point. |
| A correct declaration was refused | When a description has stopped matching what it describes | The platform turned away correct work with the authority of a rule. |
| A description stopped matching | When the shape of a kind changes and the description does not | Today this is silent, and stays silent until someone dispatches it. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Which kind is described by what | The structure subdomain |
| What a declaration of a kind may contain | The subdomain that owns the kind |
| Whether a kind requires a description | The structure subdomain |
| What any particular artifact declares | The artifact's author |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Changing what any artifact declares | The artifacts are what the platform currently builds; it is the descriptions that are wrong. |
| The content of any kind's declaration | Each kind's own subdomain decides what a declaration means; this change decides that it is described. |
| Kinds that do not exist in the composition | Nothing to describe and nothing to decide. |
| The one kind already corrected and dispatched | Done; it validates cleanly and is named by the table. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| structure | MODIFIED |
| actor | ADJACENT |
| event | ADJACENT |
| intent | ADJACENT |
| transport | ADJACENT |
| authority | ADJACENT |
| trace | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| Where a kind's description is stale, does the description move to the artifacts or is the shape reconsidered? | The artifacts are current, but a description written deliberately and then diverged from may be recording an intent worth recovering. | NO | GOVERNANCE |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Every artifact kind in the composition is described or recorded as exempt, with the ground stated. |
| Dispatching every described kind refuses no artifact the composition currently carries. |
| The two transport boundary kinds are described and dispatched. |
| Every dispatched description admits only what it names. |
| A declaration carrying content its description does not name is refused. |
| A description that stops matching the artifacts of its kind is reported without anyone dispatching it to find out. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Description | The kind it governs | One kind is described by one description. |
| Kind | Its name in the declaration | Two declarations naming one kind are of one kind. |
| Dispatch | The table it is stated in | One table states every dispatch. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Kind | Undescribed | Described | Its description being measured against every artifact of that kind, then named by the table. | Declarations of that kind are checked from the next build onward. |
| Kind | Undescribed | Exempt | A decision that the kind needs no description, with the ground recorded. | Nothing checks it, and the reason is readable rather than an absence. |
| Description | Stale | Current | Being brought to the shape the platform builds. | Its kind becomes dispatchable without refusing correct work. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a composition | A declaration carries content the description of its kind does not name | An artifact may say only what its kind admits, or the description states nothing. |
| Building a composition | An artifact kind is neither described nor recorded as exempt | A kind nobody decided about is a kind nobody described, and the absence reads the same as a decision. |
| Dispatching a description | It refuses an artifact the composition currently carries | A description that turns away correct work refuses with the authority of a rule, which is worse than describing nothing. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| What a declaration of each kind means | The subdomain that owns the kind | That subdomain is asked what its kind admits. |
| Whether a diverged description recorded an intent worth recovering | A ruling | The clarification this seed raises is answered, per kind. |
