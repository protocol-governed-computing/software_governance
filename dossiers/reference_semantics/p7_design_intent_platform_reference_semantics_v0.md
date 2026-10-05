# Stage 7 — Design Intent: platform / reference semantics

**Stage:** 7 — Design Intent
**CR:** reference_semantics
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Read against the pinned baseline
`c55dbfd7d1ae6611e3fde9004377d52cd847891a1dc23191980a343bb83445ec`.

One vocabulary is rendered, as the new version of the declaration of what carries no meaning. It keeps
the two groups it had and adds five: the parts whose full names are references, the part whose keys
are, the reference parts where a short code is refused, the parts that declare supersession, and the
rules a comparison applies. Every reference part was surveyed across the composition: each names an
artifact wherever it holds a full name. The old version is stood down. Nothing names it.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| One declaration says what a reference is | One place declares which parts are references | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 declares `reference`, `reference_keyed`, `full_name_required` and `supersession`, beside `documentation` and `unordered` | S4 design_decisions #1 |
| One enforcer for short codes | One rule, enforced once | artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0 refuses a short code in a `full_name_required` part, read from the declaration; the record of references only records. `bindings` is not one: a workflow's admission keys its bindings by short code, as its requires and forbids do, so a short-code binding key is parked with the other short-code references | S4 design_decisions #2 |
| A full name sits only where it is declared | What names another artifact is declared | The record of references refuses a full name outside a `reference` part, a `reference_keyed` key, a `supersession` part and the artifact's own identity | S4 design_decisions #3 |
| The reach check sees no less | It must see no less than it does today | artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 reads full names from the `reference` parts, skips the `supersession` parts, and still finds a stood-down artifact's short code anywhere | S4 design_decisions #4 |
| The rules are entries | A rule in prose is not sealed | `sameness_rules` names `explanation_only_as_text` and `reference_to_declared_successor` | S4 design_decisions #6 |
| A new version | Adding to the declaration changes its meaning | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 supersedes artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | S4 design_decisions #7 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | REPLACE |  | Stood down by its new version. Nothing names it. | S6 pps_artifacts_requiring_action #1 |
| vocabulary::CONSTITUTION_VOCABULARY_V0 | REUSE |  | Governs the new version, unchanged. | S6 pps_artifacts_requiring_action #2 |
| artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 | REUSE |  | Its obligation is unchanged; its check reads the declaration. | S6 pps_artifacts_requiring_action #3 |
| artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0 | REUSE |  | Its obligation is unchanged; its check reads the declaration. | S6 pps_artifacts_requiring_action #4 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| Declare what names another artifact | VOCAB | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | The parts of a declaration that carry no meaning, the parts that name another artifact, and the rules a comparison applies | artifact | NEW | S6 governance_outcome #1 |

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|

---

## 9. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | supersedes | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | S4 design_decisions #7 |

---

## 10. Structure Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|------|------|------|----------------|

---

## 11. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| NEW | artifact | 1 | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 |
| REPLACE | artifact | 1 | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 |

---

## 12. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 13. Unchanged Registers

No act, transform, policy, entrance or generator is touched. The compiler's reading of references changes, and is named in the refusal deferral below.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|---|---|---|---|---|---|---|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | summary | A one-line statement of what the artifact is, for a reader. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | description | A fuller statement of what the artifact or one of its fields is, for a reader. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | notes | Remarks for a reader about how the artifact is written or used. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | purpose | Why a capability exists, for a reader. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | use_cases | Examples of where a capability is used, for a reader. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | failure_modes | The ways a capability can fail, described for a reader; the outcomes themselves are declared elsewhere. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | intent | What a rule is for, for a reader. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | detail | The words a rule reports a finding with; the finding itself is decided by the rule. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | documentation | lower_snake | admission_rules | Admission described for a reader; admission is decided by the declared inputs. Exempt only where its value is text. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | allowed | The outcomes a contract may end with; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | result_surface | The outcomes a step answers; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | result_status_values | The outcomes an operation can report; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | canonical_surface | The outcomes a surface contract admits; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | applies_to_kinds | The kinds an obligation applies to; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | governs | The kinds or artifacts a constitution or surface contract governs; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | superseded_by | The successors that stand in an artifact's place; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | requires | The moments an admission requires; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | forbids | The moments an admission forbids; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | consults | The bindings an act consults; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | allowed_capability_transforms | The transforms a surface admits; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | unordered | lower_snake | allowed_capability_side_effects | The side effects a surface admits; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | actor_context | The actor an act admits. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | allowed_capability_side_effects | The side effects a surface admits. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | allowed_capability_transforms | The transforms a surface admits. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | atom | The atom a molecule step runs. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | consults | The bindings an act consults. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | disposition_vocabulary | The vocabulary a structure's dispositions are drawn from. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | emit | The moments an ending announces. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | enforced_by | The rule that enforces an obligation. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | extends | The vocabulary a vocabulary builds on. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | fqdn_id | The artifact a workflow place runs. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | governed_by | The constitution that governs an artifact. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | molecule | The molecule a molecule step runs. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | phase_workflows | The phase workflows a judge consults, each under its phase. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | runtime_binding | The binding a workflow runs under. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | side_effect | The side effect a step dispatches. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | side_effects | The side effects an artifact names. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | storage_structure | The structure a binding stores under. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | structure | The structure an artifact is built or stored under. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | target | The transform a test exercises. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | transform | The transform a step runs. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | transforms | The transforms an artifact names. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | vocabulary_id | The vocabulary an artifact draws its values from. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference | lower_snake | workflow | The workflow an entrance or intent starts. A full name at or beneath it is a reference. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | reference_keyed | lower_snake | bindings | The capabilities a binding binds, each named by a key. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | consults | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | governed_by | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | runtime_binding | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | side_effects | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | structure | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | transform | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | transforms | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | full_name_required | lower_snake | vocabulary_id | A reference part where a short code is refused. | S6 boundary_rules ONE_ENFORCER_PER_RULE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | supersession | lower_snake | supersedes | The predecessors an artifact stands in for; names them without reaching them. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | supersession | lower_snake | superseded_by | The successors that stand in an artifact's place; names them without reaching them. | S6 boundary_rules ONE_PLACE_SAYS_WHAT_A_REFERENCE_IS |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | sameness_rules | lower_snake | explanation_only_as_text | An explanation part is ignored by a comparison only where its value is a sentence or a list of sentences. | S6 boundary_rules RULES_ARE_NAMED |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NONE | sameness_rules | lower_snake | reference_to_declared_successor | A reference now naming the declared successor of what it named is not a change of meaning. | S6 boundary_rules RULES_ARE_NAMED |

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---|---|---|---|---|

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|---|---|---|---|

---

## 14. Refusal Discharge

The business declared one refusal. The design language has no register for a compiler check, so it is deferred to the check this change arms.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|
| Building a composition | A full name sits in a part not declared a reference | The compiler's record of references, which reads artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | Armed by this change. Every full name in the composition sits in a declared part, so arming it fails no build. | S0 operation_refusals #1 |

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|---|---|---|---|---|

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn.

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---|---|---|---|---|---|

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---|---|---|---|

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---|---|---|---|---|---|

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|---|---|---|---|

