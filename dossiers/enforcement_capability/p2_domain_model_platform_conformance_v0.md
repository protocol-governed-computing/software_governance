# Stage 2 — Domain Model Discovery: platform / conformance
**Stage:** 2 — Domain Model Discovery
**CR:** enforcement_capability
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot and the compiler surface
it is built from. What was searched is recorded, not only what was found. Where a belief came back
narrower or wider than Stage 1 stated it, the correction is recorded against the belief.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Obligation | Something the platform requires of what it admits. | Declared as an artifact in the governance surface; 89 are published in the composition. | VERIFIED | S1 business_vocabulary #1 |
| Check | The mechanism that carries one obligation and decides whether it is met. | Not declared. Derived from the obligation when the composition is built, and bound to a module by name. | VERIFIED | S1 business_vocabulary #2 |
| Refusal | A check deciding an obligation is not met, and the admission not proceeding. | Recorded as a count against the check in the build's determination record. | VERIFIED | S1 business_vocabulary #3 |
| Capability to refuse | Whether there exists anything a check would refuse. | Held nowhere. It is a property of the check's text and of nothing the platform records. | NOT_FOUND | S1 business_vocabulary #4 |
| Enforcement status | What an obligation says about whether its check carries it today. | Partly held: every obligation declares how it responds to a violation. Nothing declares whether the check can produce one. | INSUFFICIENT_EVIDENCE | S1 business_vocabulary #5 |
| Delegation | An obligation carried somewhere other than where it is declared. | Held in the check's own prose. Two forms are declared as data; four are stated only in text. | VERIFIED | S1 business_vocabulary #6 |
| Determination record | The account of what a build decided and on what grounds. | Written per build, naming every check that ran and what it found. | VERIFIED | S1 requested_outcomes #6 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Obligation | Response to a violation | What happens when the obligation is not met. Declared by all 89: 88 say fail immediately, one says warn. | VERIFIED | S1 known_facts #1 |
| Obligation | Stage of enforcement | Where the obligation is carried. Five values are in use across the 89. | VERIFIED | S1 system_beliefs #6 |
| Obligation | Whether its check can refuse | Undeclared and unrecorded. | NOT_FOUND | S1 business_invariants #1 |
| Check | Whether it exists | A check named by an obligation and absent is refused when the composition is built. | VERIFIED | S1 known_facts #10 |
| Check | Whether it ran | Recorded per build for every check. | VERIFIED | S1 requested_outcomes #6 |
| Check | What it found | Recorded per build as a count of refusals. | VERIFIED | S1 requested_outcomes #6 |
| Delegation | Where the obligation is carried | Named in prose only. Not a field, not resolvable, not checked. | NOT_FOUND | S1 constraints #4 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Declaring an obligation | The subdomain that owns the concern | An obligation is published in the composition. | VERIFIED | S1 authority_boundaries #1 |
| Deriving its check | Building the composition | A check is synthesized from the obligation and bound to a module by name. | VERIFIED | S1 system_beliefs #1 |
| Executing the check | Building the composition | The check runs and reports what it found. | VERIFIED | S1 system_beliefs #1 |
| Recording the outcome | Building the composition | The determination record names every check that ran and its count of refusals. | VERIFIED | S1 requested_outcomes #6 |
| Establishing that an obligation is carried | Nobody | Nothing performs this. Existence is established; capability is not. | NOT_FOUND | S1 system_beliefs #1 |
| Counting what is unenforced | Nobody | Nothing performs this. | NOT_FOUND | S1 system_beliefs #5 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Deriving its check | 1 | Read the obligation and form the name of its check. | The check's identity. | VERIFIED | S1 system_beliefs #1 |
| Deriving its check | 2 | Skip the obligation if its stage says the check is carried elsewhere than the build. | Nothing; the obligation is not checked here by design. | VERIFIED | S1 system_beliefs #6 |
| Deriving its check | 3 | Bind the check to a module, by the obligation's own naming or by an override it declares. | The binding. | VERIFIED | S1 known_facts #10 |
| Deriving its check | 4 | Refuse the build if no module answers to that name. | A refusal naming the obligation. | VERIFIED | S1 known_facts #10 |
| Executing the check | 5 | Run it over what the build admits. | The count of refusals. | VERIFIED | S1 requested_outcomes #6 |
| Executing the check | 6 | Establish that something exists the check would have refused. | Nothing. No step does this. | NOT_FOUND | S1 known_facts #1 |
| Recording the outcome | 7 | Write the check's identity, whether it passed, and how many refusals it produced. | One row per check in the determination record. | VERIFIED | S1 requested_outcomes #6 |
| Recording the outcome | 8 | Write whether the check was capable of refusing. | Nothing. The record has no such column. | NOT_FOUND | S1 system_beliefs #5 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The obligation-to-check guarantee is satisfied by a check that cannot refuse. | VERIFIED | The guarantee holds by construction, not by counting: a check is derived from every obligation whose stage says the build carries it, so an obligation without a check is impossible and a check without an obligation is impossible. That construction establishes existence and says nothing whatever about capability. Fourteen derived checks ran in the pinned build, each reported no refusals, and each is indistinguishable in the record from the seventy-three that can refuse. **Stage 1 stated this as counting declarations; it is stronger than that, and the correction does not help — a guarantee by construction is no more able to see capability than a guarantee by count.** | S1 system_beliefs #1 |
| Fourteen checks cannot refuse anything. | VERIFIED | Eighty-seven checks were examined for any path that produces a refusal. Fourteen have none: those carrying the obligations on actor authority separation, authority required for execution, authority state well-formedness, conformance assertion mode validity, isolated capability side-effect execution, capability side-effect traceability, identity authority separation, no ambient authority, no runtime authorization, no runtime topology synthesis, no undeclared behavior surface, no workflow authorization logic, topology immutability after compilation, and trace authority binding. All fourteen executed in the pinned build and all fourteen passed. | S1 system_beliefs #2 |
| Ten of the fourteen declare a deferral in text nothing reads. | VERIFIED | Ten carry the words *"Phase 1 stub — full enforcement in Phase 3"* in their own prose. Nothing parses that prose, and the obligations above all ten declare that a violation fails the build immediately. The declaration and the text say opposite things and only the declaration is read. | S1 system_beliefs #3 |
| One obligation is declared as governance and its check only reports. | VERIFIED | The obligation forbidding unused capability-contract outputs declares its response to a violation as *warn* — the only one of eighty-nine that does. Its check returns warnings rather than refusals and reports passed. Its stated subject is *"code smell indicator"* and *"potential optimization opportunities"*. | S1 system_beliefs #4 |
| Nothing counts unenforced obligations. | VERIFIED | The build writes a determination record naming all eighty-seven checks that ran, each with whether it passed and how many refusals it produced. Every row of the pinned build reads passed, zero. The record has no column for whether a check could have refused, so the fourteen are unreachable from it. | S1 system_beliefs #5 |
| An obligation may be carried somewhere other than where it is declared. | VERIFIED | Two stages are declared as data and honoured: an obligation carried by a runtime outcome, and one carried by the assembler over the composed snapshot. Both cause the build to derive no check at all, deliberately, and the obligation remains governed by its own separate declaration. **Stage 1 said two of the fourteen delegate and both were verified; it is four, and they are not alike.** Three name a mechanism — one a phase of the compiler, two the runtime — and each was confirmed to exist. The fourth names *code review*, which is not a mechanism, and there is nothing to confirm. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Declares the response to a violation | governance::CONSTITUTION_INVARIANTS_V0 | Governs what every obligation must declare, including how it responds to a violation and where it is enforced. Five stages of enforcement are in use across the eighty-nine. | PARTIAL | Requires nothing about whether the check can produce a violation at all. Has no stage meaning *declared and not yet enforced*, and no way to carry the place a prose delegation names. |
| Governs what a check must be | conformance::CONSTITUTION_ASSERT_V0 | Defines the structure and semantics of a check, and names the obligations that carry its four rules. | MISMATCH | Two of its four rules name no mechanism at all — both say only that they are carried by process — and a third names the parity obligation, which never runs. The constitution that governs checks is itself half-carried. |
| Guarantees obligation-to-check parity | conformance::INVARIANT_ASSERT_PARITY_V0 | States that every obligation has exactly one check and every check exactly one obligation. | MISMATCH | Nothing carries it. Parity is now established by deriving the check from the obligation, and this obligation's check is excluded from derivation, so it never runs. It remains published and declares that a violation fails the build immediately. |
| Verifies a delegated obligation is wired | execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0 | Confirms that an obligation delegated to a runtime outcome is actually bound to one. | EXACT | Covers only the runtime-outcome stage; says nothing about the four delegations stated in prose. |
| Refuses a check that does not exist | compiler::INVARIANT_HANDLER_REGISTRY_CLOSED_V0 | Requires that every declared check has a registered implementation before the checking phase begins, and refuses the build otherwise. | PARTIAL | Establishes that a check exists. Establishes nothing about what it can do — its own text calls an unregistered check an "incomplete enforcement surface", which is exactly what a check that cannot refuse also is. |
| Declares a warning rather than a refusal | capability_contracts::INVARIANT_CC_NO_UNUSED_OUTPUTS_V0 | Declares that its violation warns rather than fails. | MISMATCH | It is admitted as an obligation while judging whether a thing is good rather than whether it is admissible. |

