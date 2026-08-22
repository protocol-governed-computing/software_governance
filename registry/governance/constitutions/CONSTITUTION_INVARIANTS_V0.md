# CONSTITUTION_INVARIANTS_V0

## Machine
```yaml
fqdn: governance::CONSTITUTION_INVARIANTS_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: governance
core:
  enforcement_model: compiler_enforced
  governs:
  - INVARIANT
rules:
- applies_to: INVARIANT
  enforced_by: federation::INVARIANT_AUTHORITY_CONSTITUTED_V0
- applies_to: INVARIANT
  enforced_by: federation::INVARIANT_CONCERN_NOT_AUTHORITY_V0
- applies_to: INVARIANT
  enforced_by: artifact::INVARIANT_SCHEMA_CONFORMANCE_V0
- applies_to: INVARIANT
  enforced_by: conformance::INVARIANT_ASSERT_PARITY_V0
- applies_to: INVARIANT
  enforced_by: artifact::INVARIANT_SCHEMA_CONFORMANCE_V0
- applies_to: ALL_ARTIFACTS
  enforced_by: artifact::INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0
- applies_to: ALL_ARTIFACTS
  enforced_by: artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0
- applies_to: INVARIANT
  enforced_by: artifact::INVARIANT_NO_SHORT_NAME_REFERENCE_V0
- applies_to: INVARIANT
  enforced_by: artifact::INVARIANT_UNIQUE_ARTIFACT_ID_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_BINDING_INTEGRITY_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_BINDING_SURFACE_CLOSED_V0
- applies_to: CC
  enforced_by: capability_contracts::INVARIANT_CC_STORAGE_OP_CONFORMANCE_V0
- applies_to: CT
  enforced_by: capability_transforms::INVARIANT_CT_OUTPUT_CONTRACT_MATCH_V0
- applies_to: INVARIANT
  enforced_by: execution::INVARIANT_NO_SMART_EXECUTION_V0
- applies_to: INVARIANT
  enforced_by: surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0
- applies_to: INVARIANT
  enforced_by: execution::INVARIANT_RUNTIME_INVARIANT_WIRED_V0
- applies_to: ALL_ARTIFACTS
  enforced_by: execution_topology::INVARIANT_TOPOLOGY_ACYCLIC_V0
- applies_to: TI_TE
  enforced_by: transport::INVARIANT_TRANSPORT_CANONICAL_NORMALIZATION_V0
- applies_to: TI_TE
  enforced_by: transport::INVARIANT_TRANSPORT_NO_DYNAMIC_ROUTING_V0
- applies_to: TI_TE
  enforced_by: transport::INVARIANT_TRANSPORT_NO_WORKFLOW_SEMANTICS_V0
- applies_to: TI_TE
  enforced_by: transport::INVARIANT_TRANSPORT_TARGET_EXISTS_V0
- applies_to: ALL_ARTIFACTS
  enforced_by: artifact::INVARIANT_FQDN_NAMESPACE_AUTHORIZED_V0
```

---

## 1. Purpose

Defines the canonical structure and semantics of **INVARIANT artifacts**.

An INVARIANT declares a **cross-cutting constraint that MUST always hold true**.

INVARIANTS are declarative and are enforced via ASSERT artifacts during compilation.

---

## 2. Core Model

```text
INVARIANT → declares constraint
ASSERT    → evaluates constraint
COMPILER  → enforces constraint
```

## 3. Core Principles

### 3.1 Declarative Only

INVARIANTS MUST declare constraints only.
They MUST NOT contain executable logic.

### 3.2 Mandatory Enforcement

Every INVARIANT MUST be enforced by at least one ASSERT.

### 3.3 Fail-Fast

Violations MUST result in immediate compilation failure.

### 3.4 Negative Enforcement

INVARIANTS define forbidden states:
- System MUST NOT do X

### 3.5 No Conditional Enforcement

INVARIANTS are always enforced.
No debug modes, no environment toggles.

## 4. Required Fields (Documentation)

```yaml
fqdn: <namespace>::INVARIANT_<NAME>_V<N>
artifact_kind: INVARIANT
version: V<N>
governed_by: governance::CONSTITUTION_INVARIANTS_V0

core:
  description: <constraint description>

  enforcement_stage:
    - compiler_validation

  scope:
    - <artifact_types>

  violation_response: FAIL_IMMEDIATELY

  enforced_by:
    - ASSERT_<NAME>_V<N>

  anti_patterns:
    - <pattern>: "<description>"

  clarification:
    <case>: "<boundary explanation>"
```

## 5. Binding Contract

### 5.1 Required

Every INVARIANT MUST:
- declare enforced_by ASSERT(s)

### 5.2 Consistency Rule

INVARIANT.enforced_by MUST match ASSERT.enforces

### 5.3 Illegal States

System MUST fail if:
- INVARIANT has no ASSERT
- ASSERT does not reference INVARIANT
- mismatch exists

## 6. Enforcement Semantics

- INVARIANT does NOT execute
- ASSERT evaluates INVARIANT
- COMPILER enforces result

## 7. Naming

`INVARIANT_<CONSTRAINT>_V<N>`

## 8. System Guarantees

No constraint exists without enforcement

## 9. Constitutional Violations

- Missing enforced_by
- violation_response not FAIL_IMMEDIATELY
- missing enforcement_stage
- missing anti_patterns

## 10. One-Line Truth

INVARIANT defines what must never be violated.

---

## Rule Statement

```yaml
core:
  description: Governs INVARIANT artifacts — declarative constraints that must never be violated
rules:
- rule_id: INVARIANT_DECLARATIVE_ONLY
  constraint: INVARIANT MUST declare constraints only; MUST NOT contain executable logic
- rule_id: INVARIANT_MANDATORY_ENFORCEMENT
  constraint: every INVARIANT MUST be enforced by at least one ASSERT
- rule_id: INVARIANT_FAIL_FAST
  constraint: 'violation_response MUST match the invariant''s enforcement class: FAIL_IMMEDIATELY (or
    WARN where the constitution admits it) for compiler-staged invariants, BUSINESS_VIOLATION for runtime_outcome
    invariants. The pairing is enforced by SCHEMA_INVARIANT_V0''s conditional contract.'
```
