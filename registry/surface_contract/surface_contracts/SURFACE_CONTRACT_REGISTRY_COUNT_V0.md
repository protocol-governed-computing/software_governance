# SURFACE_CONTRACT_REGISTRY_COUNT_V0

## Purpose

Canonical result surface for registry COUNT operations.

A registry COUNT operation either succeeds with a count or fails due to storage unavailability.
COUNT does not produce NOT_FOUND (the count of a missing key is 0, not an error) and does not
produce VIOLATION (COUNT takes no input that can be invalid). These two outcomes are exhaustive.

---

## Machine

```yaml
fqdn: surface_contract::SURFACE_CONTRACT_REGISTRY_COUNT_V0
artifact_kind: SURFACE_CONTRACT
version: V0
governed_by: execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0
authority: pgc.platform
concern: surface_contract
governs:
- CS_REGISTRY_V0
op: COUNT
canonical_surface:
- SUCCESS
- BACKEND_ERROR
```

---

## What this realizes
```yaml
capability_family: REGISTRY
```
