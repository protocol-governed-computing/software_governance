# INVARIANT_AUTHORITY_CONSTITUTED_V0

## Machine

```yaml
fqdn: federation::INVARIANT_AUTHORITY_CONSTITUTED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: federation
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  handler: pgs_governance.registry.handlers.assert_authority_constituted_v0
  scope:
    applies_to:
    - PLATFORM
  applies_to_kinds:
  - AC
  - CC
  - CONSTITUTION
  - CS
  - CT
  - EV
  - IN
  - INVARIANT
  - RB
  - SCHEMA
  - STRUCTURE
  - SURFACE
  - TE
  - TI
  - VOCAB
  - WF
```

---

## An authority named by artifacts and constituted by nothing is refused

Every distinct `authority` an artifact declares MUST be constituted by a declared constituting act:
a CONSTITUTION artifact declaring `constitutes_authority` with that value.

An authority that exists because artifacts name it is constituted by need, which `2e` CA-2 forbids —
an authority "MUST NOT be constituted by need, precedence, containment, naming, or classification."
This is the first of the two predicates `AUTHORITY_VS_CONCERN_RULING` obligates: a purported boundary
that cannot demonstrate distinct authority is not admitted as one.

It is deliberately not an allowlist. `2e` CA-3 and the ruling's clause 5 both refuse a whitelist —
the condition under which any authority may exist is what is enforced, and the number follows from
the semantics.
