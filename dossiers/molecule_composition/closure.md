# Closure — molecule_composition

**Phases reached:** P0 – P6, every one admissible
**Status:** COMPLETE. P6 is this dossier's terminal phase, by ruling
**Delivery:** authored, by a person, under this dossier, in the order `delivery_plan.md` states
**Gate 1:** CLOSED at P6 by the business author, against composition `1b0cfbd3d094…`
**Unblocks:** the conformance workload's molecule change, and `cr_01_model_response`, paused before P7

---

## Why P6 is terminal

The governance surface is authored, not constructed. This change adds two constitutions and the
invariants that hold transforms to them, and neither a constitution nor an invariant is an artifact the
design language can author or the renderer can build. The ruling is in
`transformation/THE_SHAPE_OF_A_CHANGE_V0.md` §7, and `AMENDED_ARTIFACT_NOT_AUTHORABLE` refuses a design
that claims otherwise.

A dossier that stops at P6 is not unrealized. What it authorizes is delivered by hand, under the
dossier, and recorded here and in `delivery.md` — the same governed decisions, carried out by the only
means that can author them.

## What the phase run established that the problem statement did not

- **The shape was declared, partly built, and never exercised.** The schema declared a molecule; the
  compiler lowered one; nothing could state, render or run one. No composition used a molecule, which
  is why nothing noticed.

- **"Every transform is pure" was right for everything that existed, and wrong as a universal.** The
  existing constitution keeps governing exactly what it governs; the rule becomes a declaration a
  transform makes, and two sibling constitutions govern what it does not describe. Superseding or
  renaming the existing one was rejected: either forces every existing transform to name its
  replacement.

- **Non-determinism needed a place in the standard, not an exception to it.** The standard requires
  that the same governed state and proposal determine the same result, and that replay reproduces it.
  Recording every non-deterministic result when produced, and substituting it on replay, keeps that true
  — determinism holds relative to recorded outcomes. The clock is the precedent: it answers differently
  every time and is recorded where it is used.

- **A non-deterministic step may propose and never decide.** Routing on its result directly would
  reduce governance to recording what the step said. So its result is consumed by a deterministic step
  before anything routes, and the composition refuses otherwise.

- **Repetition belongs in a molecule's loop, never in an act.** An act stays acyclic; a loop is bounded
  by a collection the composition can see, and runs every pass.

## What delivery looks like

Four repositories, in dependency order: the governance surface states the rules and the invariants
that hold them; the compiler lowers and refuses; the runtime runs, records and replays; the design
language states a molecule and construction renders it. **Delivering only the last would be a defect
rather than a partial fix** — a design could state a molecule the running system cannot run.

## What is deliberately left open

- **End-to-end evidence** is the conformance workload's own change, which this delivery unblocks.
- **The rename** of the deterministic-atom constitution is deferred to its next version.
- **The trace event schema** lags the events the runtime writes, and did before this change.
