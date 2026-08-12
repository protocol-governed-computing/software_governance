# Business Problem Statement

**Project Name:** platform — workflow execution

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed business
> requirement and the execution path a change would take. It is not a design.

## 1. Context

A governed act announces the moments the business declared matter. An act ends at a terminal node,
and that node names the moment it announces.

One act may complete more than one business moment. Registering a book registers three things at
once: the work the library now carries, the first edition of it, and the first physical copy on the
shelf. Each is a moment the business declared. The act completes all three.

---

## 2. Problem Statement

**An act can announce one moment. Some acts complete several.**

A terminal node names a single moment, and the running system resolves a single moment for a given
act and outcome. An act completing three declared moments can announce one of them, and the business
has no way to say which two go unannounced — because it never agreed that any should.

**The requirement is confirmed, not hypothetical.** `book_library_mgmt::WF_REGISTER_BOOK_V0`
registers a work, its first edition, and that edition's first physical copy. Three of the catalog's
six declared moments name exactly those things. The act completes all three and can announce one.

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
- **Split the act into three.** Registering a book is one thing the library does. Splitting it to fit
  a limitation of the announcement mechanism would change the business to suit the platform.

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

## 4. Clarifications for the business author

> **These are unanswered.** No phase may proceed on a guess about them.

- **What determines the order in which several moments are announced?** The order the design states,
  or something derived from the act?
- **If one announcement of several cannot be made, is the act refused, or are the others still
  announced?**
- **Is each moment its own evidence record, or one record naming several moments?** The requirement
  says one record per moment; this asks whether the business agrees that is what it wants observed.
- **May an act announce the same moment more than once?**
- **Does anything today rely on exactly one moment per act and outcome** — a reader, a report, a
  count?
