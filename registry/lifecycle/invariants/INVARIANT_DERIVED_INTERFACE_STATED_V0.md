# INVARIANT_DERIVED_INTERFACE_STATED_V0

## Machine

```yaml
fqdn: lifecycle::INVARIANT_DERIVED_INTERFACE_STATED_V0
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

A derived request carries the operation's inputs. An event carries what the ledger says it carries, or else the operation's identifying inputs, its actor and its time. Every derived component declares an output.

## 2. Why

An interface left to be inferred is filled in differently by each reader, and a component with no output cannot be routed on.

## 3. How it is checked

The derive route states every request, event and component interface it composes, and cites this rule where it supplies one the ledger does not name.
