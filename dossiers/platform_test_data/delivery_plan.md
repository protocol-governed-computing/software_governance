# Delivery plan — platform_test_data

Authorized by Gate 1, closed at P6 against composition `d3e4fbf45009…`. Everything below lands on
`dev/17` as one delivery, in dependency order. No transform, contract or workflow changes. Every domain
reports the same counts as today; the platform's result is new and names eleven transforms proven and
one unproven.

## What the survey for this plan found

**The platform's build declarations are named in 20 files outside the registry.** These include the
regression, `release.sh`, the RUNBOOK, `domain_authoring.py`, `test_federation.py`,
`test_governance_provenance.py`, `machine_key_mutation.py`, the node group's `NODE_CONFIG.md` and
`PLAN.md`, the compiler's and `pgc_install`'s READMEs, the surface map, and the profile-authoring
guide. A new version of each declaration means every one of those names moves. The move is mechanical,
but it reaches the node group's deployment runbook.

**A placement build writes to its own root.** The regression builds the federated and multi-worker
platforms into `software_governance/snapshot_fed` and `snapshot_mw` through `PGC_SNAPSHOT_ROOT`. The
runner today reads `<domain_root>/snapshot/compiled`, so it must be told the root the build wrote.

**The platform's transforms are declared under `capability_transforms/registry/capability_transforms/`**,
which the `REUSABLE_TRANSFORMS` layer discovers.

## 1. `software_governance` — the rules and the vectors

| Item | Content |
|---|---|
| `registry/conformance/constitutions/CONSTITUTION_TEST_DATA_V2.md` | §4: a transform's vectors run in its supplier's build; for the platform's own transforms that is each platform build, which never proves a domain's. §5: a domain's vectors come from its design; the platform's are authored under the dossier that gates them, as the rest of its surface is. §7 records what became of V1. Every rule id stands; `TD_RUN_EVERY_BUILD` and `TD_FAILURE_REFUSES` say "supplier's build" and "build". |
| `CONSTITUTION_TEST_DATA_V1.md` | Deleted (see decision 1). |
| `registry/structure/structures/STRUCTURE_BUILD_PLATFORM_{,FEDERATED_,MULTIWORKER_}CONFIG_V2.md` | Each is its V1 plus `TEST_DATA` among the discovered kinds and `output_configuration.conformance {subpath: compiled/transform_conformance}`. The description narrows "implementation-layer conformance is out of scope" to a domain's implementations. |
| The three V1 build declarations | Deleted (see decision 1). |
| `capability_transforms/registry/test_data/TEST_DATA_CT_*_V0.md` × 11 | The inherited cases restated in the Machine block. Each targets `capability_transforms::CT_…_V0`, is governed by V2, and has one case per inherited case. |
| `surface_map/governance_surface_map.yaml` | Names the V2s. |

## 2. `protocol_compiler` — build step and carried record

| Item | Content |
|---|---|
| `compile.sh` | Runs the compile without `exec`, then `protocol_runtime/run.sh conformance "$PGC_PLATFORM_ROOT" --snapshot-root "$PGC_SNAPSHOT_ROOT"`. `set -euo pipefail` stops a failed compile before conformance runs. |
| `compile_domain.sh` | Passes its snapshot root the same way, so both build steps share one form. |
| `stages/s7_materialize.py` | Writes the transforms the build carried in (the nodes `s1` marked imported) to `compiled/carried/carried.json`, sorted, in every build; the platform's record is empty. |
| Scripts naming V1 | `test_governance_provenance.py`, `machine_key_mutation.py`, README and ARCHITECTURE name V2. |
| Tests | The carried record is written for a domain and is empty for the platform. A platform vector built to trip each vector invariant refuses the platform build, which settles the open question from P3. |

## 3. `protocol_runtime` — the runner

| Item | Content |
|---|---|
| `runtime/conformance.py` | A build's own transforms are those it compiled and did not carry in, read from `carried.json`; carried transforms are the record's. A build is admitted only when no case failed. `run_domain` takes the compiled root. |
| `runtime/cli.py` | `conformance DOMAIN_ROOT [--snapshot-root PATH]`. |
| `testbed/pgc/test_federation.py` | Names the V2s. |
| Tests | Classification by record, not name, for a transform whose namespace is not the build's; a failed case for a carried transform refuses; the existing seven still pass. |

## 4. `snapshot_assembler` — evidence

| Item | Content |
|---|---|
| `scripts/testbed/test_transform_conformance_evidence.py` | Requires a platform result naming all twelve platform transforms, eleven proven, one unproven and none refused. Requires every domain's counts as before. Requires `carried/<domain>/carried.json` to be carried as a constituent. The assembler itself is unchanged. |

## 5. `transformation` — the design language

| Item | Content |
|---|---|
| `design/families.py`, `design/p7_design_intent/rules.py`, `scripts/testbed/vector_design_test.py` | Rendered vectors are governed by V2. Construction acceptance keeps reporting the fixtures' vectors as not yet delivered. |

## 6. `.github` — process

`regression.sh`, `release.sh`, `domain_authoring.py`, the RUNBOOK, `NODE_CONFIG.md`, `PLAN.md` and the
docs under `doc/` name the V2s. The RUNBOOK gains the platform's expected line:
`[conformance] platform: 11 proven, 1 unproven, 0 refused, 0 carried`, one per platform build. The
federated and multi-worker lines are the same.

## 7. Record

`delivery.md` holds the re-judgement table: every inherited case with its disposition (kept, corrected
or dropped) and the reason for each correction and drop. `closure.md` closes the dossier. Other
repositories' READMEs naming V1 are updated, including `conformance_workloads`, `pgc_install` and
`standards/profile_authoring`.

## 8. Acceptance

- `regression.sh --all` is green, except the expected `admission_contract_fidelity` red.
- Each of the three platform builds reports 11 proven, 1 unproven and 0 refused.
- Every domain's counts are unchanged.
- Construction reproduces 99/99 with zero field differences.
- A failed case for a carried transform refuses its build.
- A platform vector built to trip each vector invariant refuses the platform build.
- Nothing outside the registry and the dossiers names a V1 build declaration or the V1 constitution.

## 9. Decisions needed before editing

1. **Delete the V1s rather than supersede them.** Recommended: delete, following the precedent of
   `CONSTITUTION_EXECUTION_PLACEMENT_V1` §8 and of V0 of the constitution governing vectors.
   - A superseded V1 build declaration stays compilable, which leaves a way to build the platform
     unproven.
   - A superseded V1 constitution keeps "never in the platform's own build" in the surface, beside a
     V2 that says the opposite.
   - Nothing compiled names any of them. `pgc_release` keeps its sealed copies as evidence.
2. **Where the carried record lives.** Recommended: `compiled/carried/carried.json` in every build.
   The assembler carries it as it carries every projection, so the snapshot states what each domain
   carried, and it becomes part of the identity.
   - The alternative is a field on each carried canonical artifact. That would widen the divergence
     the advisory `republished_copies_agree` check already reports.
3. **Where the platform's vectors live.** Recommended: `capability_transforms/registry/test_data/`,
   beside the transforms they test, in the layer that already discovers those transforms.
4. **The node group.** `NODE_CONFIG.md` and `PLAN.md` change as documents only. The nodes are configured
   by hand and pick up the V2 names when they are next rebuilt; nothing is
   pushed to them by this delivery.
