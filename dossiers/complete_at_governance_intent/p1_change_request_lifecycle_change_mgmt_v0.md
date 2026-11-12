# Stage 1 — Change Request: Clarification & Fact Capture: lifecycle / change_mgmt

## Machine

```yaml
document:
  phase: p1
  domain: lifecycle
  subdomain: change_mgmt
  cr: complete_at_governance_intent
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: change_mgmt
    classification: MODIFY
    rationale: The constitution already governs every dossier; this change adds the ruling for a change whose deliverable is authored, and authors no artifact into the subdomain.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Authored Change
    definition: A change whose deliverable is written by a person and rendered by no construction, such as a constitution, an invariant, a schema, or the derive route's code and sealed documents.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Governance Intent
    definition: The phase that says where a change is owned, and the last phase an authored change runs.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Review Gate
    definition: The gate at which a reviewer approves a dossier as a body.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Lifecycle Constitution
    definition: The constitution that governs every dossier, its phases and its gates.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  requested_outcomes:
  - outcome: The lifecycle constitution states that an authored change runs the phases from the seed to governance intent, and that none of them is optional.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: The lifecycle constitution states that an authored change is complete at governance intent.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: The lifecycle constitution states that an authored change's review gate is presented at governance intent, and that approving it remains the reviewer's act.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: An invariant governed by the lifecycle constitution states that a change whose seed declares it authored has no design intent.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  known_facts:
  - fact: A design has no family for a constitution, an invariant, a schema or the derive route's code, and the renderer has no builder for any of them.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: An authored change runs the phases from the seed to governance intent, and is complete there.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: The ruling is written only in the transformation repository's account of a change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: The first route change judged by the phases looked for the ruling in the composition, did not find it, and relied on the repository's statement.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The gate that locks a mandate has nothing to lock for an authored change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: This change is itself an authored change.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  system_beliefs:
  - belief: The lifecycle constitution does not already state that an authored change is complete at governance intent.
    why_it_matters: The change adds the ruling only if the constitution lacks it.
    verification_goal: Confirm the lifecycle constitution does not state the ruling.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The design compiler already refuses a design that amends an artifact it cannot author.
    why_it_matters: That refusal covers an authored change that amends an artifact, and not one that only adds an artifact.
    verification_goal: Confirm what the design-intent rule set refuses for an artifact whose family has no builder.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  assumptions: []
  constraints:
  - constraint: A constitution is authored, and no construction renders it.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: A clause that governs dossiers has a dossier behind it.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 2}
  business_invariants:
  - invariant: An authored change runs every phase from the seed to governance intent.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: An authored change has no design intent and no authoring mandate.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: An authored change that has reached governance intent is approvable, not approved.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  lifecycle_states:
  - object: Authored Change
    state: In flight
    meaning: Its dossier has not yet reached governance intent.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Authored Change
    state: Complete
    meaning: Its dossier is admissible from the seed to governance intent, and its review gate is presented.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  business_events:
  - event: Authored Change Complete
    when_it_occurs: When its governance intent is admissible and its review gate is presented.
    significance: A reviewer may approve the authoring of what the dossier argues for.
    source_finding: {phase: p0, register: business_events, row: 1}
  authority_boundaries:
  - business_object: Authored Change
    authoritative_owner: The person who authors the dossier
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Review Gate
    authoritative_owner: The reviewer
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Lifecycle Constitution
    authoritative_owner: Change Management
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: The design compiler's rule, and the seed's declaration of delivery.
    reason: The design language is changed by the transformation repository.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Rendering a constitution from registers.
    reason: A constitution's content is argument, which no register holds.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Changing which families construction renders.
    reason: This change states how an authored change is judged, not what construction does.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  governance_scope:
  - scope_item: change_mgmt
    relationship: EXTENDED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: design
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  clarification_requests: []
  acceptance_criteria:
  - criterion: The lifecycle constitution states that an authored change runs every phase from the seed to governance intent.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: The lifecycle constitution states that an authored change is complete at governance intent.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: The lifecycle constitution states that an authored change's review gate is presented at governance intent and that approval remains the reviewer's act.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: An invariant governed by the lifecycle constitution states that a change whose seed declares it authored has no design intent.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  identity_and_sameness: null
  lifecycle_transitions: null
  operation_refusals: null
  authority_deferrals: null
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
