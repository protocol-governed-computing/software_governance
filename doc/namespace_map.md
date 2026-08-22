# Namespace Rename — Frozen Map

**FROZEN.** Supersedes the annotated draft `name_space_rename.txt` and incorporates expert review.
Supporting evidence is in `name_space_rename_review.md`.

Generated from the authored `fqdn:` keys, so the left column is complete by construction:
**157 artifacts, 15 namespaces → 28 namespaces.** 100 artifacts change namespace, 57 do not.

Rows marked **CORRECTED**, **ADDED** or **RENAMED** differ from the draft. Everything unmarked is
either concurrence with the draft or an artifact the draft left in place deliberately.

---

## The governing principle

> Namespaces partition the governance architecture. Artifact kinds partition the artifact taxonomy.
> The two axes are orthogonal.

A namespace is an **architectural ownership boundary** (a Federation Boundary) — a coherent concern
whose semantics, governance and evolution are independent of every other concern. An artifact kind
(`CONSTITUTION`, `INVARIANT`, `WF`, `AC`, `EV`, …) is the **governance role** an artifact plays
inside that boundary. Every artifact is classified independently along both axes; folders,
registries, compiler dispatch and profiles are all derivable from the pair.

The namespace answers *who owns this rule?* — never *which artifact kinds does this rule reference?*

### Test before creating a namespace

1. **Is it a first-class architectural concept?** (`authority` ✓, `transport` ✓, `execution` ✓,
   `workflow` ✓, `event` ✓, `vocabulary` ✓)
2. **Can it evolve independently?** Could its constitutions, invariants and structures change
   without forcing unrelated namespaces to change?
3. **Does it own a coherent set of rules** — a distinct semantic contract, not merely a collection
   of artifacts that resemble each other?

Never create a namespace because several artifacts reference the same artifact kind.
`applies_to_kinds` is orthogonal to namespace ownership.

### Applied to the one open call, now closed

`INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0` is placed in **`execution`**, and no `fb.capability`
namespace is created. The invariant does not govern capability *definitions*; it governs which
implementations are **admissible for execution**. Its `applies_to_kinds: [CT, CS]` is scope of
application, not ownership. Admissibility is an execution-semantics constraint enforced before
runtime, so `execution` owns it. A `fb.capability` namespace would fail test 3 — it would collect
artifacts that mention CT/CS rather than own a distinct contract.

### Re-validation of the map under this principle

The audit that produced this map leaned on `applies_to_kinds` as its discriminator. That is
*evidence* of ownership, not ownership itself, so every corrected row was re-checked against the
ownership test. None moved: surface-closure rules are owned by `surface_contract`, executor and
wiring rules by `execution`, identity and schema-integrity rules by `artifact`, and the
`[COMPILER]`-kind rules by `compiler`. The two tests agree throughout, which is the substantive
basis for freezing.

Going forward, classify new artifacts into existing namespaces unless they introduce an entirely new
architectural concern.

---

## Summary of changes to the draft

| # | Change | Why |
|---|---|---|
| 1 | `execution_topology` → `execution_topology` | Typo. Would have orphaned `CONSTITUTION_EXECUTION_TOPOLOGY_V0` into a namespace of one, apart from the ten invariants it governs. |
| 2 | 6 artifacts moved out of `compiler` | The draft keyed on `enforcement_stage: compiler_validation`, which nearly every invariant carries — it says *when* a rule is checked, not what it governs. `applies_to_kinds` is the subject discriminator. |
| 3 | 2 artifacts moved *into* `compiler` | `INVARIANT_HANDLER_REGISTRY_CLOSED_V0` and `INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0` both declare `governed_by: CONSTITUTION_COMPILER_V0` and `applies_to_kinds: [COMPILER]`. |
| 4 | `INVARIANT_ASSERT_NOT_RUNTIME_REFERENCED_V0` → `conformance` | Unannotated in the draft. It governs ASSERT artifacts, and the draft already moves `CONSTITUTION_ASSERT_V0` to `conformance`. |
| 5 | `fb.identity` → `actor` | Its three members are all actor artifacts. Leaving it named `identity` alongside the new `artifact` gives two namespaces both meaning "identity", separated only by an implied noun. |
| 6 | `fb.change_mgmt` → `lifecycle` | Both members are `enforcement_model: process_enforced` with rules scoped to *stages* — `all_construction_stages`, `stage_8`, `stages_1_through_4`, `stages_8_and_9`, `all_stages`. That is a staged lifecycle covering construction *and* change governance. The draft's `fb.transformation` also collides with `capability_transforms` and the planned `transformation`. |

