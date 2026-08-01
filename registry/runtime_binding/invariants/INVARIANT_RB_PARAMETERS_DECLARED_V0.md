# INVARIANT_RB_PARAMETERS_DECLARED_V0

Architectural Invariant

## Machine

```yaml
fqdn: fb.runtime_binding::INVARIANT_RB_PARAMETERS_DECLARED_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - RB
```

## Summary

A runtime binding declares the template parameters its policies expand at runtime:

```yaml
parameters:
  - module_data_root
core:
  bindings:
    capability_side_effects::CS_REGISTRY_V0:
      policy:
        path: "{{module_data_root}}/ai_governance/ai_licensing/license_registry.json"
```

The template is load-bearing — the compiler emits it unchanged and the runtime expands it against
the supplied data root. The `parameters` list is the binding's *declaration* of what it requires,
and nothing consumed it, so it could disagree with the policies indefinitely without any signal.
A machine-block census flagged it as a key with no detected consumer, which is exactly what an
undetected drift looks like.

Two directions of disagreement, both silent before this invariant:

- A template with **no declared parameter** is an undeclared runtime requirement: the binding
  depends on a value its own contract never announces, so provisioning it correctly relies on
  reading the policy strings rather than the declaration.
- A declared parameter used by **no template** is a stale declaration: it claims the binding needs
  something it does not, which misleads anyone provisioning the runtime.

Neither breaks a build today, and both make the declaration untrustworthy. This invariant makes
`parameters` a checked contract rather than documentation that happens to be nearby.

## Rule

For every RB artifact:

1. Collect every `{{name}}` appearing in any value under `core.bindings`, at any nesting depth.
2. Collect every entry in the artifact's `parameters` list.
3. Every used template name MUST appear in `parameters`.
4. Every declared parameter MUST be used by at least one template.

An RB that declares no parameters and uses no templates is conformant — the rule constrains
agreement, not the presence of parameters.

## Anti-Patterns

- `undeclared_template`: a policy expands `{{x}}` while `parameters` omits `x`
- `stale_parameter`: `parameters` lists `x` while no policy expands `{{x}}`

## Enforcement

- **Stage:** compiler_assertion
- **Failure Mode:** FAIL_IMMEDIATELY

## Version History

- **V0**: Closes the drift between an RB's declared parameters and the templates its binding
  policies actually expand.
