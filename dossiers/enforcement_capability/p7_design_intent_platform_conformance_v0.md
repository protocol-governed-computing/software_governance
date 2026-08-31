# Stage 7 — Design Intent: platform / conformance
**Stage:** 7 — Design Intent
**CR:** enforcement_capability
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Where enforcement status is declared | Every obligation already declares where it is enforced, and two of the five values already route it away from the build. | Status is a value of `core.enforcement_stage`, governed by a new vocabulary. No second field is added, because two fields that must agree is the defect this change is about. The vocabulary extends nothing: it reserves the `enforcement_stage` category, which no vocabulary held before, and an obligation's constitution is not a vocabulary that could reserve one. | S6 boundary_rules A_DEFERRAL_IS_DECLARED_NOT_WRITTEN |
| How a destination is stated | Three delegations name a mechanism and one names a practice, all in prose nothing reads. | An obligation whose stage routes it elsewhere declares `core.enforced_by`, naming the mechanism that carries it. A stage that routes elsewhere without it is refused. | S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE |
| Where capability is established | The build already refuses an obligation naming a check no module answers to, at the point the check is derived. | Capability is established at the same point, from the same two things: the derived check's module and the obligation's declared stage. An obligation declaring itself enforced whose module has no refusal-producing path is refused there. | S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED |
| What capability means, operationally | A check with no refusal path is decidable from the check alone; whether a refusal path is reachable by its own obligation is not decidable in general. | The rule is *has a path that produces a refusal*. It is not *has a path this obligation can reach*. The fifteenth instance is corrected by declaration, not caught by rule. | S6 boundary_rules ONLY_WHAT_CAN_BE_DECIDED_IS_REQUIRED |
| Where the count lives | The build already writes one row per check, naming whether it passed and how many refusals it produced. | The row gains the obligation's declared stage, so the count of what is unenforced is read from the record every build already writes. No inspection operation is added. | S6 boundary_rules THE_RELATION_ONLY_GAINS |
| What happens to the parity obligation | Its content is guaranteed by derivation and holds more strongly than when it was checked by comparison; it is excluded from derivation by name and evaluated by nothing. | It is restated with the stage that names derivation as its carrier, and its check module is withdrawn along with the exclusion that named it. | S6 pps_artifacts_requiring_action #3 |
| What happens to the obligation that judges quality | It is the one obligation of eighty-nine whose violation warns, its subject is whether a thing is good, and it has no consumers. | It is named for its owning subdomain to withdraw. This dossier does not write it, because `capability_contracts` owns it. | S6 ownership #6 |
| Who restates the fourteen | The fourteen are declared by six subdomains, and none of the six is `conformance`. | Each is named for its owner to act on. This dossier delivers the mechanism and the vocabulary and writes no obligation it does not own. | S6 boundary_rules AN_OBLIGATION_IS_RESTATED_BY_ITS_OWNER |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| governance::CONSTITUTION_INVARIANTS_V0 | REVIEW | Governs what every obligation declares and how it is enforced | Gains the requirement that an obligation's declared response to a violation be true of its check, and that a stage routing elsewhere name its destination. The governance surface is authored rather than rendered, so this amendment is written by hand and cited here, not scheduled for construction. Reached by forty-seven obligations on the platform surface. | S6 pps_artifacts_requiring_action #1 |
| conformance::CONSTITUTION_ASSERT_V0 | REVIEW | Defines the structure and semantics of a check, and names the carrier of each of its rules | Two of its four rules name no carrier and a third names an obligation that never runs. Gains the rule that a declared check is capable of refusing, and a carrier for every rule it declares. Authored by hand, not rendered. | S6 pps_artifacts_requiring_action #2 |
| conformance::INVARIANT_ASSERT_PARITY_V0 | REVIEW | States that every obligation has exactly one check and every check exactly one obligation | Published, declaring that a violation fails the build immediately, excluded from derivation by name, evaluated by no build, referenced by no artifact. Restated by hand with derivation named as its carrier, because the governance surface is authored rather than rendered. | S6 pps_artifacts_requiring_action #3 |
| compiler::INVARIANT_HANDLER_REGISTRY_CLOSED_V0 | REUSE | Requires every declared check to have a registered implementation before the checking phase begins | The existing refusal of a check that does not exist, at the point capability is established. Unchanged; named because the new refusal is placed beside it. | S6 pps_artifacts_requiring_action #4 |
| execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | REUSE | Confirms an obligation delegated to a runtime outcome is bound to one | The existing confirmation of a delegation, covering one destination. Unchanged; named as the model the new destination follows. | S6 pps_artifacts_requiring_action #5 |
| capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0 | REVIEW | The one obligation of eighty-nine declaring that its violation warns | Its check returns warnings and reports passed; its subject is whether a thing is good. Named for `capability_contracts` to withdraw; not written here. | S6 pps_artifacts_requiring_action #6 |
| authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `authority` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #7 |
| authority::INVARIANT_AUTHORITY_REQUIRED_FOR_EXECUTION_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `authority` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #8 |
| authority::INVARIANT_AUTHORITY_STATE_WELL_FORMED_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `authority` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #9 |
| authority::INVARIANT_NO_AMBIENT_AUTHORITY_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `authority` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #10 |
| authority::INVARIANT_NO_RUNTIME_AUTHORIZATION_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `authority` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #11 |
| authority::INVARIANT_NO_WORKFLOW_AUTHORIZATION_LOGIC_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `authority` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #12 |
| authority::INVARIANT_TRACE_AUTHORITY_BINDING_REQUIRED_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `authority` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #13 |
| actor::INVARIANT_IDENTITY_AUTHORITY_SEPARATION_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `actor` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #14 |
| execution_topology::INVARIANT_NO_RUNTIME_TOPOLOGY_SYNTHESIS_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `execution_topology` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #15 |
| execution_topology::INVARIANT_TOPOLOGY_IMMUTABLE_AFTER_COMPILATION_V0 | REVIEW | Declares that a violation fails the build immediately; its check has no refusal-producing path | Named for `execution_topology` to restate with the stage its own prose already states. Not written here. | S6 pps_artifacts_requiring_action #16 |
| capability_side_effects::INVARIANT_CS_ISOLATED_EXECUTION_V0 | REVIEW | Declares that a violation fails the build immediately; its check states the runtime's executor routing carries it | Named for `capability_side_effects` to restate as carried elsewhere, naming the runtime. Not written here. | S6 pps_artifacts_requiring_action #17 |
| capability_side_effects::INVARIANT_CS_TRACEABLE_V0 | REVIEW | Declares that a violation fails the build immediately; its check states the runtime execution engine carries it | Named for `capability_side_effects` to restate as carried elsewhere, naming the runtime. Not written here. | S6 pps_artifacts_requiring_action #18 |
| conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | REVIEW | Declares that a violation fails the build immediately; its check states a phase of the compiler carries it | Owned by this subdomain, so it is restated by hand as carried elsewhere, naming that phase. The one of the seventeen this dossier may write, and it is authored rather than rendered. | S6 pps_artifacts_requiring_action #19 |
| surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0 | REVIEW | Declares that a violation fails the build immediately; its check states code review carries it, which is not a mechanism | Named for `surface_contract` to restate as not yet enforced, since a practice is not a destination a mechanism can confirm. Not written here. | S6 pps_artifacts_requiring_action #20 |
| conformance::STRUCTURE_CONFORMANCE_POLICY_V0 | REVIEW | Declares what the conformance subdomain compiles | Unchanged; named because the amended artifacts are compiled under it. | S6 ownership #1 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|-----------|--------|------|---------|-----------------|--------|----------------|
| Declaring whether an obligation is enforced | VOCAB | conformance::VOCAB_ENFORCEMENT_STATUS_V0 | The places an obligation may be enforced, and what each requires of the obligation that declares it | conformance | NEW | S6 governance_outcome #2 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Execution Topology

