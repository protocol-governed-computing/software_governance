# Closure — multi_emission

**Phases reached:** P0 – P6, every one admissible
**Status:** COMPLETE. P6 is this dossier's terminal phase, by ruling
**Delivery:** authored, by a person, under this dossier
**Gate 1:** CLOSED at P6 by the business author, against composition `dd8da7a04010…`
**Unblocks:** `cr_03_catalog`, halted at P2, and the six declared moments announced by nothing

---

## Why P6 is terminal

The governance surface is authored, not constructed. This change states what a terminal node
announces — a clause in the constitution that governs acts, and the rules that hold it — and neither
a constitution nor an invariant is an artifact the design language can author or the renderer can
build. The ruling is in `transformation/doc/THE_SHAPE_OF_A_CHANGE_V0.md` §7, and
`AMENDED_ARTIFACT_NOT_AUTHORABLE` refuses a design that claims otherwise.

## What the phase run established that the problem statement did not

- **The singular is one announcement per *transition*, not per act.** Twelve announcements exist
  across nine acts, and four acts already announce different moments on different endings. Plurality
  is not foreign to the model; what widens is the shape one transition carries. That makes this a
  smaller change than it reads, and it means every act announcing today keeps announcing exactly what
  it does — a sequence of one is the case that already runs.

- **The cost is already being paid, and paid as silence.** One subdomain declares six moments and
  carries **zero** announcements, against twelve elsewhere in the composition. Faced with announcing
  one of three, its design announced none. That is a stronger argument for the change than the
  original statement made: the limitation is not producing wrong accounts, it is producing no account
  at all, and no check anywhere notices.

- **Nothing in the composition counts announcements.** No invariant, no inspection operation, no
  boundary declaration. The occurrence counts in the domain validations read store records written by
  capability steps, not announced moments — a distinction easy to get wrong, and the reason those
  counts are unaffected.

- **One reader would accept several without noticing.** The reference workload's test takes the first
  announcement it finds and asserts its identity. It is the single place where several would arrive
  silently, which is this change's own failure mode. Tightening it is in scope, at GAP-6.

## What delivery looks like

Four repositories, and the order is the dependency order recorded at P0 §3: the constitution states
the model and an invariant holds it; the compiler seals an ordered sequence per transition rather
than a name; the running system announces each in the sealed order; the design language states
several and construction renders them.

**Amending only the last would be a defect rather than a partial fix** — a design could declare three
announcements while the running system fires one, silently, which is the same class of failure as a
field declared and read by nothing.

## What is deliberately left open

- **A moment announced per member of a collection.** An act completing several instances of one kind
  of moment is a different shape; this change admits a known few, named when the act is designed.
- **Whether a declared moment announced by nothing should be refused.** One subdomain has six. The
  change makes announcing them possible; whether the composition should refuse a moment nobody
  announces is its own question, and answering it here would refuse six moments that are correct
  today for a reason this change did not settle.
