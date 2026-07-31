# INVARIANT_TRANSPORT_RESULT_CLASS_PROTOCOL_INDEPENDENCE_V0

## Machine

```yaml
fqdn: fb.transport::INVARIANT_TRANSPORT_RESULT_CLASS_PROTOCOL_INDEPENDENCE_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.governance::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - TE
```

---

## Purpose

A Result Class is governed and protocol-neutral. Every class a `TE` emits — through its
`result_classification` map and `default_result_class` — MUST be one of the governed
classes and MUST NOT encode an external-protocol response semantic (no HTTP status, no RPC
error code). Protocol meaning enters only in the adapter's response projection.

---

## Scope

**Applies to:** all `TE_` artifacts.

Governed classes: `SUCCESS`, `VIOLATION`, `UNAUTHORIZED`, `EXECUTION_FAILURE`,
`OPERATION_NOT_FOUND`.

---

## Rule Statement

```yaml
core:
  description: 'Every Result Class a TE emits MUST be a governed, protocol-neutral class;
    protocol-specific response semantics are forbidden in a TE.'
  anti_patterns:
  - non_governed_result_class: result_classification or default maps to a class outside the governed set
  - protocol_result_class: a result class carries HTTP/RPC/CLI response semantics
```
