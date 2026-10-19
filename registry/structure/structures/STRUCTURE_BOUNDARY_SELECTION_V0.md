# STRUCTURE_BOUNDARY_SELECTION_V0

## Machine

```yaml
fqdn: structure::STRUCTURE_BOUNDARY_SELECTION_V0
artifact_code: STRUCTURE_BOUNDARY_SELECTION_V0
artifact_kind: STRUCTURE
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: structure
contract:
  selectable_boundaries:
  - namespace: execution_placement
    names_mode_in: placement_mode
    declared_by_prefix: STRUCTURE_EXECUTION_PLACEMENT_
    declares_mode_in: placement_mode
  - namespace: execution_scheduling
    names_mode_in: scheduling_mode
    declared_by_prefix: STRUCTURE_EXECUTION_SCHEDULING_
    declares_mode_in: scheduling_mode
  - namespace: security_domain
    names_mode_in: security_domain
    declared_by_prefix: STRUCTURE_SECURITY_DOMAIN_
    declares_mode_in: security_domain
  - namespace: cryptographic_trust
    names_mode_in: trust_mode
    declared_by_prefix: STRUCTURE_CRYPTOGRAPHIC_TRUST_
    declares_mode_in: trust_mode
```

---

## Purpose

Names the boundaries whose mode a build selects, and where each side of that selection is written.

A **selectable boundary** is one where the governance surface declares several arrangements and a
composition may have only one. Placement is the worked example: a surface declares that single-node
and multi-worker execution are both available, and a build says which it is. Scheduling, security
domain and cryptographic trust have the same shape.

## Why this is declared and not coded

The compiler needs to know, for each such boundary, which build-configuration field names the mode
and which artifacts declare one. Holding that in the compiler would make the set of selectable
boundaries a property of a build tool — unversioned, unreadable from a composition, and extendable
by editing Python. The same argument the family makes about rule sets applies: a table that decides
what a build may choose is governance.

It is loaded the way `STRUCTURE_DISCOVERY_V0` and `STRUCTURE_IDENTITY_V0` are, and for the same
reason: the compiler is pointed at its own configuration rather than carrying it.

## What this does not decide

**Which modes are authorized.** That is each boundary's constitution, and nothing here may widen it.
A mode no structure declares resolves to nothing and the build refuses — which is how an
unauthorized mode fails, because a surface carries a structure only for a mode its constitution
admits.

**Which mode is active.** That is the build configuration, per build.

**Whether the composition ended up with one.** That is each boundary's own invariant, checked over
the composition after selection has run. Selection and verification are deliberately separate: the
first is what the compiler intended, the second is what the composition carries, and a mechanism
that only intended correctly would be trusted rather than checked.
