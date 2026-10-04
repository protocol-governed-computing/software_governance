# INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V1

## Machine

```yaml
fqdn: cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V1
artifact_kind: INVARIANT
version: V1
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: cryptographic_trust
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    scope: ALL_ARTIFACTS
  applies_to_kinds:
  - SNAPSHOT
  composition_check:
    rule: exactly_one
    subject: cryptographic trust structure carried by the composition
    selector:
      namespace: cryptographic_trust
      artifact_type: STRUCTURE
      artifact_code_prefix: STRUCTURE_CRYPTOGRAPHIC_TRUST_
```

---

## Purpose

Trust posture is declared for every composition, even one built for unsigned local development.
`LOCAL_DEV_UNSIGNED` is not an absence of trust governance. It states that no cryptographic
verification is required of this composition, and a reader can see that it says so.

The surface may declare every trust mode its constitution authorizes. A build configuration names
one in `trust_mode`, the compiler materializes only the structure declaring it, and this invariant
counts what the composition carries.

## What this realizes
For every compiled snapshot:
1. The composition MUST carry exactly one cryptographic trust structure.
2. That structure's `trust_mode` is the composition's trust mode.
3. Compile MUST fail if the composition carries none, or more than one.

## Anti-Patterns

- `no_trust_structure`: a composition carrying no trust structure, so declaring no trust mode
- `several_trust_structures`: a composition carrying more than one, so declaring two answers
- `runtime_trust_negotiation`: a runtime selecting or upgrading the trust mode at execution time

## Change from V0

V0 selected the trust contract by `status: active` on the structure, so the trust mode was a
property of the surface's inventory. A surface declaring two modes was malformed, even when two
compositions built from it each wanted one. V1 counts what the composition carries, the same change
`INVARIANT_EXECUTION_PLACEMENT_DECLARED_V1` made for placement.

## Enforcement

- **Stage:** compiler_validation
- **Failure Mode:** FAIL_COMPILE — no snapshot is produced if violated

---

## What this realizes
```yaml
core:
  rule: 'A composition MUST carry exactly one cryptographic trust structure. None is a missing
    declaration; more than one is an ambiguity.

    '
  summary: Every composition carries exactly one cryptographic trust structure, and so declares one trust mode
assert_projection:
  enforcement:
    failure_mode: HARD_FAIL
```
