# VOCAB_EXECUTION_STATES_V0 — Execution Semantics

**Governance Header**
- Vocabulary ID: vocabulary::VOCAB_EXECUTION_STATES_V0
- Version: v0
- Governed By: vocabulary::CONSTITUTION_VOCABULARY_V0
- Status: Active

---

## Purpose

Defines execution outcome symbols: result statuses for node-level outcomes and exit reasons for workflow-level termination.

## Allowed Usage

- `result_status`: In `on_result` clauses, `result_status_contract.allowed` arrays, trace event `result_status` fields
- `exit_reasons`: In EXIT node `reason` field, `execution_end` trace events

## Prohibited Usage

- Must NOT be used as protocol identifiers
- Must NOT be used as node names or parameter names
- A `result_status` value must not be used where an `exit_reason` is required, or vice versa

## Governance Rules

- Status symbols represent semantic outcomes, not data values
- Each capability contract declares which result statuses it may return
- Exit reasons represent workflow-level termination states only
- The two sets are **scope-distinct, not disjoint**: `result_status` classifies a node outcome,
  `exit_reasons` classifies a workflow termination. The same word MAY appear in both when the
  outcome is meaningful at both scopes (a node may time out; a workflow may terminate on timeout).
  Each set independently closes its own scope.
- Additive changes preferred; removal requires migration planning

### Domain extension

This artifact is the **reserving declaration** for the outcome space — the statuses the platform
compiler and runtime interpret. A domain requiring a domain-specific outcome SHALL declare its own
`VOCABULARY` artifact in its own namespace, or map the outcome onto a declared status; it SHALL
NOT add domain symbols here.

Extension is authorized per category, by this artifact, and is machine-checked:

| Category | `domain_extensible` | Why |
|---|---|---|
| `result_status` | `true` | A CC may report a domain-specific outcome; the workflow routes on it. The platform does not need to interpret it. |
| `exit_reasons` | `false` | Terminal dispositions are interpreted by the runtime scheduler. A reason it cannot interpret has no meaning. |

An extending vocabulary declares `extends: vocabulary::VOCAB_EXECUTION_STATES_V0` and lists
only the categories it contributes to. Contributing to a category that is not
`domain_extensible: true` is a compile-time violation, as is a symbol colliding with
`VOCAB_LANGUAGE_CONSTRAINTS_V0.reserved_non_authorable`.

The compiled result is one **vocabulary closure** per build — reserved vocabulary plus imported
governance plus authorized extensions. There is no separate "domain vocabulary" that rules are
evaluated against; there is one closure, and every symbol rule is evaluated against it.

---

## Machine

```yaml
fqdn: vocabulary::VOCAB_EXECUTION_STATES_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: vocabulary
result_status:
  casing: UPPER_SNAKE
  domain_extensible: true
  entries:
  - SUCCESS
  - FAILURE
  - VIOLATION
  - ERROR
  - NOT_FOUND
  - ALREADY_EXISTS
  - BACKEND_ERROR
  - TIMEOUT
exit_reasons:
  casing: UPPER_SNAKE
  domain_extensible: false
  entries:
  - COMPLETED
  - EXITED
  - FAILED
  - TIMEOUT
```
