# Closure — transform_conformance

**Phases reached:** P0 – P6, every one admissible
**Status:** COMPLETE. P6 is this dossier's terminal phase, by ruling
**Delivery:** authored, by a person, under this dossier, in the order `delivery_plan.md` states
**Gate 1:** CLOSED at P6 by the business author, against composition `54412f835e6d…`
**Unblocks:** the conformance workload's declared-iteration change

---

## Why P6 is terminal

This change amends the governance surface: a constitution, its invariants and a schema. Neither a
constitution nor an invariant is an artifact the design language can author or the renderer can
build. The ruling is in `transformation/THE_SHAPE_OF_A_CHANGE_V0.md` §7. What this dossier authorized
was delivered by hand, under the dossier, and is recorded here and in `delivery.md`.

## What the phase run established that the problem statement did not

- **The dormancy was half a decision.** Taking conformance out of the platform's build was sound,
  because a transform's implementation belongs to the domain that supplies it. The other half, a domain
  build that runs conformance, was never carried out. So the rules over vectors passed on nothing,
  and reported the same result as rules that had judged everything.

- **Proving only on first release was rejected.** Grandfathering a proof needs a record of what was
  proven and when: a fingerprint, and the bookkeeping to keep it. A re-run needs neither, and it
  catches exactly the drift the dormancy let through. So every build runs every vector.

- **A molecule's non-determinism is proven the way replay works.** A case supplies the recorded result
  of each non-deterministic step. The runner substitutes it and confirms the step never ran. A bespoke
  replay test per molecule is the hand-written proof this change replaces.

- **Unproven is a result, not a failure.** Refusing every domain whose transforms have no vectors
  would have stopped every build today. Instead, the result names each unproven transform, so a
  reader sees what was not judged, and nothing is reported as passing over nothing.

- **The design is where a new transform can be told from an existing one.** A build cannot know
  when a transform was authored. A design does: it declares a transform new or amended. That is why
  the requirement to supply vectors is a P7 rule and not a build check.

- **What a domain proved belongs to the composition.** Its result is written before assembly and
  follows from the declarations alone, so it sits inside the snapshot's identity. Excluding it would
  be a carve-out the identity's totality refuses.

## What delivery looks like

Six repositories, in dependency order:

1. the governance surface states what a vector is;
2. the compiler reads and refuses;
3. the runtime proves;
4. the build step runs the runtime after a successful compile;
5. the assembler carries the result;
6. the design language states vectors, and construction renders them.

**Delivering the runner without the build step would be a defect rather than a partial fix.** A
runner that nothing invokes is the dormancy this change removes.

## What is deliberately left open

- **The first proven transforms and the first proven molecule** belong to the conformance workload's
  own change.
- **Carried platform transforms** are named in every domain that carries them and proven in none.
- **The implementation's source is not sealed by content**, so a vector proves the code that ran at
  build time and nothing after it.
- **P7 resolves a value's case per register, not per transform**, and cell normalization reaches values.
