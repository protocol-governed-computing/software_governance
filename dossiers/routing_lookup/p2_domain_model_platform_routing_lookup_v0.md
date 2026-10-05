# Stage 2 — Domain Model Verification: platform / routing is a lookup

**Stage:** 2 — Domain Model Verification
**CR:** routing_lookup
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. The rule that
governs how contracts are built and the rule that a contract's outcomes are all reachable were read
in full, with the check that enforces the second. Every routing answer in the composition was
counted, and execution's handling of each answer was read.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Step | One capability a contract runs, with the outcomes it can produce. | Part of the contract that declares it; sealed in the composition. | OBSERVED | S1 business_vocabulary #1 |
| The Routing | What a step says happens next for each outcome it can produce. | Part of the step; sealed in the composition. | OBSERVED | S1 business_vocabulary #2 |
| The Evaluation Target | A named condition over a step's result, with an outcome for when it holds and one for when it does not. | Part of the contract that declares it; sealed in the composition. | OBSERVED | S1 business_vocabulary #5 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Routing | Its answer | Going on, ending, or the name of an evaluation target. | OBSERVED | S2 belief_verification #4 |
| The Evaluation Target | Its condition | A comparison written over the step's result and the contract's inputs. | OBSERVED | S2 belief_verification #4 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Check a contract's outcomes are all reachable | The platform, when it builds a composition | The build is refused if an outcome is unreachable or uncontracted. | OBSERVED | S1 requested_outcomes #1 |
| Run a contract's steps | The platform, when a contract runs | The contract ends with an outcome. | OBSERVED | S1 requested_outcomes #4 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Check a contract's outcomes are all reachable | 1 | Count as reachable each outcome a step ends on, each outcome the last step goes on with, and both outcomes of every evaluation target. | The outcomes the contract can reach. | OBSERVED | S2 belief_verification #2 |
| Check a contract's outcomes are all reachable | 2 | Refuse an outcome reached and not contracted, or contracted and not reached. | A refusal per outcome. | OBSERVED | S2 belief_verification #2 |
| Run a contract's steps | 1 | Look up the step's outcome in its routing; refuse an outcome it does not list. | The answer. | OBSERVED | S2 belief_verification #3 |
| Run a contract's steps | 2 | End the contract on ending; otherwise run the next step, or end with the outcome after the last. | The contract's outcome. | OBSERVED | S2 belief_verification #3 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The rule governing how contracts are built allows only going on and ending. | NOT_FOUND | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 contradicts itself. Its §4 says routing maps each outcome to exactly two answers, continue or exit, and must not use evaluation logic, conditions or expressions. Its §1 says every outcome is routed to continue, exit or an evaluation target, and its §3 counts evaluation outcomes among a contract's exits. | S1 system_beliefs #1 |
| The rule that a contract's outcomes are all reachable admits evaluation targets, and the compiler follows it. | VERIFIED | execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 counts both outcomes of every evaluation target as reachable. Its check does the same and accepts any routing answer; it is the only compiler check that reads an evaluation block. No schema declares one. | S1 system_beliefs #2 |
| Execution reads an unknown routing answer as going on. | VERIFIED | The runtime's step loop refuses an outcome the routing does not list, ends on exit, and otherwise runs the next step. Nothing in the runtime reads an evaluation block. A contract routing to one ends with the outcome of its last step. | S1 system_beliefs #3 |
| Exactly two contracts route to an evaluation target: the licence cap and the Collatz gate. | VERIFIED | Across every compiled pipeline, 441 routing answers: exit 316, continue 123, evaluate_cap 1, evaluate_conjecture 1. ai_governance::CC_ENFORCE_LICENSE_CAP_V0 routes SUCCESS to evaluate_cap, assigned_count below cap; workload::CC_VERIFY_TERMINATION_V0 routes SUCCESS to evaluate_conjecture, all_terminate true. Both run on live routes, in licence provisioning and the Collatz workflow. | S1 system_beliefs #4 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Governing how contracts are built | execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | Governs every contract's steps and names the invariants that enforce them. | PARTIAL | States two answers in one section and three in two others. |
| Checking a contract's outcomes are reachable | execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 | Refuses an unreachable or uncontracted outcome. | PARTIAL | Admits evaluation targets and any routing answer. |
| Refusing an unlisted outcome | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0 | Requires every outcome a step can produce to be routed. | EXACT | Nothing for this purpose; it is unchanged. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Building a composition admits a routing answer nothing performs. | CRITICAL | Two contracts succeed where their declarations say they fail: the licence cap is never enforced and the Collatz gate cannot fail. | OBSERVED | S2 belief_verification #4 |
| The governing rule contradicts itself about what routing may say. | MAJOR | The invariant followed the sections that admit evaluation targets; aligning only the invariant would leave the governing rule admitting them. | OBSERVED | S2 belief_verification #1 |
| Execution goes on past a routing answer it does not know. | MAJOR | A routing answer the build missed would be read as going on, without a trace of it. | OBSERVED | S2 belief_verification #3 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A check is bound to its invariant by the invariant's identity. | The compiler derives each check's module from the invariant's name and version, so a new version of an invariant has a check of its own. | OBSERVED | S2 belief_verification #2 |
| The governing rule is named by twenty artifacts. | si.artifact.refs reports 21 artifacts that name execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0: the thirteen invariants it lists and the eight surface contracts it governs. One of them is the invariant this change replaces. | OBSERVED | S2 belief_verification #1 |
| The invariant is named only by the governing rule. | si.artifact.refs reports one referrer of execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0. | OBSERVED | S2 belief_verification #2 |
| A decision a condition stated can be made by a capability. | A transform answers with an outcome, and a refusal is routed like any other outcome. | OBSERVED | S2 belief_verification #3 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Replacing the governing rule reaches the twenty artifacts that name it. | Each names it as the rule that governs it or the rule it enforces; each must name the successor. | MAJOR | OBSERVED | S2 architectural_observations #2 |
| Building this change before the two contracts are replaced refuses two compositions. | Both route to an evaluation target today. | MAJOR | OBSERVED | S2 belief_verification #4 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
