# Business Problem Statement

**Project Name:** platform — capability transforms

## 1. Context

A capability transform is a unit of computation a governed act performs. Most are atoms: one
implementation, one result. The platform also declares a second shape, the **molecule**: a transform
composed of other transforms, run as a stated sequence of steps. One kind of step is a **loop**,
which runs a composed body once for each member of a stated collection and carries values from one
pass to the next.

A molecule exists so that a computation made of several decisions can be declared as those decisions,
each one visible in the composition, rather than hidden inside a single implementation. Where a
computation repeats, the loop keeps the repetition declared and bounded: it runs once per member of a
collection the composition can see, never an unstated number of times.

## 2. Problem Statement

**The platform declares composed transforms, and nothing can carry one from design to execution.**

The molecule's shape is declared: its steps, its loop, the collection a loop runs over, the values it
carries between passes, and the one value it emits. The compiler reads that declaration and lowers it.
Every other stage of the lifecycle either cannot express it or cannot run it.

- **Design cannot state one.** No register of the design language describes a molecule's steps. A
  design can name a transform, its module and its purity, and nothing about what it is composed of.
- **Construction cannot render one.** The renderer writes an atom's implementation and never a
  molecule's steps, its loop or its emission. A design naming a molecule leaves construction
  undetermined, and construction emits nothing at less than full determinacy.
- **Compilation accepts a molecule it cannot vouch for.** A loop's body is lowered as a reference to a
  molecule, with no implementation attached and nothing checking that what the loop names can be run.
- **Execution cannot run one.** The runtime dispatches every step, including each pass of a loop, as
  a single implementation. A composed body has none. Running the compiler's own loop shape fails with
  `CTExecutionError: CT-IR step missing handler_ref`, and a molecule nested inside another fails the
  same way.

**No composition has ever used one, which is why the gap was invisible.** Every transform in the
composition is an atom. The only repeated computation in it runs its whole repetition inside one atom,
where none of its decisions can be seen. The path through molecules was declared, partly built, and
never exercised end to end.

**The requirement is confirmed rather than anticipated, and one change is where it surfaced.** A
business domain needed a response written word by word, with a rule decision on every word that
governance can see: each pass offering candidate words and then choosing one under declared rules.
That is a loop whose body is two declared steps. The domain's design reached the point of stating it
and could not. The instance belongs to a domain this platform does not require; it is evidence that
the shape occurs, not the problem itself.

**The limit is not a rule anyone wrote.** The workflow constitution requires an act to be acyclic, and
that is correct: repetition does not belong in an act. The molecule is where the platform already
placed it. No constitution or invariant forbids a composed loop body. The schema declares one, and the
compiler emits one. What is missing is everything else.

Two ways of avoiding the problem were examined and rejected:

- **Put the whole repetition inside one atom.** This is what the composition does today, and it is
  the defect: every decision inside the atom is invisible to governance, and an act that must show
  its decisions cannot.
- **Unroll the repetition into the act.** An act bounded by a longest response of several hundred
  words would need several hundred copies of the same steps. The act stays acyclic, and the
  composition becomes unreadable in exactly the place it must be read.

This change shall:

- let a design state a molecule's steps, including a loop and its body, so construction renders it at
  full determinacy;
- refuse, when the composition is built, a molecule whose steps or loop body cannot be run;
- run a molecule's steps in their declared order, including a composed body once per pass of a loop;
- show, by a composed transform designed, constructed, compiled and run end to end, that the path
  holds.

### What this change does not decide

- **What any domain composes.** Each domain states its own molecules in its own change.
- **Whether a computation should be one atom or several steps.** That is each design's judgement.
- **Anything about an act's shape.** Acts stay acyclic. Repetition lives in molecules.

---

## 3. The execution path a change would take

Four repositories, in dependency order. Recorded so the scope is visible before anyone begins.

| # | Repository | What changes |
|---|---|---|
| 1 | `software_governance` | States what a molecule is and how it runs, which no constitution currently says: its steps run in declared order, a loop runs its body once per member of the stated collection, and the composition refuses a molecule it cannot run. An invariant holds a composition to it. |
| 2 | `protocol_compiler` | Checks, when the composition is built, that every molecule's steps and every loop's body resolve to something the runtime can run, and refuses otherwise. |
| 3 | `protocol_runtime` | Runs a molecule as a sequence of steps, both at the top of a transform and as a loop's body, carrying the loop's values between passes. |
| 4 | `transformation` | A design register for a molecule's steps, and the renderer that writes them, so a design can state a molecule and construction renders it. |

**Amending the runtime alone would be a defect, not a partial fix.** A molecule could then run while no
design could state it and no construction could render it. A domain needing one would have to write
it by hand, outside the path the lifecycle governs.

**The evidence must not come from the domain that found the gap.** A composed transform with a loop is
designed, constructed, compiled and run end to end as part of this change, in the platform's own
conformance evidence.

---

## 4. Clarifications — answered by the business author

- **Does a loop run for every member of its collection, or may it stop early when its work is done?**
  **Every member, every time.** A loop whose work is finished carries that fact forward in the values
  it passes between passes, and the passes that remain do nothing. The number of passes is the size
  of the stated collection, fixed and visible; a loop that stopped early would make its own length
  depend on the data it computes, which is the unbounded repetition the loop exists to prevent.

- **May a molecule contain other molecules to any depth, and may a loop's body itself contain a loop?**
  **Yes, to any depth, provided no molecule contains itself, directly or through others.** A molecule
  that contains itself is repetition with no stated bound, and it is refused when the composition is
  built.

- **Is a molecule's purity declared, derived from its steps, or both?**
  **Declared, and checked against its steps.** A molecule declared pure is refused when any of its
  steps is not. The declaration is what a reader relies on to see where determinism ends; the check
  is what makes the declaration true.

- **Does each step a molecule runs leave its own evidence, or does the molecule leave one record for
  the whole?**
  **Each step leaves its own record,** holding the names of its results and not their values, as
  every other step's evidence does. A decision made inside a molecule is then observable when it is
  made, not only declared in the composition. The cost is volume: a loop of many passes leaves a
  record per step per pass.
