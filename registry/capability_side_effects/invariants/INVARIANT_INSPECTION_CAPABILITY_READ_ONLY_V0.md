# INVARIANT_INSPECTION_CAPABILITY_READ_ONLY_V0

Architectural Invariant

## Machine

```yaml
fqdn: capability_side_effects::INVARIANT_INSPECTION_CAPABILITY_READ_ONLY_V0
artifact_kind: INVARIANT
version: V0
governed_by: capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
authority: pgc.platform
concern: capability_side_effects
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - CS
```

## Summary

**Whenever a workflow requires observation of the assembled system, it observes through a governed
snapshot capability.** Not by reading compiled projections, not by importing the compiler that
produced them, and not by discovering a path — through a declared capability whose subject is bound
by a runtime binding.

That rule is only load-bearing if an inspection capability cannot change what it observes. Two
things follow, and this invariant enforces both:

- A workflow executing from a sealed snapshot must not be able to alter that snapshot. A mutating
  "inspection" capability would make the sealed composition writable from inside its own execution.
- Evidence gathered by a capability that could rewrite its subject is not evidence. A phase that
  records "confirmed against the snapshot" is making a claim that depends entirely on the
  observation having been passive.

The capability's *subject* must also be bound rather than discovered. A capability that located its
own snapshot could answer truthfully about a composition other than the one it was asked about,
which is the same failure wearing a more convincing disguise.

## What this realizes
For every CS artifact declaring `core.category: inspection`:

1. No declared operation may name a mutating verb (`WRITE`, `DELETE`, `APPEND`, `UPDATE`, `PUT`,
   `SET`, `CREATE`, `REMOVE`, `REGISTER`, `DEREGISTER`, `DRAIN`, `CLEAR`, …).
2. Every declared operation must be `idempotent: true` — observing the same snapshot twice gives
   the same answer.
3. `core.semantics.durability` must be `read_only`.
4. `core.configuration_schema` must declare `snapshot_root` — the subject is bound, never
   discovered.

## Anti-Patterns

- `mutating_inspection`: an inspection capability declaring a write-class operation
- `non_idempotent_observation`: an inspection operation not declared idempotent
- `discovered_subject`: an inspection capability with no bound `snapshot_root`

## Enforcement

- **Stage:** compiler_assertion
- **Failure Mode:** FAIL_IMMEDIATELY

