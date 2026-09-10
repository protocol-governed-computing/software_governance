# Stage 2 — Domain Model Discovery: platform / workflow
**Stage:** 2 — Domain Model Discovery
**CR:** multi_emission
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, the sealed dispatch each
domain compiles to, and the readers of an announced moment. What was searched is recorded, not only
what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Act | Something the business does as one unit, which completes or is refused. | Declared, and traced when it runs. | VERIFIED | S1 business_vocabulary #1 |
| Moment | Something the business declared matters, recognised when it occurs. | Twenty declared across four domains. | VERIFIED | S1 business_vocabulary #2 |
| Announcement | An act stating that a moment occurred. | Twelve declared across nine acts, each naming exactly one moment. | VERIFIED | S1 business_vocabulary #3 |
| Terminal node | Where an act ends, and what carries its announcement. | One announcement per terminal node, and several terminal nodes per act. | VERIFIED | S1 business_vocabulary #4 |
| Order | The sequence in which several announcements are made. | Nothing holds one. No act announces more than one moment at a terminal node. | NOT_FOUND | S1 business_vocabulary #5 |
| Evidence record | The observable trace that a moment was announced. | One entry per announcement, written as the act runs. | VERIFIED | S1 business_vocabulary #6 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Terminal node | The moment it announces | What the act says it completed. | VERIFIED | S1 system_beliefs #1 |
| Terminal node | The moments it announces | Several, in a stated order. | NOT_FOUND | S1 requested_outcomes #1 |
| Announcement | Its position in the order | Which of several it is. | NOT_FOUND | S1 requested_outcomes #2 |
| Announcement | The transition it fires on | The act, the step, and the outcome that step produced. | VERIFIED | S1 system_beliefs #1 |
| Evidence record | The moment it records | Which moment was announced. | VERIFIED | S1 requested_outcomes #3 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Completing an act that recognises one moment | The caller of the act | The moment is announced and recorded. | VERIFIED | S1 system_beliefs #1 |
| Completing an act that recognises several moments | The caller of the act | One moment could be announced, so the domain announces none. | VERIFIED | S1 system_beliefs #4 |
| Reading what an act announced | Anyone reading the trail | The moments announced, one record each. | VERIFIED | S1 system_beliefs #5 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Completing an act that recognises one moment | 1 | Reach the end of the act by an outcome that announces. | The transition the announcement is keyed to. | VERIFIED | S1 system_beliefs #1 |
| Completing an act that recognises one moment | 2 | Announce the moment that transition names. | One evidence record. | VERIFIED | S1 requested_outcomes #3 |
| Completing an act that recognises several moments | 1 | Reach the end of the act. | The transition. | VERIFIED | S1 system_beliefs #1 |
| Completing an act that recognises several moments | 2 | Announce the moments it completed, in order. | Nothing — a terminal node carries one name, and the design declared none rather than choose. | NOT_FOUND | S1 system_beliefs #4 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| A terminal node names a single moment, and the running system resolves a single moment for a given act and outcome. | VERIFIED | Every terminal node in the composition carries at most one `emit`, and the sealed dispatch holds twelve announcements across nine acts, each keyed to one transition and naming one moment. `ai_governance::WF_PROVISION_AI_LICENSING_V0` shows the shape most clearly: two terminal nodes, one moment each, never two from one. | S1 system_beliefs #1 |
| An act exists that completes several declared moments and can announce one. | VERIFIED | `book_library_mgmt::WF_REGISTER_BOOK_V0` registers a work, its first edition and that edition's first physical copy. Three of its subdomain's six declared moments — `book_library_mgmt::EV_WORK_REGISTERED_V0`, `book_library_mgmt::EV_BOOK_REGISTERED_V0` and `book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V0` — name exactly those things. | S1 system_beliefs #2 |
| Nothing governing states what a terminal node announces. | VERIFIED | `workflow::CONSTITUTION_WORKFLOW_V0` governs the act and does not use the word. `event::CONSTITUTION_EVENT_V0` speaks of records being immutable once written and says nothing about how many an act may write. `event::INVARIANT_EV_APPEND_ONLY_V0` and `event::INVARIANT_EV_SCHEMA_REQUIRED_V0` require append-only writing and a declared schema, and neither counts. | S1 system_beliefs #3 |
| A subdomain exists whose declared moments are announced by nothing at all. | VERIFIED | The catalog declares six moments and its acts carry **no announcement whatsoever** — zero `emit` declarations across every one of its workflows, against twelve elsewhere in the composition. Faced with announcing one of three, the design announced none. Silence was chosen over a wrong answer. | S1 system_beliefs #4 |
| Nothing counts the moments an act announces — no rule, no published surface, no boundary declaration. | VERIFIED | No invariant counts announcements. No inspection operation reads them. No egress declaration enumerates the moments an act emits. The occurrence counts in the domain validations count records written by capability steps, which are writes rather than announcements and are unaffected by this change. | S1 system_beliefs #5 |
| A reader exists that takes the first announced moment it finds. | VERIFIED | The reference workload's execution test selects the first announcement in the trace and asserts its identity. It would accept a second and a third without noticing, which is the one place several would arrive silently. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Governs the act | workflow::CONSTITUTION_WORKFLOW_V0 | Declares what an act is, how it routes, and where it ends. | PARTIAL | Says nothing about what a terminal node announces, or how many moments it may. |
| Governs a moment | event::CONSTITUTION_EVENT_V0 | Declares what a moment is and that its record is immutable once written. | PARTIAL | Says nothing about how many moments one act may announce. |
| Holds a moment's record append-only | event::INVARIANT_EV_APPEND_ONLY_V0 | Refuses a moment's record being altered after it is written. | EXACT | Nothing — it is why an announced moment cannot be unannounced. |
| Requires a moment to declare its schema | event::INVARIANT_EV_SCHEMA_REQUIRED_V0 | Refuses a moment with no declared shape. | EXACT | Does not count announcements. |
| An act announcing on each of two outcomes | ai_governance::WF_PROVISION_AI_LICENSING_V0 | Announces one moment when it provisions and another when it denies. | EXACT | Announces one moment per outcome, which is the model working as declared. |
| An act announcing one moment | workload::WF_COLLATZ_CONJECTURE_V0 | Announces the moment it evaluated the conjecture. | EXACT | Nothing. It is the case of one, which must keep behaving identically. |
| An act completing several moments | book_library_mgmt::WF_REGISTER_BOOK_V0 | Registers a work, its first edition and its first physical copy. | MISMATCH | Announces none of the three, because it can announce one. |
| A moment declared and never announced | book_library_mgmt::EV_WORK_REGISTERED_V0 | Declares that the collection now carries a work. | MISMATCH | Nothing announces it. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A terminal node cannot name more than one moment. | CRITICAL | An act completing several announces one, and the business never agreed which. | VERIFIED | S1 system_beliefs #1 |
| Nothing states an order for several announcements. | CRITICAL | Without a normative order the account of an act varies between runs, or is incidental to a serialization. | NOT_FOUND | S1 requested_outcomes #2 |
| Nothing governs announcement at all, so there is no rule to relax. | CRITICAL | The change states the model for the first time rather than widening an existing one. | VERIFIED | S1 system_beliefs #3 |
| An announcement that cannot be made has no declared outcome. | MAJOR | The act would pass over it, which is the silence this change exists to remove. | NOT_FOUND | S1 business_invariants #5 |
| Nothing refuses one moment announced twice. | MINOR | A reader counting occurrences would conclude something happened that did not. | NOT_FOUND | S1 operation_refusals #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Several announcements per act already exist — across outcomes, never within one. Four acts announce different moments on different endings, so plurality is not foreign to the model; the singular is one announcement per *transition*. | Twelve announcements across nine acts, one per terminal node. | VERIFIED | S1 system_beliefs #1 |
| The cost is already being paid, and paid as silence. A subdomain with six declared moments announces none rather than announce one of three and imply the other two did not occur. | The catalog carries zero announcements against twelve elsewhere. | VERIFIED | S1 system_beliefs #4 |
| The limit is two lines of implementation and no governance. The compiler reads one name off a terminal node and re-keys it to the transition that reaches it; the running system fires the one moment that resolves to. | The governing constitution does not use the word, and no invariant covers it. | VERIFIED | S1 system_beliefs #3 |
| A terminal node carries no address of its own, which is why the announcement is re-keyed to the transition — the act, the step, and the outcome the step produced. Whatever a design states several against, the composition keys them by the transition. | The sealed dispatch is keyed by act, source step and outcome. | VERIFIED | S1 system_beliefs #1 |
| The evidence writer is already per-moment. It records one entry per announcement, so several announcements need no new kind of record — only more of the one that exists. | Each announcement writes one trace entry naming the moment and its payload. | VERIFIED | S1 requested_outcomes #3 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A subdomain declared six moments, wired none, and every check passed. Nothing asks whether a declared moment is ever announced, so the silence is invisible to the composition and visible only to a person reading both lists. | Six declared moments and zero announcements in one subdomain. | CRITICAL | VERIFIED | S1 system_beliefs #4 |
| The one reader of announcements takes the first it finds. When several arrive it will keep passing while checking a third of what happened. | The reference test selects the first announcement and asserts its identity. | MAJOR | VERIFIED | S1 system_beliefs #6 |
| Nothing counts announcements anywhere in the composition, so a change to how many are made cannot be detected by any existing check. The conformance test for this change has to be written with it. | No invariant, no inspection operation and no boundary declaration reads an announcement. | MAJOR | VERIFIED | S1 system_beliefs #5 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
