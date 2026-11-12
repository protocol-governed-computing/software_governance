# INVARIANT_ADMISSION_COVERS_BINDINGS_V0

## Machine

```yaml
fqdn: transport::INVARIANT_ADMISSION_COVERS_BINDINGS_V0
artifact_kind: INVARIANT
version: V0
governed_by: governance::CONSTITUTION_INVARIANTS_V0
authority: pgc.platform
concern: transport
core:
  enforcement_stage:
  - compiler_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - WF
```

---

## Purpose

A workflow's IN gate admits a payload against its declared input contract, and the workflow's nodes
read payload fields through their bindings. The two state one fact twice. Where a workflow binds a
field its gate does not declare, the gate admits a payload the workflow cannot resolve, and a gap in
the declaration surfaces as a runtime failure instead of a refusal at the boundary (`3a` EX-7).

---

## How it is checked
### Rule: Every bound payload field is declared by the gate

For each workflow whose start node is an IN gate, every field a node binds as `$.payload.<field>`
MUST be a key of that gate's `core.inputs`.

**Violation**:
```yaml
# IN_REQUEST_V0
core:
  inputs:
    name: {type: string, required: true}
# WF_REQUEST_V0
core:
  nodes:
    CC_RECORD_V0:
      inputs:
        email: $.payload.email    # the gate never declared `email`
```

---

## Scope

**Applies to**: every WF whose start node is an IN gate.

**Does NOT validate**: a field the gate declares and no node binds. A gate may require a field for
its own determination, or for accountability, without any step reading it; whether such a field is
a defect depends on what callers send, which a compiler cannot see.
