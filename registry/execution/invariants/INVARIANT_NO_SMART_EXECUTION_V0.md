# INVARIANT_NO_SMART_EXECUTION_V0

Architectural Invariant

## Machine

```yaml
fqdn: execution::INVARIANT_NO_SMART_EXECUTION_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: execution
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: protocol_runtime's testbed/pgc/test_no_smart_execution.py, which scans every runtime module
    that hands values to a transform or takes them back, and which the regression runs
assert_projection:
  applies_to_kinds:
  - WF
  - CC
  - CT
  - CS
```

## Summary

The runtime is a plain executor. It passes inputs to transforms and stores their outputs without
reading a type declaration as an instruction and without converting a value.

## What this realizes
For all execution code:
1. NO type-based input conversion (e.g., hex_string → bytes)
2. NO type-based output conversion (e.g., bytes → hex_string)
3. NO interpretation of CC type declarations as execution instructions
4. NO caching of type metadata for runtime decisions
5. Type declarations are checked, never used to convert

All canonicalization happens inside atom implementations.

## Where it applies
- **Code Layer**: the runtime's execution modules: the dispatcher, the scheduler and the CT executor
- **Enforcement**: the runtime's own test, run by the regression. The execution code is not part of
  any build, so no compiler stage can see it.

## Examples

### ✅ VALID - Plain Executor

```python
def adapter(ctx, step: dict):
    # Resolve inputs without type interpretation
    resolved_inputs = {}
    for key, value in step.items():
        if key in RESERVED_KEYS:
            continue
        resolved_inputs[key] = resolve_value(value)

    # Call atom - atom handles its own canonicalization
    result = execute_fn(inputs=resolved_inputs)

    # Store result without conversion
    ctx.set_value(step["as"], result)
```

### ❌ INVALID - Smart Executor

```python
# ❌ Type-based input conversion
input_types = load_contract_input_types(atom_code)
for key, value in inputs.items():
    if input_types[key] == "hex_string":
        inputs[key] = bytes.fromhex(value[2:])  # ❌ VIOLATION

# ❌ Type-based output conversion
output_types = load_contract_output_types(atom_code)
for key, value in result.items():
    if output_types[key] == "hex_string":
        result[key] = "0x" + value.hex()  # ❌ VIOLATION
```

## Rationale

Plain executors ensure:
- Single source of truth (atoms own their canonicalization)
- No hidden transformations
- Explicit type handling in atoms
- No executor-atom coupling via type metadata
- Constitutional principle: "Code is executor, not decision maker"

## Detection Strategy

The runtime test scans its execution modules for:
- Calls to `load_contract()` or type metadata loaders
- Conditional logic based on type names (if type == "hex_string")
- `.hex()` calls on values (output conversion)
- `bytes.fromhex()` calls on values (input conversion)
- `_OUTPUT_TYPES_CACHE` or similar type caching

`conformance.py` is outside the scan: it reads a vector's expected value against an assertion's
form, which judges a result and hands nothing to a transform. A planted conversion proves the scan
finds what it looks for.

## Related Artifacts

- `capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0` - Defines pure atom behavior
- `runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0` - Defines executor boundaries

---

## What this realizes
```yaml
core:
  rule: Runtime executors must pass inputs to transforms without type-based interpretation or conversion
  summary: Execution layer must not interpret type declarations or perform conversions
```
