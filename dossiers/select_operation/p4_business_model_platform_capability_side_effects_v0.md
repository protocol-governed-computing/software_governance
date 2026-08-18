# Stage 4 — Business Model: platform / capability_side_effects
**Stage:** 4 — Business Model
**CR:** select_operation
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Platform | Decides what a capability offers, for every domain that reaches it. | Deciding — the offer is its to set. | S1 known_facts #1 |
| Domain | Composes what is offered, and needs what it needs. | Consuming — it may ask, and never decide. | S1 known_facts #1 |
| Change | Adds an operation, and is the thing that knows why. | Recording — the reason exists nowhere else. | S1 known_facts #5 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Capability | The platform's offer of something the business cannot do for itself. | Six exist, and the admitted set is closed. | S2 entities #1 |
| Operation | One thing a capability offers to do, named and declared. | Twenty-one across the six. | S2 entities #2 |
| Offer | The whole set of operations a capability declares. | One per capability. | S2 entities #3 |
| Selection | Answering a question by looking at records rather than the keys they are filed under. | Offered as one operation, added after the capability was first declared. | S2 entities #5 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The two contracts that perform the operation | One asks which records match, the other which copies are held of a book. Both are evidence the operation is general. | S3 impact_analysis #2 |
| The change request that carried the operation in | Holds the reason today, in its inventory of artifacts it said it was extending. | S3 analysis_findings Q4 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A capability's offer changed | An operation is added to or withdrawn from a capability | Every domain that reaches the capability is affected, whether or not it composes the operation. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Change | records | Operation | Recording why the capability offers an operation that reads every record. | S3 authoring_decisions #1 |
| Change | records | Offer | Recording that the change crossed an authority boundary. | S3 authoring_decisions #2 |
| Domain | composes | Operation | The operation itself, unchanged. | S3 authoring_decisions #3 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Recording why the capability offers an operation that reads every record | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The reason exists and is held by the first caller that needed it. |
| Recording that the change crossed an authority boundary | S3 authoring_decisions #2 | CRITICAL | GAP-2 | Without it the record explains the offer and hides how it came to be unexplained. |
| The operation itself | S3 authoring_decisions #3 | SATISFIED | | Declared, reached by two contracts and running. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| capability_side_effects | capability_side_effects | capability call | GAP | S3 analysis_findings Q1 — the two gaps are one absence seen twice. |
| capability_side_effects | catalog | data read | SATISFIED | S3 impact_analysis #2 — the callers are unchanged and stay as they are. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | A capability's offer is decided by the platform, never by a domain that reaches it. | S1 business_invariants #1 | invariant |
| 2 | Every operation a capability offers has a recorded reason for being offered. | S1 business_invariants #2 | invariant |
| 3 | A change to a capability is recorded where the capability is declared. | S1 business_invariants #3 | invariant |
| 4 | The operation stays exactly as it is; this change records it and alters nothing. | S1 constraints #1 | governance rule |
| 5 | The record is made where the capability lives, not where the caller lives. | S1 constraints #2 | governance rule |
| 6 | The change is not re-delivered through the pipeline, because there is nothing left to deliver. | S1 constraints #3 | governance rule |
| 7 | A change that crossed a boundary before the boundary was stated is not a breach of a rule in force. | S1 known_facts #6 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Recording why the capability offers an operation that reads every record | capability_side_effects | NEW |
| GAP-2 | S3 authoring_decisions #2 | Recording that the change crossed an authority boundary | capability_side_effects | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | What is delivered is a record; the operation is untouched. | S3 analysis_findings Q2 | It is declared, reached by two contracts and running against real stores; altering it would break callers to satisfy bookkeeping. | Rules out re-delivery, and rules out withdrawing and re-adding the operation. |
| 2 | The reason is recorded with the capability, not with the caller. | S3 analysis_findings Q3 | Every domain reads the capability and only one reads the catalog's change request. A justification held by an operation's first caller is unfindable by its second. | Rules out leaving the reason where it is. |
| 3 | The record states that the need came from a domain. | S3 analysis_findings Q5 | Recording the operation does not make it the platform's decision retrospectively, and a reader should be able to see where the need came from. | The record is history rather than a claim the platform decided it unprompted. |
| 4 | The boundary crossing is recorded as declared rather than hidden. | S3 analysis_findings Q4 | The change request stated the action and the reason in its own registers; every check passed because none asked whether a domain may amend a platform capability. | The record distinguishes an unenforced rule from a broken one. |
| 5 | Whether an offer should carry its provenance in general is left open. | S3 analysis_findings Q6 | Nothing distinguishes an operation the platform decided from one a caller needed, and this change records one instance rather than answering the general question. | Bounds the change, and names what it deliberately leaves for later. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Recording why the capability offers an operation that reads every record | GAP-1 |
| Recording that the change crossed an authority boundary | GAP-2 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Whether every operation should carry the change that added it | The general question; this change records one instance. |
| What other capabilities offer | Each is its own question. |
| Withdrawing an operation nothing composes | No such operation has been found. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
