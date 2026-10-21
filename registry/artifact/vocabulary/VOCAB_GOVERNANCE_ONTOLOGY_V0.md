# VOCAB_GOVERNANCE_ONTOLOGY_V0

## Machine

```yaml
fqdn: artifact::VOCAB_GOVERNANCE_ONTOLOGY_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: artifact
extends: ''
semantic_categories:
  casing: lower_snake
  entries:
  - definitional
  - normative
  - contractual
  - operational
  - participatory
  - evidential
provenances:
  casing: lower_snake
  entries:
  - authored
  - derived
  - produced
category_definitional:
  casing: UPPER_SNAKE
  entries:
  - STRUCTURE
  - VOCABULARY
category_normative:
  casing: UPPER_SNAKE
  entries:
  - ASSERT
  - CONSTITUTION
  - INVARIANT
  - TEST_DATA
category_contractual:
  casing: UPPER_SNAKE
  entries:
  - CAPABILITY_CONTRACT
  - SURFACE_CONTRACT
  - TRANSPORT_EGRESS
  - TRANSPORT_INGRESS
category_operational:
  casing: UPPER_SNAKE
  entries:
  - CAPABILITY_SIDE_EFFECT
  - CAPABILITY_TRANSFORM
  - INTENT
  - RUNTIME_BINDING
  - WORKFLOW
category_participatory:
  casing: UPPER_SNAKE
  entries:
  - ACTOR
category_evidential:
  casing: UPPER_SNAKE
  entries:
  - EVENT
provenance_authored:
  casing: UPPER_SNAKE
  entries:
  - ACTOR
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
  - TEST_DATA
  - TRANSPORT_EGRESS
  - TRANSPORT_INGRESS
  - VOCABULARY
  - WORKFLOW
provenance_derived:
  casing: UPPER_SNAKE
  entries:
  - ASSERT
runtime_disposition_not_executable:
  casing: lower_snake
  entries:
  - definitional
  - normative
runtime_disposition_not_independently_executable:
  casing: lower_snake
  entries:
  - contractual
runtime_disposition_executable:
  casing: lower_snake
  entries:
  - operational
runtime_disposition_participates_in_execution:
  casing: lower_snake
  entries:
  - participatory
runtime_disposition_produced_by_execution:
  casing: lower_snake
  entries:
  - evidential
```

---

## Intent

The Governance Ontology, sealed. Each artifact kind declares its semantic category and the
provenance it carries, and nobody infers either from a kind's name or location (GO-3). Runtime
disposition belongs to the category contract, so a kind's disposition is read from its category and
never stated per kind.

A `category_` group lists the kinds in one semantic category. A `provenance_` group lists the kinds
that carry one provenance. A `runtime_disposition_` group lists the categories whose contract has
that disposition. No kind is produced, so `produced` has no group: an occurrence of an event is
produced by execution, and an occurrence is evidence, not an artifact kind.

The compiler classifies kinds from a built-in table, because it needs the classification to compile
this vocabulary. `artifact::INVARIANT_GOVERNANCE_ONTOLOGY_AGREES_V0` refuses a build in which the
table and this vocabulary differ. A reader of the snapshot learns the ontology here and needs no
compiler.
