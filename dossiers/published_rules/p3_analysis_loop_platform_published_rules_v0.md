# Stage 3 — Analysis Loop: platform / published rules

**Stage:** 3 — Analysis Loop

**CR:** published_rules

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The two gaps and one concern carried from Stage 2 are driven to committed decisions against the
pinned composition and v5.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The routing rule gains a successor, INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1, stating what is enforced today: a step routes every outcome it lists, and lists every outcome its capability declares (3d CP-13). Its check is today's, bound to the new identity. | The widened rule has an identity that says so. | OBSERVED | HIGH | CLOSED | S2 gaps #2; S2 architectural_observations #1 |
| Q2 | The record rule gains a successor, CONSTITUTION_TRACE_EXECUTION_V1, naming SCHEMA_TRACE_EVENT_V2, and saying V1 stays the schema of traces written under it. | The rule a trace conforms to says which schema it is. | OBSERVED | HIGH | CLOSED | S2 gaps #1; S2 belief_verification #2 |
| Q3 | Each published rule is returned to its v5 text and stood down. The routing rule's check returns to its v5 form and stays registered under the v5 identity, which derives no assertion once stood down. | v5 means what it published, and the record says what was enforced under it. | OBSERVED | HIGH | CLOSED | S2 gaps #1; S2 discovery_concerns #1 |
| Q4 | CONSTITUTION_EXECUTION_TOPOLOGY_V1, unpublished, names the routing rule's successor. Nothing names the record rule, so nothing else is re-pointed. The compiler's registry and scope table, the routing-closure test and the trace check's docstring name the successors. | Nothing in force names a stood-down rule. | OBSERVED | HIGH | CLOSED | S2 belief_verification #3 |
| Q5 | No other published rule of the governance surface is in scope. The other changes the sweep found were returned to v5, or are realizations of unchanged rules. | The change is the whole of it. | OBSERVED | HIGH | CLOSED | S2 belief_verification #4 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The routing rule's text and check require more than they did in v5. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 and Q3 |
| The record rule names a different schema than it did in v5. | S2 belief_verification #2 | CONFIRMED | Resolved in Q2 and Q3 |
| Few artifacts name either rule. | S2 belief_verification #3 | CONFIRMED | Resolved in Q4 |
| No other published rule changed what it requires this cycle. | S2 belief_verification #4 | CONFIRMED | Resolved in Q5 |
| Returning the routing rule's check to its v5 form changes nothing that runs. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q3 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| The routing rule | Invariant | AUTHOR_NEW | INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1; V0 returned to v5 and stood down |
| The record rule | Constitution | AUTHOR_NEW | CONSTITUTION_TRACE_EXECUTION_V1; V0 returned to v5 and stood down |
| Governing how contracts are built | Constitution | EXISTING | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1, unpublished, names the successor |
| The second trace schema | Schema | REUSE | SCHEMA_TRACE_EVENT_V2, unchanged |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Stood down; named by the stood-down V0 constitution and the unpublished V1 | 2 | si.artifact.refs |
| trace::CONSTITUTION_TRACE_EXECUTION_V0 | Stood down; named by nothing | 0 | si.artifact.refs |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| State the routing rule | AUTHOR_NEW | A successor that says what is enforced today. | Keeping the widened text under V0 was rejected: identity is fixed at publication. | S3 analysis_findings Q1 |
| State the record rule | AUTHOR_NEW | A successor that names the schema traces conform to. | Naming both schemas under V0 was rejected for the same reason. | S3 analysis_findings Q2 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | execution_topology | What a step must route is execution topology's. | S3 analysis_findings Q1 |
| EXTEND | trace | What a trace must conform to is trace's. | S3 analysis_findings Q2 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The CRITICAL gap resolves in Q1, Q2 and Q3 |
| No open analyst questions | SATISFIED | All five findings are CLOSED |
| No dependency expansion in the last pass | SATISFIED | The sweep found no further published rule |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Every item CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