Consequence of items 3 and 4: **`fb.constitution` and `fb.topology` both reach zero and retire.**
The draft would have left them holding two and zero artifacts respectively — `fb.constitution`
surviving only as a vestige of two unannotated rows.

## Settled on review

- **`surface_contract` stays singular.** A namespace names the domain, not a collection, and the
  surrounding namespaces are all singular: `workflow`, `runtime_binding`, `transport`,
  `authority`, `compiler`. An earlier draft of this proposal pluralized it; that is withdrawn.
  The three `fb.capability_*` plurals are the deliberate exception — they mirror the bare
  `capability_transforms` / `capability_side_effects` namespaces that hold the instances, and
  singularizing them would break that pairing.
- **`runtime_binding` stays exactly as-is** — not folded into the `execution*` family. The
  separation between execution semantics (`execution`, `execution_topology`,
  `execution_placement`, `execution_scheduling`) and runtime realization
  (`runtime_binding`) is architecturally load-bearing and worth the asymmetry.

## A distinction worth stating explicitly

`capability_transforms` (6 governance artifacts) and `capability_transforms` (12 CT declarations)
both survive, as do `capability_side_effects` and `capability_side_effects`. This is coherent —
`fb.*` is the federation boundary that *governs* a kind, the bare namespace holds *instances* of it —
but it is only coherent if stated. Recommend recording it in `CONSTITUTION_FEDERATION_BOUNDARY_V0`
so the pairing reads as intent rather than accident.

---

## Final map

### `capability_side_effects`  (3)

| Artifact | From | |
|---|---|---|
| `CS_APPENDONLY_JSONL_V0` | `capability_side_effects` |  |
| `CS_MUTABLE_JSON_V0` | `capability_side_effects` |  |
| `CS_REGISTRY_V0` | `capability_side_effects` |  |

### `capability_transforms`  (12)

| Artifact | From | |
|---|---|---|
| `CT_EXEC_EMIT_V0` | `capability_transforms` |  |
| `CT_PURE_ASSEMBLE_RECORD_V0` | `capability_transforms` |  |
| `CT_PURE_COMPARE_EQUAL_V0` | `capability_transforms` |  |
| `CT_PURE_EXTRACT_V0` | `capability_transforms` |  |
| `CT_PURE_FILTER_RECORDS_V0` | `capability_transforms` |  |
| `CT_PURE_GENERATE_ID_V0` | `capability_transforms` |  |
| `CT_PURE_LOOKUP_V0` | `capability_transforms` |  |
| `CT_PURE_MAP_RESULT_TO_HTTP_V0` | `capability_transforms` |  |
| `CT_PURE_PASSTHROUGH_V0` | `capability_transforms` |  |
| `CT_PURE_VALIDATE_PARAMETER_RULES_V0` | `capability_transforms` |  |
| `CT_PURE_VALIDATE_RECORD_STRUCTURE_V0` | `capability_transforms` |  |
| `CT_PURE_VALIDATE_SET_MEMBERSHIP_V0` | `capability_transforms` |  |

### `actor`  (3)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_ACTOR_IDENTITY_V0` | `fb.identity` | **RENAMED from fb.identity** |
| `INVARIANT_AC_DECLARATION_WELL_FORMED_V0` | `fb.identity` | **RENAMED from fb.identity** |
| `INVARIANT_IDENTITY_AUTHORITY_SEPARATION_V0` | `fb.identity` | **RENAMED from fb.identity** |

