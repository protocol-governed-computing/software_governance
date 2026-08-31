# Stage 2 — Domain Model Discovery: platform / snapshot
**Stage:** 2 — Domain Model Discovery
**CR:** composition_identity
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned composition and against the code
that constitutes it. What was searched is recorded, not only what was found. Where a belief came back
narrower or wider than Stage 1 stated it, the correction is recorded against the belief.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Composition | Everything a build produces, taken together as one thing. | Assembled from each domain's compiled output into one tree. | VERIFIED | S1 business_vocabulary #1 |
| Identity | The name a composition has, computed from what it carries. | Recomputed from the bytes on disk whenever the composition is verified; not stored as an authority. | VERIFIED | S1 business_vocabulary #2 |
| Constituent | A file the composition carries as part of what it is. | Enumerated by walking the tree, with a value over each file's bytes. | VERIFIED | S1 business_vocabulary #3 |
| Accompaniment | A file the composition carries that records something about it rather than constituting it. | Two are excluded today, by a named list and a named rule. | VERIFIED | S1 business_vocabulary #4 |
| Pin | A record of the composition a change was validated against. | One file per dossier; twenty-two exist. | VERIFIED | S1 business_vocabulary #5 |
| Attestation | A statement that a composition was signed, and when. | One file per domain, written by the last stage of that domain's build. | VERIFIED | S1 business_vocabulary #6 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Composition | Its artifact count | How many artifacts it carries. Identical across two builds of unchanged source. | VERIFIED | S1 known_facts #6 |
| Composition | Its address map, per domain | What each artifact resolves to. Byte-identical across two builds of unchanged source, for all seven domains. | VERIFIED | S1 known_facts #5 |
| Constituent | Its path and its bytes | What makes it the file it is. Both enter the identity. | VERIFIED | S1 known_facts #1 |
| Attestation | What it binds | The projection the build produced, and a value over it. Both stable across builds. | VERIFIED | S1 system_beliefs #1 |
| Attestation | When it was signed | The wall-clock moment the build ran, to the microsecond. Different on every build. | VERIFIED | S1 known_facts #4 |
| Attestation | Its signature | A placeholder. Reads `STUB_NOT_CRYPTOGRAPHICALLY_SIGNED`, with a placeholder algorithm and key reference. | VERIFIED | S1 system_beliefs #4 |
| Pin | The identity it names | The composition the change was validated against. Twenty of twenty-two name one that cannot be produced. | VERIFIED | S1 system_beliefs #6 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Constituting a composition | Assembling a build's output | The composition exists and has an identity. | VERIFIED | S1 business_events #1 |
| Attesting a domain's build | The last stage of that domain's compile | A statement of what was built, and when it was signed. | VERIFIED | S1 business_vocabulary #6 |
| Verifying a composition | A reader, or the runtime at boot | The composition is what its identity says, or it is refused. | VERIFIED | S1 operation_refusals #1 |
| Pinning a composition | A change, when its phase run begins | A record that later readers may re-check the change against. | VERIFIED | S1 business_vocabulary #5 |
| Reproducing a pinned composition | Nobody, successfully | Rebuilding unchanged source produces a different identity every time. | NOT_FOUND | S1 lifecycle_states #2 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Constituting a composition | 1 | Walk the tree and list every file with a value over its bytes. | The list of constituents. | VERIFIED | S1 known_facts #1 |
| Constituting a composition | 2 | Exclude the self-description doing the enumerating, and material written after the composition was constituted. | Two exclusions, each with a stated ground. | VERIFIED | S1 known_facts #8 |
| Constituting a composition | 3 | Compute the identity from the domains, the constituents and the profile. | The identity. | VERIFIED | S1 known_facts #1 |
| Attesting a domain's build | 4 | Bind the projection the build produced, and a value over it. | Two stable fields. | VERIFIED | S1 system_beliefs #1 |
| Attesting a domain's build | 5 | Record the wall-clock moment, to the microsecond. | One field, different on every build. | VERIFIED | S1 known_facts #4 |
| Verifying a composition | 6 | Recompute the identity from the bytes and compare. | A refusal, or nothing. | VERIFIED | S1 operation_refusals #1 |
| Constituting a composition | 7 | Exclude what merely records when the composition was signed. | Nothing. No step performs this. | NOT_FOUND | S1 business_invariants #4 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| One field of one file makes the identity unstable. | VERIFIED | Two builds of one unchanged domain, each writing ninety-one files, were compared file by file over their bytes. Ninety are identical. The one that differs is that domain's attestation, and within it exactly one field differs: the moment the build ran. Assembling twice without rebuilding produces one identity, so what is unstable is the compile and nothing downstream of it. | S1 system_beliefs #1 |
| Some files are already excluded from the identity, deliberately. | VERIFIED | Two exclusions, each carrying its ground in the code that makes it: the composition's self-description, because it is the thing doing the enumerating and is covered by the identity being taken over the list it produces; and the conformance material, because it is written after the composition has been constituted. The exclusion list is named and read, not inferred from where a file sits. | S1 system_beliefs #2 |
| Nothing else about the composition differs between the two builds. | VERIFIED | With this session's change held aside, the rebuild returns the pinned count of three hundred and ninety-five artifacts, the same seven domains, and an address map byte-identical to the pin for every one of the seven. The identity still differs. | S1 system_beliefs #3 |
| The signature the moment accompanies attests nothing. | VERIFIED | The signature reads `STUB_NOT_CRYPTOGRAPHICALLY_SIGNED`, the algorithm reads `STUB`, and the key reference reads `STUB`. Nothing about the attestation is signed today. | S1 system_beliefs #4 |
| Nothing reads the recorded moment. | VERIFIED | Every consumer of the attestation across the runtime, the assembler and the inspector was searched. The runtime's loader reads the projection binding and the value over it, and refuses a mismatch. No mechanism anywhere reads the moment. It is written, carried into the identity, and read by nobody. | S1 system_beliefs #5 |
| Every pin in the workspace has the same expiry. | VERIFIED | Twenty-two pins exist. **Twenty of them cannot be verified against the composition on disk**, each reporting that the snapshot does not match and no phase may run. The two that verify were taken minutes ago and will fail on the next compile. Every completed change in this workspace names a composition that cannot be produced. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Governs what may be trusted and how | cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0 | States the trust model a composition is built under. | PARTIAL | Says nothing about which parts of an attestation constitute the composition and which accompany it. |
| Requires a trust declaration | cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0 | Requires a build to declare the trust arrangement it runs under. | PARTIAL | Requires the declaration, not that what it records be stable across builds of one source. |
| Declares the unsigned local arrangement | cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0 | Declares the arrangement in force: local, unsigned. | EXACT | Nothing. It is the declaration that makes the placeholder signature admissible, and it is unchanged by this. |
| Requires an artifact to declare a value over its content | compiler::INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0 | Requires every artifact to carry a value computed over its content. | EXACT | Covers an artifact's content. A composition's identity is a different question, taken over files rather than artifacts. |
| Requires an artifact's identity to be consistent wherever it is stated | artifact::INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0 | Requires one artifact to carry one identity everywhere it appears. | PARTIAL | Governs an artifact's identity. A composition's identity is a different question, taken over files rather than artifacts, and nothing states the same requirement for it. |

