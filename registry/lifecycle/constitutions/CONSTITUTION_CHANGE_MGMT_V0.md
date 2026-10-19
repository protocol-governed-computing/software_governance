# CONSTITUTION_CHANGE_MGMT_V0

## Machine

```yaml
fqdn: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: lifecycle
core:
  enforcement_model: process_and_compiler_enforced
  governs:
  - INVARIANT
rules:
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_ANNOUNCEMENT_FROM_COMPLETING_ENDING_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_BUILD_ORDER_TOPOLOGICAL_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_BUSINESS_REFUSAL_DISCHARGED_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_CONTENT_ENTERS_AT_OWNING_PHASE_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_DECLARED_ARTIFACT_FULLY_STATED_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_DESIGN_NAMES_RESOLVE_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_EXISTING_ARTIFACT_OBSERVED_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_NEW_IDENTITY_UNUSED_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_NO_QUESTION_LEFT_OPEN_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_PHASE_SPEAKS_ITS_RUNG_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_REACH_DECLARED_AND_USED_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_RESTATEMENT_MATCHES_SOURCE_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_REUSE_FROM_PERMITTING_DOMAIN_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_ROW_PROVENANCE_CITED_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_TOUCHED_SUBDOMAIN_DECLARED_V0
- applies_to: phase_document
  enforced_by: lifecycle::INVARIANT_UPSTREAM_COMMITMENT_CARRIED_V0
- applies_to: phase_gate
  enforced_by: PROCESS_ENFORCED
- applies_to: dossier
  enforced_by: PROCESS_ENFORCED
```

---

## 1. Purpose

This constitution governs the design half of the transformation lifecycle: phases P0 to P8, from a
business problem statement to the Authoring Mandate. It establishes what makes a phase document
admissible, and it hands an admissible mandate to construction, which
`CONSTITUTION_CONSTRUCTION_V0` governs.

## 2. What it governs

- **Phase documents.** A phase document is admissible when every rule its phase seals is
  satisfied. The rules are declared in the phase's register schema and sealed into the phase
  workflow. Each relational rule and each named procedure realises one of the invariants this
  constitution names, and the design compiler enforces them all, with no short-circuit and no
  warning tier.
- **Phase gates.** A human gate closes P0 (the seed says what the business meant), P7 (the dossier
  reviewed as a body) and the mandate. A gate is a governance concern: no rule can decide it.
- **Dossiers.** A dossier is evidence, not an artifact. It lives with the domain it changes, is
  judged against a pinned composition, and is never edited once delivered.

## 3. Principles

- **Phases, not stages.** A dossier has phases P0 to P8. A compilation has stages S1 to S9. No
  document uses one word for the other.
- **Each phase answers one question.** P1 to P4 state what the business needs, P5 its intent, P6
  where it is owned, P7 how it is built, and P8 in what order. A phase speaks only its rung.
- **Validation is against a named baseline.** A dossier pins the composition it changes. A phase
  judged against any other composition is refused before it is judged.
- **Determinism decides admissibility.** A drafting worker may propose a register. Only the sealed
  rules and the human gates admit it.

## 4. Non-goals

This constitution does not govern construction, compilation, or runtime execution.

---

## 5. Supersedes

`CONSTITUTION_CHANGE_MGMT_V0` governed the same pipeline as stages 0 to 7, enforced by process
alone. This version restates it as phases and names the invariants the design compiler enforces.
