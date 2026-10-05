# Stage 3 — Analysis Loop: platform / routing is a lookup

**Stage:** 3 — Analysis Loop

**CR:** routing_lookup

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The three gaps and two concerns carried from Stage 2 are driven to committed decisions against the
pinned composition. The governing rule was found to contradict itself, so it is replaced with the
invariant.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The governing rule is replaced by a version that says routing has two answers in every section: each outcome is routed to continue or exit, and a contract's exits are the outcomes its steps exit on and the outcomes its last step continues with. It names the new invariant in place of the old. | One rule says what routing may be, and says it once. | OBSERVED | HIGH | CLOSED | S2 gaps #2; S2 belief_verification #1 |
| Q2 | The invariant is replaced by a version that counts as reachable only the outcomes a step exits on and the outcomes the last step continues with. It refuses a routing answer other than continue or exit, naming the step and the answer, and refuses a contract that declares an evaluation block. | Building a composition refuses routing nothing performs. | OBSERVED | HIGH | CLOSED | S2 gaps #1; S2 belief_verification #2 |
| Q3 | The new invariant has a check of its own, bound by its identity. The old check stays with the old invariant, which is stood down and derives no assertion. | Each version is enforced by its own check. | OBSERVED | HIGH | CLOSED | S2 architectural_observations #1 |
| Q4 | Execution refuses a routing answer other than continue or exit, records where, and ends the workflow refused, as it does for an outcome the routing does not list. | A routing answer the build missed cannot be read as going on. | OBSERVED | HIGH | CLOSED | S2 gaps #3 |
| Q5 | The twenty artifacts that name the governing rule, other than the invariant this change replaces, are re-pointed to its successor. Each names it in a part declared a reference, so each keeps its identity. | The replacement accounts for its whole reach. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #1; S2 architectural_observations #2 |
| Q6 | This change is built after the licence cap and Collatz gate contracts are replaced by their own changes, which move each decision into a capability. | No composition the platform holds is refused by it. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #2; S1 constraints #1 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The rule governing how contracts are built allows only going on and ending. | S2 belief_verification #1 | OVERTURNED | Its §1 and §3 admit evaluation targets; resolved in Q1 |
| The rule that a contract's outcomes are all reachable admits evaluation targets, and the compiler follows it. | S2 belief_verification #2 | CONFIRMED | Resolved in Q2 and Q3 |
| Execution reads an unknown routing answer as going on. | S2 belief_verification #3 | CONFIRMED | Resolved in Q4 |
| Exactly two contracts route to an evaluation target: the licence cap and the Collatz gate. | S2 belief_verification #4 | CONFIRMED | Resolved in Q6 |
| Replacing the governing rule reaches the twenty artifacts that name it. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q5 |
| Building this change before the two contracts are replaced refuses two compositions. | S2 discovery_concerns #2 | CONFIRMED | Resolved in Q6 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| The rule governing how contracts are built | Constitution | AUTHOR_NEW | Replaced by a new version; execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 is stood down |
| The rule that a contract's outcomes are all reachable | Invariant | AUTHOR_NEW | Replaced by a new version; execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 is stood down |
| Requiring every outcome to be routed | Invariant | REUSE | execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0; its obligation is unchanged, and it is re-pointed |
| Governing contracts | Constitution | REUSE | capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0 governs the new rule, unchanged |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0 | Stood down; every artifact naming it is re-pointed or replaced | 21 | si.artifact.refs ref_count 21 |
| execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0 | Stood down; named only by the rule this change also replaces | 1 | si.artifact.refs ref_count 1 |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Govern routing as a lookup | AUTHOR_NEW | A new version of the governing rule that states two answers in every section. | Aligning only the invariant was rejected: the governing rule would still admit evaluation targets. | S3 analysis_findings Q1 |
| Refuse routing nothing performs | AUTHOR_NEW | A new version of the invariant, with a check of its own. | Running conditions at execution was rejected: the governing rule forbids an expression in routing. | S3 analysis_findings Q2 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | execution_topology | What makes a contract's steps sound is the execution topology subdomain's. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The CRITICAL gap resolves in Q2 and Q6 |
| No open analyst questions | SATISFIED | All six findings are CLOSED |
| No dependency expansion in the last pass | SATISFIED | A second search for rules that read routing found none beyond the three |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | The one OVERTURNED item resolves in Q1 |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