### `artifact`  (6)

| Artifact | From | |
|---|---|---|
| `INVARIANT_FQDN_NAMESPACE_AUTHORIZED_V0` | `fb.constitution` |  |
| `INVARIANT_FQDN_ONLY_REFERENCES_V0` | `fb.constitution` |  |
| `INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0` | `fb.constitution` |  |
| `INVARIANT_NO_SHORT_NAME_REFERENCE_V0` | `fb.constitution` |  |
| `INVARIANT_SCHEMA_CONFORMANCE_V0` | `fb.topology` | **CORRECTED from compiler** |
| `INVARIANT_UNIQUE_ARTIFACT_ID_V0` | `fb.constitution` |  |

### `authority`  (8)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_AUTHORITY_GOVERNANCE_V0` | `authority` |  |
| `INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0` | `authority` |  |
| `INVARIANT_AUTHORITY_REQUIRED_FOR_EXECUTION_V0` | `authority` |  |
| `INVARIANT_AUTHORITY_STATE_WELL_FORMED_V0` | `authority` |  |
| `INVARIANT_NO_AMBIENT_AUTHORITY_V0` | `authority` |  |
| `INVARIANT_NO_RUNTIME_AUTHORIZATION_V0` | `authority` |  |
| `INVARIANT_NO_WORKFLOW_AUTHORIZATION_LOGIC_V0` | `authority` |  |
| `INVARIANT_TRACE_AUTHORITY_BINDING_REQUIRED_V0` | `authority` |  |

### `capability_contracts`  (9)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_CAPABILITY_CONTRACT_V0` | `fb.topology` |  |
| `INVARIANT_CC_CAPABILITY_BINDING_VALID_V0` | `fb.topology` |  |
| `INVARIANT_CC_INPUTS_SATISFIED_V0` | `fb.topology` |  |
| `INVARIANT_CC_NO_IMPLICIT_CHAINING_V0` | `fb.topology` |  |
| `INVARIANT_CC_NO_MISSING_DEPENDENCIES_V0` | `fb.topology` |  |
| `INVARIANT_CC_NO_UNUSED_OUTPUTS_V0` | `fb.topology` |  |
| `INVARIANT_CC_STORAGE_OP_CONFORMANCE_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_CAPABILITY_REFERENCE_UNIQUE_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_INPUT_REFERENCE_DECLARED_V0` | `fb.topology` |  |

### `capability_side_effects`  (4)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0` | `fb.topology` |  |
| `INVARIANT_CS_ISOLATED_EXECUTION_V0` | `fb.topology` |  |
| `INVARIANT_CS_SURFACE_CLOSED_V1` | `fb.topology` |  |
| `INVARIANT_CS_TRACEABLE_V0` | `fb.topology` |  |

### `capability_transforms`  (6)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_CAPABILITY_TRANSFORMS_V0` | `fb.topology` |  |
| `INVARIANT_ATOM_OUTPUT_PURITY_V0` | `fb.topology` |  |
| `INVARIANT_CT_OUTPUT_CONTRACT_MATCH_V0` | `fb.topology` |  |
| `INVARIANT_CT_SURFACE_CLOSED_V1` | `fb.topology` |  |
| `INVARIANT_CT_TEST_DATA_OUTCOME_DECLARED_V0` | `fb.topology` |  |
| `STRUCTURE_CT_IR_CONTRACT_V0` | `fb.topology` |  |

### `compiler`  (5)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_COMPILER_V0` | `fb.constitution` |  |
| `INVARIANT_ARTIFACT_CONTENT_HASH_DECLARED_V0` | `fb.constitution` | **ADDED (unannotated in proposal)** |
| `INVARIANT_COMPILER_GOVERNANCE_DECLARED_V0` | `fb.constitution` |  |
| `INVARIANT_COMPILER_NO_EXECUTION_V0` | `fb.constitution` |  |
| `INVARIANT_HANDLER_REGISTRY_CLOSED_V0` | `fb.constitution` | **CORRECTED from governance** |

