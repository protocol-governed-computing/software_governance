# Can the root constitution be governed by a subordinate one?

## Open. The declared graph contains a two-node cycle through the supreme constitution.

This is recorded separately from `AUTHORITY_VS_CONCERN_RULING.md` because it may be a different
problem. That ruling concerns how authority and concern are encoded in a namespace; this concerns
what the `governed_by` relation means, and whether the surface is consistent under it.

## The cycle

```
governance::CONSTITUTION_GOVERNANCE_V0  ──governed_by──▶  vocabulary::CONSTITUTION_VOCABULARY_V0
vocabulary::CONSTITUTION_VOCABULARY_V0  ──governed_by──▶  governance::CONSTITUTION_GOVERNANCE_V0
```

Both edges are declared in the artifacts' own `## Machine` blocks. `CONSTITUTION_INVARIANTS_V0`,
also in `governance`, declares the same `governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0`.

`CONSTITUTION_GOVERNANCE_V0` states of itself:

> This constitution is supreme. All other constitutions derive authority from this document. In the
> event of conflict between this constitution and any other, this constitution prevails.

So the supreme constitution declares itself governed by a constitution that derives its authority from
the supreme constitution.

## Why this is not obviously a defect

`governed_by` is used widely and consistently across the surface — 46 artifacts name
`CONSTITUTION_INVARIANTS_V0`, 21 name `CONSTITUTION_GOVERNANCE_V0`, and every constitution carries
one. A relation that pervasive is load-bearing, and its meaning may be narrower than "derives its
authority from."

Two readings are available:

**`governed_by` means authority derivation.** Then the cycle is a genuine defect: the root authority
derives from something that derives from it, and the chain of authority the constitution calls
"explicit, versioned, and immutable" is not well-founded.

**`governed_by` means governed subject** — which artifact's rules constrain this artifact's form.
Then there is no contradiction: the supreme constitution is written in vocabulary the vocabulary
constitution governs, without surrendering supremacy to it. Form is constrained by one artifact;
authority derives from another.

The surface does not say which. That is the finding.

## The question to rule

**Can the root authority be governed by a subordinate constitution without deriving its authority from
that constitution?**

If yes, the model must distinguish *governance of subject matter* from *derivation of authority*, and
`governed_by` needs a companion relation — or an explicit statement that it never carried the second
meaning.

If no, this is a circular authority defect, and one of the two edges is wrong.

## Why it matters beyond the two artifacts

`vocabulary` is one of only two boundaries declaring universal reach — its rules enumerate all
sixteen artifact kinds. If `governed_by` does mean authority derivation, then the surface's root
authority derives from a boundary whose jurisdiction is unbounded, which compounds rather than
resolves the bounded-jurisdiction problem recorded in `AUTHORITY_VS_CONCERN_EVIDENCE.md`.

## What this finding does not claim

That either edge is wrong. Both are declared deliberately and the surface compiles. The claim is only
that two statements — supremacy, and being governed by a derivative — cannot both hold under the
strong reading of `governed_by`, and the surface does not declare which reading is intended.
