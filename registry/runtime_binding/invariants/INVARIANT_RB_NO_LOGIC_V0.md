# INVARIANT_RB_NO_LOGIC_V0

## Machine

```yaml
fqdn: runtime_binding::INVARIANT_RB_NO_LOGIC_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: runtime_binding
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - RB
```

---

## Purpose

Keep runtime bindings as pure mapping declarations with no embedded programs.

---

## How it is checked
### Rule: No Conditional Logic

Binding config strings must not contain conditional expressions.

**Violation**:
```yaml
config:
  path: "{{env == 'prod' ? '/prod' : '/dev'}}/data"  # WRONG
```

**Correct**:
```yaml
config:
  path: "{{data_root}}/name_registry.json"  # Template substitution OK
```

### Rule: No Callable References

Binding config must not reference callables or function syntax.

**Violation**:
```yaml
config:
  resolver: "module.get_path()"  # WRONG
```

---

## Scope

**Applies to**: All RB artifacts

**Does NOT restrict**: Template variable substitution ({{var}} patterns)

---

## What this realizes
```yaml
core:
  description: 'RB artifacts must contain no execution logic. Binding configuration values must be static
    declarations — strings, numbers, booleans, lists, or maps. Template variable substitution ({{var}})
    is permitted. Conditional expressions, callable references, and dynamic evaluation are forbidden.

    '
  anti_patterns:
  - conditional_expression: Binding value contains if/else or ternary logic
  - callable_reference: Binding value contains function call syntax
  - dynamic_evaluation: Binding value uses eval-style expression beyond {{var}} substitution
  clarification:
    template_variables_ok: '{{var}} style parameter substitution is permitted and expected. It is static
      substitution, not logic evaluation.

      '
    logic_belongs_in_ct_cs: Any computation required to derive a configuration value must be performed
      in a CT artifact, not inlined into an RB declaration.
```
