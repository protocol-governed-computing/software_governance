# Stage 6 — Governance Intent: platform / structure
**Stage:** 6 — Governance Intent
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `structure` — EXISTING — modified by this CR |
| Authority class | reuse existing — a subdomain declares what its kind admits, the structure subdomain says which description binds, the build refuses; no new actor type |
| Governing constitutions | `structure::CONSTITUTION_STRUCTURE_V0` |

Which kind is described by what, and what makes a description binding, is the structure subdomain's
own question. So the dispatch, the disposition of each kind, the requirement that a description state
something, and the report that a description has stopped matching all belong here.

**What a declaration of a kind may contain is not this subdomain's to write.** The three drifted
descriptions and the two absent ones describe kinds owned elsewhere — actors, events, intents and the
two transport boundary contracts. This dossier states that they are described and what makes a
description binding; each owning subdomain states what its declarations admit. They are recorded
below as artifacts requiring action by their owners.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Reporting a description that has stopped matching | structure | OWNED | | S4 gap_register GAP-1 |
| Stating what makes a description one | structure | OWNED | structure::CONSTITUTION_STRUCTURE_V0 | S4 gap_register GAP-3 |
| Recording that a kind needs no description | structure | OWNED | structure::STRUCTURE_SCHEMA_DISPATCH_V0 | S4 gap_register GAP-5 |
| Correcting a description that has drifted | actor | DEFERRED | actor::CONSTITUTION_ACTOR_V0 | S4 gap_register GAP-2 |
| Describing a kind that has no description | transport | DEFERRED | transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0 | S4 gap_register GAP-4 |
| Refusing a non-conforming declaration | artifact | SATISFIED | artifact::INVARIANT_SCHEMA_CONFORMANCE_V0 | S4 capability_graph #6 |
| Describing runtime data | trace | SATISFIED | trace::CONSTITUTION_TRACE_EXECUTION_V0 | S4 capability_graph #7 |
| Reconsidering the shape of a kind whose description drifted | structure | DEFERRED | | S4 authoring_scope deferred #1 |
| Separating the runtime-data descriptions from the artifact-kind ones | structure | DEFERRED | | S4 authoring_scope deferred #2 |
| What a declaration of each kind means | structure | DEFERRED | | S4 authoring_scope deferred #3 |

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
| What an actor, event or intent declaration admits | structure -> actor | actor::CONSTITUTION_ACTOR_V0 | GAP | S4 dependency_graph #3 |
| What a transport boundary declaration admits | structure -> transport | transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0 | GAP | S4 dependency_graph #4 |
| The refusal of a non-conforming declaration | structure -> artifact | artifact::INVARIANT_SCHEMA_CONFORMANCE_V0 | SATISFIED | S4 dependency_graph #1 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| structure::STRUCTURE_SCHEMA_DISPATCH_V0 | Names ten of fifteen kinds. A kind absent from it is skipped in silence, and it cannot say a kind is exempt rather than forgotten. | EXTEND | S4 gap_register GAP-5 |
| structure::CONSTITUTION_STRUCTURE_V0 | Governs the structure subdomain and says nothing about whether a kind must be described, nor what makes a description one. | EXTEND | S4 gap_register GAP-3 |
| artifact::INVARIANT_SCHEMA_CONFORMANCE_V0 | Checks each declaration against the description its kind is dispatched to and refuses on a violation. Correct; it is only ever handed ten kinds. | REUSE | S4 capability_graph #6 |
| actor::CONSTITUTION_ACTOR_V0 | Governs what an actor is. Its description expects a role and forbids the attributes every actor carries, across 11 artifacts. Named for `actor` to correct; not written here. | REVIEW | S4 gap_register GAP-2 |
| event::CONSTITUTION_EVENT_V0 | Governs what a moment is. Its description forbids content 20 event declarations legitimately carry. Named for `event` to correct; not written here. | REVIEW | S4 gap_register GAP-2 |
| intent::CONSTITUTION_INTENT_V0 | Governs what a boundary admits. Its description rejects a whole number as a type across 31 declarations. Named for `intent` to correct; not written here. | REVIEW | S4 gap_register GAP-2 |
| transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0 | Governs the boundary contracts. Its two kinds carry 44 artifacts and are described by nothing. Named for `transport` to describe; not written here. | REVIEW | S4 gap_register GAP-4 |
| trace::CONSTITUTION_TRACE_EXECUTION_V0 | Governs the runtime trace. Named because four descriptions counted as failing to close a surface describe runtime data of this sort, not declarations. Unchanged. | REUSE | S4 design_decisions #5 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| EVERY_KIND_HAS_A_DISPOSITION | A kind is described, or recorded as exempt with its ground stated. An absence is neither, and reads the same as nobody having decided. | S4 constraint_register #4 |
| A_DESCRIPTION_MATCHES_WHAT_IT_DESCRIBES | A description states the shape the platform currently builds. One that disagrees is disagreeing with the working system. | S4 constraint_register #7 |
| A_DESCRIPTION_STATES_SOMETHING | A description requiring no field and closing no surface is not a description, and dispatching a kind to it is not governance. | S4 constraint_register #8 |
| COVERAGE_IS_NOT_GOVERNANCE | The count of dispatched kinds measures neither. Both errors are present in one composition: five kinds checked against nothing, and one checked against nothing while appearing checked. | S4 constraint_register #8 |
| NO_CORRECT_DECLARATION_IS_REFUSED | A description that would turn away an artifact the composition carries is corrected before it is dispatched, never dispatched to find out. | S4 constraint_register #1 |
| NO_ARTIFACT_IS_EDITED_TO_MATCH_A_STALE_DESCRIPTION | The artifacts are current. Editing one to satisfy a description nobody had read would change the working system to preserve a mistake. | S4 constraint_register #2 |
| DRIFT_IS_REPORTED_NOT_DISCOVERED | A description that stops matching is reported. Finding one by dispatching it and reading the refusals only works while nobody relies on it. | S4 constraint_register #7 |
| A_KINDS_SHAPE_IS_ITS_OWNERS | What a declaration admits is stated by the subdomain that owns the kind. This dossier says that a kind is described and what makes a description binding, never what any description says. | S4 design_decisions #6 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Reporting a description that has stopped matching | structure | S4 gap_register GAP-1 |
| Stating what makes a description one | structure | S4 gap_register GAP-3 |
| Recording that a kind needs no description | structure | S4 gap_register GAP-5 |

---

## Gate 1 — Design Approval
