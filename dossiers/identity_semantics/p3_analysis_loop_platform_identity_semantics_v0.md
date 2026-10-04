# Stage 3 — Analysis Loop: platform / identity semantics

**Stage:** 3 — Analysis Loop

**CR:** identity_semantics

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The two gaps carried from Stage 2 are driven to committed decisions against the pinned composition.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | One vocabulary of the artifact subdomain declares both groups: the parts that only explain, and the lists whose order carries no meaning. | One place, read by any comparison. | OBSERVED | HIGH | CLOSED | S2 gaps #1; S2 gaps #2 |
| Q2 | A part is named in the explanation group only where every occurrence in the composition only explains; prose that is data stays out. | Nothing that carries meaning is exempted by name. | OBSERVED | HIGH | CLOSED | S2 architectural_observations #1; S1 constraints #2 |
| Q3 | A list is named in the unordered group only where every occurrence is read as a set; a list announced or run in order stays out. | Nothing whose order decides is exempted. | OBSERVED | HIGH | CLOSED | S2 architectural_observations #2 |
| Q4 | A name later reused for data is caught by review, because adding to or relying on the declaration is a reviewed change. | The concern is owned, not open. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #1; S1 known_facts #3 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| Nothing in the platform declares which parts of a declaration are explanation. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 |
| Some lists are written in an order that carries no meaning. | S2 belief_verification #2 | CONFIRMED | Resolved in Q1 and Q3 |
| A part named the same way in two places could mean different things. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q4 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| The declaration of what carries no meaning | Vocabulary | AUTHOR_NEW | No vocabulary classifies the parts of a declaration |
| Governing vocabularies | Constitution | REUSE | vocabulary::CONSTITUTION_VOCABULARY_V0, unchanged |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| vocabulary::CONSTITUTION_VOCABULARY_V0 | Governs one more vocabulary; unchanged | 0 | si.topology.impact impacted_count 0; a constitution is applied, not referenced |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Declare what carries no meaning | AUTHOR_NEW | One vocabulary, two groups, in the artifact subdomain that owns identity. | Two vocabularies were rejected: the two groups answer one question for one reader. | S3 analysis_findings Q1 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | artifact | What an identity stands for is the artifact subdomain's. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | No CRITICAL gap was raised; both MAJOR gaps resolve in Q1 |
| No open analyst questions | SATISFIED | All four findings are CLOSED |
| No dependency expansion in the last pass | SATISFIED | A second survey of the composition's lists added no candidate |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All three items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
