# Stage 4 — Business Model: platform / workflow
**Stage:** 4 — Business Model
**CR:** multi_emission
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Act | Completes the moments the business declared, and states which it completed. | Announcing — it is the only party that knows what it did. | S1 business_vocabulary #1 |
| Domain | Declares which moments matter and which its acts announce. | Deciding — the moments are its business. | S1 authority_boundaries #1 |
| Platform | Decides whether an act may announce several, and what counts as evidence of one. | Governing — the model is its to state. | S1 authority_boundaries #2 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Moment | Something the business declared matters, recognised when it occurs. | Twenty declared across four domains. | S2 entities #2 |
| Announcement | An act stating that a moment occurred. | Twelve declared, each naming exactly one moment. | S2 entities #3 |
| Terminal node | Where an act ends, and what carries its announcement. | One announcement each, several endings per act. | S2 entities #4 |
| Order | The sequence in which several announcements are made. | Nothing holds one. | S2 entities #5 |
| Evidence record | The observable trace that a moment was announced. | One entry per announcement. | S2 entities #6 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The twelve announcements that exist | Each names one moment, and each keeps behaving exactly as it does — a sequence of one is today's case. | S3 impact_analysis #3 |
| The six moments announced by nothing | Declared by a subdomain that chose silence over announcing one of three. | S3 impact_analysis #4 |
| The one reader of announcements | Takes the first it finds, and must be tightened by this change rather than after it. | S3 authoring_decisions #7 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| An act announced its moments | An act reaches an ending that announces | The business's account of what the act completed is complete and observable. | S1 business_events #1 |
| An announcement could not be made | A moment an act completed cannot be stated | The account is incomplete, and the incompleteness is visible rather than silent. | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Terminal node | announces | Moment | Announcing an ordered sequence at one ending. | S3 authoring_decisions #3 |
| Platform | states | Announcement | Stating what a terminal node announces. | S3 authoring_decisions #1 |
| Design | orders | Announcement | Declaring the order normative. | S3 authoring_decisions #2 |
| Act | reports | Announcement | Reporting an announcement that cannot be made. | S3 authoring_decisions #4 |
| Act | announces once | Moment | Refusing a moment announced twice. | S3 authoring_decisions #5 |
| Announcement | leaves | Evidence record | Writing one evidence record per moment. | S3 authoring_decisions #6 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Stating what a terminal node announces | S3 authoring_decisions #1 | CRITICAL | GAP-1 | Nothing says it today; the model is declared rather than relaxed. |
| Declaring the order normative | S3 authoring_decisions #2 | CRITICAL | GAP-2 | A sequence is not a set with an order bolted on. |
| Announcing an ordered sequence at one ending | S3 authoring_decisions #3 | CRITICAL | GAP-3 | What widens is the shape a transition carries, not routing or endings. |
| Reporting an announcement that cannot be made | S3 authoring_decisions #4 | MAJOR | GAP-4 | The only choice available is loud or silent. |
| Refusing a moment announced twice | S3 authoring_decisions #5 | MINOR | GAP-5 | Twice from one act says it occurred twice. |
| Asserting what an act announced | S3 authoring_decisions #7 | MAJOR | GAP-6 | The one reader takes the first it finds. |
| Writing one evidence record per moment | S3 authoring_decisions #6 | SATISFIED | | The evidence writer is already per-announcement. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| workflow | workflow | capability call | GAP | S3 analysis_findings Q1 — naming several and ordering them are one change. |
| workflow | event | data read | SATISFIED | S3 impact_analysis #2 — a moment's record is unchanged; only how many an act announces. |
| workflow | design | data read | GAP | S3 dependency_discoveries #8 — the design language states one announcement and must state several. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | The stated order is normative; announcing in a different order is announcing something else. | S1 constraints #1 | governance rule |
| 2 | One evidence record per moment announced, whether the act announces one moment or several. | S1 constraints #2 | governance rule |
| 3 | A terminal node names each moment at most once. | S1 constraints #3 | governance rule |
| 4 | No declared moment an act completes is passed over in silence. | S1 constraints #4 | governance rule |
| 5 | An act is never split, and no moment is dropped, to fit the announcement mechanism. | S1 constraints #5 | governance rule |
| 6 | A moment per member of a collection is not admitted by this change. | S1 constraints #6 | governance rule |
| 7 | An act whose announcement cannot be made is not refused; its work is done and a record is immutable once written. | S1 known_facts #5 | domain knowledge |
| 8 | A behaviour the platform performs and no document governs is ungoverned rather than leniently governed. | S1 known_facts #10 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Stating what a terminal node announces | workflow | NEW |
| GAP-2 | S3 authoring_decisions #2 | Declaring the order normative | workflow | NEW |
| GAP-3 | S3 authoring_decisions #3 | Announcing an ordered sequence at one ending | workflow | EXTEND |
| GAP-4 | S3 authoring_decisions #4 | Reporting an announcement that cannot be made | workflow | NEW |
| GAP-5 | S3 authoring_decisions #5 | Refusing a moment announced twice | workflow | NEW |
| GAP-6 | S3 authoring_decisions #7 | Asserting what an act announced | workflow | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | A terminal node announces an ordered sequence of moments, of which today's behaviour is the case of one. | S3 analysis_findings Q3 | Several announcements per act already exist across outcomes, so what widens is the shape one transition carries — not routing, not outcomes, not endings. | Every act that announces today keeps announcing exactly what it does. |
| 2 | A design states the announcement at the ending it belongs to; the composition keys it by the transition. | S3 analysis_findings Q2 | A terminal node carries no address of its own, and declaring several against one spelling while the platform keys them by the other is how a design comes to declare what the composition cannot carry. | Fixes what the design language states and what the compiler seals. |
| 3 | The order is sealed in the composition, not resolved when the act runs. | S3 analysis_findings Q4 | An order the running system chose would make the account of an act depend on something nobody declared — the same defect, one level down. | Rules out ordering by anything discovered at run time. |
| 4 | An announcement that cannot be made is reported, and moments already announced stand. | S3 analysis_findings Q5 | The act's work is done and a record is immutable once written, so the only choice is loud or silent. | Rules out refusing the act, and rules out a two-phase announcement. |
| 5 | A repeated moment is refused when the composition is built, not when the act runs. | S3 authoring_decisions #5 | A design naming one moment twice is wrong before it ever runs, and refusing it early costs a reader nothing. | Rules out de-duplicating in every reader. |
| 6 | The conformance test and the tightened reader are part of this change. | S3 analysis_findings Q6 | Nothing in the composition counts announcements, so the change has no safety net it did not bring. | The change delivers its own evidence. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Stating what a terminal node announces | GAP-1 |
| Declaring the order normative | GAP-2 |
| Announcing an ordered sequence at one ending | GAP-3 |
| Reporting an announcement that cannot be made | GAP-4 |
| Refusing a moment announced twice | GAP-5 |
| Asserting what an act announced | GAP-6 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| A moment announced per member of a collection | A different shape, and not what the confirmed requirement needs. |
| Deciding which moments each act announces | Each domain's business, stated in its own change. |
| Checking that every declared moment is announced by something | A subdomain declared six and wired none; whether that should be refused is its own question. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
