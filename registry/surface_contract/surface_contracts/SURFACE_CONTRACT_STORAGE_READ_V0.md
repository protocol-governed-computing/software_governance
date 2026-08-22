# SURFACE_CONTRACT_STORAGE_READ_V0

## Purpose

Canonical result surface for mutable storage READ operations.

A storage READ can succeed with the document, report that the document does not exist,
encounter invalid input, or fail due to storage unavailability. These four outcomes are
exhaustive across all mutable storage capabilities.

---

## Machine

```yaml
fqdn: surface_contract::SURFACE_CONTRACT_STORAGE_READ_V0
artifact_kind: SURFACE_CONTRACT
version: V0
governed_by: execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0
authority: pgc.platform
concern: surface_contract
governs:
- CS_MUTABLE_JSON_V0
- CS_NAME_REGISTRY_V0
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
capability_family: STORAGE
```
