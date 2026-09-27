# Stage 5 — Business Intent: platform / conformance

**Stage:** 5 — Business Intent
**CR:** platform_test_data
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
| conformance | Governs how the platform proves that what a composition declares is what runs — for a transform, by its test vectors, run in the build of whoever supplies it, on every build. | S1 cr_type #1 |
| structure | Governs how each build is declared, extended so every platform build compiles the platform's vectors. | S1 governance_scope #2 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| State that a transform's vectors run in its supplier's build | IN_SCOPE | A new version of the constitution governing vectors. | S4 authoring_scope #1 |
| Compile the platform's vectors in every platform build | IN_SCOPE | New versions of the three platform build declarations. | S4 authoring_scope #2 |
| Run the platform's vectors after each platform build compiles | IN_SCOPE | The step a domain's build already takes. | S4 authoring_scope #3 |
| Tell a build's own transforms from carried ones by what the compiler carried in | IN_SCOPE | Never by name. | S4 authoring_scope #4 |
| Refuse a build with any failed case | IN_SCOPE | Whoever supplies the transform. | S4 authoring_scope #5 |
| Bring the inherited vectors across, re-judged | IN_SCOPE | Every correction and drop recorded with its reason. | S4 authoring_scope #6 |
| Carry the platform's result into the snapshot and check it | IN_SCOPE | Carried already; the check is reversed. | S4 authoring_scope #7 |
| Vectors for ai_governance's own transforms | DEFERRED | ai_governance's question, in its own change. | S4 authoring_scope deferred #1 |
| A vector for the platform transform no inherited case tests | DEFERRED | None is invented here. | S4 authoring_scope deferred #2 |
| How much proof is enough beyond the inherited cases | DEFERRED | The inherited cases are the floor they were. | S4 authoring_scope deferred #3 |

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
| Every platform vector tests a platform transform the composition declares. | A vector for nothing proves nothing. | S4 constraint_register #1 |
| Every platform vector runs on every build of the platform. | Each composition states what it proved, and the code is proven again each time. | S4 constraint_register #2 |
| No build with a failed case is admitted. | A failed case that admits its build is the silence conformance exists to end. | S4 constraint_register #3 |
| A transform's vectors run in the build of its supplier and nowhere else. | A vector proves its supplier's code. | S4 constraint_register #4 |
| No inherited case is kept as written only because it was inherited. | Inheritance is not evidence. | S4 constraint_register #5 |
| The platform's build never proves a domain's transforms. | The platform does not own a domain's implementations. | S4 constraint_register #8 |
| No vector is invented for a platform transform the reference implementation never tested. | This change lifts proof; it does not author it. | S4 constraint_register #10 |
| A domain that carries a platform transform reports it as carried, unchanged. | A domain's result states what that domain proved. | S4 constraint_register #12 |
| A build's own transforms are told from carried ones by what the compiler carried in, never by name. | A name says nothing about who supplies the code. | S4 constraint_register #13 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| State where a transform's vectors run | Test vector | The supplier of the platform's transforms being the platform. | IN_SCOPE | S4 capability_graph #1 |
| Compile the platform's vectors | Test vector | A platform build compiling. | IN_SCOPE | S4 capability_graph #2 |
| Run the platform's vectors | Platform conformance result | A platform build's compile succeeding. | IN_SCOPE | S4 capability_graph #3 |
| Record the transforms a build carried in | Carried transform | A build carrying a platform transform. | IN_SCOPE | S4 capability_graph #4 |
| Refuse a build with a failed case | Platform conformance result | Any case failing. | IN_SCOPE | S4 capability_graph #5 |
| Restate and re-judge an inherited case | Inherited case | The platform's vectors being authored. | IN_SCOPE | S4 capability_graph #6 |
| Carry the platform's result into the composition | Platform conformance result | A composition being assembled. | IN_SCOPE | S4 capability_graph #7 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| NONE IDENTIFIED |

The constitution, the platform's build declarations and its vectors are governance surface, authored
rather than constructed, and belong to no construction family.

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
