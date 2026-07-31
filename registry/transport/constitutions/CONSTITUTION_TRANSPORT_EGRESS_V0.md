# CONSTITUTION_TRANSPORT_EGRESS_V0

## Machine

```yaml
fqdn: fb.transport::CONSTITUTION_TRANSPORT_EGRESS_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: fb.governance::CONSTITUTION_GOVERNANCE_V0
core:
  enforcement_model: process_and_compiler_enforced
  governs:
  - TE
rules:
- applies_to: TE
  enforced_by: fb.transport::INVARIANT_TRANSPORT_CANONICAL_NORMALIZATION_V0
- applies_to: TE
  enforced_by: fb.transport::INVARIANT_TRANSPORT_NO_WORKFLOW_SEMANTICS_V0
- applies_to: TE
  enforced_by: fb.transport::INVARIANT_TRANSPORT_RESULT_CLASS_PROTOCOL_INDEPENDENCE_V0
- applies_to: TE
  enforced_by: fb.transport::INVARIANT_TRANSPORT_RESPONSE_PROJECTION_EXTERNAL_V0
- applies_to: TE
  enforced_by: PROCESS_ENFORCED
```

---

## §1. Purpose

Governs **Transport Egress** — the `TE` boundary contract by which a governed outcome is
projected back out. The semantic authority is `TRANSPORT_STANDARD_V0` (§7); this constitution
binds its egress rules into the governed platform surface.

A `TE` **declares** the governed classification of outcomes into a protocol-neutral **Result
Class** and the permitted projection of result payload and evidence. It is a declaration —
compiled and applied at runtime — not a runtime decision engine. A PGC Result exists
independently of any transport boundary; the `TE` projects it, it does not own it.

---

## §2. Rules

- **Projection normalization.** Every `TE` MUST declare an explicit projection from the
  governed outcome into the canonical response. Raw execution-result passthrough leaks
  internal state and is a boundary violation. Enforced by
  `INVARIANT_TRANSPORT_CANONICAL_NORMALIZATION_V0`.
- **Membrane, not stage.** A `TE` MUST NOT contain execution logic, capability references
  (`CC`/`CT`/`CS`), or side effects; it MUST NOT alter execution state. Enforced by
  `INVARIANT_TRANSPORT_NO_WORKFLOW_SEMANTICS_V0`.
- **Result Class protocol independence.** A Result Class
  (`SUCCESS | VIOLATION | UNAUTHORIZED | EXECUTION_FAILURE | OPERATION_NOT_FOUND`) MUST carry
  no protocol semantics (no HTTP status, no RPC error code). Enforced by
  `INVARIANT_TRANSPORT_RESULT_CLASS_PROTOCOL_INDEPENDENCE_V0`.
- **Response projection is external.** Mapping a Result Class to an external representation
  (HTTP status, RPC error, CLI exit code) MUST occur in the adapter, never in a `TE`.
  Enforced by `INVARIANT_TRANSPORT_RESPONSE_PROJECTION_EXTERNAL_V0`.
- **Domain separation.** A `TE` MUST NOT define domain-specific result interpretation; result
  meaning is governed, not domain-encoded at the boundary. *(Process-enforced pending its
  Phase-3 invariant.)*

---

## §3. Semantic Category

Under the Governance Ontology, a `TE` is **Contractual** — the egress boundary contract. It
exposes a classification-and-projection interface over governed outcomes; it carries no
behavior. The governed outcome it projects is itself an **Evidential/Operational** runtime
construct, not a transport artifact.

---

## §4. Scope

Governs `TE` egress semantics only. It does **not** govern the adapter's response projection
(external), the producing execution (`fb.execution_topology`), or ingress (`TI`).

---

## §5. Versioning

Version-immutable. Any normative change requires `CONSTITUTION_TRANSPORT_EGRESS_V1`; never
edited in place.

---

## Rule Statement

```yaml
core:
  description: Governs the TE egress boundary contract — declared classification of governed
    outcomes into protocol-neutral Result Classes and the permitted projection of result and
    evidence, isolated from execution and external-protocol semantics.
rules:
- rule_id: TE_PROJECTION_NORMALIZED
  constraint: every TE MUST declare an explicit projection; raw result passthrough is forbidden
- rule_id: TE_MEMBRANE_NOT_STAGE
  constraint: TE MUST NOT carry execution logic, capability references, side effects, or execution state
- rule_id: TE_RESULT_CLASS_PROTOCOL_INDEPENDENT
  constraint: a Result Class MUST carry no external-protocol semantics
- rule_id: TE_PROJECTION_EXTERNAL
  constraint: Result Class to external representation mapping MUST live in the adapter, never in TE
```
