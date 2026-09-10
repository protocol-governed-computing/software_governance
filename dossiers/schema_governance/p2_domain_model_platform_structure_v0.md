# Stage 2 — Domain Model Discovery: platform / structure
**Stage:** 2 — Domain Model Discovery
**CR:** schema_governance
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned composition and the schemas beside
it. What was searched is recorded, not only what was found. Where a belief came back narrower or
wider than Stage 1 stated it, the correction is recorded against the belief.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Kind | A class of artifact the platform builds. | Fifteen appear in the composition, carrying 428 artifacts. | VERIFIED | S1 business_vocabulary #5 |
| Description | A statement of what a declaration of one kind may contain. | Twenty-five files sit beside the registry. Eleven govern a kind; the rest describe something else. | VERIFIED | S1 business_vocabulary #2 |
| Dispatch | The table naming which description governs which kind. | One table, ten rows, read by the build. | VERIFIED | S1 business_vocabulary #3 |
| Closed surface | A description admitting only what it names. | Twenty of twenty-five close; five do not. | VERIFIED | S1 business_vocabulary #4 |
| Exemption | A kind recorded as needing no description, with the ground stated. | Does not exist. No kind is recorded as exempt, and no place records one. | NOT_FOUND | S1 known_facts #13 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Kind | Whether it is dispatched | Ten of fifteen are. Five are not. | VERIFIED | S1 known_facts #1 |
| Kind | Whether a description exists for it | Thirteen of fifteen have one. The two transport boundary kinds do not. | VERIFIED | S1 known_facts #9 |
| Description | Whether it closes its surface | Twenty do. Five state nothing about what may appear beside what they name. | VERIFIED | S1 known_facts #10 |
| Description | Whether it matches what it describes | Three do not, and each stopped matching at a change nobody applied to it. | VERIFIED | S1 known_facts #5 |
| Description | Whether it describes an artifact kind at all | Four describe runtime data rather than a declaration, and are dispatched by nothing for that reason. | VERIFIED | S1 known_facts #10 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Selecting a description for a declaration | The build | The declaration is checked, or it is not. | VERIFIED | S1 system_beliefs #1 |
| Checking a declaration | The build | The declaration conforms, or the build refuses. | VERIFIED | S1 business_events #1 |
| Recording that a kind needs no description | Nobody | Nothing performs this, and nothing holds the record. | NOT_FOUND | S1 lifecycle_states #2 |
| Reporting a description that has stopped matching | Nobody | Nothing performs this. A description is found stale only by dispatching it. | NOT_FOUND | S1 system_beliefs #4 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Selecting a description for a declaration | 1 | Read the kind from the declaration itself. | Nothing. | VERIFIED | S1 system_beliefs #1 |
| Selecting a description for a declaration | 2 | Look the kind up in the dispatch table. | Nothing. | VERIFIED | S1 system_beliefs #1 |
| Selecting a description for a declaration | 3 | Skip the declaration where the table names no description. | Nothing. Silence is indistinguishable from conformance. | VERIFIED | S1 known_facts #1 |
| Checking a declaration | 4 | Compare it against the description and collect what does not conform. | A refusal, or nothing. | VERIFIED | S1 business_events #1 |
| Checking a declaration | 5 | Ask whether the description still matches the kind it describes. | Nothing. No step performs this. | NOT_FOUND | S1 business_events #3 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The dispatch table is the sole authority for which kind is described by what. | VERIFIED | One table maps a kind to a description, and the build's own account says the kind read from the declaration is "the sole authority for schema selection". Nothing selects a description another way, and a kind absent from the table is skipped in silence. | S1 system_beliefs #1 |
| The four unnamed descriptions rotted at a namespace change and not before. | INSUFFICIENT_EVIDENCE | Every one of the sixty-two constitution mismatches is consistent with the namespace change, and the remaining thirty-eight are not: an actor with a role and no attributes, an event forbidding content it carries, and a type list omitting whole numbers describe shapes that changed at three different times nobody recorded. **Staleness is continuous drift, not one event.** | S1 system_beliefs #2 |
| Every one of the hundred refusals is the description being wrong. | VERIFIED | Each of the four shapes was compared against what the platform builds today. The artifacts are what every green build produces and what the runtime executes; the descriptions are what nobody has read since they were written. | S1 system_beliefs #3 |
| Nothing reports a description that has stopped matching. | VERIFIED | No check compares a description against the artifacts of its kind. A description is found stale by dispatching it and reading the refusals, which is how all one hundred were found. | S1 system_beliefs #4 |
| Not every artifact kind requires a description. | VERIFIED | Ruled by the business author. Nothing in the composition records an exemption, so the ruling has no place to be written down yet. | S1 system_beliefs #5 |
| Closing an open surface refuses nothing that is currently built. | NOT_FOUND | **Stage 1 counted five open surfaces as one kind of thing and they are two.** One is the description of an artifact kind: it names nothing, requires nothing and closes nothing, so the kind dispatched to it is checked against a description that describes nothing — the dispatch is a formality. The other four describe **runtime data, not declarations** — an authority state, an authority registry, an authenticated authority state and a trace event are none of them artifact kinds in this composition. They are dispatched by nothing because there is nothing to dispatch them to. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Names which description governs which kind | structure::STRUCTURE_SCHEMA_DISPATCH_V0 | Maps an artifact kind to the description that governs it. Read by the build; the sole authority for selection. | PARTIAL | Names ten of fifteen kinds. A kind absent from it is skipped in silence, and the table cannot say a kind is exempt rather than forgotten. |
| Refuses a declaration that does not conform | artifact::INVARIANT_SCHEMA_CONFORMANCE_V0 | Checks each declaration against the description its kind is dispatched to, and refuses the build on a violation. | EXACT | Nothing. It refuses correctly; it is only ever handed ten kinds. |
| Governs what a structural declaration is | structure::CONSTITUTION_STRUCTURE_V0 | States what the structure subdomain governs, including the dispatch. | PARTIAL | Says nothing about whether a kind must be described, nor about what makes a description current. |
| Governs what a structural declaration is | structure::CONSTITUTION_STRUCTURE_V0 | Named again because the description the structure kind is dispatched to requires no field and closes no surface, so the thirty-three artifacts dispatched to it are checked against a description that admits anything. | MISMATCH | Says nothing about what a description must state to count as one. |
| Governs what an execution trace records | trace::CONSTITUTION_TRACE_EXECUTION_V0 | Governs the runtime trace. Named because four of the five descriptions counted as failing to close a surface describe runtime data of this sort, not declarations, and are dispatched by nothing for that reason. | EXACT | Nothing; it is unchanged by this and is named to separate two populations that share a directory. |

