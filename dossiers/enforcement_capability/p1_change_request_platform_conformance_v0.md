# Stage 1 — Change Request: Clarification & Fact Capture: platform / conformance
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** enforcement_capability
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
| conformance | MODIFY | The obligation-to-check relation is guaranteed by count and not by capability, so a check that cannot refuse satisfies it. The relation is stated; what it must additionally require has never been. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Obligation | Something the platform requires of what it admits. | CR seed §2 Business Vocabulary #1 |
| Check | The mechanism that carries one obligation and decides whether it is met. | CR seed §2 Business Vocabulary #2 |
| Refusal | A check deciding an obligation is not met, and the admission not proceeding. | CR seed §2 Business Vocabulary #3 |
| Capable of refusing | There exists something a check would refuse. A check no input can fail carries nothing. | CR seed §2 Business Vocabulary #4 |
| Enforcement status | What an obligation says about whether its check carries it today. | CR seed §2 Business Vocabulary #5 |
| Delegated enforcement | An obligation carried somewhere other than where it is declared, with that place named. | CR seed §2 Business Vocabulary #6 |
| Coverage | How much of what is declared is actually carried. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| An obligation states whether it is enforced, and the statement is read by a mechanism rather than by a person. | CR seed §3 Requested Outcomes #1 |
| An obligation stating that it is enforced, whose check cannot refuse, is refused when the composition is built. | CR seed §3 Requested Outcomes #2 |
| An obligation not yet enforced can say so, and saying so is different from silence. | CR seed §3 Requested Outcomes #3 |
| An obligation whose check only reports is not admitted as governance. | CR seed §3 Requested Outcomes #4 |
| An obligation enforced elsewhere names where, and the claim is checkable. | CR seed §3 Requested Outcomes #5 |
| How many obligations are unenforced is observable without reading the checks. | CR seed §3 Requested Outcomes #6 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| An obligation whose check cannot refuse anything is not enforced, whatever is declared about it. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A guarantee that counts declarations does not establish that anything is carried. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Fourteen of eighty-seven checks on this platform cannot refuse anything. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Ten of those fourteen state in their own text that enforcement was deferred and would be built later. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Enforcement deferred and never built is indistinguishable, from outside, from enforcement in force. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Two of the fourteen carry their obligation somewhere else, and both were verified to do so. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| A check that only reports leaves the obligation unmet and the admission proceeding. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A check whose only refusal path guards its own inputs cannot refuse its obligation. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A count of checks that cannot refuse is a floor, because a check with an unreachable refusal path is not visible to counting. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| Correcting the present instances does not prevent the next one; nothing refuses a new check that cannot refuse. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| Deciding whether a thing is good is a different act from deciding whether it may be admitted. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| An obligation stating a deferral honestly is more governable than one that is silent about it. | HIGH | CR seed §4 Known Facts — Business Truths #12 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The obligation-to-check guarantee is satisfied by a check that cannot refuse. | The whole of this change. | Establish what the guarantee requires today and confirm capability is not among it. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Fourteen checks cannot refuse anything. | Says the requirement is confirmed rather than anticipated. | Confirm the count, and confirm each one's reason. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Ten of the fourteen declare a deferral in text nothing reads. | Decides whether enforcement status must be declared or can be inferred. | Establish where each deferral is written and what, if anything, consumes it. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| One obligation is declared as governance and its check only reports. | Establishes the second, sharper form of the defect. | Confirm the check reports and never refuses, and confirm what its obligation claims. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Nothing counts unenforced obligations. | Says the defect is invisible rather than tolerated. | Establish whether any published surface answers how much is enforced. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| An obligation may be carried somewhere other than where it is declared. | Decides whether "not enforced here" and "not enforced" are the same statement. | Confirm the two delegated cases and how each is verified. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| An obligation's author knows whether they built its enforcement. | Ten of the fourteen wrote the deferral down in prose. | CR seed §6 Assumptions #1 |
| Whether a check can refuse is decidable from the check itself in most cases and not in all. | Fourteen were found by measuring; a fifteenth had to be read. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Correcting the present instances is not sufficient; the next one must be refused. | Business author | CR seed §7 Constraints #1 |
| An obligation not yet enforced is not deleted for being unenforced. The declaration has value. | Business author | CR seed §7 Constraints #2 |
| Declaring an obligation unenforced does not make it optional. | Business author | CR seed §7 Constraints #3 |
| An obligation enforced elsewhere names where; a bare claim of delegation is not admitted. | Business author | CR seed §7 Constraints #4 |
| The obligation-to-check relation as it stands is kept, and gains a requirement rather than losing one. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| An obligation declared as enforced has a check capable of refusing it. | CR seed §8 Business Invariants #1 |
| An obligation not enforced says so, in a form a mechanism reads. | CR seed §8 Business Invariants #2 |
| An obligation whose check only reports is not admitted as governance. | CR seed §8 Business Invariants #3 |
| An obligation enforced elsewhere names where, and that place is checkable. | CR seed §8 Business Invariants #4 |
| The number of obligations not enforced is observable at any time. | CR seed §8 Business Invariants #5 |
| Deciding admissibility and judging quality are never carried by one obligation. | CR seed §8 Business Invariants #6 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Obligation | Enforced | A check carries it and there is something that check refuses. | CR seed §9 Lifecycle States #1 |
| Obligation | Declared, not enforced | Stated deliberately, with no check carrying it yet, and saying so. | CR seed §9 Lifecycle States #2 |
| Obligation | Enforced elsewhere | Carried somewhere other than where declared, with that place named. | CR seed §9 Lifecycle States #3 |
| Obligation | Believed enforced | Declared as governance, carried by nothing, indistinguishable from enforced. This is the state this change ends. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| An obligation was declared enforced | When an obligation states that its check carries it | The claim is now checkable, and false claims are refused. | CR seed §10 Business Events #1 |
| An obligation was refused for claiming enforcement it does not have | When a composition is built and a check cannot refuse | The defect is caught where it is introduced rather than years later. | CR seed §10 Business Events #2 |
| The unenforced count changed | When an obligation gains or loses enforcement | Coverage is a number rather than an impression. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What an obligation requires | The subdomain that declares it | CR seed §11 Authority Boundaries #1 |
| Whether a check is capable of refusing | The platform | CR seed §11 Authority Boundaries #2 |
| What enforcement statuses exist | The platform | CR seed §11 Authority Boundaries #3 |
| Whether a delegation claim holds | The place the delegation names | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Building the enforcement the ten deferred obligations describe | Each is its own change with its own subject; this one makes the deferral honest and countable. | CR seed §12 Out of Scope #1 |
| Whether any particular obligation should exist | Each subdomain's business. | CR seed §12 Out of Scope #2 |
| Whether a check has ever been observed to refuse | A stronger question than capability, needing a case per check, and a separate change. | CR seed §12 Out of Scope #3 |
| The obligations of domains other than the platform | Each domain's own change. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| conformance | MODIFIED | CR seed §13 Governance Scope #1 |
| governance | ADJACENT | CR seed §13 Governance Scope #2 |
| compiler | ADJACENT | CR seed §13 Governance Scope #3 |
| capability_contracts | ADJACENT | CR seed §13 Governance Scope #4 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| Does an obligation carried by a rule of the pipeline rather than by its own check count as enforced, or as enforced elsewhere? | Decides whether a third status is needed or two suffice. | NO | GOVERNANCE | CR seed §14 Clarification Requests #1 |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| Building a composition in which an obligation declares itself enforced and its check cannot refuse is refused, and the refusal names the obligation. | CR seed §15 Acceptance Criteria #1 |
| An obligation declaring itself not enforced builds, and is counted as not enforced. | CR seed §15 Acceptance Criteria #2 |
| An obligation declaring enforcement elsewhere without naming where is refused. | CR seed §15 Acceptance Criteria #3 |
| Every one of the fourteen present instances carries a status that matches what its check actually does. | CR seed §15 Acceptance Criteria #4 |
| The obligation whose check only reports is no longer admitted as governance. | CR seed §15 Acceptance Criteria #5 |
| The number of obligations not enforced can be read from the built composition without inspecting any check. | CR seed §15 Acceptance Criteria #6 |
| An obligation that is enforced today builds exactly as it does now. | CR seed §15 Acceptance Criteria #7 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Obligation | The declaration that states it | They are the same declaration, whatever their text says. | CR seed §16 Identity and Sameness #1 |
| Check | The obligation it carries | Two checks carrying one obligation are one check stated twice. | CR seed §16 Identity and Sameness #2 |
| Enforcement status | The obligation it is stated on | One obligation states one status. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Obligation | Believed enforced | Declared, not enforced | Stating the deferral its author already wrote in prose. | The unenforced count rises by one. Nothing else follows; nothing was being enforced before. | CR seed §17 Lifecycle Transitions #1 |
| Obligation | Declared, not enforced | Enforced | A check being built that refuses something. | The unenforced count falls by one. | CR seed §17 Lifecycle Transitions #2 |
| Obligation | Believed enforced | Enforced elsewhere | Naming the place that carries it, and that place being checked. | Nothing else follows. The obligation was already carried; it now says where. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Building a composition | An obligation declares itself enforced and its check cannot refuse anything | A check that carries nothing makes its obligation a claim, and a reader counting obligations would conclude the system is governed where it is not. | CR seed §18 Operation Refusals #1 |
| Building a composition | An obligation declares enforcement elsewhere and does not name where | A delegation nobody can follow is indistinguishable from an absence, and absence is not permission. | CR seed §18 Operation Refusals #2 |
| Admitting an obligation as governance | Its check only reports and never refuses | An obligation whose violation produces a report leaves the violation standing, and governance that leaves the violation standing is a description. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| The enforcement the ten deferred obligations describe | A change per subject | Each subject is taken up on its own terms. | CR seed §19 Authority Deferrals #1 |
| Whether a check has ever been observed to refuse | A later change | Capability is established and the stronger question becomes the next one. | CR seed §19 Authority Deferrals #2 |
| The obligations of domains other than the platform | Each domain | That domain raises the change that needs them. | CR seed §19 Authority Deferrals #3 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
