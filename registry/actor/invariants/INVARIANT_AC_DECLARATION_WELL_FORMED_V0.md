# INVARIANT_AC_DECLARATION_WELL_FORMED_V0

## Machine

```yaml
fqdn: fb.actor::INVARIANT_AC_DECLARATION_WELL_FORMED_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.actor::CONSTITUTION_ACTOR_IDENTITY_V0
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    level: ERROR
    order: 20
  applies_to_kinds:
  - AC
```

---

## Purpose

An actor declares who execution runs as. It is an identity declaration and nothing else: the moment an actor can carry execution logic, routing, or side effects, identity becomes a place to hide behaviour.

---

## Validation Rules

### Rule 1: Type declared

Every AC MUST declare a non-empty `core.type`.

### Rule 2: Attributes typed

Every entry under `core.attributes` MUST declare an explicit `type`. Schemaless attributes are inadmissible.

### Rule 3: Identity only

An AC MUST NOT declare execution, routing, or side-effect surface. The forbidden keys are `implementation`, `pipeline`, `steps`, `operations`, `side_effects`, `transforms`, `bindings`, `next`, and `on_result`, at any depth.

### Rule 4: Identity governed

Attribute values MUST be literal declarations. A runtime path expression (`$.…`) makes identity a function of execution state rather than a compile-time governed fact.

---

## Rationale

Identity resolved at compile time is identity that can be reasoned about before anything runs. Ambient or inferred identity cannot be audited, because the thing being audited does not exist until the run does.
