# Stage 5 — Business Intent: platform / capability_transforms

**Stage:** 5 — Business Intent
**CR:** molecule_composition
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The capability transforms subdomain governs the units of computation a governed act performs: what a
transform is, what it is composed of, how it runs, and whether its result is determined by its
inputs, as each transform declares. A transform is either an atom, one implementation with one
result, or a molecule, a stated sequence of steps in which a loop may run a composed body once per
member of a stated collection. Its authority is to decide the shape of a transform and how that shape
runs, and it decides nothing about what any domain computes or whether a computation should be one
step or several.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| capability_transforms | Governs the transform — its kind, its composition, how it runs, and whether its result is determined by its inputs. | S1 cr_type #1 |
| design | Governs how a design states what a change will build, extended so a design can state a molecule's steps. | S1 governance_scope #2 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| State how a molecule runs | IN_SCOPE | Nothing says it today; stated in its own constitution. | S4 authoring_scope #1 |
| Admit an atom declaring it is not deterministic, and forbid it side effects | IN_SCOPE | Stated in its own constitution; the existing one stays unchanged. | S4 authoring_scope #2 |
| Place every transform under exactly one constitution by its kind and declared purity | IN_SCOPE | Decided by what a transform declares, not by convention. | S4 authoring_scope #3 |
| Refuse at build a molecule that cannot be run, contains itself, or claims a purity its steps do not have | IN_SCOPE | A molecule that cannot keep its declaration never enters a composition. | S4 authoring_scope #4 |
| Run a molecule's steps in order, a loop's body once per member | IN_SCOPE | The only execution path the platform has. | S4 authoring_scope #5 |
| Write one evidence record per step a molecule runs | IN_SCOPE | A decision inside a molecule is observable when made. | S4 authoring_scope #6 |
| State and render a molecule in a design | IN_SCOPE | The design language anticipates a molecule by kind only. | S4 authoring_scope #7 |
| Show the path holds end to end | IN_SCOPE | Delivered as the domain half: a conformance workload designed and constructed through its own change once this change lands, because it needs the extended renderer to be constructed at all. | S4 authoring_scope #8 |
| Record every non-deterministic result, and replay from the records | IN_SCOPE | Keeps the platform within the determinism and replay its standard requires. | S4 authoring_scope #9 |
| Refuse routing on a non-deterministic result before a deterministic step consumes it | IN_SCOPE | A non-deterministic step may propose and never decide. | S4 authoring_scope #10 |
| Renaming the existing constitution for deterministic atoms | DEFERRED | To its next version, made for its own reasons. | S4 authoring_scope deferred #1 |
| What any domain composes | DEFERRED | Each domain's business, stated in its own change. | S4 authoring_scope deferred #2 |
| Whether any domain uses a non-deterministic transform | DEFERRED | Each domain decides, and declares it where it is made. | S4 authoring_scope deferred #3 |

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
| Every molecule in a composition can be run. | A molecule that cannot run is a declaration nothing can keep. | S4 constraint_register #1 |
| A molecule's steps run in their declared order. | The order is the composition a reader relies on. | S4 constraint_register #2 |
| A loop runs its body exactly once per member of its stated collection. | A loop's length never depends on the data it computes, so the repetition stays bounded and visible. | S4 constraint_register #3 |
| No molecule contains itself. | A molecule containing itself is repetition with no stated bound. | S4 constraint_register #4 |
| A molecule declared pure contains only pure steps. | The declaration is what a reader relies on to see where determinism ends. | S4 constraint_register #5 |
| Every step a molecule runs leaves one evidence record. | A decision inside a molecule is observable when it is made, not only declared. | S4 constraint_register #6 |
| Every transform declares whether it is deterministic. | A reader must see exactly where determinism ends. | S4 constraint_register #7 |
| No transform has side effects. | Side effects are the business of capability side effects, whatever a transform's purity. | S4 constraint_register #8 |
| No existing transform changes; the platform grows by adding. | A platform that must re-author its past to grow cannot grow. | S4 constraint_register #13 |
| Each transform is governed by exactly one of the three constitutions. | A transform naming the wrong constitution would escape its rules. | S4 constraint_register #14 |
| Every result a non-deterministic atom produced is recorded. | Determinism holds only relative to what was recorded. | S4 constraint_register #15 |
| A replay reproduces the same result from the same inputs and recorded outcomes, and never runs a non-deterministic atom. | Replay is what lets anyone re-establish a determination after the fact. | S4 constraint_register #16 |
| Nothing routes directly on a non-deterministic atom's result. | Otherwise governance would reduce to recording what the non-deterministic step said. | S4 constraint_register #17 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| State how a molecule runs | Molecule | The model being declared for the first time. | IN_SCOPE | S4 capability_graph #2 |
| Admit a non-deterministic atom | Atom | A design declaring an atom's result is not determined by its inputs. | IN_SCOPE | S4 capability_graph #3 |
| Place a transform under its constitution | Transform | A composition being built. | IN_SCOPE | S4 capability_graph #4 |
| Refuse a molecule | Molecule | A composition built with a molecule that cannot keep its declaration. | IN_SCOPE | S4 capability_graph #7 |
| Run a molecule | Molecule | A governed act running one. | IN_SCOPE | S4 capability_graph #8 |
| Record a step's evidence | Evidence record | A step inside a molecule running. | IN_SCOPE | S4 capability_graph #9 |
| State a molecule in a design | Molecule | A change whose design composes transforms. | IN_SCOPE | S4 capability_graph #10 |
| Record a non-deterministic result, and replay from it | Recorded outcome | A non-deterministic atom producing a result; a run being replayed. | IN_SCOPE | S4 capability_graph #12 |
| Refuse routing on a non-deterministic result | Composition | A design routing on a non-deterministic result before a deterministic step consumes it. | IN_SCOPE | S4 capability_graph #13 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| NONE IDENTIFIED |

Constitutions and invariants are governance surface, authored rather than constructed, and belong to
no construction family. The conformance workload that shows the path holds is the domain half of this
change and receives its codes in its own change.

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
