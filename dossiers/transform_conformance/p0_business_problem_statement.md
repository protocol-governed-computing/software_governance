# Business Problem Statement

**Project Name:** platform — transform conformance

## 1. Context

A capability transform is a unit of computation a governed act performs. Its declaration says what it
takes and what it yields; its implementation is code that lives outside the composition, reached
through the path the declaration names. The composition vouches for the declaration. Nothing in it
can vouch for the code.

**Conformance** is how the platform closes that gap. A transform is given **test vectors**: stated
inputs and the outputs it must produce from them. When the composition is built, each vector is run
against the transform exactly as the composition sealed it, and a transform that does not produce what
its vectors say is refused. The vectors are declarations like any other, so what a transform was
proven to do is part of the composition a reader can inspect, not a claim in a test file somewhere
else.

The platform governs this. A constitution states what a vector is, three invariants hold vectors to
the transforms they test, the compiler turns vectors into runnable cases, and the runtime carries the
runner that executes them.

## 2. Problem Statement

**The platform governs transform conformance, and no transform in the composition has been proven by
it.**

The reference implementation this platform was derived from ran conformance on every build and failed
the build on any vector that failed. When the platform was narrowed to its normative surface,
conformance was deliberately taken out of the platform's own build, for a sound reason: a transform's
implementation belongs to the domain that supplies it, so conformance against it belongs in that
domain's build. The platform's build manifest records the decision and says so.

The second half of that decision was never carried out.

- **No domain runs conformance.** No domain's build declares where its vectors are read from or where
  its runnable cases are written, and no build step invokes the runner.
- **No transform has a vector.** The vectors the reference implementation carried were not brought
  across when its domains were rebuilt through the governed design path, and they could not have been:
  **the design language has no way to state a vector**, so no design could author one and no
  construction could render one.
- **The rules over vectors pass on nothing.** The three invariants governing vectors are checked on
  every build, find none, and report success. A rule that has never had anything to judge reports the
  same result as a rule that judged everything and found it sound. That is the failure this platform
  exists to refuse.
- **The runner and the composition's own evidence have collided.** The runner reads its cases from a
  place in the snapshot that composition conformance now uses for a different kind of evidence. Were
  the runner invoked today, it would read the wrong thing.

**The gap now matters more than it did.** Transforms are no longer only single implementations. A
molecule is composed of other transforms, and may contain a step whose result is not determined by its
inputs — whose every result is recorded, and replayed from the record. Those are the transforms whose
behaviour is hardest to see from outside, and the platform has no way to prove any of it outside a
bespoke test written for one example. What a molecule does, and that a replay substitutes what was
recorded rather than running the step again, should be proven for every molecule any domain composes,
the same way, as part of the composition.

Two ways of avoiding the problem were examined and rejected:

- **Keep proving transforms in hand-written tests beside the code.** That is how every transform is
  tested today where it is tested at all. The proof is outside the composition, a reader of the
  composition cannot see it, and a transform can enter a composition with no proof and nothing notices.
- **Restore conformance to the platform's own build.** That reverses a correct decision. The platform
  does not own a domain's implementations and cannot vouch for them; the domain can, in its own build.

This change shall:

- let a design state test vectors for the transforms it authors, so construction renders them as
  declarations like any other artifact;
- run every transform's vectors in the build of the domain that supplies it, against the transform as
  the composition sealed it, and refuse the domain if any vector fails;
- prove a molecule by its vectors, run whole, as the composition sealed it;
- prove a molecule containing a step that is not deterministic by supplying, in the vector, the
  results that step is recorded as having produced — so the expected result is exact, and the vector
  also proves that a replay uses the record and does not run the step;
- refuse to report a transform as proven when nothing proved it;
- separate the runner's cases from the composition's own conformance evidence.

### What this change does not decide

- **What any transform does.** Each domain states its transforms and their vectors in its own change.
- **The vectors for transforms that already exist.** Each is named as unproven until a change gives it
  vectors; none is written here on behalf of a domain.
- **How much proof is enough.** At least one vector per transform is a floor, not a standard of
  sufficiency, and each design judges the rest.

---

## 3. The execution path a change would take

Six repositories, in dependency order. Recorded so the scope is visible before anyone begins.

| # | Repository | What changes |
|---|---|---|
| 1 | `software_governance` | A new version of the constitution governing test vectors. It states that a vector tests a transform as sealed, that a molecule is tested whole, that a vector supplies the recorded results of any step that is not deterministic, and that a transform no vector tests is unproven rather than passing. An invariant refuses a vector that supplies recorded results for a step that is deterministic, or omits them for one that is not. |
| 2 | `protocol_compiler` | Turns a vector for a molecule into a runnable case carrying its recorded results, and writes a domain's cases where its build declares. |
| 3 | `protocol_runtime` | The runner substitutes a vector's recorded results for steps that are not deterministic, confirms none was run, and reads its cases from a place of their own. |
| 4 | `snapshot_assembler` | Carries each domain's conformance result into the composition as evidence, apart from composition conformance, naming every transform proven and every transform unproven. |
| 5 | `transformation` | A design register for test vectors, and the renderer that writes them; a domain's generated build manifest declares where its vectors are read and its cases written. |
| 6 | `.github` | The regression runs each domain's conformance and fails on any failed vector. |

**Amending the runner alone would be a defect, not a partial fix.** Conformance would run, find no
vectors, and pass — which is what happens now, one step later.

**The evidence must not come from a domain that needs it.** A molecule with a step that is not
deterministic is proven by vectors as part of this change, in the platform's own conformance evidence.

---

## 4. Clarifications — answered by the business author

- **Is a domain refused when one of its transforms has no vector, or is it reported?**
  **Reported by name, never counted as passing,** for every transform that exists when this change
  lands. A transform a change authors or amends after it is refused without a vector. Refusing every
  existing transform at once would stop every domain until each ran a change it did not ask for; passing
  them silently is the defect this change removes.

- **What does a vector for a step that is not deterministic, run on its own, assert?**
  **The shape of what it yields, never its values.** The runner already supports asserting a field's
  form rather than its content. The values are proven where the step is used: in the molecule that
  consumes it, with its results supplied as recorded.

- **Does a failed vector stop the domain's build, or only the composition?**
  **The domain's build.** A domain whose transform does not do what it says is not admitted to any
  composition; the composition never sees it.

- **Where are a domain's vectors authored?**
  **In the design, like every other declaration.** A vector written by hand beside the code is proof
  nobody gated.
