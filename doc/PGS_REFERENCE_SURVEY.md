# `pgs_*` references in the governance surface — a read-only survey

Every `pgs_*` reference in `software_governance/registry/`, classified from evidence. The survey was
read-only; the remediation it drove is recorded per class below, and one of its own classifications
was wrong and is corrected in place.

**58 references across 28 files** — 36 in machine fields, 22 in prose. The split matters because the
two fail differently: a machine field either resolves or does not, and that is checkable; a prose
reference is a claim a reader believes, and only a person can judge it.

## The headline: most of them are not broken

The largest class is **live lookup keys that carry a dead package name**. The compiler's assertion
registry is keyed by RI-0 module strings and implemented entirely in PGC code:

```
compiler/stages/s4_govern.py:100     _HANDLER_MODULE_PREFIX = "pgs_governance.registry.handlers"
compiler/governance_engine/assertions/handlers   HANDLER_REGISTRY — 85 handlers, all keyed pgs_*
```

Every derived ASSERT binds its handler by that prefix, looks it up in `HANDLER_REGISTRY`, and a miss
is a hard `E702_UNKNOWN_ASSERT`. Six sampled handlers all resolve. **These invariants fire.** The
name is legacy; the mechanism is current and PGC-owned.

This corrects an earlier claim in this workspace that an invariant naming a `pgs_*` handler "cannot
fire". It fires. The defect is nominal, not functional — which changes what the fix is worth.

## Classification

| Class | What it is | Count | Live? |
|---|---|---|---|
| **A — legacy name, live key** | Resolves through `HANDLER_REGISTRY` or a schema `$id` | 27 | yes |
| **B — contradictory** | Declares a layer root that contradicts the live one | 9 | mixed |
| **C — enumerated surface, unverifiable** | Names implementation files that no longer exist | 6 | untestable |
| **D — historical citation** | Correctly names RI-0 as history | 5 | n/a |
| **E — ungrounded prose claim** | States a path or tool as current when it is not | 11 | no |

### A — legacy name, live key (27)

- **5 invariant `handler:` fields** — `INVARIANT_FQDN_NAMESPACE_AUTHORIZED_V0`,
  `INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0`, `INVARIANT_NO_SHORT_NAME_REFERENCE_V0`,
  `INVARIANT_CS_SURFACE_CLOSED_V1`, `INVARIANT_CT_SURFACE_CLOSED_V1`. All resolve.
- **11 JSON schema `$id` values** — `pgs_governance.schemas.SCHEMA_*_V0`. Identifiers, not import
  paths. Renaming one changes an identity and everything that cites it.
- **11 remaining handler/registry key mentions** in the same artifacts.

**Disposition:** a coordinated rename, or leave it. Both are defensible; neither is a cleanup. The
key string appears in the compiler, in `HANDLER_REGISTRY`, and in the artifacts, and all three must
move together or assertions stop resolving. It changes artifact content, so it changes hashes and
the snapshot. **Renaming buys accuracy of naming and nothing else** — nothing is currently broken.

### B — contradictory, and **not** inert (9) — *acted on; the survey's first reading was wrong*

`STRUCTURE_REGISTRY_LOCATION_GOVERNANCE_V0`, `…_REUSABLE_TRANSFORMS_V0`, `…_REUSABLE_SIDE_EFFECTS_V0`
each declared:

```yaml
core:
  layer_code: GOVERNANCE                       # and REUSABLE_TRANSFORMS / REUSABLE_SIDE_EFFECTS
  registry_module: pgs_governance.registry     # and pgs_transforms / pgs_side_effects
  module_path_pattern: '{registry_module}'
```

`STRUCTURE_DISCOVERY_V0` declares the same three layers as `software_governance.registry`,
`capability_transforms.registry` and `capability_side_effects.registry`, and says of itself that it
is the *"single source of truth for artifact discovery, replacing fragmented registry location and
layer authority discovery definitions"*. The supersession was declared; the superseded artifacts were
left in place, still reading as authority.

