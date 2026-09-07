# Business Problem Statement

**Project Name:** platform — snapshot

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed business
> requirement and the execution path a change would take. It is not a design.

## 1. Context

A built composition has an identity, computed over the bytes of every file it carries. That identity
is what lets a reader say two compositions are the same one, and what lets a change pin the
composition it was validated against so that anything grounded on it can be re-checked later.

## 2. Problem Statement

**Building the same source twice produces two different compositions, and nothing distinguishes that
from a real change.**

Compiling one unchanged domain twice, with nothing edited between the two builds, yields two
identities. Ninety-one files are written by each build and ninety are byte-identical; one differs,
and it differs in one field: **the moment the build ran, recorded to the microsecond.**

**The identity is therefore a function of when it was built, not of what it contains.** Everything
that establishes what the composition *is* — the artifacts it carries, the domains, the address each
artifact resolves to — is identical across the two builds. Only the clock moved.

**The consequence is that a pin cannot be kept.** A change records the composition it was validated
against, so that every claim resting on that composition can be re-checked. The record survives until
someone rebuilds, which is the ordinary act of working, and then it names a composition that no
longer exists. What was pinned is not recoverable by rebuilding the same source.

**And a genuine change becomes indistinguishable from none.** Identity was made a function of the
bytes so that a composition altered after it was sealed, or moved somewhere it was not built for,
would be caught by recomputing. A field that changes on every build regardless makes every rebuild
look like an alteration, and a reader who sees identities differ learns nothing from it.

## 3. Why This Surfaced Now

**A change tried to use its own pin and could not.** A change request pinned the composition it was
designed against, had every claim resting on that composition approved, and was then reported as
resting on a composition that is not the one on disk. Nothing in the registry had changed. The
composition had been rebuilt.

**Isolating it took holding the change's own artifacts aside.** With them removed, the rebuild
returns the pinned count of artifacts and every domain's address map is byte-identical to the pin —
and the identity still differs. Assembling twice without recompiling is stable, so what is unstable
is the compile.

## 4. What This Is Not

**It is not the change's defect.** The pin was correct when taken and the artifacts it names are
unchanged. What expired is the identity, and it expired because a build wrote the time.

**It is not a case for weakening the identity.** Computing identity over the bytes is what makes
tampering and relocation detectable, and that is worth keeping. What is wrong is that a field
recording *when the composition was signed* is being counted as part of *what the composition is*.
