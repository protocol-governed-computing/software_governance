# INVARIANT_VOCABULARY_SYMBOLS_WELL_FORMED_V0

## Machine

```yaml
fqdn: vocabulary::INVARIANT_VOCABULARY_SYMBOLS_WELL_FORMED_V0
artifact_kind: INVARIANT
version: V0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: vocabulary
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    level: ERROR
    order: 21
  applies_to_kinds:
  - AC
  - CC
  - CONSTITUTION
  - CS
  - CT
  - EV
  - IN
  - INVARIANT
  - RB
  - SCHEMA
  - STRUCTURE
  - SURFACE
  - TE
  - TI
  - VOCAB
  - WF
```

---

## Purpose

A symbol that no vocabulary declares is a symbol nobody agreed to. Closing the symbol space is what makes the vocabulary authoritative rather than descriptive.

---

## How it is checked
### Rule 1: Artifact codes are UPPER_SNAKE_CASE with a version suffix

Every artifact code MUST match `^[A-Z][A-Z0-9_]*_V[0-9]+$`.

### Rule 2: Node types are declared

Every workflow node `type` MUST appear in `VOCAB_PROTOCOL_KINDS_V0.node_types.entries`.

### Rule 3: Result statuses are declared

Every status in a capability contract's `core.result_status_contract.allowed` MUST appear in `VOCAB_EXECUTION_STATES_V0.result_status.entries`.

### Rule 6: A vocabulary that names artifacts names ones that exist

A vocabulary group that declares `names_kind` lists artifacts by code. Every entry MUST be the code of an artifact of that kind that the build can see, in its own artifacts or in the surface it imports.

Rules 4 and 5 govern extension and are stated in `vocabulary::CONSTITUTION_VOCABULARY_V0` §9.1.

Rules 2 and 3 are evaluated only where the vocabulary artifact is present in the compiled set; a build that carries no vocabulary cannot be measured against one.

---

## Rationale

Implicit symbol creation is how a protocol acquires meaning nobody declared. Every symbol the compiler accepts must trace to a vocabulary entry.
