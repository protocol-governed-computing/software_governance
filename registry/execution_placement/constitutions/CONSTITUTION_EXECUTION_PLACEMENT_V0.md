# CONSTITUTION_EXECUTION_PLACEMENT_V0

## Machine

```yaml
fqdn: execution_placement::CONSTITUTION_EXECUTION_PLACEMENT_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: execution_placement
core:
  enforcement_model: process_and_compiler_enforced
rules:
- applies_to: compiled_snapshot
  enforced_by: execution_placement::INVARIANT_EXECUTION_PLACEMENT_DECLARED_V0
- applies_to: build_configuration
  enforced_by: execution_placement::INVARIANT_EXECUTION_PLACEMENT_DECLARED_V0
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
| `FEDERATED_NODE` | several separately addressable nodes, one authority | yes | yes |

A mode not in this table is unauthorized. Authorizing one is an amendment to this constitution, not
a configuration.

## §2. Placement belongs to a composition, not to a surface

A surface cannot hold the active placement. Marking one declaration `status: active` works while a
surface serves one composition. It is incoherent once a surface serves more than one: an inventory cannot hold two
answers to where execution runs, and two compositions built from one surface may legitimately differ
in placement without either being wrong.

The boundary in which the compiler discovers the active placement is a build, not a repository. For
one composition the two cannot be told apart. So:

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

## §5a. What `FEDERATED_NODE` permits, and what it does not

**Permits.** Several separately addressable nodes under one governance authority, work reaching a
node from a coordinating party across a network, and a node executing a governed topology it did not
itself receive from a caller.

**Does not permit** — and this is the line the mode exists to hold — **more than one authority.**
Federation here is placement and distribution. Nodes are where execution happens; they are not
parties that determine anything. A node's refusal is the one authority refusing, reached on that
node. Nothing about this mode constitutes an authority, and a realization that let a node determine
under its own closure would have left what this authorizes.

**Does not decide** how nodes are realized, how many machines carry them, how they are addressed, or
what happens when one is unreachable. A deployment placing every node on one host and one spanning
several both satisfy it. Unreachability already has a determination and it is to refuse.

**Changes nothing about determination.** A determination reached on one node is reached under the
same closure, against the same sealed snapshot, and yields the result it would have reached
anywhere. What crosses between nodes is work and evidence, never authority.

**The distinction from `LOCAL_MULTI_WORKER` is reachability, not count.** Several workers on one host
are not addressable and cannot be reached from outside; several nodes are, which is why this mode
and not that one is what an environment profile requiring addressable nodes can be met under.

## §6. Expansion path

```
LOCAL_SINGLE_NODE
  → LOCAL_MULTI_WORKER          ← authorized here
  → REMOTE_WORKER_POOL          ← not authorized; a pool is not a node group
  → FEDERATED_NODE              ← authorized here
  → SILICON_HOSTED
```

The axis extends additively. Each mode is authorized by amendment, and an unauthorized mode is
unreachable rather than merely undocumented.

`REMOTE_WORKER_POOL` is deliberately skipped rather than reached. A pool is a set of interchangeable
executors reached through one address; a node group is a set of addressable participants with
declared roles. The profile requiring this axis names roles — a boundary, a coordinator, workers —
so the pool is not on the path to it. Skipping a step leaves that step unexercised, which is a cost
worth stating: nothing here has been demonstrated against an arrangement where executors are
anonymous.

## §7. Versioning

Changes to placement semantics require a new constitution version and migration rationale.

## §8. What placement holds

Placement is a property of the composition being built, not of a surface's
inventory. `LOCAL_MULTI_WORKER` is authorized
alongside it. The build configuration selects the mode, and no structure marks itself selected.

**Rationale.** Two profiles came into force over one governance surface — one requiring no
particular arrangement, one requiring several workers. Under V0 the second could not be built
without changing what the first was permitted, because the permission lived in the surface they
shared. Placement was widened for one composition or withheld from the other, and neither is a
governed outcome.

The alternative considered and rejected was authorizing the broader mode surface-wide and relying on
compositions not to use it. That grants every composition a permission one of them needs, which is
the widening this family forbids a profile from doing to its base, done one layer beneath where the
prohibition is written.
