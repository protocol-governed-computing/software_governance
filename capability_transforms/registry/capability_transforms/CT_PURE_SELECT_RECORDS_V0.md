# CT_PURE_SELECT_RECORDS_V0

## Human

### 1. Intent

Select the records of an array that satisfy declared field criteria, and answer none when none do.

---

### 2. Rationale

`CT_PURE_FILTER_RECORDS_V0` refuses an empty result. That is right where the caller expected to find something, and wrong for a read: "no record is in that state" is a true answer about what is held, not a failed lookup. A listing or a search that finds nothing must answer empty, and with only the filter it was refused.

This transform applies the same criteria and answers what matched, possibly nothing. Whether nothing matching is a problem is the caller's judgement. The filter stays for callers that mean "nothing matched" as a refusal.

---

### 3. Naming Convention

- **Operation:** SELECT_RECORDS (execution opcode used in molecules)

---

### 4. Applicability & Non-Applicability

#### 4.1 Valid Use Cases
- Answering a listing or a search from a CS store SELECT result, where nothing matching is an answer
- Selecting records by exact field value or field presence

#### 4.2 Invalid Use Cases
- Refusing when nothing matches (use `CT_PURE_FILTER_RECORDS_V0`)
- Selecting by complex expressions, ranges, or nested conditions
- Sorting or ordering records
- Reshaping or transforming record fields
- Domain-specific eligibility logic (that belongs in domain CC)

---

### 5. Determinism & Purity Declaration

| Property | Value | Notes |
|--------|------|------|
| Deterministic | YES | Same source and criteria yield same output |
| Purity Class | ct_pure | No side effects, no state |
| Side Effects | NONE | Fully pure computation |
| Replay Safe | YES | Identical inputs produce identical output |

---

### 6. Structural Checklist

Author MUST confirm all items before writing YAML:

- [x] Single responsibility
- [x] No implicit state
- [x] No domain semantics
- [x] Inputs fully declared
- [x] Outputs fully declared
- [x] No hidden control flow
- [x] Composition rules respected

---

### 7. Composition Rules (Atom-Specific)

As an **atom**, this CT:
- MUST NOT invoke other CTs (atoms or molecules)
- MUST perform exactly one atomic operation
- MAY be composed by molecules

---

### 8. Criterion Semantics

The `filter` input is a flat dict of field criteria applied with AND logic:

| Criterion Value | Semantic |
|----------------|---------|
| `"present"` | Field must exist in record and not be None |
| any other value | Field must equal that value exactly |

All criteria must be satisfied for a record to be included.

---

### 9. Validation Expectations

**Runtime validation MUST fail if:**
- `source` is not an array
- `filter` is not an object

An empty result is not a failure: it answers `extracted: []`.

---

### 10. Observability

This atom does NOT emit traces.

**Rationale:** Pure computation with no side effects or state changes.

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_SELECT_RECORDS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: capability_transforms
core:
  summary: Select the records satisfying declared field criteria, answering none when none do
  refusal: never
  description: Accepts a source array and a criteria object. Returns the records satisfying all
    criteria, possibly none. Raises CTExecutionError only on malformed inputs.
  inputs:
    source:
      type: array
      required: true
      description: Array of record objects to select from
    filter:
      type: object
      required: true
      description: Field criteria dict. Values are exact match or "present" for existence check.
  outputs:
    extracted:
      type: array
      description: The records satisfying all criteria, possibly none
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: SELECT_RECORDS
  implementation:
    module: capability_transforms.implementation.ct_pure_select_records_v0
    callable: execute
```