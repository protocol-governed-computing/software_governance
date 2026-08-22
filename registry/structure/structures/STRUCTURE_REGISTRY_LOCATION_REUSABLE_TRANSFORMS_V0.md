# STRUCTURE_REGISTRY_LOCATION_REUSABLE_TRANSFORMS_V0

Registry location declaration for REUSABLE_TRANSFORMS layer.

## Header

- **Artifact Code:** STRUCTURE_REGISTRY_LOCATION_REUSABLE_TRANSFORMS_V0
- **Artifact Kind:** structure
- **Governed By:** structure::CONSTITUTION_STRUCTURE_V0
- **Version:** V0
- **Status:** canonical
- **Authority:** foundational

---

## Purpose

Declares the physical registry module location for REUSABLE_TRANSFORMS layer artifacts. This artifact enables federated ownership of registry locations while maintaining deterministic resolution.

**Constitutional Rule**: Each layer owns exactly one registry location artifact.

---

## Machine

```yaml
fqdn: structure::STRUCTURE_REGISTRY_LOCATION_REUSABLE_TRANSFORMS_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
# The shared mechanism every domain composes with. Declared here because a reusable
# layer has no build manifest of its own, and substrate that declares nothing would
# have to have its eligibility inferred.
structure_scope: capability_transforms
reuse_visibility: substrate
core:
  layer_code: REUSABLE_TRANSFORMS
  description: 'Platform capability transforms (CT artifacts). Pure, deterministic, side-effect-free functions.

    '
  notes: 'Pattern-based resolution: module_path_pattern defines how to compose registry path. No domain
    composition for platform transforms layer.

    '
output_configuration:
  artifacts_path:
    layer: REUSABLE_TRANSFORMS
    subpath: compiled/artifacts
  molecules_path:
    layer: REUSABLE_TRANSFORMS
    subpath: compiled/molecules
```

---

## Usage

Loaded by artifact discovery during build:

1. Discovery reads `STRUCTURE_LAYER_AUTHORITY_V0` → enumerates layers
2. For REUSABLE_TRANSFORMS layer → loads this artifact
3. Extracts `registry_module: pgs_transforms.registry`
4. Scans that module for protocol artifacts

---

## Version History

- **V0**: Initial federated registry location (2026-03-25)
  - Extracted from central STRUCTURE_LAYER_REGISTRY_LOCATIONS_V0
  - REUSABLE_TRANSFORMS layer now owns its registry location
  - Moved to central pgs_governance namespace (2026-03-26)
