# Stage 6 — Governance Intent: platform / capability_transforms

**Stage:** 6 — Governance Intent
**CR:** molecule_composition
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `capability_transforms` — EXISTING — extended by this CR |
| Authority class | reuse existing — the platform states how transforms run, a design declares what it composes and whether each transform is deterministic; no new actor type |
| Governing constitutions | `capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0` (unchanged), and two siblings this change authors: one for molecules, one for atoms declaring they are not deterministic |

A transform's kind, its composition and its determinism are the transform's own concerns, so the
model belongs to the subdomain that governs transforms. It is stated in two sibling constitutions
beside the existing one, which stays unchanged and keeps governing every transform that exists: the
platform grows by adding. The design language that lets a design state a molecule belongs to the
design subdomain; the compiler's checks and the runtime's execution, recording and replay realize the
model and own no rule of it.

**No domain artifact appears in the action registers below.** The one transform that repeats a
computation today, and the domain whose need surfaced this change, are recorded at S2 and S3 as what
was observed in the composition this dossier was validated against. What any domain composes is that
domain's business. The conformance workload that shows the path holds is the domain half of this
change and is scheduled by its own change once this one is delivered.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| State how a molecule runs | capability_transforms | OWNED | | S4 gap_register GAP-01 |
| Admit an atom declaring it is not deterministic, and forbid it side effects | capability_transforms | OWNED | | S4 gap_register GAP-02 |
| Place every transform under exactly one constitution by its kind and declared purity | capability_transforms | OWNED | | S4 gap_register GAP-03 |
| Refuse at build a molecule that cannot be run, contains itself, or claims a purity its steps do not have | capability_transforms | OWNED | | S4 gap_register GAP-04 |
| Run a molecule's steps in order, a loop's body once per member | capability_transforms | OWNED | | S4 gap_register GAP-05 |
| Write one evidence record per step a molecule runs | capability_transforms | OWNED | | S4 gap_register GAP-06 |
| State and render a molecule in a design | design | OWNED | | S4 gap_register GAP-07 |
| Show the path holds end to end | capability_transforms | OWNED | | S4 gap_register GAP-08 |
| Record every non-deterministic result, and replay from the records | capability_transforms | OWNED | | S4 gap_register GAP-09 |
| Refuse routing on a non-deterministic result before a deterministic step consumes it | capability_transforms | OWNED | | S4 gap_register GAP-10 |
| Keep governing every existing transform as deterministic | capability_transforms | SATISFIED | capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | S4 capability_graph #1 |
| Hold every atom to returning its outcomes | capability_transforms | SATISFIED | capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 | S4 capability_graph #5 |
| Renaming the existing constitution for deterministic atoms | capability_transforms | DEFERRED | | S4 authoring_scope deferred #1 |
| What any domain composes | capability_transforms | DEFERRED | | S4 authoring_scope deferred #2 |
| Whether any domain uses a non-deterministic transform | capability_transforms | DEFERRED | | S4 authoring_scope deferred #3 |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Acts stay acyclic, so repetition belongs to transforms | capability_transforms -> workflow | workflow::CONSTITUTION_WORKFLOW_V0 | SATISFIED | S4 dependency_graph #4 |
| The design language that states a molecule's steps, loop and emission | capability_transforms -> design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | GAP | S4 dependency_graph #7 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|------------------------------------------|----------------|
| capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 | Governs every transform the composition carries and states that every transform is pure. Left unchanged; its accurate name is deferred to its next version. | REUSE | S4 dependency_graph #1 |
| capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 | Holds every atom to returning its outcomes, whatever its determinism. | REUSE | S4 dependency_graph #2 |
| capability_transforms::INVARIANT_CT_SURFACE_CLOSED_V1 | Holds every transform's surface closed. | REUSE | S4 dependency_graph #3 |
| workflow::CONSTITUTION_WORKFLOW_V0 | Holds every act acyclic. | REUSE | S4 dependency_graph #4 |
| transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | Admits a transform's kind and no statement of a molecule's steps. Its rule set is extended and re-sealed. | EXTEND | S4 dependency_graph #7 |
| capability_side_effects::CS_CLOCK_V0 | The existing precedent for a value that varies and is recorded where it is used. Examined; unchanged. | REVIEW | S3 analysis_findings #10 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| THE_PLATFORM_GROWS_BY_ADDING | No existing transform changes. The existing constitution keeps governing every transform that exists, and what it does not describe is stated beside it. | S4 constraint_register #13 |
| ONE_TRANSFORM_ONE_CONSTITUTION | Each transform is governed by exactly one constitution, decided by its kind and declared purity: a deterministic atom by the existing one, a molecule by the molecule constitution, a non-deterministic atom by its own. | S4 constraint_register #14 |
| EVERY_MOLECULE_CAN_RUN | A molecule whose steps or loop body cannot be run never enters a composition. | S4 constraint_register #1 |
| THE_DECLARED_ORDER_IS_THE_ORDER | A molecule's steps run in their declared order. | S4 constraint_register #2 |
| EVERY_PASS_RUNS | A loop runs its body exactly once per member of its stated collection, so its length never depends on the data it computes. | S4 constraint_register #3 |
| NO_MOLECULE_CONTAINS_ITSELF | A molecule containing itself, directly or through others, is repetition with no stated bound and is refused. | S4 constraint_register #4 |
| PURITY_IS_DECLARED_AND_TRUE | Every transform declares whether it is deterministic; a molecule declared pure contains only pure steps. | S4 constraint_register #7 |
| NO_TRANSFORM_HAS_SIDE_EFFECTS | Whatever its purity, a transform has no side effects; they belong to capability side effects. | S4 constraint_register #8 |
| EVERY_STEP_LEAVES_EVIDENCE | Every step a molecule runs leaves one record naming its results and not their values. | S4 constraint_register #6 |
| NON_DETERMINISM_IS_RECORDED | Every result a non-deterministic atom produces is recorded when produced, and determinism holds relative to the recorded outcomes. | S4 constraint_register #15 |
| REPLAY_NEVER_RERUNS_NON_DETERMINISM | A replay reproduces the result from the same inputs and the recorded outcomes, and never runs a non-deterministic atom. | S4 constraint_register #16 |
| OFFERED_NEVER_DECIDED | Nothing routes on a non-deterministic atom's result until a deterministic step has consumed it. | S4 constraint_register #17 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| State how a molecule runs | capability_transforms | S4 gap_register GAP-01 |
| Admit an atom declaring it is not deterministic, and forbid it side effects | capability_transforms | S4 gap_register GAP-02 |
| Place every transform under exactly one constitution by its kind and declared purity | capability_transforms | S4 gap_register GAP-03 |
| Refuse at build a molecule that cannot be run, contains itself, or claims a purity its steps do not have | capability_transforms | S4 gap_register GAP-04 |
| Run a molecule's steps in order, a loop's body once per member | capability_transforms | S4 gap_register GAP-05 |
| Write one evidence record per step a molecule runs | capability_transforms | S4 gap_register GAP-06 |
| State and render a molecule in a design | design | S4 gap_register GAP-07 |
| Show the path holds end to end | capability_transforms | S4 gap_register GAP-08 |
| Record every non-deterministic result, and replay from the records | capability_transforms | S4 gap_register GAP-09 |
| Refuse routing on a non-deterministic result before a deterministic step consumes it | capability_transforms | S4 gap_register GAP-10 |

---

## Gate 1 — Design Approval

**Gate 1 closes at this stage for this dossier.** The governance surface is authored, not
constructed, so this change is terminal at P6, and the gate that reviews a dossier as a body belongs
at the end of the dossier. Stages 0 through 6 are presented for review as a body; approval
authorizes the authoring of the two sibling constitutions and the invariants that hold them, the
compiler's checks, the runtime's execution, evidence, recording and replay, and the design language's
statement and rendering of a molecule.

Gate 2 has no subject here: no mandate is drafted, so there is none to lock.

**Status: CLOSED.** Approved by the business author, as a body, against the composition
`1b0cfbd3d094…` — the same composition every grounded register of this dossier was re-read against
and attested to in `baseline.json`. What approval authorizes is the authoring described above, and
nothing else: a clause that appears in the governance surface beyond what this dossier argues for is
an ungoverned change, and the dossier is what that statement points at.

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE — APPROVED |
