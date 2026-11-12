# INVARIANT_GOVERNANCE_ONTOLOGY_AGREES_V0

## Machine

```yaml
fqdn: artifact::INVARIANT_GOVERNANCE_ONTOLOGY_AGREES_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: artifact
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - VOCAB
```

---

## Purpose

The compiler classifies every artifact kind from a built-in table. It cannot read the
classification from the composition, because it needs it to compile the composition. The sealed
`artifact::VOCAB_GOVERNANCE_ONTOLOGY_V0` states the same classification for every reader that
does not hold the compiler.

Two statements of one ontology drift unless something compares them. This invariant compares them
at every platform build and refuses the build when they differ.

---

## How it is checked

The build that authors the ontology vocabulary compares it with the built-in table:

- the semantic categories and the provenances are the same sets;
- each classified kind is in the same category group and the same provenance group in both, and in
  exactly one of each;
- each category is in the same runtime disposition group in both.

A build that does not author the vocabulary has nothing to compare and passes. Imported governance
is never a subject.

---

## What this realizes
```yaml
core:
  description: The sealed Governance Ontology and the compiler's built-in classification state one
    ontology.
  anti_patterns:
  - unsealed_ontology: a kind is classified in code and nowhere a reader of the snapshot can see
  - drifted_ontology: the vocabulary and the built-in table classify a kind differently
```
