# SURFACE_CONTRACT_TRANSPORT_SEND_V0

## Header

- **Artifact Code:** SURFACE_CONTRACT_TRANSPORT_SEND_V0
- **Artifact Kind:** surface_contract
- **Governed By:** fb.topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0
- **Version:** V0
- **Status:** canonical

---

## Purpose

Canonical result surface for transport SEND operations.

A transport SEND can succeed, encounter invalid input (malformed payload or target), or
fail due to transport unavailability. These three outcomes are exhaustive. Transport
capabilities MUST NOT introduce domain-specific result codes at the step level.

---

## Machine

```yaml
artifact_kind: SURFACE_CONTRACT
version: V0
governed_by: fb.topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0
surface_contract_code: SURFACE_CONTRACT_TRANSPORT_SEND_V0
governs: []
op: SEND
canonical_surface:
- SUCCESS
- VIOLATION
- BACKEND_ERROR
```

---

## Rule Statement

```yaml
capability_family: TRANSPORT
```
