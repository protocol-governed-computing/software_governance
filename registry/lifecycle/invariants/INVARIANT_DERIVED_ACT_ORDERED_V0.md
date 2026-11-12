# INVARIANT_DERIVED_ACT_ORDERED_V0

## Machine

```yaml
fqdn: lifecycle::INVARIANT_DERIVED_ACT_ORDERED_V0
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
  - WF
```

---

## 1. Claim

An act derived from decisions authorizes, validates, checks what must hold, claims, writes, and records its trail last. After the first claim that can refuse, nothing else refuses: every later claim is checked first.

## 2. Why

A refusal after a claim leaves the claim taken and the act refused, a state no decision asked for. Recording first would record moments that did not happen.

## 3. How it is checked

The derive route orders every component it composes by this rule, and cites it on each row it orders.
