# Closure — multi_structure_binding

**Phases reached:** P0 – P6, every one admissible
**Status:** COMPLETE. P6 is this dossier's terminal phase, by ruling
**Delivery:** authored, by a person, under this dossier
**Gate 1:** CLOSED at P6 by the business author, against composition `dd8da7a04010…`
**Do not:** author a P7 that inventories a constitution or an invariant as an artifact this design amends

---

## Why it stops

This change delivers three things into the governance surface: a clause in the constitution that
governs bindings, stating for the first time how an act resolves its records; an invariant that
holds that clause, because a resolution rule nothing checks is a sentence; and a widened shape for
what an act may name.

**The design language cannot name any of them.** A design authors an artifact by giving it a family,
and the families are fixed:

```
AC  IN  WF  CC  CT  EV  RB  VOCAB  STRUCTURE  TI  TE          authorable
CS                                                            substrate — a change reuses one, never writes one
```

There is no family for a constitution and none for an invariant, and the renderer has a builder for
each of the eleven and for nothing else. A design that inventoried the constitution as an artifact it
extends would schedule, for a renderer with no way to render one, a document whose every clause is
prose the registers do not carry — and construction renders an extended artifact **whole**, so the
result would be a governing document rewritten from a design that never held its content.

The design is complete and sound. The language to express its delivery does not exist.

## This is the third dossier to stop at P7, and the wall is not the same plank

| dossier | phases | why it stopped |
|---|---|---|
| `generated_artifacts` | P0–P6 | P7 cannot name a generator — the gap it existed to close. **Delivered by hand; that exception is spent.** |
| `rule_effectivity` | P0–P6 | the same, for the same nine generated artifacts |
| `multi_structure_binding` | P0–P6 | P7 has no family for the artifacts the platform is made of |

The first two stopped on how an artifact is *reached*. This one stops on what an artifact *is*. They
are different gaps in one language, and the pattern is worth stating plainly: **the design compiler
can author every artifact a business domain writes, and none of the artifacts the platform is made
of.** Every platform change so far has therefore been delivered by hand, and each was correct at the
moment it was made and left no rule behind.

## What must not happen

The constitution and the invariant could be edited directly, and every check in the workspace would
pass — the compile does not ask which change authorized a clause. That is how the platform has always
been changed, and the reason it is called out here is that this dossier exists to remove exactly that
shape of workaround one level down: an act reaching another subdomain's records by copying its
description also works today, and also passes everything.

Delivering this change by hand while it argues against hand-delivery does not invalidate the
argument, but it should be recorded as what it is rather than absorbed as normal.

## Ruled — this is a boundary, not a gap

**The governance surface is authored, not constructed.** A constitution, an invariant and a schema are
written by a person under a governed dossier; the pipeline's authority over such a change ends at P6.
A constitution's content is argument, and a register that determined it would have to carry the
argument — at which point the register is the constitution and the document is its rendering. The
ruling is recorded in `transformation/doc/THE_SHAPE_OF_A_CHANGE_V0.md` §7 and enforced by
`AMENDED_ARTIFACT_NOT_AUTHORABLE`.

So this dossier is **complete**, not halted. Its six capabilities are settled, its eight boundary
rules are stated, Gate 1 is closed at P6 — where a governance change closes it, by ruling — and
delivery is the authoring of the clause and the invariant it argues for.

The cost is stated where the ruling is: a governance artifact cannot be re-rendered from its dossier
and compared, so nothing mechanically catches a document that drifts from the design that argued for
it. The alternative was a generator inventing the argument.

## What resumes downstream

The wallet is not blocked on this dossier's *delivery mechanism* — it is blocked on the capability.
Once the resolution model exists in the governance surface, the domain half is an ordinary change
request in `blockchain`: the act names the binding it consults, and the two artifacts it amends are
a WF and an RB, both of which the design language has families for and construction can render.
