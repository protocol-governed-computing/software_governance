# Stage 2 — Domain Model Discovery: platform / artifact
**Stage:** 2 — Domain Model Discovery
**CR:** data_parts
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, the declaration of how a
declaration is read, and the readers that find references. What was searched is recorded, not only
what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Declaration | What an artifact states, read the same way by every reader. | One per artifact, in its own source. | VERIFIED | S1 business_vocabulary #1 |
| Part | A named place in a declaration, read the way the platform declares. | Declared once, by name, for every kind. | VERIFIED | S1 business_vocabulary #2 |
| Data part | A part whose contents are values, never read for references. | Nothing declares one. | NOT_FOUND | S1 business_vocabulary #4 |
| Test vector | A statement of what a transform is handed and what it must return. | Twenty-nine in the composition. | VERIFIED | S1 business_vocabulary #5 |
| Case | One stated input and its expected result, within a test vector. | Held in the vector's cases. | VERIFIED | S1 business_vocabulary #6 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Part | How it is read | A reference, an explanation, a set, history, or data. | VERIFIED | S1 known_facts #1 |
| Test vector | The transform it tests | A reference, outside its cases. | VERIFIED | S1 known_facts #9 |
| Case | What it hands the transform | Values. | VERIFIED | S1 known_facts #5 |
| Case | What it expects back | Values. | VERIFIED | S1 known_facts #5 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Reading a declaration | The platform, when it builds a composition | Every reference found and resolved; any other name refused. | VERIFIED | S1 known_facts #2 |
| Proving a transform | The platform, when it builds a composition | Each case run, and its result compared with what the case expects. | VERIFIED | S1 known_facts #7 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Reading a declaration | 1 | Walk every part of the declaration. | The names it holds. | VERIFIED | S1 known_facts #1 |
| Reading a declaration | 2 | Pass over a part that records history. | Nothing. | VERIFIED | S1 known_facts #4 |
| Reading a declaration | 3 | Take a name in a reference part as a reference, and refuse a name anywhere else. | The references, or a refusal. | VERIFIED | S1 known_facts #2 |
| Proving a transform | 1 | Hand the transform each case's inputs. | The transform's result. | VERIFIED | S1 known_facts #5 |
| Proving a transform | 2 | Compare the result with what the case expects. | Proven, refused or unproven. | VERIFIED | S1 known_facts #7 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| A value written as a full name inside a vector's cases is refused as an undeclared reference. | VERIFIED | A vector for a transform that renders artifacts, whose expected result carries the constitution governing the artifact it renders, is refused when its domain builds: the build reports an undeclared reference at each place in its cases where a full name is written. `artifact::VOCAB_DECLARATION_REPRESENTATION_V0` declares reference parts and supersession parts, and no part whose contents are values. | S1 system_beliefs #1 |
| Every reader that finds references reads one declaration of how a declaration is read. | VERIFIED | `artifact::VOCAB_DECLARATION_REPRESENTATION_V0` is the declaration. The build reads it once and every place that finds a reference — extraction, surface closure, the superseded-not-referenced and full-name-only checks — reads the references it yields. Nothing else decides what a reference is. | S1 system_beliefs #2 |
| No kind other than a test vector uses a part named for its cases. | VERIFIED | Of 580 artifacts in the pinned composition, the 29 that declare cases are all test vectors, and only the test-vector schema declares the part. | S1 system_beliefs #3 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Declares how a declaration is read | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | Declares the parts that explain, the lists read as sets, the reference parts and the history parts. | PARTIAL | Declares no part whose contents are values. |
| Governs a vocabulary | vocabulary::CONSTITUTION_VOCABULARY_V0 | Declares what a vocabulary is and how its groups are stated. | EXACT | Nothing. A new group is stated the way every group is. |
| Governs a test vector | conformance::CONSTITUTION_TEST_DATA_V2 | Declares what a vector states and how a transform is proven by it. | EXACT | Says nothing about how a vector's cases are read for references. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing declares a part whose contents are values. | CRITICAL | A vector whose data names an artifact cannot be built, so the transforms whose data must name artifacts cannot be proven. | VERIFIED | S1 system_beliefs #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A part that names without reaching is already declared and already passed over: the supersession parts. A data part is read the same way, so no reader needs a new mechanism, only a new group. | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 declares `supersession`, and the walk that finds references passes over it. | VERIFIED | S1 known_facts #4 |
| One declaration and one walk decide what a reference is for every reader, so declaring a data part changes every reader at once and none separately. | Every reference finder reads the references the build's one walk yields. | VERIFIED | S1 system_beliefs #2 |
| The transform a vector tests sits outside its cases, so declaring the cases data leaves the test's subject a reference. | The test-vector schema declares the target beside the cases, not within them. | VERIFIED | S1 system_beliefs #3 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A part is declared by its name across every kind, so a data part named for cases would be data wherever the name appears. Today only vectors use it. | 29 of 29 artifacts declaring cases are test vectors. | MINOR | VERIFIED | S1 system_beliefs #3 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
