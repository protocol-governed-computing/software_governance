# STRUCTURE_BUILD_PLATFORM_CONFIG_V1

**Artifact Type**: STRUCTURE
**Version**: V1
**Status**: CANONICAL
**Governed By**: fb.structure::CONSTITUTION_STRUCTURE_V0

---

## Purpose

Defines artifact discovery and output paths for **PGC normative-platform** compilation.

This STRUCTURE governs:

* Where the compiler discovers artifacts
* Which artifact types are in scope
* Where compiled artifacts are written

**Scope**: PGC normative platform surface only.

**Change from V0 (first PGC normative divergence from the faithful RI-0 harvest):**
V0 encoded RI-0's platform scope, which is wider than the PGC platform. V1 narrows it to
the PGC normative surface by removing concerns that are **not** platform-owned:

* `CAPABILITIES` layer — the `name_service` registry is a **domain** capability (`pgs::`),
  excluded from the PGC platform (the 150). Returns later as a `pgs::` domain extension.
* `TEST_DATA` layer + `conformance_generate` / `conformance_execute` phases — **implementation-
  layer conformance**. Per the capability-ownership decision, capability *implementations*
  (and therefore conformance against them) are not platform-owned; they are enforced where
  the implementations live, not in the normative-surface compile.

---

## Core

Build-time STRUCTURE configuration.

This artifact is the **single source of truth** for:

* discovery scope
* artifact inclusion
* output location

No fallback or implicit behavior is permitted.

---

## Machine

```yaml
fqdn: fb.structure::STRUCTURE_BUILD_PLATFORM_CONFIG_V1
artifact_kind: STRUCTURE
version: V1
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0
structure_scope: platform
reuse_visibility: substrate
core:
  summary: Build-time STRUCTURE configuration (PGC normative-platform scope)
  description: 'Defines artifact discovery and output paths for PGC normative-platform compilation. Domain
    layers and implementation-layer conformance are out of scope.

    '
artifact_discovery:
  search_layers:
  - GOVERNANCE
  - REUSABLE_TRANSFORMS
  - REUSABLE_SIDE_EFFECTS
  artifact_types:
  - VOCAB
  - CONSTITUTION
  - INVARIANT
  - ASSERT
  - SCHEMA
  - STRUCTURE
  - EXECUTION_POLICY
  - WF
  - IN
  - TI
  - TE
  - CC
  - CT
  - CS
  - EV
  - RB
  - SURFACE
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
    GOVERNANCE:
      layer: GOVERNANCE
      subpath: compiled/canonical
    REUSABLE_TRANSFORMS:
      layer: REUSABLE_TRANSFORMS
      subpath: compiled/canonical
    REUSABLE_SIDE_EFFECTS:
      layer: REUSABLE_SIDE_EFFECTS
      subpath: compiled/canonical
  bootstrap_search_roots:
  - layer: GOVERNANCE
    subpath: structure/structures
build_phases:
- phase: discover
  description: Discover artifacts via STRUCTURE
- phase: parse
  description: Parse artifacts into canonical machine form
- phase: normalize
  description: Resolve references to FQDN with deterministic binding
- phase: validate
  description: Validate artifacts using compiler schema rules
- phase: assert
  description: Evaluate cross-artifact invariants (surface closure)
- phase: materialize
  description: Emit deterministic compiled artifacts
  target: compiled/artifacts/
```

## Version History

- **V1**: PGC normative-platform scope. Removed `CAPABILITIES` (domain) and `TEST_DATA` +
  conformance phases (implementation-layer). First PGC normative divergence from RI-0.
- **V0**: RI-0 platform scope (faithful harvest). Retained immutable as provenance.
