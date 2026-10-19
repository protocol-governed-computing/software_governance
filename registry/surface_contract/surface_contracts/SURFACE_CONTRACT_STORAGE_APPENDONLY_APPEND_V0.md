# SURFACE_CONTRACT_STORAGE_APPENDONLY_APPEND_V0

## Purpose

Canonical result surface for append-only storage APPEND operations.

An append-only APPEND can succeed, encounter invalid input (malformed record), or fail
due to storage unavailability. APPEND does not produce NOT_FOUND or ALREADY_EXISTS —
append-only storage grows monotonically. These three outcomes are exhaustive.

---

## Machine

```yaml
fqdn: surface_contract::SURFACE_CONTRACT_STORAGE_APPENDONLY_APPEND_V0
artifact_kind: SURFACE_CONTRACT
version: V0
governed_by: execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0
authority: pgc.platform
concern: surface_contract
governs:
- CS_APPENDONLY_JSONL_V0
op: APPEND
canonical_surface:
- SUCCESS
- VIOLATION
- BACKEND_ERROR
```

---

## What this realizes
```yaml
capability_family: STORAGE_APPENDONLY
```
