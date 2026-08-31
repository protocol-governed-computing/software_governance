# Change Seed — platform / conformance

**Stage:** 0 — Change Seed
**CR:** enforcement_capability
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The conformance subdomain governs the relation between an obligation and the check that carries it:
that every obligation has one, that every check has an obligation, and that the pair can be counted.
Its authority is to decide what makes that relation sound. It decides nothing about what any
particular obligation requires.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-------------------------------------------|
| conformance | MODIFY | The obligation-to-check relation is guaranteed by count and not by capability, so a check that cannot refuse satisfies it. The relation is stated; what it must additionally require has never been. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Obligation | Something the platform requires of what it admits. |
| Check | The mechanism that carries one obligation and decides whether it is met. |
| Refusal | A check deciding an obligation is not met, and the admission not proceeding. |
| Capable of refusing | There exists something a check would refuse. A check no input can fail carries nothing. |
| Enforcement status | What an obligation says about whether its check carries it today. |
| Delegated enforcement | An obligation carried somewhere other than where it is declared, with that place named. |
| Coverage | How much of what is declared is actually carried. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| An obligation states whether it is enforced, and the statement is read by a mechanism rather than by a person. |
| An obligation stating that it is enforced, whose check cannot refuse, is refused when the composition is built. |
| An obligation not yet enforced can say so, and saying so is different from silence. |
| An obligation whose check only reports is not admitted as governance. |
| An obligation enforced elsewhere names where, and the claim is checkable. |
| How many obligations are unenforced is observable without reading the checks. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| An obligation whose check cannot refuse anything is not enforced, whatever is declared about it. | HIGH |
| A guarantee that counts declarations does not establish that anything is carried. | HIGH |
| Fourteen of eighty-seven checks on this platform cannot refuse anything. | HIGH |
| Ten of those fourteen state in their own text that enforcement was deferred and would be built later. | HIGH |
| Enforcement deferred and never built is indistinguishable, from outside, from enforcement in force. | HIGH |
| Two of the fourteen carry their obligation somewhere else, and both were verified to do so. | HIGH |
| A check that only reports leaves the obligation unmet and the admission proceeding. | HIGH |
| A check whose only refusal path guards its own inputs cannot refuse its obligation. | HIGH |
| A count of checks that cannot refuse is a floor, because a check with an unreachable refusal path is not visible to counting. | HIGH |
| Correcting the present instances does not prevent the next one; nothing refuses a new check that cannot refuse. | HIGH |
| Deciding whether a thing is good is a different act from deciding whether it may be admitted. | HIGH |
| An obligation stating a deferral honestly is more governable than one that is silent about it. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The obligation-to-check guarantee is satisfied by a check that cannot refuse. | The whole of this change. | Establish what the guarantee requires today and confirm capability is not among it. |
| Fourteen checks cannot refuse anything. | Says the requirement is confirmed rather than anticipated. | Confirm the count, and confirm each one's reason. |
| Ten of the fourteen declare a deferral in text nothing reads. | Decides whether enforcement status must be declared or can be inferred. | Establish where each deferral is written and what, if anything, consumes it. |
| One obligation is declared as governance and its check only reports. | Establishes the second, sharper form of the defect. | Confirm the check reports and never refuses, and confirm what its obligation claims. |
| Nothing counts unenforced obligations. | Says the defect is invisible rather than tolerated. | Establish whether any published surface answers how much is enforced. |
| An obligation may be carried somewhere other than where it is declared. | Decides whether "not enforced here" and "not enforced" are the same statement. | Confirm the two delegated cases and how each is verified. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| An obligation's author knows whether they built its enforcement. | Ten of the fourteen wrote the deferral down in prose. |
| Whether a check can refuse is decidable from the check itself in most cases and not in all. | Fourteen were found by measuring; a fifteenth had to be read. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Correcting the present instances is not sufficient; the next one must be refused. | Business author |
| An obligation not yet enforced is not deleted for being unenforced. The declaration has value. | Business author |
| Declaring an obligation unenforced does not make it optional. | Business author |
| An obligation enforced elsewhere names where; a bare claim of delegation is not admitted. | Business author |
| The obligation-to-check relation as it stands is kept, and gains a requirement rather than losing one. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| An obligation declared as enforced has a check capable of refusing it. |
| An obligation not enforced says so, in a form a mechanism reads. |
| An obligation whose check only reports is not admitted as governance. |
| An obligation enforced elsewhere names where, and that place is checkable. |
| The number of obligations not enforced is observable at any time. |
| Deciding admissibility and judging quality are never carried by one obligation. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Obligation | Enforced | A check carries it and there is something that check refuses. |
| Obligation | Declared, not enforced | Stated deliberately, with no check carrying it yet, and saying so. |
| Obligation | Enforced elsewhere | Carried somewhere other than where declared, with that place named. |
| Obligation | Believed enforced | Declared as governance, carried by nothing, indistinguishable from enforced. This is the state this change ends. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| An obligation was declared enforced | When an obligation states that its check carries it | The claim is now checkable, and false claims are refused. |
| An obligation was refused for claiming enforcement it does not have | When a composition is built and a check cannot refuse | The defect is caught where it is introduced rather than years later. |
| The unenforced count changed | When an obligation gains or loses enforcement | Coverage is a number rather than an impression. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What an obligation requires | The subdomain that declares it |
| Whether a check is capable of refusing | The platform |
| What enforcement statuses exist | The platform |
| Whether a delegation claim holds | The place the delegation names |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Building the enforcement the ten deferred obligations describe | Each is its own change with its own subject; this one makes the deferral honest and countable. |
| Whether any particular obligation should exist | Each subdomain's business. |
| Whether a check has ever been observed to refuse | A stronger question than capability, needing a case per check, and a separate change. |
| The obligations of domains other than the platform | Each domain's own change. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| conformance | MODIFIED |
| governance | ADJACENT |
| compiler | ADJACENT |
| capability_contracts | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| Does an obligation carried by a rule of the pipeline rather than by its own check count as enforced, or as enforced elsewhere? | Decides whether a third status is needed or two suffice. | NO | GOVERNANCE |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Building a composition in which an obligation declares itself enforced and its check cannot refuse is refused, and the refusal names the obligation. |
| An obligation declaring itself not enforced builds, and is counted as not enforced. |
| An obligation declaring enforcement elsewhere without naming where is refused. |
| Every one of the fourteen present instances carries a status that matches what its check actually does. |
| The obligation whose check only reports is no longer admitted as governance. |
| The number of obligations not enforced can be read from the built composition without inspecting any check. |
| An obligation that is enforced today builds exactly as it does now. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Obligation | The declaration that states it | They are the same declaration, whatever their text says. |
| Check | The obligation it carries | Two checks carrying one obligation are one check stated twice. |
| Enforcement status | The obligation it is stated on | One obligation states one status. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Obligation | Believed enforced | Declared, not enforced | Stating the deferral its author already wrote in prose. | The unenforced count rises by one. Nothing else follows; nothing was being enforced before. |
| Obligation | Declared, not enforced | Enforced | A check being built that refuses something. | The unenforced count falls by one. |
| Obligation | Believed enforced | Enforced elsewhere | Naming the place that carries it, and that place being checked. | Nothing else follows. The obligation was already carried; it now says where. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Building a composition | An obligation declares itself enforced and its check cannot refuse anything | A check that carries nothing makes its obligation a claim, and a reader counting obligations would conclude the system is governed where it is not. |
| Building a composition | An obligation declares enforcement elsewhere and does not name where | A delegation nobody can follow is indistinguishable from an absence, and absence is not permission. |
| Admitting an obligation as governance | Its check only reports and never refuses | An obligation whose violation produces a report leaves the violation standing, and governance that leaves the violation standing is a description. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| The enforcement the ten deferred obligations describe | A change per subject | Each subject is taken up on its own terms. |
| Whether a check has ever been observed to refuse | A later change | Capability is established and the stronger question becomes the next one. |
| The obligations of domains other than the platform | Each domain | That domain raises the change that needs them. |
