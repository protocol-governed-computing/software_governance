# STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V0

The same governance surface, composed for multi-worker placement.

A build configuration names exactly one arrangement per selectable boundary, so two
compositions differing in placement are two configurations. That is the shape rather than a
duplication to be factored away: a configuration *is* the definition of a composition, and the
surface it draws from is identical — what differs is one named mode, visible on one line.

Everything else here is deliberately the same as `STRUCTURE_BUILD_PLATFORM_CONFIG_V0`. Where the
two diverge in anything but placement, that divergence is a defect: it would mean two
compositions claiming one surface and drawing different artifacts from it.

**Artifact Type**: STRUCTURE
**Version**: V2
**Governed By**: structure::CONSTITUTION_STRUCTURE_V0

---

## Purpose

Defines artifact discovery and output paths for **PGC normative-platform** compilation.

This STRUCTURE governs:

* Where the compiler discovers artifacts
* Which artifact types are in scope
* Where compiled artifacts are written

**Scope**: PGC normative platform surface only.

A domain's capabilities, and conformance against a domain's implementations, are not
platform-owned and are built where the domain lives. The platform's own transforms are: this build
compiles the platform's test vectors (`TEST_DATA`) and declares where their runnable cases are
written, so the platform's build proves its own transforms (`conformance::CONSTITUTION_TEST_DATA_V0`
§4). It never proves a domain's.

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
fqdn: structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
structure_scope: platform
reuse_visibility: substrate
core:
  summary: Build-time STRUCTURE configuration, multi-worker placement (PGC normative-platform scope)
  description: 'Defines artifact discovery and output paths for PGC normative-platform compilation. Domain
    layers and conformance against a domain''s implementations are out of scope; the platform''s
    own transforms are proven against their vectors.

    '
placement_mode: LOCAL_MULTI_WORKER
scheduling_mode: SERIAL_SINGLE_WORKER
security_domain: UNCLASSIFIED_LOCAL
trust_mode: LOCAL_DEV_UNSIGNED
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
  - TEST_DATA
  - CS
  - EV
  - RB
  - SURFACE
output_configuration:
  root: snapshot_mw
  artifacts:
    layer: PROTOCOL_BUILD_ROOT
    subpath: compiled/canonical
  conformance:
    layer: GOVERNANCE
    subpath: compiled/transform_conformance
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

