# INVARIANT_STRUCTURE_PATHS_WELL_FORMED_V0

## Machine

```yaml
fqdn: structure::INVARIANT_STRUCTURE_PATHS_WELL_FORMED_V0
artifact_kind: INVARIANT
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    level: ERROR
    order: 23
  applies_to_kinds:
  - STRUCTURE
```

---

## Purpose

STRUCTURE artifacts are the only authority for where anything lives. A path that escapes its layer, or resolves against the host filesystem, or is absent and defaulted, moves that authority out of the protocol and into whatever happens to be running.

---

## Validation Rules

### Rule 1: No absolute paths

No path value may begin with `/`. All paths are layer-relative.

### Rule 2: No layer escape

No path value may contain a `..` segment.

### Rule 3: Paths are explicitly declared

A path-valued key MUST carry a non-empty string. An absent or empty path is an implicit default.

### Rule 4: Referenced layers are declared

Every layer code referenced by a build configuration — in `artifact_discovery.search_layers`, in `output_configuration.layer_outputs`, or as a `layer` value — MUST be declared, either in the discovery master's `discovery.layers` or in a build manifest's own `layer_definitions`.

Rule 4 is evaluated only where a declaring artifact is present in the compiled set.

---

## Scope

Cross-artifact by nature: layer declaration and layer reference routinely live in different STRUCTURE artifacts, which is why this cannot be expressed as a per-artifact schema constraint.

---

## Rationale

Deterministic resolution is a property of the declarations, not of the resolver. If every path is explicit, relative, and non-escaping, and every layer resolves to a declaration, then two compilers reading the same surface must reach the same files.
