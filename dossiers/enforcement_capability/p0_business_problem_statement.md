# Business Problem Statement

**Project Name:** platform — conformance

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed business
> requirement and the execution path a change would take. It is not a design.

## 1. Context

The platform declares obligations and renders each as an assertion the compiler evaluates. The
relation between the two is guarded: every obligation has an assertion, and every assertion has an
obligation. That guarantee is what lets a reader take the count of obligations as the measure of what
is enforced.

An assertion that cannot refuse anything satisfies the same guarantee. It is present, it is named by
its obligation, it runs on every build, it matches nothing, and it reports clean. The obligation
above it reads as governance and governs nothing.

## 2. Problem Statement

**An obligation declared as governance that cannot refuse is not governance, and nothing tells the
two apart.**

Measured over the platform's own surface: **fourteen of eighty-seven assertions cannot refuse
anything.** Ten of them say so in their own text — *"Phase 1 stub — full enforcement in Phase 3"* —
enforcement that was described and never written. Two delegate to the runtime and were checked and do
hold. One exists only to satisfy the obligation-to-assertion guarantee, and says so: *"this handler
exists to satisfy 1:1 INVARIANT/ASSERT parity."*

**The guarantee is therefore satisfied by a stub.** It counts declarations, not capability, and
fourteen unenforced obligations pass a check designed to prove coverage.

A fifteenth is worse than absent. Its obligation is declared as governance; its assertion returns no
violations and reports PASSED; its only refusal path is a guard for missing input rather than a
refusal of the obligation. Its stated subject is *"code smell indicator"* and *"potential
optimization opportunities"* — which is a judgement about whether a thing is good, made by machinery
whose whole remit is whether a thing is admissible.

**The count was found by measuring, and the fifteenth was found by reading.** A structural census
counts the fifteenth as capable, because it does have a refusal path — just not one that can ever
refuse its own obligation. So the fourteen is a floor rather than a total, and no measurement
currently establishes the ceiling.

**What makes this a business problem rather than a cleanup.** Fifteen artifacts could be corrected
this afternoon and the surface would be back where it is now the moment someone adds the sixteenth.
The declarations were all written in good faith by people who intended to build the enforcement
later; nothing refused them then and nothing would refuse them now. **The requirement is a mechanism
that refuses the next one**, and a way for an obligation to say honestly that it is not yet enforced
without that statement being indistinguishable from silence.

## 3. Why This Surfaced Now

An unrelated change turned on an admission gate that had been admitting everything. The gate was
declared, inert, and indistinguishable from enforcing — and behind it sat contract mismatches nobody
had seen, in three domains.

That was one instance. Measuring the platform's own assertions for the same shape found fourteen
more, and the pattern is the same every time: **declared, believed enforced, enforcing nothing, and
no way to tell from the outside.**