<!-- register:execution_topology -->
| Workflow | Node | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|-----------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| NONE IDENTIFIED |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| governance::CONSTITUTION_INVARIANTS_V0 | ATTRIBUTE | core.enforcement_stage | array | YES | — | Where the obligation is enforced. Its admissible values are governed by the new vocabulary. |
| governance::CONSTITUTION_INVARIANTS_V0 | ATTRIBUTE | core.enforced_by | string | NO | — | The mechanism that carries the obligation. Required when the declared stage routes the obligation away from the build; refused otherwise. |
| governance::CONSTITUTION_INVARIANTS_V0 | ATTRIBUTE | core.violation_response | string | YES | — | How a violation is answered. Unchanged in form, and now checked against what the derived check can produce. |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | ATTRIBUTE | symbols | object | YES | — | Each admissible stage, what carries the obligation there, and whether a destination must be named. |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|----------------------|-----------------------------|----------------------------------|----------------|
| NONE IDENTIFIED |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | NONE | enforcement_stage | lower_snake | compiler_assertion | The build derives a check and runs it. The check must have a path that produces a refusal. | S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | NONE | enforcement_stage | lower_snake | compiler_validation | A phase of the build carries the obligation directly. The check must have a path that produces a refusal. | S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | NONE | enforcement_stage | lower_snake | compiler_meta_validation | The build carries the obligation over its own governance surface. The check must have a path that produces a refusal. | S6 boundary_rules A_CLAIM_OF_ENFORCEMENT_IS_CHECKED |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | NONE | enforcement_stage | lower_snake | runtime_outcome | The obligation is carried by a violation outcome and its routing. No check is derived. A destination is named. | S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | NONE | enforcement_stage | lower_snake | composition_conformance | The obligation is carried by the assembler over the composed snapshot. No check is derived. A destination is named. | S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | NONE | enforcement_stage | lower_snake | enforced_elsewhere | The obligation is carried by a named mechanism outside the build. No check is derived. A destination is named, and it is confirmed to exist. | S6 boundary_rules A_DELEGATION_NAMES_ITS_PLACE |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | NONE | enforcement_stage | lower_snake | declared_not_enforced | The obligation is stated deliberately and carried by nothing yet. No check is derived, no destination is named, and the obligation is counted as unenforced. | S6 boundary_rules A_DEFERRAL_IS_DECLARED_NOT_WRITTEN |

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|-----------|-----|-------|----------------|
| NONE IDENTIFIED |

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| conformance::INVARIANT_ASSERT_PARITY_V0 | core.enforcement_stage | enforced_elsewhere | S7 design_resolution #6 |
| conformance::INVARIANT_ASSERT_PARITY_V0 | core.enforced_by | The step of the build that derives a check from its obligation | S7 design_resolution #6 |
| conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | core.enforcement_stage | enforced_elsewhere | S7 design_resolution #2 |
| conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0 | core.enforced_by | The phase of the build that validates test data | S7 design_resolution #2 |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | governed_by | vocabulary::CONSTITUTION_VOCABULARY_V0 | S7 new_artifacts VOCAB_ENFORCEMENT_STATUS_V0 |
| conformance::VOCAB_ENFORCEMENT_STATUS_V0 | concern | conformance | S6 ownership #2 |

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|
| NONE IDENTIFIED |

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|
| NONE IDENTIFIED |

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NEW | conformance | 1 | conformance::VOCAB_ENFORCEMENT_STATUS_V0 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|
| NONE IDENTIFIED |

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|
| NONE IDENTIFIED |

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|
| Building a composition | An obligation declares itself enforced and its check cannot refuse anything | The six subdomains that own the fourteen | Each restates its own obligations with the stage that matches what its check does. The rule is written by this change and armed after they have, because arming it first would fail every build on obligations this dossier may not write. | S1 operation_refusals #1 |
| Building a composition | An obligation declares enforcement elsewhere and does not name where | The four subdomains whose obligations delegate in prose | Each names the mechanism its check's own text already states. The rule is written by this change and armed after they have. | S1 operation_refusals #2 |
| Admitting an obligation as governance | Its check only reports and never refuses | capability_contracts | That subdomain withdraws the one obligation of eighty-nine whose violation warns. The rule this change writes refuses a check with no refusal path; this check has one its obligation cannot reach, so the correction is a declaration rather than a refusal. | S1 operation_refusals #3 |

---

## 20. Refusal Governance Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|
| NONE IDENTIFIED |

---

## Gate 1 — Design Approval

**Gate 1 closes here.** Stages 0 through 7 are presented for review as a body — a unified review of
the complete design, not a per-stage approval. Approval authorizes Stage 8, the Authoring Mandate.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`10aa26e1582f…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the rendering of one vocabulary, and the hand-authoring of the four
governance amendments §2 cites as REVIEW. It authorizes nothing else.

Two things about this design are worth naming at its closure. The governance surface is authored
rather than constructed, so the constitutions and obligations this change amends are cited and
written by hand; only the vocabulary is rendered. And every refusal the seed states is recorded in
§19 as a deferral rather than a discharge: the rules are written by this change and armed after the
six subdomains that own the fourteen have restated them. Arming them first would fail every build on
obligations this dossier may not write.
