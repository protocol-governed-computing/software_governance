# Stage 3 — Analysis Loop: platform / structure
**Stage:** 3 — Analysis Loop
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

The two questions Stage 2 left open, closed against the pinned composition; every belief it verified,
re-grounded rather than carried.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | **A drifted description moves to the artifacts, and the exception is narrow enough to name.** The artifacts are what every green build produces and what the runtime executes; a description that disagrees is disagreeing with the working system. Reconsidering the shape would mean the platform builds something it should not, which is a claim about the kind rather than about its description — and belongs to the subdomain that owns the kind, not here. So each divergence is corrected toward the artifacts, and any divergence somebody wants to argue is escalated to that subdomain rather than settled by a description nobody read. | Settles the correction for all three drifted descriptions and for every future one. | OBSERVED | HIGH | CLOSED | The four shapes were compared against what the platform builds. Each artifact form is produced by the current renderer, admitted by the current compiler and executed by the current runtime. |
| Q2 | **The two populations should be separated, and the separation is the diagnosis rather than tidiness.** Four descriptions were counted as artifact-kind descriptions that failed to close a surface. They describe runtime data — an authority state, a registry, an authenticated state, a trace event — none of which is an artifact kind here. They were miscounted because a directory and a naming convention are all that identify a description's population, and neither says what it describes. | Removes four of the five open surfaces from this change's subject and states why they were ever in it. | OBSERVED | HIGH | CLOSED | No artifact in the composition carries any of those four kinds. The dispatch table names none of them, and could not: there is nothing to dispatch. |
| Q3 | **Dispatch is not the measure; a description that describes is.** One kind is dispatched to a description requiring no field and closing no surface, and thereby reads as governed. Thirty-three artifacts are checked against it and every one passes, because everything passes. **A count of dispatched kinds cannot distinguish that from governance**, which is why the count was the measure until it was measured. | Fixes what the change must deliver: a description that states something, for every kind it dispatches. | OBSERVED | HIGH | CLOSED | The structure description requires no field, names no property as forbidden, and admits any content beside what it does not name. |
| Q4 | **Correcting the descriptions restores today and does nothing about tomorrow.** The hundred refusals span at least three separate divergences and none was recorded when it happened. Every one was found by dispatching a description and reading what it refused, which is a method that only works on a description nobody is relying on. | Fixes that the change must deliver a report, not only corrections. Without it the next drift is found the same way, by a build refusing correct work. | OBSERVED | HIGH | CLOSED | No check compares a description against the artifacts of its kind. Three divergences of three different shapes, none dated, none reported. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| The dispatch table is the sole authority for which kind is described by what. | S2 belief_verification #1 | CONFIRMED | One table, read by the build, and nothing selects a description another way. |
| The four unnamed descriptions rotted at a namespace change and not before. | S2 belief_verification #2 | OVERTURNED | Sixty-two mismatches are consistent with that change; thirty-eight are not. Staleness is continuous drift across at least three undated divergences. |
| Every one of the hundred refusals is the description being wrong. | S2 belief_verification #3 | CONFIRMED | Re-compared against what the platform builds. No artifact form among them is anything but current. |
| Nothing reports a description that has stopped matching. | S2 belief_verification #4 | CONFIRMED | No check compares a description against the artifacts of its kind. |
| Not every artifact kind requires a description. | S2 belief_verification #5 | CONFIRMED | Ruled by the business author, and nothing in the composition can record the ruling. |
| Closing an open surface refuses nothing that is currently built. | S2 belief_verification #6 | OVERTURNED | The five were two populations. One is an artifact-kind description that describes nothing; four describe runtime data and are not this change's subject. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The dispatch table | governance | EXTEND | Names ten kinds and cannot say a kind is exempt. Gains the kinds that gain a description, and a way to record an exemption. |
| The refusal of a non-conforming declaration | governance | REUSE | Refuses correctly; it is only ever handed ten kinds. Unchanged. |
| The description of each artifact kind | data | EXTEND | Thirteen exist, three have drifted, one describes nothing, two kinds have none. |
| The report of a description that has stopped matching | governance | AUTHOR_NEW | Nothing performs it. Every divergence here was found by a build refusing correct work. |
| The constitution governing structural declarations | governance | EXTEND | Says nothing about whether a kind must be described, nor what makes a description one. |
| What a declaration of each kind means | governance | INVESTIGATE | Each kind's own subdomain, and where a drift is argued rather than corrected it escalates there. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| structure::STRUCTURE_SCHEMA_DISPATCH_V0 | Every artifact in every domain, on every build. It decides what is checked. | 1 | Reported by the composition; read by the build's schema analysis. |
| artifact::INVARIANT_SCHEMA_CONFORMANCE_V0 | Every declaration of every dispatched kind. Unchanged in what it does. | 0 | Reported by the composition. |
| structure::CONSTITUTION_STRUCTURE_V0 | The structure subdomain's own rules; gains what a description must state and whether a kind must have one. | 13 | Reported by the composition. |
| The three drifted descriptions | 62 artifacts of three kinds, none of which changes. | — | Actor, event and intent declarations across five domains. |
| The two absent descriptions | 44 transport boundary artifacts, none of which changes. | — | Ingress and egress contracts in the inspection surface. |
| The description that describes nothing | 33 structure declarations, currently dispatched and unchecked in substance. | — | Every domain carries at least one. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|-----------|----------|-----------|---------------------|----------------|
| Describing a kind that has no description | AUTHOR_NEW | Two kinds carrying forty-four artifacts are described by nothing that could be dispatched. | Leaving them undescribed was considered and rejected: a boundary contract's surface is the one a caller depends on. | analysis_findings #3 |
| Correcting a description that has drifted | EXTEND | The artifacts are the working system; a description disagreeing with them is wrong about them. | Reconsidering the artifact shape was considered and confined: it is a claim about the kind, owned by that kind's subdomain, and escalated rather than settled here. | analysis_findings #1 |
| Recording that a kind needs no description | AUTHOR_NEW | Exemption is admissible with a stated ground, and there is nowhere to state one. An exempt kind and a forgotten kind are the same absence today. | Requiring every kind to be described was ruled against by the business author. | analysis_findings #3 |
| Reporting a description that has stopped matching | AUTHOR_NEW | Every divergence here was found by a build refusing correct work, which only works on a description nobody relies on. | Correcting the three and stopping was considered and rejected: it restores today and does nothing about tomorrow. | analysis_findings #4 |
| Stating what makes a description one | EXTEND | A description requiring no field and closing no surface is dispatched and reads as governance. Nothing says that is not a description. | Measuring governance by the count of dispatched kinds was what allowed it. | analysis_findings #3 |
| Describing runtime data | REUSE | Four descriptions describe runtime data, not declarations. They are correct, dispatched by nothing, and not this change's subject. | Counting them as artifact-kind descriptions was the error Stage 2 corrected. | analysis_findings #2 |

---

## 6. Placement Decision

<!-- register:placement_decision -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | structure | Which kind is described by what, and what makes a description binding, is what this subdomain governs. What a declaration of a kind *means* belongs to the kind's own subdomain and is escalated, not decided here. | S1 governance_scope #1 |

---

## 7. Discovery Saturation

<!-- register:saturation -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| Every question Stage 2 left open is closed. | SATISFIED | A drift is corrected toward the artifacts, with escalation named for the exception; the two populations are separated. |
| Every belief Stage 2 verified was re-grounded. | SATISFIED | Six re-grounded, two overturned — the staleness is continuous rather than one event, and the five open surfaces were two populations. |
| The subject is bounded. | SATISFIED | Eleven artifact-kind descriptions, of which three have drifted and one describes nothing; two kinds have none; four runtime-data descriptions are out. |
| What the change must deliver is determined. | SATISFIED | Corrections, two descriptions, a way to record an exemption, a statement of what makes a description one, and a report that finds the next drift before a build does. |
| Nothing further is needed to state what the change does. | SATISFIED | Every capability rests on the dispatch table, the conformance refusal or the structure constitution, all of which exist. |
