# CONSTITUTION_TEST_DATA_V2

## Machine
```yaml
fqdn: conformance::CONSTITUTION_TEST_DATA_V2
artifact_kind: CONSTITUTION
version: V2
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

It replaces `conformance::CONSTITUTION_TEST_DATA_V1`, which placed every vector in a domain's build,
never in the platform's, and required every vector to come from a design. The platform supplies
transforms of its own, authored as the rest of its surface is, and V1 left them provable nowhere.

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

- **In the supplier's build.** A transform's vectors belong to whoever supplies its implementation,
  because what a vector proves is that supplier's code. A domain's transforms are proven in that
  domain's build. The platform's own transforms are proven in the platform's build — every platform
  build, since each composition is sealed on its own and states what it proved. The platform's build
  never proves a domain's transforms: it does not own their implementations.
- **After the compile, on every build.** Vectors run once the build compiles and before it is
  assembled. The composition seals a transform's declaration and not its code, so only running the
  vectors shows the code still does what the declaration says. No earlier result stands for a later
  build.
- **Own and carried.** A build carries a platform transform it uses and does not supply. What a build
  carried is a fact its compile records; a transform is never taken as a build's own, or as carried,
  by its name.
- **Refused.** A build with a failed case is not admitted to any composition, whoever supplies the
  transform the case tests.
- **Proven or unproven, never passing by default.** A transform whose every case ran and passed is
  **proven**. A transform no vector tests is **unproven**, and is named as such; it is never counted as
  passing. A result that reports success over nothing is a result about nothing.

---

## 5. Where vectors come from

A vector comes the way its transform does. A domain's transform is authored in the design of the
change that authors or amends it, and so is its vector: rendered by construction like every other
declaration, and the design language refuses a transform authored or amended without one. The
platform's transforms are authored by hand under the dossier that gates them, as the rest of the
governance surface is, and so are their vectors. Either way a vector is gated; a vector written beside
the code and gated by nobody proves nothing.

---

## 6. What became of V1

**V1 was deleted, not superseded.** A superseded version stays compiled, and V1 would have kept "never
in the platform's own build" in the surface beside a version that says the opposite. Nothing compiled
named V1: no vector existed under it. Its declaration remains in this repository's history and in every
composition deposited under it. V0 was deleted before it, with the invariant that claimed enforcement
by a compiler phase that does not exist.

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
  constraint: every vector MUST run in its supplier's build, on every build
- rule_id: TD_FAILURE_REFUSES
  constraint: a build with a failed case MUST NOT be admitted to a composition, whoever supplies the transform the case tests
- rule_id: TD_UNPROVEN_NAMED
  constraint: a transform no vector tests MUST be reported unproven, and MUST NOT be counted as passing
```
