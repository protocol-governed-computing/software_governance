# Stage 7 — Design Intent: platform / structure
**Stage:** 7 — Design Intent
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| How a kind's disposition is recorded | A kind absent from the dispatch table is absent for three different reasons and one representation. | The dispatch table carries a disposition per kind, drawn from a vocabulary: described, or exempt with a ground. A kind carrying neither is refused. | S6 boundary_rules EVERY_KIND_HAS_A_DISPOSITION |
| What makes a description a description | One is dispatched, requires no field, closes no surface, and reads as governance. | The constitution governing structural declarations states that a description names at least one required field and closes its surface. A kind dispatched to one that does neither is refused. | S6 boundary_rules A_DESCRIPTION_STATES_SOMETHING |
| How drift is reported | Three divergences, none recorded, all found by a build refusing correct work. | Every dispatched description is measured against every artifact of its kind on each build, and a description that refuses one is reported before it is enforced. | S6 boundary_rules DRIFT_IS_REPORTED_NOT_DISCOVERED |
| Who corrects a drifted description | The three describe kinds owned by `actor`, `event` and `intent`. | Each is cited for its owner. This dossier states the requirement and the report; it writes no description. | S6 boundary_rules A_KINDS_SHAPE_IS_ITS_OWNERS |
| Who describes the two undescribed kinds | Both are transport boundary contracts, 44 artifacts. | Cited for `transport`. Same ground. | S6 boundary_rules A_KINDS_SHAPE_IS_ITS_OWNERS |
| Whether any artifact is authored here | Every capability but one is a requirement added to something that exists. | One vocabulary is authored: the dispositions a kind may have. The governance surface is authored by hand rather than rendered, so the two amendments are cited and not scheduled. | S6 ownership #1 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| structure::STRUCTURE_SCHEMA_DISPATCH_V0 | REVIEW | Declares which description governs each artifact kind | Gains a disposition per kind, so an exemption and an oversight stop being the same absence. Authored by hand, not rendered. | S6 pps_artifacts_requiring_action #1 |
| structure::CONSTITUTION_STRUCTURE_V0 | REVIEW | Governs what a structural declaration is | Gains what a description must state to count as one, and that every kind carries a disposition. Authored by hand. | S6 pps_artifacts_requiring_action #2 |
| artifact::INVARIANT_SCHEMA_CONFORMANCE_V0 | REUSE | Checks each declaration against the description its kind is dispatched to | Correct and unchanged; it is only ever handed ten kinds, which is the dispatch table's doing rather than its own. | S6 pps_artifacts_requiring_action #3 |
| actor::CONSTITUTION_ACTOR_V0 | REVIEW | Governs what an actor is | Its description expects a role and forbids the attributes every actor carries, across 11 artifacts. Named for `actor` to correct. | S6 pps_artifacts_requiring_action #4 |
| event::CONSTITUTION_EVENT_V0 | REVIEW | Governs what a moment is | Its description forbids content 20 event declarations carry. Named for `event` to correct. | S6 pps_artifacts_requiring_action #5 |
| intent::CONSTITUTION_INTENT_V0 | REVIEW | Governs what a boundary admits | Its description rejects a whole number as a type across 31 declarations. Named for `intent` to correct. | S6 pps_artifacts_requiring_action #6 |
| transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0 | REVIEW | Governs the boundary contracts | Its two kinds carry 44 artifacts described by nothing. Named for `transport` to describe. | S6 pps_artifacts_requiring_action #7 |
| trace::CONSTITUTION_TRACE_EXECUTION_V0 | REUSE | Governs the runtime trace | Named because four descriptions counted as failing to close a surface describe runtime data of this sort. Unchanged. | S6 pps_artifacts_requiring_action #8 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|-----------|--------|------|---------|-----------------|--------|----------------|
| Recording that a kind needs no description | VOCAB | structure::VOCAB_SCHEMA_DISPOSITION_V0 | The dispositions a kind may have toward description, and which of them the build admits | structure | NEW | S6 governance_outcome #3 |

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
| structure::VOCAB_SCHEMA_DISPOSITION_V0 | ATTRIBUTE | symbols | object | YES | — | The two dispositions a kind may have and what each means. A kind carrying neither is refused, which needs no symbol of its own. |

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
| structure::VOCAB_SCHEMA_DISPOSITION_V0 | NONE | schema_disposition | lower_snake | described | A description governs the kind and the build reads it. The description must name at least one required field and close its surface. | S7 design_resolution #2 |
| structure::VOCAB_SCHEMA_DISPOSITION_V0 | NONE | schema_disposition | lower_snake | exempt | The kind needs no description and the ground is stated beside the disposition. Admitted, and readable as a decision rather than an absence. | S7 design_resolution #1 |

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
| structure::VOCAB_SCHEMA_DISPOSITION_V0 | governed_by | vocabulary::CONSTITUTION_VOCABULARY_V0 | S7 new_artifacts VOCAB_SCHEMA_DISPOSITION_V0 |
| structure::VOCAB_SCHEMA_DISPOSITION_V0 | concern | structure | S6 ownership #3 |

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
| NEW | structure | 1 | structure::VOCAB_SCHEMA_DISPOSITION_V0 |

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
| Building a composition | A declaration carries content the description of its kind does not name | structure | Carried today for ten kinds and extended to every kind that gains a description. Recorded as a deferral because the kinds whose descriptions are corrected elsewhere are dispatched by their owners, not here. | S1 operation_refusals #1 |
| Building a composition | An artifact kind is neither described nor recorded as exempt | structure | The dispatch table carries a disposition for every kind. Armed once every kind has one, because arming it first would refuse every build on kinds this dossier does not describe. | S1 operation_refusals #2 |
| Dispatching a description | It refuses an artifact the composition currently carries | structure | The report is written by this change and names such a description before it is enforced. The dispatch itself is the owning subdomain's act, once its description is corrected. | S1 operation_refusals #3 |

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
`8f82acb652c8…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the authoring of one vocabulary and the hand-authoring of the two
amendments §2 cites for this subdomain. It authorizes nothing else.

The scope narrowed twice in discovery and both narrowings are the finding. Five open surfaces were
two populations, and four of them describe runtime data rather than declarations — miscounted because
a directory and a naming convention are all that identify a description's population. And a kind
dispatched to a description that describes nothing reads as governed, so **the count of dispatched
kinds measures neither coverage nor governance**, which is why this change delivers a report rather
than a tally.
