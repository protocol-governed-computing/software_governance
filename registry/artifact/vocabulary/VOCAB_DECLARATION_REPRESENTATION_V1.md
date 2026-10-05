# VOCAB_DECLARATION_REPRESENTATION_V1

## Machine

```yaml
fqdn: artifact::VOCAB_DECLARATION_REPRESENTATION_V1
artifact_kind: VOCABULARY
version: v1
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: artifact
supersedes: artifact::VOCAB_DECLARATION_REPRESENTATION_V0
extends: ''
documentation:
  casing: lower_snake
  entries:
  - summary
  - description
  - notes
  - purpose
  - use_cases
  - failure_modes
  - intent
  - detail
  - admission_rules
unordered:
  casing: lower_snake
  entries:
  - allowed
  - result_surface
  - result_status_values
  - canonical_surface
  - applies_to_kinds
  - governs
  - superseded_by
  - requires
  - forbids
  - consults
  - allowed_capability_transforms
  - allowed_capability_side_effects
reference:
  casing: lower_snake
  entries:
  - actor_context
  - allowed_capability_side_effects
  - allowed_capability_transforms
  - atom
  - code
  - consults
  - disposition_vocabulary
  - emit
  - enforced_by
  - extends
  - fqdn_id
  - governed_by
  - molecule
  - phase_workflows
  - runtime_binding
  - side_effect
  - side_effects
  - storage_structure
  - structure
  - target
  - transform
  - transforms
  - vocabulary_id
  - workflow
reference_keyed:
  casing: lower_snake
  entries:
  - bindings
full_name_required:
  casing: lower_snake
  entries:
  - consults
  - governed_by
  - runtime_binding
  - side_effects
  - structure
  - transform
  - transforms
  - vocabulary_id
supersession:
  casing: lower_snake
  entries:
  - supersedes
  - superseded_by
sameness_rules:
  casing: lower_snake
  entries:
  - explanation_only_as_text
  - reference_to_declared_successor
```

---

## Intent


