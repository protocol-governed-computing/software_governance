# Stage 4 — Business Model — lifecycle / change_mgmt

## Machine

```yaml
document:
  phase: p4
  domain: lifecycle
  subdomain: change_mgmt
  cr: complete_at_governance_intent
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Author of an authored change
    role: Writes the dossier of a change whose deliverable no construction renders
    authority_class: Operator
    source_finding: {phase: p2, register: business_processes, row: 1}
  bm_entities:
  - entity: Authored change
    description: A change whose deliverable is written by a person and rendered by no construction.
    store_model: One dossier per change, kept with the domain it changes as evidence and never in the composition.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: Review gate
    description: The gate at which a reviewer approves a dossier as a body.
    store_model: Presented in the last phase document of the dossier, and approved by the reviewer.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: Lifecycle constitution
    description: The constitution that governs every dossier, its phases and its gates.
    store_model: One authored document in the composition, stating its principles as prose.
    source_finding: {phase: p2, register: entities, row: 3}
  resources: []
  events:
  - event: Authored change complete
    trigger: When its governance intent is admissible and its review gate is presented
    lifecycle_meaning: A reviewer may approve the authoring of what the dossier argues for.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: Lifecycle constitution
    verb: governs
    object: Authored change
    capability_need: State the last phase of an authored change and where its review gate stands
    source_finding: {phase: p2, register: entities, row: 3}
  capability_graph:
  - capability: Stating that an authored change runs every phase and is complete at governance intent
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    status: GAP
    gap_register_entry: GAP-01
    notes: Added as a principle of the lifecycle constitution.
  - capability: Stating where an authored change's review gate is presented
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    status: GAP
    gap_register_entry: GAP-02
    notes: Added to the constitution's account of the gates.
  - capability: Stating as an invariant that an authored change has no design intent
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    status: GAP
    gap_register_entry: GAP-03
    notes: Authored as a lifecycle invariant the constitution names.
  dependency_graph:
  - from: lifecycle
    to: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    dependency_type: governance
    pps_status: EXTENDED
    source_finding: {phase: p3, register: dependency_discoveries, row: 1}
  - from: lifecycle
    to: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    dependency_type: judgement
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, row: 2}
  constraint_register:
  - number: '1'
    constraint: An authored change runs every phase from the seed to governance intent.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '2'
    constraint: An authored change has no design intent and no authoring mandate.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: An authored change that has reached governance intent is approvable, not approved.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: A constitution is authored, and no construction renders it.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: constraint
  - number: '5'
    constraint: A clause that governs dossiers has a dossier behind it.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: constraint
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, row: 1}
    capability: Stating that an authored change runs every phase and is complete at governance intent
    owner_subdomain: change_mgmt
    resolution: EXTEND
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, row: 2}
    capability: Stating where an authored change's review gate is presented
    owner_subdomain: change_mgmt
    resolution: EXTEND
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, row: 3}
    capability: Stating as an invariant that an authored change has no design intent
    owner_subdomain: change_mgmt
    resolution: AUTHOR_NEW
  design_decisions:
  - number: '1'
    decision: Change Management stays the subdomain it is; the change extends its constitution.
    source_finding: {phase: p3, register: placement_decision, row: 1}
    rationale: The ruling governs the dossiers Change Management already governs.
    constraints_imposed: The constitution gains clauses and names one new invariant; its other rules stay as they are.
  authoring_scope:
  - capability: Stating that an authored change runs every phase and is complete at governance intent
    gap_register_ref: GAP-01
  - capability: Stating where an authored change's review gate is presented
    gap_register_ref: GAP-02
  - capability: Stating as an invariant that an authored change has no design intent
    gap_register_ref: GAP-03
```

Consolidated from the analysis. Every row cites what it consolidates.

---

## 1. Discovery Summary

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)
