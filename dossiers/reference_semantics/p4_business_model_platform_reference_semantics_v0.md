# Stage 4 — Business Model: platform / reference semantics

**Stage:** 4 — Business Model

**CR:** reference_semantics

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Artifact | Declares which parts of a declaration carry no meaning and which name another artifact. | Owning subdomain | S3 placement_decision artifact |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Declaration | What an artifact states about itself. | Sealed in the composition. | S2 entities #1 |
| The Reference | A part of a declaration whose value names another artifact. | Part of the declaration that holds it. | S2 entities #2 |
| The Record of References | Which artifact names which. | Sealed in the composition's evidence. | S2 entities #3 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Artifact | declares | what names another artifact | Declare what names another artifact | S3 authoring_decisions Declare what names another artifact |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Declare what names another artifact | S3 authoring_decisions Declare what names another artifact | CRITICAL | GAP-01 | A new version of the declaration, with the reference groups and the rules. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| artifact | vocabulary::CONSTITUTION_VOCABULARY_V0 | constitution | SATISFIED | S3 dependency_discoveries Governing vocabularies |
| artifact | artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 | invariant | SATISFIED | S3 dependency_discoveries Keeping a stood-down artifact out of reach |
| artifact | artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0 | invariant | SATISFIED | S3 dependency_discoveries Refusing a short-code reference |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Every composition the platform holds builds and runs as it does today, with a fuller record of references. | S1 constraints #1 | The business author |
| 2 | One declaration says what a reference is; nothing else decides it. | S1 constraints #2 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Declare what names another artifact | Declare what names another artifact | artifact | AUTHOR_NEW |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The declaration's new version declares the reference parts, the keyed reference parts, the parts where a short code is refused, and the supersession parts. | S3 analysis_findings Q1 | One place says what a reference is. | No other list of reference parts remains. |
| 2 | The record of references and the short-code check read the declaration; the record only records. | S3 analysis_findings Q2 | One rule, enforced once. | The record refuses nothing about short codes. |
| 3 | A full name outside a reference part, the artifact's own identity and a supersession part is refused. | S3 analysis_findings Q3 | What names another artifact is declared, never inferred. | Every full name in the composition sits in a declared part. |
| 4 | The reach check reads full names from the declaration and still finds a short code anywhere. | S3 analysis_findings Q4 | It must see no less than it does today. | Short codes stay undeclared. |
| 5 | Explanation is exempt only as text, a sentence or a list of sentences. | S3 analysis_findings Q5 | Data under an explanation part carries meaning. | None. |
| 6 | The rules a comparison applies are named entries of their own group. | S3 analysis_findings Q6 | A rule in prose is not sealed. | The comparison applies exactly the named rules. |
| 7 | The declaration is replaced by a new version, and the old one is stood down. | S3 analysis_findings Q7 | Adding to it changes its meaning. | Nothing is re-pointed, because nothing names it. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Declare what names another artifact | GAP-01 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Declare short-code references | The compiler resolves a workflow's places and contracts by short code its own way. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
