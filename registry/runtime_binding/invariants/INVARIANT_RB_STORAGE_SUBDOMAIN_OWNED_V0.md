# INVARIANT_RB_STORAGE_SUBDOMAIN_OWNED_V0

Architectural Invariant

## Machine

```yaml
fqdn: runtime_binding::INVARIANT_RB_STORAGE_SUBDOMAIN_OWNED_V0
artifact_kind: INVARIANT
version: V0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: runtime_binding
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - RB
```

## Summary

A binding names the storage description its own subdomain wrote. It never names another
subdomain's, because a description maintained by someone other than the owner of what it
describes is a second copy of one truth, and the second copy is the one nobody maintains.

## What this realizes
For every RB artifact declaring `core.storage_structure`:

1. The named structure MUST resolve to a STRUCTURE artifact in the composition.
2. The structure's owning subdomain MUST equal the binding's owning subdomain.

A binding that declares no `storage_structure` is out of scope: it binds capabilities that
address no records.

Ownership is read from the artifact's module organization, which is the same source the
composition uses everywhere else and is immutable for a given version.

## Where it applies
- **Artifact Types**: RB
- **Validation Phase**: ASSERT (Phase 5, compile-time, hard fail)
- **Enforced By**: ASSERT_RB_STORAGE_SUBDOMAIN_OWNED_V0

## Rationale

An act that needs records another subdomain owns has one workaround available today: describe
those records in its own storage description. It works, it needs nothing from the platform, and
every check passes — which is what makes it the easy wrong act. Two subdomains then declare where
one record lives, and nothing says which is authoritative.

This invariant closes that route. It does not grant the reach the workaround was standing in for —
that is a wider change, and this rule is what stops the wider change from being answered by copying
while it is still being made.

**What it does not check.** Whether two descriptions elsewhere in the composition name one record
is a question about the composition as a whole and belongs where descriptions meet, at assembly.
This invariant sees one binding at a time and holds the narrower, sharper statement: a binding
speaks for its own subdomain and no other.

---
