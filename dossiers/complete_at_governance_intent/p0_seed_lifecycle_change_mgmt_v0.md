# Change Seed — lifecycle / change_mgmt

## Machine

```yaml
document:
  phase: p0
  domain: lifecycle
  subdomain: change_mgmt
  cr: complete_at_governance_intent
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Change Management subdomain governs how a change to a composition is judged: the phases from
    the seed to the authoring mandate, the gates that close them, and the dossier that records them.
    This change states how a change is judged when construction renders none of what it delivers.
  cr_type:
  - subdomain: change_mgmt
    classification: MODIFY
    rationale: The constitution already governs every dossier; this change adds the ruling for a change whose deliverable is authored, and authors no artifact into the subdomain.
  business_vocabulary:
  - term: Authored Change
    definition: A change whose deliverable is written by a person and rendered by no construction, such as a constitution, an invariant, a schema, or the derive route's code and sealed documents.
  - term: Governance Intent
    definition: The phase that says where a change is owned, and the last phase an authored change runs.
  - term: Review Gate
    definition: The gate at which a reviewer approves a dossier as a body.
  - term: Lifecycle Constitution
    definition: The constitution that governs every dossier, its phases and its gates.
  requested_outcomes:
  - outcome: The lifecycle constitution states that an authored change runs the phases from the seed to governance intent, and that none of them is optional.
  - outcome: The lifecycle constitution states that an authored change is complete at governance intent.
  - outcome: The lifecycle constitution states that an authored change's review gate is presented at governance intent, and that approving it remains the reviewer's act.
  - outcome: An invariant governed by the lifecycle constitution states that a change whose seed declares it authored has no design intent.
  known_facts:
  - fact: A design has no family for a constitution, an invariant, a schema or the derive route's code, and the renderer has no builder for any of them.
    certainty: HIGH
  - fact: An authored change runs the phases from the seed to governance intent, and is complete there.
    certainty: HIGH
  - fact: The ruling is written only in the transformation repository's account of a change.
    certainty: HIGH
  - fact: The first route change judged by the phases looked for the ruling in the composition, did not find it, and relied on the repository's statement.
    certainty: HIGH
  - fact: The gate that locks a mandate has nothing to lock for an authored change.
    certainty: HIGH
  - fact: This change is itself an authored change.
    certainty: HIGH
  system_beliefs:
  - belief: The lifecycle constitution does not already state that an authored change is complete at governance intent.
    why_it_matters: The change adds the ruling only if the constitution lacks it.
    verification_goal: Confirm the lifecycle constitution does not state the ruling.
  - belief: The design compiler already refuses a design that amends an artifact it cannot author.
    why_it_matters: That refusal covers an authored change that amends an artifact, and not one that only adds an artifact.
    verification_goal: Confirm what the design-intent rule set refuses for an artifact whose family has no builder.
  assumptions: []
  constraints:
  - constraint: A constitution is authored, and no construction renders it.
    source: Business policy
  - constraint: A clause that governs dossiers has a dossier behind it.
    source: Business policy
  business_invariants:
  - invariant: An authored change runs every phase from the seed to governance intent.
  - invariant: An authored change has no design intent and no authoring mandate.
  - invariant: An authored change that has reached governance intent is approvable, not approved.
  lifecycle_states:
  - object: Authored Change
    state: In flight
    meaning: Its dossier has not yet reached governance intent.
  - object: Authored Change
    state: Complete
    meaning: Its dossier is admissible from the seed to governance intent, and its review gate is presented.
  business_events:
  - event: Authored Change Complete
    when_it_occurs: When its governance intent is admissible and its review gate is presented.
    significance: A reviewer may approve the authoring of what the dossier argues for.
  authority_boundaries:
  - business_object: Authored Change
    authoritative_owner: The person who authors the dossier
  - business_object: Review Gate
    authoritative_owner: The reviewer
  - business_object: Lifecycle Constitution
    authoritative_owner: Change Management
  out_of_scope:
  - item: The design compiler's rule, and the seed's declaration of delivery.
    reason: The design language is changed by the transformation repository.
  - item: Rendering a constitution from registers.
    reason: A constitution's content is argument, which no register holds.
  - item: Changing which families construction renders.
    reason: This change states how an authored change is judged, not what construction does.
  governance_scope:
  - scope_item: change_mgmt
    relationship: EXTENDED
  - scope_item: design
    relationship: ADJACENT
  clarification_requests: []
  acceptance_criteria:
  - criterion: The lifecycle constitution states that an authored change runs every phase from the seed to governance intent.
  - criterion: The lifecycle constitution states that an authored change is complete at governance intent.
  - criterion: The lifecycle constitution states that an authored change's review gate is presented at governance intent and that approval remains the reviewer's act.
  - criterion: An invariant governed by the lifecycle constitution states that a change whose seed declares it authored has no design intent.
  identity_and_sameness: null
  lifecycle_transitions: null
  operation_refusals: null
  authority_deferrals: null
```

Reorganized faithfully from `p0_business_problem_statement.md`. Human input only — nothing here was
added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals
