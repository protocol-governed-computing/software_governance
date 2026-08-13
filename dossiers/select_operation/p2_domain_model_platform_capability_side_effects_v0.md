# Stage 2 — Domain Model Discovery: platform / capability_side_effects
**Stage:** 2 — Domain Model Discovery
**CR:** select_operation
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, the change request that
carried the operation in, and the recorded history of when it arrived. What was searched is recorded,
not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Capability | The platform's offer of something the business cannot do for itself. | Six exist, and the admitted set is closed. | VERIFIED | S1 business_vocabulary #1 |
| Operation | One thing a capability offers to do, named and declared. | Twenty-one across the six, each declaring what it answers with. | VERIFIED | S1 business_vocabulary #2 |
| Offer | The whole set of operations a capability declares. | One per capability, read from the capability itself. | VERIFIED | S1 business_vocabulary #3 |
| Record | A durable statement the business keeps and addresses by a key. | Held by the capability that offers mutable records. | VERIFIED | S1 business_vocabulary #4 |
| Selection | Answering a question by looking at records rather than the keys they are filed under. | Offered as one operation, added after the capability was first declared. | VERIFIED | S1 business_vocabulary #5 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Operation | What it answers with | The fields a caller may read from it. | VERIFIED | S1 system_beliefs #1 |
| Operation | Whether it reads or changes | Declared on every operation, and the read-only reach across a boundary rests on it. | VERIFIED | S1 system_beliefs #1 |
| Operation | The reason it is offered | Why the platform offers it at all. | NOT_FOUND | S1 system_beliefs #5 |
| Offer | Which change last altered it | What a reader would follow to find the reasoning. | NOT_FOUND | S1 system_beliefs #3 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Answering a question about what is held | A caller searching the catalog | The records themselves, selected by content. | VERIFIED | S1 system_beliefs #2 |
| Adding an operation to a capability | The change that needs it | A wider offer, reachable by every domain. | VERIFIED | S1 system_beliefs #3 |
| Finding out why an operation is offered | Anyone reading the capability | The capability says what the operation does and not why it exists. | VERIFIED | S1 system_beliefs #5 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Adding an operation to a capability | 1 | Declare the operation on the capability. | The wider offer. | VERIFIED | S1 system_beliefs #1 |
| Adding an operation to a capability | 2 | Record which change added it and why. | Nothing — no dossier states it. | NOT_FOUND | S1 system_beliefs #5 |
| Answering a question about what is held | 1 | Read every record the store holds. | The records, and the keys they are filed under. | VERIFIED | S1 system_beliefs #2 |
| Answering a question about what is held | 2 | Select among them by content. | The matching records. | VERIFIED | S1 system_beliefs #2 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The capability offers an operation that reads every record it holds. | VERIFIED | capability_side_effects::CS_MUTABLE_JSON_V0 declares SELECT — *read every record in storage, for a caller that selects among them by content* — answering with the records and the keys, declared a read, and published on the capability surface alongside the other eight operations it offers. | S1 system_beliefs #1 |
| The operation is reached by acts of a business domain and is running. | VERIFIED | book_library_mgmt::CC_SEARCH_CATALOG_V0 and book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 each perform it, reached by book_library_mgmt::WF_SEARCH_CATALOG_V0 and book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0. The catalog's acceptance criteria hold, twenty-three of twenty-three, driving those acts against real stores. | S1 system_beliefs #2 |
| The operation was carried into the platform by a business change request that inventoried the capability as one it extends. | VERIFIED | The catalog's first change request lists the capability in its inventory of existing artifacts with the action EXTEND, and gives as its reason that it was extended with an operation publishing the records themselves. The operation arrived in the same release as that change. | S1 system_beliefs #3 |
| Nothing in the composition asked whether a business change request may amend a platform capability. | VERIFIED | The design phase held an inventoried artifact to resolving and to carrying a summary, and asked nothing about who may amend what. A rule refusing it exists only as of this session, and the capability is substrate a change reuses rather than a family it may author. | S1 system_beliefs #4 |
| The reason the capability offers this operation is written down in another domain's change request. | VERIFIED | The reason is the catalog's: a search must see records rather than the keys they are filed under. It is stated in that change request's inventory row and nowhere on the capability, which says what the operation does and not why it is offered. | S1 system_beliefs #5 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Holds durable records addressed by a key | capability_side_effects::CS_MUTABLE_JSON_V0 | Writes, reads, lists, selects, updates in place and deletes. | PARTIAL | Says what each operation does and never why it is offered. |
| Governs what a capability may be | fb.capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0 | Declares what a capability side effect is and what it may carry. | PARTIAL | Says nothing about who may change what an admitted capability offers. |
| Keeps the admitted set closed | fb.capability_side_effects::INVARIANT_CS_SURFACE_CLOSED_V1 | Refuses a capability nobody admitted. | PARTIAL | Governs which capabilities exist, not which operations one offers. |
| Searches the catalog | book_library_mgmt::CC_SEARCH_CATALOG_V0 | Selects the book records matching stated criteria. | EXACT | Nothing — it is the caller the operation was added for. |
| Assembles a book's details | book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0 | Reads a book and selects the copies held of it. | EXACT | Nothing — the second caller, and evidence the operation is general. |
| The act a reader reaches it through | book_library_mgmt::WF_SEARCH_CATALOG_V0 | Answers a question about what the library holds. | EXACT | Nothing. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No dossier records why the capability offers an operation that reads every record. | CRITICAL | The next domain to reach it cannot tell a load-bearing operation from one added for a single caller. | VERIFIED | S1 system_beliefs #5 |
| The reason lives in a business change request that consumed the operation rather than with the capability that offers it. | CRITICAL | A reader learns the platform's offer from whichever domain needed it first. | VERIFIED | S1 system_beliefs #3 |
| Nothing recorded that a domain amended a platform capability. | MINOR | The first instance of a boundary crossing is absorbed rather than visible, and the rule that now refuses it has nothing to point at. | VERIFIED | S1 system_beliefs #4 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The operation is general, not a favour to one caller. Two contracts reach it for different questions — which records match, and which copies are held of a book. | Both perform it, and the acceptance criteria that drive them hold. | VERIFIED | S1 system_beliefs #2 |
| The capability's offer is discoverable and its reasons are not. Every operation states what it does, what it answers with and whether it reads or writes; none states why it exists. | The capability declares nine operations and no reason among them. | VERIFIED | S1 system_beliefs #5 |
| The closed set governs which capabilities exist and not what one offers. A capability nobody admitted is refused; an operation added to an admitted one is not examined at all. | The invariant that closes the surface names capabilities, never operations. | VERIFIED | S1 system_beliefs #4 |
| The extension was declared, not smuggled. The change request said in its own registers that it was extending the capability, and every check passed because none of them asked whether it may. | The inventory row states the action and the reason plainly. | VERIFIED | S1 system_beliefs #3 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A domain amending a platform capability passed every check in the workspace, and the platform's own rule against it was doctrine that nothing enforced. | The change request declared the extension and was admissible; the rule refusing it dates from this session. | CRITICAL | VERIFIED | S1 system_beliefs #4 |
| An operation whose reason lives in another domain's change request reads, to the next domain, as part of the platform's permanent offer. Nothing distinguishes an operation the platform decided from one a caller needed. | The capability presents all nine operations identically. | MAJOR | VERIFIED | S1 system_beliefs #5 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
