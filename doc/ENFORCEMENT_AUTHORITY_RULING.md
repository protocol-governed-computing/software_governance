# Invariant enforcement authority — the ruling

Three defects, three rulings, three tamperable tests. They are ruled separately because they are
different failures: one field is contradicted, one is coarse, one guards nothing.

## Defect 2 — the second spelling. Ruled: **remove.**

`assert_projection.enforcement.phase` is declared on 14 of 88 invariants, on none of them alone, and
is read by **nothing**. `s1_extract` carries it through canonicalization and `s4_govern` copies it
into the derived ASSERT frontmatter; no handler, no assembler phase and no runtime path ever branches
on its value. Its schema type is `{"type": "string", "minLength": 1}` — no enum, so no authored value
was ever wrong.

Against that, it disagrees with the field that does decide:

```
INVARIANT_INSPECTION_BOUNDARY_COMPOSED_V0    composition_conformance  vs  assert
INVARIANT_SECURITY_DOMAIN_DECLARED_V0        compiler_validation      vs  assert
INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0    compiler_validation      vs  assert
INVARIANT_EXECUTION_PLACEMENT_DECLARED_V0    compiler_validation      vs  assert
INVARIANT_EXECUTION_SCHEDULING_DECLARED_V0   compiler_validation      vs  assert
INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0       discovery + validation   vs  validation
INVARIANT_ASSERT_NOT_RUNTIME_REFERENCED_V0   compiler_assertion       vs  assert
```

The first is the one that matters: `composition_conformance` gates the invariant out of ASSERT
derivation entirely (`s4_govern.py:136`), so it is not compiler-enforced — while the same machine
block says it runs at the assert phase. A contradiction inside one machine block is exactly what the
governance surface exists to refuse, and here the surface authored it.

Migration is not available: there is nothing to migrate *to*, because the authoritative field already
carries the distinction and carries it more finely. Enforcing agreement would mean enforcing a
derived restatement — 14 authored copies of a value the compiler can compute. So: delete the key from
the 14 invariants and delete the property from `SCHEMA_INVARIANT_V0.json`.

**Tamperable test.** `assert_projection.enforcement` already declares `additionalProperties: false`.
Removing the `phase` property therefore converts every future `phase:` into a hard schema failure —
no new handler, no new invariant. The test is to re-add `phase: assert` to one invariant and show the
build fail, then remove it and show it pass. A schema constraint nobody has watched reject something
is a constraint nobody has watched.

## Defect 1 — the dimension that does not discriminate. Ruled: **keep; already bounded.**

88 invariants declare `core.enforcement_stage`; the compiler branches on one distinction — whether
any declared stage is in `{runtime_outcome, composition_conformance}`. The four `compiler_*` values
are, mechanically, one value.

They are not therefore worthless: they name which mechanism enforces the rule, and
`doc/rule_ownership.md` is written in those terms.

The repair first proposed here was to add the enum the schema lacked. **It lacked nothing.**
`core.enforcement_stage.items` already declares a closed six-value enum, and the probe below confirms
it bites. The field is not an unconstrained string; it is a bounded vocabulary that happens to
contain four values the compiler treats alike. Coarse consequence is not the same defect as absent
constraint, and only the first is true here.

So: **no change.** What this defect actually produced is knowledge — that the four `compiler_*`
values are documentation riding on an enforced vocabulary — and one probe that turns a believed
constraint into an observed one.

## Defect 3 — the handler guarding an empty set. Ruled: **keep, and make it fail once.**

`assert_runtime_invariant_wired_v0` checks that invariants declaring `runtime_outcome` are bound to a
real runtime path. No invariant declares it. The handler runs every build, matches nothing, reports
clean.

This is dormancy, not death. The check is the thing that would catch the first `runtime_outcome`
invariant authored without a wiring — which is precisely when nobody would be looking. Removing it
removes the guard at the moment before it is first needed. But a check that has never been observed
to fail is evidence of nothing, and this one has never been observed at all.

So: keep it, and probe it. The handler stays; what changes is that its refusal has been seen.

**And the probe found something the emptiness did not show.** The check is not merely waiting for a
subject — it is scoped away from where its subjects live. `INVARIANT_RUNTIME_INVARIANT_WIRED_V0`
declares `assert_projection.scope.applies_to: [PLATFORM]`, and `s1_extract.py:583` excludes any
scope-bearing invariant from a domain build's imported governance closure. Runtime business
invariants are authored in **domains**. So the check runs only in the build where such an invariant
would never be written, and is absent from every build where one might be.

The probe fires because it was authored into the platform surface, which is not where the real
subject would appear. That is a scope defect, not an enforcement defect. It is ruled below.

## Defect 4 — the mislabelled scope. Ruled: **one field deleted.**

The tempting reading is that `assert_projection.scope.applies_to` and the governance closure disagree
about which compilation space an invariant belongs to, and that closure admission must be rebuilt so
that scope selects *where* an invariant applies rather than *whether* it is admitted.

That reading does not survive contact with the field. `scope.applies_to` is not an applicability
axis; it is the **surface whose allowed-list the invariant carries**. Its authored vocabulary is
`{PLATFORM, WORKLOAD}` — there is no `DOMAIN` value — and only 4 of 88 invariants declare it:

