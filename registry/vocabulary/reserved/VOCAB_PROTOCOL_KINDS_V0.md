# VOCAB_PROTOCOL_KINDS_V0 — Protocol Ontology

**Governance Header**
- Vocabulary ID: vocabulary::VOCAB_PROTOCOL_KINDS_V0
- Version: v0
- Governed By: vocabulary::CONSTITUTION_VOCABULARY_V0
- Status: Active

---

## Purpose

Defines what things ARE in the protocol: node type prefixes and artifact kind names.

## Allowed Usage

- `node_types`: As node type values in workflow DAG definitions
- `artifact_kinds`: In artifact header `Artifact Kind` field and schema routing

## Prohibited Usage

- Must NOT be used as protocol identifiers (WF_*, CC_*, etc.)
- Must NOT be used as parameter names or free-form identifiers
- Node types and artifact kinds must not appear in other vocabulary files

## Governance Rules

- Node types are globally unique UPPER_SNAKE symbols. Most are the two-letter kind prefix of an
  authorable artifact; `EXIT` is structural and has no artifact kind.
- Artifact kinds are globally unique UPPER_SNAKE names, and are exactly the canonical values of the
  Kind Vocabulary. A kind absent from that vocabulary is invalid for this revision.
- An artifact kind MAY have a governing JSON Schema. Twelve of the sixteen kinds do; `ASSERT`,
  `VOCABULARY`, `TRANSPORT_INGRESS`, and `TRANSPORT_EGRESS` are governed by their constitutions
  without a separate schema.
- `TRANSPORT_INGRESS` and `TRANSPORT_EGRESS` are first-class kinds, not aliases of `EVENT` / `INTENT`.

### Domain extension

This artifact declares the **platform** symbol space. A domain that requires a symbol the platform
does not interpret SHALL declare its own `VOCABULARY` artifact in its own namespace; it SHALL NOT
add domain symbols here. Platform vocabulary is closed to domain concepts — a symbol belongs here
only if the platform compiler or runtime interprets it.

---

## Machine

```yaml
fqdn: vocabulary::VOCAB_PROTOCOL_KINDS_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: vocabulary
node_types:
  casing: UPPER_SNAKE
  entries:
  - AC
  - CC
  - CS
  - CT
  - EV
  - EXIT
  - IN
  - RB
  - TE
  - TI
  - WF
artifact_kinds:
  casing: UPPER_SNAKE
  entries:
  - ACTOR
  - ASSERT
  - CAPABILITY_CONTRACT
  - CAPABILITY_SIDE_EFFECT
  - CAPABILITY_TRANSFORM
  - CONSTITUTION
  - EVENT
  - INTENT
  - INVARIANT
  - RUNTIME_BINDING
  - STRUCTURE
  - SURFACE_CONTRACT
  - TRANSPORT_EGRESS
  - TRANSPORT_INGRESS
  - VOCABULARY
  - WORKFLOW
```
