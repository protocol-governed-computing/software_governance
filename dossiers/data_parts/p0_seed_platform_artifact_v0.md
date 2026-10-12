# Change Seed — platform / artifact

**Stage:** 0 — Change Seed
**CR:** data_parts
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the two clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The artifact subdomain governs how a declaration is read: which parts name another artifact, which
parts only explain, which lists are read as sets, and which parts record history. Its authority is
to state, once, how every reader of a declaration tells a name from a value, and it decides nothing
about what any declaration says.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| artifact | MODIFY | A vector's cases are data, and the platform reads them as declarations, so a value that looks like a name is refused. The platform declares a kind of part it does not yet have. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Declaration | What an artifact states, read the same way by every reader. |
| Reference | A name, in a part declared to hold names, that the platform resolves. |
| Value | Something a declaration states that names nothing. |
| Data part | A part whose contents are values, never read for references. |
| Test vector | A statement of what a transform is handed and what it must return. |
| Case | One stated input and its expected result, within a test vector. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A test vector's cases are declared to be data. |
| A value inside a vector's cases is never read as a reference, whatever it looks like. |
| The transform a vector tests is still a reference the platform resolves. |
| Every other part of every declaration is read exactly as it is today. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A name written in a part declared to hold names is a reference, and the platform resolves it. | HIGH |
| A name written in any other part is refused as undeclared. | HIGH |
| What names another artifact is declared, never inferred. | HIGH |
| A supersession part names an artifact without reaching it, and is not read for references. | HIGH |
| A test vector's cases hold the values a transform is handed and must return. | HIGH |
| A transform that turns a design into artifacts is handed and returns values that name artifacts. | HIGH |
| Every transform is required to carry a test vector. | HIGH |
| A data part is declared one by one, as a reference part is. | HIGH |
| The transform a vector tests is outside its cases. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| A value written as a full name inside a vector's cases is refused as an undeclared reference. | The whole of this change. | Confirm a vector whose case holds a full name is refused when the composition is built. |
| Every reader that finds references reads one declaration of how a declaration is read. | Says the change is one declaration and the readers that read it. | Establish every place that finds references, and what each reads. |
| No kind other than a test vector uses a part named for its cases. | Says a data part named for cases changes nothing else. | Establish every kind that declares such a part. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| Vectors are the only data that holds names today. | No other kind states values handed to or returned by a transform. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| A data part is declared, never inferred. | Business author |
| A part outside a vector's cases is read exactly as it is today. | Business author |
| An unrecognised name outside a data part is still refused. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Every reference is in a part declared to hold references. |
| Nothing inside a data part is read as a reference. |
| A reader of a declaration reads it the way every other reader does. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Part | Declared | The platform says how its contents are read. |
| Part | Undeclared | The platform says nothing about it, and a name in it is refused. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A declaration was read | When the platform builds a composition | Every reference in it was found and resolved, and every value was left as a value. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| How a declaration is read | The platform |
| What a vector states | The domain that owns the transform |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What any vector states | Each domain's business. |
| Which vectors any domain carries | Each domain's business. |
| Any other part of how a declaration is read | Not what this change needs. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| artifact | MODIFIED |
| conformance | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| A vector whose cases hold a value written as a full name builds. |
| The transform a vector tests is still resolved, and a vector naming a transform that does not exist is still refused. |
| A name written outside any declared part is still refused. |
| Every composition that built before builds the same afterwards. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Part | Its name | Two parts carry the same name, in any kind. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Part | Undeclared | Declared | The platform declaring how its contents are read. | Every reader reads it the declared way. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a composition | A name is written outside any declared part | What names another artifact is declared, never inferred. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE |
