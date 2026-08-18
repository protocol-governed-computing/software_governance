# Invariant enforcement authority — a read-only evidence pass

Measurement before framing. Nothing was changed. This answers the first three questions a P0 on
enforcement authority has to answer, and deliberately stops before the fourth, which is a ruling.

## 1. Which mechanisms read these fields

`core.enforcement_stage` is read by **four**:

```
s4_govern.py:136                               gates ASSERT derivation entirely
assert_assert_parity_v0.py:61
assert_governance_declaration_resolves_v0.py:90
assert_runtime_invariant_wired_v0.py:53
```

`assert_projection` is read by **three**:

```
s1_extract.py:580                              carried through canonicalization
s4_govern.py:139                               supplies handler override and check parameters
assert_governance_declaration_resolves_v0.py:95
```

**The claim that `enforcement_stage` is read by one handler is false.** It appears in
`MACHINE_BLOCK_CLOSURE.md` §4 and was repeated in the workspace handoff. The first consumer above is
the consequential one: an invariant whose stage is `runtime_outcome` or `composition_conformance`
gets **no derived ASSERT at all**, so the field decides whether an invariant is compiler-enforced.

## 2. Duplicate, complementary, or contradictory

**Contradictory, on 43% of the artifacts that carry both.**

```
88 invariants
  both enforcement_stage and assert_projection.phase   14
  enforcement_stage only                               74
  phase only                                            0
  neither                                               0
```

Every invariant carries `enforcement_stage`. None carries `phase` alone. So `phase` is not an
alternative model — it is a second, partial spelling of the same distinction:

```
enforcement_stage            assert_projection.phase
  compiler_assertion    48     assert            6
  compiler_validation   37     validation        6
  compiler_meta_val…     2     meta_validation   2
  compiler_discovery     1
  composition_conform…   1
  runtime_outcome        0
```

The mapping is mechanical — strip `compiler_`. Of the 14 that declare both, **8 agree and 6 do
not**:

```
INVARIANT_SECURITY_DOMAIN_DECLARED_V0        compiler_validation      vs  assert
INVARIANT_EXECUTION_SCHEDULING_DECLARED_V0   compiler_validation      vs  assert
INVARIANT_EXECUTION_PLACEMENT_DECLARED_V0    compiler_validation      vs  assert
INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0    compiler_validation      vs  assert
INVARIANT_INSPECTION_BOUNDARY_COMPOSED_V0    composition_conformance  vs  assert
… and one more
```

The last is the worst of them. `composition_conformance` **gates the invariant out of ASSERT
derivation**, so it is not compiler-enforced at all — while its own `assert_projection.phase` says it
runs at the assert phase. Both statements are in the same machine block, and they cannot both be
acted on.

## 3. Which invariants are enforced where

- **87 of 88** declare a `compiler_*` stage and therefore derive an ASSERT that runs at every build.
- **1** (`composition_conformance`) is gated out of compile-time assertion by design, and is enforced
  by the assembler over the assembled snapshot.
- **0** declare `runtime_outcome`.

That last line is a finding in its own right. `assert_runtime_invariant_wired_v0` exists to check that
invariants tagged `runtime_outcome` are bound to a real runtime path. **No invariant carries the
tag.** The handler runs on every build, matches nothing, and reports clean — a check guarding an empty
set, inside the enforcement machinery.

## What this changes about the question

The proposed framing was *declared doctrine that no mechanism reads*. The evidence does not support
it. What the evidence supports is narrower and more awkward:

1. **A dimension that does not discriminate.** 88 authored values, one consequential distinction.
2. **A second, partial spelling of it** on 14 artifacts, disagreeing with the first on 6.
3. **A handler enforcing an empty set.**

Those are three different defects with three different repairs, and only the second is urgent — a
contradiction inside one machine block is the condition the governance surface exists to refuse.

## Not answered here

- **Whether to enforce, migrate, demote or remove.** That is a ruling, and it should be made per
  defect rather than once for the field.
- **The tamperable acceptance test.** It cannot be written until the ruling names what the correct
  state is. Whatever is chosen, the test must be shown to fail on a document that violates it before
  it is trusted — a check nobody has seen fail is a check nobody has seen.
