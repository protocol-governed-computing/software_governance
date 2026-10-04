# Stage 2 — Domain Model Verification: platform / routing closure

**Stage:** 2 — Domain Model Verification
**CR:** routing_closure
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. The step check
and the workflow checks were read for what they compare; execution and the step record were read for
what they do with a step's outcome.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Step | One part of a contract, dispatching one capability and answering its outcomes. | Declared in the contract; not stored. | OBSERVED | S1 business_vocabulary #1 |
| The Step Record | The platform's account of one step that ran. | One line of the run's record, written once and never changed. | OBSERVED | S1 business_vocabulary #6 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Step | The outcomes it answers | The outcomes the step's author listed, each with a continuation. | OBSERVED | S2 belief_verification #1 |
| The Step Record | What it carries | The names of what the step produced, and nothing of its outcome. | OBSERVED | S2 belief_verification #4 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Build a composition | The platform owner | The composition is admitted by every check, or refused. | OBSERVED | S1 lifecycle_states #1 |
| Run a request | Whoever the composition admits | The request ends where its workflow routes it, or is refused. | OBSERVED | S1 business_events #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Build a composition | 1 | Check every step's answers against the outcomes its author listed. | A finding per unanswered listed outcome. | OBSERVED | S2 belief_verification #1 |
| Run a request | 1 | Run each step, and look up what its contract says for the outcome. | A step record. | OBSERVED | S2 belief_verification #3 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The step check compares a step's answers with what its author listed, not with what its capability declares. | VERIFIED | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 states that routing is validated step-locally against the step's result_surface, which the author declares. Its check reads no capability. | S1 system_beliefs #1 |
| No check closes a workflow place against what its contract can end with. | VERIFIED | workflow::CONSTITUTION_WORKFLOW_V0 names five obligations; none compares a place's routes with its contract's outcomes. execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 closes a contract against itself, not the workflow. | S1 system_beliefs #2 |
| Execution carries a contract on past a step outcome nothing answers. | VERIFIED | The runtime's dispatcher reads a step's continuation with a default of carry on. The SoSyM study's case O3 accepted a person after a failed lookup. | S1 system_beliefs #3 |
| The step record names what a step produced and not its outcome. | VERIFIED | trace::CONSTITUTION_TRACE_EXECUTION_V0 governs the record; its step entry requires the step and the names of its results only. | S1 system_beliefs #4 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Checking a step's answers | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Refuses a step that leaves an outcome its author listed without a continuation. | PARTIAL | Does not compare the listed outcomes with what the capability declares. |
| Closing a contract | execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 | Refuses a contract whose possible endings differ from what it declares. | EXACT | Nothing for this purpose; it is the level between step and workflow. |
| Governing workflows | workflow::CONSTITUTION_WORKFLOW_V0 | Names the obligations every workflow is held to. | PARTIAL | Names none that closes a place against its contract. |
| Keeping a superseded thing out of reach | artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 | Refuses a build in which a superseded workflow can be run. | EXACT | Nothing for this purpose; it says which workflows are reachable at all. |
| Governing the run's record | trace::CONSTITUTION_TRACE_EXECUTION_V0 | Governs what each line of the run's record carries. | PARTIAL | Its step entry carries no outcome and no continuation. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A step may answer fewer outcomes than its capability declares. | CRITICAL | The step passes the build and is carried past when the outcome arrives. | OBSERVED | S2 belief_verification #1 |
| A reachable workflow place may leave an outcome without a route. | MAJOR | The gap is sealed and found only when a request reaches it. | OBSERVED | S2 belief_verification #2 |
| Execution carries on past an unanswered step outcome. | CRITICAL | A failed step is treated as a successful one. | OBSERVED | S2 belief_verification #3 |
| The step record carries no outcome. | MAJOR | A decision that went wrong leaves no record. | OBSERVED | S2 belief_verification #4 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The two build checks close each other's gap. | Closing a step's answer adds an ending to its contract, which opens a gap at the workflow unless the workflow answers it too. | OBSERVED | S2 belief_verification #2 |
| The run-time refusal for an unrouted workflow outcome already exists. | The runtime refuses an outcome with neither a route nor an ending, and stays as the safeguard. | OBSERVED | S2 belief_verification #3 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A domain contract reaches platform capabilities it does not hold. | A domain is built against the platform's surface, so the step check needs that surface's declarations. | MINOR | OBSERVED | S2 pps_baseline_fqdns #1 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
