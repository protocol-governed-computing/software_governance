# Stage 3 — Analysis Loop: platform / runtime_binding
**Stage:** 3 — Analysis Loop
**CR:** multi_structure_binding
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here. Every finding was re-grounded against the pinned
snapshot and the act that fails rather than inherited.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The five gaps are two problems, not five. Four are one problem seen from four sides — an act reaches one description, so the reach cannot be stated, cannot be reviewed and cannot be scoped. The fifth, that nothing detects one record described twice, is separate: it is the check that the first problem is not solved by copying. | Fixes what the change must deliver and rules out delivering the reach without the check that keeps it honest. | OBSERVED | HIGH | CLOSED | Four gaps trace to one storage description per act; the fifth traces to nothing comparing two descriptions. |
| Q2 | The reach is stated by the act, not by the owner. The act is the only party that knows it reads elsewhere; the owner would otherwise maintain a list of readers that nothing keeps in step with the readers themselves. | Places the declaration with the party that has the knowledge. | OBSERVED | HIGH | CLOSED | Nothing in the composition holds a list of who reads a subdomain's records, and no artifact names its readers. |
| Q3 | Widening what a binding names and widening what an act names are different changes with different owners. Widening the binding puts one subdomain's storage inside another's artifact; widening the act leaves every description with the subdomain that wrote it. The business ruled the second. | Decides which declaration the change amends, and why it is not the smaller one. | OBSERVED | HIGH | CLOSED | Every binding in the composition is owned by one subdomain and names that subdomain's description. |
| Q4 | Reading and writing are already distinguishable, so the read-only half of this change is enforcement rather than invention. What does not exist is the statement of which places an act owns and which it merely consults. | Removes an obligation the problem statement carried and isolates the one that remains. | OBSERVED | HIGH | CLOSED | Twenty-one operations declare an effect; no artifact declares owned against consulted. |
| Q5 | One record described twice must be refused where descriptions meet, which is assembly. No phase rule can see it: a design states its own subdomain's storage and never another's, so two designs each stating one description are each correct alone. | Places one obligation outside the design layer, deliberately. | OBSERVED | HIGH | CLOSED | Assembly already compares copies of one identity across domains and refuses when they disagree; no phase register carries a second subdomain's records. |
| Q6 | The act that fails passes every check before it. A change that only widens the declaration would leave the same class of defect arriving the same way — admissible, compiled, attested, and refused when it runs. Making the reach visible in the design is therefore part of the fix, not a convenience. | Prevents delivering the mechanism without the visibility the change set out to gain. | OBSERVED | HIGH | CLOSED | The wallet act is admissible at every phase, compiles, verifies, attests, and stops on its second step. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| An act reaches one place where storage is described, and every capability it performs resolves against that one place. | S2 belief_verification #1 | CONFIRMED | Re-read: every binding in the composition names one description, and the compiler seals the one it finds. |
| An act that reuses a capability owned by another subdomain stops when it runs, because the records that capability reads are described somewhere the act cannot reach. | S2 belief_verification #2 | CONFIRMED | Re-run: the act stops on its second step, naming the records it could not find. |
| Nothing governing states that an act resolves its records against one description, or why it should. | S2 belief_verification #3 | CONFIRMED | Re-read: the governing constitution and its four invariants mention where storage is described in no form. |
| The composition can tell a reading operation from a writing one. | S2 belief_verification #4 | CONFIRMED | Re-read: every operation declares an effect, and a reach to a writing contract across a boundary is refused. |
| Assembly already refuses a composition where two copies of one thing disagree, rather than answering from whichever it resolved. | S2 belief_verification #5 | CONFIRMED | Re-read: copies of one identity are compared and the composition is refused when they differ. |
| The design language can say which capability an act reuses and where the act's own records live, and cannot say that the act also reads what another subdomain holds. | S2 belief_verification #6 | CONFIRMED | Re-read: no design register carries a second subdomain's storage. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| A statement, on an act, of the bindings it operates under | declaration | AUTHOR_NEW | An act names one binding and nothing carries more. |
| A statement of which named places an act owns and which it consults | declaration | AUTHOR_NEW | Nothing declares the distinction in any form. |
| A governing statement of how an act resolves its records | declaration | AUTHOR_NEW | No constitution and no invariant says anything about it. |
| The rule that a record is described exactly once | declaration | AUTHOR_NEW | Stated by this change and checked by nothing today. |
| A binding, owned by the subdomain that wrote it | mechanism | REUSE | Every subdomain already has one, correct and maintained. |
| The declaration that an operation reads or writes | mechanism | REUSE | Delivered and enforced; the read-only rule already rests on it. |
| The refusal of a reach that would write across a boundary | mechanism | EXTEND | Holds a design today; must hold what an act reaches at run time too. |
| The comparison that refuses a composition where copies disagree | mechanism | EXTEND | Compares copies of one identity; must also compare descriptions of one record. |
| The design register that states where an act's records live | mechanism | EXTEND | States one subdomain's storage; must carry the reach and its kind. |
| The resolution of an act's binding when it is compiled | mechanism | EXTEND | Looks up one description and seals it; must compose several. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0 | States the resolution model for the first time: what an act reaches, whose description is authoritative, and what happens when two disagree. | 7 | Seven bindings are governed by it across five domains. |
| blockchain::RB_WALLET_BINDINGS_V0 | The act it binds gains a second binding to read from, and keeps describing only wallet records. | 1 | One act operates under it. |
| blockchain::RB_IDENTITY_BINDINGS_V0 | Unchanged, and reached by an act that does not own it. | 3 | Three identity acts operate under it. |
| blockchain::WF_CREATE_WALLET_V0 | Names the bindings it operates under, and completes rather than stopping at its second step. | 0 | Nothing in the composition invokes it; it is invoked from outside. |
| Every existing act | Each names one binding today and must be readable as naming one it owns. | 7 | Seven bindings, each named by the acts of its own subdomain. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Naming, on an act, the bindings it operates under | AUTHOR_NEW | An act reaches one description today, and the reach is the thing this change exists to make sayable. | Naming several descriptions on one binding was rejected by the business: it puts one subdomain's storage inside another's artifact. Resolving a reused capability silently against its owner's binding was rejected earlier: it declares nothing, so nothing can be reviewed or scoped. | S2 gaps #1 |
| Stating which named places an act owns and which it consults | AUTHOR_NEW | A read-only reach cannot be held without it, because nothing could tell which place a write was aimed at. | Inferring ownership from which subdomain wrote the binding was rejected: it makes the permission depend on a fact the act never states, which is how the reach became invisible in the first place. | S2 gaps #4 |
| Stating how an act resolves its records | AUTHOR_NEW | Nothing says it today, so there is no rule to widen and the model must be stated. | Amending the field's declared shape alone was rejected: it would widen what can be written without saying what any of it means. | S2 gaps #3 |
| Refusing a composition where two subdomains describe one record | EXTEND | The comparison exists one level up and refuses rather than preferring; this is the same judgement over descriptions rather than copies. | A precedence rule was rejected by the business: it makes the answer depend on the order somebody wrote a list in. Checking it in a phase was rejected: a design states its own storage only, so two contesting designs are each correct alone. | S2 gaps #5 |
| Making the reach visible in the design | EXTEND | The register that states where an act's records live is the one place a reviewer already looks. | A separate declaration of reach was rejected: two statements about one act's storage can disagree. | S2 gaps #2 |
| Refusing a reach that would change what it does not own | EXTEND | The rule holds a design today and must hold an act when it runs, because the design layer cannot see what a caller does. | Re-deriving the effect at run time was rejected: it is declared, and re-deriving a declared fact is how two answers appear. | S2 belief_verification #4 |
| Telling a reading operation from a writing one | REUSE | Delivered and enforced, with every operation declaring it. | Nothing to check — this was the third obligation and it is met. | S2 architectural_observations #3 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | runtime_binding | Where an act finds its records is what this subdomain governs; the change states the model it has been operating without. | S2 belief_verification #3 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All five are resolved: four by authoring what does not exist, one by extending a comparison that already refuses. |
| No open analyst questions | SATISFIED | Stage 2 carried none, and the six raised here are closed. |
| No dependency expansion in the last pass | SATISFIED | Ten dependencies established in one pass; re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Six items re-grounded; all six CONFIRMED. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. None rests on inference. |
