# SURFACE_CONTRACT_REGISTRY_DEREGISTER_V0

## Purpose

Canonical result surface for registry DEREGISTER operations.

A registry DEREGISTER operation can succeed, report that the key was not found, or fail
due to storage unavailability. Invalid input is caught upstream before reaching the DEREGISTER
operation. These three outcomes are exhaustive.

---

## Machine

```yaml
fqdn: surface_contract::SURFACE_CONTRACT_REGISTRY_DEREGISTER_V0
artifact_kind: SURFACE_CONTRACT
version: V0
governed_by: execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0
authority: pgc.platform
concern: surface_contract
governs:
- CS_REGISTRY_V0
op: DEREGISTER
canonical_surface:
- SUCCESS
- NOT_FOUND
- BACKEND_ERROR
```

---

## What this realizes
```yaml
capability_family: REGISTRY
```
