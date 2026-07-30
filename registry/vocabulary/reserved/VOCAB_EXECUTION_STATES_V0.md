# VOCAB_EXECUTION_STATES_V0 — Execution Semantics

**Governance Header**
- Vocabulary ID: fb.vocabulary::VOCAB_EXECUTION_STATES_V0
- Version: v0
- Governed By: fb.vocabulary::CONSTITUTION_VOCABULARY_V0
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

This artifact declares the **platform** outcome space — the statuses the platform compiler and
runtime interpret. A domain requiring a domain-specific outcome SHALL declare its own `VOCABULARY`
artifact in its own namespace, or map the outcome onto a platform status; it SHALL NOT add domain
symbols here.

---

## Machine

```yaml
fqdn: fb.vocabulary::VOCAB_EXECUTION_STATES_V0
artifact_kind: VOCABULARY
version: v0
governed_by: fb.vocabulary::CONSTITUTION_VOCABULARY_V0
result_status:
  casing: UPPER_SNAKE
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
  entries:
  - COMPLETED
  - EXITED
  - FAILED
  - TIMEOUT
```
