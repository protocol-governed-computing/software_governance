# CONSTITUTION_CONSTRUCTION_V1

## Machine

```yaml
fqdn: lifecycle::CONSTITUTION_CONSTRUCTION_V1
supersedes: lifecycle::CONSTITUTION_CONSTRUCTION_V0
artifact_kind: CONSTITUTION
version: V1
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: lifecycle
core:
  enforcement_model: process_and_compiler_enforced
  governs:
  - INVARIANT
rules:
- applies_to: design
  enforced_by: lifecycle::INVARIANT_DESIGN_UNIQUELY_DETERMINES_ARTIFACT_V0
- applies_to: design
  enforced_by: lifecycle::INVARIANT_MEANING_CHANGE_IS_NEW_IDENTITY_V0
- applies_to: design
  enforced_by: lifecycle::INVARIANT_ONE_PRODUCER_PER_ARTIFACT_V0
- applies_to: design
  enforced_by: lifecycle::INVARIANT_RENDER_INVENTS_NOTHING_V0
- applies_to: construction_emit
  enforced_by: PROCESS_ENFORCED
```

---

## 1. Purpose

This constitution governs the construction half of the transformation lifecycle: rendering the
artifacts an admissible Authoring Mandate schedules. `CONSTITUTION_CHANGE_MGMT_V1` governs the
design that construction reads.

## 2. What it governs

- **Designs.** Construction renders only what a design determines, and stops rather than supply a
  fact the design does not state. Each property it holds to is one of the invariants this
  constitution names, and the construction compiler enforces them on every design it renders.
- **Emission.** Rendered artifacts are written into a domain's registry only after construction
  completeness is total and the human who drives the change accepts them. The compiler then judges
  them like any other artifact.

## 3. Principles

- **A design failure and a construction failure are different.** A design that is incomplete or
  contradictory is refused by its phase. A valid design that does not determine an artifact is a
  defect in the design language, refused by construction.
- **Meaning decides identity.** An amendment that changes what an artifact means takes a new
  identity. One that does not keeps it.

## 4. Non-goals

This constitution does not govern phase documents, compilation, or runtime execution.

---

## 5. Supersedes

`CONSTITUTION_CONSTRUCTION_V0` governed construction as stages 8 and 9 with a build sheet set and a
construction record, enforced by process alone. This version names the invariants the construction
compiler enforces.
