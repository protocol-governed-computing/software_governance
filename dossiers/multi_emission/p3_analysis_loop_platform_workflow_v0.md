# Stage 3 — Analysis Loop: platform / workflow
**Stage:** 3 — Analysis Loop
**CR:** multi_emission
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot and the sealed dispatch rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The five gaps are one change and two guards. Naming several moments and stating their order are one thing — a sequence is not a set with an order bolted on. What an unmakeable announcement does, and what a repeated moment does, are the two ways the sequence can be wrong. | Fixes what the change delivers and rules out delivering the sequence without the two rules that keep it honest. | OBSERVED | HIGH | CLOSED | Three gaps trace to a terminal node naming one moment; the other two are conditions on a sequence that does not exist yet. |
| Q2 | The announcement is keyed to the transition, not to the terminal node, and the change must state which of the two it declares several against. A design states the announcement where it belongs — at the node the act ends on — and the composition keys it by the act, the step and the outcome, because a terminal node carries no address. | Settles the one thing the first repository must decide before the design language can be changed. | OBSERVED | HIGH | CLOSED | The sealed dispatch is keyed by act, source step and outcome throughout; every terminal node's announcement is re-keyed on the way in. |
| Q3 | Several announcements per act already exist across outcomes, so the singular is one announcement per transition rather than per act. That makes the change smaller than it reads: the shape a transition carries widens from a name to an ordered sequence of names, and nothing about routing, outcomes or endings moves. | Bounds the change and identifies exactly what widens. | OBSERVED | HIGH | CLOSED | Twelve announcements across nine acts; four acts announce different moments on different endings. |
| Q4 | The order is normative and therefore sealed, not resolved at run time. If the composition sealed a set and the running system chose an order, the account of an act would depend on something nobody declared — which is the defect this change exists to remove, one level down. | Places the order in the sealed composition rather than in the runtime. | OBSERVED | HIGH | CLOSED | The composition already seals what the running system may do rather than leaving it to be resolved. |
| Q5 | An announcement that cannot be made cannot refuse the act, because the act's work is done and its records are immutable once written. The only choice available is loud or silent, and silence is the defect. | Settles the failure behaviour and rules out a two-phase announcement. | OBSERVED | HIGH | CLOSED | A moment's record cannot be altered once written, and no mechanism in the composition undoes a completed act. |
| Q6 | Nothing in the composition would notice several moments arriving. That is a finding about the change's own safety net: it needs a conformance test written with it, and the one existing reader needs tightening in the same change or it will keep passing while checking a third of what happened. | Makes the test part of the delivery rather than an afterthought. | OBSERVED | HIGH | CLOSED | No invariant, inspection operation or boundary declaration counts announcements; the one reader takes the first it finds. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| A terminal node names a single moment, and the running system resolves a single moment for a given act and outcome. | S2 belief_verification #1 | CONFIRMED | Re-read: every terminal node carries at most one announcement, and the sealed dispatch keys twelve of them one per transition. |
| An act exists that completes several declared moments and can announce one. | S2 belief_verification #2 | CONFIRMED | Re-read: one act registers a work, its first edition and its first copy, and three declared moments name exactly those. |
| Nothing governing states what a terminal node announces. | S2 belief_verification #3 | CONFIRMED | Re-read: the workflow constitution does not use the word, the event constitution speaks only of immutability, and neither invariant counts. |
| A subdomain exists whose declared moments are announced by nothing at all. | S2 belief_verification #4 | CONFIRMED | Re-counted: six declared moments, zero announcements, against twelve announcements elsewhere in the composition. |
| Nothing counts the moments an act announces — no rule, no published surface, no boundary declaration. | S2 belief_verification #5 | CONFIRMED | Re-searched: no invariant, no inspection operation, no egress declaration. The domain occurrence counts read store records, not announcements. |
| A reader exists that takes the first announced moment it finds. | S2 belief_verification #6 | CONFIRMED | Re-read: the reference workload's test selects the first announcement and asserts its identity. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| A governing statement of what a terminal node announces | declaration | AUTHOR_NEW | No constitution uses the word and no invariant covers it. |
| The statement that a declared order is normative | declaration | AUTHOR_NEW | Nothing orders announcements, because no act makes two at one ending. |
| The rule that an act announces each moment at most once | declaration | AUTHOR_NEW | Nothing refuses a repeat. |
| The rule that an unmakeable announcement is reported | declaration | AUTHOR_NEW | Nothing declares what happens when an announcement cannot be made. |
| The announcement keyed to a transition | mechanism | EXTEND | Carries one name per transition; must carry an ordered sequence and seal the order. |
| The firing of an announcement when an act ends | mechanism | EXTEND | Resolves one moment per act and outcome; must announce each in the sealed order. |
| The evidence record written per announcement | mechanism | REUSE | Already one entry per announcement; several announcements need more of the same record, not a new kind. |
| The design language that states a terminal node's announcement | mechanism | EXTEND | States one; must state several, in order. |
| The reader that asserts what an act announced | mechanism | EXTEND | Takes the first announcement it finds and would accept extras silently. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| workflow::CONSTITUTION_WORKFLOW_V0 | States what a terminal node announces, for the first time: an ordered sequence of moments, of which today's behaviour is the case of one. | 9 | Nine acts declare an announcement under it. |
| event::CONSTITUTION_EVENT_V0 | Unchanged in what it says about a moment's record; read alongside the new statement about how many an act may announce. | 20 | Twenty moments are declared across four domains. |
| Every act that announces today | Each keeps announcing exactly what it announces now. A sequence of one is the case that already runs. | 12 | Twelve announcements across nine acts. |
| Every act that announces nothing today | Unaffected by the model, and unblocked by it where the silence was a choice. | 6 | Six declared moments in one subdomain wait on this change. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Stating what a terminal node announces | AUTHOR_NEW | Nothing says it today, so there is no rule to widen and the model must be declared. | Widening the implementation alone was rejected: a behaviour the platform performs and no document governs is ungoverned rather than leniently governed, and the next reader would find the plurality by discovering it. | S2 gaps #3 |
| Declaring the order normative | AUTHOR_NEW | Every serialization is ordered incidentally; only a declaration makes the order something a reader may rely on and a change to it a change to the account. | Deriving the order was rejected: the moments of one act sit at one ending with no path between them, so every derivation falls back on an incidental — code order, row order, the order a renderer walks a map. | S2 gaps #2 |
| Announcing an ordered sequence at one ending | EXTEND | The announcement already exists and is keyed to a transition; what widens is the shape it carries. | Splitting the act into several was rejected by the business: it changes the business to suit the platform. Announcing one and dropping the rest was rejected: that is the defect. | S2 gaps #1 |
| Reporting an announcement that cannot be made | AUTHOR_NEW | The act's work is done and its records are immutable, so the only choice is loud or silent. | Refusing the act was rejected: nothing can undo what it did. Announcing nothing unless all can be announced was rejected: the platform has no two-phase anything and a commit fails mid-way exactly as this does. | S2 gaps #4 |
| Refusing a moment announced twice | AUTHOR_NEW | Twice from one act says it occurred twice, and a reader counting occurrences would be right to conclude something happened that did not. | Allowing it and leaving readers to de-duplicate was rejected: it moves a platform guarantee into every reader. | S2 gaps #5 |
| Writing one evidence record per moment | REUSE | The evidence writer already records one entry per announcement; several need more of the same, not a new kind. | A record naming several moments was rejected by the business: it turns a per-moment question into a substring question and changes the evidence shape of a moment an act already had. | S2 architectural_observations #5 |
| Asserting what an act announced | EXTEND | The one existing reader takes the first announcement it finds and would accept extras without noticing. | Leaving it was rejected: it is the single place several would arrive silently, which is this change's own failure mode. | S2 discovery_concerns #2 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | workflow | A terminal node is part of the act, and what an act says it completed is the act's account of itself. The moment being announced belongs to the event subdomain; the announcing does not. | S2 belief_verification #3 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All three are resolved: two by declaring what nothing states, one by widening the shape an existing announcement carries. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the six raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Nine dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Six items re-grounded; all six CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. None rests on inference. |
