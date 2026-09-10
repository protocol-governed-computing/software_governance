# Stage 6 — Governance Intent: platform / conformance
**Stage:** 6 — Governance Intent
**CR:** enforcement_capability
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `conformance` — EXISTING — modified by this CR |
| Authority class | reuse existing — an obligation declares, the platform decides admissibility, a named place carries a delegated obligation; no new actor type |
| Governing constitutions | `governance::CONSTITUTION_INVARIANTS_V0`, `conformance::CONSTITUTION_ASSERT_V0` |

What makes the obligation-to-check relation sound is the conformance subdomain's own question, so the
requirement that a check be capable of refusing belongs here, and so does the vocabulary that lets an
obligation say whether its check carries it. Nothing new stands on its own beyond that vocabulary.

**The seventeen obligations that carry the defect are owned by seven subdomains, and none of them is
this one.** The fourteen whose checks cannot refuse are declared by `authority`, `actor`,
`capability_side_effects`, `execution_topology`, `surface_contract` and `conformance`; the one that
judges quality is declared by `capability_contracts`. Restating any of them is that subdomain's act,
not this dossier's. They are recorded below as artifacts requiring action by their owners, and the
capabilities that would restate them are deferred to those owners. **This dossier delivers the
mechanism and the vocabulary; each owning subdomain declares its own status.**

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Refusing a check that cannot refuse | conformance | OWNED | | S4 gap_register GAP-1 |
| Declaring whether an obligation is enforced | conformance | OWNED | | S4 gap_register GAP-2 |
| Naming where a delegated obligation is carried | conformance | OWNED | | S4 gap_register GAP-3 |
| Counting what is unenforced | conformance | OWNED | | S4 gap_register GAP-4 |
| Restating the parity obligation | conformance | OWNED | conformance::INVARIANT_ASSERT_PARITY_V0 | S4 gap_register GAP-6 |
| Withdrawing the obligation that judges quality | capability_contracts | DEFERRED | capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0 | S4 gap_register GAP-5 |
| Refusing a check that does not exist | compiler | SATISFIED | compiler::INVARIANT_HANDLER_REGISTRY_CLOSED_V0 | S4 capability_graph #7 |
| Verifying that a delegated obligation is wired | execution | SATISFIED | execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | S4 capability_graph #8 |
| Deriving a check from its obligation | conformance | SATISFIED | conformance::CONSTITUTION_ASSERT_V0 | S4 capability_graph #9 |
| Building the enforcement the ten deferred obligations describe | authority | DEFERRED | | S4 authoring_scope deferred #1 |
| Deciding whether a refusal path can be reached by its own obligation | conformance | DEFERRED | | S4 authoring_scope deferred #2 |
| Establishing that a check has ever been observed to refuse | conformance | DEFERRED | | S4 authoring_scope deferred #3 |
| The obligations of domains other than the platform | conformance | DEFERRED | | S4 authoring_scope deferred #4 |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| What every obligation must declare, which the new vocabulary extends | conformance -> governance | governance::CONSTITUTION_INVARIANTS_V0 | GAP | S4 dependency_graph #1 |
| The point at which a check is derived and a non-existent one refused | conformance -> compiler | compiler::INVARIANT_HANDLER_REGISTRY_CLOSED_V0 | SATISFIED | S4 dependency_graph #2 |
| The confirmation that a delegated obligation is bound to the place it names | conformance -> execution | execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | SATISFIED | S4 dependency_graph #4 |
| The withdrawal of the obligation that judges quality | conformance -> capability_contracts | capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0 | GAP | S4 gap_register GAP-5 |
| The status each of the fourteen obligations must declare | conformance -> authority | authority::INVARIANT_NO_AMBIENT_AUTHORITY_V0 | GAP | S4 capability_graph #2 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| governance::CONSTITUTION_INVARIANTS_V0 | Requires every obligation to declare how it answers a violation and where it is enforced. Requires nothing about whether the check can produce a violation. Reached by forty-seven obligations on the platform surface. | EXTEND | S4 gap_register GAP-2 |
| conformance::CONSTITUTION_ASSERT_V0 | Declares four rules governing what a check must be. Two name no carrier at all; a third names the parity obligation, which never runs. | EXTEND | S4 design_decisions #8 |
| conformance::INVARIANT_ASSERT_PARITY_V0 | Published, declares that a violation fails the build immediately, excluded from derivation by name, evaluated by no build, referenced by no artifact. Its check module is on disk and reached by nothing. | REPLACE | S4 gap_register GAP-6 |
| compiler::INVARIANT_HANDLER_REGISTRY_CLOSED_V0 | Refuses the build when an obligation names a check no module answers to, at the point the check is derived. Its own text calls an unregistered check an incomplete enforcement surface. | REUSE | S4 gap_register GAP-1 |
| execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | Confirms an obligation delegated to a runtime outcome is bound to one. Covers that one destination. | REUSE | S4 capability_graph #8 |
| capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0 | The one obligation of eighty-nine declaring that its violation warns. Its check returns warnings and reports passed; its subject is whether a thing is good. Referenced by no artifact. | REVIEW | S4 gap_register GAP-5 |
| authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| authority::INVARIANT_AUTHORITY_REQUIRED_FOR_EXECUTION_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| authority::INVARIANT_AUTHORITY_STATE_WELL_FORMED_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| authority::INVARIANT_NO_AMBIENT_AUTHORITY_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| authority::INVARIANT_NO_RUNTIME_AUTHORIZATION_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| authority::INVARIANT_NO_WORKFLOW_AUTHORIZATION_LOGIC_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| authority::INVARIANT_TRACE_AUTHORITY_BINDING_REQUIRED_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| actor::INVARIANT_IDENTITY_AUTHORITY_SEPARATION_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| execution_topology::INVARIANT_NO_RUNTIME_TOPOLOGY_SYNTHESIS_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| execution_topology::INVARIANT_TOPOLOGY_IMMUTABLE_AFTER_COMPILATION_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal, and its own prose defers enforcement. | REVIEW | S4 capability_graph #2 |
| capability_side_effects::INVARIANT_CS_ISOLATED_EXECUTION_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal and states that the runtime's executor routing carries it. | REVIEW | S4 capability_graph #3 |
| capability_side_effects::INVARIANT_CS_TRACEABLE_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal and states that the runtime execution engine carries it. | REVIEW | S4 capability_graph #3 |
| conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal and states that a phase of the compiler carries it. | REVIEW | S4 capability_graph #3 |
| surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0 | Declares that a violation fails the build immediately; its check has no path producing a refusal and states that code review carries it, which is not a mechanism. | REVIEW | S4 capability_graph #3 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_CLAIM_OF_ENFORCEMENT_IS_CHECKED | An obligation declaring that a violation fails the build has a check with a path that produces one. A check that carries nothing makes its obligation a claim, and a reader counting obligations concludes the system is governed where it is not. | S4 constraint_register #1 |
| A_DEFERRAL_IS_DECLARED_NOT_WRITTEN | An obligation not yet enforced says so in a form a mechanism reads. Ten authors wrote the deferral into prose because there was no field for it, and prose is why the deferral became indistinguishable from enforcement. | S4 constraint_register #2 |
| UNENFORCED_IS_NOT_OPTIONAL | An obligation declared unenforced is a debt the platform has taken on, not a preference. Saying so honestly is what makes it a debt rather than a fiction. | S4 constraint_register #3 |
| A_DELEGATION_NAMES_ITS_PLACE | An obligation carried elsewhere names where, and that place is confirmed. A delegation nobody can follow is indistinguishable from an absence, and absence is not permission. | S4 constraint_register #4 |
| THE_RELATION_ONLY_GAINS | Every obligation carried today is carried afterwards on the same terms. The change adds what the relation must additionally require and removes nothing it already establishes. | S4 constraint_register #5 |
| ADMISSIBILITY_IS_NOT_QUALITY | No obligation carries both the decision whether a thing may be admitted and the judgement whether it is good. An obligation whose violation produces a report leaves the violation standing, and governance that leaves the violation standing is a description. | S4 constraint_register #6 |
| ONLY_WHAT_CAN_BE_DECIDED_IS_REQUIRED | The change requires what is decidable from one check and declares what is not. Requiring that a refusal path be reachable by its own obligation would demand what no author could supply. | S4 constraint_register #7 |
| ELSEWHERE_IS_ONE_STATUS | Carried elsewhere is one status with a destination, not one status per kind of destination. A status per kind of place would multiply as new kinds appear. | S4 constraint_register #8 |
| AN_OBLIGATION_IS_RESTATED_BY_ITS_OWNER | The status of an obligation is declared by the subdomain that owns it. This dossier delivers the mechanism and the vocabulary; seventeen obligations across seven subdomains are named for their owners to act on, and none is written here. | S4 dependency_graph #3 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Refusing a check that cannot refuse | conformance | S4 gap_register GAP-1 |
| Declaring whether an obligation is enforced | conformance | S4 gap_register GAP-2 |
| Naming where a delegated obligation is carried | conformance | S4 gap_register GAP-3 |
| Counting what is unenforced | conformance | S4 gap_register GAP-4 |
| Restating the parity obligation | conformance | S4 gap_register GAP-6 |

---

## Gate 1 — Design Approval
