# Stage 3 — Analysis Loop: platform / routing closure

**Stage:** 3 — Analysis Loop

**CR:** routing_closure

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The four gaps carried from Stage 2 are driven to committed decisions against the pinned composition.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The step check also compares a step's listed outcomes with what its capability declares. A side effect declares its outcomes per operation; a transform declares success, and refusal unless it never refuses. | A narrowed step is refused at build time. | OBSERVED | HIGH | CLOSED | S2 belief_verification #1 |
| Q2 | A new workflow obligation closes every reachable place against what its contract or entrance declares. Reach is traversal from the start; a superseded workflow is not reachable. | An unrouted reachable outcome is refused at build time. | OBSERVED | HIGH | CLOSED | S2 belief_verification #2; S2 pps_baseline_fqdns #4 |
| Q3 | Execution looks up a step's continuation with no default, and refuses where there is none, recording why. | No request carries on past an unanswered outcome. | OBSERVED | HIGH | CLOSED | S2 belief_verification #3 |
| Q4 | The step entry of the run's record gains the outcome and the continuation, both required. An admission's continuation names the route. | Every step decision is in the record. | OBSERVED | HIGH | CLOSED | S2 belief_verification #4; S1 known_facts #5 |
| Q5 | In a domain build the step check reads the declarations of the platform surface the domain is built against. | Platform capabilities are checked in every domain. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #1 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The step check compares a step's answers with what its author listed, not with what its capability declares. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 |
| No check closes a workflow place against what its contract can end with. | S2 belief_verification #2 | CONFIRMED | Resolved in Q2 |
| Execution carries a contract on past a step outcome nothing answers. | S2 belief_verification #3 | CONFIRMED | Resolved in Q3 |
| The step record names what a step produced and not its outcome. | S2 belief_verification #4 | CONFIRMED | Resolved in Q4 |
| A domain contract reaches platform capabilities it does not hold. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q5 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| Checking a step's answers | Obligation | EXTEND | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 gains the capability comparison |
| Governing workflows | Constitution | EXTEND | workflow::CONSTITUTION_WORKFLOW_V0 names the new obligation |
| Governing the run's record | Constitution | EXTEND | trace::CONSTITUTION_TRACE_EXECUTION_V0 governs a step entry that now carries its outcome |
| Keeping a superseded thing out of reach | Obligation | REUSE | artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0, unchanged |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Amended — every contract in every domain is checked against its capabilities | 0 | si.topology.impact impacted_count 0; an obligation is applied, not referenced |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Refuse a narrowed step | EXTEND | The existing step check gains the comparison, so one obligation closes a step. | A second step obligation was rejected: two checks of one step must agree. | S3 analysis_findings Q1 |
| Refuse an unrouted reachable place | AUTHOR_NEW | No workflow obligation compares a place with its contract. | Extending the contract closure was rejected: it governs contracts, not workflows. | S3 analysis_findings Q2 |
| Refuse an unanswered step outcome | EXTEND | Execution's step loop refuses where it defaulted. | Treating the outcome as an ending was rejected: a missing answer is never a default. | S3 analysis_findings Q3 |
| Record each step's decision | EXTEND | The existing step entry gains two required fields. | A separate entry was rejected: one step, one record. | S3 analysis_findings Q4 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | execution_topology | A step's answers are the step's own subdomain's. | S3 analysis_findings Q1 |
| EXTEND | workflow | A workflow's routes are the workflow subdomain's. | S3 analysis_findings Q2 |
| EXTEND | trace | The run's record is the trace subdomain's. | S3 analysis_findings Q4 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | Both CRITICAL gaps resolve in Q1 and Q3 |
| No open analyst questions | SATISFIED | All five findings are CLOSED |
| No dependency expansion in the last pass | SATISFIED | A second pass over the superseded workflows found them already out of reach |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All five items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
