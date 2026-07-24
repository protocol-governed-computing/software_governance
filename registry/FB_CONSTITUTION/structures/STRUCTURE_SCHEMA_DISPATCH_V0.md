# STRUCTURE_SCHEMA_DISPATCH_V0

## Machine

```yaml
structure_code: STRUCTURE_SCHEMA_DISPATCH_V0
version: V0
governed_by: fb.constitution::CONSTITUTION_STRUCTURE_V0
core:
  summary: Declares which schema governs each artifact kind.
  schema_dispatch:
    CT: SCHEMA_CAPABILITY_TRANSFORM_V0.json
    CS: SCHEMA_CAPABILITY_SIDE_EFFECT_V0.json
    CC: SCHEMA_CAPABILITY_CONTRACT_V0.json
    WF: SCHEMA_WORKFLOW_V0.json
    RB: SCHEMA_RUNTIME_BINDING_V0.json
    INVARIANT: SCHEMA_INVARIANT_V0.json
    CONSTITUTION: SCHEMA_CONSTITUTION_V0.json
    SURFACE: SCHEMA_SURFACE_CONTRACT_V0.json
```

---

## Purpose

Which artifacts are schema-governed was decided by a dictionary inside the compiler. That made the governed set a property of the implementation rather than of the protocol — the same defect the closure work removed from artifact machine blocks, one level up.

This artifact declares the mapping. The compiler resolves it.

---

## Scope

Deliberately narrow: **artifact-type prefix → schema identity**, and nothing else.

The mapping does not carry compiler phase, loader selection, error severity, or exception behaviour. Admitting any of those would relocate the hardcoded dispatch table into a protocol artifact without improving the architecture — the declaration would become an opaque registry of compiler behaviour, which is harder to reason about than the dictionary it replaced.

Keys are artifact-code type prefixes, matching `ArtifactKindRegistry`. Values are filenames resolved against the governance schema directory. A kind absent from this mapping is not schema-governed.

---

## Rationale

A declaration the compiler follows can be inspected, versioned, and reasoned about by anyone reading the protocol surface. A dictionary in `s4_govern.py` can be reasoned about only by reading the compiler.
