# Stage 1 — Change Request: Clarification & Fact Capture: platform / runtime_binding
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** multi_structure_binding
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| runtime_binding | MODIFY | An act reaches one place where storage is described, so an act reusing another subdomain's capability cannot reach the records that capability reads. The singular is a field's shape rather than a stated rule, and no rule about reach exists to change. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Act | Something the business does that runs as one unit and either completes or is refused. | CR seed §2 Business Vocabulary #1 |
| Subdomain | A part of the business that owns a set of records and answers for them. | CR seed §2 Business Vocabulary #2 |
| Storage description | A subdomain's statement of where its own records live. | CR seed §2 Business Vocabulary #3 |
| Binding | What connects an act, at the moment it runs, to the storage descriptions it works against. | CR seed §2 Business Vocabulary #4 |
| Reach | An act reading records a subdomain other than its own owns. | CR seed §2 Business Vocabulary #5 |
| Owner | The subdomain answerable for a record, and the only one that may change it. | CR seed §2 Business Vocabulary #6 |
| Contested description | One record described by two subdomains, whose descriptions may disagree. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| One act can reach the records of more than one subdomain, by naming each place they are described. | CR seed §3 Requested Outcomes #1 |
| The reach is read-only, and the platform can tell a read from a write well enough to hold it. | CR seed §3 Requested Outcomes #2 |
| Every record stays described exactly once, by the subdomain that owns it. | CR seed §3 Requested Outcomes #3 |
| A reach across a boundary is something a reviewer sees in the design rather than something a run discovers. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A subdomain owns what it holds, and ownership that does not include being the only writer is not ownership. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| An act may consult what another subdomain holds, because a second copy of one truth can disagree with the thing it describes. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| An act may never change what another subdomain holds; two subdomains deciding what is true leaves neither answerable. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Naming another subdomain's records is not the same act as being permitted to write to them. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| An act may reach what its own domain holds, and no further. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A dependency on another domain goes through that domain's capability, which is declared and resolvable, rather than through its storage, which is a private arrangement. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Naming is enough to reach, and the act that reaches is the one that names it. Its owner does not consent first. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| An act distinguishes the records it owns from those it merely consults, because a permission that hides that distinction cannot be held. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| One record described by two subdomains refuses the composition when it is assembled. Choosing between two descriptions would license the state this change forbids. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A subdomain's storage description stays in that subdomain's own artifact, maintained by whoever answers for it. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| An act names the bindings it operates under, and each binding stays owned by the subdomain that wrote it. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| The reach is a relationship between two subdomains, and it is worth changing how an act resolves its records in order to declare it as one. | HIGH | CR seed §4 Known Facts — Business Truths #12 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| An act reaches one place where storage is described, and every capability it performs resolves against that one place. | The whole of this change. | Establish how many storage descriptions an act reaches today and where that number is stated. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| An act that reuses a capability owned by another subdomain stops when it runs, because the records that capability reads are described somewhere the act cannot reach. | Establishes the requirement occurred rather than being foreseen. | Confirm an instance, confirm where it stops, and confirm the reason is the records rather than the capability. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Nothing governing states that an act resolves its records against one description, or why it should. | Decides whether this changes a rule or states a model for the first time. | Establish what governs storage resolution today, and what it says. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The composition can tell a reading operation from a writing one. | The read-only ruling is unenforceable without it. | Confirm every operation declares whether it reads or writes, and that a reach across a boundary is already held to reading. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Assembly already refuses a composition where two copies of one thing disagree, rather than answering from whichever it resolved. | Says the refusal this change requires has a precedent and a place to live. | Confirm what assembly compares, and what it does when copies disagree. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| The design language can say which capability an act reuses and where the act's own records live, and cannot say that the act also reads what another subdomain holds. | Says why the reach is invisible until execution. | Establish what a design can state today about the records an act reaches. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| The reach needed today is one act reading records owned by one other subdomain of the same domain. | The one confirmed instance reaches a single other subdomain. | CR seed §6 Assumptions #1 |
| An act's own records are the ones it writes, so ownership and the right to write are the same distinction seen from two sides. | The business author's ruling that ownership is being the only writer. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| No subdomain's artifact describes another subdomain's storage. | Business author | CR seed §7 Constraints #1 |
| A reach is read-only, whatever form the declaration takes. | Business author | CR seed §7 Constraints #2 |
| A reach stays inside the act's own domain. | Business author | CR seed §7 Constraints #3 |
| Every record is described exactly once, by the subdomain that owns it. | Business author | CR seed §7 Constraints #4 |
| The reach is declared where a reviewer reads it, not inferred from what an act happens to reuse. | Business author | CR seed §7 Constraints #5 |
| An act may not gain the ability to reach records by restating another subdomain's description as its own. | Business author | CR seed §7 Constraints #6 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A record has exactly one description, written by the subdomain that owns it. | CR seed §8 Business Invariants #1 |
| The owner of a record is the only writer of it. | CR seed §8 Business Invariants #2 |
| An act that reaches records it does not own reads them and never changes them. | CR seed §8 Business Invariants #3 |
| An act reaches only what its own domain holds. | CR seed §8 Business Invariants #4 |
| A reach is declared by the act that reaches, in an artifact that act owns. | CR seed §8 Business Invariants #5 |
| An act's own records are distinguishable from those it merely consults. | CR seed §8 Business Invariants #6 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Record description | Sole | One subdomain describes the record, and it is the owner. | CR seed §9 Lifecycle States #1 |
| Record description | Contested | Two subdomains describe one record, and the composition is refused. | CR seed §9 Lifecycle States #2 |
| Reach | Declared | The act states which other subdomain's records it reads. | CR seed §9 Lifecycle States #3 |
| Reach | Undeclared | The act reads records it never named, which is what a run discovers. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A composition was refused for a contested description | When assembly finds one record described by two subdomains | The rule that every record is described once held, and it held before anything ran. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Where a subdomain's records live | That subdomain | CR seed §11 Authority Boundaries #1 |
| Which records an act reaches | The act that reaches them | CR seed §11 Authority Boundaries #2 |
| Whether a record's description is contested | Assembly, when the composition is put together | CR seed §11 Authority Boundaries #3 |
| Which records a subdomain owns | Settled already, and outside this change | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Which acts should reuse which capabilities | Each domain's business, stated in its own change. | CR seed §12 Out of Scope #1 |
| Whether one subdomain should read another at all | Some do; this change follows that fact. | CR seed §12 Out of Scope #2 |
| Which records a subdomain owns | Ownership is settled; this change is about reach. | CR seed §12 Out of Scope #3 |
| How a subdomain's ownership is declared | A separate problem with its own change. | CR seed §12 Out of Scope #4 |
| Whether a subdomain may hold records only some readers may see | Access control needs its own mechanism, and no act needs it. | CR seed §12 Out of Scope #5 |
| Whether a domain may depend on another domain at all | A question about which parts are composed together, answered there. | CR seed §12 Out of Scope #6 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| runtime_binding | MODIFIED | CR seed §13 Governance Scope #1 |
| workflow | MODIFIED | CR seed §13 Governance Scope #2 |
| design | ADJACENT | CR seed §13 Governance Scope #3 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| An act that reads records another subdomain of its own domain owns completes, rather than stopping when it runs. | CR seed §15 Acceptance Criteria #1 |
| An act that would change records it does not own is refused, and the refusal names what it tried to change. | CR seed §15 Acceptance Criteria #2 |
| A composition in which two subdomains describe one record is refused when it is assembled. | CR seed §15 Acceptance Criteria #3 |
| An act reaching another subdomain's records states so in its design, and a reviewer can see which boundary it crosses without running it. | CR seed §15 Acceptance Criteria #4 |
| No subdomain's artifact describes another subdomain's storage. | CR seed §15 Acceptance Criteria #5 |
| An act that names a place without saying whether it owns it or consults it is refused. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Record description | The records it describes, together with the subdomain that wrote it | They describe the same records for the same subdomain. | CR seed §16 Identity and Sameness #1 |
| Reach | The act that reaches and the subdomain reached | One act names one other subdomain, however many records it reads there. | CR seed §16 Identity and Sameness #2 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Record description | Sole | Contested | A second subdomain describing a record it does not own | Assembly refuses the composition. Nothing else follows, and no description is preferred over the other. | CR seed §17 Lifecycle Transitions #1 |
| Record description | Contested | Sole | The subdomain that does not own the record withdrawing its description | Assembly proceeds. Nothing else follows. | CR seed §17 Lifecycle Transitions #2 |
| Reach | Undeclared | Declared | The act naming the subdomain whose records it reads | The reach becomes reviewable. Nothing is granted that was not already permitted, because reading was never the thing in doubt. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Changing a record | The act does not own it | Two subdomains deciding what is true leaves neither answerable for the result. | CR seed §18 Operation Refusals #1 |
| Assembling a composition | Two subdomains describe one record | Preferring one description makes the answer depend on the order somebody wrote a list in. | CR seed §18 Operation Refusals #2 |
| Reaching records | They belong to another domain | An act correct only in the compositions that happen to include that domain would compile and fail when it runs. | CR seed §18 Operation Refusals #3 |
| Declaring a reach | The act does not say which places it owns and which it consults | The permission rests on that distinction, and a declaration that hides it cannot be held to it. | CR seed §18 Operation Refusals #4 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Which readers may see which records | A later change | A subdomain needs to hold records some readers may not see. | CR seed §19 Authority Deferrals #1 |
| How a subdomain's ownership of a record is declared | A later change | Ownership needs to be stated rather than settled by convention. | CR seed §19 Authority Deferrals #2 |
| Whether one domain may depend on another | Whichever change decides what is composed together | A domain needs something another domain holds. | CR seed §19 Authority Deferrals #3 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
