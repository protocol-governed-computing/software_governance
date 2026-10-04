# Delivery — multi_emission

**Authorized by:** Gate 1, closed at P6 against composition `dd8da7a04010…`
**Delivered:** an act may complete several moments at one ending and announces each of them, in a
declared order the composition seals and the runtime keeps
**Unblocks:** `book_library_mgmt/cr_dossiers/cr_03_catalog`, halted at P2 for exactly this

---

## What was authored

**`CONSTITUTION_WORKFLOW_V0` §2a — Announcement.** The model, stated for the first time. An
announcement is the account the business keeps of what happened; it is not how the act did it, and it
is not a record a capability step wrote. Several moments may be completed at one ending and each is
announced. The order is declared and normative — an account whose order varies between runs cannot be
compared with another. A moment is announced at most once at one transition. An announcement that
cannot be made is reported, never dropped.

**`SCHEMA_WORKFLOW_V0`** — `emit` admits a moment or an ordered, unique sequence of them.

**`INVARIANT_WF_ANNOUNCEMENT_DISTINCT_V0`**, with its compiler handler: no moment twice at one
ending, and every moment a fully-qualified identity. A repeat is easy to introduce in a sequence and
invisible afterwards — the trail is append-only, so an account saying something happened twice when
it happened once cannot be withdrawn.

**`dispatch.py`** seals `emit_map[wf][cc][outcome]` as a list, even where the author wrote one name.
The runtime therefore never has to know which form was written, and the order is fixed at seal time
rather than left to whatever a map happened to iterate.

**`scheduler.py`** announces the sealed sequence in order, and records a moment that is declared for a
transition and absent from what was sealed rather than falling silent.

**`render.py`** renders several `emit.<node>` rows — or one comma-separated cell — in document order,
and keeps a single moment as a single name.

**`test_reference_collatz.py`** asserts the whole sequence rather than taking the first announcement
it finds. That was the one place in the composition where several would have arrived silently, which
is this change's own failure mode.

---

## What the phase run established, and what delivery confirmed

**The singular was never about acts.** Twelve announcements exist across nine acts, and four already
announce different moments on different endings. What was singular is the shape one *transition*
carries. So this is a smaller change than it reads: every act announcing today announces exactly what
it announced before, because **a sequence of one is the case that already runs**. Nothing in the
corpus was rewritten, and construction still reproduces 52 of 52 artifacts with zero field
differences.

**The cost was being paid as silence.** One subdomain declares six moments and carries zero
announcements. Faced with announcing one of three, its design announced none — the limitation was not
producing wrong accounts, it was producing no account at all, and nothing anywhere noticed.

---

## What it took

**The governance closure refused the invariant, and was right to.** The invariant was authored, its
handler written and registered, and the build failed at S4 with
`ASSERT_GOVERNANCE_DECLARATION_RESOLVES_V0` — because **no constitution rule named it**. An invariant
nothing names enforces nothing, and the composition will not seal one. The fix is a rule in
`CONSTITUTION_WORKFLOW_V0`'s statement block binding `WF_ANNOUNCEMENT_DISTINCT` to it.

That is worth carrying beyond this change. It is the discharge check the *design* pipeline lacks: a
declared refusal travels nine phases as prose and arrives as nothing, because no rule asks what
carries it out. Here, one layer down, the same obligation cannot be declared without something being
bound to it — and the build stops until it is.

**Proved by tampering, not by the green.**

```
one moment announced twice   refused twice over — the invariant, and the schema's uniqueItems
two different moments        compiles; runs; the trace shows both, in the declared order
a design with two rows       renders ['…EV_WALLET_CREATED_V0', '…EV_ACTOR_ACCEPTED_V0']
a design with one row        renders the bare name; 52/52 reproduced, 0 field differences
```

---

## What is deliberately left open

**A moment announced per member of a collection.** An act completing several instances of one kind of
moment is a different shape; this change admits a known few, named when the act is designed.

**Whether a declared moment announced by nothing should be refused.** One subdomain has six. This
change makes announcing them possible; whether the composition should refuse a moment nobody
announces is its own question, and answering it here would refuse six moments that are correct today
for a reason this change did not settle.
