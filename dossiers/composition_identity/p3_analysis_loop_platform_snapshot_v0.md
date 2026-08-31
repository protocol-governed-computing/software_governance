# Stage 3 — Analysis Loop: platform / snapshot
**Stage:** 3 — Analysis Loop
**CR:** composition_identity
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

The two questions Stage 2 left open, closed against the pinned composition; every belief it verified,
re-grounded rather than carried.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | **An attestation both constitutes and accompanies, and the file is the wrong unit to decide about.** Two of its fields bind what was built — the projection and a value over it — and the runtime refuses a composition whose projection does not match them. Those constitute. One field records when the signing happened, is read by nothing, and changes on every build. That accompanies. Excluding the whole file would drop a binding the runtime enforces from the identity, which is the opposite of what this change wants. | Settles the shape: the exclusion is of a field, not of a file. The existing exclusions are whole files because those files carry nothing determinative; this one does. | OBSERVED | HIGH | CLOSED | The runtime's loader reads the projection binding and refuses a mismatch. Nothing anywhere reads the moment. The two are in one file and nothing couples them. |
| Q2 | **The twenty pins failed for a reason that does not touch what they name.** A pin records an identity so a later reader can re-check what a change rested on. Every one of the twenty names a composition whose artifacts, domains and address maps are reproducible; what is not reproducible is a timestamp written beside them. Nothing any of those changes was approved against has moved. | Bears directly on whether the approvals stand, which is the second open question and is a ruling rather than a derivation. This finding supplies the ground for it and does not make it. | OBSERVED | HIGH | CLOSED | Holding this session's change aside, a rebuild returns the pinned artifact count and an address map byte-identical to the pin for all seven domains, and the identity still differs. |
| Q3 | **The fix is available today and its precedent is exact.** Two files are already outside the identity, each because it does not constitute the composition — one is the self-description doing the enumerating, the other is written after the composition was constituted. Both are named, both carry their ground, and neither is inferred from where a file sits. A field excluded on the same ground is the same act at a finer grain. | Fixes that the change extends an existing distinction rather than introducing one, and that what is excluded stays declared. | OBSERVED | HIGH | CLOSED | The exclusion is a named list plus one named file, read by the walk that enumerates constituents. Nothing is excluded by directory, by suffix or by convention. |
| Q4 | **Stability is not the same as reproducibility, and only stability is established.** Two builds on one machine, minutes apart, differ in one field. That the remaining ninety files are identical across those two builds does not establish that they would be identical on another machine, another interpreter, or another day. The change can require that a rebuild reproduce an identity; it cannot claim that property has been measured anywhere but here. | Fixes what the change may assert. It removes a known cause of instability and states honestly that it has not established there is no other. | INFERRED | MEDIUM | CLOSED | The comparison was two builds of one domain in one session. Nine other build configurations were never compared, and no comparison across machines was attempted. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| One field of one file makes the identity unstable. | S2 belief_verification #1 | CONFIRMED | Re-compared over the bytes: ninety-one files per build, ninety identical, one differing in one field. |
| Some files are already excluded from the identity, deliberately. | S2 belief_verification #2 | CONFIRMED | Two exclusions, each named and each carrying its ground where the exclusion is made. |
| Nothing else about the composition differs between the two builds. | S2 belief_verification #3 | CONFIRMED | Artifact count, domain list and all seven address maps identical to the pin. |
| The signature the moment accompanies attests nothing. | S2 belief_verification #4 | CONFIRMED | Signature, algorithm and key reference are all placeholders. |
| Nothing reads the recorded moment. | S2 belief_verification #5 | CONFIRMED | Re-searched across the runtime, the assembler and the inspector. The loader reads the projection binding; nothing reads the moment. |
| Every pin in the workspace has the same expiry. | S2 belief_verification #6 | CONFIRMED | Twenty-two pins; twenty refuse to verify, and the two that verify were taken in this session. |
| The attestation carries determinative content as well as the unstable field. | S3 analysis_findings #1 | CONFIRMED | The runtime refuses a composition whose projection does not match what the attestation binds, so the file cannot simply be excluded. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| The enumeration of what a composition carries | capability | EXTEND | Walks the tree and excludes two named things. The change adds what is excluded at the grain of a field. |
| The declaration of what does not constitute a composition | governance | EXTEND | Exists as a named list with its ground stated. The change states one more ground and one more exclusion. |
| The attestation a build writes | data | EXTEND | Carries two determinative fields and one that records when. The change reaches only the third. |
| The runtime's refusal of a mismatched projection | capability | REUSE | Already refuses a composition whose projection does not match what the attestation binds. Unchanged, and the reason the file stays a constituent. |
| The trust arrangement in force | governance | REUSE | Declares the local unsigned arrangement that makes a placeholder signature admissible. Unchanged. |
| Whether an expired pin's approvals stand | governance | INVESTIGATE | A ruling reaching every completed change in the workspace, and not one a mechanism makes. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | States the trust model a build runs under. Gains what an attestation may contribute to a composition's identity. | 1 | Reported by the composition. |
| cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0 | Requires a build to declare its trust arrangement. Unchanged. | 0 | Reported by the composition. |
| cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0 | Declares the arrangement in force. Unchanged. | 0 | Reported by the composition. |
| The enumeration of constituents | Every composition, on every build, in every domain. | — | One place computes the identity, and it is where the exclusion is stated. |
| Every pin in the workspace | Twenty become verifiable against a rebuild; two already are. | 22 | Every pin was run against the composition on disk. |
| The attestation of every domain | Seven files, one field each. What each binds is unchanged. | — | One per domain, written by the last stage of that domain's build. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|-----------|----------|-----------|---------------------|----------------|
| Excluding what does not constitute a composition | EXTEND | Two exclusions already exist on exactly this ground, named and read rather than inferred. Adding a third is the same act. | A new mechanism for stable identity was considered and rejected: the distinction and the place to state it both already exist. | analysis_findings #3 |
| Excluding at the grain of a field | AUTHOR_NEW | The existing exclusions are whole files because those files carry nothing determinative. The attestation carries a binding the runtime enforces, so excluding the file would weaken the identity. | Excluding the attestation file was checked and rejected: it would drop the projection binding from the identity. | analysis_findings #1 |
| Stating what an attestation contributes to identity | EXTEND | The constitution that governs trust is where a reader looks for what an attestation is. Nothing there says which of its fields constitute the composition. | A rule on the snapshot side was considered and rejected: what an attestation carries is the trust subdomain's to state, and the snapshot subdomain's to consume. | analysis_findings #1 |
| Requiring a rebuild to reproduce an identity | AUTHOR_NEW | Nothing requires it today, which is why nothing reported twenty failing pins. | Requiring full reproducibility across machines was considered and rejected: it has not been measured and would demand what nobody has established. | analysis_findings #4 |

---

## 6. Placement Decision

<!-- register:placement_decision -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | snapshot | What belongs to a composition's identity is what this subdomain governs. What an attestation states belongs to the trust subdomain and is consumed here, not decided here. | S1 governance_scope #1 |

---

## 7. Discovery Saturation

<!-- register:saturation -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| Every question Stage 2 left open is closed. | SATISFIED | The exclusion is of a field rather than a file, and the ground for ruling on the expired approvals is established without the ruling being made here. |
| Every belief Stage 2 verified was re-grounded. | SATISFIED | All six confirmed against the composition and the code that constitutes it; none overturned. A seventh was added and confirmed. |
| The cause is established to one field of one file. | SATISFIED | Ninety of ninety-one files identical across two builds; one field of the ninety-first differs. |
| The blast radius is established. | SATISFIED | Twenty-two pins, seven attestations, one place where identity is computed. Nothing else is reached. |
| What the change may claim is bounded. | SATISFIED | It removes a known cause of instability. It does not claim reproducibility has been established anywhere but on one machine in one session. |
