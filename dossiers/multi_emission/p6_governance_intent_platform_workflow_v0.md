# Stage 6 — Governance Intent: platform / workflow
**Stage:** 6 — Governance Intent
**CR:** multi_emission
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `platform` |
| Primary subdomain | `workflow` — EXISTING — modified by this CR |
| Authority class | reuse existing — an act announces, a domain declares its moments, the platform states the model; no new actor type |
| Governing constitutions | `fb.workflow::CONSTITUTION_WORKFLOW_V0`, `fb.event::CONSTITUTION_EVENT_V0` |

A terminal node is part of the act, and what an act says it completed is the act's account of itself,
so the model belongs to the subdomain that governs acts. The moment being announced belongs to the
event subdomain; the announcing does not. Nothing new stands on its own, so no subdomain is declared.

**No domain artifact appears in the action registers below.** The acts that announce, the moments they
declare, and the subdomain whose six moments are announced by nothing are recorded at S2 and S3 as
what was observed in the composition this dossier was validated against. Which moments an act
announces is that domain's business, and scheduling it here would claim work this dossier does not
own.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Stating what a terminal node announces | workflow | OWNED | | S4 gap_register GAP-1 |
| Declaring the order normative | workflow | OWNED | | S4 gap_register GAP-2 |
| Announcing an ordered sequence at one ending | workflow | OWNED | | S4 gap_register GAP-3 |
| Reporting an announcement that cannot be made | workflow | OWNED | | S4 gap_register GAP-4 |
| Refusing a moment announced twice | workflow | OWNED | | S4 gap_register GAP-5 |
| Asserting what an act announced | workflow | OWNED | | S4 gap_register GAP-6 |
| Writing one evidence record per moment | workflow | SATISFIED | fb.event::INVARIANT_EV_APPEND_ONLY_V0 | S4 capability_graph #7 |
| A moment announced per member of a collection | workflow | DEFERRED | | S4 authoring_scope deferred #1 |
| Deciding which moments each act announces | workflow | DEFERRED | | S4 authoring_scope deferred #2 |
| Checking that every declared moment is announced by something | workflow | DEFERRED | | S4 authoring_scope deferred #3 |

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
| The moment an announcement names, and the immutability of its record | workflow -> event | fb.event::CONSTITUTION_EVENT_V0 | SATISFIED | S4 dependency_graph #2 |
| The design language that states a terminal node's announcement | workflow -> design | transformation::WF_P7_DESIGN_INTENT_ADMISSIBILITY_V0 | GAP | S4 dependency_graph #3 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| fb.workflow::CONSTITUTION_WORKFLOW_V0 | Governs the act and does not use the word announcement, so what a terminal node states is carried by implementation alone. | EXTEND | S4 gap_register GAP-1 |
| fb.event::CONSTITUTION_EVENT_V0 | Declares a moment and the immutability of its record, and says nothing about how many an act may announce. | REVIEW | S4 dependency_graph #2 |
| fb.event::INVARIANT_EV_APPEND_ONLY_V0 | Refuses a moment's record being altered once written, which is why an announced moment cannot be unannounced. | REUSE | S4 constraint_register #7 |
| fb.event::INVARIANT_EV_SCHEMA_REQUIRED_V0 | Requires a moment to declare its shape, and does not count announcements. | REVIEW | S4 capability_graph #7 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_DECLARED_MOMENT_IS_ANNOUNCED | Every declared moment an act completes is announced by that act. The business declared it matters; one never announced is a fact the business asked to see and cannot. | S4 constraint_register #4 |
| THE_STATED_ORDER_IS_THE_ORDER | Several moments are announced in the order the design states. Every serialization is ordered incidentally, so only a declaration makes the order something a reader may rely on. | S4 constraint_register #1 |
| ONE_MOMENT_ONE_RECORD | Each moment announced has its own evidence record, whether the act announced one moment or several. A record naming several turns a per-moment question into a substring question. | S4 constraint_register #2 |
| A_MOMENT_IS_ANNOUNCED_ONCE | An act announces each moment at most once. Twice from one act says it occurred twice, and a reader counting occurrences would be right to conclude something happened that did not. | S4 constraint_register #3 |
| SILENCE_IS_REFUSED | An announcement that cannot be made is reported. The act's work is done and its records are immutable, so the choice is loud or silent, and silence is the defect this change removes. | S4 constraint_register #7 |
| THE_ACT_IS_NOT_RESHAPED_TO_FIT | An act is never split, and no moment dropped, to fit the announcement mechanism. That changes the business to suit the platform. | S4 constraint_register #5 |
| WHAT_THE_PLATFORM_DOES_IS_STATED | A behaviour the platform performs is governed by a document that states it, or it is ungoverned rather than leniently governed. | S4 constraint_register #8 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Stating what a terminal node announces | workflow | S4 gap_register GAP-1 |
| Declaring the order normative | workflow | S4 gap_register GAP-2 |
| Announcing an ordered sequence at one ending | workflow | S4 gap_register GAP-3 |
| Reporting an announcement that cannot be made | workflow | S4 gap_register GAP-4 |
| Refusing a moment announced twice | workflow | S4 gap_register GAP-5 |
| Asserting what an act announced | workflow | S4 gap_register GAP-6 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, scope, invariants, actions | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
