# INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1

## Machine

```yaml
fqdn: execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1
supersedes: execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0
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
  - WF
```

---

## Summary

An unrouted status code is an ungoverned execution path. If a step declares that its
capability may produce `VIOLATION` (via `result_surface`) but its `on_result` has no entry
for `VIOLATION`, the runtime has no declared path — it must guess, default, or crash.
All three outcomes violate deterministic execution topology.

Routing completeness is validated step-locally against `result_surface`, not against the
CC-level `result_status_contract.allowed`. Different steps bind different capabilities with
different reachable outcome sets. A pure transform step cannot produce BACKEND_ERROR; a
registry side-effect step cannot produce custom domain status codes. Forcing every step to
route the full CC contract would require ghost routes for codes the step's capability cannot
produce — governance noise, not governance.

## What this realizes
For every execution topology step in a CC pipeline:
1. Every step MUST declare a `result_surface` — the set of status codes that step's specific
   capability can actually produce. It MUST hold every outcome that capability declares: a side
   effect's operation declares its `result_status_values`, and a transform declares `SUCCESS`, and
   `VIOLATION` unless its `refusal` is `never` (`3d` CP-13)
2. `on_result` MUST contain an entry for every code in that step's `result_surface`
3. Each routing value MUST be exactly one of: `continue`, `exit`, or an evaluation target
   name declared in the CC's `evaluation` block
4. `on_result` MUST NOT contain status codes not declared in that step's `result_surface`
   (unknown routes are governance noise)
5. `on_result` is a finite lookup map — no expressions, no conditions, no dynamic predicates

## Where it applies
- **Artifact Types**: CC
- **Validation Phase**: compile_time
- **Enforced By**: ASSERT_TOPOLOGY_ROUTING_COMPLETE_V1

## Rationale

Routing completeness is the topology equivalent of exhaustive pattern matching. When every
result code in a step's declared surface has a routing outcome, the step is deterministic:
given any result the capability can actually produce, the runtime knows exactly what to do
next. No defaults. No implicit fallbacks. No runtime inference.

Step-local validation against `result_surface` is correct because the capability surface is
per-step, not per-CC. A CC contract declares what the full topology can surface to callers.
A step's `result_surface` declares what that step's specific capability can produce. These
are different scopes. ROUTING_COMPLETE governs the step scope.
CC-level contract closure is governed by INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V0.

## Why the surface cannot narrow the capability

The step's `result_surface` is the author's statement; the capability's declaration is the platform's.
Checked only against the first, a step could leave out an outcome its capability can produce, and the
check would pass a step that has no route for it. The SoSyM study found fourteen such steps in three
domains. One of them let a failed lookup carry on, and the person was accepted. So the surface is
checked against what the capability declares, and a step answers for the whole of it (`3d` CP-13).

---

## What this realizes
```yaml
core:
  rule: The result_surface of every step must hold every outcome the capability it dispatches declares,
    and the on_result map must contain an entry for every code in that result_surface; a narrowed surface
    or an unrouted surface code is an ungoverned execution path and a compile-time violation
  summary: a step answers every outcome its capability declares; a surface narrower than the capability,
    or a surface code without routing, constitutes an ungoverned execution path
```
