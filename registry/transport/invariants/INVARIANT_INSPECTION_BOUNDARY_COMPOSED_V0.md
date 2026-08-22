# INVARIANT_INSPECTION_BOUNDARY_COMPOSED_V0

## Machine

```yaml
fqdn: transport::INVARIANT_INSPECTION_BOUNDARY_COMPOSED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: transport
core:
  enforcement_stage:
  - composition_conformance
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    scope: ALL_ARTIFACTS
  applies_to_kinds:
  - SNAPSHOT
  composition_check:
    rule: at_least_one
    subject: composed inspection boundary contract
    selector:
      artifact_type: TI
      where:
        handler.kind: SNAPSHOT_READ
```

---

## Purpose

A snapshot that carries no inspection boundary cannot be inspected. Nothing about such a snapshot
is malformed — it composes cleanly, verifies, and executes — which is precisely the problem: the
absence is invisible until a consumer tries to inspect and finds no operations declared.

Compiling the inspection tool domain is a **mandatory activation step**, not an optional
composition choice, because consumers expect inspection to be available. This invariant makes the
step load-bearing: forget it, and assembly fails with a named cause rather than producing a
snapshot that is silently unusable by every inspection client.

The defect it prevents is a specific one, observed in practice. `compile.sh` compiles only the
platform; each domain needs its own `compile_domain.sh` run. Miss one and the assembler composes
whatever compiled roots exist and reports success — correctly, since a composition without a given
domain is still a valid composition. "Assembly succeeded" was therefore not evidence that the
intended composition had been assembled. Now it is, for this domain.

---

## Scope

**Applies to:** the composed snapshot, evaluated by the Composition Conformance phase.

The selector matches transport ingress contracts whose handler kind is `SNAPSHOT_READ` — the
inspection boundary itself, rather than the domain that happens to publish it. That is deliberate:
the requirement is that a caller can *ask something*, and it stays true if the inspection surface
is ever re-homed to a different namespace or split across several. A selector naming a namespace
or a build-config artifact would assert where the contracts live, which is not what any consumer
depends on.

`at_least_one` rather than `exactly_one`: the inspection surface publishes one contract per
operation, and the count is expected to grow as operations are added. Fixing a number here would
make adding an operation a governance violation.

---

## Why this invariant lives in the platform

**A rule requiring a domain cannot live inside that domain.** Composition Conformance evaluates
rules read from the assembled snapshot's own artifacts; an invariant authored in the inspection
domain would be composed only when that domain is composed. Omit the domain and the rule vanishes
with it, the phase finds nothing to evaluate, and the composition passes — reporting green over an
empty set.

That vacuity pattern has bitten this codebase repeatedly: four profile invariants sat unevaluated
across two migrations, and vocabulary rules silently skipped because no vocabulary artifact was in
the domain build's set. The structural fix is the same each time — **the checker must not be a
member of the thing it checks.** The platform is present in every composition by construction, so
a rule authored here is always evaluated.

---

## Rule Statement

```yaml
core:
  description: 'Every assembled composition MUST carry at least one transport ingress contract
    declaring a SNAPSHOT_READ handler kind.

    Inspection is a consumer-facing capability of the platform, not an optional extra: clients,
    CI gates and change-management tooling all address a snapshot through the si. operation family.
    A composition that omits the inspection boundary offers those consumers nothing, and does so
    without any other symptom.

    The rule is deliberately about the BOUNDARY, not about a namespace or a build manifest: what a
    consumer depends on is that inspection operations are declared, not where they were authored.

    '
  anti_patterns:
  - uncompiled_inspection_domain: 'the inspection tool domain was not compiled before assembly,
      so no boundary contract entered the composition

      '
  - inspection_rule_self_hosted: 'a rule requiring the inspection boundary is authored inside the
      inspection domain, so omitting the domain also omits the rule and the check passes vacuously

      '
```

## Version History

- **V0**: First composition-scoped invariant covering the inspection boundary. Introduces the
  `at_least_one` cardinality rule, for a subject whose expected count grows with the operation set.
