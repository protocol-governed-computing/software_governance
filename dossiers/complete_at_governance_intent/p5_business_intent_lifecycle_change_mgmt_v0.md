# Stage 5 — Business Intent — lifecycle / change_mgmt

## Machine

```yaml
document:
  phase: p5
  domain: lifecycle
  subdomain: change_mgmt
  cr: complete_at_governance_intent
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Change Management subdomain governs how a change to a composition is judged: the phases from
    the seed to the authoring mandate, the gates that close them, and the dossier that records them.
    This change states how a change is judged when construction renders none of what it delivers.
  purpose_provenance:
  - source: Change seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: null
  subdomain_purposes:
  - subdomain: change_mgmt
    purpose: Change Management states, in the constitution that governs every dossier, that an authored change runs every phase from the seed to governance intent and is complete there.
    source_finding: {phase: p0, register: cr_type, row: 1}
  scope_boundary:
  - capability: Stating that an authored change runs every phase and is complete at governance intent
    status: IN_SCOPE
    notes: None of the phases from the seed to governance intent is optional
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - capability: Stating where an authored change's review gate is presented
    status: IN_SCOPE
    notes: Presented at governance intent; approval remains the reviewer's act
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - capability: Stating as an invariant that an authored change has no design intent
    status: IN_SCOPE
    notes: Governed by the lifecycle constitution, realised by the design compiler
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - capability: Refusing a design intent for an authored change, and declaring delivery in the seed
    status: DEFERRED
    notes: The design language is changed by the transformation repository
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - capability: Rendering a constitution from registers
    status: DEFERRED
    notes: A constitution's content is argument, which no register holds
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - capability: Changing which families construction renders
    status: DEFERRED
    notes: This change states how an authored change is judged, not what construction does
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  business_objects: []
  identity_semantics: []
  invariants:
  - invariant: An authored change runs every phase from the seed to governance intent.
    business_reason: An authored change is judged as any other change is, up to the point where an artifact would be rendered.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: An authored change has no design intent and no authoring mandate.
    business_reason: Construction renders nothing it delivers, so there is nothing to design or schedule.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: An authored change that has reached governance intent is approvable, not approved.
    business_reason: Approval is the reviewer's act, and no phase decides it.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  actions:
  - action: Judge an authored change
    object: authored change
    trigger: Requested by the author of the change
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  provisional_codes: []
  cross_subdomain_refs: []
```

Every row cites the seed row it states.

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References
