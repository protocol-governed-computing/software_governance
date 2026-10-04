# Stage 4 — Business Model: platform / runtime_binding
**Stage:** 4 — Business Model
**CR:** multi_structure_binding
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3, not re-litigation. Every row projects from a finding already made.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Act | Names the bindings it operates under and states which of them it owns. | Declaring — it is the only party that knows it reads elsewhere. | S1 business_vocabulary #1 |
| Subdomain | Describes where its own records live, and is the only writer of them. | Owning — answerable for the records it holds. | S1 business_vocabulary #2 |
| Assembly | Puts the composition together and refuses one where two subdomains describe one record. | Refusing — the only place two descriptions meet. | S3 analysis_findings Q5 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Binding | What connects an act to the storage descriptions it works against. | One per subdomain, and an act names exactly one. | S2 entities #4 |
| Storage description | A subdomain's statement of where its own records live. | One per subdomain, naming the records it holds. | S2 entities #3 |
| Reach | An act reading records another subdomain owns. | Nothing holds one. There is nowhere to state it. | S2 entities #5 |
| Contested description | One record described by two subdomains. | Nothing holds one, and nothing detects one. | S2 entities #7 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The seven existing bindings | Each names one description today and must be readable as one the act owns. | S3 impact_analysis #5 |
| The act that fails | The confirmed case, which completes when the reach exists and stops on its second step until then. | S3 impact_analysis #4 |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| A composition was refused for a contested description | Assembly finds one record described by two subdomains | The rule that every record is described once held, and held before anything ran. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Act | names | Binding | Naming, on an act, the bindings it operates under. | S3 authoring_decisions #1 |
| Act | distinguishes | Reach | Stating which named places an act owns and which it consults. | S3 authoring_decisions #2 |
| Subdomain | describes | Storage description | Stating how an act resolves its records. | S3 authoring_decisions #3 |
| Assembly | refuses | Contested description | Refusing a composition where two subdomains describe one record. | S3 authoring_decisions #4 |
| Design | shows | Reach | Making the reach visible in the design. | S3 authoring_decisions #5 |
| Act | is refused by | Reach | Refusing a reach that would change what it does not own. | S3 authoring_decisions #6 |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Naming, on an act, the bindings it operates under | S3 authoring_decisions #1 | CRITICAL | GAP-1 | The reach itself; nothing else is reachable without it. |
| Stating which named places an act owns and which it consults | S3 authoring_decisions #2 | CRITICAL | GAP-2 | What a read-only reach is held to. |
| Stating how an act resolves its records | S3 authoring_decisions #3 | CRITICAL | GAP-3 | Nothing says it today, so the model is stated rather than widened. |
| Refusing a composition where two subdomains describe one record | S3 authoring_decisions #4 | CRITICAL | GAP-4 | The check that the reach is not answered by copying. |
| Making the reach visible in the design | S3 authoring_decisions #5 | CRITICAL | GAP-5 | Without it the next reach is discovered the same way this one was. |
| Refusing a reach that would change what it does not own | S3 authoring_decisions #6 | CRITICAL | GAP-6 | Holds a design today; must hold an act when it runs. |
| Telling a reading operation from a writing one | S3 authoring_decisions #7 | SATISFIED | | Delivered and enforced; every operation declares an effect. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| runtime_binding | runtime_binding | capability call | GAP | S3 analysis_findings Q1 — four of the five gaps are one problem seen from four sides. |
| runtime_binding | workflow | data read | GAP | S3 authoring_decisions #1 — the act is what names the bindings, so the declaration lands on the act. |
| runtime_binding | design | data read | GAP | S3 authoring_decisions #5 — the register that states an act's storage must carry the reach. |
| runtime_binding | structure | data read | SATISFIED | S2 pps_baseline_fqdns #5 — each subdomain's description is correct and stays where it is. |

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | A record has exactly one description, written by the subdomain that owns it. | S1 business_invariants #1 | invariant |
| 2 | The owner of a record is the only writer of it. | S1 business_invariants #2 | invariant |
| 3 | An act that reaches records it does not own reads them and never changes them. | S1 business_invariants #3 | invariant |
| 4 | An act reaches only what its own domain holds. | S1 business_invariants #4 | invariant |
| 5 | A reach is declared by the act that reaches, in an artifact that act owns. | S1 business_invariants #5 | invariant |
| 6 | An act's own records are distinguishable from those it merely consults. | S1 business_invariants #6 | invariant |
| 7 | No subdomain's artifact describes another subdomain's storage. | S1 constraints #1 | governance rule |
| 8 | The reach is declared where a reviewer reads it, not inferred from what an act happens to reuse. | S1 constraints #5 | governance rule |
| 9 | An act may not gain the ability to reach records by restating another subdomain's description as its own. | S1 constraints #6 | governance rule |
| 10 | Naming another subdomain's records is not the same act as being permitted to write to them. | S1 known_facts #4 | domain knowledge |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-1 | S3 authoring_decisions #1 | Naming, on an act, the bindings it operates under | runtime_binding | NEW |
| GAP-2 | S3 authoring_decisions #2 | Stating which named places an act owns and which it consults | runtime_binding | NEW |
| GAP-3 | S3 authoring_decisions #3 | Stating how an act resolves its records | runtime_binding | NEW |
| GAP-4 | S3 authoring_decisions #4 | Refusing a composition where two subdomains describe one record | runtime_binding | EXTEND |
| GAP-5 | S3 authoring_decisions #5 | Making the reach visible in the design | runtime_binding | EXTEND |
| GAP-6 | S3 authoring_decisions #6 | Refusing a reach that would change what it does not own | runtime_binding | EXTEND |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The act names the bindings it operates under; a binding keeps naming one description. | S3 analysis_findings Q3 | Widening the binding puts one subdomain's storage inside another's artifact; widening the act leaves every description with the subdomain that wrote it. | Rules out the smaller change, and fixes which declaration is amended. |
| 2 | The reach is stated by the act, never by the owner. | S3 analysis_findings Q2 | The act is the only party that knows it reads elsewhere, and an owner's list of readers is a second copy nothing keeps in step. | Rules out consent, and rules out a registry of readers. |
| 3 | An act says of each place it names whether it owns it or consults it. | S3 analysis_findings Q4 | A read-only reach cannot be held without it, because nothing could tell which place a write was aimed at. | Rules out inferring ownership from which subdomain wrote the binding. |
| 4 | One record described twice refuses the composition at assembly. | S3 analysis_findings Q5 | It is the only place two descriptions meet; a design states its own subdomain's storage only, so two contesting designs are each correct alone. | Places one obligation outside the design layer, and rules out a precedence rule. |
| 5 | The reach appears in the design, in the register that already states where an act's records live. | S3 analysis_findings Q6 | A change that only widened the declaration would leave the next reach discovered exactly as this one was — at execution, after everything passed. | Rules out a separate declaration of reach, which could disagree with the first. |
| 6 | The read-only rule is enforced when the act runs as well as when it is designed. | S3 authoring_decisions #6 | The design layer cannot see what a caller does; the rule holds a design today and must hold the act. | Rules out re-deriving an operation's effect, which is declared. |

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR
<!-- register:authoring_scope -->
| Capability | Gap Register Ref |
|-----------|-----------------|
| Naming, on an act, the bindings it operates under | GAP-1 |
| Stating which named places an act owns and which it consults | GAP-2 |
| Stating how an act resolves its records | GAP-3 |
| Refusing a composition where two subdomains describe one record | GAP-4 |
| Making the reach visible in the design | GAP-5 |
| Refusing a reach that would change what it does not own | GAP-6 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Deciding which acts reach which subdomains | Each domain's business, stated in its own change. |
| Declaring which readers may see which records | Access control needs its own mechanism, and no act needs it. |
| Declaring how a subdomain's ownership of a record is established | Ownership is settled by convention today and stating it is a separate problem. |
| Reaching records another domain holds | A question about what is composed together, answered there. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | COMPLETE |
