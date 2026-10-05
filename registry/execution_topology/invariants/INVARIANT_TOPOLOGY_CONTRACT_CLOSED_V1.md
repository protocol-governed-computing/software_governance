# INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1

## Machine

```yaml
fqdn: execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1
supersedes: execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0
artifact_kind: INVARIANT
version: V1
governed_by: execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1
authority: pgc.platform
concern: execution_topology
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - CC
  - CT
  - CS
```

---

## Summary

The CC-level result status contract is a promise to callers about what outcomes this CC can
produce. That promise is only valid if the execution topology can actually deliver every
declared outcome, and cannot deliver any undeclared one.

CONTRACT_CLOSED verifies that the topology fulfills the contract — not just that routing is
locally complete per step (ROUTING_COMPLETE), but that the full CC exit surface matches the
declared contract exactly. A contract's exits come from its steps, and a step's outcomes come from
the capability it runs: routing is a lookup with two answers, and a decision is a capability's.

## What this realizes
For every CC:

1. **No uncontracted exits**: every status code that can exit the CC topology (via `exit` or
   last-step `continue`) MUST appear in `result_status_contract.allowed`
2. **No unreachable contract codes**: every code in `result_status_contract.allowed` MUST
   be reachable as a CC exit — there MUST exist at least one execution path that exits
   with that code
3. The contract is closed when `reachable_exits == allowed` exactly
4. **Two routing answers**: every value in a step's `on_result` MUST be `continue` or `exit`.
   Anything else is a routing answer nothing performs, refused by contract, step and answer
5. **No conditions**: a CC MUST NOT declare an `evaluation` block. A decision a condition would
   state is made by a capability, which answers with an outcome the step routes on

A contract that is not in force (`INVARIANT_SUPERSEDED_NOT_IN_FORCE_V0`) is not checked: it runs
nowhere, and it stays in the record as it was sealed.

## Exit Reachability

A status code is reachable as a CC exit when ANY of the following hold:

- A step routes that code as `exit` in `on_result` (and the code is in the step's `result_surface`)
- The LAST step in the pipeline routes that code as `continue` (last-step `continue` exits the CC)

Codes routed as `continue` in non-last steps remain in-pipeline — they do not exit the CC.

## Where it applies
- **Artifact Types**: CC
- **Validation Phase**: compile_time
- **Enforced By**: ASSERT_TOPOLOGY_CONTRACT_CLOSED_V1

## Relationship to ROUTING_COMPLETE

ROUTING_COMPLETE and CONTRACT_CLOSED are complementary, not redundant:

- **ROUTING_COMPLETE** (step-local): every code in a step's `result_surface` must have a
  routing declaration in that step's `on_result`. Scope: individual step.
- **CONTRACT_CLOSED** (CC-level): the union of all CC exits must equal `result_status_contract.allowed`.
  Scope: full CC topology.

ROUTING_COMPLETE ensures no step has a declared surface code without a routing decision.
CONTRACT_CLOSED ensures the full topology's exit surface matches the CC contract.

## Rationale

A CC's `result_status_contract.allowed` is a governance contract. Callers of the CC —
workflow nodes, orchestration logic, integration tests — rely on it to declare what outcomes
to handle. If a code can exit the topology but is not in the contract, callers cannot handle
it. If a code is in the contract but no path exits with it, the contract is overclaiming
and callers are writing dead routing branches.

Contract closure is the CC-level equivalent of exhaustive match. It cannot be inferred by
reading individual steps — it requires aggregating all exit paths across the full topology.

---

## What this realizes
```yaml
core:
  rule: For every CC in force, every routing answer is continue or exit, no evaluation block is declared,
    and the set of status codes that can exit the topology (via step exit routes and last-step continue
    routes) equals exactly the set declared in result_status_contract.allowed — no uncontracted exits,
    no unreachable contract codes
  summary: routing has two answers and a CC declares no condition; the union of all codes that can exit
    a CC execution topology must exactly match result_status_contract.allowed; any other routing answer,
    an evaluation block, uncontracted exits and unreachable contract codes are compile-time violations
```
