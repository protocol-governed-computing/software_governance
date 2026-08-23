# INVARIANT_RUNTIME_INVARIANT_WIRED_V0

## Machine

```yaml
fqdn: execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: execution
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - WF
  - CC
```

## Summary

Constitutional rule that runtime business invariants must be bound to the
capability-contract outcome-routing mechanism that enforces them. The runtime is
unchanged; this is verified at compile time by `ASSERT_RUNTIME_INVARIANT_WIRED_V0`.

## What this realizes
```yaml
core:
  description: 'Every runtime-enforced business invariant must be wired to a real enforcement point. A
    runtime invariant (core.enforcement_stage contains "runtime_outcome") is enforced through the existing
    capability-contract outcome-routing mechanism: an enforcing CC emits a non-SUCCESS violation outcome
    which the enforcing workflow routes to a terminal node, and the trace is classified as a BUSINESS_VIOLATION.
    This invariant requires that each such declaration is authoritative — bound to a CC that declares
    the violation outcome and a workflow that routes it to the declared terminal — so that no runtime
    invariant is decorative.

    '
  anti_patterns:
  - unbound_invariant: runtime invariant missing runtime_binding fields
  - missing_outcome: enforcing CC does not declare the violation outcome in result_surface
  - missing_route: enforcing workflow does not route the violation outcome to the declared terminal node
  - decorative_governance: invariant artifact exists but no enforcement point upholds it
```
