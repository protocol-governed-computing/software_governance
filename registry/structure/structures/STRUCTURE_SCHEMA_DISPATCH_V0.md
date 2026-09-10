# STRUCTURE_SCHEMA_DISPATCH_V0

## Machine

```yaml
fqdn: structure::STRUCTURE_SCHEMA_DISPATCH_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
core:
  summary: Declares which schema governs each artifact kind, and the disposition of every kind toward
    description.
  disposition_vocabulary: structure::VOCAB_SCHEMA_DISPOSITION_V0
  schema_dispatch:
    CAPABILITY_TRANSFORM: SCHEMA_CAPABILITY_TRANSFORM_V0.json
    CAPABILITY_SIDE_EFFECT: SCHEMA_CAPABILITY_SIDE_EFFECT_V0.json
    CAPABILITY_CONTRACT: SCHEMA_CAPABILITY_CONTRACT_V0.json
    WORKFLOW: SCHEMA_WORKFLOW_V0.json
    RUNTIME_BINDING: SCHEMA_RUNTIME_BINDING_V0.json
    INVARIANT: SCHEMA_INVARIANT_V0.json
    CONSTITUTION: SCHEMA_CONSTITUTION_V0.json
    VOCABULARY: SCHEMA_VOCABULARY_V0.json
    SURFACE_CONTRACT: SCHEMA_SURFACE_CONTRACT_V0.json
    STRUCTURE: SCHEMA_STRUCTURE_V0.json
  # Every kind the composition carries, and what was decided about describing it. A kind absent from
  # the dispatch above was absent for three different reasons and one representation — nobody wrote a
  # description, one exists and nobody named it, or the kind needs none — so a reader could not tell a
  # decision from an oversight. Each disposition is drawn from the vocabulary named above.
  schema_disposition:
    CAPABILITY_TRANSFORM: described
    CAPABILITY_SIDE_EFFECT: described
    CAPABILITY_CONTRACT: described
    WORKFLOW: described
    RUNTIME_BINDING: described
    INVARIANT: described
    CONSTITUTION: described
    VOCABULARY: described
    SURFACE_CONTRACT: described
    STRUCTURE: described
    ACTOR: described
    EVENT: described
    INTENT: described
    TRANSPORT_INGRESS: described
    TRANSPORT_EGRESS: described
  # Where a kind is described and its description is not yet dispatched, the ground is recorded here
  # rather than left as an absence. Removing a row means the description was corrected and the kind
  # dispatched; a row that stays is a debt that stays readable.
  description_pending:
    ACTOR: description expects a role and forbids the attributes every actor carries; owned by actor
    EVENT: description forbids content twenty declarations carry; owned by event
    INTENT: description rejects a whole number as a type; owned by intent
    TRANSPORT_INGRESS: no description exists; owned by transport
    TRANSPORT_EGRESS: no description exists; owned by transport
```

---

## Purpose

Which artifacts are schema-governed was decided by a dictionary inside the compiler. That made the governed set a property of the implementation rather than of the protocol — the same defect the closure work removed from artifact machine blocks, one level up.

This artifact declares the mapping. The compiler resolves it.

---

## Scope

Deliberately narrow: **canonical `artifact_kind` → schema identity**, and nothing else.

The mapping does not carry compiler phase, loader selection, error severity, or exception behaviour. Admitting any of those would relocate the hardcoded dispatch table into a protocol artifact without improving the architecture — the declaration would become an opaque registry of compiler behaviour, which is harder to reason about than the dictionary it replaced.

Keys are canonical `artifact_kind` values (the in-block discriminator), matching the kind registry. Values are filenames resolved against the governance schema directory. A kind absent from this mapping is not schema-governed.

---

## Rationale

A declaration the compiler follows can be inspected, versioned, and reasoned about by anyone reading the protocol surface. A dictionary in `s4_govern.py` can be reasoned about only by reading the compiler.
