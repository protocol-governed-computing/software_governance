# VOCAB_DECLARATION_REPRESENTATION_V0

## Machine

```yaml
fqdn: artifact::VOCAB_DECLARATION_REPRESENTATION_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: artifact
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
  - bootstrap_exception
  - code
  - consults
  - disposition_vocabulary
  - emit
  - enforced_by
  - event_code
  - event_type
  - extends
  - fqdn_id
  - governed_by
  - governs
  - molecule
  - phase_workflows
  - runtime_binding
  - side_effect
  - side_effects
  - storage_structure
  - structure
  - target
  - target_cs
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
named_in_full:
  casing: lower_snake
  entries:
  - bootstrap_exception
  - event_code
  - event_type
  - governs
  - target_cs
supersession:
  casing: lower_snake
  entries:
  - supersedes
data:
  casing: lower_snake
  entries:
  - cases
sameness_rules:
  casing: lower_snake
  entries:
  - explanation_only_as_text
  - reference_to_declared_successor
```

---

## Intent

How every reader of a declaration tells a name from a value. A full name at or beneath a
`reference` part is a reference; a full-name key of a `reference_keyed` part is one too. A
`supersession` part names an artifact without reaching it. A `data` part holds values: nothing
beneath it is read for references, whatever it looks like. A full name anywhere else is refused as
undeclared.

A part that carries an artifact's name as a value is a reference part like any other: a claim's
`target_cs`, an audit record's `event_code` or `event_type`, a surface contract's `governs`. Only a
value written as a full name is a reference. A kind token or a path under the same part is a value,
so these parts are `named_in_full`, not `full_name_required`: a value written as an artifact's code
is refused, and a value of any other shape is not a name.

A test vector's `cases` are data. The transform a vector tests, its `target`, sits outside its cases and stays a reference.
