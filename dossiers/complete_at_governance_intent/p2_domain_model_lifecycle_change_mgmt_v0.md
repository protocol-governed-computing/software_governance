# Stage 2 — Domain Model — lifecycle / change_mgmt

## Machine

```yaml
document:
  phase: p2
  domain: lifecycle
  subdomain: change_mgmt
  cr: complete_at_governance_intent
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Authored change
    description: A change whose deliverable is written by a person and rendered by no construction.
    store_model: One dossier per change, kept with the domain it changes as evidence and never in the composition.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: Review gate
    description: The gate at which a reviewer approves a dossier as a body.
    store_model: Presented in the last phase document of the dossier, and approved by the reviewer.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - entity: Lifecycle constitution
    description: The constitution that governs every dossier, its phases and its gates.
    store_model: One authored document in the composition, stating its principles as prose.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  entity_attributes:
  - entity: Authored change
    attribute: Last phase
    meaning: The phase at which the change is complete, which for an authored change is governance intent.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  business_processes:
  - process: Judge an authored change
    initiator: The person who authors the dossier
    outcome: The dossier is admissible from the seed to governance intent, and its review gate is presented.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  process_steps:
  - process: Judge an authored change
    step: '1'
    action: Judge every phase document from the seed to governance intent against the documents before it
    record_produced: One verdict per phase
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Judge an authored change
    step: '2'
    action: Present the review gate at governance intent
    record_produced: A dossier that is approvable
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  belief_verification:
  - belief: The lifecycle constitution does not already state that an authored change is complete at governance intent.
    result: VERIFIED
    evidence: lifecycle::CONSTITUTION_CHANGE_MGMT_V0 states that each phase answers one question and names the gates that close P0, P7 and the mandate. It does not state when an authored change is complete.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The design compiler already refuses a design that amends an artifact it cannot author.
    result: VERIFIED
    evidence: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 seals the rule AMENDED_ARTIFACT_NOT_AUTHORABLE, which refuses a design that amends an artifact whose family has no builder. It refuses nothing for a design that only adds such an artifact.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  pps_baseline_fqdns:
  - capability: Governing the change lifecycle
    fqdn: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    what_it_does: States the principles every dossier is judged by, and the gates that close its phases.
    fit: PARTIAL
    cannot_do: It does not state that an authored change is complete at governance intent, or where its review gate is presented.
  - capability: Judging governance intent
    fqdn: transformation::WF_P6_GOVERNANCE_INTENT_ADMISSIBILITY_V0
    what_it_does: Judges a governance intent against the business intent and the seed before it.
    fit: EXACT
    cannot_do: It judges one document; it does not say which phase is a change's last.
  gaps:
  - gap: The lifecycle constitution does not state that an authored change runs every phase from the seed to governance intent and is complete there.
    severity: MAJOR
    impact: A dossier that relies on the ruling cannot find it in the composition that judges it.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - gap: The lifecycle constitution names no review gate at governance intent.
    severity: MINOR
    impact: An authored change's review gate is stated only outside the composition.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - gap: No invariant states that a change whose seed declares it authored has no design intent.
    severity: MAJOR
    impact: A design intent for an authored change that only adds an artifact is refused by nothing.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  architectural_observations:
  - observation: The design compiler refuses an authored change that amends an artifact, and nothing refuses one that only adds an artifact.
    evidence: transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  discovery_concerns:
  - concern: The constitution is authored, so nothing re-renders it and compares it with this dossier.
    evidence: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: constraints, row: 1}
  open_questions: []
```

Every row cites the change-request row it models.

---

## 1. Business Entities

---

## 2. Business Processes

---

## 3. Belief Verification — THE SPINE (fill this register FIRST)

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3
