# Stage 8 — Authoring Mandate: platform / identity semantics

**Stage:** 8 — Authoring Mandate
**CR:** identity_semantics
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. One vocabulary is built, in the subdomain that governs identity.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | NEW | artifact | — |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 1 | The vocabulary naming the parts of a declaration that only explain and the lists whose order carries no meaning. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | artifact |

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
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | Read by the change that compares two declarations, which belongs to the transformation domain. Nothing is built or run differently because of it. |