---

## 5. Gaps

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Five kinds are dispatched to nothing, and silence reads as conformance. | HIGH | 106 artifacts are checked against nothing, and no reader can tell that from their having been checked and passed. | VERIFIED | S1 known_facts #1 |
| Three descriptions have drifted from what they describe. | HIGH | Dispatching them refuses one hundred correct declarations. The descriptions are wrong and would refuse with the authority of a rule. | VERIFIED | S1 known_facts #5 |
| The two transport boundary kinds have no description. | HIGH | Forty-four artifacts carrying the surface a caller reaches the composition through are described by nothing that could be dispatched. | VERIFIED | S1 known_facts #9 |
| One dispatched description describes nothing. | MEDIUM | The structure kind is dispatched and thereby appears governed. It is checked against a description requiring no field and closing no surface. **Dispatch without a description that describes is worse than no dispatch, because it reads as coverage.** | VERIFIED | S1 known_facts #11 |
| No kind can be recorded as exempt. | MEDIUM | The business author has ruled that exemption is admissible with a stated ground, and there is nowhere to state one. An exempt kind and a forgotten kind are the same absence. | VERIFIED | S1 business_invariants #1 |
| Nothing reports a description that has stopped matching. | HIGH | Every instance here was found by dispatching and reading the wreckage. Without a report, the next drift is found the same way. | VERIFIED | S1 system_beliefs #4 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A description nobody reads rots exactly as a profile nobody reads rots. | Four descriptions written, never named by the table, and wrong about the shape they describe. The same shape as a published conformance profile whose required artifacts stopped resolving. Neither was found wrong, because being unread is what prevents being found wrong. | VERIFIED | S1 known_facts #12 |
| Coverage and governance are not the same measure. | Dispatching four descriptions raised coverage from ten kinds to fourteen and would have refused one hundred correct declarations. The structure kind is dispatched and governed by a description that describes nothing. **Both directions of the error are present in one composition.** | VERIFIED | S1 known_facts #14 |
| The schema directory holds two populations and names them alike. | Eleven describe an artifact kind's declaration. Four describe runtime data — an authority state, a registry, an authenticated state, a trace event. They share a naming convention and a directory, and nothing distinguishes them, which is why four of them were counted as artifact-kind descriptions that failed to close. | VERIFIED | S1 system_beliefs #6 |
| The absence of a kind from the dispatch table carries no meaning. | A kind is absent because nobody wrote a description, because a description exists and nobody named it, or because the kind needs none. Three different facts, one representation. | VERIFIED | S1 lifecycle_states #3 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Staleness is continuous, so a correction made once decays. | The hundred refusals span at least three separate divergences, none recorded when it happened. Correcting the three descriptions restores them to today and does nothing about tomorrow. | HIGH | VERIFIED | S1 system_beliefs #2 |
| Every dispatched description was validated only against what is built, never against what should be refused. | A description that admits everything passes every artifact, which is exactly what the structure description does. Conformance measured only by "nothing was refused" cannot distinguish a good description from an empty one. | HIGH | VERIFIED | S1 known_facts #11 |
| Whether the two transport kinds need describing is not established. | They carry forty-four artifacts and a boundary contract's surface is the one a caller depends on, which argues for describing them. Nothing has decided it, and this change must not decide it by writing one. | MEDIUM | VERIFIED | S1 known_facts #9 |

---

## 8. Open Questions

<!-- register:open_questions business_language -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Where a description has drifted, does it move to the artifacts or is the shape reconsidered? | GOVERNANCE | Carried from the seed and sharpened: the drift is not one event but at least three, so the question is asked once per divergence rather than once. | S1 clarification_requests #1 |
| Do the four runtime-data descriptions belong beside the artifact-kind descriptions at all? | GOVERNANCE | They were counted as failures to close a surface because they sit in the same directory under the same naming convention. Separating them would make the count of artifact-kind descriptions readable without measuring. | S2 architectural_observations #3 |
