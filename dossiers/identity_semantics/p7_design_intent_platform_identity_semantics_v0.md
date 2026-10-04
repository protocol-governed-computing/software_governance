# Stage 7 — Design Intent: platform / identity semantics

**Stage:** 7 — Design Intent
**CR:** identity_semantics
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Read against the pinned baseline
`53acd1c4879c83841f5bbea0943d45506fed85e4da92bdcf653b59b264af7c0b`.

One vocabulary is rendered. It names, in two groups, the parts of a declaration that only explain
and the lists whose order carries no meaning. Every name in it was surveyed across the composition:
each part named only explains wherever it appears, and each list named is read as a set wherever it
appears. Prose that is data stays out, and so do lists whose order decides.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| One vocabulary declares both groups | One place declares what carries no meaning | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 declares a `documentation` group and an `unordered` group, extending nothing | S4 design_decisions #1 |
| A name is entered only where every occurrence qualifies | Nothing that carries meaning is exempted by name | The survey excludes a test case's question, supporting material and model prompt, which are data; an invariant's subject; and the ordered lists, such as the moments an ending announces and a contract's steps | S4 design_decisions #2 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| vocabulary::CONSTITUTION_VOCABULARY_V0 | REUSE |  | Governs the new vocabulary, unchanged. | S6 pps_artifacts_requiring_action #1 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| Declare what carries no meaning | VOCAB | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | The parts of a declaration that only explain, and the lists whose order carries no meaning | artifact | NEW | S6 governance_outcome #1 |

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
| NEW | artifact | 1 | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 |

---

## 12. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 13. Unchanged Registers

No act, transform, policy, entrance or generator is touched.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|---|---|---|---|---|---|---|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | summary | A one-line statement of what the artifact is, for a reader. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | description | A fuller statement of what the artifact or one of its fields is, for a reader. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | notes | Remarks for a reader about how the artifact is written or used. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | purpose | Why a capability exists, for a reader. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | use_cases | Examples of where a capability is used, for a reader. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | failure_modes | The ways a capability can fail, described for a reader; the outcomes themselves are declared elsewhere. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | intent | What a rule is for, for a reader. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | detail | The words a rule reports a finding with; the finding itself is decided by the rule. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | documentation | lower_snake | admission_rules | Admission described for a reader; admission is decided by the declared inputs. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | allowed | The outcomes a contract may end with; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | result_surface | The outcomes a step answers; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | result_status_values | The outcomes an operation can report; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | canonical_surface | The outcomes a surface contract admits; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | applies_to_kinds | The kinds an obligation applies to; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | governs | The kinds or artifacts a constitution or surface contract governs; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | superseded_by | The successors that stand in an artifact's place; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | requires | The moments an admission requires; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | forbids | The moments an admission forbids; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | consults | The bindings an act consults; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | allowed_capability_transforms | The transforms a surface admits; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NONE | unordered | lower_snake | allowed_capability_side_effects | The side effects a surface admits; a set. | S6 boundary_rules NAMED_ONLY_WHERE_TRUE_EVERYWHERE |

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

The business declared no refusal.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|

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

