# SURFACE_CONTRACT_REGISTRY_RESOLVE_V0

## Purpose

Canonical result surface for registry READ (resolve/lookup) operations.

A registry READ operation can succeed with the resolved record, report that the key is not
registered, encounter an invalid input, or fail due to storage unavailability. These four
outcomes are exhaustive.

---

## Machine

```yaml
fqdn: surface_contract::SURFACE_CONTRACT_REGISTRY_RESOLVE_V0
artifact_kind: SURFACE_CONTRACT
version: V0
governed_by: execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0
authority: pgc.platform
concern: surface_contract
governs:
- CS_REGISTRY_V0
op: READ
canonical_surface:
- SUCCESS
- NOT_FOUND
- VIOLATION
- BACKEND_ERROR
```

---

## What this realizes
```yaml
capability_family: REGISTRY
```
