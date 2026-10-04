# Stage 4 — Business Model: platform / conformance
**Stage:** 4 — Business Model
**CR:** enforcement_capability
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The subdomain that declares an obligation | States what the platform requires of what it admits, and how a violation is answered. | Declaring — an obligation is its author's account of what must hold. | S1 authority_boundaries #1 |
| The platform | Derives a check from every obligation, runs it, and refuses what it will not admit. | Deciding — it alone decides whether a composition is admissible. | S1 authority_boundaries #2 |
| The place a delegated obligation names | Carries an obligation declared somewhere other than where it is enforced. | Carrying — three such places exist and are confirmed; a fourth names a practice. | S3 analysis_findings #1 |
| A reader of the composition | Counts obligations and concludes from that count what is governed. | Observing — the party the defect misleads. | S1 known_facts #2 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Obligation | Something the platform requires of what it admits. | Eighty-nine are published in the composition. | S2 entities #1 |
| Check | The mechanism that carries one obligation and decides whether it is met. | Not declared. Derived from the obligation when the composition is built. | S2 entities #2 |
| Capability to refuse | Whether there exists anything a check would refuse. | Held nowhere. A property of the check's text and of nothing the platform records. | S2 entities #4 |
| Enforcement status | What an obligation says about whether its check carries it today. | Partly held: every obligation declares how it answers a violation and where it is enforced. Neither says whether the check can produce one. | S2 entities #5 |
| Delegation | An obligation carried somewhere other than where it is declared. | Two forms declared as data and honoured; four stated in prose only. | S2 entities #6 |
| Determination record | The account of what a build decided and on what grounds. | One row per check, per build: whether it passed and how many refusals it produced. | S2 entities #7 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The fourteen checks that cannot refuse | No path within any of them produces a refusal. All fourteen ran in the pinned build and all fourteen passed. | S3 verification_results #2 |
| The ten deferrals written in prose | *"Phase 1 stub — full enforcement in Phase 3"*, in text nothing reads, above obligations that all declare a violation fails the build immediately. | S3 verification_results #3 |
| The check that only reports | The one obligation of eighty-nine declaring that its violation warns; its subject is whether a thing is good. | S3 verification_results #4 |
| The two obligations carried by nothing | The parity obligation, and two rules of the constitution above it that name no carrier. | S3 verification_results #7 |
| The five declared places of enforcement | Three derive a check; two route the obligation away from the build and are honoured. | S3 analysis_findings #1 |
| The derivation step of the build | The single place a check is derived from its obligation, which already refuses a check that does not exist. | S3 dependency_discoveries #4 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| An obligation was declared enforced | An obligation stating that its check carries it | The claim becomes checkable, and a false claim is refused. | S1 business_events #1 |
| An obligation was refused for claiming enforcement it does not have | A composition being built whose check cannot refuse | The defect is caught where it is introduced rather than years later. | S1 business_events #2 |
| The unenforced count changed | An obligation gaining or losing enforcement | Coverage becomes a number rather than an impression. | S1 business_events #3 |
| An obligation was believed enforced | An obligation declaring governance while its check carries nothing | The state this change ends. Seventeen obligations are in it. | S3 saturation #3 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Obligation | declares | Enforcement status | Declaring whether an obligation is enforced. | S3 authoring_decisions #1 |
| Obligation | names | Destination | Naming where a delegated obligation is carried. | S3 authoring_decisions #2 |
| Platform | refuses | Check | Refusing a check that cannot refuse. | S3 authoring_decisions #3 |
| Determination record | counts | Obligation | Counting what is unenforced. | S3 authoring_decisions #4 |
| Platform | withdraws | Obligation | Withdrawing the obligation that judges quality. | S3 authoring_decisions #5 |
| Obligation | is carried by | Derivation | Restating the parity obligation. | S3 authoring_decisions #6 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Refusing a check that cannot refuse | S3 authoring_decisions #3 | CRITICAL | GAP-1 | The mechanism that refuses the next one. Without it the other five are a cleanup. |
| Declaring whether an obligation is enforced | S3 authoring_decisions #1 | CRITICAL | GAP-2 | Fourteen obligations claim a response their check cannot produce, and the claim is the only thing written down. |
| Naming where a delegated obligation is carried | S3 authoring_decisions #2 | MAJOR | GAP-3 | Four delegations are prose; one names a practice rather than a mechanism. |
| Counting what is unenforced | S3 authoring_decisions #4 | MAJOR | GAP-4 | Every row of the pinned build reads passed with zero refusals, including all fourteen. |
| Withdrawing the obligation that judges quality | S3 authoring_decisions #5 | MAJOR | GAP-5 | The one obligation of eighty-nine that warns rather than refuses. |
| Restating the parity obligation | S3 authoring_decisions #6 | MAJOR | GAP-6 | Published, unenforced, superseded by derivation, with a check module nothing reaches. |
| Refusing a check that does not exist | S3 dependency_discoveries #3 | SATISFIED | | Already refuses the build and records the absence, at the point the check is derived. |
| Verifying that a delegated obligation is wired | S3 dependency_discoveries #6 | SATISFIED | | Already confirms an obligation delegated to a runtime outcome is bound to one. |
| Deriving a check from its obligation | S3 dependency_discoveries #4 | SATISFIED | | One place, on every build, already reading the obligation and knowing the check. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| conformance | governance | data read | SATISFIED | S3 dependency_discoveries #2 — the constitution governing obligations already requires the response to a violation. |
| conformance | compiler | capability call | SATISFIED | S3 dependency_discoveries #3 — the refusal of a non-existent check runs at the point capability would be established. |
| conformance | conformance | data read | SATISFIED | S3 dependency_discoveries #7 — the constitution governing checks names the carrier of each of its rules. |
| conformance | execution | data read | SATISFIED | S3 dependency_discoveries #6 — a delegated obligation is already confirmed wired for one destination. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Correcting the present instances is not sufficient; the next one must be refused. | S1 constraints #1 | governance rule |
| 2 | An obligation not yet enforced is not deleted for being unenforced. The declaration has value. | S1 constraints #2 | governance rule |
| 3 | Declaring an obligation unenforced does not make it optional. | S1 constraints #3 | governance rule |
| 4 | An obligation enforced elsewhere names where; a bare claim of delegation is not admitted. | S1 constraints #4 | governance rule |
| 5 | The obligation-to-check relation gains a requirement rather than losing one. | S1 constraints #5 | governance rule |
| 6 | Deciding admissibility and judging quality are never carried by one obligation. | S1 business_invariants #6 | governance rule |
| 7 | The change requires what capability can be decided, and declares what cannot. | S3 analysis_findings #4 | domain knowledge |
| 8 | Carried elsewhere is one status with a destination, not one status per kind of destination. | S3 analysis_findings #1 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #3 | Refusing a check that cannot refuse | conformance | EXTEND |
| GAP-2 | S3 authoring_decisions #1 | Declaring whether an obligation is enforced | conformance | EXTEND |
| GAP-3 | S3 authoring_decisions #2 | Naming where a delegated obligation is carried | conformance | AUTHOR_NEW |
| GAP-4 | S3 authoring_decisions #4 | Counting what is unenforced | conformance | EXTEND |
| GAP-5 | S3 authoring_decisions #5 | Withdrawing the obligation that judges quality | capability_contracts | AUTHOR_NEW |
| GAP-6 | S3 authoring_decisions #6 | Restating the parity obligation | conformance | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Capability is established where the check is derived, not by a pass over the checks. | S3 authoring_decisions #3 | That place already reads the obligation, already knows the check, and already refuses a check that does not exist. A separate pass would run after the build had admitted them. | Rules out a report produced alongside a green build, and fixes the refusal at the same point as the existing one. |
| 2 | Enforcement status is a value of the place of enforcement, not a second field. | S3 authoring_decisions #1 | Two fields that must agree is the defect this change is about. The place is already declared by every obligation and already honoured. | Rules out a separate status field, and puts the deferral where a reader already looks. |
| 3 | An obligation carried elsewhere names its destination, and the destination is confirmed. | S3 analysis_findings #1 | A delegation nobody can follow is indistinguishable from an absence, and absence is not permission. Three of four present delegations name something that exists; the fourth names a practice. | Rules out admitting a bare claim of delegation, and rules out treating a practice as a destination. |
| 4 | The change requires no refusal path at all, and does not require that a refusal path be reachable. | S3 analysis_findings #4 | The first is a property of one check and decidable. The second is a relation between a check and its obligation, established for one case by reading and not decidable in general. | Fixes fourteen as what the change refuses, and leaves the fifteenth to be corrected by declaration rather than caught by rule. |
| 5 | The count is a column of the record every build already writes. | S3 authoring_decisions #4 | The record already names every check that ran; what the count needs is a column, not a surface. | Rules out a new inspection operation as premature, and makes coverage an output of building rather than of asking. |
| 6 | The parity obligation is restated as carried by derivation, not retired. | S3 analysis_findings #2 | What it asserts is true and holds more strongly than when it was checked by comparison. Its check module is dead and is withdrawn with it. | Rules out deleting an obligation whose content holds, and rules out leaving a published obligation that nothing carries. |
| 7 | The obligation that judges quality is withdrawn as an obligation. | S3 authoring_decisions #5 | Its subject is whether a thing is good; the machinery it sits in decides whether a thing is admissible. It has no consumers. | Rules out making its check refuse, which would enforce a preference as a rule. |
| 8 | The constitution governing checks names a carrier for every rule it declares. | S3 analysis_findings #3 | Two of its four rules name no carrier, and a third names an obligation that never runs. A constitution that can name a carrier that does not exist is how the defect stayed invisible. | Rules out completing the change at the level of obligations while the constitution above them remains unchecked. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Refusing a check that cannot refuse | GAP-1 |
| Declaring whether an obligation is enforced | GAP-2 |
| Naming where a delegated obligation is carried | GAP-3 |
| Counting what is unenforced | GAP-4 |
| Withdrawing the obligation that judges quality | GAP-5 |
| Restating the parity obligation | GAP-6 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Building the enforcement the ten deferred obligations describe | Each is its own change with its own subject; this one makes the deferral honest and countable. |
| Deciding whether a refusal path can be reached by its own obligation | Established for one case by reading and not decidable in general; requiring it would demand what cannot be supplied. |
| Establishing that a check has ever been observed to refuse | A stronger question than capability, needing a case per check. |
| The obligations of domains other than the platform | Each domain's own change, once the platform can express what it needs. |
