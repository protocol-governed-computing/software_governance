# Stage 8 — Authoring Mandate: platform / structure
**Stage:** 8 — Authoring Mandate
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Artifact Authoring

Mechanical. Stage 7's assignments re-ordered into a build sequence; nothing added, nothing dropped.

---

## 1. Build Dependency Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | structure::VOCAB_SCHEMA_DISPOSITION_V0 | NEW | structure | — |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | structure::VOCAB_SCHEMA_DISPOSITION_V0 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 1 | The two dispositions a kind may have toward description. It is admitted first because the dispatch table's new column draws every value from it. |
| EXTEND | 0 | Two amendments are written by hand, because the governance surface is authored rather than rendered: the dispatch table gains a disposition per kind, and the constitution gains what a description must state to count as one. Neither carries a build step. |
| REPLACE | 0 | Nothing is stood down. Three descriptions are corrected by the subdomains that own their kinds, and two are written by the subdomain that owns theirs; none of that is scheduled here. |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| structure::VOCAB_SCHEMA_DISPOSITION_V0 | structure |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| NONE IDENTIFIED |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| NONE IDENTIFIED |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| actor::CONSTITUTION_ACTOR_V0 | Corrected by `actor`, not here. Its description expects a role and forbids the attributes every actor carries. What a declaration admits is its owner's to state; this mandate states only that the kind is described. |
| event::CONSTITUTION_EVENT_V0 | Corrected by `event`, not here. Its description forbids content twenty declarations carry. |
| intent::CONSTITUTION_INTENT_V0 | Corrected by `intent`, not here. Its description rejects a whole number as a type across thirty-one declarations. |
| transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0 | Described by `transport`, not here. Its two kinds carry forty-four artifacts and have no description at all. |
| structure::STRUCTURE_SCHEMA_DISPATCH_V0 | Amended by hand. Every value of its new column is drawn from the vocabulary this mandate schedules, so the vocabulary is admitted first. |

---

## Gate 2 — Mandate Approval

**Gate 2 closes here**, and it freezes scope before authoring begins. After it, any departure is an
Approved Deviation recorded in the authoring manifest — never a silent change.

**Status: CLOSED.** Approved by the business author against the composition `8f82acb652c8…`, the one
`baseline.json` pins, after Construction Completeness read 100% on the single artifact this mandate
renders.

What is frozen is one vocabulary of two dispositions, and two hand-authored amendments: a disposition
per kind, and a statement of what a description must contain to be one. **A description of any
artifact kind is outside this mandate** — three are corrected and two are written by the subdomains
that own those kinds, because what a declaration may contain is theirs to state and this change
decides only that it is stated.

The refusals this change writes are recorded in §19 as deferrals rather than discharges. The kind
disposition refusal arms once every kind carries one; arming it first would refuse every build on
kinds this dossier does not describe.
