# INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0

## Machine

```yaml
fqdn: surface_contract::INVARIANT_NO_UNDECLARED_BEHAVIOR_SURFACE_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: surface_contract
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  ci_override:
    level: ERROR
  enforcement:
    order: 10
    level: WARNING
    scope: ALL_ARTIFACTS
  applies_to_kinds:
  - WF
  - CC
  - CT
  - CS
```

---

## Enforcement Rules

### Rule 1: No Fallback Defaults for Protocol-Required Fields

**Violation Pattern**:
```python
# ❌ WRONG
value = config.get("protocol_required_field", "default_value")
```

**Correct Pattern**:
```python
# ✅ CORRECT
if "protocol_required_field" not in config:
    raise ValueError(
        f"PROTOCOL_INCOMPLETE: 'protocol_required_field' not declared in {artifact_code}. "
        f"Protocol artifacts must explicitly declare all required fields."
    )
value = config["protocol_required_field"]
```

### Rule 2: No Hardcoded Paths

**Violation Pattern**:
```python
# ❌ WRONG
output_path = "/abs/path/to/compiled/artifacts"
output_path = Path("domains/blockchain/outputs")
```

**Correct Pattern**:
```python
# ✅ CORRECT - Declared in STRUCTURE
output_path = paths.resolve_output_path(
    'build_manifest_path',
    structure_artifact,
    domain=domain
)
```

### Rule 3: No Implicit Domain Resolution

**Violation Pattern**:
```python
# ❌ WRONG - Lost domain information
layer_code = "DOMAINS"
layer_root = resolver.resolve_layer_root(layer_code)  # Which domain?
```

**Correct Pattern**:
```python
# ✅ CORRECT - Explicit domain binding
layer_code = "DOMAINS"
domain = extract_domain_from_path(artifact_source_path)
if not domain:
    raise ValueError("PROTOCOL_INCOMPLETE: domain required for DOMAINS layer")
layer_root = resolver.resolve_layer_root(layer_code, domain=domain)
```

### Rule 4: No Manual Path Traversal

**Violation Pattern**:
```python
# ❌ WRONG - Manual .parent calls
module_root = resolver.resolve_layer_root("COMPILER")
repo_root = module_root.parent
output_path = repo_root / "compiled" / "artifacts"
```

**Correct Pattern**:
```python
# ✅ CORRECT - Use LayerResolver API
output_path = resolver.resolve_output_path("artifacts", "COMPILER", structure)
```

### Rule 5: No Heuristic Selection

**Violation Pattern**:
```python
# ❌ WRONG - Filesystem heuristic
for path in module.__path__:
    if (Path(path).parent / "schemas").exists():
        return path  # Guessing based on filesystem
```

**Correct Pattern**:
```python
# ✅ CORRECT - Protocol-declared authority
for path in module.__path__:
    authority_artifact = Path(path) / "layers" / "STRUCTURE_LAYER_AUTHORITY_V0.md"
    if parse(authority_artifact).get("role") == "platform_root":
        return path  # Declared in protocol
```

---

## Clarification: Legal vs Illegal Fallbacks

### Illegal Fallbacks (Protocol-Required Fields)

Fields that SHOULD be declared in protocol artifacts:

**STRUCTURE artifacts**:
- `output_configuration` (required)
- `build_manifest_path` (required in output_configuration)
- `trace_output_path` (required in output_configuration)
- `artifact_discovery.search_roots` (required)

**Workflow artifacts**:
- `runtime_binding` (required - can be in WF or passed as parameter)
- `workflow_code` (required)
- `states` (required)

**Intent artifacts**:
- `core` (required)
- `core.workflow` (required)

**Runtime Binding artifacts**:
- `core.bindings` (required)

### Legal Fallbacks (Truly Optional Fields)

Fields that are genuinely optional:

- `optional_metadata` - Not protocol-required
- Static error message lookups - Not protocol data
- Runtime execution context defaults (e.g., `exit_reason or "COMPLETED"`) - Runtime values

**Test**: If removing the field would make the artifact invalid per constitution → illegal fallback. If field is supplementary → legal fallback.

---

## What this realizes
```yaml
examples:
  violation_1:
    code: '# ❌ WRONG - Fallback for protocol-required field

      output_config = structure.get(''output_configuration'', {})

      '
    fix: "# ✅ CORRECT - Fail hard if missing\nif 'output_configuration' not in structure:\n    raise ValueError(\"\
      PROTOCOL_INCOMPLETE: 'output_configuration' not declared\")\noutput_config = structure['output_configuration']\n"
  violation_2:
    code: '# ❌ WRONG - Manual path traversal

      module_root = resolver.resolve_layer_root("COMPILER")

      repo_root = module_root.parent

      output_path = repo_root / "testbed" / "outputs"

      '
    fix: "# ✅ CORRECT - Use STRUCTURE-declared path\noutput_path = paths.resolve_output_path(\n    'testbed_output_path',\n\
      \    structure_artifact,\n    domain=domain\n)\n"
  violation_3:
    code: '# ❌ WRONG - Lossy domain resolution

      layer_code = "DOMAINS"  # Lost which domain!

      '
    fix: "# ✅ CORRECT - Explicit domain binding\nlayer_code = \"DOMAINS\"\ndomain = extract_domain_from_path(artifact_source_path)\n\
      if not domain:\n    raise ValueError(\"PROTOCOL_INCOMPLETE: domain required for DOMAINS layer\"\
      )\n"
  legal_pattern_1:
    code: '# ✅ OK - Genuinely optional metadata

      metadata = artifact.get(''optional_metadata'', {})

      '
    reason: optional_metadata is not protocol-required, genuinely optional
  legal_pattern_2:
    code: '# ✅ OK - Static error message lookup

      message = ERROR_MESSAGES.get(code, DEFAULT_MESSAGE)

      '
    reason: Static mapping, not protocol data
extensions:
  error_codes:
  - PROTOCOL_INCOMPLETE: Required protocol field not declared
  - UNDECLARED_OUTPUT_PATH: Output path not declared in STRUCTURE
  - UNDECLARED_SIDE_EFFECT: CS runtime attempted undeclared I/O operation
  - DOMAIN_REQUIRED: Domain parameter required but not provided
  - REFERENCE_UNRESOLVED: Artifact reference does not resolve
core:
  description: 'All runtime behavior must originate from declared protocol artifacts. Eliminate fallback
    logic, heuristic resolution, and smart coding that makes implicit decisions outside protocol governance.

    '
  anti_patterns:
  - fallback_defaults_for_protocol_values: config.get('trace_output_path', 'default') when trace_output_path
      SHOULD be in STRUCTURE
  - hardcoded_paths: literal path strings outside STRUCTURE
  - implicit_domain: layer='DOMAINS' without domain field
  - manual_traversal: .parent navigation outside LayerResolver
  - heuristic_selection: filesystem checks to choose behavior
  clarification:
    illegal_fallback: config.get('required_protocol_field', 'default') → field MUST be in STRUCTURE
    legal_fallback: config.get('optional_metadata', {}) → truly optional field, not protocol-required
    rule: If STRUCTURE/WF/RB SHOULD declare it → fallback is illegal. If genuinely optional → fallback
      is OK.
non_enum_enforcement_stages:
- structure_resolution
- workflow_execution
- side_effect_execution
assert_projection:
  enforcement:
    failure_mode: HARD_FAIL
```