---

## 5. Gaps

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| A composition's identity counts when it was built. | HIGH | Building unchanged source twice produces two compositions. The identity answers a different question from the one a reader asks it. | VERIFIED | S1 business_invariants #1 |
| No pin in the workspace can be kept. | HIGH | Twenty of twenty-two fail today. Every claim any completed change grounded on its composition is unverifiable, and nothing announced it — each failure surfaces only when someone asks. | VERIFIED | S1 lifecycle_states #2 |
| Two identities differing tells a reader nothing. | HIGH | The identity exists to make an alteration after sealing, or a relocation, detectable. A field that changes on every build makes a genuine alteration and a rebuild indistinguishable. | VERIFIED | S1 business_invariants #3 |
| A field nothing reads is load-bearing for the identity. | MEDIUM | The moment is written by one stage and read by no mechanism anywhere, yet it alone decides whether a composition is the same composition. | VERIFIED | S1 system_beliefs #5 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The distinction the fix needs already exists and is already applied. | Two files are excluded from the identity on the stated ground that they do not constitute the composition. The change extends a distinction the platform already makes rather than introducing one. | VERIFIED | S1 system_beliefs #2 |
| The exclusion is by declaration, not by inference. | What is excluded is a named list plus one named file, read by the walk. Nothing is excluded because of where it sits or what it is called. | VERIFIED | S1 constraints #5 |
| The instability is in the compile, not the assembly. | Assembling the same compiled output twice produces one identity. Compiling the same source twice does not. | VERIFIED | S1 known_facts #7 |
| A build's determination record carries a moment and does not reach the identity. | The record written per build states when it was determined, and it is not a constituent, so the same kind of field is already held outside what constitutes the composition. | VERIFIED | S1 known_facts #8 |
| The moment is separable from what the attestation binds. | The attestation carries two stable fields that bind the build's projection, and one unstable field that records when. Nothing in the file couples them. | VERIFIED | S1 system_beliefs #1 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Other unstable fields may exist in files no build has yet rewritten. | Two builds of one domain were compared. The comparison would not see a field that changes only under some other condition — a different machine, a different interpreter, a different day. | MEDIUM | INSUFFICIENT_EVIDENCE | S1 known_facts #3 |
| The failure is silent until someone asks. | Twenty pins have been failing for an unknown length of time and nothing reported it. A pin is checked only when a phase runs against it. | MEDIUM | VERIFIED | S1 system_beliefs #6 |
| Whether an expired pin's approvals still stand is undecided. | Fifteen registers were approved against a composition that can no longer be produced, for each of two completed changes in this session alone. | HIGH | VERIFIED | S1 out_of_scope #3 |

---

## 8. Open Questions

<!-- register:open_questions business_language -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Does an attestation belong to the composition it attests, or accompany it? | GOVERNANCE | Discovery sharpened this rather than answering it. The file carries two fields that bind what was built and one that records when it was signed, and nothing couples them. Excluding the file and removing the field are both available and they are not the same act. | S1 clarification_requests #1 |
| Do the approvals recorded against the twenty expired pins still stand? | GOVERNANCE | The pins failed because the identity was unstable, not because anything they name changed. Whether that distinction preserves the approvals is a ruling, and it reaches every completed change in the workspace. | S1 out_of_scope #3 |
