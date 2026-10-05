# Change Seed — platform / published rules

**Stage:** 0 — Change Seed
**CR:** published_rules
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The execution topology subdomain governs how a contract is built from steps: that each step
dispatches one capability, answers the outcomes it can produce, and says for each what happens next.
The trace subdomain governs the run's record: what a trace holds and the schema every line conforms
to. Each decides what makes its subject sound, and neither decides what any particular contract does.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| execution_topology | MODIFY | The rule that a step routes every outcome it can produce requires more than it did when published, under its published identity. |
| trace | MODIFY | The rule that governs the run's record names a schema other than the one it named when published, under its published identity. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Published | Sealed into a composition that was released and cited. |
| Published identity | An identity a released composition holds; what it means is fixed. |
| Successor | The new identity that states what a rule now requires. |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. |
| Routing rule | The rule that a step routes every outcome it can produce. |
| Record rule | The rule that governs the run's record and names the schema its lines conform to. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The routing rule has a successor that states what it now requires. |
| The record rule has a successor that names the schema traces now conform to. |
| Each published rule says again what it said when it was published, and is stood down. |
| Everything that names a changed rule names its successor. |
| Every check enforces what it enforces today, under the identity that now says so. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| Identity is fixed at publication; an unpublished identity may change before release. | HIGH |
| A change of meaning is a new identity, and the old one stays in the record and out of reach. | HIGH |
| What the two rules now require is right; nothing they enforce is relaxed. | HIGH |
| No composition changes what it does. | HIGH |
| Each stood-down rule keeps the check that realized it when it was published. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The routing rule's text and check require more than they did in v5. | It is what this change re-identifies. | Establish what the rule and its check required in v5 and require now. |
| The record rule names a different schema than it did in v5. | It is what this change re-identifies. | Establish what the rule named in v5 and names now. |
| Few artifacts name either rule. | Each must name its successor. | Establish every artifact, and any code, that names either rule by identity. |
| No other published rule changed what it requires this cycle. | The change must be the whole of it. | Establish every published identity whose meaning changed since v5. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every composition builds and runs as it does today. | Business author |
| No published identity changes what it says, except to be stood down. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A published identity means what it meant when it was published. |
| Every rule in force says what its check enforces. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Routing rule | In force | Checked whenever a composition is built. |
| Routing rule | Stood down | Replaced by its successor, kept in the record as published. |
| Record rule | In force | Governs every trace a run writes. |
| Record rule | Stood down | Replaced by its successor, kept in the record as published. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | | |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a step must route | Execution topology |
| What a trace must conform to | Trace |
| What is published, and when | The business author |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Contracts and workflows whose routes changed in place this cycle | Each domain's own change. |
| What either rule requires | Settled; only its identity changes. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| execution_topology | MODIFIED |
| trace | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| The routing rule's successor states every outcome a capability declares must be routed, and its check is today's. |
| The record rule's successor names the schema traces now conform to. |
| Each published rule's text is what v5 published, with only its stand-down added. |
| Each stood-down rule keeps the check that realized it in v5. |
| Nothing in force names a stood-down rule. |
| Every composition builds and runs as it does today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Published rule | Its identity | Its text is what the release sealed |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Routing rule | In force | Stood down | This change adds its successor | Whatever names it is re-pointed |
| Record rule | In force | Stood down | This change adds its successor | Whatever names it is re-pointed |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| NONE IDENTIFIED | | |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Routes changed in place in contracts and workflows | Each domain | Its own change |
