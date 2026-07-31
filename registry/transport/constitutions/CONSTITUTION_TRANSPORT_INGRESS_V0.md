# CONSTITUTION_TRANSPORT_INGRESS_V0

## Machine

```yaml
fqdn: fb.transport::CONSTITUTION_TRANSPORT_INGRESS_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: fb.governance::CONSTITUTION_GOVERNANCE_V0
core:
  enforcement_model: process_and_compiler_enforced
  governs:
  - TI
rules:
- applies_to: TI
  enforced_by: fb.transport::INVARIANT_TRANSPORT_TARGET_EXISTS_V0
- applies_to: TI
  enforced_by: fb.transport::INVARIANT_TRANSPORT_NO_DYNAMIC_ROUTING_V0
- applies_to: TI
  enforced_by: fb.transport::INVARIANT_TRANSPORT_NO_WORKFLOW_SEMANTICS_V0
- applies_to: TI
  enforced_by: fb.transport::INVARIANT_TRANSPORT_OPERATION_IDENTITY_INDEPENDENCE_V0
- applies_to: TI
  enforced_by: PROCESS_ENFORCED
```

---

## §1. Purpose

Governs **Transport Ingress** — the `TI` boundary contract by which an external interaction
enters governed execution. The semantic authority is `TRANSPORT_STANDARD_V0` (§6); this
constitution binds its ingress rules into the governed platform surface.

A `TI` declares admission for a stable **Operation Identity**: the input contract by
reference, context requirements, and an **invocation binding** to a governed executable
target. It is a membrane, not an execution stage — it is declared here and resolved by the
compiler, never interpreted at request time.

---

## §2. Rules

- **Invocation target exists.** Every `TI` MUST declare an invocation binding to a governed
  executable target, and that target MUST resolve in the compiled artifact set — no
  inference, no fallback. Enforced by `INVARIANT_TRANSPORT_TARGET_EXISTS_V0`.
- **Static binding, no dynamic routing.** Ingress routing MUST be fully resolved at compile
  time. Conditional, payload-dependent, or runtime-computed target selection is forbidden.
  Enforced by `INVARIANT_TRANSPORT_NO_DYNAMIC_ROUTING_V0`.
- **Membrane, not stage.** A `TI` MUST NOT contain execution logic, capability references
  (`CC`/`CT`/`CS`), side effects, or execution-retry semantics; it MUST NOT read or alter
  execution state. Enforced by `INVARIANT_TRANSPORT_NO_WORKFLOW_SEMANTICS_V0`.
- **Operation Identity independence.** The Operation Identity a `TI` admits MUST be uniquely
  resolvable within the governance universe and MUST NOT equal a workflow (or other target)
  identity; the target is re-pointable without any adapter change. Enforced by
  `INVARIANT_TRANSPORT_OPERATION_IDENTITY_INDEPENDENCE_V0`.
- **Input contract by reference.** A `TI` MUST reference an existing governed input contract
  and MUST NOT define operation input semantics inline. *(Process-enforced: the reference-vs-
  inline distinction awaits a governed input-contract kind.)*
- **Domain separation.** A `TI` MUST NOT define domain state-transition, resource, or result
  semantics; domain meaning enters only through declared execution artifacts. *(Process-
  enforced pending its Phase-3 invariant.)*

---

## §3. Semantic Category

Under the Governance Ontology, a `TI` is **Contractual** — the ingress boundary contract. It
exposes an admission interface and binds it to governed execution; it carries no behavior.

---

## §4. Scope

Governs `TI` admission semantics only. It does **not** govern the external-protocol binding
(adapter-owned), the executable target's behavior (`fb.execution_topology`), or egress (`TE`).

---

## §5. Versioning

Version-immutable. Any normative change requires `CONSTITUTION_TRANSPORT_INGRESS_V1`; never
edited in place.

---

## Rule Statement

```yaml
core:
  description: Governs the TI ingress boundary contract — admission for an Operation Identity,
    static invocation binding to a governed executable target, and membrane isolation from
    execution semantics.
rules:
- rule_id: TI_TARGET_RESOLVES
  constraint: every TI MUST bind to a governed executable target that resolves at compile time
- rule_id: TI_STATIC_ROUTING
  constraint: TI routing MUST be compile-time static; no dynamic or payload-dependent selection
- rule_id: TI_MEMBRANE_NOT_STAGE
  constraint: TI MUST NOT carry execution logic, capability references, side effects, or execution state
- rule_id: TI_OPERATION_IDENTITY_INDEPENDENT
  constraint: the admitted Operation Identity MUST be uniquely resolvable and MUST NOT equal a target identity
- rule_id: TI_INPUT_CONTRACT_BY_REFERENCE
  constraint: TI MUST reference an existing governed input contract and MUST NOT inline input semantics
```
