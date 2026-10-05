# Stage 2 — Domain Model Verification: platform / reference semantics

**Stage:** 2 — Domain Model Verification
**CR:** reference_semantics
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. Every
declaration in the composition was read for the parts that hold a full name, the parts that hold a
short code, and the value of every part declared explanation. The record of references was asked who
refers to five artifacts, and the two places that find references were read.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Declaration | What an artifact states about itself, in the form the platform reads. | Sealed in the composition; not stored by this change. | OBSERVED | S1 business_vocabulary #1 |
| The Reference | A part of a declaration whose value names another artifact. | Part of the declaration that holds it. | OBSERVED | S1 business_vocabulary #2 |
| The Record of References | The platform's account of which artifact names which. | Sealed in the composition's evidence; answered by inspection. | OBSERVED | S1 business_vocabulary #5 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Reference | The part it sits in | The named part of the declaration that holds the name. | OBSERVED | S2 belief_verification #4 |
| The Reference | How it is written | By full name, with the namespace, or by short code alone. | OBSERVED | S2 belief_verification #4 |
| The Declaration | Its explanation parts | Parts declared to explain; most hold text, some hold data. | OBSERVED | S2 belief_verification #3 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Record what names what | The platform, when it builds a composition | The record of references. | OBSERVED | S1 requested_outcomes #4 |
| Keep a stood-down artifact out of reach | The platform, when it builds a composition | The build is refused if a live artifact names a stood-down one. | OBSERVED | S1 requested_outcomes #4 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Record what names what | 1 | Read each declaration's names from a fixed list of parts. | The names each artifact refers to. | OBSERVED | S2 belief_verification #1 |
| Record what names what | 2 | Refuse a short code in one of those parts. | A refusal. | OBSERVED | S2 belief_verification #1 |
| Keep a stood-down artifact out of reach | 1 | Read every value in each live declaration, by full name or short code, except the supersession itself. | A refusal per reach. | OBSERVED | S2 belief_verification #2 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The record of references reads a fixed list of parts and misses most of them. | VERIFIED | The compiler's extraction reads nine parts: vocabulary_id, governed_by, structure, runtime_binding, transform, transforms, side_effects, consults, and the keys of a binding's bindings; it refuses a short code in any of them. Asked through si.artifact.refs, the record reports conformance::CONSTITUTION_ASSERT_V0 referred to by 1 artifact, while 138 name it under enforced_by; transformation::AC_SEED_AUTHOR_V0 by none, while 39 name it under actor_context; causal_language_model::EV_MODEL_REGISTERED_V0 by none, while workflows announce it under emit. | S1 system_beliefs #1 |
| The check that nothing reaches a stood-down artifact reads every value that looks like a name. | VERIFIED | artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 is enforced by a handler that walks every string of a live declaration and matches it against every full name and every short code, skipping only supersedes and superseded_by. It finds short-code references the record does not hold. | S1 system_beliefs #2 |
| No part of a declaration declared explanation holds anything but text today. | NOT_FOUND | Forty-six values of parts declared explanation are not a single string. Most are lists of sentences: failure_modes 24, use_cases 9, notes 4, admission_rules 1. Eight are data: test data writes a model's settings under description and a count under summary. | S1 system_beliefs #3 |
| Every full name in the composition sits in a part that can be declared a reference. | VERIFIED | Across 540 declarations, full names sit under 31 named parts and under the keys of a binding's bindings. Five of the nine parts the record reads hold one today: governed_by, structure, runtime_binding, transform and consults. The rest are enforced_by, side_effect, actor_context, emit, target, allowed_capability_transforms, allowed_capability_side_effects, storage_structure, workflow, atom, molecule, extends, disposition_vocabulary, fqdn_id, and the phase workflows a judge consults, each named under its phase; supersedes and superseded_by declare supersession. Every one of them names an artifact wherever it appears. workflow also holds short codes, in 39 intents. | S1 system_beliefs #4 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Declaring what carries no meaning | artifact::VOCAB_DECLARATION_REPRESENTATION_V0 | Names the explanation parts and the unordered lists. | PARTIAL | Names no reference, and does not say explanation is exempt only as text. |
| Keeping a stood-down artifact out of reach | artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0 | Refuses a live declaration that names a stood-down artifact. | PARTIAL | Decides what a reference is by itself. |
| Governing vocabularies | vocabulary::CONSTITUTION_VOCABULARY_V0 | Governs what a vocabulary declares and how its entries are written. | EXACT | Nothing for this purpose; it governs the new declaration. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing declares which parts of a declaration are references. | CRITICAL | A replacement cannot learn what reaches what it replaces, and a re-point reads as a change of meaning. | OBSERVED | S2 belief_verification #1 |
| The record of references and the reach check each decide what a reference is. | MAJOR | The two disagree, and inspection under-reports who depends on an artifact. | OBSERVED | S2 belief_verification #2 |
| Nothing says explanation is exempt only as text. | MAJOR | Data written under an explanation part would be ignored when two declarations are compared. | OBSERVED | S2 belief_verification #3 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Text is a sentence or a list of sentences. | Every non-string explanation value that is not test data is a list of sentences. | OBSERVED | S2 belief_verification #3 |
| Some reference parts may hold a short code and some may not. | The record refuses a short code in its nine parts; 39 intents name their workflow by short code. | OBSERVED | S2 belief_verification #4 |
| Supersession names an artifact without reaching it. | The reach check skips supersedes and superseded_by, because naming what you stand in for is the relation itself. | OBSERVED | S2 belief_verification #2 |
| The reach check is the only guard on short-code references. | Nothing else finds a short code naming a stood-down artifact. | OBSERVED | S2 belief_verification #2 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Narrowing the reach check to declared parts would stop it seeing short codes. | Short-code references are out of scope here and sit in parts this change does not declare. | MAJOR | OBSERVED | S2 architectural_observations #4 |
| A rule written only in prose cannot be read by the comparison that applies it. | A vocabulary's meanings are not sealed with its entries. | MINOR | OBSERVED | S2 belief_verification #3 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
