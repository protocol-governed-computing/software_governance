# Business Problem Statement

**Project Name:** platform — workflow execution

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed business
> requirement and the execution path a change would take. It is not a design.

## 1. Context

A governed act announces the moments the business declared matter. An act ends at a terminal node,
and that node names the moment it announces.

One act may complete more than one business moment, and this is ordinary rather than exotic. Wherever
a business does one thing that establishes several — a party admitted and its first agreement recorded,
a resource created and its first allocation made, a thing catalogued and the first instance of it
placed — the act is one and the moments are several. Each is a moment the business declared, and the
act completes all of them.

---

## 2. Problem Statement

**An act can announce one moment. Some acts complete several.**

A terminal node names a single moment, and the running system resolves a single moment for a given
act and outcome. An act completing three declared moments can announce one of them, and the business
has no way to say which two go unannounced — because it never agreed that any should.

**The requirement is confirmed rather than anticipated, and one composition is where it surfaced.**
The instance belongs to a business domain this platform does not require and a later composition may
not contain; it is evidence that the shape occurs, not the problem itself. In that composition, one
act registers a work, its first edition, and that edition's first physical copy. Three of the
domain's six declared moments name exactly those things. The act completes all three and can
announce one.

**And the limit is not a rule anyone wrote.** No constitution mentions a terminal node's
announcement — not the workflow constitution, which does not use the word, and not the event
constitution, which speaks only of records being immutable once written. No invariant covers it. The
whole of the model is two lines of implementation: the compiler reads a single name off a terminal
node when it builds the dispatch table, and the running system fires the one moment that name
resolves to.

So this change does not relax a rule. **It states the model for the first time**, and states it as an
ordered several of which today's behaviour is the case of one. A behaviour the platform performs and
no document governs is not a lenient rule; it is an ungoverned one, and the first act here is to
write it down.

Two ways of avoiding the problem were examined and rejected:

- **Announce only one and leave the others silent.** The business declared all six; a declared moment
  that is never announced is the defect this was found while fixing.
- **Split the act into several.** An act completing three moments is one thing the business does.
  Splitting it to fit a limitation of the announcement mechanism would change the business to suit
  the platform.

This change shall:

- let one terminal node announce more than one declared moment;
- announce them in a stated order, the same order every time;
- produce one distinct evidence record per moment announced, so a moment announced is a moment
  observable.

### What this change does not decide

- **Which moments any act announces.** That is each domain's business, stated in its own change.
- **Whether an act should complete several moments.** Some do. This change follows that fact rather
  than judging it.
- **Anything about the lifecycle that governs change.** This is a platform capability, distinct from
  the three lifecycle dossiers.

---

## 3. The execution path a change would take

Four repositories, in dependency order. Recorded so the scope is visible before anyone begins.

| # | Repository | What changes |
|---|---|---|
| 1 | `software_governance` | Declares the emission model, which no constitution currently states: a terminal node announces an ordered sequence of moments, and the order is normative. An invariant holds a composition to it, because a guarantee nothing checks is a sentence. |
| 2 | `protocol_compiler` | The dispatch projection that maps an act and outcome to a moment. Today it carries one; it must carry an ordered several, and seal that order. |
| 3 | `protocol_runtime` | The scheduler resolves a single moment per act and outcome (`scheduler.py:131`) and must announce each in the sealed order, emitting one evidence record per moment. |
| 4 | `transformation` | The design language and the renderer that writes a terminal node's announcement, so a design can state several and construction renders them. |

**Amending only the fourth would be a defect, not a partial fix.** A design could declare three
announcements while the running system fires one, silently — the same class of failure as a field
that is declared and read by nothing.

**One thing the first repository must settle before the fourth can be designed: what an announcement
attaches to.** There are two spellings of it already. A design states the announcement against the
terminal node it belongs to; the compiler re-keys it to the transition that reaches that node — the
act, the step, and the outcome the step produced — because a terminal node carries no address of its
own. The running system fires on the transition. Declaring several announcements against one spelling
while the platform keys them by the other is how a design would come to declare something the
composition cannot carry, so the model names one of them and the rest follow it.

