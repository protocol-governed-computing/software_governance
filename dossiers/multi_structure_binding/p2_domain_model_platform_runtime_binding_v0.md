# Stage 2 — Domain Model Discovery: platform / runtime_binding
**Stage:** 2 — Domain Model Discovery
**CR:** multi_structure_binding
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot, the governance surface it
seals, and the act that fails today. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Act | Something the business does as one unit, which completes or is refused. | Not stored. Declared, and traced when it runs. | VERIFIED | S1 business_vocabulary #1 |
| Subdomain | A part of the business that owns records and answers for them. | Not stored. Declared by each artifact that names its owner. | VERIFIED | S1 business_vocabulary #2 |
| Storage description | A subdomain's statement of where its own records live. | One per subdomain, naming the records it holds. | VERIFIED | S1 business_vocabulary #3 |
| Binding | What connects an act to the storage descriptions it works against. | One per subdomain, and an act names exactly one. | VERIFIED | S1 business_vocabulary #4 |
| Reach | An act reading records another subdomain owns. | Nothing holds one. There is nowhere to state it. | NOT_FOUND | S1 business_vocabulary #5 |
| Owner | The subdomain answerable for a record and the only one that may change it. | Declared per artifact as the subdomain that owns it. | VERIFIED | S1 business_vocabulary #6 |
| Contested description | One record described by two subdomains. | Nothing holds one, and nothing detects one. | NOT_FOUND | S1 business_vocabulary #7 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Binding | The storage description it names | Where the act's records are found. | VERIFIED | S1 system_beliefs #1 |
| Binding | The subdomain that owns it | Who maintains the statement. | VERIFIED | S1 known_facts #10 |
| Act | The bindings it operates under | Which descriptions its records resolve against. | NOT_FOUND | S1 known_facts #11 |
| Reach | The subdomain reached | Whose records the act reads. | NOT_FOUND | S1 business_invariants #5 |
| Reach | Owned or consulted | Whether the act may change what it names. | NOT_FOUND | S1 business_invariants #6 |
| Storage description | The records it describes | What the subdomain holds. | VERIFIED | S1 business_vocabulary #3 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Running an act against its own records | The caller of the act | The records are found and the act completes. | VERIFIED | S1 system_beliefs #1 |
| Running an act that reads another subdomain's records | The caller of the act | The act stops when it runs, because the records it asks for are described somewhere it cannot reach. | VERIFIED | S1 system_beliefs #2 |
| Reviewing a design for what it reaches | The person reviewing the change | Nothing about the reach is visible, because nothing states it. | VERIFIED | S1 system_beliefs #6 |
| Assembling a composition | The person building it | A composition, or a refusal where two copies of one thing disagree. | VERIFIED | S1 system_beliefs #5 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Running an act that reads another subdomain's records | 1 | Resolve the act's binding to one storage description. | The description the act works against. | VERIFIED | S1 system_beliefs #1 |
| Running an act that reads another subdomain's records | 2 | Look for the records the reused capability reads. | Nothing — they are not in that description. | VERIFIED | S1 system_beliefs #2 |
| Running an act that reads another subdomain's records | 3 | Refuse the act, naming the records it could not find. | A refusal, at the moment it runs. | VERIFIED | S1 system_beliefs #2 |
| Declaring a reach | 1 | Name the other subdomain whose records the act reads. | Nothing — there is nowhere to state it. | NOT_FOUND | S1 requested_outcomes #4 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| An act reaches one place where storage is described, and every capability it performs resolves against that one place. | VERIFIED | Every runtime binding in the composition names exactly one storage description, and the compiler looks up exactly one when it seals the binding policy. Seven bindings exist across five domains and no shape other than one-to-one appears. | S1 system_beliefs #1 |
| An act that reuses a capability owned by another subdomain stops when it runs, because the records that capability reads are described somewhere the act cannot reach. | VERIFIED | blockchain::WF_CREATE_WALLET_V0 reuses blockchain::CC_RESOLVE_ACTOR_V0, which reads records described in blockchain::STRUCTURE_IDENTITY_STORAGE_V0, while blockchain::RB_WALLET_BINDINGS_V0 names blockchain::STRUCTURE_WALLET_STORAGE_V0 and describes three wallet records and no people. The act is admissible at every phase, compiles, verifies and attests, and stops on its second step. | S1 system_beliefs #2 |
| Nothing governing states that an act resolves its records against one description, or why it should. | VERIFIED | runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 governs bindings and never mentions where storage is described. Its four invariants — runtime_binding::INVARIANT_RB_BINDING_POLICY_CONFORMANCE_V0, runtime_binding::INVARIANT_RB_CS_ONLY_V0, runtime_binding::INVARIANT_RB_NO_LOGIC_V0 and runtime_binding::INVARIANT_RB_PARAMETERS_DECLARED_V0 — mention it in no form. The singular exists only as a field's declared type. | S1 system_beliefs #3 |
| The composition can tell a reading operation from a writing one. | VERIFIED | Every capability operation declares whether it reads or writes, twenty-one across six capabilities with none undeclared, and a design that reaches a writing contract across a subdomain boundary is refused. The enforcement exists and holds today. | S1 system_beliefs #4 |
| Assembly already refuses a composition where two copies of one thing disagree, rather than answering from whichever it resolved. | VERIFIED | The assembler compares every copy of an artifact identity and refuses the composition when they disagree, naming the identity and the copies. The precedent for refusing rather than preferring is established and running. | S1 system_beliefs #5 |
| The design language can say which capability an act reuses and where the act's own records live, and cannot say that the act also reads what another subdomain holds. | VERIFIED | A design declares the capabilities an act composes and the storage its own subdomain describes. No register carries a second subdomain's records, so the reach is stated nowhere and is discovered when the act runs. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Governs bindings | runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 | Declares what a binding is and what it may carry. | PARTIAL | Says nothing about where storage is described, or how much of it an act reaches. |
| Holds a binding to its declared parameters | runtime_binding::INVARIANT_RB_BINDING_POLICY_CONFORMANCE_V0 | Checks the binding policy the compiler sealed. | PARTIAL | Checks the one description it finds, and cannot ask whether there should be more. |
| Binds the wallet's act | blockchain::RB_WALLET_BINDINGS_V0 | Names the storage description the wallet act resolves against. | MISMATCH | Names one description, so the act cannot reach the people it must read. |
| Binds identity's acts | blockchain::RB_IDENTITY_BINDINGS_V0 | Names the storage description identity's acts resolve against. | EXACT | Nothing — it is the description the wallet needs and cannot reach. |
| Describes where people live | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | Identity's statement of the records it holds. | EXACT | Nothing. It is correct and unreachable from another subdomain. |
| Describes where wallets live | blockchain::STRUCTURE_WALLET_STORAGE_V0 | The wallet's statement of the records it holds. | EXACT | Describes no people, correctly. |
| Resolves a person | blockchain::CC_RESOLVE_ACTOR_V0 | Establishes that a person exists and has been accepted. | EXACT | Nothing — the capability is right; the records it reads are out of reach. |
| The act that fails | blockchain::WF_CREATE_WALLET_V0 | Creates a wallet for an accepted person. | MISMATCH | Completes only against a composition assembled to make its second step reachable. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| An act cannot name more than one place where storage is described. | CRITICAL | The confirmed act stops when it runs, and every later one will. | VERIFIED | S1 system_beliefs #1 |
| A design cannot state that an act reads another subdomain's records. | CRITICAL | The reach is invisible until execution, so no review and no rule can see it. | VERIFIED | S1 system_beliefs #6 |
| Nothing states how storage resolution works, so there is no rule to amend. | CRITICAL | The change states a governing model for the first time rather than widening an existing one. | VERIFIED | S1 system_beliefs #3 |
| Nothing distinguishes the records an act owns from those it consults. | CRITICAL | A read-only reach cannot be held without it. | VERIFIED | S1 business_invariants #6 |
| Nothing detects one record described by two subdomains. | CRITICAL | The rule that a record is described once is stated and unchecked. | NOT_FOUND | S1 business_invariants #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Two declarations are singular here, not one: a binding names one storage description, and an act names one binding. The reach can be widened at either, which is why the shape was a decision rather than a detail. | Every binding in the composition names one description, and every act names one binding. | VERIFIED | S1 system_beliefs #1 |
| The singular is a field's type rather than a governed statement. Nothing declares that an act resolves against one description, so nothing has to be relaxed — the model is stated here for the first time. | The governing constitution and its four invariants mention where storage is described in no form. | VERIFIED | S1 system_beliefs #3 |
| The half of this change that makes the read-only rule enforceable is already delivered. Every operation declares whether it reads or writes, and a reach to a writing contract across a boundary is refused at design time. | Twenty-one operations across six capabilities declare an effect, with none undeclared. | VERIFIED | S1 system_beliefs #4 |
| The refusal this change requires has a precedent one level up and a place to live. Assembly already refuses when two copies of one identity disagree rather than answering from either. | The assembler compares copies by content and names both when they differ. | VERIFIED | S1 system_beliefs #5 |
| The act fails late and passes everything before it. Every document check, the completeness measure and the compile all pass on an act that cannot run. | The wallet act is admissible at every phase, compiles, verifies, attests, and stops on its second step. | VERIFIED | S1 system_beliefs #2 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The only way to make the act work today is for one subdomain to describe another's records, which every document check would accept. Nothing refuses the second copy, so the workaround is easier than the change. | The wallet's own description could name where people live, and nothing in the composition would object. | CRITICAL | VERIFIED | S1 known_facts #10 |
| A rule stated in this dossier and checkable only at assembly leaves the design layer unable to see its own violation. A design that contests a description would pass every phase and be refused later. | Nothing in the design registers carries a second subdomain's records, so no phase rule can compare two descriptions. | MAJOR | VERIFIED | S1 business_invariants #1 |
| The failure surfaces only when the act runs, and everything before it reports success. Any later act that reaches across a boundary will be discovered the same way until this lands. | The wallet act passes every check and stops on its second step. | MAJOR | VERIFIED | S1 system_beliefs #2 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| NONE IDENTIFIED |
