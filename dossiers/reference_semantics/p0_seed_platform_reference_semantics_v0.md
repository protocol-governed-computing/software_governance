# Change Seed — platform / reference semantics

**Stage:** 0 — Change Seed
**CR:** reference_semantics
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
| artifact | MODIFY | Nothing declares which parts of a declaration name another artifact, so three parts of the platform decide it three ways. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Declaration | What an artifact states about itself, in the form the platform reads. |
| Reference | A part of a declaration whose value names another artifact. |
| Full name | An artifact's name with the namespace it is declared in. |
| Re-point | Changing a reference to name the declared successor of what it named, and nothing else. |
| Record of references | The platform's account of which artifact names which, that inspection answers from. |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The declaration of what carries no meaning also names every part of a declaration that is a reference. |
| It states that a reference re-pointed to the declared successor of what it named is not a change of meaning. |
| It states that a part declared explanation is exempt only where its value is text. |
| The record of references and the check that nothing reaches a stood-down artifact read that one declaration. |
| A full name written in a part not declared a reference is refused. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A change of meaning is a new identity; a change of how it is written is not. | HIGH |
| What carries no meaning, and what names another artifact, is declared, never inferred. | HIGH |
| A reference to a stood-down artifact is re-pointed or retired. | HIGH |
| Re-pointing keeps the referring artifact's identity. | HIGH |
| Adding to the declaration is a change of meaning, so the declaration is replaced by a new version. | HIGH |
| This is the last change to the declaration in this cycle. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The record of references reads a fixed list of parts and misses most of them. | A change cannot learn what reaches an artifact it stands down. | Establish which parts the record reads, and which artifacts it under-counts. |
| The check that nothing reaches a stood-down artifact reads every value that looks like a name. | It and the record disagree about what a reference is. | Establish how the check finds references. |
| No part of a declaration declared explanation holds anything but text today. | Stating the text-only rule must refuse no composition the platform holds. | Establish the value of every part declared explanation. |
| Every full name in the composition sits in a part that can be declared a reference. | Refusing undeclared references must refuse no composition the platform holds. | Establish every part that holds a full name. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every composition the platform holds builds and runs as it does today, with a fuller record of references. | Business author |
| One declaration says what a reference is; nothing else decides it. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| One place declares which parts of a declaration are references. |
| Every full name in a declaration sits in a part declared a reference. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Declaration of what carries no meaning | In force | Consulted wherever two declarations are compared or references are found. |
| Declaration of what carries no meaning | Stood down | Replaced by the version this change adds, kept in the record and out of reach. |

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
| Which parts of a declaration are references | Artifact |
| What any part of a declaration means | The subdomain that declares the artifact |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Comparing a change with what it changes | The design and build change that follows. |
| Checking what a replacement reaches | The design and build change that follows. |
| Names written by short code | The compiler resolves a workflow's places and contracts its own way; declaring them is later work. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| artifact | MODIFIED |
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
| The new declaration names every part of a declaration that holds a full name in the composition. |
| It states the re-point rule and the text-only rule. |
| The old declaration is stood down, kept in the record and out of reach. |
| The record of references names every artifact that names another, including the rule that governs assertion and the actor a phase admits. |
| The check that nothing reaches a stood-down artifact finds exactly the references the declaration names. |
| A full name written in a part not declared a reference is refused, and the refusal names the part. |
| Every composition the platform holds builds and runs as it does today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Reference | The part it sits in and the artifact it names | They name the same artifact, or the second names the declared successor of the first |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Declaration of what carries no meaning | In force | Stood down | This change adds its successor | Nothing names it, so nothing is re-pointed |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a composition | A full name sits in a part not declared a reference | What names another artifact is declared, never inferred. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| How two declarations are compared | The design and build change that follows | It is designed |
