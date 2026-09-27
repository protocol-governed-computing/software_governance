# Business Problem Statement

**Project Name:** platform — platform transform test data

## 1. Context

The platform supplies capability transforms that any domain may carry: lookup, extract, filter, emit,
and the others a governed act uses to shape its data. Each is declared in `software_governance` and
implemented once, and every domain that uses one runs the same code.

Every domain build now proves its transforms against their test vectors, once its compile succeeds.
The build names each transform the domain owns as proven, unproven or refused, and names separately
each platform transform the domain carries. The result is part of the snapshot. That mechanism was
delivered under `transform_conformance`, which deliberately wrote no vectors: each transform that
already existed was left unproven until a change gave it vectors.

The reference implementation this platform was derived from carried hand-written vectors for its
transforms. Eleven of them test platform transforms that the composition still carries under the
same codes.

## 2. Problem Statement

**Eleven platform transforms are carried by three business domains and proven by none.**

- **The platform's own build runs no conformance, by decision.** The platform does not own a domain's
  implementations, so conformance belongs in a domain's build. That decision stands.
- **The domains that carry a platform transform name it and do not test it.** Today ai_governance
  carries four, book_library_mgmt five and blockchain six. Every domain build reports "carried", and
  no build anywhere proves one.
- **Vectors for them already exist and are not used.** The reference implementation's vectors for
  these eleven transforms were not brought across when the platform was rebuilt. A read-only run of
  those cases against the current implementations found that ten transforms match on every case.
  The eleventh, the passthrough transform, returns its value bare, and whether the runner's handling
  of its output yields what the vectors expect is confirmed only when it is built.
- **The vectors are in a format nothing reads.** They state their cases in prose, under numbered
  headings, and name their targets by identities that no longer exist. The platform reads cases from
  the Machine block only, and the human-block fidelity check refuses a declaration made in prose.

Two ways of closing the gap were considered and rejected:

- **Prove each platform transform in every domain that carries it.** The same vector would be stated
  and run up to three times, and a fourth domain would need a fifth copy. The transform is the
  platform's; its proof should be stated once.
- **Return conformance to the platform's build.** That reverses the decision `transform_conformance`
  kept, for the reason it kept it.

This change shall:

- bring the reference implementation's vectors for the eleven platform transforms across as
  declarations of the platform, with their cases in the Machine block and their targets named by
  current identity;
- re-judge every case against the current declaration and implementation rather than trusting it,
  so a case that no longer holds is either corrected, with the reason recorded, or dropped, with the
  reason recorded;
- run those vectors in a build that carries the platform transforms and exists to prove them, so each
  is proven once, in one place, on every build;
- report each of the eleven proven by name.

### What this change does not decide

- **The vectors of any domain's own transforms.** Three of ai_governance's transforms also have
  vectors in the reference implementation. Those vectors disagree with the current implementations:
  where the reference implementation answered "no", the current one refuses. That is a question for
  the ai_governance domain, in its own change.
- **Vectors for the platform transforms the reference implementation never tested.** None is invented
  here.
- **How much proof is enough.** The inherited cases are the floor they were.

---

## 3. The execution path a change would take

| # | Repository | What changes |
|---|---|---|
| 1 | `software_governance` | Eleven vectors, one per platform transform, declared beside the transforms they test. |
| 2 | `conformance_workloads` | A workload whose build carries the platform transforms and their vectors, so its conformance proves them. It declares no act. |
| 3 | `protocol_runtime` | Only if a case runs as a carried transform and not as an owned one: the runner proves a carried transform whose vector the domain supplies, and still names each carried transform without a vector as carried. |
| 4 | `.github` | The regression builds the workload, and the RUNBOOK records eleven platform transforms proven. |

**Lifting the vectors without a build to run them would be a defect, not a partial fix.** Eleven
declarations would sit in the platform, judged by nothing, which is the dormancy `transform_conformance`
removed.

---

## 4. Clarifications — for the business author

- **Where do the platform's vectors live: with the platform, or with the workload that runs them?**
  Recommended: **with the platform.** A vector says what a platform transform must do, which is a
  platform declaration. The workload only runs it.

- **Is a workload that declares no act a legitimate domain?** Recommended: **yes.** A workload exists
  to exercise the platform. This one exercises its transforms and nothing else, and its snapshot
  result states exactly that.

- **What becomes of an inherited case that no longer holds?** Recommended: **corrected where the
  current behaviour is the intended one, dropped where the case tested something no longer declared,
  and never kept as written only because it was inherited.** Each correction or drop is recorded with
  its reason.

- **Does a domain that carries a platform transform still report it as carried once it is proven
  elsewhere?** Recommended: **yes, unchanged.** A domain's result states what that domain proved. The
  platform transforms' proof is in the workload's result, and the snapshot carries both.
