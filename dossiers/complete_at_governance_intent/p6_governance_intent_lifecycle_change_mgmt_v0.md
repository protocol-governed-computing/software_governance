# Stage 6 — Governance Intent — lifecycle / change_mgmt

## Machine

```yaml
document:
  phase: p6
  domain: lifecycle
  subdomain: change_mgmt
  cr: complete_at_governance_intent
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Stating that an authored change runs every phase and is complete at governance intent
    owner_subdomain: change_mgmt
    disposition: OWNED
    existing_artifact: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    source_finding: {phase: p5, register: scope_boundary, row: 1}
  - capability: Stating where an authored change's review gate is presented
    owner_subdomain: change_mgmt
    disposition: OWNED
    existing_artifact: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    source_finding: {phase: p5, register: scope_boundary, row: 2}
  - capability: Stating as an invariant that an authored change has no design intent
    owner_subdomain: change_mgmt
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 3}
  - capability: Refusing a design intent for an authored change, and declaring delivery in the seed
    owner_subdomain: change_mgmt
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 4}
  - capability: Rendering a constitution from registers
    owner_subdomain: change_mgmt
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 5}
  - capability: Changing which families construction renders
    owner_subdomain: change_mgmt
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, row: 6}
  storage_governance:
  - storage_need: The lifecycle constitution
    purpose: The constitution is held in the composition as an authored document, and a clause is added to it only under a dossier.
    subdomain: change_mgmt
    source_finding: {phase: p5, register: subdomain_purposes, row: 1}
  cross_subdomain_deps: []
  pps_artifacts_requiring_action:
  - fqdn: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    current_status: Governs every dossier, its phases and its gates; states no last phase for an authored change.
    action: EXTEND
    source_finding: {phase: p5, register: scope_boundary, row: 1}
  boundary_rules:
  - rule_name: CHANGE_MGMT_OWNS_THE_LAST_PHASE
    statement: Only the lifecycle constitution says which phase is a change's last, and for an authored change it is governance intent.
    source_finding: {phase: p5, register: subdomain_purposes, row: 1}
  governance_outcome:
  - capability: Stating that an authored change runs every phase and is complete at governance intent
    owner_subdomain: change_mgmt
    source_finding: {phase: p6, register: ownership, key: Stating that an authored change runs every phase and is complete at governance intent}
  - capability: Stating where an authored change's review gate is presented
    owner_subdomain: change_mgmt
    source_finding: {phase: p6, register: ownership, key: Stating where an authored change's review gate is presented}
  - capability: Stating as an invariant that an authored change has no design intent
    owner_subdomain: change_mgmt
    source_finding: {phase: p6, register: ownership, key: Stating as an invariant that an authored change has no design intent}
```

This change authors clauses of a constitution and one invariant, which construction does not render, so this dossier
is complete at governance intent. Its review gate is presented here.

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome
