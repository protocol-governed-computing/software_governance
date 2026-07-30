# INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0

## Machine

```yaml
fqdn: fb.governance::INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.governance::CONSTITUTION_GOVERNANCE_V0
core:
  enforcement_stage:
  - compiler_meta_validation
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  enforcement:
    level: ERROR
    order: 5
    phase: meta_validation
  applies_to_kinds:
  - CONSTITUTION
  - INVARIANT
```

---

## Purpose

A constitution rule that names an enforcing invariant makes a claim: *this rule is enforced, and here is what enforces it.* An invariant that exists makes the reverse claim: *some constitution declared the rule I enforce.* Neither claim was checked. A rule could bind to an invariant that does not exist, and an invariant could enforce a rule no constitution ever declared.

This invariant closes the governance chain in both directions, so that a declaration is authoritative rather than decorative.

---

## Validation Rules

### Rule 1: Forward resolution

Every `rules[].enforced_by` FQDN in a compiled CONSTITUTION MUST resolve to a compiled INVARIANT, and that invariant's derived ASSERT MUST have a registered handler.

The non-compiler sentinels `PROCESS_ENFORCED` and `RUNTIME_ENFORCED` are terminal: they declare that enforcement is deliberately outside the compiler, and are not resolved further. Their admissibility is governed by the constitution's `core.enforcement_model` and enforced by `SCHEMA_CONSTITUTION_V0`.

### Rule 2: Reverse closure

Every compiled INVARIANT MUST be named by at least one constitution rule. An invariant no constitution declares is an orphan: it enforces a rule that was never constitutionally established.

---

## Scope

Evaluated against the compiled graph of the current build. A domain build carries no CONSTITUTION or INVARIANT nodes — governance imports are resolve-only — so both rules are vacuous there and total in a platform build. A platform constitution is therefore never required to name a domain invariant.

---

## Rationale

**A governance relationship that is not verified is not a governance relationship.**

The chain `CONSTITUTION → INVARIANT → ASSERT → HANDLER` is the platform's entire enforcement pathway. Verifying it forward proves that every declared rule has a mechanism; verifying it backward proves that every mechanism has a mandate. Together they make the constitution surface authoritative: what it declares is what the compiler enforces, and what the compiler enforces is what it declares.
