# Stage 4 — Business Model: platform / published rules

**Stage:** 4 — Business Model

**CR:** published_rules

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Execution topology | States what a step must route. | Owning subdomain | S3 placement_decision execution_topology |
| Trace | States what a trace must conform to. | Owning subdomain | S3 placement_decision trace |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Published Identity | An identity a released composition holds. | Sealed in the release. | S2 entities #1 |
| The Routing Rule | The rule that a step routes every outcome it can produce. | Sealed in the composition. | S2 entities #2 |
| The Record Rule | The rule that governs the run's record. | Sealed in the composition. | S2 entities #3 |

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
| Execution topology | states | the routing rule | State the routing rule | S3 authoring_decisions State the routing rule |
| Trace | states | the record rule | State the record rule | S3 authoring_decisions State the record rule |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| State the routing rule | S3 authoring_decisions State the routing rule | CRITICAL | GAP-01 | A successor stating CP-13; V0 returned to v5. |
| State the record rule | S3 authoring_decisions State the record rule | CRITICAL | GAP-02 | A successor naming the second schema; V0 returned to v5. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| execution_topology | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1 | constitution | SATISFIED | S3 dependency_discoveries Governing how contracts are built |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Every composition builds and runs as it does today. | S1 constraints #1 | The business author |
| 2 | No published identity changes what it says, except to be stood down. | S1 constraints #2 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions State the routing rule | State the routing rule | execution_topology | AUTHOR_NEW |
| GAP-02 | S3 authoring_decisions State the record rule | State the record rule | trace | AUTHOR_NEW |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1 states CP-13, and today's check is bound to it. | S3 analysis_findings Q1 | The widened rule has its own identity. | Nothing enforced is relaxed. |
| 2 | CONSTITUTION_TRACE_EXECUTION_V1 names SCHEMA_TRACE_EVENT_V2. | S3 analysis_findings Q2 | The rule names the schema traces conform to. | V1 stays the schema of traces written under it. |
| 3 | Both published rules return to their v5 text and are stood down; the routing rule's v5 check stays registered under V0. | S3 analysis_findings Q3 | Identity is fixed at publication. | Only the stand-down is added to their text. |
| 4 | The unpublished execution topology constitution names the routing rule's successor; code naming either rule names its successor. | S3 analysis_findings Q4 | Nothing in force names a stood-down rule. | Nothing is re-pointed by construction. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| State the routing rule | GAP-01 |
| State the record rule | GAP-02 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Return routes changed in place in contracts and workflows | Each domain's own change. |

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
