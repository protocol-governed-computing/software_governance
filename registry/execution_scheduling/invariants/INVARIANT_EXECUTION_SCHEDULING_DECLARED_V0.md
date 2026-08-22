# INVARIANT_EXECUTION_SCHEDULING_DECLARED_V0

## Machine

```yaml
fqdn: execution_scheduling::INVARIANT_EXECUTION_SCHEDULING_DECLARED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: execution_scheduling
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    scope: ALL_ARTIFACTS
  applies_to_kinds:
  - SNAPSHOT
  composition_check:
    rule: exactly_one
    subject: active execution scheduling contract
    selector:
      namespace: execution_scheduling
      artifact_type: STRUCTURE
      artifact_code_prefix: STRUCTURE_EXECUTION_SCHEDULING_
      where:
        status: active
```

---

## Purpose

This invariant makes the V0 scheduling contract load-bearing. It forces the compiler
to validate that execution scheduling legality is explicitly declared for every snapshot —
rather than assumed. In V0, `SERIAL_SINGLE_WORKER` is the declared and intentional
scheduling mode, not a default that was never articulated.

## What this realizes
For every compiled snapshot:
1. The compiler MUST scan `execution_scheduling/` for active contracts
2. Exactly one MUST be present
3. The active contract's scheduling mode MUST be materialized into `federation_profile.execution_scheduling`
4. Compile MUST fail if no contract is found or more than one is found

## Anti-Patterns

- `no_scheduling_contract`: Snapshot compiled without any scheduling contract present
- `multiple_active_contracts`: More than one scheduling contract marked active simultaneously
- `implicit_serial_assumption`: Runtime assuming serial execution without a governing declaration

## Enforcement

- **Stage:** compiler_validation
- **Failure Mode:** FAIL_COMPILE — no snapshot is produced if violated

---

## What this realizes
```yaml
core:
  rule: 'The compiler MUST locate exactly one active scheduling contract within FB_EXECUTION_SCHEDULING.
    Zero contracts is a missing declaration violation. More than one active contract is an ambiguity violation.

    '
  summary: Every compiled snapshot must declare exactly one active execution scheduling contract
assert_projection:
  enforcement:
    failure_mode: HARD_FAIL
```
