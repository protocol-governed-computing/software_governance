# INVARIANT_TRANSPORT_RESPONSE_PROJECTION_EXTERNAL_V0

## Machine

```yaml
fqdn: fb.transport::INVARIANT_TRANSPORT_RESPONSE_PROJECTION_EXTERNAL_V0
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

Mapping a governed Result Class to an external representation (HTTP status, RPC error, CLI
exit code) is adapter-owned and protocol-specific. A `TE` MUST NOT declare any such
projection. A `TE` that maps outcomes to protocol representations collapses the
transport/adapter separation the boundary exists to protect.

---

## Scope

**Applies to:** all `TE_` artifacts.

**Does NOT apply to:** the adapter's own response-projection table (external, correct).

---

## Rule Statement

```yaml
core:
  description: 'A TE MUST NOT declare external-protocol response projection (HTTP status, RPC
    error, CLI exit code, or an equivalent status map). Projection is adapter-owned.'
  anti_patterns:
  - protocol_projection_in_te: TE declares http_status, status_code, exit_code, rpc_error, or a status map
```
