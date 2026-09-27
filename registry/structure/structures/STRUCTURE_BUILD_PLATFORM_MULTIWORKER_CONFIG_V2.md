# STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V2

The same governance surface, composed for multi-worker placement.

A build configuration names exactly one arrangement per selectable boundary, so two
compositions differing in placement are two configurations. That is the shape rather than a
duplication to be factored away: a configuration *is* the definition of a composition, and the
surface it draws from is identical — what differs is one named mode, visible on one line.

Everything else here is deliberately the same as `STRUCTURE_BUILD_PLATFORM_CONFIG_V2`. Where the
two diverge in anything but placement, that divergence is a defect: it would mean two
compositions claiming one surface and drawing different artifacts from it.

**Artifact Type**: STRUCTURE
**Version**: V2
**Status**: CANONICAL
**Governed By**: structure::CONSTITUTION_STRUCTURE_V0

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


**Change from V1:** V1 kept all implementation-layer conformance out of the platform's build, on
the ground that capability implementations are not platform-owned. That holds for a domain's
implementations and not for the platform's own transforms, which the platform supplies. V2 compiles
the platform's test vectors (`TEST_DATA`) and declares where their runnable cases are written, so the
platform's build proves its own transforms (`conformance::CONSTITUTION_TEST_DATA_V2` §4). It never
proves a domain's.

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
fqdn: structure::STRUCTURE_BUILD_PLATFORM_MULTIWORKER_CONFIG_V2
artifact_kind: STRUCTURE
version: V2
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

