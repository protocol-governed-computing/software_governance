# Business Problem Statement

**Project Name:** platform — platform transform test data

## 1. Context

The platform supplies capability transforms that any domain may carry: lookup, extract, filter, emit,
and the others a governed act uses to shape its data. Each is declared in `software_governance` and
implemented once, in `software_governance` as well, and every domain that uses one runs the same code.

Every domain build now proves its transforms against their test vectors, once its compile succeeds.
The build names each transform the domain owns as proven, unproven or refused, and names separately
each platform transform the domain carries. The result is part of the snapshot. That mechanism was
delivered under `transform_conformance`, which deliberately wrote no vectors: each transform that
already existed was left unproven until a change gave it vectors.

The platform governs vectors for everyone: its constitution states what a vector is, what counts as
proven, and that a transform's vectors run in the build of the domain that supplies it. Which vectors
a transform has belongs to whoever supplies the transform, because what a vector proves is that
supplier's code.

The reference implementation this platform was derived from carried hand-written vectors for its
transforms. Eleven of them test platform transforms that the composition still carries under the
same codes.

## 2. Problem Statement

**The platform supplies twelve transforms and proves none of them.**

- **The platform's build runs no conformance.** When the platform was narrowed to its normative
  surface, conformance was taken out of its build because the platform does not own a domain's
  implementations. That reason is sound for a domain's transforms and says nothing about the
  platform's own. The platform does own its transforms' implementations, so by the platform's own
  rule, its build is where they are proven. The decision was applied more broadly than its reason.
- **Nothing else proves them either.** A domain that carries a platform transform names it as carried
  and does not test it, correctly: the domain does not supply it. Three of the platform's transforms
  are carried by no domain at all.
- **Vectors for eleven of them already exist and are not used.** The reference implementation's
  vectors for these transforms were not brought across when the platform was rebuilt. A read-only run
  of those cases against the current implementations found that ten transforms match on every case.
  The eleventh, the passthrough transform, returns its value bare, and whether the runner's handling
  of its output yields what the vectors expect is confirmed only when it is built.
- **The vectors are in a format nothing reads.** They state their cases in prose, under numbered
  headings, and name their targets by identities that no longer exist. The platform reads cases from
  the Machine block only, and the human-block fidelity check refuses a declaration made in prose.

Two ways of closing the gap were considered and rejected:

- **Prove each platform transform in every domain that carries it.** The same vector would be stated
  and run up to three times, a transform carried by no domain would be proven nowhere, and each
  domain would be proving code it does not supply.
- **Prove them in a workload built to carry them.** A domain carries a platform transform only when
  one of its own declarations invokes it, so a workload would need acts that exist only to carry
  transforms, the compiler would have to import vectors into domains, and the runner would have to
  prove transforms a build carries rather than supplies. That is three changes to move a proof away
  from the build that supplies the code.

This change shall:

- bring the reference implementation's vectors for the eleven platform transforms across as
  declarations of the platform, with their cases in the Machine block and their targets named by
  current identity;
- re-judge every case against the current declaration and implementation rather than trusting it,
  so a case that no longer holds is either corrected, with the reason recorded, or dropped, with the
  reason recorded;
- run those vectors in the platform's own build, after its compile succeeds, and refuse the platform
  if any fails, exactly as a domain's build does;
- report each of the eleven proven by name, and the twelfth unproven.

### What this change does not decide

- **The vectors of any domain's own transforms.** Three of ai_governance's transforms also have
  vectors in the reference implementation. Those vectors disagree with the current implementations:
  where the reference implementation answered "no", the current one refuses. That is a question for
  the ai_governance domain, in its own change.
- **Vectors for the platform transform the reference implementation never tested.** None is invented
  here.
- **How much proof is enough.** The inherited cases are the floor they were.
- **Proving a domain's transforms in the platform's build.** The platform still does not own a
  domain's implementations.

---

## 3. The execution path a change would take

| # | Repository | What changes |
|---|---|---|
| 1 | `software_governance` | Eleven vectors, one per platform transform, declared beside the transforms they test. A new version of each of the platform's three build declarations, which compiles vectors and declares where their cases are written, and records why the platform proves its own transforms. |
| 2 | `protocol_compiler` | The platform's build step runs conformance after its compile succeeds, as a domain's build step does. |
| 3 | `protocol_runtime` | The runner takes a transform as a build's own when that build declares it, not when its namespace matches the build's scope, since the platform's transforms are not named for the platform. A failed case refuses the build whoever supplies the transform it tests. |
| 4 | `snapshot_assembler` | Only if the platform's result is not carried as a domain's is: the platform's conformance result is carried into the snapshot beside every domain's. |
| 5 | `.github` | The regression and the RUNBOOK record eleven platform transforms proven and one unproven. |

**Lifting the vectors without running them would be a defect, not a partial fix.** Eleven
declarations would sit in the platform, judged by nothing, which is the dormancy `transform_conformance`
removed.

---

## 4. Clarifications — answered by the business author

- **Who governs a vector, and who owns one?**
  **The platform governs every vector; each vector belongs to whoever supplies the transform it
  tests.** The platform supplies its own transforms, so their vectors are the platform's.

- **Where are the platform's vectors run?**
  **In the platform's own build.** The decision to keep conformance out of that build was about a
  domain's implementations; it does not cover the platform's own.

- **What becomes of an inherited case that no longer holds?**
  **It is corrected where the current behaviour is the intended one, dropped where the case tested
  something no longer declared, and never kept as written only because it was inherited.** Each
  correction or drop is recorded with its reason.

- **Does a domain that carries a platform transform still report it as carried once the platform
  proves it?**
  **Yes, unchanged.** A domain's result states what that domain proved. The platform's proof is in the
  platform's result, and the snapshot carries both.

- **Which of the platform's builds prove its transforms?**
  **All three.** The platform has a reference build and two placement builds, a federated and a
  multi-worker one, and all three seal the same transforms. Each composition is sealed on its own and
  states what it proved; none relies on another build's evidence.

- **Is a build admitted when a case for a transform it carries fails?**
  **No. Any failed case refuses the build, whoever supplies the transform it tests.** Today the runner
  judges only a build's own transforms, so such a case would run and be ignored. No domain declares one,
  and this change adds none, but a failed case that admits its build is the silence conformance exists
  to end.
