# CONSTITUTION_ASSERT_V0

## Machine
```yaml
fqdn: conformance::CONSTITUTION_ASSERT_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: conformance
core:
  enforcement_model: process_and_compiler_enforced
  governs:
  - ASSERT
rules:
- applies_to: ASSERT
  enforced_by: conformance::INVARIANT_ASSERT_PARITY_V0
- applies_to: ASSERT
  enforced_by: conformance::INVARIANT_ASSERT_NOT_RUNTIME_REFERENCED_V0
- applies_to: ASSERT
  enforced_by: conformance::INVARIANT_ASSERT_CAPABLE_OF_REFUSING_V0
- applies_to: ASSERT
  enforced_by: conformance::INVARIANT_ASSERT_CAPABLE_OF_REFUSING_V0
```


---

## A declared check is capable of refusing

An obligation declaring that a violation fails the build has a check with a path that produces one.

**A check carrying nothing makes its obligation a claim.** Fourteen of eighty-seven checks on this
platform have no path that produces a refusal; ten say so in their own prose — *"Phase 1 stub — full
enforcement in Phase 3"* — enforcement described and never written. All fourteen declare that a
violation fails the build immediately, all fourteen run on every build, and all fourteen report
passed. A reader counting obligations concludes the platform is governed where it is not.

The relation between an obligation and its check is guaranteed by **derivation**: a check is
synthesized from every obligation whose declared stage is the build, so an obligation without a check
is impossible and a check without an obligation is impossible. That establishes existence and says
nothing whatever about capability, and until this rule nothing did.

**Two rules of this constitution named no carrier at all**, saying only that they were carried by
process. A rule carried by process is a rule carried by whoever remembers it.

## Two rules named no carrier, and now do

Both said only `PROCESS_ENFORCED` — carried by whoever remembers. Both now name
`conformance::INVARIANT_ASSERT_CAPABLE_OF_REFUSING_V0`, which carries the rule above.

**That obligation is `declared_not_enforced`**, which is the stage this change introduced for a rule
stated deliberately and carried by nothing yet. Arming it would refuse every build today, on fourteen
obligations owned by six subdomains of which five are not this one. Each restates its own; then the
stage moves and the count of unenforced obligations becomes readable.

**Authoring it found something the design missed.** `enforcement_capability` named the vocabulary of
stages and stopped one artifact short of the description that would admit them: the schema governing
an obligation closed its `core` surface over exactly three fields and its stage list carried neither
new value. The vocabulary was authored and nothing could use it. That schema now admits both stages
and the destination field, which is what made this obligation writable.

## Capability is what can be decided, not what would be ideal

The rule is *the check has a path that produces a refusal*. It is **not** *the check has a path this
obligation can reach*.

The first is a property of one artifact and decidable from it. The second is a relation between a
check and its obligation, established once by reading — a check whose only refusal path guards its
own inputs rather than its obligation — and not decidable in general. Requiring the second would
demand what no author could supply, so the count of fourteen is a floor and is stated as one.

---

## 1. Purpose

Defines the canonical structure and semantics of **ASSERT artifacts**.

An ASSERT evaluates an INVARIANT and produces violations.

ASSERT execution occurs during compiler validation.

---

## 2. Core Model

```text
INVARIANT → declares constraint
ASSERT    → evaluates constraint
COMPILER  → enforces constraint
```

## 3. Core Principles

### 3.1 Mandatory Binding

Every ASSERT MUST enforce exactly one INVARIANT.

### 3.2 Compiler Execution Only

ASSERT MUST execute in compiler validation phase.

ASSERT MUST NOT execute in:
- CT pipeline
- CS pipeline
- workflow runtime

### 3.3 Purity

ASSERT MUST be:
- pure
- deterministic
- side-effect free

### 3.4 Fail-Fast

Any violation MUST cause compilation failure.
No warnings. No partial success.

### 3.5 Explicit Output

ASSERT MUST return violations array.

## 4. Required Fields (Documentation)

```yaml
fqdn: <namespace>::ASSERT_<NAME>_V<N>
artifact_kind: ASSERT
version: V<N>
governed_by: conformance::CONSTITUTION_ASSERT_V0

enforces: INVARIANT_<NAME>_V<N>

core:
  summary: <one-line>
  description: <detailed description>

inputs: {}

outputs:
  violations:
    type: ARRAY
    element_type: ConformanceViolation
    required: true

logic:
  description: <evaluation logic>

purity:
  pure: true
  side_effects: NONE
  deterministic: true
```

## 5. Output Contract (Documentation)

```yaml
violations:
  - artifact_fqdn: <string>
    violation_code: <string>
    message: <string>
    severity: CRITICAL
```

## 6. Binding Contract

### 6.1 Required

ASSERT.enforces MUST reference exactly one INVARIANT.

### 6.2 Consistency Rule

ASSERT.enforces MUST match INVARIANT.enforced_by.

### 6.3 Illegal States

System MUST fail if:
- ASSERT has no INVARIANT
- ASSERT references missing INVARIANT
- mismatch exists

## 7. Execution Model

Compiler MUST execute:
Discovery
→ Parse
→ Validation
→ ASSERT
→ Materialization

## 8. Enforcement Semantics

```python
for assert in ASSERTS:
    result = evaluate(assert)
    if result.violations:
        FAIL_BUILD(result.violations)
```

## 9. Forbidden Behavior

- ASSERT in CT pipeline
- ASSERT in runtime
- ASSERT with side effects
- ASSERT without violations output

## 10. Naming

`ASSERT_<CONSTRAINT>_V<N>`

## 11. System Guarantees

No violation survives compilation.

## 12. Constitutional Violations

- missing enforces
- impurity
- missing violations output
- runtime execution

## 13. One-Line Truth

ASSERT makes invariants enforceable.

---

## What this realizes
```yaml
core:
  description: 'Governs ASSERT — the compiler-derived executable projection of an INVARIANT. ASSERT is
    NOT a hand-authored artifact: the compiler synthesizes ASSERT_X from INVARIANT_X at governance time
    (S4), binding a handler by convention (handlers.assert_<stem>) or an invariant `assert_projection.handler`
    override, and drawing check parameters from the invariant''s `assert_projection`. Covers binding,
    purity, compiler-only execution, and violations output.

    '
  derivation:
    authored: false
    derived_from: INVARIANT
    rule: ASSERT_X is the executable projection of INVARIANT_X; parameters come from the invariant's assert_projection
      block
rules:
- rule_id: ASSERT_BINDS_ONE_INVARIANT
  constraint: every ASSERT MUST enforce exactly one INVARIANT
- rule_id: ASSERT_COMPILER_ONLY
  constraint: ASSERT MUST execute during compiler ASSERT phase only; never at runtime
- rule_id: ASSERT_PURITY
  constraint: ASSERT MUST be pure, deterministic, and side-effect free
- rule_id: ASSERT_VIOLATIONS_OUTPUT
  constraint: ASSERT MUST return violations array; missing output is a constitutional violation
```
