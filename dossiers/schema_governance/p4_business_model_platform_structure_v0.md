# Stage 4 — Business Model: platform / structure
**Stage:** 4 — Business Model
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The structure subdomain | Decides which kind is described by what, and what makes a description binding. | Declaring | S1 authority_boundaries #1 |
| The subdomain owning a kind | Decides what a declaration of that kind may contain. | Declaring — and where a drift is argued rather than corrected, it escalates here. | S1 authority_boundaries #2 |
| The build | Selects a description by kind and refuses a declaration that does not conform. | Deciding | S2 actors — the process that checks |
| A reader | Concludes from a kind being dispatched that its declarations are governed. | Observing — the party a description that describes nothing misleads. | S3 analysis_findings #3 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Kind | A class of artifact the platform builds. | Fifteen in the composition, carrying 428 artifacts. | S2 entities #1 |
| Description | A statement of what a declaration of one kind may contain. | Eleven describe an artifact kind; four describe runtime data. | S2 entities #2 |
| Dispatch | The table naming which description governs which kind. | One table, ten rows, read by the build. | S2 entities #3 |
| Exemption | A kind recorded as needing no description, with the ground stated. | Does not exist anywhere. | S2 entities #5 |
| Drift | A description that has stopped matching what it describes. | Three instances, at least three separate undated divergences. | S3 analysis_findings #4 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The hundred refusals | What dispatching four descriptions produced. Not one is a defective artifact. | S3 verification_results #3 |
| The five undispatched kinds | Actor, event, intent and the two transport boundary kinds — 106 artifacts checked against nothing. | S2 gaps #1 |
| The description that describes nothing | Dispatched, requiring no field, closing no surface; 33 artifacts read as governed. | S2 gaps #4 |
| The four runtime-data descriptions | Correct, dispatched by nothing, and not this change's subject. | S3 analysis_findings #2 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A declaration was refused | It does not match the description of its kind | The platform caught something wrong, which is the point. | S1 business_events #1 |
| A correct declaration was refused | A description has stopped matching what it describes | The platform turned away correct work with the authority of a rule. | S1 business_events #2 |
| A description stopped matching | The shape of a kind changed and the description did not | Silent today, and stays silent until somebody dispatches it. | S1 business_events #3 |
| A kind was skipped in silence | It is named by the dispatch table nowhere | Indistinguishable from having been checked and passed. This is the state the change ends. | S2 process_steps #3 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Kind | is described by | Description | Describing a kind that has no description. | S3 authoring_decisions #1 |
| Description | matches | Kind | Correcting a description that has drifted. | S3 authoring_decisions #2 |
| Kind | is recorded as | Exemption | Recording that a kind needs no description. | S3 authoring_decisions #3 |
| Platform | reports | Drift | Reporting a description that has stopped matching. | S3 authoring_decisions #4 |
| Description | states | Something | Stating what makes a description one. | S3 authoring_decisions #5 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Reporting a description that has stopped matching | S3 authoring_decisions #4 | CRITICAL | GAP-1 | Without it the next drift is found by a build refusing correct work, which is how all three were found. |
| Correcting a description that has drifted | S3 authoring_decisions #2 | CRITICAL | GAP-2 | Three descriptions, 62 artifacts, none of which changes. |
| Stating what makes a description one | S3 authoring_decisions #5 | MAJOR | GAP-3 | A description requiring no field and closing no surface is dispatched and reads as governance. |
| Describing a kind that has no description | S3 authoring_decisions #1 | MAJOR | GAP-4 | The two transport boundary kinds, 44 artifacts. |
| Recording that a kind needs no description | S3 authoring_decisions #3 | MAJOR | GAP-5 | An exempt kind and a forgotten kind are the same absence today. |
| Refusing a non-conforming declaration | S3 dependency_discoveries #2 | SATISFIED | | Refuses correctly; it is only ever handed ten kinds. |
| Describing runtime data | S3 authoring_decisions #6 | SATISFIED | | Correct, dispatched by nothing, and out of scope. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| structure | artifact | capability call | SATISFIED | S3 dependency_discoveries #2 — the conformance refusal is unchanged and already correct. |
| structure | structure | data read | SATISFIED | S3 dependency_discoveries #1 — the dispatch table exists and is the sole authority. |
| structure | actor | data read | GAP | S3 dependency_discoveries #6 — a drift argued rather than corrected escalates to the kind's own subdomain. |
| structure | transport | data read | GAP | S3 impact_analysis — the two kinds needing a description are that subdomain's. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | No correct declaration is refused. A description that would turn one away is corrected before it is dispatched. | S1 constraints #1 | governance rule |
| 2 | No artifact is edited to satisfy a description that describes a shape the platform has stopped building. | S1 constraints #2 | governance rule |
| 3 | A kind is dispatched only after its description has been measured against every artifact of that kind. | S1 constraints #3 | governance rule |
| 4 | Whether a kind requires a description is decided and recorded, never left to whether one happens to exist. | S1 constraints #4 | governance rule |
| 5 | The 139 currently undescribed artifacts are not treated as defects. | S1 constraints #5 | governance rule |
| 6 | A genuinely invalid declaration is still refused; this change does not weaken what is checked. | S1 constraints #6 | governance rule |
| 7 | A drift is corrected toward the artifacts. Reconsidering a kind's shape is that subdomain's, and is escalated rather than settled by a description. | S3 analysis_findings #1 | domain knowledge |
| 8 | Coverage is not governance. A kind dispatched to a description that describes nothing is not governed by it. | S3 analysis_findings #3 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #4 | Reporting a description that has stopped matching | structure | AUTHOR_NEW |
| GAP-2 | S3 authoring_decisions #2 | Correcting a description that has drifted | structure | EXTEND |
| GAP-3 | S3 authoring_decisions #5 | Stating what makes a description one | structure | EXTEND |
| GAP-4 | S3 authoring_decisions #1 | Describing a kind that has no description | transport | AUTHOR_NEW |
| GAP-5 | S3 authoring_decisions #3 | Recording that a kind needs no description | structure | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | A drift is corrected toward the artifacts. | S3 analysis_findings #1 | The artifacts are what every green build produces and what the runtime executes; a description disagreeing with them is disagreeing with the working system. | Rules out editing an artifact to satisfy a stale description, and confines a disagreement about a kind's shape to that kind's own subdomain. |
| 2 | The change delivers a report, not only corrections. | S3 analysis_findings #4 | Three divergences, none recorded when it happened, all found by a build refusing correct work. Correcting them restores today and does nothing about tomorrow. | Rules out closing this by amending three files. |
| 3 | A description must state something to count as one. | S3 analysis_findings #3 | One is dispatched, requires no field, closes no surface, and reads as governance to any reader counting dispatched kinds. | Rules out measuring this change by how many kinds are dispatched. |
| 4 | Exemption is recorded with its ground, and an absence is not an exemption. | S1 business_invariants #2 | Ruled by the business author. A kind nobody decided about and a kind decided to need nothing are the same absence today. | Rules out total coverage as the goal, and rules out silence as a way of expressing a decision. |
| 5 | The four runtime-data descriptions are out of scope. | S3 analysis_findings #2 | They describe no artifact kind in this composition and are dispatched by nothing for that reason. They were counted in because a directory and a naming convention are all that identify a description's population. | Rules out closing surfaces that govern nothing, and names why the original count was five. |
| 6 | The two transport boundary kinds are described by the subdomain that owns them. | S3 impact_analysis | What a boundary contract may contain is the transport subdomain's to state, and this change decides that it is described rather than what it says. | Rules out this subdomain authoring another's description. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Reporting a description that has stopped matching | GAP-1 |
| Correcting a description that has drifted | GAP-2 |
| Stating what makes a description one | GAP-3 |
| Describing a kind that has no description | GAP-4 |
| Recording that a kind needs no description | GAP-5 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Reconsidering the shape of a kind whose description drifted | A claim about the kind, owned by that kind's subdomain, and escalated rather than settled here. |
| Separating the runtime-data descriptions from the artifact-kind ones | They describe no artifact kind and govern correctly where they are; the shared directory is a naming concern, not a governance one. |
| What a declaration of each kind means | Each kind's own subdomain, asked when its description is written or corrected. |