### `conformance`  (7)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_ASSERT_V0` | `fb.constitution` |  |
| `CONSTITUTION_TEST_DATA_V0` | `conformance` |  |
| `INVARIANT_ASSERT_NOT_RUNTIME_REFERENCED_V0` | `fb.constitution` | **ADDED (unannotated in proposal)** |
| `INVARIANT_ASSERT_PARITY_V0` | `conformance` |  |
| `INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0` | `conformance` |  |
| `INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0` | `conformance` |  |
| `STRUCTURE_CONFORMANCE_POLICY_V0` | `conformance` |  |

### `cryptographic_trust`  (3)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0` | `cryptographic_trust` |  |
| `INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0` | `cryptographic_trust` |  |
| `STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0` | `cryptographic_trust` |  |

### `event`  (3)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_EVENT_V0` | `fb.constitution` |  |
| `INVARIANT_EV_APPEND_ONLY_V0` | `fb.constitution` |  |
| `INVARIANT_EV_SCHEMA_REQUIRED_V0` | `fb.constitution` |  |

### `execution`  (6)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_EXECUTION_POLICY_V0` | `fb.topology` |  |
| `CONSTITUTION_EXECUTION_V0` | `fb.topology` |  |
| `INVARIANT_IMPLEMENTATION_ADMISSIBLE_V0` | `fb.topology` | **CORRECTED from compiler** |
| `INVARIANT_NO_SMART_EXECUTION_V0` | `fb.topology` | **CORRECTED from compiler** |
| `INVARIANT_RUNTIME_INVARIANT_WIRED_V0` | `fb.topology` | **CORRECTED from compiler** |
| `STRUCTURE_RUNTIME_EXECUTION_V0` | `fb.topology` |  |

### `execution_placement`  (3)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_EXECUTION_PLACEMENT_V0` | `execution_placement` |  |
| `INVARIANT_EXECUTION_PLACEMENT_DECLARED_V0` | `execution_placement` |  |
| `STRUCTURE_EXECUTION_PLACEMENT_LOCAL_SINGLE_NODE_V0` | `execution_placement` |  |

### `execution_scheduling`  (3)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_EXECUTION_SCHEDULING_V0` | `execution_scheduling` |  |
| `INVARIANT_EXECUTION_SCHEDULING_DECLARED_V0` | `execution_scheduling` |  |
| `STRUCTURE_EXECUTION_SCHEDULING_SERIAL_SINGLE_WORKER_V0` | `execution_scheduling` |  |

### `execution_topology`  (11)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_EXECUTION_TOPOLOGY_V0` | `fb.topology` | **CORRECTED from execution_topology** |
| `INVARIANT_NO_RUNTIME_TOPOLOGY_SYNTHESIS_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_ACYCLIC_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_AUTHORITY_ORTHOGONAL_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_IMMUTABLE_AFTER_COMPILATION_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_STEP_DECLARED_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_STEP_ID_UNIQUE_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_SURFACE_CANONICAL_V0` | `fb.topology` |  |
| `INVARIANT_TOPOLOGY_TRANSPORT_ORTHOGONAL_V0` | `fb.topology` |  |

### `federation`  (1)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_FEDERATION_BOUNDARY_V0` | `fb.constitution` |  |

### `governance`  (3)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_GOVERNANCE_V0` | `fb.constitution` |  |
| `CONSTITUTION_INVARIANTS_V0` | `fb.constitution` |  |
| `INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0` | `fb.constitution` |  |

### `intent`  (4)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_INTENT_V0` | `fb.topology` |  |
| `INVARIANT_IN_NO_EXECUTION_LOGIC_V0` | `fb.topology` |  |
| `INVARIANT_IN_SCHEMA_REQUIRED_V0` | `fb.topology` |  |
| `INVARIANT_IN_WORKFLOW_BINDING_V0` | `fb.topology` |  |