---

## 4. Clarifications — answered

All five are answered. Four by the business author; the fifth was raised for the author and turned
out to be answerable from the composition, so it is answered by looking rather than by asking.

### Answered by the business author

- **What determines the order in which several moments are announced?**
  **The order the design states, and the model declares that order normative.** There is nothing else
  to derive it from: the moments of one act are announced at one terminal node, with no path between
  them, no dependency to sort by and no step boundary separating them. Every derivation available
  falls back on an incidental — the alphabetical order of codes, the order rows sit in a register,
  the order a renderer walks a map — and each makes a business statement depend on something nobody
  decided.

  The composition already orders declarations this way: a capability contract's steps run in the
  order they are authored, and so does a molecule's stream of atoms. What must be *said*, and is the
  substance of this answer, is that the order **carries meaning**. Every serialization is ordered
  incidentally; a declaration that the order is normative is what lets a reader of the trail rely on
  it, and what makes a change to the order a change to the account of what happened.

- **If one announcement of several cannot be made, is the act refused, or are the others still
  announced?**
  **The act is not refused. A moment that cannot be announced is a failure the act reports, and every
  moment already announced stands.**

  This is arithmetic about when announcement happens, not tolerance. A terminal node is reached after
  the act's work is done: the records are written, the identities claimed, the trail appended. Refusing
  the act there would claim to undo work nothing can undo, and a record is immutable once written —
  there is nothing to unannounce.

  So the choice is not *refuse or continue*; it is **fail loudly or fail silently**, and silence is
  the defect this change exists to remove. The act reports that it could not complete its account of
  what happened, and the moments it did announce remain announced, because they are true.

  **Rejected: announce nothing unless all can be announced.** The platform has no two-phase anything,
  and a commit phase fails in the middle exactly as this does — it moves the problem. It would also
  erase moments that genuinely occurred, which is a worse falsehood than an incomplete account.

- **Is each moment its own evidence record, or one record naming several moments?**
  **One record per moment.** The trail holds one entry per event and every reader of it asks a
  per-moment question — *was this announced?* A record naming three moments turns that into a
  substring question, and a count of moments into a count of records that is no longer the same
  number.

  It also keeps a moment's evidence the same shape whether the act announced one moment or three. An
  act that grows from one moment to two must not change the evidence for the moment it already had,
  which a composite record would do and which every existing reader would then be wrong about.

- **May an act announce the same moment more than once?**
  **No. A terminal node names each moment at most once, and a repeat is refused when the composition
  is built.** Announcing one moment twice from one act says it occurred twice; for a single act that
  is false, and a reader counting occurrences would rightly conclude something happened that did not.

  The apparent exception is a different question. An act completing several instances of the same
  *kind* of moment — three copies shelved — is completing several moments about different subjects,
  and how an act announces a moment per member of a collection is a shape this change does not need
  and must not smuggle in.

  Refusing at build time rather than at run time follows the composition's existing treatment of a
  declaration that says one thing about a subject: reading the first, reading the last and refusing
  are three different behaviours, and only refusing is declared.

### Answered from the composition

- **Does anything today rely on exactly one moment per act and outcome — a reader, a report, a
  count?**
  **Almost nothing, and nothing that would break loudly.** The singular is where §2 says it is: the
  compiler reads one name off a terminal node and re-keys it to the transition, and the scheduler
  performs one lookup and one write. The evidence writer is already per-moment — it records one entry
  per call.

  What does *not* rely on it is the more useful half. **No invariant counts events**; the two that
  govern them require append-only writing and a declared schema. **No inspection operation reads
  emitted moments at all.** **No egress declaration enumerates the moments an act emits.** And the
  occurrence counts in the domain validations count *records written by capability steps*, not
  announced moments — a distinction easy to get wrong, and the reason those counts are unaffected by
  this change.

  **One reader must be tightened as part of the change.** The reference workload's test takes the
  first announced moment it finds and asserts its identity. It would accept extra moments without
  noticing, which is the one place several would arrive silently. It should assert the moments and
  their order.
