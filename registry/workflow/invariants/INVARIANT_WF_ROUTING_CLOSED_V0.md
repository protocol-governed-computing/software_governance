# INVARIANT_WF_ROUTING_CLOSED_V0

## Machine

```yaml
fqdn: workflow::INVARIANT_WF_ROUTING_CLOSED_V0
artifact_kind: INVARIANT
version: V0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: workflow
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - WF
```

## Summary

A workflow node that execution can reach answers every outcome the thing it runs can end with. An
outcome with neither a route nor an ending is a place where execution refuses. Construction refuses
it first, so a sealed workflow cannot present itself as complete while it carries the gap.

## What this realizes

For every `WF` artifact in force, for every node reachable from `start_node` over `next`:

1. A node of type `CC` MUST declare in `next` every code in its contract's
   `result_status_contract.allowed`.
2. A node of type `IN` MUST declare in `next` every outcome its intent declares.
3. A code in `next` is answered whether it names a node or an ending. Both are routes the
   declarations give, and the build derives routing and termination from the same map.

## Where it applies

- **Artifact Types**: WF
- **Validation Phase**: compile_time
- **Enforced By**: ASSERT_WF_ROUTING_CLOSED_V0
- **Realizes**: `4a` GC-15

## Why reach, and why a superseded workflow is not checked

The obligation binds what execution can reach. A node no path from `start_node` arrives at runs on no
request. A superseded workflow is not in force and has no dispatch entry
(`artifact::INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0`), so execution cannot reach any of its nodes. It
stays in the canonical record as evidence, and the record does not run.

## Relationship to the step-level invariants

`execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0` closes a contract's steps against the
capabilities they dispatch. `execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0` closes what a
contract can end with against what it declares. This closes the workflow against both. Closing an
outcome at the step adds it to what the contract can end with, which opens a gap here unless the
workflow answers it too, so the three are realized together.

---

## What this realizes
```yaml
core:
  rule: Every node a workflow can reach MUST declare in next every outcome the contract or intent it runs
    declares; an outcome with neither a route nor an ending is a compile-time violation
  summary: a reachable workflow node answers every outcome of what it runs; construction refuses an
    unanswered one rather than leaving execution to refuse it
```
