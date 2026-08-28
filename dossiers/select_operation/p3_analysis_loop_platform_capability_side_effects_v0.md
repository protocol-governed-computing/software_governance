# Stage 3 — Analysis Loop: platform / capability_side_effects
**Stage:** 3 — Analysis Loop
**CR:** select_operation
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot and the change request that carried the operation in, rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The three gaps are one gap and one note. Two are the same absence seen twice — the reason exists and is in the wrong place — and the third is the fact that nothing objected when it was put there. | Fixes what this change delivers: a record, in one place, and an account of how it came to be missing. | OBSERVED | HIGH | CLOSED | Both critical gaps trace to the same inventory row in the catalog's change request. |
| Q2 | What is delivered is a record, not a change to the platform. The operation is declared, reached by two contracts and running against real stores; altering it would break callers to satisfy bookkeeping. | Rules out re-delivering the operation, and fixes the change as retrospective. | OBSERVED | HIGH | CLOSED | The catalog's acceptance criteria hold, twenty-three of twenty-three, driving both callers. |
| Q3 | The reason belongs with the capability because every domain reads the capability and only one reads the catalog's change request. An operation's justification held by its first caller is unfindable by its second. | Places the record, and states why the placement is the substance rather than a filing preference. | OBSERVED | HIGH | CLOSED | A second caller already exists and its question is a different one. |
| Q4 | The boundary crossing was declared rather than hidden. The change request stated the action and the reason in its own registers, and every check passed because none of them asked whether a domain may amend a platform capability. | Distinguishes an unenforced rule from a broken one, and keeps the record factual rather than accusatory. | OBSERVED | HIGH | CLOSED | The inventory row names the action plainly, and the rule that refuses it dates from this session. |
| Q5 | Recording the operation does not make it the platform's decision retrospectively. The platform now owns the reason, but a reader should be able to see that the need came from a domain, because that is what makes the offer's history legible. | Decides what the record must say, not merely that one must exist. | OBSERVED | HIGH | CLOSED | The reason as written is a catalog need: a search must see records rather than keys. |
| Q6 | Nothing distinguishes an operation the platform decided from one a caller needed, and this change does not fix that. It records one instance; the general question is whether an offer should carry its provenance at all. | Bounds the change, and names what it deliberately leaves open. | OBSERVED | HIGH | CLOSED | All nine operations of the capability present identically. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| The capability offers an operation that reads every record it holds. | S2 belief_verification #1 | CONFIRMED | Re-read: the operation is declared, answers with the records and the keys, and is declared a read. |
| The operation is reached by acts of a business domain and is running. | S2 belief_verification #2 | CONFIRMED | Re-run: the catalog's criteria hold, driving both contracts that perform it. |
| The operation was carried into the platform by a business change request that inventoried the capability as one it extends. | S2 belief_verification #3 | CONFIRMED | Re-read: the inventory row names the action and the reason, in the change request that needed it. |
| Nothing in the composition asked whether a business change request may amend a platform capability. | S2 belief_verification #4 | CONFIRMED | Re-read: the design phase held an inventoried artifact to resolving and to carrying a summary, and to nothing else. |
| The reason the capability offers this operation is written down in another domain's change request. | S2 belief_verification #5 | CONFIRMED | Re-read: the capability states what each operation does and no reason for offering any of them. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| A dossier recording why the capability offers this operation | declaration | AUTHOR_NEW | No dossier states it; the reason is in a business change request. |
| A statement that the change crossed an authority boundary | declaration | AUTHOR_NEW | Nothing records the crossing, and the rule refusing it has nothing to point at. |
| The operation as declared on the capability | mechanism | REUSE | Declared, published, reached by two contracts and running. |
| The rule that refuses a design amending what it cannot author | mechanism | REUSE | Written this session; this dossier is what it points at. |
| The closed set of admitted capabilities | mechanism | EXISTING | Governs which capabilities exist, and is untouched by this change. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | Gains a recorded reason for one of the nine operations it offers. Its behaviour, its surface and its callers are unchanged. | 2 | Two catalog contracts perform the operation. |
| book_library_mgmt::CC_SEARCH_CATALOG_V0 | Unchanged. It keeps performing the operation exactly as it does. | 1 | One act reaches it. |
| book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Unchanged, and evidence the operation is general rather than a favour to one caller. | 1 | One act reaches it. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Recording why the capability offers an operation that reads every record | AUTHOR_NEW | The reason exists and is held by the first caller that needed it, where the second caller and every later one cannot find it. | Leaving it in the change request was rejected: a second caller already exists and its question is a different one. Copying it onto the capability as a comment was rejected: a reason with no dossier behind it is the state this change is correcting. | S2 gaps #1 |
| Recording that the change crossed an authority boundary | AUTHOR_NEW | The crossing is the reason the record was missing, and a rule now refuses the act without anything showing what it refuses. | Recording only the operation was rejected: it would explain the offer and hide how it came to be unexplained. | S2 gaps #3 |
| The operation itself | REUSE | Declared, reached by two contracts and running; altering it would break callers to satisfy bookkeeping. | Re-delivering it through the pipeline was rejected: there is nothing left to deliver. Withdrawing and re-adding it was rejected for the same reason and at greater cost. | S2 belief_verification #1 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | capability_side_effects | What a capability offers is what this subdomain governs, and the record belongs where the offer is declared. | S2 belief_verification #5 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | Both are resolved by authoring the record; the third gap is a note the record carries. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the six raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Five dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Five items re-grounded; all five CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. None rests on inference. |
