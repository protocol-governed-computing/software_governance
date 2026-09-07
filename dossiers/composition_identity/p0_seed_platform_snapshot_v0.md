# Change Seed — platform / snapshot

**Stage:** 0 — Change Seed
**CR:** composition_identity
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The snapshot subdomain governs what a built composition is: the files it carries, the identity that
names it, and what a reader may conclude from two identities being the same or different. Its
authority is to decide what belongs to a composition's identity and what merely accompanies it. It
decides nothing about what any composition contains.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| snapshot | MODIFY | A composition's identity counts a record of when it was built, so building the same source twice produces two compositions. What belongs to the identity is restated to exclude what accompanies a composition rather than constituting it. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Composition | Everything a build produces, taken together as one thing. |
| Identity | The name a composition has, computed from what it carries. |
| Constituent | A file the composition carries as part of what it is. |
| Accompaniment | A file the composition carries that records something about it rather than constituting it. |
| Pin | A record of the composition a change was validated against. |
| Attestation | A statement that a composition was signed, and when. |
| Rebuild | Building again from source that has not changed. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Building unchanged source twice produces one identity, not two. |
| A pin taken today can be verified after a rebuild. |
| Two identities differing means the composition differs. |
| A composition altered after it was sealed is still caught by recomputing its identity. |
| What belongs to a composition's identity is declared rather than inferred from where a file sits. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A composition's identity is computed over the bytes of every file it carries. | HIGH |
| Two builds of one unchanged domain produce two identities. | HIGH |
| Ninety-one files are written by each build and ninety are byte-identical. | HIGH |
| The one that differs records the moment the build ran, to the microsecond. | HIGH |
| Every domain's map of what it carries is byte-identical across the two builds. | HIGH |
| The count of artifacts is identical across the two builds. | HIGH |
| Assembling twice without rebuilding produces one identity, so what is unstable is the compile. | HIGH |
| Two files are already excluded from the identity because they are written after the composition is constituted. | HIGH |
| A pin names a composition and is the only way a later reader can re-check what a change rested on. | HIGH |
| A pin cannot survive a rebuild, and rebuilding is the ordinary act of working. | HIGH |
| The signature accompanying the moment is a placeholder and signs nothing today. | HIGH |
| Identity over bytes is what makes an alteration after sealing, or a relocation, detectable. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| One field of one file makes the identity unstable. | The whole of this change. | Confirm the field, and confirm no other file differs across two builds of unchanged source. |
| Some files are already excluded from the identity, deliberately. | Decides whether the change extends an existing distinction or invents one. | Establish which are excluded and on what stated ground. |
| Nothing else about the composition differs between the two builds. | Says the defect is the field and not something the field stands for. | Compare the artifact count, the domains and each domain's address map across both. |
| The signature the moment accompanies attests nothing. | Decides whether the moment is load-bearing for anything today. | Establish what the signature is and what reads it. |
| Nothing reads the recorded moment. | Decides whether the field may be excluded, derived or removed. | Establish every consumer of the attestation and which of its fields each reads. |
| Every pin in the workspace has the same expiry. | Says whether this reaches one change or all of them. | Establish how many pins exist and whether any can be verified against the composition on disk. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| Recording when a composition was signed is worth keeping. | It is what an attestation is for, once the signature is real. |
| The distinction between constituting a composition and accompanying it is already understood. | Two files are excluded from the identity today on exactly that ground. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Identity stays a function of the bytes; nothing is weakened to make a pin survive. | Business author |
| A composition altered after sealing is still refused. | Business author |
| A composition moved somewhere it was not built for is still refused. | Business author |
| The record of when a composition was signed is not deleted for being unstable. | Business author |
| What is excluded from the identity is stated, not inferred from where a file sits. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A composition's identity is a function of what it contains and of nothing else. |
| Building unchanged source twice produces one identity. |
| Two identities differing means the compositions differ. |
| What accompanies a composition is excluded from its identity by declaration. |
| An alteration after sealing changes the identity. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Pin | Verifiable | The composition it names can be produced from source. |
| Pin | Expired | The composition it names cannot be produced again, though the source is unchanged. This is the state this change ends. |
| Composition | Constituted | Built, with an identity taken over what it carries. |
| Composition | Accompanied | Carrying files that record something about it and do not constitute it. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A composition was constituted | When a build completes | The composition has an identity a reader may rely on. |
| Two identities were found to differ | When a composition is verified against a pin | Something about the composition differs, and today that conclusion is not safe to draw. |
| A pin expired | When any domain is rebuilt | Everything grounded on that pin becomes unverifiable, silently. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What belongs to a composition's identity | The snapshot subdomain |
| What a composition carries | The build |
| What an attestation states | The cryptographic trust subdomain |
| Whether a pin is verifiable | Whoever recomputes the identity |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Making the signature real | Its own change, with its own subject; this one makes the identity stable whether the signature is a placeholder or not. |
| What a composition should contain | Each domain's business. |
| Whether an expired pin's approvals stand | A separate ruling, and not one a mechanism makes. |
| The identity of anything other than a composition | Artifacts and domains have their own identities and are not affected. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| snapshot | MODIFIED |
| cryptographic_trust | ADJACENT |
| compiler | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| Does an attestation belong to the composition it attests, or accompany it? | Decides whether the fix excludes the file or removes the field. | NO | GOVERNANCE |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Two builds of unchanged source produce one identity. |
| A pin taken before a rebuild verifies after it. |
| A composition whose file is altered after sealing is refused. |
| A composition moved to a place it was not built for is refused. |
| The record of when a composition was signed is still written. |
| What is excluded from the identity can be read from a declaration rather than inferred. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Composition | Its identity | Two identities are equal, and today that is not sufficient to conclude they are the same. |
| Constituent | Its path within the composition and its bytes | Both are equal. |
| Pin | The composition it names | Two pins name one identity. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Pin | Expired | Verifiable | The identity ceasing to count what accompanies the composition. | Every pin in the workspace becomes verifiable against a rebuild. Nothing about what was approved changes. |
| Composition | Constituted | Constituted | A rebuild from unchanged source. | The identity is the same identity, which is what makes the rebuild a rebuild rather than a new composition. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Verifying a composition | A file it carries as a constituent does not match the bytes its identity was taken over | The composition was altered after it was sealed, and a reader relying on the identity would be relying on something that is no longer there. |
| Verifying a composition | It is read somewhere other than where its identity says it was built for | A composition that answers correctly in a place it was never constituted for is a composition nobody can locate. |
| Verifying a composition against a pin | The identity differs | Something about the composition differs from what the change was validated against, and every claim resting on it must be re-checked. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| What an attestation states and how it is signed | cryptographic_trust | That subdomain raises the change that makes the signature real. |
| Whether an expired pin's approvals stand | A human ruling | Each affected change is taken up on its own terms. |
