# STRUCTURE_EXECUTION_PLACEMENT_FEDERATED_NODE_V1

## Machine

```yaml
fqdn: execution_placement::STRUCTURE_EXECUTION_PLACEMENT_FEDERATED_NODE_V1
artifact_code: STRUCTURE_EXECUTION_PLACEMENT_FEDERATED_NODE_V1
artifact_kind: STRUCTURE
version: V1
governed_by: execution_placement::CONSTITUTION_EXECUTION_PLACEMENT_V1
authority: pgc.platform
concern: execution_placement
placement_mode: FEDERATED_NODE
remote_execution_allowed: true
cross_node_dispatch_allowed: true
placement_target: node_group
```

---

## Purpose

Declares that several separately addressable nodes under one governance authority is an available
placement arrangement.

Work reaches a node from a coordinating party across a network, and a node executes a governed
topology it did not receive from a caller. Every node executes against the same sealed snapshot,
under the same closure, and reaches the determination it would have reached anywhere.

## One authority, many nodes

Federation here is placement and distribution. A node is where execution happens; it is not a party
that determines anything, and its refusal is the one authority refusing, reached on that node.

Nothing in this structure constitutes an authority, and nothing may be read as constituting one. A
realization in which a node determined under a closure of its own would have left what this
authorizes — not exceeded it, left it: that is a different arrangement requiring a different
declaration, and this one would no longer describe the system.

## What distinguishes this from `LOCAL_MULTI_WORKER`

Reachability, not count. Several workers in processes on one host are not addressable and cannot be
reached from outside the host. Several nodes are addressable, and that is the whole difference — it
is why an environment profile requiring separately addressable nodes can be met under this mode and
cannot be met under the other, at any host count.

## Availability is not activity

This structure carries no `status`. It states that the mode is **available** to a build, never that
it is **active** in one — activity is named by a build configuration and recorded in the snapshot
that results (`CONSTITUTION_EXECUTION_PLACEMENT_V1` §2).
