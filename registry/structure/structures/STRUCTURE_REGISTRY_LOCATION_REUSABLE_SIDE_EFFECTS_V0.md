# STRUCTURE_REGISTRY_LOCATION_REUSABLE_SIDE_EFFECTS_V0

Registry location declaration for REUSABLE_SIDE_EFFECTS layer.

## Purpose

Declares the physical registry module location for REUSABLE_SIDE_EFFECTS layer artifacts. This artifact enables federated ownership of registry locations while maintaining deterministic resolution.

**Constitutional Rule**: Each layer owns exactly one registry location artifact.

---

## Machine

```yaml
fqdn: structure::STRUCTURE_REGISTRY_LOCATION_REUSABLE_SIDE_EFFECTS_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
# The shared mechanism every domain composes with. Declared here because a reusable
# layer has no build manifest of its own, and substrate that declares nothing would
# have to have its eligibility inferred.
structure_scope: capability_side_effects
reuse_visibility: substrate
core:
  layer_code: REUSABLE_SIDE_EFFECTS
  description: 'Platform capability side effects (CS artifacts). External I/O boundary modules (network,
    filesystem, database).

    '
  notes: 'Pattern-based resolution: module_path_pattern defines how to compose registry path. No domain
    composition for platform side effects layer.

    '
output_configuration:
  artifacts_path:
    layer: REUSABLE_SIDE_EFFECTS
    subpath: compiled/artifacts
```

---

## Usage

Loaded by artifact discovery during build:

1. Discovery reads `STRUCTURE_LAYER_AUTHORITY_V0` → enumerates layers
2. For REUSABLE_SIDE_EFFECTS layer → loads this artifact
3. Extracts `registry_module: pgs_side_effects.registry`
4. Scans that module for protocol artifacts

---

