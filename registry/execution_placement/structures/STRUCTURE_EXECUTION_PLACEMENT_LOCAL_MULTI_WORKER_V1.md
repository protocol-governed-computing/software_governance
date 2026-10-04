# STRUCTURE_EXECUTION_PLACEMENT_LOCAL_MULTI_WORKER_V1

## Machine

```yaml
fqdn: execution_placement::STRUCTURE_EXECUTION_PLACEMENT_LOCAL_MULTI_WORKER_V1
artifact_code: STRUCTURE_EXECUTION_PLACEMENT_LOCAL_MULTI_WORKER_V1
artifact_kind: STRUCTURE
version: V1
governed_by: execution_placement::CONSTITUTION_EXECUTION_PLACEMENT_V1
authority: pgc.platform
concern: execution_placement
placement_mode: LOCAL_MULTI_WORKER
remote_execution_allowed: false
cross_node_dispatch_allowed: false
placement_target: local_process
```

---

## Purpose

Declares that several worker processes on one host is an available placement arrangement.

Execution runs in more than one worker process on the local host, each drawing work from a
coordinating party and executing a governed topology in its own process.

Every worker executes against the same sealed snapshot, under the same closure, and reaches the
determination it would have reached alone. The arrangement changes where work runs and not what it
means — a worker that determined differently for being one of several would be an environment
supplying governed behavior.

What this structure does not say: how work is divided, which worker takes which unit, or what
follows when a worker is lost. Those belong to scheduling. This declares only that more than one
worker is a permitted arrangement.

## Availability is not activity

This structure carries no `status`. It states that the mode is **available** to a build, never that
it is **active** in one — activity is named by a build configuration and recorded in the snapshot
that results (`CONSTITUTION_EXECUTION_PLACEMENT_V1` §2).

The same artifact is available to a build that selects it and to a build that does not. An artifact
asserting its own activity could not be both, which is why V0's `status: active` could not survive
a surface serving more than one composition.
