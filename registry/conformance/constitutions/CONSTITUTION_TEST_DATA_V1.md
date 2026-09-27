# CONSTITUTION_TEST_DATA_V1

## Machine
```yaml
fqdn: conformance::CONSTITUTION_TEST_DATA_V1
artifact_kind: CONSTITUTION
version: V1
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: conformance
core:
  enforcement_model: compiler_enforced
  governs:
  - TEST_DATA
rules:
- applies_to: TEST_DATA
  enforced_by: conformance::INVARIANT_TEST_DATA_MATCH_CT_OUTPUT_V0
- applies_to: TEST_DATA
  enforced_by: artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0
- applies_to: TEST_DATA
  enforced_by: conformance::INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V1
- applies_to: TEST_DATA
  enforced_by: conformance::INVARIANT_TEST_DATA_RECORDS_MATCH_PURITY_V0
```

---

## 1. Purpose

This constitution governs the **test vector** (`TEST_DATA`): the declaration that proves a capability
transform does what its declaration says. A transform's implementation lives outside the composition;
the composition vouches for the declaration and cannot vouch for the code. A vector closes that gap:
stated inputs, and what the transform must produce from them, run against the transform exactly as the
composition sealed it.

It replaces `conformance::CONSTITUTION_TEST_DATA_V0`, which admitted deterministic outputs only and
said nothing of molecules, of results recorded for steps that are not deterministic, of where vectors
run, or of what counts as proven.

---

## 2. What a vector is

- A vector names **one transform**, by its identity, and carries one or more **cases**.
- A case states the **bindings** the transform is handed, the **outcome** expected — `SUCCESS`, or
  `VIOLATION` for a transform expected to refuse — and what the result must be: **expected** values,
  field by field, or **assertions** on the form of a field whose value cannot be stated.
- Cases are governed content and live in the Machine block. Prose around a vector declares nothing.

---

## 3. What a vector proves

- **As sealed.** A case runs against the transform exactly as the composition sealed it, never against
  a copy or a reconstruction.
- **A molecule whole.** A vector for a molecule runs the whole molecule — every step, every pass of
  every loop — and proves what it yields.
- **Recorded results, exactly.** A case for a molecule states the **recorded** result of each of its
  non-deterministic steps, addressed by the path the runtime gives that step. The run substitutes the
  recorded result and never runs the step, so the expected result is exact, and the case is also a
  proof that a replay uses the record. A case supplies a recorded result for every non-deterministic
  step the molecule runs and for no deterministic one; a case for an atom supplies none.
- **Shape, for a step that is not deterministic.** A vector for a non-deterministic atom on its own
  asserts the form of what it yields and never its values. Its values are proven where it is used, in
  the molecule that consumes it.

---

## 4. Where vectors run, and what counts as proven

- **In the supplying domain's build.** A transform's implementation belongs to the domain that supplies
  it, so its vectors run in that domain's build, after the domain compiles and before it is assembled —
  never in the platform's own build.
- **On every build.** The composition seals a transform's declaration and not its code, so only running
  the vectors shows the code still does what the declaration says. No earlier result stands for a later
  build.
- **Refused.** A domain with a failed case is not admitted to any composition.
- **Proven or unproven, never passing by default.** A transform whose every case ran and passed is
  **proven**. A transform no vector tests is **unproven**, and is named as such; it is never counted as
  passing. A result that reports success over nothing is a result about nothing.

---

## 5. Where vectors come from

A vector is authored in the design of the change that authors or amends its transform, and rendered by
construction like every other declaration. A vector written by hand beside the code is proof nobody
gated. The design language refuses a transform authored or amended without one.

---

## 6. What became of V0

**V0 was deleted, not superseded**, with the invariant that claimed enforcement by a compiler phase
that does not exist. Supersession keeps a predecessor compiled so that a claim discharged under it stays
evaluable, and a superseded invariant is still enforced. No vector was ever judged under V0, so there
is no claim to keep evaluable; and keeping the old invariant would have kept a check that passes
without reading anything — the defect this version removes. Their declarations remain in this
repository's history and in every composition deposited under them.

---

## What this realizes
```yaml
core:
  description: Governs test vectors — what a vector is, what it proves, where it runs, and what counts as proven
rules:
- rule_id: TD_ONE_TARGET
  constraint: a vector MUST name exactly one transform, by identity
- rule_id: TD_CT_OUTPUT_MATCH
  constraint: a case's expected outputs MUST be outputs its transform declares
- rule_id: TD_ASSERTION_FORMS_CLOSED
  constraint: a case's assertions MUST use a declared mode and type
- rule_id: TD_RECORDED_RESULTS_MATCH_PURITY
  constraint: a case MUST supply a recorded result for every non-deterministic step of what it tests and for no deterministic one
- rule_id: TD_RUN_AS_SEALED
  constraint: a case MUST run against its transform exactly as the composition sealed it
- rule_id: TD_RUN_EVERY_BUILD
  constraint: every vector MUST run in its supplying domain's build, on every build
- rule_id: TD_FAILURE_REFUSES
  constraint: a domain with a failed case MUST NOT be admitted to a composition
- rule_id: TD_UNPROVEN_NAMED
  constraint: a transform no vector tests MUST be reported unproven, and MUST NOT be counted as passing
```