### `lifecycle`  (2)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_CHANGE_MGMT_V0` | `fb.change_mgmt` | **RENAMED from fb.transformation** |
| `CONSTITUTION_CONSTRUCTION_V0` | `fb.change_mgmt` | **RENAMED from fb.transformation** |

### `runtime_binding`  (6)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_RUNTIME_BINDING_V0` | `fb.topology` |  |
| `INVARIANT_BINDING_INTEGRITY_V0` | `fb.topology` |  |
| `INVARIANT_BINDING_SURFACE_CLOSED_V0` | `fb.topology` |  |
| `INVARIANT_RB_BINDING_POLICY_CONFORMANCE_V0` | `fb.topology` |  |
| `INVARIANT_RB_CS_ONLY_V0` | `fb.topology` |  |
| `INVARIANT_RB_NO_LOGIC_V0` | `fb.topology` |  |

### `security_domain`  (3)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_SECURITY_DOMAIN_V0` | `security_domain` |  |
| `INVARIANT_SECURITY_DOMAIN_DECLARED_V0` | `security_domain` |  |
| `STRUCTURE_SECURITY_DOMAIN_UNCLASSIFIED_LOCAL_V0` | `security_domain` |  |

### `structure`  (13)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_STRUCTURE_V0` | `fb.constitution` |  |
| `INVARIANT_STRUCTURE_PATHS_WELL_FORMED_V0` | `fb.topology` |  |
| `STRUCTURE_ARTIFACT_IDENTITY_V0` | `fb.constitution` |  |
| `STRUCTURE_BUILD_PLATFORM_CONFIG_V0` | `fb.constitution` |  |
| `STRUCTURE_BUILD_PLATFORM_CONFIG_V1` | `fb.constitution` |  |
| `STRUCTURE_DISCOVERY_V0` | `fb.constitution` |  |
| `STRUCTURE_FQDN_TREE_V0` | `fb.constitution` |  |
| `STRUCTURE_IDENTITY_V0` | `fb.constitution` |  |
| `STRUCTURE_MODULE_DATA_ROOTS_V0` | `fb.constitution` |  |
| `STRUCTURE_REGISTRY_LOCATION_GOVERNANCE_V0` | `fb.constitution` |  |
| `STRUCTURE_REGISTRY_LOCATION_REUSABLE_SIDE_EFFECTS_V0` | `fb.topology` |  |
| `STRUCTURE_REGISTRY_LOCATION_REUSABLE_TRANSFORMS_V0` | `fb.topology` |  |
| `STRUCTURE_SCHEMA_DISPATCH_V0` | `fb.constitution` |  |

### `surface_contract`  (10)

| Artifact | From | |
|---|---|---|
| `INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0` | `fb.topology` | **CORRECTED from compiler** |
| `INVARIANT_PROTOCOL_SURFACE_CLOSED_V0` | `fb.topology` | **CORRECTED from compiler** |
| `SURFACE_CONTRACT_CT_PURE_V0` | `fb.topology` |  |
| `SURFACE_CONTRACT_REGISTRY_COUNT_V0` | `fb.topology` |  |
| `SURFACE_CONTRACT_REGISTRY_DEREGISTER_V0` | `fb.topology` |  |
| `SURFACE_CONTRACT_REGISTRY_REGISTER_V0` | `fb.topology` |  |
| `SURFACE_CONTRACT_REGISTRY_RESOLVE_V0` | `fb.topology` |  |
| `SURFACE_CONTRACT_STORAGE_APPENDONLY_APPEND_V0` | `fb.topology` |  |
| `SURFACE_CONTRACT_STORAGE_READ_V0` | `fb.topology` |  |
| `SURFACE_CONTRACT_STORAGE_WRITE_V0` | `fb.topology` |  |

### `trace`  (1)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_TRACE_EXECUTION_V0` | `fb.topology` |  |