```
INVARIANT_CT_SURFACE_CLOSED_WORKLOAD_V0  WORKLOAD  allowed_capability_transforms
INVARIANT_CS_SURFACE_CLOSED_V1           PLATFORM  allowed_capability_side_effects
INVARIANT_CT_SURFACE_CLOSED_V1           PLATFORM  allowed_capability_transforms
INVARIANT_RUNTIME_INVARIANT_WIRED_V0     PLATFORM  — no allowed-list
```

Three of the four carry an allow-list, and excluding those from a domain build is **correct**:
importing one would assert the platform's allow-list against domain artifacts. `s1_extract.py:585` is
doing its job. The odd one out is the fourth, which carries no allow-list at all — it borrowed a
surface-identity field to say "I am a platform concern", and the import filter read it as what it
actually means and dropped the invariant from every domain build.

So the repair is not to closure construction. It is to delete `scope.applies_to` from
`INVARIANT_RUNTIME_INVARIANT_WIRED_V0`. Its `applies_to_kinds: [WF, CC]` then intersects the
domain-instantiated kinds and the invariant is imported wherever its subjects live. The imported
closure goes from 74 members to 75.

**Changing the admission rule instead would have broken surface closure**, and probe F below is what
that looks like.

### Probes D–F

```
D  author an unwired runtime_outcome INVARIANT in a domain, compile the domain
     before the fix → S4_GOVERN fails on ASSERT_PROTOCOL_SURFACE_CLOSED_V0 only.
                      ASSERT_RUNTIME_INVARIANT_WIRED_V0 is silent — the false negative, observed.
     after the fix  → S4_GOVERN fails on ASSERT_RUNTIME_INVARIANT_WIRED_V0 — 1 violation.

E  admission census over the platform's canonical invariants
     72 admitted into a domain closure, 15 excluded;
     both surface-closure invariants still excluded, RUNTIME_INVARIANT_WIRED now admitted.

F  strip scope.applies_to from INVARIANT_CT_SURFACE_CLOSED_V1 — the generalised fix, applied to a
   genuine surface-closure invariant
     → domain build fails, ASSERT_CT_SURFACE_CLOSED_V1, 7 violations.
       The platform's allow-list, asserted against a domain that never declared it.
```

D is the one that matters. The same probe, on the same artifact, passes before the fix and fails
after it — so what changed is not the strictness of a check but whether the check was present at all.
F is the counterfactual: it shows that the exclusion rule is load-bearing for the three invariants
that legitimately carry a surface, and that the defect was never in the rule.

## Measurement of record

The evidentiary bridge from "this field looks redundant" to "this field has no authority". Taken
before any edit, over the 88 invariants in the platform surface.

```
invariants declaring core.enforcement_stage             88  (all)
invariants declaring assert_projection.enforcement.phase 14
invariants declaring phase alone                          0

distinct enforcement_stage values authored (6 in enum)
  compiler_assertion        49      compiler_discovery        1
  compiler_validation       36      composition_conformance   1
  compiler_meta_validation   2      runtime_outcome           0

consumers of core.enforcement_stage                       4   (one gates ASSERT derivation)
consumers of assert_projection.enforcement.phase          0   (canonicalized and copied, never read)
```

Of the 14 carrying both, 7 differ under a strict `strip("compiler_")` comparison. They are not one
kind of disagreement:

```
1  hard contradiction   INSPECTION_BOUNDARY_COMPOSED   composition_conformance vs assert
                        — gated out of ASSERT derivation while claiming the assert phase
4  substantive          SECURITY_DOMAIN, CRYPTOGRAPHIC_TRUST,
                        EXECUTION_PLACEMENT, EXECUTION_SCHEDULING   validation vs assert
1  spelling artifact    ASSERT_NOT_RUNTIME_REFERENCED   compiler_assertion vs assert
1  superset, not clash  IDENTITY_FQDN_CONSISTENCY       discovery+validation vs validation
```

Recording seven as seven contradictions would overstate the case. One is a contradiction; four are
disagreements; two are notation. All seven are moot, because nothing read the field.

## The probes, and what they showed

Each was authored, built, observed to fail, and reverted. A platform build — not a domain build:
`s4_govern.py:724` treats imported governance as asserter state, so schema conformance is evaluated
where the artifacts are authored.

```
A  re-add  enforcement.phase: assert     → S4_GOVERN  ASSERT_SCHEMA_CONFORMANCE_V0  1 violation
B  set     enforcement_stage: compiler_typo → S4_GOVERN  ASSERT_SCHEMA_CONFORMANCE_V0  1 violation
C  author  runtime_outcome invariant bound to a CC and WF that do not exist
                                          → S4_GOVERN  ASSERT_RUNTIME_INVARIANT_WIRED_V0  1 violation
```

A proves the loophole is closed by `additionalProperties: false` rather than by vigilance. B proves
the live authority was already a bounded vocabulary. C is the first observed refusal by
`assert_runtime_invariant_wired_v0` — and it required authoring the subject in the platform surface,
which is the scope defect recorded above.

## What is not ruled here

Whether `enforcement.order`, `level` and `scope` are read. They are outside the question that was
asked, and guessing about them here would repeat the error this pass exists to correct — the claim
that a field is unread, made without measuring.
