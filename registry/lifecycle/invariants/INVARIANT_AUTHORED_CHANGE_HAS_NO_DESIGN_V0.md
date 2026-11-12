# INVARIANT_AUTHORED_CHANGE_HAS_NO_DESIGN_V0

## Machine

```yaml
fqdn: lifecycle::INVARIANT_AUTHORED_CHANGE_HAS_NO_DESIGN_V0
artifact_kind: INVARIANT
version: V0
governed_by: lifecycle::CONSTITUTION_CHANGE_MGMT_V0
authority: pgc.platform
concern: lifecycle
core:
  enforcement_stage:
  - enforced_elsewhere
  violation_response: FAIL_IMMEDIATELY
  enforced_by: the design compiler, refusing a design intent whose seed declares the change authored
assert_projection:
  applies_to_kinds:
  - WF
```

---

## 1. Claim

A change whose seed declares it authored has no design intent.

## 2. Why

Construction renders nothing an authored change delivers. A design intent for it would schedule a constitution, an invariant or the derive route's code to be rendered from registers that never held their content. Its dossier is complete at governance intent.

## 3. How it is checked

The seed declares how the change is delivered. A design intent whose seed declares the change authored is refused.
