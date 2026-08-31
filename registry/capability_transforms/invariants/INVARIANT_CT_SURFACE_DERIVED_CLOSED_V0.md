# INVARIANT_CT_SURFACE_DERIVED_CLOSED_V0

## Machine

```yaml
fqdn: capability_transforms::INVARIANT_CT_SURFACE_DERIVED_CLOSED_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: capability_transforms
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - CT
  - CC
```

---

## Purpose

Close a domain's capability-transform surface **by derivation rather than by enumeration**: every
transform a domain declares is invoked by a capability contract of that domain, and every transform
one of its contracts invokes is declared where it can be resolved.

## Why this exists beside `INVARIANT_CT_SURFACE_CLOSED_V1`

The platform closes its own surface with an allow-list, which is right: the platform's transform
universe is a deliberate, enumerated set, and a list is how you state a deliberate set.

**A domain's surface cannot be closed the same way.** The allow-list belongs to the artifact that
carries it, so importing the platform's invariant into a domain asserts the *platform's* list against
that domain's transforms — which is not the domain's surface and would refuse every transform the
domain legitimately declares. So the platform's invariant scopes itself to `PLATFORM`, and for a
while nothing closed a domain surface at all: a workload's own closure invariant was withdrawn when
the governance chain was closed, because no constitution named it, and **nothing would have refused a
third transform being added to that domain.** The property held as a fact and was enforced by nothing.

A domain must not author its own invariant to fix that — an invariant no constitution names is
exactly what the governance chain refuses. So the closure must be stated once, by the platform, in a
form that does not name any domain.

**That form is a quantification.** Closure is the equality
`declared == invoked`, evaluated within a domain, and neither side is a list anyone maintains:

- **declared** — the transforms the domain's own registry carries
- **invoked** — the transforms named by the pipeline steps of the domain's capability contracts

A list goes stale the moment a domain adds a transform. An equality does not, because both sides move
together or the build refuses.

## What it refuses

| Condition | Why it is refused |
|---|---|
| a declared transform no contract of the domain invokes | the surface is not enumerable — something executable exists that no act reaches, and nothing constrains what it may do |
| an invoked transform declared in neither the domain nor the imported platform surface | the contract names a capability that resolves nowhere |

## What it does not reach

**The platform's own surface.** Platform transforms are invoked by the domains that import them, not
by platform contracts, so the equality does not hold there and is not asserted there —
`INVARIANT_CT_SURFACE_CLOSED_V1` remains the platform's closure and is unchanged.

**Purity.** Whether a transform imports or invokes a side effect is
`INVARIANT_ATOM_OUTPUT_PURITY_V0`'s subject. This one is about the surface being closed, not about
what is on it.
