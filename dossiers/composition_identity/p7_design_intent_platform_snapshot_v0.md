# Stage 7 — Design Intent: platform / snapshot
**Stage:** 7 — Design Intent
**CR:** composition_identity
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

HOW it is built. FQDNs, topology, schemas and bindings. The full dossier is reviewed as a body.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| What is excluded from a composition's identity | The attestation carries two fields the runtime enforces and one that records when the signing happened. | The exclusion is stated as a field within a named file, not as a path. The enumeration that lists constituents excludes that field from the value it takes over the attestation's bytes, and takes the value over what remains. | S6 boundary_rules DETERMINATIVE_CONTENT_STAYS |
| Where the exclusion is stated | Two exclusions already exist, each naming its ground where the exclusion is made. | The new exclusion is added beside them, in the same list, carrying its own ground. Nothing is excluded by directory, by suffix or by convention. | S6 boundary_rules EXCLUSION_IS_DECLARED |
| Who states which fields constitute | What an attestation carries is the cryptographic trust subdomain's to declare. | `cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0` states the division. This dossier consumes it and does not write it; the constitution is cited for its owner to author. | S6 boundary_rules AN_ATTESTATION_IS_STATED_BY_ITS_OWNER |
| How a rebuild is required to reproduce | Nothing requires it today, which is why twenty failing pins went unreported. | An obligation of the snapshot subdomain requires that constituting the same source twice yields one identity, carried by the assembler over a composition it has just built. | S6 boundary_rules A_REBUILD_REPRODUCES |
| What the change does not claim | Two builds on one machine minutes apart is what was measured. | The obligation is stated over a rebuild of unchanged source, not over builds on different machines. A further instability is a further change. | S6 boundary_rules ONLY_WHAT_WAS_MEASURED_IS_CLAIMED |
| Whether any artifact is authored | Every capability this change needs is a requirement added to something that exists. | No artifact is authored. The governance surface is authored by hand rather than rendered, so every row of §2 is cited and none is scheduled. | S6 ownership #1 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | REVIEW | Governs what may be trusted and how a build attests what it produced | Gains the statement of which of an attestation's fields constitute the composition it attests and which accompany it. Authored by hand by its owning subdomain, not rendered, and not written here. | S6 pps_artifacts_requiring_action #1 |
| cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0 | REVIEW | Requires a build to declare the trust arrangement it runs under | Requires the declaration and nothing about what the resulting attestation may contribute to an identity. Named as the obligation the new statement sits beside. | S6 pps_artifacts_requiring_action #2 |
| cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0 | REUSE | Declares the arrangement in force: local, unsigned | What makes a placeholder signature admissible. Unchanged, and named because the change holds whether the signature is a placeholder or real. | S6 pps_artifacts_requiring_action #3 |
| compiler::INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0 | REUSE | Requires an artifact to declare a value over its content | Covers an artifact. A composition's identity is taken over files rather than artifacts, and this is the nearest existing requirement. | S6 pps_artifacts_requiring_action #4 |
| artifact::INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0 | REVIEW | Requires one artifact to carry one identity everywhere it appears | The same requirement stated for an artifact. Nothing states it for a composition, which is the gap this change fills. | S6 pps_artifacts_requiring_action #5 |
| execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | REUSE | Confirms an obligation delegated to a runtime outcome is bound to one | The runtime's refusal of a composition whose projection does not match its attestation is why the attestation stays a constituent. Unchanged. | S6 pps_artifacts_requiring_action #6 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family | Code | Summary | Owner Subdomain | Status | Source Finding |
|-----------|--------|------|---------|-----------------|--------|----------------|
| NONE IDENTIFIED |

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
| cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | ATTRIBUTE | attestation.constitutes | array | YES | — | The fields of an attestation that constitute the composition it attests. A composition's identity is taken over these. |
| cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | ATTRIBUTE | attestation.accompanies | array | YES | — | The fields of an attestation that record about the composition rather than constitute it. A composition's identity is taken over the attestation with these removed. |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|----------------------|-----------------------------|----------------------------------|----------------|
| NONE IDENTIFIED |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Value | Meaning | Source Finding |
|-----------------|---------|-------|---------|----------------|
| NONE IDENTIFIED |

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
| cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | attestation.accompanies | signed_at | S7 design_resolution #1 |
| cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | attestation.constitutes | tokenized_projection_hash, attestation_hash | S7 design_resolution #1 |

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
| NEW | snapshot | 0 | |

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
| Verifying a composition | A file it carries as a constituent does not match the bytes its identity was taken over | snapshot | Already carried today, and unchanged by this. It is recorded here rather than as a discharge because this change adds no act; what it changes is which bytes the identity is taken over. | S1 operation_refusals #1 |
| Verifying a composition | It is read somewhere other than where its identity says it was built for | snapshot | Already carried today, and unchanged by this. Recorded for the same reason. | S1 operation_refusals #2 |
| Verifying a composition against a pin | The identity differs | snapshot | Already carried today. What changes is that a difference will mean the compositions differ, which is the point of the change rather than a new refusal. | S1 operation_refusals #3 |

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
`47dd8edc2123…` — the composition `baseline.json` pins and every grounded register was read against.
What the approval authorizes is the hand-authoring of the two amendments §2 cites, and nothing else.
This design schedules no artifact and construction renders none.

The design's whole substance is two declarations: an attestation's projection binding and the value
over it constitute the composition, and the moment it was signed accompanies it. Excluding the file
rather than the field was considered and refused, because the runtime enforces the binding and
dropping it from the identity is the opposite of what this change wants.
