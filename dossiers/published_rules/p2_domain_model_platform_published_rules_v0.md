# Stage 2 — Domain Model Verification: platform / published rules

**Stage:** 2 — Domain Model Verification
**CR:** published_rules
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition and against v5
as `pgc_release/snapshot` and each repository's `v5` tag hold it. Both rules were read as published
and as they stand, with the routing rule's check at both points, and the workspace was searched for
every artifact and every line of code that names either rule.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Published Identity | An identity a released composition holds. | Sealed in the release; not stored by this change. | OBSERVED | S1 business_vocabulary #2 |
| The Routing Rule | The rule that a step routes every outcome it can produce. | Sealed in the composition. | OBSERVED | S1 business_vocabulary #5 |
| The Record Rule | The rule that governs the run's record. | Sealed in the composition. | OBSERVED | S1 business_vocabulary #6 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Routing Rule | What a step's outcomes are compared with | In v5, the outcomes the step's author lists; now also every outcome the capability declares. | OBSERVED | S2 belief_verification #1 |
| The Record Rule | The schema it names | In v5, the first trace schema; now the second. | OBSERVED | S2 belief_verification #2 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Check a step's routing | The platform, when it builds a composition | The build is refused if a step leaves an outcome unrouted. | OBSERVED | S1 requested_outcomes #1 |
| Check a run's record | The regression, after the runs | Every trace line is validated against the schema the record rule names. | OBSERVED | S1 requested_outcomes #2 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Check a step's routing | 1 | Compare the step's routes with the outcomes it lists, and the list with what its capability declares. | A refusal per unrouted or unlisted outcome. | OBSERVED | S2 belief_verification #1 |
| Check a run's record | 1 | Validate every line of every trace against the second trace schema. | A refusal per line that does not conform. | OBSERVED | S2 belief_verification #2 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The routing rule's text and check require more than they did in v5. | VERIFIED | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 as v5 published it requires a step's on_result to route every code in its own result_surface, and says full enforcement is later work. As it stands, it also requires the result_surface to hold every outcome the capability declares (3d CP-13), and its check gained that comparison: 47 lines since the v5 tag, reading the capability from the platform surface a domain is built against. | S1 system_beliefs #1 |
| The record rule names a different schema than it did in v5. | VERIFIED | trace::CONSTITUTION_TRACE_EXECUTION_V0 as v5 published it requires every trace line to conform to SCHEMA_TRACE_EVENT_V1 and declares event types there. As it stands, it names SCHEMA_TRACE_EVENT_V2 and says V1 stays the schema of traces written under it. | S1 system_beliefs #2 |
| Few artifacts name either rule. | VERIFIED | si.artifact.refs reports the routing rule named by execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0, stood down, and its successor V1, added this cycle and unpublished; the record rule is named by none. In code, the compiler registers the routing rule's check by identity, author_invariant_scope.py lists its scope, test_routing_closure.py imports its check, and trace_schema_conformance.py names the record rule in its docstring and reads SCHEMA_TRACE_EVENT_V2 by path. Prose elsewhere mentions the record rule and names nothing. | S1 system_beliefs #3 |
| No other published rule changed what it requires this cycle. | VERIFIED | The SU-11 sweep compared every identity v5 published with the working composition by declaration, by text and by realization. Of the governance surface, these two rules, CONSTITUTION_WORKFLOW_V0 and the stood-down CONSTITUTION_EXECUTION_TOPOLOGY_V0 changed; the last two have been returned to their v5 text. The reference checks were rewritten under rules whose text did not change. | S1 system_beliefs #4 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Requiring every outcome routed | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Refuses an unrouted or unlisted outcome. | MISMATCH | Says more than v5 published under the published identity. |
| Governing the run's record | trace::CONSTITUTION_TRACE_EXECUTION_V0 | Names the schema every trace line conforms to. | MISMATCH | Names a schema v5 did not, under the published identity. |
| Governing how contracts are built | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1 | Names the routing rule among its invariants. | PARTIAL | Names the routing rule's published identity. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Two published identities say what they did not say when published. | CRITICAL | A composition v5 admitted can be refused, and a trace v5 wrote fails, under the rule v5 named. | OBSERVED | S2 belief_verification #1; S2 belief_verification #2 |
| Nothing states the widened routing rule under its own identity. | MAJOR | The check that enforces it has no rule of its own to be bound to. | OBSERVED | S2 belief_verification #1 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A check is bound to its invariant by identity. | The compiler derives each check's module from the invariant's name and version. | OBSERVED | S2 belief_verification #3 |
| An unpublished identity may change. | CONSTITUTION_EXECUTION_TOPOLOGY_V1 was added this cycle and can name the routing rule's successor directly. | OBSERVED | S2 belief_verification #3 |
| The trace check reads the schema, not the rule. | trace_schema_conformance.py validates against SCHEMA_TRACE_EVENT_V2 by path. | OBSERVED | S2 belief_verification #3 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Returning the routing rule's check to its v5 form changes nothing that runs. | A stood-down invariant derives no assertion, so the v5 check is kept for the record and never runs. | MINOR | OBSERVED | S2 architectural_observations #1 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
