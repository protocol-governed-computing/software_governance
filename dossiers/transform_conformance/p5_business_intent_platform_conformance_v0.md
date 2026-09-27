# Stage 5 — Business Intent: platform / conformance

**Stage:** 5 — Business Intent
**CR:** transform_conformance
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The conformance subdomain governs how the platform proves that what a composition declares is what
runs. For a transform, whose implementation lives outside the composition, the proof is its test
vectors: stated inputs and the outputs the transform must produce from them, run against the transform
exactly as the composition sealed it. Its authority is to decide what a vector is, what it may assert,
where it is run and what counts as proven, and it decides nothing about what any transform computes or
how much proof a design judges enough.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| conformance | Governs how the platform proves that what a composition declares is what runs — for a transform, by its test vectors, run in its domain's build on every build. | S1 cr_type #1 |
| design | Governs how a design states what a change will build, extended so a design states a transform's vectors and is refused a transform without them. | S1 governance_scope #2 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| State what a vector proves | IN_SCOPE | A new version of the constitution governing vectors. | S4 authoring_scope #1 |
| Hold a vector's assertions to known forms by a check that runs | IN_SCOPE | Replaces a rule bound to a compiler phase that does not exist. | S4 authoring_scope #2 |
| Refuse a vector whose recorded results do not match the purity of what it tests | IN_SCOPE | Refused when the domain compiles. | S4 authoring_scope #3 |
| Run every transform's vectors in its domain's build, on every build, and stop the build on a failure | IN_SCOPE | Where the platform's build manifest said conformance belongs. | S4 authoring_scope #4 |
| Prove a molecule with a non-deterministic step by its recorded results | IN_SCOPE | Every such vector is also a proof of replay. | S4 authoring_scope #5 |
| Report every transform proven, unproven or refused by name | IN_SCOPE | Never success over nothing. | S4 authoring_scope #6 |
| Keep runnable cases apart from composition conformance evidence, and carry each domain's result into the composition | IN_SCOPE | Composition evidence stays where it is. | S4 authoring_scope #7 |
| State vectors in a design, and refuse a transform authored or amended without one | IN_SCOPE | The design is where a new transform can be told from an existing one. | S4 authoring_scope #8 |
| Show a molecule with a non-deterministic step proven in a composition | IN_SCOPE | Delivered as the domain half: the conformance workloads' next change, designed with vectors from the start once this change lands, because it needs the extended design language to be designed at all. | S4 authoring_scope #9 |
| Vectors for each transform that already exists | DEFERRED | To the domain that owns it, until its next change to the transform. | S4 authoring_scope deferred #1 |
| What any transform does | DEFERRED | Each domain's business, stated in its own change. | S4 authoring_scope deferred #2 |
| How much proof is enough beyond one vector | DEFERRED | Each design judges it. | S4 authoring_scope deferred #3 |
| Sealing the code a composition vouches for | DEFERRED | Running every vector on every build binds declaration and code until it is taken up. | S4 authoring_scope deferred #4 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| NONE IDENTIFIED |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Every vector tests a transform the composition declares. | A vector for nothing proves nothing. | S4 constraint_register #1 |
| Every vector runs against the transform as sealed. | Proof of anything other than what runs is proof of the wrong thing. | S4 constraint_register #2 |
| A domain with a failed vector is not admitted to a composition. | A transform that does not do what it says never enters a composition. | S4 constraint_register #3 |
| Every transform is either proven or named as unproven. | An unproven transform reported as passing misleads every reader of the composition. | S4 constraint_register #4 |
| A vector supplies recorded results for exactly the non-deterministic steps of what it tests. | A vector that does not match what it tests proves nothing about it. | S4 constraint_register #5 |
| No vector's run runs a non-deterministic step whose result it supplies. | The vector's expected result is exact only because the step's result is supplied. | S4 constraint_register #6 |
| Transform conformance evidence and composition conformance evidence are kept apart. | Two kinds of proof in one place are read as one. | S4 constraint_register #7 |
| A domain's transforms are proven in that domain's own build, never in the platform's. | The platform does not own a domain's implementations and cannot vouch for them. | S4 constraint_register #8 |
| Vectors are authored in the design, never by hand beside the code. | A vector written by hand is proof nobody gated. | S4 constraint_register #10 |
| A transform authored or amended after this change is refused at design without a vector. | A new transform enters the composition proven. | S4 constraint_register #13 |
| Every build runs every vector; no earlier result stands for a later build. | The composition seals a transform's declaration and not its code, so only running the vector shows the code still does what it says. | S4 constraint_register #14 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| State what a vector proves | Test vector | The model being restated for molecules and recorded results. | IN_SCOPE | S4 capability_graph #1 |
| Check a vector's assertions | Test vector | A domain compiling a vector. | IN_SCOPE | S4 capability_graph #2 |
| Refuse a vector whose recorded results do not match | Test vector | A domain compiling a vector for a molecule. | IN_SCOPE | S4 capability_graph #4 |
| Run a domain's vectors | Runnable case | A domain being built. | IN_SCOPE | S4 capability_graph #5 |
| Prove a molecule by its recorded results | Runnable case | A molecule's vector being run. | IN_SCOPE | S4 capability_graph #6 |
| Report a domain's transforms by standing | Domain conformance result | A domain's vectors having run. | IN_SCOPE | S4 capability_graph #7 |
| Carry a domain's result into the composition | Domain conformance result | A composition being assembled. | IN_SCOPE | S4 capability_graph #8 |
| State a transform's vectors in a design | Test vector | A change whose design authors or amends a transform. | IN_SCOPE | S4 capability_graph #9 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| NONE IDENTIFIED |

Constitutions and invariants are governance surface, authored rather than constructed, and belong to
no construction family. The conformance workload that shows a molecule proven in a composition is the
domain half of this change and receives its codes in its own change.

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|
| NONE IDENTIFIED |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 0, Stage 4 | subdomain_purpose · actors · bm_entities · resources · events · capability_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · subdomain_purposes · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
