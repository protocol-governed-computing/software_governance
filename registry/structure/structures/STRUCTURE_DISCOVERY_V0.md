# STRUCTURE_DISCOVERY_V0

**Artifact Type**: STRUCTURE
**Version**: V0
**Status**: CANONICAL
**Authority**: CONSTITUTIONAL

---

## Purpose

Single source of truth for artifact discovery. Defines which layers are searched, how layer codes map to physical registry modules, and the rules governing artifact scanning.

---

## Machine

```yaml
fqdn: structure::STRUCTURE_DISCOVERY_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
core:
  summary: Consolidated artifact discovery configuration
  description: 'Single source of truth for artifact discovery, replacing fragmented registry location
    and layer authority discovery definitions.

    '
discovery:
  layers:
    GOVERNANCE:
      registry_module: software_governance.registry
      layer_category: platform
    REUSABLE_TRANSFORMS:
      registry_module: capability_transforms.registry
      implementation_namespace: transforms.atoms
      layer_category: platform
    REUSABLE_SIDE_EFFECTS:
      registry_module: capability_side_effects.registry
      layer_category: platform
    CAPABILITIES:
      registry_module: business_domains.registry
      layer_category: platform
    COMPILER:
      registry_module: protocol_compiler.registry
      layer_category: platform
    STRUCTURE:
      registry_module: protocol_compiler.structure
      layer_category: platform
    INGRESS:
      registry_module: protocol_transport.registry
      layer_category: platform
    EXECUTION:
      registry_module: protocol_runtime
      layer_category: platform
    BLOCKCHAIN:
      registry_module: business_domains.blockchain.registry
      module_path_pattern: '{registry_module}.{subdomain}'
      implementation_namespace: capability_transforms.atoms
      layer_category: domain
      allowed_subdomains:
      - identity
      - transaction
      - wallet
    AI_GOVERNANCE:
      registry_module: business_domains.ai_governance.registry
      module_path_pattern: '{registry_module}.{domain}'
      implementation_namespace: capability_transforms.atoms
      layer_category: domain
      allowed_domains:
      - ai_licensing
      - agent_governance
      - agent_admission
    TEST_DATA:
      registry_module: conformance_workloads.testbed.ct_test_data
      layer_category: platform
  rules:
    filename_pattern: ^(?P<type>TEST_DATA|[A-Z]+)_(?P<name>[A-Z0-9_]+)_V(?P<version>\d+)\.md$
    excluded_directories:
    - .git
    - __pycache__
    - node_modules
    - .venv
    - metadata
    format_precedence:
    - json
    - markdown
    format_extensions:
      json: .json
      markdown: .md
    resolution:
      method: importlib
      fallback: forbidden
    scope:
      type: platform_only
    validation:
      require_registry: true
      on_missing_registry: FAIL
    ordering:
      deterministic: true
```
