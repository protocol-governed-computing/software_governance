# Delivery — platform_test_data

**Authorized by:** Gate 1, closed at P6 against composition `d3e4fbf45009…`
**Delivered:** the platform proves the transforms it supplies, in each of its three builds, against
eleven vectors restated from the reference implementation and re-judged; every build tells what it
supplies from what it carries by the record its compile makes, never by a name; and a failed case
refuses its build, whoever supplies the transform
**Unblocks:** the ai_governance change for its own inherited vectors, and the conformance workload's
declared-iteration change

---

## What was authored

**`CONSTITUTION_TEST_DATA_V2`.** A transform's vectors run in its supplier's build. For the
platform's own transforms that means every platform build, and the platform's build never proves a
domain's. A vector is gated the way its transform is: rendered from a design for a domain, and
authored under the dossier that gates it for the platform. What a build carried is a fact its compile
records, and a failed case refuses the build that ran it. Every other rule of V1 stands.

**V1 was deleted, not superseded.** A superseded V1 would have kept "never in the platform's own
build" in the surface beside a version that says the opposite. Nothing compiled named it.

**`SCHEMA_TEST_DATA_V1`.** V0 pinned `governed_by` to the V1 constitution, so the schema was versioned
with it. V0 was deleted and the dispatch entry repointed. The delivery plan did not foresee this; the
business author ruled on it during delivery.

**`STRUCTURE_BUILD_PLATFORM_{,FEDERATED_,MULTIWORKER_}CONFIG_V2`.** Each is its V1 with the vector
kind discovered and a place declared for runnable cases. The reason V1 gave, that implementation-layer
conformance is out of scope, is narrowed to a domain's implementations. The three V1s were deleted,
because a superseded V1 would stay buildable and leave a way to build the platform unproven.

**Eleven vectors in `capability_transforms/registry/test_data/`,** one per platform transform with
inherited cases, beside the transforms they test. The twelfth platform transform,
`CT_PURE_COMPARE_EQUAL_V0`, has none and stays unproven.

**The compiler.**
- It no longer skips vectors when it writes a build's canonical output, so a vector is a declaration
  in the snapshot like any other.
- A build's attestation records the capabilities the build carried in, as `imported_capabilities`,
  beside the governance it imported.
- `compile.sh` runs conformance after the compile. It tells the runner where the build wrote and which
  of the platform's build declarations it built.

**The runner.**
- What a build supplies is read from its attestation, never from a transform's name.
- A build is admitted only when no case failed.
- It takes a build's own output root, and the name of its build declaration when the build compiled
  more than one.

**The assembler** needed no change. Its evidence check now covers the platform's result, and checks
every build's carried list against its attestation.

---

## Re-judgement of the inherited cases

Every inherited case was restated in the Machine block and judged by the platform's own build: first
by the compiler, against the four invariants over vectors, and then by the runner, against the
transform as sealed. **All 49 cases were kept as written; none was corrected and none dropped.**

| Transform | Cases | Disposition |
|---|---|---|
| `CT_EXEC_EMIT_V0` | 15: `emit_string`, `emit_integer`, `emit_boolean_true`, `emit_boolean_false`, `emit_null`, `emit_simple_object`, `emit_nested_object`, `emit_array_primitives`, `emit_array_objects`, `emit_empty_object`, `emit_empty_array`, `emit_mixed_array`, `emit_workflow_result`, `emit_large_array`, `emit_unicode_strings` | Kept |
| `CT_PURE_ASSEMBLE_RECORD_V0` | 2: `assemble_simple_record`, `assemble_nested_record` | Kept |
| `CT_PURE_EXTRACT_V0` | 3: `extract_top_level_field`, `extract_nested_field`, `extract_nested_numeric` | Kept |
| `CT_PURE_FILTER_RECORDS_V0` | 4: `filter_by_exact_value`, `filter_by_field_presence`, `filter_multi_criteria`, `filter_single_match` | Kept |
| `CT_PURE_GENERATE_ID_V0` | 4: `generate_id_string_data`, `generate_id_object_data`, `generate_id_numeric_data`, `generate_id_deterministic` | Kept |
| `CT_PURE_LOOKUP_V0` | 4: `lookup_string_value`, `lookup_numeric_value`, `lookup_object_value`, `lookup_array_value` | Kept |
| `CT_PURE_MAP_RESULT_TO_HTTP_V0` | 6: `success_with_data`, `failure_with_error`, `error_with_custom_mapping`, `success_empty_value`, `success_complex_nested`, `failure_validation_array` | Kept |
| `CT_PURE_PASSTHROUGH_V0` | 5: `passthrough_string`, `passthrough_number`, `passthrough_object`, `passthrough_array`, `passthrough_boolean` | Kept |
| `CT_PURE_VALIDATE_PARAMETER_RULES_V0` | 2: `all_rules_pass`, `rule_fails` (VIOLATION) | Kept |
| `CT_PURE_VALIDATE_RECORD_STRUCTURE_V0` | 2: `valid_record`, `invalid_record_missing_field` | Kept |
| `CT_PURE_VALIDATE_SET_MEMBERSHIP_V0` | 2: `value_in_set`, `value_not_in_set` (VIOLATION) | Kept |

