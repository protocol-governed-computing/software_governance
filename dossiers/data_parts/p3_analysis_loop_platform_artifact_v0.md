# Stage 3 — Analysis Loop: platform / artifact
**Stage:** 3 — Analysis Loop
**CR:** data_parts
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | A data part is a fourth way a part is read, beside references, explanations and history. It is declared as a group of the vocabulary that declares the other three, and read by the one walk that reads them. | Makes the change one declaration and one rule of the walk, with no reader changed separately. | OBSERVED | HIGH | CLOSED | The vocabulary already declares a group of parts the walk passes over, the supersession parts. |
| Q2 | The data part is named for a vector's cases. The cases hold every value a case hands its transform and expects back, and the transform a vector tests sits beside them. | Leaves the vector's subject a reference, and every value it states a value. | OBSERVED | HIGH | CLOSED | The test-vector schema declares the target and the cases as siblings. |
| Q3 | A data part is declared by name, so the name chosen must mean data in every kind that uses it. Only vectors use a part named for cases. A part named for bindings would not do: a runtime binding's bindings name the capabilities it binds, and are references. | Rules out the name that reads most naturally and would break bindings everywhere. | OBSERVED | HIGH | CLOSED | 29 of 29 artifacts declaring cases are vectors; the representation declares a binding's bindings a keyed reference part. |
| Q4 | Adding a group changes what the vocabulary declares, so it is a new version, and every reader that names the vocabulary by its identity names the new one. | Makes the version change part of the delivery. | OBSERVED | HIGH | CLOSED | The build and the sameness comparison each read the vocabulary by its exact identity. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| A value written as a full name inside a vector's cases is refused as an undeclared reference. | S2 belief_verification #1 | CONFIRMED | Re-read: the vocabulary declares no part whose contents are values, and a vector naming an artifact in its cases is refused at each place. |
| Every reader that finds references reads one declaration of how a declaration is read. | S2 belief_verification #2 | CONFIRMED | Re-read: every reference finder reads the references the build's one walk yields. |
| No kind other than a test vector uses a part named for its cases. | S2 belief_verification #3 | CONFIRMED | Re-counted: 29 of 580 artifacts declare cases, all of them vectors. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The declaration of how a declaration is read | declaration | EXTEND | Declares reference, explanation, set and history parts; gains data parts. |
| The walk that finds references | mechanism | EXTEND | Passes over history parts; passes over data parts the same way. |
| The comparison that decides whether meaning changed | mechanism | EXTEND | Reads the declaration by its identity; reads the new version. |
| The governance of a vocabulary | declaration | REUSE | A new group is stated the way every group is. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | Superseded by a version that declares data parts; every other group is unchanged. | 580 | Every artifact in the composition is read by it. |
| Every test vector | Its cases are read as data; its target is read as a reference, as now. | 29 | 29 vectors in the composition. |
| Every other artifact | Read exactly as it is today: no part it uses is a data part. | 551 | No other kind declares cases. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Declaring a part whose contents are values | EXTEND | The vocabulary that declares how every part is read is where a new way of reading one belongs. | Exempting vectors by kind inside the build was rejected: it is an exemption nobody declared, against the rule that what names another artifact is declared, never inferred. Reading every unrecognised name as a value was rejected by the business: a misspelled reference would pass. | S2 gaps #1 |
| Passing over a data part when finding references | EXTEND | The walk already passes over history parts; a data part is passed over the same way. | A separate pass for vectors was rejected: two walks could disagree about what a reference is. | S2 architectural_observations #1 |
| Reading the new version wherever the vocabulary is read | EXTEND | A reader that named the old version would read a declaration that no longer stands. | None: the old version stands down. | S3 analysis_findings Q4 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | artifact | How a declaration is read belongs to the subdomain that already declares it. Vectors are what need it; the reading is not theirs to declare. | S2 belief_verification #2 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The one CRITICAL gap is resolved by declaring data parts. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the four raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Four dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Three items re-grounded; all three CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All four findings are OBSERVED. None rests on inference. |
