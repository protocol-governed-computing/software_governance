# STRUCTURE_EXECUTION_PLACEMENT_LOCAL_SINGLE_NODE_V1

## Machine

```yaml
fqdn: execution_placement::STRUCTURE_EXECUTION_PLACEMENT_LOCAL_SINGLE_NODE_V1
artifact_code: STRUCTURE_EXECUTION_PLACEMENT_LOCAL_SINGLE_NODE_V1
artifact_kind: STRUCTURE
version: V1
governed_by: execution_placement::CONSTITUTION_EXECUTION_PLACEMENT_V1
authority: pgc.platform
concern: execution_placement
placement_mode: LOCAL_SINGLE_NODE
remote_execution_allowed: false
cross_node_dispatch_allowed: false
placement_target: local_process
```

---

## Purpose

Declares that one process on one host is an available placement arrangement.

Execution runs in a single process on the local host. No worker pool is consulted and no
dispatch occurs, because there is nothing to dispatch to.

This is the same mode V0 declared and it means the same thing. What changed is how a build reaches
it: the structure no longer marks itself active, and a build configuration names it.

## Availability is not activity

This structure carries no `status`. It states that the mode is **available** to a build, never that
it is **active** in one — activity is named by a build configuration and recorded in the snapshot
that results (`CONSTITUTION_EXECUTION_PLACEMENT_V1` §2).

The same artifact is available to a build that selects it and to a build that does not. An artifact
asserting its own activity could not be both, which is why V0's `status: active` could not survive
a surface serving more than one composition.
