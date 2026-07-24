# INVARIANT_NO_SHORT_NAME_REFERENCE_V0

## Machine

```yaml
fqdn: fb.constitution::INVARIANT_NO_SHORT_NAME_REFERENCE_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.constitution::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  handler: pgs_governance.registry.handlers.assert_fqdn_only_references_v0
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

Enforce FQDN discipline at the source.

**Constraint**: All references must be resolved to FQDNs during parsing, and the underlying frontmatter must store these as FQDNs.

**Benefit**: Deterministic builds, no ambiguity, portable artifacts.

---

## Rule Statement

```yaml
core:
  description: 'All artifact references in machine frontmatter must be fully qualified (FQDN). Short names
    are prohibited to ensure deterministic, unambiguous resolution across layers and domains.

    '
  anti_patterns:
  - short_name_in_id_field: 'vocabulary_id: VOCAB_STATES_V0 (should be fully qualified)'
  - short_name_in_governed_by: 'governed_by: CONSTITUTION_WF_V0 (should be fully qualified)'
  - ambiguous_reference: Any reference without double-colon separator
```
