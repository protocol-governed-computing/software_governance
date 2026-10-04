# Stage 4 — Business Model: platform / routing closure

**Stage:** 4 — Business Model

**CR:** routing_closure

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Execution Topology | Refuses a step that answers fewer outcomes than its capability declares. | Owning subdomain | S3 placement_decision execution_topology |
| Workflow | Refuses a reachable place that leaves an outcome of its contract without a route. | Owning subdomain | S3 placement_decision workflow |
| Trace | Records each step's outcome and what happened next. | Owning subdomain | S3 placement_decision trace |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Step | One part of a contract, answering its capability's outcomes. | Declared in the contract. | S2 entities #1 |
| The Step Record | The account of one step that ran. | One line of the run's record. | S2 entities #2 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A request was refused at an unanswered step outcome | A step ends with an outcome nothing answers | The request ends refused, with the reason recorded. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Execution Topology | refuses | a narrowed step | Refuse a narrowed step | S3 authoring_decisions Refuse a narrowed step |
| Workflow | refuses | an unrouted reachable place | Refuse an unrouted reachable place | S3 authoring_decisions Refuse an unrouted reachable place |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Refuse a narrowed step | S3 authoring_decisions Refuse a narrowed step | CRITICAL | GAP-01 | The step check compares with the capability. |
| Refuse an unrouted reachable place | S3 authoring_decisions Refuse an unrouted reachable place | CRITICAL | GAP-02 | A new workflow obligation. |
| Refuse an unanswered step outcome | S3 authoring_decisions Refuse an unanswered step outcome | CRITICAL | GAP-03 | Execution refuses where it defaulted. |
| Record each step's decision | S3 authoring_decisions Record each step's decision | CRITICAL | GAP-04 | The step entry gains two required fields. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| execution_topology | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | amended obligation | SATISFIED | S3 dependency_discoveries Checking a step's answers |
| workflow | workflow::CONSTITUTION_WORKFLOW_V0 | amended constitution | SATISFIED | S3 dependency_discoveries Governing workflows |
| trace | trace::CONSTITUTION_TRACE_EXECUTION_V0 | amended constitution | SATISFIED | S3 dependency_discoveries Governing the run's record |
| workflow | artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 | obligation | SATISFIED | S3 dependency_discoveries Keeping a superseded thing out of reach |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Every composition the domains now hold builds and runs as it does today. | S1 constraints #1 | The business author |
| 2 | The run-time refusal for an unrouted workflow outcome stays. | S1 constraints #2 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Refuse a narrowed step | Refuse a narrowed step | execution_topology | EXTEND |
| GAP-02 | S3 authoring_decisions Refuse an unrouted reachable place | Refuse an unrouted reachable place | workflow | AUTHOR_NEW |
| GAP-03 | S3 authoring_decisions Refuse an unanswered step outcome | Refuse an unanswered step outcome | execution_topology | EXTEND |
| GAP-04 | S3 authoring_decisions Record each step's decision | Record each step's decision | trace | EXTEND |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | A step's listed outcomes hold every outcome its capability declares. | S3 analysis_findings Q1 | A missing answer is never a default. | Read in a domain build from the platform surface it is built against. |
| 2 | A reachable workflow place answers every outcome of what it runs. | S3 analysis_findings Q2 | A refusal at build time comes first. | A superseded workflow is not reachable and is not checked. |
| 3 | Execution refuses a step outcome with no continuation. | S3 analysis_findings Q3 | Execution never carries on past an outcome nothing answers. | Nothing after the refused step runs. |
| 4 | The step record carries the outcome and the continuation. | S3 analysis_findings Q4 | Every step decision is in the record. | Both fields are required. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Refuse a narrowed step | GAP-01 |
| Refuse an unrouted reachable place | GAP-02 |
| Refuse an unanswered step outcome | GAP-03 |
| Record each step's decision | GAP-04 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| NONE IDENTIFIED | |

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
