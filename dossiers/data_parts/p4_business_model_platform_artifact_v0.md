# Stage 4 — Business Model: platform / artifact
**Stage:** 4 — Business Model
**CR:** data_parts
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Platform | Declares how every part of a declaration is read, and reads every declaration that way. | Governing — how a declaration is read is its to state. | S1 authority_boundaries #1 |
| Domain | States what its vectors hand a transform and expect back. | Deciding — what a vector states is its business. | S1 authority_boundaries #2 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Declaration | What an artifact states, read the same way by every reader. | One per artifact, in its own source. | S2 entities #1 |
| Part | A named place in a declaration, read the way the platform declares. | Declared once, by name, for every kind. | S2 entities #2 |
| Data part | A part whose contents are values, never read for references. | Nothing declares one. | S2 entities #3 |
| Test vector | A statement of what a transform is handed and what it must return. | Twenty-nine in the composition. | S2 entities #4 |
| Case | One stated input and its expected result, within a test vector. | Held in the vector's cases. | S2 entities #5 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The twenty-nine vectors that exist | Each builds today and builds the same afterwards: none of them states a full name in its cases. | S3 impact_analysis #2 |
| The one walk that finds references | Passes over history parts already, and passes over data parts the same way. | S3 dependency_discoveries #2 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A declaration was read | The platform builds a composition | Every reference in it was found and resolved, and every value was left as a value. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Platform | declares | Data part | Declaring a part whose contents are values. | S3 authoring_decisions #1 |
| Platform | passes over | Data part | Passing over a data part when finding references. | S3 authoring_decisions #2 |
| Platform | reads | Declaration | Reading the new version wherever the vocabulary is read. | S3 authoring_decisions #3 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Declaring a part whose contents are values | S3 authoring_decisions #1 | CRITICAL | GAP-1 | A data part is declared by name, as a reference part is. |
| Passing over a data part when finding references | S3 authoring_decisions #2 | CRITICAL | GAP-2 | One walk decides what a reference is for every reader. |
| Reading the new version wherever the vocabulary is read | S3 authoring_decisions #3 | MAJOR | GAP-3 | A reader of the old version reads a declaration that no longer stands. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| artifact | vocabulary | data read | SATISFIED | S3 dependency_discoveries #4 — a new group is stated the way every group is. |
| conformance | artifact | data read | GAP | S3 analysis_findings Q2 — a vector's cases are read by the declaration that does not yet say they are data. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | A data part is declared, never inferred. | S1 constraints #1 | governance rule |
| 2 | A part outside a vector's cases is read exactly as it is today. | S1 constraints #2 | governance rule |
| 3 | An unrecognised name outside a data part is still refused. | S1 constraints #3 | governance rule |
| 4 | A part's name means the same thing in every kind. | S3 analysis_findings Q3 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Declaring a part whose contents are values | artifact | EXTEND |
| GAP-2 | S3 authoring_decisions #2 | Passing over a data part when finding references | artifact | EXTEND |
| GAP-3 | S3 authoring_decisions #3 | Reading the new version wherever the vocabulary is read | artifact | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Data is a group of the vocabulary that declares how a declaration is read, beside references and history. | S3 analysis_findings Q1 | The vocabulary already declares a group of parts the walk passes over, so a data part needs a group and no new mechanism. | Rules out exempting vectors by kind. |
| 2 | The data part is the vector's cases, and nothing else. | S3 analysis_findings Q2 | The cases hold every value a case states, and the transform a vector tests sits beside them. | Leaves the vector's target a reference. |
| 3 | The vocabulary is versioned, and every reader names the new version. | S3 analysis_findings Q4 | Adding a group changes what the vocabulary declares. | The old version stands down. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Declaring a part whose contents are values | GAP-1 |
| Passing over a data part when finding references | GAP-2 |
| Reading the new version wherever the vocabulary is read | GAP-3 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Declaring any other part data | Nothing needs it today; each is declared when it is needed. |
| What any vector states | Each domain's business. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
