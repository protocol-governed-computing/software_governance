# Stage 1 — Change Request: Clarification & Fact Capture: platform / reference semantics
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** reference_semantics
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
| artifact | MODIFY | Nothing declares which parts of a declaration name another artifact, so three parts of the platform decide it three ways. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Declaration | What an artifact states about itself, in the form the platform reads. | CR seed §2 Business Vocabulary #1 |
| Reference | A part of a declaration whose value names another artifact. | CR seed §2 Business Vocabulary #2 |
| Full name | An artifact's name with the namespace it is declared in. | CR seed §2 Business Vocabulary #3 |
| Re-point | Changing a reference to name the declared successor of what it named, and nothing else. | CR seed §2 Business Vocabulary #4 |
| Record of references | The platform's account of which artifact names which, that inspection answers from. | CR seed §2 Business Vocabulary #5 |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. | CR seed §2 Business Vocabulary #6 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The declaration of what carries no meaning also names every part of a declaration that is a reference. | CR seed §3 Requested Outcomes #1 |
| It states that a reference re-pointed to the declared successor of what it named is not a change of meaning. | CR seed §3 Requested Outcomes #2 |
| It states that a part declared explanation is exempt only where its value is text. | CR seed §3 Requested Outcomes #3 |
| The record of references and the check that nothing reaches a stood-down artifact read that one declaration. | CR seed §3 Requested Outcomes #4 |
| A full name written in a part not declared a reference is refused. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A change of meaning is a new identity; a change of how it is written is not. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| What carries no meaning, and what names another artifact, is declared, never inferred. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A reference to a stood-down artifact is re-pointed or retired. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Re-pointing keeps the referring artifact's identity. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Adding to the declaration is a change of meaning, so the declaration is replaced by a new version. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| This is the last change to the declaration in this cycle. | HIGH | CR seed §4 Known Facts — Business Truths #6 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The record of references reads a fixed list of parts and misses most of them. | A change cannot learn what reaches an artifact it stands down. | Establish which parts the record reads, and which artifacts it under-counts. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The check that nothing reaches a stood-down artifact reads every value that looks like a name. | It and the record disagree about what a reference is. | Establish how the check finds references. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| No part of a declaration declared explanation holds anything but text today. | Stating the text-only rule must refuse no composition the platform holds. | Establish the value of every part declared explanation. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Every full name in the composition sits in a part that can be declared a reference. | Refusing undeclared references must refuse no composition the platform holds. | Establish every part that holds a full name. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

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
| Every composition the platform holds builds and runs as it does today, with a fuller record of references. | Business author | CR seed §7 Constraints #1 |
| One declaration says what a reference is; nothing else decides it. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| One place declares which parts of a declaration are references. | CR seed §8 Business Invariants #1 |
| Every full name in a declaration sits in a part declared a reference. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Declaration of what carries no meaning | In force | Consulted wherever two declarations are compared or references are found. | CR seed §9 Lifecycle States #1 |
| Declaration of what carries no meaning | Stood down | Replaced by the version this change adds, kept in the record and out of reach. | CR seed §9 Lifecycle States #2 |

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
| Which parts of a declaration are references | Artifact | CR seed §11 Authority Boundaries #2 |
| What any part of a declaration means | The subdomain that declares the artifact | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Comparing a change with what it changes | The design and build change that follows. | CR seed §12 Out of Scope #1 |
| Checking what a replacement reaches | The design and build change that follows. | CR seed §12 Out of Scope #2 |
| Names written by short code | The compiler resolves a workflow's places and contracts its own way; declaring them is later work. | CR seed §12 Out of Scope #3 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| artifact | MODIFIED | CR seed §13 Governance Scope #1 |
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
| The new declaration names every part of a declaration that holds a full name in the composition. | CR seed §15 Acceptance Criteria #1 |
| It states the re-point rule and the text-only rule. | CR seed §15 Acceptance Criteria #2 |
| The old declaration is stood down, kept in the record and out of reach. | CR seed §15 Acceptance Criteria #3 |
| The record of references names every artifact that names another, including the rule that governs assertion and the actor a phase admits. | CR seed §15 Acceptance Criteria #4 |
| The check that nothing reaches a stood-down artifact finds exactly the references the declaration names. | CR seed §15 Acceptance Criteria #5 |
| A full name written in a part not declared a reference is refused, and the refusal names the part. | CR seed §15 Acceptance Criteria #6 |
| Every composition the platform holds builds and runs as it does today. | CR seed §15 Acceptance Criteria #7 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Reference | The part it sits in and the artifact it names | They name the same artifact, or the second names the declared successor of the first | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Declaration of what carries no meaning | In force | Stood down | This change adds its successor | Nothing names it, so nothing is re-pointed | CR seed §17 Lifecycle Transitions #1 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Building a composition | A full name sits in a part not declared a reference | What names another artifact is declared, never inferred. | CR seed §18 Operation Refusals #1 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| How two declarations are compared | The design and build change that follows | It is designed | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
