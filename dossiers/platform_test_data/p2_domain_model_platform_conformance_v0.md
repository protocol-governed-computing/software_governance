# Stage 2 — Domain Model Discovery: platform / conformance

**Stage:** 2 — Domain Model Discovery
**CR:** platform_test_data
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned baseline
`d3e4fbf45009e0661bba3f964c1a026b41e9cbdb7d485973e74644d655ac05a8` — 414 artifacts across seven
domains — read through the inspection interface, and against the compiler, runner and assembler that
build, prove and compose it. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Platform transform | A transform the platform declares and implements once, which any domain may carry. | Declared and implemented in the platform and sealed by each of its builds; twelve are in the composition, none with a vector. | OBSERVED | S1 business_vocabulary #2 |
| Carried transform | A platform transform a domain uses; the domain's build names it and does not test it. | Copied into a domain's build when one of the domain's own declarations references it; nine of the twelve are carried by some domain, and three by none. | OBSERVED | S1 business_vocabulary #4 |
| Test vector | Stated inputs and the outputs a transform must produce from them. | A declaration kind a build compiles into runnable cases when the build discovers it; none is carried by the composition. | OBSERVED | S1 business_vocabulary #5 |
| Inherited case | A case brought across from the reference implementation. | Held outside the composition, in prose, by the reference implementation; fifty-three cases for the eleven platform transforms. | OBSERVED | S1 business_vocabulary #7 |
| Platform build | The build in which the platform's declarations are compiled. | Three build declarations, a reference one and two placement ones, each compiling the same platform transforms. | OBSERVED | S1 business_vocabulary #13 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Test vector | Target | The transform it tests, named by identity. | OBSERVED | S1 business_vocabulary #5 |
| Test vector | Cases | Each case's inputs, expected outcome and expected outputs. | OBSERVED | S1 business_vocabulary #6 |
| Inherited case | Standing | Whether it holds as written against the current declaration and implementation. | INFERRED | S1 lifecycle_states #4 |
| Platform transform | Supplier | The platform, which declares and implements it. | OBSERVED | S1 business_vocabulary #3 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Build the platform | The platform's build step | The platform is compiled; nothing runs after the compile. | OBSERVED | S1 system_beliefs #4 |
| Prove a build's transforms | A domain's build step, after its compile | Each transform whose namespace is the build's scope is named proven, unproven or refused; every other is named carried, whatever its cases did. | OBSERVED | S1 system_beliefs #5 |
| Compose the snapshot | The assembler | Every projection each build wrote is carried under that build's name, conformance results included. | OBSERVED | S1 system_beliefs #6 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Prove a build's transforms | 1 | Run every runnable case the build wrote | A pass or a failure per case | OBSERVED | S1 system_beliefs #5 |
| Prove a build's transforms | 2 | Classify each transform whose namespace is the build's scope by its cases | Proven, unproven or refused | OBSERVED | S1 system_beliefs #5 |
| Prove a build's transforms | 3 | Name every other transform as carried, without reading its cases | The carried list | OBSERVED | S1 system_beliefs #5 |
| Prove a build's transforms | 4 | Admit the build when nothing classified was refused | The build's result | OBSERVED | S1 system_beliefs #5 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| No platform transform has a vector in the composition. | VERIFIED | si.artifact.list --kind TEST_DATA answers NOT_FOUND: "no artifact of kind 'TEST_DATA' in this composition". | S1 system_beliefs #1 |
| The eleven platform transforms keep the codes the reference implementation's vectors name. | VERIFIED | Each of the eleven is sealed in the platform under the capability_transforms namespace with the code its inherited vector names. The platform seals a twelfth, capability_transforms::CT_PURE_COMPARE_EQUAL_V0, which no inherited vector tests. | S1 system_beliefs #2 |
| The platform's build does not discover vectors and declares no place for runnable cases. | VERIFIED | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1, structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 and structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 each list the kinds they discover without the vector kind, and none declares a conformance place. The reference build's declaration says implementation-layer conformance is out of its scope. | S1 system_beliefs #3 |
| The platform's build step does not run conformance. | VERIFIED | The platform's build step hands control to the compiler and ends with it. A domain's build step runs the compile and then the runner, stopping on either's failure. | S1 system_beliefs #4 |
| The runner takes a transform as a build's own only when its namespace is the build's scope. | VERIFIED | The runner reads the build's scope from its build declaration and counts a transform as the build's own when the transform's namespace equals it. The platform's scope is platform and its transforms are named capability_transforms, so every one would be named carried and none judged. The runner admits a build when nothing it classified was refused, so a failed case for a carried transform is run and admitted. | S1 system_beliefs #5 |
| The platform's conformance result would be carried into the snapshot as a domain's is. | VERIFIED | The assembler carries every projection kind each build wrote, under that build's name, and names no kind; a platform result would arrive at the same place a domain's does. The assembler's evidence check asserts that no platform result is carried, on the ground that the platform's build runs none. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Governs test vectors | conformance::CONSTITUTION_TEST_DATA_V1 | States what a vector is, that a transform no vector tests is unproven, and that vectors run in the supplying domain's build. | EXACT | Nothing this change needs; the platform is the supplying domain of its own transforms. |
| Declares the platform's reference build | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | Compiles the platform without a vector layer or conformance, and says implementation-layer conformance is out of its scope. | PARTIAL | Does not discover the vector kind or declare a place for runnable cases. |
| Declares the platform's federated build | structure::STRUCTURE_BUILD_PLATFORM_FEDERATED_CONFIG_V1 | Compiles the platform for federated placement. | PARTIAL | Does not discover the vector kind or declare a place for runnable cases. |
| Declares the platform's multi-worker build | structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V1 | Compiles the platform for multi-worker scheduling. | PARTIAL | Does not discover the vector kind or declare a place for runnable cases. |
| Assembles a record from fields | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | A platform transform with two inherited cases. | EXACT | Has no vector in the composition. |
| Emits an event payload | capability_transforms::CT_EXEC_EMIT_V0 | A platform transform with fifteen inherited cases; carried by no domain. | EXACT | Has no vector in the composition. |
| Extracts a field | capability_transforms::CT_PURE_EXTRACT_V0 | A platform transform with three inherited cases. | EXACT | Has no vector in the composition. |
| Filters records | capability_transforms::CT_PURE_FILTER_RECORDS_V0 | A platform transform with four inherited cases. | EXACT | Has no vector in the composition. |
| Generates an identifier | capability_transforms::CT_PURE_GENERATE_ID_V0 | A platform transform with four inherited cases. | EXACT | Has no vector in the composition. |
| Looks up a key | capability_transforms::CT_PURE_LOOKUP_V0 | A platform transform with four inherited cases. | EXACT | Has no vector in the composition. |
| Maps a result to an HTTP response | capability_transforms::CT_PURE_MAP_RESULT_TO_HTTP_V0 | A platform transform with six inherited cases; carried by no domain. | EXACT | Has no vector in the composition. |
| Passes a value through | capability_transforms::CT_PURE_PASSTHROUGH_V0 | A platform transform with five inherited cases; carried by no domain. | EXACT | Has no vector in the composition. |
| Validates parameter rules | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | A platform transform with two inherited cases. | EXACT | Has no vector in the composition. |
| Validates a record's structure | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | A platform transform with two inherited cases. | EXACT | Has no vector in the composition. |
| Validates set membership | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | A platform transform with two inherited cases. | EXACT | Has no vector in the composition. |
| Compares two values | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | A platform transform with no inherited case. | EXACT | Has no vector, and none is written here. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| None of the platform's three builds discovers vectors or declares a place for runnable cases. | CRITICAL | A vector declared with the platform is never compiled. | OBSERVED | S2 belief_verification #3 |
| The platform's build step ends at the compile. | CRITICAL | The platform's vectors would be compiled and never run. | OBSERVED | S2 belief_verification #4 |
| The runner judges a transform only when its namespace is the build's scope. | CRITICAL | Every platform transform would be named carried by the build that supplies it, and none judged. | OBSERVED | S2 belief_verification #5 |
| The runner admits a build whose case for a carried transform failed. | MAJOR | A failed case can be run and ignored. | OBSERVED | S2 belief_verification #5 |
| The inherited cases are in prose and name targets by identities that no longer exist. | MAJOR | None can be compiled as written. | OBSERVED | S1 known_facts #19 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The constitution governing vectors already places a transform's proof in its supplier's build, so proving the platform's transforms in the platform's build needs no new rule. | conformance::CONSTITUTION_TEST_DATA_V1 | OBSERVED | S1 known_facts #7 |
| The reference build's declaration scopes out implementation-layer conformance as a whole, which is the broader reading the problem statement corrects. | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | OBSERVED | S2 belief_verification #3 |
| The assembler names no projection kind, so a platform result is carried with no change to it; only its evidence check asserts the opposite. | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | INFERRED | S2 belief_verification #6 |
| Three platform transforms are carried by no domain, each with inherited vectors, so the platform's build is the only place they can be proven. | capability_transforms::CT_EXEC_EMIT_V0 | OBSERVED | S1 known_facts #15 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| A build declaration is immutable within its version, so each of the three platform build declarations needs a new version, and each composition's build step names the version it builds. | structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1 | MAJOR | INFERRED | S2 gaps #1 |
| Telling a build's own transforms from carried ones by what the build declares, rather than by namespace, changes the classification every domain's result is written with. | conformance::CONSTITUTION_TEST_DATA_V1 | MINOR | INFERRED | S2 gaps #3 |
| Admitting a build whose carried transform's case failed is a defect in delivered work, found here rather than introduced by this change. | conformance::CONSTITUTION_TEST_DATA_V1 | MAJOR | OBSERVED | S2 gaps #4 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
