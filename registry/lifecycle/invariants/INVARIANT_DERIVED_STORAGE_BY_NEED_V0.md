# INVARIANT_DERIVED_STORAGE_BY_NEED_V0

## Machine

```yaml
fqdn: lifecycle::INVARIANT_DERIVED_STORAGE_BY_NEED_V0
artifact_kind: INVARIANT
version: V0
governed_by: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
authority: pgc.platform
concern: lifecycle
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the design compiler's derive route, applying its sealed doctrine to a decision ledger
assert_projection:
  applies_to_kinds:
  - STRUCTURE
```

---

## 1. Claim

A derived design holds a thing's identity in a registry, a thing's records and states in a mutable store, and a part's trail in an append-only store, and no store for anything else.

## 2. Why

A store chosen by habit rather than by what is held lets an identity be overwritten, or a trail edited.

## 3. How it is checked

The derive route chooses each store from what the ledger says a thing holds, and cites this rule on each store row.
