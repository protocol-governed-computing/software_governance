# WF_DEMO_COLLATZ_CONJECTURE_V0

## Header (Mandatory)

- **Artifact Code:** WF_DEMO_COLLATZ_CONJECTURE_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** v0
- **Status:** draft
- **Supersedes:** NONE
- **Dependencies:** IN_COLLATZ_INPUT_VALIDATED_V0, CC_COMPUTE_SEQUENCES_V0, CC_VERIFY_TERMINATION_V0

---

## 1. Intent

Reference workload: compute Collatz sequences and verify the conjecture holds for the input set —
demonstrating that the PGC runtime traverses an independently-authored domain graph with zero
domain knowledge. A recursive computation expressed as a finite, acyclic protocol DAG.

**Phase 1 (pure):** compute → verify. No persistence (the `CC_STORE_RESULTS` step and its platform
`CS_MUTABLE_JSON` dependency are added in Phase 2, which exercises cross-domain capability
consumption).

---

## 2. Execution Graph

```
IN_COLLATZ_INPUT_VALIDATED_V0
    ├─ ACK  → CC_COMPUTE_SEQUENCES_V0
    │            ├─ SUCCESS   → CC_VERIFY_TERMINATION_V0
    │            │                ├─ SUCCESS   → EXIT:CONJECTURE_PROVEN
    │            │                └─ VIOLATION → EXIT:CONJECTURE_VIOLATED
    │            └─ VIOLATION → EXIT:ERROR
    └─ NACK → EXIT:REJECTED
```

---

## Machine

```yaml
wf_code: WF_DEMO_COLLATZ_CONJECTURE_V0
version: v0
governed_by: fb.topology::CONSTITUTION_WORKFLOW_V0

subdomain: collatz
structure: fb.topology::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Compute and verify Collatz sequences — domain-blind PGC execution (pure, Phase 1)

  start_node: IN_COLLATZ_INPUT_VALIDATED_V0

  nodes:
    IN_COLLATZ_INPUT_VALIDATED_V0:
      type: IN
      code: IN_COLLATZ_INPUT_VALIDATED_V0
      next:
        ACK: CC_COMPUTE_SEQUENCES_V0
        NACK: EXIT_REJECTED

    CC_COMPUTE_SEQUENCES_V0:
      type: CC
      code: CC_COMPUTE_SEQUENCES_V0
      inputs:
        numbers: $.payload.numbers
      next:
        SUCCESS: CC_VERIFY_TERMINATION_V0
        VIOLATION: EXIT_ERROR

    CC_VERIFY_TERMINATION_V0:
      type: CC
      code: CC_VERIFY_TERMINATION_V0
      inputs:
        sequences: $.results.CC_COMPUTE_SEQUENCES_V0.sequences
      next:
        SUCCESS: EXIT_CONJECTURE_PROVEN
        VIOLATION: EXIT_CONJECTURE_VIOLATED

    EXIT_CONJECTURE_PROVEN:
      type: EXIT
      reason: COMPLETED

    EXIT_CONJECTURE_VIOLATED:
      type: EXIT
      reason: COMPLETED

    EXIT_REJECTED:
      type: EXIT
      reason: EXITED

    EXIT_ERROR:
      type: EXIT
      reason: FAILED
```
