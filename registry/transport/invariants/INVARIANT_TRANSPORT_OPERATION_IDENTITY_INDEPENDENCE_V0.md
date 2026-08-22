# INVARIANT_TRANSPORT_OPERATION_IDENTITY_INDEPENDENCE_V0

## Machine

```yaml
fqdn: transport::INVARIANT_TRANSPORT_OPERATION_IDENTITY_INDEPENDENCE_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: transport
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - TI
```

---

## Purpose

The Operation Identity a `TI` admits is the stable, protocol-neutral public name of a
governed interaction. It MUST exist and MUST be independent of the implementation it binds
to: it MUST NOT equal a workflow identity, nor its own invocation target. The public name is
re-pointable to a new target with no adapter change; conflating the two collapses that
indirection.

---

## Scope

**Applies to:** all `TI_` artifacts.

---

## Rule Statement

```yaml
core:
  description: 'Every TI MUST declare an Operation Identity, and that identity MUST NOT equal
    a workflow identity or its own bound invocation target.'
  anti_patterns:
  - operation_missing: TI declares no operation identity
  - operation_equals_workflow: operation identity equals a WF identity
  - operation_equals_target: operation identity equals its own handler target
```
