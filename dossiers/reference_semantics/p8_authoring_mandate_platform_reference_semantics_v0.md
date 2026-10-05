# Stage 8 — Authoring Mandate: platform / reference semantics

**Stage:** 8 — Authoring Mandate
**CR:** reference_semantics
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. One vocabulary is built, in the subdomain that governs identity, and the version it replaces is stood down.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | NEW | artifact | — |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | artifact::VOCAB_DECLARATION_REPRESENTATION_V1 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 1 | The new version of the declaration of what carries no meaning, naming also the parts that name another artifact and the rules a comparison applies. |
| REPLACE | 1 | The version it stands down. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | artifact |

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
| artifact::VOCAB_DECLARATION_REPRESENTATION_V1 | Read by the compiler's record of references and its two reference checks, and by the design and build change that compares two declarations. |
