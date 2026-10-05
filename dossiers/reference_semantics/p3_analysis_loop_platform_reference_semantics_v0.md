# Stage 3 — Analysis Loop: platform / reference semantics

**Stage:** 3 — Analysis Loop

**CR:** reference_semantics

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The three gaps and two concerns carried from Stage 2 are driven to committed decisions against the
pinned composition. A fourth place that decides what a reference is was found and is resolved here.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The declaration of what carries no meaning gains the groups that say which parts name another artifact: the parts whose full names are references, the parts whose keys are, the reference parts where a short code is refused, and the parts that declare supersession. | One place says what a reference is, beside what carries no meaning. | OBSERVED | HIGH | CLOSED | S2 gaps #1 |
| Q2 | A fourth place decides it too. artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0 refuses a short code in governed_by, structure, runtime_binding and a contract step's transform, each listed by its handler. The record of references refuses a short code in its own nine parts. Both read the group of parts where a short code is refused, and the record only records. | One rule, one place it is enforced, one list it reads. | OBSERVED | HIGH | CLOSED | S2 gaps #2 |
| Q3 | The record of references reads every full name at or beneath a reference part, and the keys of a part whose keys are references. A full name anywhere else is refused, except in the artifact's own identity and in a supersession part. | The record is whole; inspection reports every artifact that names another. | OBSERVED | HIGH | CLOSED | S2 gaps #1; S2 belief_verification #4 |
| Q4 | The reach check reads the reference parts for full names and the supersession parts from the declaration. It keeps finding a short code anywhere, because nothing else guards a short-code reference and declaring short codes is later work. | The check sees no less than it does today. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #1 |
| Q5 | Text is a sentence or a list of sentences. Explanation is exempt only where its value is text, so the data test cases write under description and summary carries meaning. | No data is ignored when two declarations are compared. | OBSERVED | HIGH | CLOSED | S2 gaps #3; S2 architectural_observations #1 |
| Q6 | The two rules a comparison applies are declared as named entries of their own group, so the comparison can refuse to run when the declaration names a rule it does not apply. A meaning written only in prose is not sealed. | The rules are declared, not described. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #2 |
| Q7 | Adding the groups is a change of meaning, so the declaration is replaced by a new version. Nothing names the old one, so nothing is re-pointed. | The change follows the rule it serves. | OBSERVED | HIGH | CLOSED | S1 known_facts #5 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The record of references reads a fixed list of parts and misses most of them. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 and Q3 |
| The check that nothing reaches a stood-down artifact reads every value that looks like a name. | S2 belief_verification #2 | CONFIRMED | Resolved in Q4 |
| No part of a declaration declared explanation holds anything but text today. | S2 belief_verification #3 | OVERTURNED | Eight test-data values are data; resolved in Q5 |
| Every full name in the composition sits in a part that can be declared a reference. | S2 belief_verification #4 | CONFIRMED | Resolved in Q3 |
| Narrowing the reach check to declared parts would stop it seeing short codes. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q4 |
| A rule written only in prose cannot be read by the comparison that applies it. | S2 discovery_concerns #2 | CONFIRMED | Resolved in Q6 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| The declaration of what carries no meaning | Vocabulary | AUTHOR_NEW | Replaced by a new version; artifact::VOCAB_DECLARATION_REPRESENTATION_V0 is stood down |
| Governing vocabularies | Constitution | REUSE | vocabulary::CONSTITUTION_VOCABULARY_V0, unchanged |
| Keeping a stood-down artifact out of reach | Invariant | REUSE | artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0; its obligation is unchanged and its check reads the declaration |
| Refusing a short-code reference | Invariant | REUSE | artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0; its obligation is unchanged and its check reads the declaration |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | Stood down; nothing names it | 0 | si.artifact.refs ref_count 0, and no declaration in the composition holds its name |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Declare what names another artifact | AUTHOR_NEW | A new version of the declaration of what carries no meaning, with the reference groups and the rules beside the groups it already holds. | A separate declaration of references was rejected: a comparison reads both, and two places would drift. | S3 analysis_findings Q1 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | artifact | What an identity names, and what reaches it, is the artifact subdomain's. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The CRITICAL gap resolves in Q1 and Q3 |
| No open analyst questions | SATISFIED | All seven findings are CLOSED |
| No dependency expansion in the last pass | SATISFIED | A second search for places that decide what a reference is found none beyond the four |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | The one OVERTURNED item resolves in Q5 |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
