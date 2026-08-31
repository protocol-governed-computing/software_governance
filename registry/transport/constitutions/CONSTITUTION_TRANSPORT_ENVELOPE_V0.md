# CONSTITUTION_TRANSPORT_ENVELOPE_V0

## Machine

```yaml
fqdn: transport::CONSTITUTION_TRANSPORT_ENVELOPE_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: transport
core:
  enforcement_model: process_and_compiler_enforced
  governs:
  - TI
  - TE
rules:
- applies_to: TI
  enforced_by: transport::INVARIANT_TRANSPORT_CANONICAL_NORMALIZATION_V0
- applies_to: TE
  enforced_by: transport::INVARIANT_TRANSPORT_CANONICAL_NORMALIZATION_V0
- applies_to: TI
  enforced_by: PROCESS_ENFORCED
- applies_to: TE
  enforced_by: PROCESS_ENFORCED
- applies_to: compiled_snapshot
  enforced_by: transport::INVARIANT_INSPECTION_BOUNDARY_COMPOSED_V0
```

---

## §1. Purpose

Governs the **Canonical Transport Contract** — the single protocol-neutral request and
response objects through which every interaction crosses the PGC boundary. The semantic
authority is `TRANSPORT_STANDARD_V0` (§5); this constitution binds its envelope rules into
the governed platform surface.

The canonical contract is the boundary's normalization membrane: inbound interactions are
normalized into a canonical request before admission, and governed outcomes are normalized
into a canonical response before egress. The membrane is explicit, governed, and closed.

---

## §2. Rules

- **Protocol independence.** The canonical request/response and the `TI`/`TE` contracts that
  produce them MUST NOT depend on HTTP, RPC, CLI, or any external protocol. External-protocol
  mechanics live only in adapters (Layer 2).
- **Canonical normalization.** Every `TI` MUST declare an explicit admission normalization
  into the canonical request; every `TE` MUST declare an explicit projection normalization
  from the governed outcome into the canonical response. Raw passthrough of inbound payloads
  or raw execution results is a boundary violation. Enforced by
  `INVARIANT_TRANSPORT_CANONICAL_NORMALIZATION_V0`.
- **Representation independence.** The canonical contract is representation-independent. A
  serialization (JSON in the reference implementation) is not normative unless separately
  specified.

---

## §3. Semantic Category

Under the Governance Ontology, the transport boundary contracts (`TI`, `TE`) and the
canonical envelope they normalize to are **Contractual** — a typed boundary exposed between
the external world and governed execution. They carry no behavior and no domain truth.

---

## §4. Scope

Governs the shape and normalization obligations of the canonical transport envelope and the
`TI`/`TE` contracts that produce it. It does **not** govern external-protocol mechanics
(adapter-owned) or execution semantics (`execution_topology`).

---

## §5. Versioning

This constitution is version-immutable. Any normative change requires a new version
(`CONSTITUTION_TRANSPORT_ENVELOPE_V1`); it is never edited in place.

---

## What this realizes
```yaml
core:
  description: Governs the canonical, protocol-neutral, representation-independent transport
    envelope and the normalization membrane declared by TI/TE contracts.
rules:
- rule_id: TRANSPORT_ENVELOPE_PROTOCOL_INDEPENDENT
  constraint: the canonical transport contract MUST NOT depend on any external protocol
- rule_id: TRANSPORT_ENVELOPE_NORMALIZED
  constraint: TI and TE MUST declare explicit normalization; raw passthrough is forbidden
- rule_id: TRANSPORT_ENVELOPE_REPRESENTATION_INDEPENDENT
  constraint: a serialization of the canonical contract is not normative unless separately specified
```
