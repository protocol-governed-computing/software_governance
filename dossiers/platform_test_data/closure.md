# Closure — platform_test_data

**Phases reached:** P0 – P6, every one admissible
**Status:** COMPLETE. P6 is this dossier's terminal phase, by ruling
**Delivery:** authored, by a person, under this dossier, in the order `delivery_plan.md` states
**Gate 1:** CLOSED at P6 by the business author, against composition `d3e4fbf45009…`
**Unblocks:** the ai_governance change for its own inherited vectors

---

## Why P6 is terminal

This change amends the governance surface: a constitution, a schema, the platform's build declarations
and the platform's vectors. None of them is an artifact the design language can author or the renderer
can build. The ruling is in `transformation/THE_SHAPE_OF_A_CHANGE_V0.md` §7. What this dossier
authorized was delivered by hand, under the dossier, and is recorded here and in `delivery.md`.

## What the phase run established that the problem statement did not

- **The first framing put the proof in the wrong build.** The dossier began by proving the platform's
  transforms in a workload, on the reading that the platform's build runs no conformance. Stage 2
  found that a workload with no act cannot carry a transform, and that a vector declared with the
  platform reaches no build. The business author then asked the question that settled it: who
  governs a vector, and who owns one? The platform governs every vector. Each vector belongs to
  whoever supplies the transform it tests, and the platform supplies its own. The dossier was
  re-authored from P0 on that basis.

- **The decision it corrected was right, and applied too broadly.** Keeping conformance out of the
  platform's build was sound for a domain's implementations and says nothing about the platform's own.
  Proving the platform's transforms in its own build does not reverse that decision; it narrows it to
  what its reason covers.

- **The constitution said otherwise.** Stage 2 took it as sound. Stage 3 read it again and found
  "never in the platform's own build", and a requirement that every vector come from a design. Both
  held only for domains. V2 states the rule by supplier.

- **A name does not say who supplies the code.** A carried copy is byte-identical to its supplier's,
  and the platform's transforms are not named for the platform. So the runner judged the platform's
  build to supply nothing, and a domain's by an accident of namespaces. What a build carried is now a
  record its compile makes.

- **A failed case must refuse its build, whoever supplies the transform.** The runner admitted a build
  whose carried transform's case failed. No build declared such a case, so nothing had shown it.

- **Each composition states what it proved.** All three platform builds prove the platform's
  transforms. None relies on another build's evidence.

## What delivery looks like

Six repositories, in dependency order:
1. the governance surface states the rule and supplies the vectors;
2. the compiler materializes them, records what a build carried, and runs conformance;
3. the runtime judges by that record and refuses on any failed case;
4. the assembler's evidence check covers the platform;
5. the design language names the new constitution;
6. the process names the new build declarations.

**Lifting the vectors without the build step would have been a defect rather than a partial fix.**
Eleven declarations judged by nothing is the dormancy transform conformance removed.

## What is deliberately left open

- **`CT_PURE_COMPARE_EQUAL_V0`** stays unproven until a change gives it a vector.
- **ai_governance's inherited vectors** disagree with its implementations, and are its own change.
- **Three documents** still name the V1 build declarations: a main-only README, a frozen standard, and
  the stale surface map.
