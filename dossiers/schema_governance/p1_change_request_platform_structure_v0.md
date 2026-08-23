# Stage 1 — Change Request: Clarification & Fact Capture: platform / structure
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** schema_governance
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
| structure | MODIFY | A third of the composition is described by nothing, the descriptions that exist have rotted unread, two kinds have none, and five leave their surface open. Which kinds are described, by what, and how a description stays current are restated together. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Declaration | What an artifact says about itself, in the block the platform reads. | CR seed §2 Business Vocabulary #1 |
| Description | A statement of what a declaration of one kind may contain. | CR seed §2 Business Vocabulary #2 |
| Dispatch | The table naming which description governs which kind. | CR seed §2 Business Vocabulary #3 |
| Closed surface | A description that admits only what it names. An open one admits anything beside it. | CR seed §2 Business Vocabulary #4 |
| Governed kind | A kind whose declarations are checked against a description. | CR seed §2 Business Vocabulary #5 |
| Stale description | One that describes a shape the platform has stopped building. | CR seed §2 Business Vocabulary #6 |
| False refusal | A correct declaration turned away by a description that is wrong about it. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Every artifact kind either has a description that governs it, or a recorded reason why it needs none. | CR seed §3 Requested Outcomes #1 |
| Whether a kind is described is a decision somebody made, readable as such. | CR seed §3 Requested Outcomes #2 |
| A description matches the shape the platform currently builds. | CR seed §3 Requested Outcomes #3 |
| A description admits only what it names. | CR seed §3 Requested Outcomes #4 |
| The two boundary kinds a caller reaches the composition through are described. | CR seed §3 Requested Outcomes #5 |
| A genuinely invalid declaration is refused, and a correct one is not. | CR seed §3 Requested Outcomes #6 |
| A description that stops matching what it describes is reported before it turns correct work away. | CR seed §3 Requested Outcomes #7 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| Six of fifteen artifact kinds are named by the dispatch table nowhere. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Those six carry 139 of the composition's 428 artifacts. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Four of the six have a description written and never named by the table. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Dispatching those four refuses one hundred declarations. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Not one of the hundred is a defective artifact; every one is the description being wrong. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Sixty-two expect a constitution named by a bare name where every artifact now carries a qualified one. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Twenty-two describe an actor with a role and no attributes, which is not the actor the platform builds. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| Ten forbid content an event legitimately carries, and five reject a whole number as a type. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| Two kinds — the transport boundary contracts, forty-four artifacts — have no description at all. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| Five descriptions that are dispatched do not close their surface. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| One of the six undispatched kinds validates cleanly against its description and is now dispatched. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| A description nobody reads cannot be found wrong, which is why these rotted unnoticed. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| Not every kind requires a description; a kind may be exempt where the ground is stated. Ruled by the business author. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| An exemption recorded is governed; an absence reads the same as nobody having decided, and is not. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| A wrong description refuses correct work with the authority of a rule, so more coverage is not automatically more governance. | HIGH | CR seed §4 Known Facts — Business Truths #15 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The dispatch table is the sole authority for which kind is described by what. | Decides whether the fix is one table or many places. | Establish what reads the table and whether anything selects a description another way. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The four unnamed descriptions rotted at a namespace change and not before. | Says whether staleness is one event or continuous drift. | Establish when each description last matched what it describes. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Every one of the hundred refusals is the description being wrong. | The whole basis for not treating 139 artifacts as defects. | Confirm, for each of the four shapes, that the artifacts are what the platform currently builds. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Nothing reports a description that has stopped matching. | Says whether the fix must include a mechanism or only a correction. | Establish whether any check compares a description against the artifacts of its kind. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Not every artifact kind requires a description. | Decides whether the goal is total coverage or a stated policy. | Establish, for each of the fifteen kinds, whether a description is required and on what ground. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| Closing an open surface refuses nothing that is currently built. | Decides whether closing five surfaces is a correction or a change in what is admissible. | Measure each of the five against every artifact of its kind. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| A description was correct when written. | Each matches an artifact shape the platform did build, and each stopped matching at a change nobody applied to it. | CR seed §6 Assumptions #1 |
| A kind carrying many artifacts is more likely to need describing than one carrying few. | Not established, and named here so it is argued rather than assumed. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| No correct declaration is refused. A description that would turn one away is wrong and is corrected before it is dispatched. | Business author | CR seed §7 Constraints #1 |
| No artifact is edited to satisfy a description that describes a shape the platform has stopped building. | Business author | CR seed §7 Constraints #2 |
| A kind is dispatched only after its description has been measured against every artifact of that kind. | Business author | CR seed §7 Constraints #3 |
| Whether a kind requires a description is decided and recorded, never left to whether one happens to exist. | Business author | CR seed §7 Constraints #4 |
| The 139 currently undescribed artifacts are not treated as defects. | Business author | CR seed §7 Constraints #5 |
| A genuinely invalid declaration is still refused; this change does not weaken what is checked. | Business author | CR seed §7 Constraints #6 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every artifact kind is either described, or recorded as exempt with the ground stated. | CR seed §8 Business Invariants #1 |
| An exemption states its ground. An exemption without one is an absence wearing a decision's clothes. | CR seed §8 Business Invariants #2 |
| A description matches the shape the platform currently builds. | CR seed §8 Business Invariants #3 |
| A description admits only what it names. | CR seed §8 Business Invariants #4 |
| A correct declaration is never refused. | CR seed §8 Business Invariants #5 |
| A description that stops matching what it describes is reported. | CR seed §8 Business Invariants #6 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Kind | Described | A description governs it and the build reads it. | CR seed §9 Lifecycle States #1 |
| Kind | Exempt | Recorded as needing no description, with the ground stated. | CR seed §9 Lifecycle States #2 |
| Kind | Undescribed | Neither, and nobody has decided which. This is the state this change ends. | CR seed §9 Lifecycle States #3 |
| Description | Current | It matches what the platform builds. | CR seed §9 Lifecycle States #4 |
| Description | Stale | It describes a shape the platform has stopped building, and nothing reports it. | CR seed §9 Lifecycle States #5 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A declaration was refused | When it does not match the description of its kind | The platform caught something wrong, which is the point. | CR seed §10 Business Events #1 |
| A correct declaration was refused | When a description has stopped matching what it describes | The platform turned away correct work with the authority of a rule. | CR seed §10 Business Events #2 |
| A description stopped matching | When the shape of a kind changes and the description does not | Today this is silent, and stays silent until someone dispatches it. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Which kind is described by what | The structure subdomain | CR seed §11 Authority Boundaries #1 |
| What a declaration of a kind may contain | The subdomain that owns the kind | CR seed §11 Authority Boundaries #2 |
| Whether a kind requires a description | The structure subdomain | CR seed §11 Authority Boundaries #3 |
| What any particular artifact declares | The artifact's author | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Changing what any artifact declares | The artifacts are what the platform currently builds; it is the descriptions that are wrong. | CR seed §12 Out of Scope #1 |
| The content of any kind's declaration | Each kind's own subdomain decides what a declaration means; this change decides that it is described. | CR seed §12 Out of Scope #2 |
| Kinds that do not exist in the composition | Nothing to describe and nothing to decide. | CR seed §12 Out of Scope #3 |
| The one kind already corrected and dispatched | Done; it validates cleanly and is named by the table. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| structure | MODIFIED | CR seed §13 Governance Scope #1 |
| actor | ADJACENT | CR seed §13 Governance Scope #2 |
| event | ADJACENT | CR seed §13 Governance Scope #3 |
| intent | ADJACENT | CR seed §13 Governance Scope #4 |
| transport | ADJACENT | CR seed §13 Governance Scope #5 |
| authority | ADJACENT | CR seed §13 Governance Scope #6 |
| trace | ADJACENT | CR seed §13 Governance Scope #7 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| Where a kind's description is stale, does the description move to the artifacts or is the shape reconsidered? | The artifacts are current, but a description written deliberately and then diverged from may be recording an intent worth recovering. | NO | GOVERNANCE | CR seed §14 Clarification Requests #1 |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| Every artifact kind in the composition is described or recorded as exempt, with the ground stated. | CR seed §15 Acceptance Criteria #1 |
| Dispatching every described kind refuses no artifact the composition currently carries. | CR seed §15 Acceptance Criteria #2 |
| The two transport boundary kinds are described and dispatched. | CR seed §15 Acceptance Criteria #3 |
| Every dispatched description admits only what it names. | CR seed §15 Acceptance Criteria #4 |
| A declaration carrying content its description does not name is refused. | CR seed §15 Acceptance Criteria #5 |
| A description that stops matching the artifacts of its kind is reported without anyone dispatching it to find out. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Description | The kind it governs | One kind is described by one description. | CR seed §16 Identity and Sameness #1 |
| Kind | Its name in the declaration | Two declarations naming one kind are of one kind. | CR seed §16 Identity and Sameness #2 |
| Dispatch | The table it is stated in | One table states every dispatch. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Kind | Undescribed | Described | Its description being measured against every artifact of that kind, then named by the table. | Declarations of that kind are checked from the next build onward. | CR seed §17 Lifecycle Transitions #1 |
| Kind | Undescribed | Exempt | A decision that the kind needs no description, with the ground recorded. | Nothing checks it, and the reason is readable rather than an absence. | CR seed §17 Lifecycle Transitions #2 |
| Description | Stale | Current | Being brought to the shape the platform builds. | Its kind becomes dispatchable without refusing correct work. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Building a composition | A declaration carries content the description of its kind does not name | An artifact may say only what its kind admits, or the description states nothing. | CR seed §18 Operation Refusals #1 |
| Building a composition | An artifact kind is neither described nor recorded as exempt | A kind nobody decided about is a kind nobody described, and the absence reads the same as a decision. | CR seed §18 Operation Refusals #2 |
| Dispatching a description | It refuses an artifact the composition currently carries | A description that turns away correct work refuses with the authority of a rule, which is worse than describing nothing. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| What a declaration of each kind means | The subdomain that owns the kind | That subdomain is asked what its kind admits. | CR seed §19 Authority Deferrals #1 |
| Whether a diverged description recorded an intent worth recovering | A ruling | The clarification this seed raises is answered, per kind. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
