# CONSTITUTION_GOVERNANCE_ONTOLOGY_V0

## Machine
```yaml
fqdn: artifact::CONSTITUTION_GOVERNANCE_ONTOLOGY_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: artifact
core:
  enforcement_model: compiler_enforced
rules:
- applies_to: VOCAB
  enforced_by: artifact::INVARIANT_GOVERNANCE_ONTOLOGY_AGREES_V0
```

---

## 1. Purpose

This constitution establishes that the Governance Ontology is part of the composition. The
classification of every artifact kind is sealed, so a verifier can read it from the snapshot and
does not depend on the tool that built the snapshot.

---

## 2. Core Principles

- **One ontology.** The compiler's built-in classification and the sealed vocabulary state the same
  ontology. A build in which they differ is refused.
- **Classified once.** Each artifact kind declares one semantic category and the provenance it
  carries. Runtime disposition belongs to the category contract, never to a kind.
- **Read, not inferred.** A reader takes a kind's classification from the vocabulary. Nothing
  derives it from a kind's name, prefix or location.

---

## How it is checked
- The platform build compares the vocabulary with the compiler's built-in table and fails on any
  difference.

---

## What this realizes
```yaml
core:
  description: Seals the Governance Ontology into the composition and holds the compiler to it
rules:
- rule_id: GOVERNANCE_ONTOLOGY_AGREES
  constraint: the sealed ontology vocabulary and the compiler's built-in classification MUST state
    one ontology
```
