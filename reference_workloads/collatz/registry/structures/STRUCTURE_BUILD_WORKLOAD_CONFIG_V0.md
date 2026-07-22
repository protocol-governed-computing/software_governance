# STRUCTURE_BUILD_WORKLOAD_CONFIG_V0

**Artifact Type**: STRUCTURE
**Version**: V0
**Status**: CANONICAL
**Governed By**: fb.constitution::CONSTITUTION_STRUCTURE_V0

---

## Purpose

Self-describing build manifest for the **PGC reference-workload** domain (`workload::`) — an
independently-authored domain compiled **against** the already-compiled platform surface, then
composed into the assembled universe.

This artifact lives in the **domain's own source** (not in `platform/registry/`), so the platform
surface is never edited to add a domain — its identity/hash is unchanged. The compiler merges this
manifest's `layer_definitions` and `identity_rules` **additively** (only for this build) on top of
the immutable platform `STRUCTURE_DISCOVERY_V0` / `STRUCTURE_IDENTITY_V0`.

First consumer: `workload::collatz` (Phase 1 — pure compute → verify).

---

## Machine

```yaml
structure_code: STRUCTURE_BUILD_WORKLOAD_CONFIG_V0
version: V0
governed_by: fb.constitution::CONSTITUTION_STRUCTURE_V0

# Domain/structure scope this build materializes — becomes the assembled snapshot domain id.
structure_scope: workload

core:
  summary: Build-time STRUCTURE manifest (PGC reference-workload domain scope)
  description: >
    Compiles the workload domain's own artifacts (WF/IN/CC/CT), resolving governance and platform
    capability references against the imported compiled platform surface. Emits only workload
    artifacts. Self-describing: declares its own source layer and namespace rule additively.

# --- Domain-extension declarations (merged additively; platform artifacts untouched) ---

# Additive layer definition — merged into discovery layers for THIS build only.
layer_definitions:
  WORKLOAD:
    # Filesystem source (data-driven): a subdir of the platform repo. No compiler edit.
    platform_subpath: reference_workloads/collatz/registry
    # Namespace prefix for FQDN derivation (module_path); mapped to `workload` by identity_rules.
    registry_module: workload.registry
    implementation_namespace: reference_workloads.collatz.implementation.capability_transforms.atoms
    layer_category: workload

# Additive namespace rule — merged into identity derivation rules for THIS build only.
identity_rules:
  - match: "workload.registry"
    namespace: "workload"

artifact_discovery:

  search_layers:
    - WORKLOAD

  # Import the compiled platform surface as resolvable externals (governance + capabilities).
  # Resolved/validated against, but NOT re-discovered or re-emitted into this domain.
  import_surface:
    domain: platform

  # Workload executable artifact types (Phase 1 subset — no CS/RB/store yet).
  artifact_types:
    - WF
    - IN
    - CC
    - CT
    - EV
    - AC

output_configuration:

  artifacts:
    layer: PROTOCOL_BUILD_ROOT
    subpath: compiled/canonical

  vocabulary_projection_path:
    layer: GOVERNANCE
    subpath: compiled/vocabulary

  tokenized_projection_path:
    layer: GOVERNANCE
    subpath: compiled/tokenized

  evidence_projection_path:
    layer: GOVERNANCE
    subpath: compiled/evidence

  trust_attestation_path:
    layer: GOVERNANCE
    subpath: compiled/trust

  visualization_projection_path:
    layer: GOVERNANCE
    subpath: compiled/visualization

  layer_outputs:
    WORKLOAD:
      layer: WORKLOAD
      subpath: compiled/canonical

  bootstrap_search_roots:
    - layer: GOVERNANCE
      subpath: FB_CONSTITUTION/structures

build_phases:
  - phase: discover
    description: Discover workload artifacts via STRUCTURE
  - phase: parse
    description: Parse artifacts into canonical machine form
  - phase: normalize
    description: Resolve references (workload + imported platform surface)
  - phase: validate
    description: Validate artifacts using compiler schema rules
  - phase: assert
    description: Evaluate cross-artifact invariants (surface closure)
  - phase: materialize
    description: Emit deterministic compiled artifacts (workload scope only)
    target: "compiled/artifacts/"

```

## Version History

- **V0**: First PGC reference-workload domain build manifest. Self-describing (declares its own
  layer + namespace rule); compiles `workload::` against the imported compiled platform surface;
  emits only workload artifacts. Platform surface unchanged.
