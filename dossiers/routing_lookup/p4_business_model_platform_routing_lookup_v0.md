# Stage 4 — Business Model: platform / routing is a lookup

**Stage:** 4 — Business Model

**CR:** routing_lookup

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Execution topology | Governs what routing may say and which outcomes a contract can reach. | Owning subdomain | S3 placement_decision execution_topology |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Step | One capability a contract runs, with the outcomes it can produce. | Part of the contract that declares it. | S2 entities #1 |
| The Routing | What a step says happens next for each outcome. | Part of the step. | S2 entities #2 |
| The Evaluation Target | A named condition over a step's result. | Part of the contract that declares it; refused by this change. | S2 entities #3 |

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
| Execution topology | governs | routing as a lookup | Govern routing as a lookup | S3 authoring_decisions Govern routing as a lookup |
| Execution topology | refuses | routing nothing performs | Refuse routing nothing performs | S3 authoring_decisions Refuse routing nothing performs |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Govern routing as a lookup | S3 authoring_decisions Govern routing as a lookup | MAJOR | GAP-01 | A new version of the governing rule, stating two answers in every section. |
| Refuse routing nothing performs | S3 authoring_decisions Refuse routing nothing performs | CRITICAL | GAP-02 | A new version of the invariant, with a check of its own. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| execution_topology | capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0 | constitution | SATISFIED | S3 dependency_discoveries Governing contracts |
| execution_topology | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | invariant | SATISFIED | S3 dependency_discoveries Requiring every outcome to be routed |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | The refusal takes effect once no composition the platform holds routes to an evaluation target; the two contracts are replaced by their own changes before this one is built. | S1 constraints #1 | The business author |
| 2 | Every other composition builds and runs as it does today. | S1 constraints #2 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Govern routing as a lookup | Govern routing as a lookup | execution_topology | AUTHOR_NEW |
| GAP-02 | S3 authoring_decisions Refuse routing nothing performs | Refuse routing nothing performs | execution_topology | AUTHOR_NEW |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The governing rule's new version states two routing answers in every section and names the new invariant. | S3 analysis_findings Q1 | One rule says what routing may be, once. | No section admits an evaluation target. |
| 2 | The invariant's new version counts exits only from exit and the last step's continue, refuses any other routing answer by step and answer, and refuses an evaluation block. | S3 analysis_findings Q2 | Building refuses routing nothing performs. | A decision is a capability's. |
| 3 | The new invariant has its own check; the old one is stood down with its invariant. | S3 analysis_findings Q3 | A check is bound to its invariant by identity. | None. |
| 4 | Execution refuses a routing answer other than continue or exit and records where. | S3 analysis_findings Q4 | A continuation not declared is refused, never assumed. | None. |
| 5 | Every artifact naming the governing rule is re-pointed to its successor. | S3 analysis_findings Q5 | The replacement accounts for its whole reach. | Each keeps its identity. |
| 6 | This change is built after the two contracts are replaced. | S3 analysis_findings Q6 | No composition is refused by it. | Construction waits on two domain changes. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Govern routing as a lookup | GAP-01 |
| Refuse routing nothing performs | GAP-02 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Replace the licence cap contract | Its own change, in ai_governance. |
| Replace the Collatz gate contract | Its own change, in the conformance workload. |

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
