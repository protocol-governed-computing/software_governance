# INVARIANT_TRANSPORT_TARGET_EXISTS_V0

## Machine

```yaml
fqdn: transport::INVARIANT_TRANSPORT_TARGET_EXISTS_V0
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
  - TI
  - TE
  - WF
```

---

## Purpose

Every transport ingress must have a verified, static invocation target. A TI_ artifact with
no declared target is a dead letter — a boundary with no destination. The compiler enforces
this at build time so the boundary never admits an unroutable request.

What a "target" is depends on the handler KIND, and the check is as strong as each kind
admits. `WF_INVOCATION` names `handler.workflow`, an artifact, so it is checked for
resolvability against the compiled set. `SNAPSHOT_READ` / `SNAPSHOT_QUERY` name
`handler.operation`, an Operation Identity belonging to the inspector's own internal registry
— which is in no compiled artifact set, and which the compiler cannot consult without
importing an implementation. For those kinds the enforced check is that the target is
**declared and static**; nothing stronger is claimed. The kind set is closed: an unrecognised
handler kind is a violation.

---

## Scope

**Applies to:** All TI_ artifacts, of every handler kind.

**Does NOT apply to:**
- TE_ artifacts (egress declares no invocation target)
- WF_ artifacts (workflows declare their own steps, not transport bindings)

---

## What this realizes
```yaml
core:
  description: 'Every TI_ artifact MUST declare an explicit, static invocation target for its
    declared handler kind, and where that target is an artifact it MUST exist in the compiled
    artifact set.

    Transport ingress is the system boundary. It must be fully closed at compile time: - The
    handler kind is one of the governed kinds (WF_INVOCATION, SNAPSHOT_READ, SNAPSHOT_QUERY) -
    The kind''s target field is declared (handler.workflow for WF_INVOCATION, handler.operation
    for the inspection kinds) - The target is static; no inference, no fallback, no request-time
    resolution - For WF_INVOCATION the declared workflow resolves to an existing WF artifact

    This invariant ensures no transport ingress point leads to a dead end. Every admitted request
    has a declared, verified destination.

    '
  anti_patterns:
  - missing_target_binding: 'TI artifact omits the target field its handler kind declares

      '
  - ungoverned_handler_kind: 'TI declares a handler kind outside the governed set

      '
  - unresolvable_workflow_ref: 'TI core.workflow declares a WF FQDN that does not exist in the snapshot

      '
  - dynamic_workflow_ref: 'TI core.workflow uses a runtime-computed reference ($ prefix)

      '
  - null_or_empty_workflow: TI core.workflow is declared but empty or null
```
