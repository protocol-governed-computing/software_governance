# CONSTITUTION_ADMISSION_V0

## Machine
```yaml
fqdn: transport::CONSTITUTION_ADMISSION_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: transport
core:
  enforcement_model: runtime_enforced
  governs:
  - WF
rules:
- applies_to: WF
  enforced_by: RUNTIME_ENFORCED
- applies_to: WF
  enforced_by: RUNTIME_ENFORCED
- applies_to: WF
  enforced_by: RUNTIME_ENFORCED
- applies_to: WF
  enforced_by: transport::INVARIANT_ADMISSION_COVERS_BINDINGS_V0
```

---

## §1. Purpose

Admission decides whether a workflow MAY proceed past its entrance. It does not decide how the
workflow executes.

An **IN gate** is the point of admission. It is a node of the workflow, so admission is part of the
declared topology rather than a phase beside it.

Admission is **read-only**. An IN gate SHALL NOT:
- mutate the payload;
- emit side effects;
- dispatch capabilities.

---

## §2. What an IN gate determines

An IN gate judges the payload against its **declared input contract** and nothing else.

| Contract term | The gate refuses when |
|---|---|
| `required: true` | the field is absent |
| `type` | the field is present and does not have the declared type |

Any failed check is NACK. Every check passing is ACK. Prose on the gate, such as
`extensions.admission_rules`, determines nothing (MB-1). Where a gate must enforce more than its
contract states, the contract is what must say so.

A gate that declares no input contract refuses. A declared admission point that determines nothing
would behave like one that permits (AI-6).

---

## §3. Outcome and routing

ACK and NACK are outcomes, and the workflow routes them as it routes any other outcome. A refusal
is therefore carried by the topology, not raised past it. An outcome with no declared routing and no
declared ending refuses (EX-5).

---

## §4. Evidence

The runtime records every check the gate evaluated, held or not, with the outcome. A reader can see
which check refused, and an admission is evidenced as fully as a refusal (EN-12). The checks name
fields and declared types, never payload values.

---

## §5. Declaration site

An IN gate's input contract is its intent's `core.inputs`: each field's `type` and whether it is
`required`. The compiler projects it into the snapshot's dispatch table. The runtime reads the
compiled contract and nothing else.

The workflow behind the gate reads payload fields through its bindings (`$.payload.<field>`). Every
field it binds is declared by the gate's contract, so nothing the workflow reads enters unchecked.
The compiler enforces this (`transport::INVARIANT_ADMISSION_COVERS_BINDINGS_V0`). A field the gate
declares and no node binds is allowed: the gate may require it for accountability.

---

## §6. Versioning

A change to this constitution's semantics requires a new version.

---

## What this realizes
```yaml
core:
  description: Governs admission at a workflow's IN gate, determined from the gate's declared input contract
rules:
- rule_id: ADMISSION_READ_ONLY
  constraint: an IN gate MUST NOT mutate the payload, emit side effects or dispatch capabilities
- rule_id: ADMISSION_FROM_CONTRACT_ONLY
  constraint: an IN gate MUST determine admission from its declared input contract alone, and a gate with no contract MUST refuse
- rule_id: ADMISSION_OUTCOME_IS_ROUTED
  constraint: ACK and NACK MUST be routed by the workflow, and every evaluated check MUST be recorded in the trace
- rule_id: ADMISSION_COVERS_BINDINGS
  constraint: a workflow MUST bind only payload fields its IN gate's input contract declares
```
