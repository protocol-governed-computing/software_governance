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
    TEST_DATA: SCHEMA_TEST_DATA_V0.json
    EVENT: SCHEMA_EVENT_V0.json
    ACTOR: SCHEMA_ACTOR_V0.json
    INTENT: SCHEMA_INTENT_V0.json
    TRANSPORT_INGRESS: SCHEMA_TRANSPORT_INGRESS_V0.json
    TRANSPORT_EGRESS: SCHEMA_TRANSPORT_EGRESS_V0.json
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
    TEST_DATA: described
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
