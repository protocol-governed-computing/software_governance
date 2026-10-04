# INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V1

## Machine

```yaml
fqdn: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V1
artifact_kind: INVARIANT
version: V1
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: conformance
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - TEST_DATA
```

## Summary

Every assertion a vector's case makes uses a mode and a type drawn from a closed, declared vocabulary.
No implicit or ad-hoc assertion semantics are admitted.

## What this realizes

For every assertion `{field: spec}` in a case of a `TEST_DATA` artifact:

1. `spec.mode` MUST be present, and one of `exact`, `property`, `schema`.
2. Where `mode` is `property`, `spec.type` MUST be one of `hex_string`, `byte_length_range`, `non_zero`.
3. Where `mode` is `schema`, `spec.type` MUST be `json_schema`.
4. The fields a type requires MUST be present, and no field it does not declare may be.

| type | required | optional |
|---|---|---|
| hex_string | — | byte_length |
| byte_length_range | min, max | — |
| non_zero | — | — |
| json_schema | schema_ref | — |

`exact` is the default when a case states an expected value; an assertion exists for a field whose
value cannot be stated, such as what a non-deterministic step yields.

## Why this version

V0 stated the same vocabulary and declared itself enforced by a compiler phase that does not exist. The
check bound to it passed without reading a vector, so the rule could not refuse anything — the one
property a rule must have. This version is enforced by a compiler assertion that reads every case's
assertions and refuses an unknown mode, an unknown type, a missing required field or an undeclared one.