### `transport`  (11)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_ADMISSION_V0` | `transport` |  |
| `CONSTITUTION_TRANSPORT_EGRESS_V0` | `transport` |  |
| `CONSTITUTION_TRANSPORT_ENVELOPE_V0` | `transport` |  |
| `CONSTITUTION_TRANSPORT_INGRESS_V0` | `transport` |  |
| `INVARIANT_TRANSPORT_CANONICAL_NORMALIZATION_V0` | `transport` |  |
| `INVARIANT_TRANSPORT_NO_DYNAMIC_ROUTING_V0` | `transport` |  |
| `INVARIANT_TRANSPORT_NO_WORKFLOW_SEMANTICS_V0` | `transport` |  |
| `INVARIANT_TRANSPORT_OPERATION_IDENTITY_INDEPENDENCE_V0` | `transport` |  |
| `INVARIANT_TRANSPORT_RESPONSE_PROJECTION_EXTERNAL_V0` | `transport` |  |
| `INVARIANT_TRANSPORT_RESULT_CLASS_PROTOCOL_INDEPENDENCE_V0` | `transport` |  |
| `INVARIANT_TRANSPORT_TARGET_EXISTS_V0` | `transport` |  |

### `vocabulary`  (6)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_VOCABULARY_V0` | `vocabulary` |  |
| `INVARIANT_VOCABULARY_SYMBOLS_WELL_FORMED_V0` | `vocabulary` |  |
| `STRUCTURE_BUILD_VOCABULARY_AGGREGATE_V0` | `vocabulary` |  |
| `VOCAB_EXECUTION_STATES_V0` | `vocabulary` |  |
| `VOCAB_LANGUAGE_CONSTRAINTS_V0` | `vocabulary` |  |
| `VOCAB_PROTOCOL_KINDS_V0` | `vocabulary` |  |

### `workflow`  (5)

| Artifact | From | |
|---|---|---|
| `CONSTITUTION_WORKFLOW_V0` | `fb.topology` |  |
| `INVARIANT_WF_CC_ONLY_NODES_V0` | `fb.topology` |  |
| `INVARIANT_WF_ENTRY_INTENT_V0` | `fb.topology` |  |
| `INVARIANT_WF_EXECUTION_PATH_VALID_V0` | `fb.topology` |  |
| `INVARIANT_WF_NODE_KEY_BINDING_UNIQUE_V0` | `fb.topology` |  |

---

## What this map does not cover

Three things must change with the map but are not namespace assignments:

- **`STRUCTURE_IDENTITY_V0`** — its allow-list must be rewritten to exactly these 28 namespaces. It
  currently authorizes eight with zero artifacts (`fb.blockchain`, `fb.ai_governance`, `blockchain`,
  `ai_governance`, `structure`, `execution`, `compiler`, `ingress_gateway`). The bare `compiler`
  entry in particular reads as a collision with the new `compiler`.
- **`STRUCTURE_FQDN_TREE_V0`** — a live compiler input (`structure_loader.py:60`) whose machine
  block still describes RI-0: `./pgs_governance` physical roots, blockchain/ai_licensing domain
  packages, `namespace_mappings` pointing at the retired `registry/FB_*` layout, and
  `id: omnibachi-machine-v0`. Its `namespace_mappings` block is where a real path→namespace
  derivation belongs — which would also make `STRUCTURE_IDENTITY_V0`'s declared
  `derivation.method: module_path` true rather than inert.
- **The Python sweep.** 24 compiler files hardcode `fb.*::` FQDNs — the assertion handlers are keyed
  by invariant FQDN, plus `protocol_loader.py` and `scripts/bind_constitution_rules.py`. Also in
  scope: compiler lookup tables, the assertion registry, dispatch, the loader, tests, and
  `standards/snapshot_profiles/NORMATIVE_PLATFORM_PROFILE_BASELINE_V0.md` (35 pinned FQDNs,
  reissued as `_V1`). A sweep that applies the map to artifacts only will break the assert phase.
