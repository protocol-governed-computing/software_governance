# Stage 1 — Change Request: Clarification & Fact Capture: platform / published rules
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** published_rules
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
| execution_topology | MODIFY | The rule that a step routes every outcome it can produce requires more than it did when published, under its published identity. | CR seed §1 CR Type #1 |
| trace | MODIFY | The rule that governs the run's record names a schema other than the one it named when published, under its published identity. | CR seed §1 CR Type #2 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Published | Sealed into a composition that was released and cited. | CR seed §2 Business Vocabulary #1 |
| Published identity | An identity a released composition holds; what it means is fixed. | CR seed §2 Business Vocabulary #2 |
| Successor | The new identity that states what a rule now requires. | CR seed §2 Business Vocabulary #3 |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. | CR seed §2 Business Vocabulary #4 |
| Routing rule | The rule that a step routes every outcome it can produce. | CR seed §2 Business Vocabulary #5 |
| Record rule | The rule that governs the run's record and names the schema its lines conform to. | CR seed §2 Business Vocabulary #6 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The routing rule has a successor that states what it now requires. | CR seed §3 Requested Outcomes #1 |
| The record rule has a successor that names the schema traces now conform to. | CR seed §3 Requested Outcomes #2 |
| Each published rule says again what it said when it was published, and is stood down. | CR seed §3 Requested Outcomes #3 |
| Everything that names a changed rule names its successor. | CR seed §3 Requested Outcomes #4 |
| Every check enforces what it enforces today, under the identity that now says so. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| Identity is fixed at publication; an unpublished identity may change before release. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A change of meaning is a new identity, and the old one stays in the record and out of reach. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| What the two rules now require is right; nothing they enforce is relaxed. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| No composition changes what it does. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Each stood-down rule keeps the check that realized it when it was published. | HIGH | CR seed §4 Known Facts — Business Truths #5 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The routing rule's text and check require more than they did in v5. | It is what this change re-identifies. | Establish what the rule and its check required in v5 and require now. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The record rule names a different schema than it did in v5. | It is what this change re-identifies. | Establish what the rule named in v5 and names now. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Few artifacts name either rule. | Each must name its successor. | Establish every artifact, and any code, that names either rule by identity. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| No other published rule changed what it requires this cycle. | The change must be the whole of it. | Establish every published identity whose meaning changed since v5. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

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
| Every composition builds and runs as it does today. | Business author | CR seed §7 Constraints #1 |
| No published identity changes what it says, except to be stood down. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A published identity means what it meant when it was published. | CR seed §8 Business Invariants #1 |
| Every rule in force says what its check enforces. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Routing rule | In force | Checked whenever a composition is built. | CR seed §9 Lifecycle States #1 |
| Routing rule | Stood down | Replaced by its successor, kept in the record as published. | CR seed §9 Lifecycle States #2 |
| Record rule | In force | Governs every trace a run writes. | CR seed §9 Lifecycle States #3 |
| Record rule | Stood down | Replaced by its successor, kept in the record as published. | CR seed §9 Lifecycle States #4 |

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
| What a step must route | Execution topology | CR seed §11 Authority Boundaries #1 |
| What a trace must conform to | Trace | CR seed §11 Authority Boundaries #2 |
| What is published, and when | The business author | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Contracts and workflows whose routes changed in place this cycle | Each domain's own change. | CR seed §12 Out of Scope #1 |
| What either rule requires | Settled; only its identity changes. | CR seed §12 Out of Scope #2 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| execution_topology | MODIFIED | CR seed §13 Governance Scope #1 |
| trace | MODIFIED | CR seed §13 Governance Scope #2 |

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
| The routing rule's successor states every outcome a capability declares must be routed, and its check is today's. | CR seed §15 Acceptance Criteria #1 |
| The record rule's successor names the schema traces now conform to. | CR seed §15 Acceptance Criteria #2 |
| Each published rule's text is what v5 published, with only its stand-down added. | CR seed §15 Acceptance Criteria #3 |
| Each stood-down rule keeps the check that realized it in v5. | CR seed §15 Acceptance Criteria #4 |
| Nothing in force names a stood-down rule. | CR seed §15 Acceptance Criteria #5 |
| Every composition builds and runs as it does today. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Published rule | Its identity | Its text is what the release sealed | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Routing rule | In force | Stood down | This change adds its successor | Whatever names it is re-pointed | CR seed §17 Lifecycle Transitions #1 |
| Record rule | In force | Stood down | This change adds its successor | Whatever names it is re-pointed | CR seed §17 Lifecycle Transitions #2 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| NONE IDENTIFIED |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Routes changed in place in contracts and workflows | Each domain | Its own change | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
