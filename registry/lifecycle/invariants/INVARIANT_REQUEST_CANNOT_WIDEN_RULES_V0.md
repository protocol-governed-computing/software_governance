# INVARIANT_REQUEST_CANNOT_WIDEN_RULES_V0

## Machine

```yaml
fqdn: lifecycle::INVARIANT_REQUEST_CANNOT_WIDEN_RULES_V0
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

A request that states rules of its own is judged by the business's rules. It is not refused for stating them, and it cannot widen them.

## 2. Why

Refusing a request for what it says would make the business's rules depend on the caller's wording. Honouring it would let the caller rewrite them.

## 3. How it is checked

The derive route checks each rule from the ledger's own values, never from the request, and cites this rule on each such check.
