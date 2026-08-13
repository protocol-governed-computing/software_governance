# Closure — select_operation

**Phases reached:** P0 – P6, every one admissible
**Status:** COMPLETE. P6 is this dossier's terminal phase, by ruling
**Delivery:** already delivered. This dossier is the record that was missing
**Subject:** `SELECT` on `capability_side_effects::CS_MUTABLE_JSON_V0`

---

## What this dossier is

A capability gained an operation and no dossier recorded it. The operation is right, declared as a
read, reached by two catalog contracts and running — so there was nothing to deliver and nothing to
undo. What was missing was the reason, and the reason was written down in another domain's change
request.

It is complete at P6 for the same reason every governance-surface change is: the governance surface
is authored, not constructed, and the pipeline's authority over such a change ends there. The ruling
is in `transformation/doc/THE_SHAPE_OF_A_CHANGE_V0.md` §7.

## What it records

- **The operation's reason belongs to the capability.** *Read every record in storage, for a caller
  that selects among them by content* — needed because a search must see the records rather than the
  keys they are filed under. Every domain reads the capability; only one reads the catalog's change
  request.
- **The operation is general, not a favour to one caller.** Two contracts reach it for different
  questions: which records match, and which copies are held of a book.
- **The change crossed an authority boundary, and it was declared rather than hidden.** The catalog's
  change request said in its own registers that it was extending the capability, and every check
  passed because none of them asked whether a domain may amend a platform capability.

## Why it matters that the crossing was unenforced rather than broken

`AMENDED_ARTIFACT_NOT_AUTHORABLE` dates from the session that opened this dossier. Before it, a
design could claim to amend anything that resolved, and the platform's rule that a domain never
modifies a platform artifact was doctrine nothing could fail. So this is not a violation to be
answered for — it is the first instance of a boundary, recorded so that the rule now refusing it has
something to point at.

The maintained fixture for the catalog's change request carries `REVIEW` where the approved original
carries `EXTEND`. The original stays as approved: it records a change that crossed an authority
boundary before the boundary was stated, which is worth keeping visible rather than editing away.

## What is deliberately left open

Nothing distinguishes an operation the platform decided from one a caller needed. This dossier
records one instance; whether an offer should carry its provenance in general is a question for a
change that means to answer it, and P5 defers it explicitly.
