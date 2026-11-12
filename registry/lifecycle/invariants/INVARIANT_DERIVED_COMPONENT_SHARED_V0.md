# INVARIANT_DERIVED_COMPONENT_SHARED_V0

## Machine

```yaml
fqdn: lifecycle::INVARIANT_DERIVED_COMPONENT_SHARED_V0
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
  - CC
```

---

## 1. Claim

A derived design has one component per thing and purpose, and every workflow that needs it runs that one.

## 2. Why

Two components doing one job drift apart, and a change made to one leaves the other behaving as before.

## 3. How it is checked

The derive route keys each component it composes by thing and purpose, and reuses the one it has.
