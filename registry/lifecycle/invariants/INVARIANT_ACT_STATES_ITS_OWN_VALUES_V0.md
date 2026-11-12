# INVARIANT_ACT_STATES_ITS_OWN_VALUES_V0

## Machine

```yaml
fqdn: lifecycle::INVARIANT_ACT_STATES_ITS_OWN_VALUES_V0
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

An act states its own values: the rules it applies, the states it writes, the trail it records on, the moment it records and every value the business fixes. None is taken from a request.

## 2. Why

A value taken from a request lets the caller decide what the business decided, which is the leak the ledger exists to close.

## 3. How it is checked

The derive route binds every rule, state, trail, moment and fixed value to the design, never to the request, and cites this rule on each such binding.