**The passthrough transform was the one open question.** Its implementation returns the value bare,
and the read-only drift check that preceded the dossier called it directly, so it could not tell.
Through the runner, which wraps the output as the transform declares it, all five cases hold.

---

## What delivery confirmed

**The platform proves its own transforms, in every composition.**

```
[conformance] platform: 11 proven, 1 unproven, 0 refused, 0 carried from another surface (49 case(s))
```

Each of the reference, federated and multi-worker builds prints this line.

**Nothing any domain reports changed.** Every domain's counts are what they were, because each carried
transform is a platform transform and no domain supplies a transform in that namespace.

**The rules over vectors judge the platform's as they judge a domain's.** Stage 3 left this open,
because a domain build imports those invariants by kind and the platform's build asserts its own. Five
defects, each introduced into a platform vector, each stopped the platform's build on the rule that
names it:
- an output the transform does not declare;
- an assertion mode nothing declares;
- a recorded result for an atom;
- a case with no outcome;
- a field outside the schema.

**The vectors are in the snapshot.** The composition grew from 421 to 432 artifacts, by the eleven
vectors, and `si artifact list --kind TEST_DATA` lists them where it had answered NOT_FOUND.

```
compiler      3/3   vectors materialized; each platform-vector defect refused on its rule; carried recorded
runtime       9/9   supplied read from the attestation; a failed case for a carried transform refuses
assembler    32/32  every build's result carried and complete, carried list matches its attestation
regression    green but for admission_contract_fidelity (31, expected)
```

---

## What it took

**A defect in delivered work, found by building.** The compiler skipped vectors when writing a
build's canonical output. That had two effects on the delivered transform conformance work:
- the runner's refusal of "a vector no case was compiled from" could never fire in a real build;
- the constitution's claim that what a transform was proven to do can be inspected in the
  composition held only for the generated cases, not the vectors.

The skip was removed in this delivery.

**The carried record moved to the attestation.** The plan put it in a file of its own. The compiler
resolves every output path from the build declaration and fails hard on an undeclared one, so a new
file would have meant a new declaration in every build. The attestation is already declared, already
records what a build imported, and already feeds the identity.

**The platform compiles every build declaration its surface holds.** So a runner told only the build's
root found four and refused. `compile.sh` now names the one it built.

**The platform's build declarations are named across the workspace.** The move from V1 to V2 reached:
- the regression, the release gate, `domain_authoring.py`, the RUNBOOK, the node group's deployment
  runbooks, one design note, and the conformance workloads' README;
- in the repositories: the compiler's README, ARCHITECTURE and two scripts, and the federation test.

Records of past builds were left as written: the SOTU's entries, and the signed federated readback.

---

## What is deliberately left open

**`CT_PURE_COMPARE_EQUAL_V0` is unproven.** No inherited case tests it, and none was invented.

**ai_governance's inherited vectors** disagree with its current implementations: where the reference
implementation answered "no", the current one refuses. That is ai_governance's question, in its own
change.

**Three documents still name the V1 build declarations.**
- `pgc_install/README.md`: that repository is main-only, and changes at a release.
- `standards/profile_authoring/README.md`: frozen with draft-3.
- `software_governance/surface_map/governance_surface_map.yaml`: stale throughout, as the SOTU
  already records.
