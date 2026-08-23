# Stage 4 — Business Model: platform / snapshot
**Stage:** 4 — Business Model
**CR:** composition_identity
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The build | Constitutes a composition and attests what it produced. | Producing — it writes both what constitutes the composition and what accompanies it. | S1 authority_boundaries #2 |
| The snapshot subdomain | Decides what belongs to a composition's identity. | Declaring — the distinction between constituting and accompanying is its to draw. | S1 authority_boundaries #1 |
| The cryptographic trust subdomain | Decides what an attestation states. | Declaring — what the attestation carries is its to state, and this change consumes rather than decides it. | S1 authority_boundaries #3 |
| A reader | Compares two identities and concludes whether two compositions are the same. | Observing — the party a changing identity misleads. | S1 known_facts #10 |
| The runtime | Refuses a composition whose projection does not match what its attestation binds. | Deciding — and the reason the attestation cannot simply be excluded. | S3 verification_results #7 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Composition | Everything a build produces, taken together as one thing. | Assembled from each domain's compiled output into one tree. | S2 entities #1 |
| Identity | The name a composition has, computed from what it carries. | Recomputed from the bytes whenever the composition is verified. | S2 entities #2 |
| Constituent | A file the composition carries as part of what it is. | Enumerated by walking the tree, with a value over each file's bytes. | S2 entities #3 |
| Accompaniment | Something the composition carries that records about it rather than constitutes it. | Two files excluded today, by a named list and a named rule. | S2 entities #4 |
| Pin | A record of the composition a change was validated against. | Twenty-two exist; twenty name a composition that cannot be produced. | S2 entities #5 |
| Attestation | A statement of what a build produced and when it was signed. | One per domain. Two fields constitute, one accompanies. | S3 analysis_findings #1 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The twenty expired pins | Every completed change in the workspace, each naming a composition that cannot be produced. | S2 belief_verification #6 |
| The two existing exclusions | The self-description doing the enumerating, and material written after the composition was constituted. | S2 belief_verification #2 |
| The seven attestations | One per domain, each carrying two determinative fields and one that records when. | S3 analysis_findings #1 |
| The unstable field | A wall-clock moment to the microsecond, written by one stage and read by no mechanism anywhere. | S2 belief_verification #5 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A composition was constituted | A build completing | The composition has an identity a reader may rely on. | S1 business_events #1 |
| A rebuild produced a different composition | Any recompile of unchanged source | The state this change ends. It happens on every build. | S1 lifecycle_states #2 |
| A pin expired | Any domain being rebuilt | Everything grounded on it becomes unverifiable, and nothing announces it. | S1 business_events #3 |
| Two identities were found to differ | A composition being verified against a pin | Today this tells a reader nothing, which is the defect stated as an event. | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Composition | excludes | Accompaniment | Excluding what does not constitute a composition. | S3 authoring_decisions #1 |
| Composition | excludes | Accompaniment | Excluding at the grain of a field. | S3 authoring_decisions #2 |
| Attestation | contributes | Identity | Stating what an attestation contributes to identity. | S3 authoring_decisions #3 |
| Rebuild | reproduces | Identity | Requiring a rebuild to reproduce an identity. | S3 authoring_decisions #4 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Excluding at the grain of a field | S3 authoring_decisions #2 | CRITICAL | GAP-1 | The whole of the fix. Excluding the file instead would drop a binding the runtime enforces. |
| Stating what an attestation contributes to identity | S3 authoring_decisions #3 | CRITICAL | GAP-2 | Nothing says today which of an attestation's fields constitute the composition. |
| Requiring a rebuild to reproduce an identity | S3 authoring_decisions #4 | MAJOR | GAP-3 | Nothing requires it, which is why twenty failing pins went unreported. |
| Excluding what does not constitute a composition | S3 authoring_decisions #1 | SATISFIED | | Two exclusions already exist on exactly this ground, named and read rather than inferred. |
| Refusing a composition whose projection does not match its attestation | S3 dependency_discoveries #4 | SATISFIED | | Already enforced at boot, and the reason the attestation stays a constituent. |
| Declaring the trust arrangement in force | S3 dependency_discoveries #5 | SATISFIED | | Declares the local unsigned arrangement; unchanged. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| snapshot | cryptographic_trust | data read | SATISFIED | S3 dependency_discoveries #3 — the attestation carries the field, and what it states is that subdomain's to declare. |
| snapshot | execution | capability call | SATISFIED | S3 dependency_discoveries #4 — the runtime already refuses a mismatched projection. |
| snapshot | snapshot | data read | SATISFIED | S3 dependency_discoveries #1 — the enumeration of constituents already excludes two named things. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Identity stays a function of the bytes; nothing is weakened to make a pin survive. | S1 constraints #1 | governance rule |
| 2 | A composition altered after sealing is still refused. | S1 constraints #2 | governance rule |
| 3 | A composition moved somewhere it was not built for is still refused. | S1 constraints #3 | governance rule |
| 4 | The record of when a composition was signed is not deleted for being unstable. | S1 constraints #4 | governance rule |
| 5 | What is excluded from the identity is stated, not inferred from where a file sits. | S1 constraints #5 | governance rule |
| 6 | An attestation's determinative fields stay in the identity, because the runtime enforces them. | S3 analysis_findings #1 | domain knowledge |
| 7 | The change claims stability, not reproducibility, because only stability was measured. | S3 analysis_findings #4 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #2 | Excluding at the grain of a field | snapshot | AUTHOR_NEW |
| GAP-2 | S3 authoring_decisions #3 | Stating what an attestation contributes to identity | cryptographic_trust | EXTEND |
| GAP-3 | S3 authoring_decisions #4 | Requiring a rebuild to reproduce an identity | snapshot | AUTHOR_NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The exclusion is of a field, not of the attestation file. | S3 analysis_findings #1 | Two of the attestation's fields bind what was built and the runtime refuses a mismatch against them. Excluding the file would drop an enforced binding from the identity. | Rules out treating the attestation like the two files already excluded, and requires the exclusion to be expressible at a finer grain than a path. |
| 2 | What an attestation contributes to identity is stated by the subdomain that owns the attestation. | S3 authoring_decisions #3 | What the attestation carries is the trust subdomain's to state; which of its fields constitute the composition is consumed by the snapshot subdomain, not decided there. | Rules out a rule on the snapshot side that would restate a fact its owner already states. |
| 3 | The exclusion stays a declaration, read rather than inferred. | S3 analysis_findings #3 | The two existing exclusions are named and carry their ground where the exclusion is made. Nothing is excluded by directory, suffix or convention. | Rules out excluding by pattern, and requires the new exclusion to name its ground as the existing two do. |
| 4 | The change requires a rebuild to reproduce an identity, and claims nothing about reproducibility elsewhere. | S3 analysis_findings #4 | Two builds on one machine minutes apart is what was measured. Requiring more would demand a property nobody has established. | Rules out claiming determinism across machines, and fixes that a further instability would be a further change. |
| 5 | Whether the twenty expired pins keep their approvals is not decided here. | S3 analysis_findings #2 | The ground is established — nothing any of those changes was approved against has moved — and the ruling reaches every completed change in the workspace. | Rules out this change silently revalidating approvals, and rules out it invalidating them. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Excluding at the grain of a field | GAP-1 |
| Stating what an attestation contributes to identity | GAP-2 |
| Requiring a rebuild to reproduce an identity | GAP-3 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Making the signature real | Its own change, with its own subject; this one makes the identity stable whether the signature is a placeholder or not. |
| Establishing reproducibility across machines | Not measured anywhere, and requiring it would demand what nobody has established. |
| Ruling on the approvals recorded against expired pins | A human ruling reaching every completed change, and not one a mechanism makes. |
| Re-pinning the twenty expired dossiers | Follows the ruling, and each is its own dossier's act. |