**They were not inert, and this survey said they were.** Deleting all three built cleanly and then
turned three P3 cases red: `REUSE_CANDIDATE_NOT_ELIGIBLE` fired twelve times, because
`…_REUSABLE_TRANSFORMS_V0` and `…_REUSABLE_SIDE_EFFECTS_V0` carry `reuse_visibility: substrate` — a
live declaration `STRUCTURE_DISCOVERY_V0` does not carry and a P3 rule reads. The artifacts held one
superseded fact and one live one, and the survey saw only the first.

**Disposition, applied:** the superseded fields alone were removed — `registry_module` and
`module_path_pattern` — leaving `layer_code`, `reuse_visibility`, `structure_scope` and
`output_configuration` untouched. The contradiction is gone and nothing live was lost. Build green at
399 artifacts, the same count as before.

**What this cost, stated so the next survey is read differently.** "Consulted by nothing" was
inferred from one field resolving to nothing, and generalised to the whole artifact. An artifact is
not a unit of liveness; a field is.

### C — declared and read by nothing (6) — *answered, and removed*

`INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0` declared `extensions.enforcement_locations`: six
`pgs_*` implementation files with `::function()` suffixes, inside the machine block.

**Nothing reads it.** No code in any repo references `enforcement_locations`; the `extensions:` block
is read in exactly one handler (`assert_ev_append_only_v0`, and only to scan key *names* on EV
artifacts), and exactly one artifact in the registry carries an `extensions:` block — this one.

**Disposition, applied: removed.** Building machinery to validate a field with no consumer would be
the more expensive error. It is the second declared-but-unread field found in two sessions — the
first, `"priors": True` in the differential harness, was deleted for the same reason — and the worse
of the two, because it sat in a machine block naming six files that do not exist, and so read as
binding while enforcing nothing.

### D — historical citation (5)

`CONSTITUTION_CHANGE_MGMT_V0` and `CONSTITUTION_CONSTRUCTION_V0` name `pgs_compiler` and
`pgs_change_mgmt` when describing where a lifecycle stage was realized.

**Disposition:** keep the citation, mark it as history. A constitution explaining *why* a rule exists
by naming the code that motivated it is doing its job — `transformation/CLAUDE.md` cites
`pgs_change_mgmt/engine/compilation_unit.py:382-383` deliberately for exactly this reason. **A sweep
that rewrites these destroys the reasoning.** What needs fixing is only the tense: where a table row
reads `| Compiler | … | pgs_compiler |` as a statement about the current toolchain, it is now false.

### E — ungrounded prose claim (11)

- `CONSTITUTION_VOCABULARY_V0` — `pgs_governance/governance/vocabulary/reserved/` and
  `…/vocabulary_semantic_index.json`, paths that do not exist.
- `CONSTITUTION_FEDERATION_BOUNDARY_V0` — seven mentions of `pgs_governance` as the federation root.
- `STRUCTURE_ARTIFACT_IDENTITY_V0`, `INVARIANT_ATOM_OUTPUT_PURITY_V0`,
  `INVARIANT_NO_SMART_EXECUTION_V0` — one each.

**Disposition:** correct in place. These are the cheapest and least risky: prose stating a current
path that is wrong. No identity moves, no hash changes beyond the artifact's own.

## What was done, and what was deliberately left

| Class | Count | Action |
|---|---|---|
| A — legacy name, live key | 27 | **Left alone**, deliberately. Nothing is broken; a rename would be an identity- and hash-changing migration across compiler, registry and artifacts, and it deserves its own reason |
| B — contradictory | 9 | **Ruled and applied** — superseded root fields removed, live fields kept |
| C — declared and unread | 6 | **Removed** |
| D — historical citation | 5 | **Keep the citation, fix the tense.** Not yet done; independent |
| E — ungrounded prose | 11 | **Correct in place.** Not yet done; independent |

`.github/process/governance_closure.py` was written **before** B was remediated, and reported the
three conflicts on its first run. That ordering is the only reason the check is known to detect the
defect rather than merely to agree with an already-clean tree. It proves two relations and claims no
more: every compiler handler is named by an invariant, and no layer is declared two ways.

## What this survey says about the folder proposal

The proposed `machine_governance/` and `software_process_governance/` split would have had to amend
the class B artifacts, because they are what declares where the registry lives. Those are precisely
the references that are already superseded and inert. **A directory move would have re-blessed a
stale declaration as current** — the move would have "worked", and the wrong artifact would have
acquired fresh authority by being edited.
