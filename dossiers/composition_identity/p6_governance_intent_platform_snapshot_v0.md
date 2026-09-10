# Stage 6 — Governance Intent: platform / snapshot
**Stage:** 6 — Governance Intent
**CR:** composition_identity
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `snapshot` — EXISTING — modified by this CR |
| Authority class | reuse existing — a build constitutes and attests, the runtime refuses a mismatch, a reader compares two identities; no new actor type |
| Governing constitutions | `cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0` |

What belongs to a composition's identity is the snapshot subdomain's own question, so the exclusion of
a field that records rather than constitutes belongs here, and so does the requirement that a rebuild
reproduce an identity. Nothing new stands on its own; no artifact is authored.

**The attestation is not this subdomain's to write.** The field being excluded sits in an artifact
the cryptographic trust subdomain owns, and what that artifact states is its to declare. This dossier
states what an identity is computed over and consumes the division; it does not write the division
into the attestation. That is recorded below as an artifact requiring action by its owner.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Excluding at the grain of a field | snapshot | OWNED | | S4 gap_register GAP-1 |
| Requiring a rebuild to reproduce an identity | snapshot | OWNED | | S4 gap_register GAP-3 |
| Stating what an attestation contributes to identity | cryptographic_trust | DEFERRED | cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | S4 gap_register GAP-2 |
| Excluding what does not constitute a composition | snapshot | SATISFIED | compiler::INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0 | S4 capability_graph #4 |
| Refusing a composition whose projection does not match its attestation | execution | SATISFIED | execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | S4 capability_graph #5 |
| Declaring the trust arrangement in force | cryptographic_trust | SATISFIED | cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0 | S4 capability_graph #6 |
| Making the signature real | cryptographic_trust | DEFERRED | | S4 authoring_scope deferred #1 |
| Establishing reproducibility across machines | snapshot | DEFERRED | | S4 authoring_scope deferred #2 |
| Ruling on the approvals recorded against expired pins | snapshot | DEFERRED | | S4 authoring_scope deferred #3 |
| Re-pinning the twenty expired dossiers | snapshot | DEFERRED | | S4 authoring_scope deferred #4 |

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
| The division of an attestation's fields into what constitutes and what accompanies | snapshot -> cryptographic_trust | cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | GAP | S4 dependency_graph #1 |
| The refusal of a composition whose projection does not match its attestation | snapshot -> execution | execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | SATISFIED | S4 dependency_graph #2 |
| The trust arrangement that makes a placeholder signature admissible | snapshot -> cryptographic_trust | cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0 | SATISFIED | S4 dependency_graph #1 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | States the trust model a build runs under, and says nothing about which of an attestation's fields constitute the composition it attests. | EXTEND | S4 gap_register GAP-2 |
| cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0 | Requires a build to declare its trust arrangement. Requires nothing about what the resulting attestation may contribute to an identity. | REVIEW | S4 dependency_graph #1 |
| cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0 | Declares the arrangement in force: local, unsigned. It is what makes a placeholder signature admissible and it is unchanged. | REUSE | S4 capability_graph #6 |
| compiler::INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0 | Requires an artifact to declare a value over its content. Covers an artifact; a composition's identity is a different question, taken over files. | REUSE | S4 capability_graph #4 |
| artifact::INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0 | Requires one artifact to carry one identity everywhere it appears. Nothing states the same requirement for a composition. | REVIEW | S2 pps_baseline_fqdns #5 |
| execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | Confirms an obligation delegated to a runtime outcome is bound to one. Named because the runtime's refusal of a mismatched projection is why the attestation stays a constituent. | REUSE | S4 capability_graph #5 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| IDENTITY_IS_CONTENT_ALONE | A composition's identity is a function of what it contains and of nothing else. An identity that counts when a build ran answers a different question from the one a reader asks it. | S4 constraint_register #1 |
| A_REBUILD_REPRODUCES | Building unchanged source twice produces one identity. A record naming a composition nobody can produce makes every claim resting on it unverifiable. | S4 constraint_register #1 |
| DIFFERENCE_MEANS_DIFFERENCE | Two identities differing means the compositions differ. A field that changes on every build makes a genuine alteration and a rebuild indistinguishable. | S4 constraint_register #2 |
| TAMPERING_IS_STILL_REFUSED | A composition altered after sealing is refused, and one read where it was not built for is refused. Nothing is weakened to make a pin survive. | S4 constraint_register #2 |
| EXCLUSION_IS_DECLARED | What is excluded from the identity names its ground where the exclusion is made. An exclusion inferred from a directory or a suffix would move whenever a file moved. | S4 constraint_register #5 |
| DETERMINATIVE_CONTENT_STAYS | An attestation's determinative fields stay in the identity, because the runtime refuses a composition whose projection does not match them. | S4 constraint_register #6 |
| THE_RECORD_IS_KEPT | The record of when a composition was signed is written and read; what changes is that it no longer decides what the composition is. | S4 constraint_register #4 |
| ONLY_WHAT_WAS_MEASURED_IS_CLAIMED | The change claims stability, not reproducibility. Two builds on one machine is what was measured, and a further instability is a further change. | S4 constraint_register #7 |
| AN_ATTESTATION_IS_STATED_BY_ITS_OWNER | What an attestation carries, and which of its fields constitute the composition, is declared by the subdomain that owns the attestation. This dossier consumes the division and does not write it. | S4 design_decisions #2 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Excluding at the grain of a field | snapshot | S4 gap_register GAP-1 |
| Requiring a rebuild to reproduce an identity | snapshot | S4 gap_register GAP-3 |

---

## Gate 1 — Design Approval
