# Change Seed — platform / runtime_binding

**Stage:** 0 — Change Seed
**CR:** multi_structure_binding
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the six clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

Runtime binding governs where an act finds the records it works on. A subdomain owns what it holds
and says where its own records live; binding is what connects an act, when it runs, to those
descriptions. Its authority is to decide what an act may reach and whose description of a record is
authoritative, and it decides nothing about what any act should do or which records a subdomain
ought to own.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| runtime_binding | MODIFY | An act reaches one place where storage is described, so an act reusing another subdomain's capability cannot reach the records that capability reads. The singular is a field's shape rather than a stated rule, and no rule about reach exists to change. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Act | Something the business does that runs as one unit and either completes or is refused. |
| Subdomain | A part of the business that owns a set of records and answers for them. |
| Storage description | A subdomain's statement of where its own records live. |
| Binding | What connects an act, at the moment it runs, to the storage descriptions it works against. |
| Reach | An act reading records a subdomain other than its own owns. |
| Owner | The subdomain answerable for a record, and the only one that may change it. |
| Contested description | One record described by two subdomains, whose descriptions may disagree. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| One act can reach the records of more than one subdomain, by naming each place they are described. |
| The reach is read-only, and the platform can tell a read from a write well enough to hold it. |
| Every record stays described exactly once, by the subdomain that owns it. |
| A reach across a boundary is something a reviewer sees in the design rather than something a run discovers. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A subdomain owns what it holds, and ownership that does not include being the only writer is not ownership. | HIGH |
| An act may consult what another subdomain holds, because a second copy of one truth can disagree with the thing it describes. | HIGH |
| An act may never change what another subdomain holds; two subdomains deciding what is true leaves neither answerable. | HIGH |
| Naming another subdomain's records is not the same act as being permitted to write to them. | HIGH |
| An act may reach what its own domain holds, and no further. | HIGH |
| A dependency on another domain goes through that domain's capability, which is declared and resolvable, rather than through its storage, which is a private arrangement. | HIGH |
| Naming is enough to reach, and the act that reaches is the one that names it. Its owner does not consent first. | HIGH |
| An act distinguishes the records it owns from those it merely consults, because a permission that hides that distinction cannot be held. | HIGH |
| One record described by two subdomains refuses the composition when it is assembled. Choosing between two descriptions would license the state this change forbids. | HIGH |
| A subdomain's storage description stays in that subdomain's own artifact, maintained by whoever answers for it. | HIGH |
| An act names the bindings it operates under, and each binding stays owned by the subdomain that wrote it. | HIGH |
| The reach is a relationship between two subdomains, and it is worth changing how an act resolves its records in order to declare it as one. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| An act reaches one place where storage is described, and every capability it performs resolves against that one place. | The whole of this change. | Establish how many storage descriptions an act reaches today and where that number is stated. |
| An act that reuses a capability owned by another subdomain stops when it runs, because the records that capability reads are described somewhere the act cannot reach. | Establishes the requirement occurred rather than being foreseen. | Confirm an instance, confirm where it stops, and confirm the reason is the records rather than the capability. |
| Nothing governing states that an act resolves its records against one description, or why it should. | Decides whether this changes a rule or states a model for the first time. | Establish what governs storage resolution today, and what it says. |
| The composition can tell a reading operation from a writing one. | The read-only ruling is unenforceable without it. | Confirm every operation declares whether it reads or writes, and that a reach across a boundary is already held to reading. |
| Assembly already refuses a composition where two copies of one thing disagree, rather than answering from whichever it resolved. | Says the refusal this change requires has a precedent and a place to live. | Confirm what assembly compares, and what it does when copies disagree. |
| The design language can say which capability an act reuses and where the act's own records live, and cannot say that the act also reads what another subdomain holds. | Says why the reach is invisible until execution. | Establish what a design can state today about the records an act reaches. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The reach needed today is one act reading records owned by one other subdomain of the same domain. | The one confirmed instance reaches a single other subdomain. |
| An act's own records are the ones it writes, so ownership and the right to write are the same distinction seen from two sides. | The business author's ruling that ownership is being the only writer. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| No subdomain's artifact describes another subdomain's storage. | Business author |
| A reach is read-only, whatever form the declaration takes. | Business author |
| A reach stays inside the act's own domain. | Business author |
| Every record is described exactly once, by the subdomain that owns it. | Business author |
| The reach is declared where a reviewer reads it, not inferred from what an act happens to reuse. | Business author |
| An act may not gain the ability to reach records by restating another subdomain's description as its own. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A record has exactly one description, written by the subdomain that owns it. |
| The owner of a record is the only writer of it. |
| An act that reaches records it does not own reads them and never changes them. |
| An act reaches only what its own domain holds. |
| A reach is declared by the act that reaches, in an artifact that act owns. |
| An act's own records are distinguishable from those it merely consults. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Record description | Sole | One subdomain describes the record, and it is the owner. |
| Record description | Contested | Two subdomains describe one record, and the composition is refused. |
| Reach | Declared | The act states which other subdomain's records it reads. |
| Reach | Undeclared | The act reads records it never named, which is what a run discovers. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A composition was refused for a contested description | When assembly finds one record described by two subdomains | The rule that every record is described once held, and it held before anything ran. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Where a subdomain's records live | That subdomain |
| Which records an act reaches | The act that reaches them |
| Whether a record's description is contested | Assembly, when the composition is put together |
| Which records a subdomain owns | Settled already, and outside this change |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Which acts should reuse which capabilities | Each domain's business, stated in its own change. |
| Whether one subdomain should read another at all | Some do; this change follows that fact. |
| Which records a subdomain owns | Ownership is settled; this change is about reach. |
| How a subdomain's ownership is declared | A separate problem with its own change. |
| Whether a subdomain may hold records only some readers may see | Access control needs its own mechanism, and no act needs it. |
| Whether a domain may depend on another domain at all | A question about which parts are composed together, answered there. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| runtime_binding | MODIFIED |
| workflow | MODIFIED |
| design | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| An act that reads records another subdomain of its own domain owns completes, rather than stopping when it runs. |
| An act that would change records it does not own is refused, and the refusal names what it tried to change. |
| A composition in which two subdomains describe one record is refused when it is assembled. |
| An act reaching another subdomain's records states so in its design, and a reviewer can see which boundary it crosses without running it. |
| No subdomain's artifact describes another subdomain's storage. |
| An act that names a place without saying whether it owns it or consults it is refused. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Record description | The records it describes, together with the subdomain that wrote it | They describe the same records for the same subdomain. |
| Reach | The act that reaches and the subdomain reached | One act names one other subdomain, however many records it reads there. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Record description | Sole | Contested | A second subdomain describing a record it does not own | Assembly refuses the composition. Nothing else follows, and no description is preferred over the other. |
| Record description | Contested | Sole | The subdomain that does not own the record withdrawing its description | Assembly proceeds. Nothing else follows. |
| Reach | Undeclared | Declared | The act naming the subdomain whose records it reads | The reach becomes reviewable. Nothing is granted that was not already permitted, because reading was never the thing in doubt. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Changing a record | The act does not own it | Two subdomains deciding what is true leaves neither answerable for the result. |
| Assembling a composition | Two subdomains describe one record | Preferring one description makes the answer depend on the order somebody wrote a list in. |
| Reaching records | They belong to another domain | An act correct only in the compositions that happen to include that domain would compile and fail when it runs. |
| Declaring a reach | The act does not say which places it owns and which it consults | The permission rests on that distinction, and a declaration that hides it cannot be held to it. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Which readers may see which records | A later change | A subdomain needs to hold records some readers may not see. |
| How a subdomain's ownership of a record is declared | A later change | Ownership needs to be stated rather than settled by convention. |
| Whether one domain may depend on another | Whichever change decides what is composed together | A domain needs something another domain holds. |
