# Stage 1 — Change Request: Clarification & Fact Capture: platform / snapshot
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** composition_identity
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
| snapshot | MODIFY | A composition's identity counts a record of when it was built, so building the same source twice produces two compositions. What belongs to the identity is restated to exclude what accompanies a composition rather than constituting it. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Composition | Everything a build produces, taken together as one thing. | CR seed §2 Business Vocabulary #1 |
| Identity | The name a composition has, computed from what it carries. | CR seed §2 Business Vocabulary #2 |
| Constituent | A file the composition carries as part of what it is. | CR seed §2 Business Vocabulary #3 |
| Accompaniment | A file the composition carries that records something about it rather than constituting it. | CR seed §2 Business Vocabulary #4 |
| Pin | A record of the composition a change was validated against. | CR seed §2 Business Vocabulary #5 |
| Attestation | A statement that a composition was signed, and when. | CR seed §2 Business Vocabulary #6 |
| Rebuild | Building again from source that has not changed. | CR seed §2 Business Vocabulary #7 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Building unchanged source twice produces one identity, not two. | CR seed §3 Requested Outcomes #1 |
| A pin taken today can be verified after a rebuild. | CR seed §3 Requested Outcomes #2 |
| Two identities differing means the composition differs. | CR seed §3 Requested Outcomes #3 |
| A composition altered after it was sealed is still caught by recomputing its identity. | CR seed §3 Requested Outcomes #4 |
| What belongs to a composition's identity is declared rather than inferred from where a file sits. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A composition's identity is computed over the bytes of every file it carries. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Two builds of one unchanged domain produce two identities. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Ninety-one files are written by each build and ninety are byte-identical. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The one that differs records the moment the build ran, to the microsecond. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Every domain's map of what it carries is byte-identical across the two builds. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The count of artifacts is identical across the two builds. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Assembling twice without rebuilding produces one identity, so what is unstable is the compile. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| Two files are already excluded from the identity because they are written after the composition is constituted. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A pin names a composition and is the only way a later reader can re-check what a change rested on. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A pin cannot survive a rebuild, and rebuilding is the ordinary act of working. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| The signature accompanying the moment is a placeholder and signs nothing today. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| Identity over bytes is what makes an alteration after sealing, or a relocation, detectable. | HIGH | CR seed §4 Known Facts — Business Truths #12 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| One field of one file makes the identity unstable. | The whole of this change. | Confirm the field, and confirm no other file differs across two builds of unchanged source. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Some files are already excluded from the identity, deliberately. | Decides whether the change extends an existing distinction or invents one. | Establish which are excluded and on what stated ground. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Nothing else about the composition differs between the two builds. | Says the defect is the field and not something the field stands for. | Compare the artifact count, the domains and each domain's address map across both. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The signature the moment accompanies attests nothing. | Decides whether the moment is load-bearing for anything today. | Establish what the signature is and what reads it. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Nothing reads the recorded moment. | Decides whether the field may be excluded, derived or removed. | Establish every consumer of the attestation and which of its fields each reads. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| Every pin in the workspace has the same expiry. | Says whether this reaches one change or all of them. | Establish how many pins exist and whether any can be verified against the composition on disk. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| Recording when a composition was signed is worth keeping. | It is what an attestation is for, once the signature is real. | CR seed §6 Assumptions #1 |
| The distinction between constituting a composition and accompanying it is already understood. | Two files are excluded from the identity today on exactly that ground. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Identity stays a function of the bytes; nothing is weakened to make a pin survive. | Business author | CR seed §7 Constraints #1 |
| A composition altered after sealing is still refused. | Business author | CR seed §7 Constraints #2 |
| A composition moved somewhere it was not built for is still refused. | Business author | CR seed §7 Constraints #3 |
| The record of when a composition was signed is not deleted for being unstable. | Business author | CR seed §7 Constraints #4 |
| What is excluded from the identity is stated, not inferred from where a file sits. | Business author | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A composition's identity is a function of what it contains and of nothing else. | CR seed §8 Business Invariants #1 |
| Building unchanged source twice produces one identity. | CR seed §8 Business Invariants #2 |
| Two identities differing means the compositions differ. | CR seed §8 Business Invariants #3 |
| What accompanies a composition is excluded from its identity by declaration. | CR seed §8 Business Invariants #4 |
| An alteration after sealing changes the identity. | CR seed §8 Business Invariants #5 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Pin | Verifiable | The composition it names can be produced from source. | CR seed §9 Lifecycle States #1 |
| Pin | Expired | The composition it names cannot be produced again, though the source is unchanged. This is the state this change ends. | CR seed §9 Lifecycle States #2 |
| Composition | Constituted | Built, with an identity taken over what it carries. | CR seed §9 Lifecycle States #3 |
| Composition | Accompanied | Carrying files that record something about it and do not constitute it. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A composition was constituted | When a build completes | The composition has an identity a reader may rely on. | CR seed §10 Business Events #1 |
| Two identities were found to differ | When a composition is verified against a pin | Something about the composition differs, and today that conclusion is not safe to draw. | CR seed §10 Business Events #2 |
| A pin expired | When any domain is rebuilt | Everything grounded on that pin becomes unverifiable, silently. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What belongs to a composition's identity | The snapshot subdomain | CR seed §11 Authority Boundaries #1 |
| What a composition carries | The build | CR seed §11 Authority Boundaries #2 |
| What an attestation states | The cryptographic trust subdomain | CR seed §11 Authority Boundaries #3 |
| Whether a pin is verifiable | Whoever recomputes the identity | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Making the signature real | Its own change, with its own subject; this one makes the identity stable whether the signature is a placeholder or not. | CR seed §12 Out of Scope #1 |
| What a composition should contain | Each domain's business. | CR seed §12 Out of Scope #2 |
| Whether an expired pin's approvals stand | A separate ruling, and not one a mechanism makes. | CR seed §12 Out of Scope #3 |
| The identity of anything other than a composition | Artifacts and domains have their own identities and are not affected. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| snapshot | MODIFIED | CR seed §13 Governance Scope #1 |
| cryptographic_trust | ADJACENT | CR seed §13 Governance Scope #2 |
| compiler | ADJACENT | CR seed §13 Governance Scope #3 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| Does an attestation belong to the composition it attests, or accompany it? | Decides whether the fix excludes the file or removes the field. | NO | GOVERNANCE | CR seed §14 Clarification Requests #1 |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| Two builds of unchanged source produce one identity. | CR seed §15 Acceptance Criteria #1 |
| A pin taken before a rebuild verifies after it. | CR seed §15 Acceptance Criteria #2 |
| A composition whose file is altered after sealing is refused. | CR seed §15 Acceptance Criteria #3 |
| A composition moved to a place it was not built for is refused. | CR seed §15 Acceptance Criteria #4 |
| The record of when a composition was signed is still written. | CR seed §15 Acceptance Criteria #5 |
| What is excluded from the identity can be read from a declaration rather than inferred. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Composition | Its identity | Two identities are equal, and today that is not sufficient to conclude they are the same. | CR seed §16 Identity and Sameness #1 |
| Constituent | Its path within the composition and its bytes | Both are equal. | CR seed §16 Identity and Sameness #2 |
| Pin | The composition it names | Two pins name one identity. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Pin | Expired | Verifiable | The identity ceasing to count what accompanies the composition. | Every pin in the workspace becomes verifiable against a rebuild. Nothing about what was approved changes. | CR seed §17 Lifecycle Transitions #1 |
| Composition | Constituted | Constituted | A rebuild from unchanged source. | The identity is the same identity, which is what makes the rebuild a rebuild rather than a new composition. | CR seed §17 Lifecycle Transitions #2 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Verifying a composition | A file it carries as a constituent does not match the bytes its identity was taken over | The composition was altered after it was sealed, and a reader relying on the identity would be relying on something that is no longer there. | CR seed §18 Operation Refusals #1 |
| Verifying a composition | It is read somewhere other than where its identity says it was built for | A composition that answers correctly in a place it was never constituted for is a composition nobody can locate. | CR seed §18 Operation Refusals #2 |
| Verifying a composition against a pin | The identity differs | Something about the composition differs from what the change was validated against, and every claim resting on it must be re-checked. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| What an attestation states and how it is signed | cryptographic_trust | That subdomain raises the change that makes the signature real. | CR seed §19 Authority Deferrals #1 |
| Whether an expired pin's approvals stand | A human ruling | Each affected change is taken up on its own terms. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
