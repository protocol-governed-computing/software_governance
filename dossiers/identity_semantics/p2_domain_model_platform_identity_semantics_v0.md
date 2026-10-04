# Stage 2 — Domain Model Verification: platform / identity semantics

**Stage:** 2 — Domain Model Verification
**CR:** identity_semantics
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. The
vocabularies were read for any that classifies parts of a declaration, and every declaration in the
composition was read for the lists it writes and the parts that hold prose.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Declaration | What an artifact states about itself, in the form the platform reads. | Sealed in the composition; not stored by this change. | OBSERVED | S1 business_vocabulary #1 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Declaration | Its parts | Each part is a named value; some explain, some commit the artifact, and some are lists read as sets. | OBSERVED | S2 belief_verification #2 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Declare what carries no meaning | The platform owner | One declaration names the explanation parts and the unordered lists. | OBSERVED | S1 requested_outcomes #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Declare what carries no meaning | 1 | Name the parts of a declaration that only explain. | The declaration's first group. | OBSERVED | S1 requested_outcomes #1 |
| Declare what carries no meaning | 2 | Name the lists whose order carries no meaning. | The declaration's second group. | OBSERVED | S1 requested_outcomes #2 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Nothing in the platform declares which parts of a declaration are explanation. | VERIFIED | The platform's vocabularies, among them vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V1 and conformance::VOCAB_ENFORCEMENT_STATUS_V0, classify trace content and enforcement places; none classifies the parts of a declaration. | S1 system_beliefs #1 |
| Some lists are written in an order that carries no meaning. | VERIFIED | Outcome lists such as a contract's allowed outcomes and a step's answered outcomes are read as sets by the compiler and the runtime; the same contract was rendered once with its allowed outcomes in another order and meant the same. | S1 system_beliefs #2 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Classifying content | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V1 | Names which trace content determines and which only observes. | MISMATCH | It classifies trace lines, not the parts of a declaration. |
| Governing vocabularies | vocabulary::CONSTITUTION_VOCABULARY_V0 | Governs what a vocabulary declares and how its entries are written. | EXACT | Nothing for this purpose; it governs the new declaration. |
| Keeping an identity sound | artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0 | Keeps a superseded artifact in the record and out of reach. | PARTIAL | Says nothing about which changes call for a new identity. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing declares which parts of a declaration only explain. | MAJOR | No comparison of two declarations can ignore their wording. | OBSERVED | S2 belief_verification #1 |
| Nothing declares which lists carry no meaning in their order. | MAJOR | A list rewritten in another order reads as a change of meaning. | OBSERVED | S2 belief_verification #2 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Prose is not the same as explanation. | Some parts that hold sentences are data the platform acts on, such as a test case's question and the text a model is given; only some prose only explains. | OBSERVED | S2 belief_verification #1 |
| Order carries meaning in some lists and not others. | The moments an ending announces are announced in the order written, while the outcomes a contract allows are a set. | OBSERVED | S2 belief_verification #2 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A part named the same way in two places could mean different things. | The declaration names parts by name, and a name could be reused for data somewhere later. | MINOR | OBSERVED | S2 architectural_observations #1 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