---

## 5. Gaps

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| An obligation cannot say whether its check carries it. | HIGH | Fourteen obligations claim their violation fails the build immediately, and none of the fourteen can produce a violation. The claim and the fact cannot be compared because only the claim is written down. | VERIFIED | S1 business_invariants #1 |
| Nothing establishes that a check can refuse. | HIGH | Correcting the fourteen leaves the fifteenth admissible. This is the gap that makes the change a mechanism rather than a cleanup. | VERIFIED | S1 constraints #1 |
| A delegation names its destination in prose. | MEDIUM | Four checks say where their obligation is carried, in text nothing reads. One of the four names code review, which no mechanism can confirm. A delegation nobody can follow is indistinguishable from an absence. | VERIFIED | S1 constraints #4 |
| The record of a build cannot answer how much is enforced. | MEDIUM | Every row of the pinned build reads passed with zero refusals, including all fourteen. Coverage is not derivable from the one surface that reports on every check. | VERIFIED | S1 requested_outcomes #6 |
| An obligation that judges quality is admitted as governance. | MEDIUM | One obligation declares that its violation warns. A violation that leaves the violation standing is a description, and the machinery that decides admissibility is being used to express a preference. | VERIFIED | S1 business_invariants #6 |
| The obligation stating the guarantee is itself carried by nothing. | HIGH | The parity obligation is published, declares that a violation fails the build immediately, and is excluded from check derivation, so it never runs. Its check module remains on disk and is never reached. **This is a fifteenth instance of the defect the change is about, found while verifying the change's own premise.** | VERIFIED | S1 system_beliefs #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Existence is governed strictly and capability is not governed at all. | An obligation naming a check that does not exist refuses the build and is recorded as having no check. An obligation naming a check that cannot refuse builds clean and is recorded as having passed. The two failures are one step apart and are treated oppositely. | VERIFIED | S1 known_facts #2 |
| The parity obligation was superseded by a mechanism and not retired. | Parity now holds because the check is derived from the obligation. The obligation that used to establish parity by comparison was excluded from derivation rather than withdrawn, leaving a published obligation with no carrier and a check module with no caller. | VERIFIED | S1 system_beliefs #1 |
| Every check names its module in a namespace that no longer exists. | All eighty-seven bindings are stated under the legacy reference implementation's package path. The names resolve because the binding is by string against a registry, not by import, so nothing is broken — but the identity every obligation gives its check is stale. | VERIFIED | S1 assumptions #2 |
| The record of a build reports on every check and cannot distinguish them. | The determination record names all eighty-seven checks that ran, each with whether it passed and how many refusals it produced. Every row of the pinned build reads passed with zero refusals. The record has no column for capability, so a check that cannot refuse and a check that found nothing to refuse are the same row. | VERIFIED | S1 requested_outcomes #6 |
| Deferral was recorded honestly in the only place available. | Ten authors wrote the deferral into the check's own prose. There was no field to put it in. The absent declaration surface, not the authors, is what made the deferral invisible. | VERIFIED | S1 assumptions #1 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Fourteen is a floor and the ceiling is not established. | The fourteen were found by looking for checks with no refusal path at all. A check with a refusal path that cannot be reached by its own obligation is counted as capable. One such was found by reading rather than by measuring, and no method now in use would find a second. | HIGH | VERIFIED | S1 known_facts #9 |
| Capability may not be decidable for every check. | Fourteen were settled by inspecting the check alone. The fifteenth needed its obligation read alongside it to see that its only refusal path guards its own inputs. Whether a general rule can decide this for every check is not established. | MEDIUM | INSUFFICIENT_EVIDENCE | S1 assumptions #2 |
| A delegation to a mechanism and a delegation to a practice were written the same way. | Three of the four delegations name something that exists and can be pointed at. The fourth names code review. Both are a sentence in a docstring, and nothing distinguishes them. | MEDIUM | VERIFIED | S1 constraints #4 |

---

## 8. Open Questions

<!-- register:open_questions business_language -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Does an obligation carried by a phase of the compiler rather than by its own check count as enforced, or as enforced elsewhere? | GOVERNANCE | Discovery sharpened this rather than answering it. Three delegations were found and they point at three different kinds of place: a phase of the compiler, the runtime, and a practice. Whether these are one status or several decides the shape of the declaration. | S1 clarification_requests #1 |
| Is the parity obligation retired, or is it an obligation still wanted whose carrier was replaced? | GOVERNANCE | It is published, unenforced and superseded by a mechanism. If it is wanted, it needs a carrier; if it is not, it needs retiring. Either way it must stop being a published obligation that nothing carries. | S1 system_beliefs #1 |
