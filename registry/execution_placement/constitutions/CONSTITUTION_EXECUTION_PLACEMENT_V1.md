# CONSTITUTION_EXECUTION_PLACEMENT_V1

## Machine

```yaml
fqdn: execution_placement::CONSTITUTION_EXECUTION_PLACEMENT_V1
artifact_kind: CONSTITUTION
version: V1
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: execution_placement
core:
  enforcement_model: process_and_compiler_enforced
rules:
- applies_to: compiled_snapshot
  enforced_by: execution_placement::INVARIANT_EXECUTION_PLACEMENT_DECLARED_V1
- applies_to: build_configuration
  enforced_by: execution_placement::INVARIANT_EXECUTION_PLACEMENT_DECLARED_V1
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: runtime
  enforced_by: PROCESS_ENFORCED
```

---

## Purpose

Placement governs *where a transition is authorized to run*. It does not schedule, route, or
distribute; it states which arrangements of execution a compiled snapshot is permitted to have, so
that an arrangement nobody declared cannot be reached by an arrangement nobody noticed.

## §1. Authorized placement modes

| Mode | Execution | Remote dispatch | Cross-node |
|---|---|---|---|
| `LOCAL_SINGLE_NODE` | one process, one host | no | no |
| `LOCAL_MULTI_WORKER` | several worker processes, one host | no | no |

A mode not in this table is unauthorized. Authorizing one is an amendment to this constitution, not
a configuration.

## §2. Placement belongs to a composition, not to a surface

**This is what V1 changes, and the reason it exists.**

V0 held that a governance surface carries exactly one placement declaration marked `status: active`,
and that the compiler finds it by that mark. That was adequate while a surface served one
composition. It is incoherent once a surface serves more than one: an inventory cannot hold two
answers to where execution runs, and two compositions built from one surface may legitimately differ
in placement without either being wrong.

V0 §2 already said the compiler discovers *"the active placement contract in this boundary."* A
boundary is a build. V0 read it as a repository, because for one composition the two could not be
told apart.

Under V1:

- **the surface declares what is available** — one structure per authorized mode, none of which
  claims to be active;
- **the build configuration declares what is active** — naming exactly one available mode;
- **the snapshot records what was active** — materialized into its federation profile, so what a
  composition was permitted is recoverable from the composition rather than from the repository that
  produced it.

A placement structure therefore carries no `status` field. Activity is not a property an artifact
can assert about itself, because the same artifact is available to a build that selects it and to a
build that does not.

## §3. Compiler behavior

The compiler MUST:

- read the placement mode named by the build configuration under construction;
- validate that exactly one is named, and that it resolves to a placement structure declared by
  this surface and authorized by §1;
- refuse where none is named, where more than one is, or where the named mode is not authorized —
  an absent placement is not a default, and defaulting one would let an arrangement be reached that
  no configuration declared;
- materialize **only the selected placement structure** into the composition, so that a snapshot
  carries the arrangement it was granted rather than every arrangement the surface declares;
- materialize the mode into the snapshot's federation profile:

```yaml
federation_profile:
  execution_placement: LOCAL_MULTI_WORKER
```

The compiler MUST NOT schedule, dispatch, or route execution. Placement states what is permitted;
what is done about it belongs to scheduling and to whatever performs the work.

## §4. Runtime behavior

Unchanged from V0, and unchanged deliberately. The runtime MUST:

- record `federation_profile.execution_placement` in trace metadata;
- execute the governed topology **without consulting placement mode for branching**.

A runtime that branched on placement would make one snapshot mean two things depending on where it
ran, which is the property placement exists to deny. It follows that multi-worker execution is not a
mode the runtime enters: a coordinating party runs several runtimes, and each runtime executes what
it was given exactly as it would alone.

## §5. What `LOCAL_MULTI_WORKER` permits, and what it does not

**Permits.** More than one worker process on one host, drawing work from a coordinating party, each
executing a governed topology in its own process.

**Does not permit.** Remote execution, cross-node dispatch, or a worker pool reached over a network.
Those are later modes and are not authorized by this constitution.

**Does not decide.** How work is divided, which worker receives which unit, in what order, or what
happens when a worker is lost. Those are scheduling questions and belong to the scheduling boundary.
Placement says only that more than one worker is a permitted arrangement.

**Changes nothing about determination.** A determination reached by one of several workers is
reached under the same closure, against the same sealed snapshot, and yields the same result it
would have reached alone. Placement that altered a determination would be an environment supplying
governed behavior, which no mode may do.

## §6. Expansion path

```
LOCAL_SINGLE_NODE
  → LOCAL_MULTI_WORKER          ← authorized here
  → REMOTE_WORKER_POOL
  → FEDERATED_NODE
  → SILICON_HOSTED
```

The axis extends additively. Each mode is authorized by amendment, and an unauthorized mode is
unreachable rather than merely undocumented.

## §7. Versioning

Changes to placement semantics require a new constitution version and migration rationale.

## §8. What became of V0

**V0 was deleted, not superseded.** `CONSTITUTION_EXECUTION_PLACEMENT_V0`, its invariant, and its
single-node structure are gone from this surface, and this constitution supersedes nothing.

That distinction is deliberate. Supersession deletes nothing: it declares a relation between two
identities, keeps the predecessor compiled so the relation is readable, and obliges nothing live to
reference the retired artifact. It is right where a claim discharged under the predecessor must
remain evaluable.

Here it was wrong in three ways at once. A superseded placement structure stays in the composition,
so a composition would carry two structures declaring one mode and the cardinality rule could not
distinguish them. A superseded invariant is still enforced, so V0's check would go on requiring a
`status: active` that V1 structures deliberately do not carry. And a successor naming a predecessor
that selection had excluded would leave a reference resolving to nothing.

Deletion has none of those consequences and loses nothing that matters: the V0 declarations are
carried by the deposited composition built under them and by this repository's history, which is
where a retired declaration's evidence belongs. A snapshot built under V0 is unaffected — it records
`LOCAL_SINGLE_NODE` in its federation profile, that remains true of it, and nothing here reaches
backwards to change what it claimed.

**What V1 changes.** Placement stops being a property of a surface's inventory and becomes a
property of the composition being built. The mode `LOCAL_SINGLE_NODE` means exactly what it meant
before; `LOCAL_MULTI_WORKER` is newly authorized; and the mark that used to select a mode no longer
exists, because selection moved to the build configuration.

**Rationale.** Two profiles came into force over one governance surface — one requiring no
particular arrangement, one requiring several workers. Under V0 the second could not be built
without changing what the first was permitted, because the permission lived in the surface they
shared. Placement was widened for one composition or withheld from the other, and neither is a
governed outcome.

The alternative considered and rejected was authorizing the broader mode surface-wide and relying on
compositions not to use it. That grants every composition a permission one of them needs, which is
the widening this family forbids a profile from doing to its base, done one layer beneath where the
prohibition is written.
