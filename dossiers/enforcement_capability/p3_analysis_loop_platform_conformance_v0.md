# Stage 3 — Analysis Loop: platform / conformance
**Stage:** 3 — Analysis Loop
**CR:** enforcement_capability
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

The two questions Stage 2 left open, closed against the pinned composition; every belief it verified,
re-grounded rather than carried.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | **A compiler phase and the runtime are the same status and different destinations.** The distinction the question asks about already exists as data and is already load-bearing: an obligation declares where it is enforced, and two of the five declared places route it away from the build entirely, so no check is derived for it and none is expected. What is missing is not a status but the destination. An obligation carried elsewhere says only that it is carried elsewhere; it cannot say where, so nothing can be followed and nothing can be confirmed. | Settles the shape of the declaration: one status for carried-elsewhere, with the place named. Not three statuses for three kinds of place. | OBSERVED | HIGH | CLOSED | Five places are declared across the eighty-nine obligations. Two of them — a runtime outcome, and the assembler over the composed snapshot — cause the build to derive no check, deliberately. The other three derive one. The two that route away are honoured; neither names a destination beyond its own name. |
| Q2 | **The parity obligation is superseded, not abandoned.** What it asserted — one check per obligation, one obligation per check — is now guaranteed by construction: the check is derived from the obligation, so an obligation without a check cannot exist and a check without an obligation cannot exist. The obligation's content holds more strongly than when it was checked by comparison. What is wrong is that it still reads as a compile-time obligation, is excluded from derivation by name, and leaves a check module nothing reaches. | Resolves it as the same answer as Q1: it is carried elsewhere, and the place is the derivation step. It is restated, not retired, and its dead check module is withdrawn. | OBSERVED | HIGH | CLOSED | The check is derived for every obligation whose declared place is the build; this obligation is excluded by an explicit list of obsolete derivations. It declares that a violation fails the build immediately, and nothing evaluates it. Its check module is present on disk and is called by nothing. |
| Q3 | **A constitution can name a carrier that does not exist and nothing objects.** The constitution governing checks names the carrier of each of its four rules. One names the parity obligation, which never runs; two name no carrier at all, saying only that they are carried by process. Those names are not references the composition traverses: the parity obligation has zero consumers in the graph despite being named by the constitution above it. | Widens the change from obligations to the constitutions that name them, and explains why the defect was undetectable rather than merely undetected. | OBSERVED | HIGH | CLOSED | `conformance::CONSTITUTION_ASSERT_V0` declares four rules; their carriers are the parity obligation, the not-runtime-referenced obligation, and twice the literal statement that the rule is carried by process. `conformance::INVARIANT_ASSERT_PARITY_V0` reports a consumer count of zero. |
| Q4 | **Capability is decidable for a check that has no refusal path, and not decidable in general.** Fourteen were settled by inspecting the check alone: no path within it produces a refusal, so no input can make it refuse. The fifteenth has a refusal path and it guards the check's own inputs rather than the obligation, which is visible only by reading the obligation alongside the check. The first is a property of the check; the second is a relation between two artifacts. | Fixes what the change can require. It can refuse a check with no refusal path at all. It cannot decide, in general, whether a refusal path can be reached by the obligation it belongs to. | OBSERVED | HIGH | CLOSED | Fourteen of eighty-seven have no refusal-producing path. The fifteenth's only such path fires when its input is absent from the compilation context, and its obligation is about unused outputs, which that path cannot express. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| The obligation-to-check guarantee is satisfied by a check that cannot refuse. | S2 belief_verification #1 | CONFIRMED | The guarantee holds by derivation and establishes existence only. Fourteen derived checks ran in the pinned build and every one reported passed with zero refusals. |
| Fourteen checks cannot refuse anything. | S2 belief_verification #2 | CONFIRMED | Re-counted over the eighty-seven: fourteen have no path producing a refusal, and all fourteen appear in the pinned build's record as passed. |
| Ten of the fourteen declare a deferral in text nothing reads. | S2 belief_verification #3 | CONFIRMED | Ten carry the deferral in their own prose. All ten obligations above them declare that a violation fails the build immediately. |
| One obligation is declared as governance and its check only reports. | S2 belief_verification #4 | CONFIRMED | One of eighty-nine declares that its violation warns. Its check returns warnings and reports passed, and it has zero consumers. |
| Nothing counts unenforced obligations. | S2 belief_verification #5 | CONFIRMED | The pinned build's record has eighty-seven rows, every one passed with zero refusals, and no column in which capability could appear. |
| An obligation may be carried somewhere other than where it is declared. | S2 belief_verification #6 | CONFIRMED | Two places route the obligation away from the build as data and are honoured. Four further delegations are stated in prose only; three name a mechanism and one names code review. |
| Two obligations are carried by nothing at all. | S2 gaps #6, S3 Q3 | CONFIRMED | The parity obligation is published, declares that a violation fails the build immediately, is excluded from derivation, and has zero consumers. Two rules of the constitution above it name no carrier. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The declaration of where an obligation is enforced | governance | EXTEND | Five places are declared and honoured. The change adds a place meaning *declared and not yet enforced*, and a destination for the places that route elsewhere. |
| The constitution governing obligations | governance | EXTEND | It requires every obligation to declare how it responds to a violation. The change adds the requirement that the claim be true of the check. |
| The refusal of a check that does not exist | governance | REUSE | An obligation naming a check no module answers to already refuses the build and is recorded as having no check. The change refuses a check that cannot refuse by the same means, at the same point. |
| The derivation of a check from its obligation | capability | EXTEND | Every check is derived at one place in the build. That place already reads the obligation, already knows the check's module, and is where capability can be established before the check runs. |
| The record of what each check found | data | EXTEND | The build writes a row per check. The change adds what the row cannot presently say. |
| The verification that a delegated obligation is wired | governance | REUSE | An obligation delegated to a runtime outcome is already confirmed to be bound to one. The change applies the same treatment to the other destinations. |
| The constitution governing checks | governance | EXTEND | It names the carrier of each of its rules, and two of the four name none. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| governance::CONSTITUTION_INVARIANTS_V0 | Every obligation in the composition. Adding a required declaration reaches all of them. | 47 | Reported by the composition for the platform surface; the whole composition carries eighty-nine obligations governed by it. |
| conformance::CONSTITUTION_ASSERT_V0 | The rules governing what a check must be. Two of its four rules name no carrier. | 1 | Reported by the composition. |
| conformance::INVARIANT_ASSERT_PARITY_V0 | Nothing. It is referenced by no artifact and evaluated by no build. | 0 | Reported by the composition. |
| capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0 | Nothing. Withdrawing it as an obligation reaches no consumer. | 0 | Reported by the composition. |
| The fourteen obligations whose checks cannot refuse | Each is restated to say what its check does. No consumer of any of them changes. | 0 each | None is referenced by another artifact; each is reached only by the build that derives its check. |
| The derivation step of the build | Every obligation, on every build, in every domain. | — | It is the single place a check is derived, and it already refuses an obligation whose check does not exist. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|-----------|----------|-----------|---------------------|----------------|
| Declaring whether an obligation is enforced | EXTEND | The place of enforcement is already declared by every obligation and already honoured. Adding a value is smaller than adding a field, and puts the deferral where a reader already looks. | A separate field for enforcement status was considered and rejected: two fields that must agree is the defect this change is about. | analysis_findings #1 |
| Naming where a delegated obligation is carried | AUTHOR_NEW | Nothing carries a destination today. Four delegations are prose, and prose is what made them unfollowable. | Reusing the place-of-enforcement value as the destination was checked and rejected: it names a kind of place, not a place. | analysis_findings #1 |
| Refusing a check that cannot refuse | EXTEND | The build already refuses an obligation whose check does not exist, at the point the check is derived. Capability is established at the same point, from the same two things. | A separate pass over the checks was considered and rejected: it would run after the build had already admitted them. | analysis_findings #4 |
| Counting what is unenforced | EXTEND | The build already writes a row per check. What the count needs is a column, not a surface. | A new inspection operation was considered and rejected as premature: the record is the thing every build already produces. | S2 gaps #4 |
| Withdrawing the obligation that judges quality | AUTHOR_NEW | It is the only obligation of eighty-nine declaring that its violation warns, it has no consumers, and its subject is whether a thing is good. | Making its check refuse was considered and rejected: that would enforce a preference as though it were a rule. | S2 gaps #5 |
| Restating the parity obligation | REUSE | Its content is guaranteed by the derivation step. It is restated to say so, and its dead check module is withdrawn. | Retiring it was considered and rejected: what it asserts is true and worth declaring. | analysis_findings #2 |

---

## 6. Placement Decision

<!-- register:placement_decision -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | conformance | The relation between an obligation and the check that carries it is what this subdomain governs. What the change adds is a further requirement on that relation. | S1 governance_scope #1 |

---

## 7. Discovery Saturation

<!-- register:saturation -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| Every question Stage 2 left open is closed. | SATISFIED | Both resolve to one answer: carried elsewhere is one status, and the place must be named. Two further questions were raised and closed in this pass. |
| Every belief Stage 2 verified was re-grounded. | SATISFIED | All six confirmed against the pinned composition and the pinned build's record; none overturned. A seventh was added and confirmed. |
| The count of the defect is established. | SATISFIED | Fourteen checks with no refusal path, one whose refusal path cannot reach its obligation, and two obligations carried by nothing. Seventeen instances over eighty-nine obligations. |
| The ceiling of the defect is understood, if not measured. | SATISFIED | Capability is decidable for a check with no refusal path and not decidable in general. The change requires what can be decided and declares what cannot. |
| Nothing further is needed to state what the change does. | SATISFIED | The declaration surface, the point of refusal, the counting surface and the destination of a delegation are all established against existing mechanisms. |
