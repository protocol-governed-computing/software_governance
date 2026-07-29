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
- result_status and exit_reasons are mutually exclusive symbol sets

## Governance Rules

- Status symbols represent semantic outcomes, not data values
- Each capability contract declares which result statuses it may return
- Exit reasons represent workflow-level termination states only
- Additive changes preferred; removal requires migration planning

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
  - ACTIVE
  - CAP_REACHED
  - BACKEND_ERROR
  - SKIPPED
  - HALTED
  - TIMEOUT
exit_reasons:
  casing: UPPER_SNAKE
  entries:
  - COMPLETED
  - DUPLICATE_NONCE
  - EXITED
  - FAILED
  - HALTED
  - TIMEOUT
```
