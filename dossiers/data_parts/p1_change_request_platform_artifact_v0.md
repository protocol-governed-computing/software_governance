# Stage 1 — Change Request: Clarification & Fact Capture: platform / artifact
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** data_parts
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
| artifact | MODIFY | A vector's cases are data, and the platform reads them as declarations, so a value that looks like a name is refused. The platform declares a kind of part it does not yet have. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Declaration | What an artifact states, read the same way by every reader. | CR seed §2 Business Vocabulary #1 |
| Reference | A name, in a part declared to hold names, that the platform resolves. | CR seed §2 Business Vocabulary #2 |
| Value | Something a declaration states that names nothing. | CR seed §2 Business Vocabulary #3 |
| Data part | A part whose contents are values, never read for references. | CR seed §2 Business Vocabulary #4 |
| Test vector | A statement of what a transform is handed and what it must return. | CR seed §2 Business Vocabulary #5 |
| Case | One stated input and its expected result, within a test vector. | CR seed §2 Business Vocabulary #6 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A test vector's cases are declared to be data. | CR seed §3 Requested Outcomes #1 |
| A value inside a vector's cases is never read as a reference, whatever it looks like. | CR seed §3 Requested Outcomes #2 |
| The transform a vector tests is still a reference the platform resolves. | CR seed §3 Requested Outcomes #3 |
| Every other part of every declaration is read exactly as it is today. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A name written in a part declared to hold names is a reference, and the platform resolves it. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A name written in any other part is refused as undeclared. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| What names another artifact is declared, never inferred. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A supersession part names an artifact without reaching it, and is not read for references. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A test vector's cases hold the values a transform is handed and must return. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A transform that turns a design into artifacts is handed and returns values that name artifacts. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Every transform is required to carry a test vector. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A data part is declared one by one, as a reference part is. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| The transform a vector tests is outside its cases. | HIGH | CR seed §4 Known Facts — Business Truths #9 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| A value written as a full name inside a vector's cases is refused as an undeclared reference. | The whole of this change. | Confirm a vector whose case holds a full name is refused when the composition is built. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Every reader that finds references reads one declaration of how a declaration is read. | Says the change is one declaration and the readers that read it. | Establish every place that finds references, and what each reads. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| No kind other than a test vector uses a part named for its cases. | Says a data part named for cases changes nothing else. | Establish every kind that declares such a part. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| Vectors are the only data that holds names today. | No other kind states values handed to or returned by a transform. | CR seed §6 Assumptions #1 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| A data part is declared, never inferred. | Business author | CR seed §7 Constraints #1 |
| A part outside a vector's cases is read exactly as it is today. | Business author | CR seed §7 Constraints #2 |
| An unrecognised name outside a data part is still refused. | Business author | CR seed §7 Constraints #3 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Every reference is in a part declared to hold references. | CR seed §8 Business Invariants #1 |
| Nothing inside a data part is read as a reference. | CR seed §8 Business Invariants #2 |
| A reader of a declaration reads it the way every other reader does. | CR seed §8 Business Invariants #3 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Part | Declared | The platform says how its contents are read. | CR seed §9 Lifecycle States #1 |
| Part | Undeclared | The platform says nothing about it, and a name in it is refused. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A declaration was read | When the platform builds a composition | Every reference in it was found and resolved, and every value was left as a value. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| How a declaration is read | The platform | CR seed §11 Authority Boundaries #1 |
| What a vector states | The domain that owns the transform | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What any vector states | Each domain's business. | CR seed §12 Out of Scope #1 |
| Which vectors any domain carries | Each domain's business. | CR seed §12 Out of Scope #2 |
| Any other part of how a declaration is read | Not what this change needs. | CR seed §12 Out of Scope #3 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| artifact | MODIFIED | CR seed §13 Governance Scope #1 |
| conformance | ADJACENT | CR seed §13 Governance Scope #2 |

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
| A vector whose cases hold a value written as a full name builds. | CR seed §15 Acceptance Criteria #1 |
| The transform a vector tests is still resolved, and a vector naming a transform that does not exist is still refused. | CR seed §15 Acceptance Criteria #2 |
| A name written outside any declared part is still refused. | CR seed §15 Acceptance Criteria #3 |
| Every composition that built before builds the same afterwards. | CR seed §15 Acceptance Criteria #4 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Part | Its name | Two parts carry the same name, in any kind. | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Part | Undeclared | Declared | The platform declaring how its contents are read. | Every reader reads it the declared way. | CR seed §17 Lifecycle Transitions #1 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Building a composition | A name is written outside any declared part | What names another artifact is declared, never inferred. | CR seed §18 Operation Refusals #1 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| NONE |  |  | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
