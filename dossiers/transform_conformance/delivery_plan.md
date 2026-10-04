# Delivery plan — transform_conformance

Authorized by Gate 1, closed at P6 against composition `54412f835e6d…`. Everything below lands on
`dev/17` as one delivery, in dependency order. No transform, contract or workflow changes, and no
domain artifact is edited: every domain builds as it does today and reports its transforms unproven.

## What the survey for this plan found

Three readers of a vector, three formats, none of them agreeing:

- **The compiler's case generator** reads cases from the document's prose — `### Case N:` headings
  with a YAML block under each — and silently skips a vector whose target it cannot find or whose
  transform has no sealed form.
- **The output-match assertion** reads `test_cases` from the Machine block and compares expected
  outputs against the output of *a capability contract it takes to be the transform's governor* — the
  first entry of the transform's `governed_by`, which in this composition is a constitution. Given a
  vector it would refuse it or skip it; it has never been given one.
- **The outcome-declared assertion** reads cases from the prose by pattern.

So the two invariants P6 reuses are sound as declarations, and their checks must be rewritten to read
one format. Cases in prose would also be refused by the human-block fidelity check, which holds that
prose declares nothing.

## 1. `software_governance` — the rules

| Item | Content |
|---|---|
| `registry/conformance/constitutions/CONSTITUTION_TEST_DATA_V1.md` | Supersedes V0. A vector names one transform by identity and tests it as sealed; a molecule is tested whole; a case states bindings, the expected outcome, expected outputs or shape assertions, and — for a molecule — the recorded results of exactly its non-deterministic steps, by the path the runtime addresses them; a non-deterministic atom on its own is asserted by shape only; a transform no vector tests is unproven, never passing; vectors run in the supplying domain's build, on every build. Rules name all four invariants below. |
| `CONSTITUTION_TEST_DATA_V0.md` | Marked superseded by V1. |
| `registry/conformance/invariants/INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V1.md` | Supersedes V0; `enforcement_stage: compiler_assertion`. |
| `INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0.md` | Marked superseded by V1. |
| `registry/conformance/invariants/INVARIANT_TEST_DATA_RECORDS_MATCH_PURITY_V0.md` | New. A case for a molecule supplies a recorded result for every non-deterministic step and for no deterministic one; a case for any other transform supplies none. |
| `registry/schema/SCHEMA_TEST_DATA_V0.json` | New. The Machine block of a vector: `target` and `cases[]` of `{case_id, expected_outcome, bindings, expected, assertions, recorded}`. Cases are governed content and live in the Machine block. |

## 2. `protocol_compiler` — build

| Item | Content |
|---|---|
| `stages/s7_materialize.py` | Read cases from the Machine block. Fail hard on a vector whose target does not resolve or has no sealed form, where it now skips. Carry `recorded` into the case. Write cases to the domain's declared conformance place. |
| Handlers | Rewrite output-match to compare against the target transform's declared outputs; rewrite outcome-declared to read the Machine block; implement assertion-mode (V1); add records-match-purity, which walks the sealed molecule for its non-deterministic step paths. |
| Tests | Each refusal on a vector built to trip it; a molecule's case carries its recorded results; an unresolved target stops the build. |

## 3. `protocol_runtime` — the runner

| Item | Content |
|---|---|
| `runtime/conformance.py` | Read cases from a domain's build output, never from the snapshot's conformance place. Hand each case's recorded results to the executor and confirm, through the step observer, that every supplied step was substituted and every supplied result was used. Report every transform of the domain proven, unproven or refused by name, with counts; a domain with no vector is reported, never passed. Write the result into the domain's build output. |
| `runtime/cli.py` | `runtime conformance <domain_root>`: exit 0 when nothing was refused, 1 otherwise. |
| Tests | A passing and a failing case; a molecule with a recorded non-deterministic step, run without calling it; a supplied result left unused refused; a domain with no vectors reported unproven. |

## 4. The domain's build step

`compile_domain.sh` invokes `runtime conformance` after the compile succeeds and exits non-zero when it
refuses. The `compiler` package still never imports the runtime; the build script composes two tools,
as the reference implementation's build did.

## 5. `snapshot_assembler` — evidence

| Item | Content |
|---|---|
| `assembler/core.py` | Carry each domain's conformance result into the snapshot at a place of its own, beside and apart from `conformance/composition.json`, which does not move. Found already true in delivery: the assembler carries every compiled projection, so the result arrives at `transform_conformance/<domain>/` with no change. |
| Tests | The result is carried for each domain; composition evidence is where it was. |

## 6. `transformation` — design and construction

| Item | Content |
|---|---|
| P7 template, `design/p7_design_intent/rules.py` | A `test_vectors` register, one row per (transform, case, field): role (INPUT, EXPECTED, ASSERT, RECORDED), field or step path, value. `TRANSFORM_WITHOUT_VECTOR` refuses a transform in `new_artifacts` or amended in `existing_inventory` with no case; rules for roles, outcomes and well-formed values. |
| `design/families.py`, `build/render.py` | `TEST_DATA` becomes an authorable family; construction renders one vector per transform into the Machine block, and a domain's generated build manifest declares the vector layer and the conformance place when the domain has vectors. |
| Fixtures and corpus | The maintained fixture dossiers author transforms, so they gain vectors. |
| Re-seal | `emit_rule_sets.py`, recompile, rebuild fixtures and payloads; `tc phase meta` and `emit --check` green. |

## 7. `.github` — process

`regression.sh` runs each domain's build with conformance; the RUNBOOK records the expected result —
every domain's transforms named unproven, none refused — until a domain's own change gives them vectors.

## 8. Guidance and record

`delivery.md` and `closure.md` in this dossier; the conformance line of the RUNBOOK.

## 9. Acceptance

- `regression.sh --all` green; construction reproduces every existing artifact with zero field differences.
- Every domain's result names its transforms, all unproven, none refused.
- The compiler and runtime tests above pass, including a molecule proven with a recorded result and
  the step not run.

## 10. Decisions needed before editing

1. **Cases in the Machine block, not in prose.** Recommended: yes — the governed content lives where
   the compiler reads, and one format serves all three readers. The reference implementation's
   prose-case format is dropped; nothing in the composition uses it.
2. **Where the build step lives.** Recommended: `compile_domain.sh` runs conformance after compiling,
   so every way of building a domain proves it. The alternative, running it only from the regression,
   leaves a domain built by hand unproven and unreported.
3. **The fixture dossiers and construction acceptance.** Once a transform must have a vector, the
   maintained fixtures need vectors, and construction will render vector artifacts that the delivered
   `book_library_mgmt` registry does not have. Recommended: the fixtures gain vectors, and the
   acceptance harness compares only what the delivered registry carries, reporting rendered vectors as
   *not yet delivered* rather than as a difference — the delivered domain gains them in its own change.
4. **Whether a domain's result is part of the snapshot's identity.** Recommended at Gate 1: carried as
   evidence and kept out of the identity, as composition evidence is. **Amended during delivery:** the
   result is part of the identity. The snapshot's identity covers every file it carries, and excludes
   only what is written after sealing and names the snapshot — which a domain's result, written by the
   domain's build before assembly, does not. In an admitted build the result follows from the
   declarations alone, because a build with a failing case is never assembled, so including it adds no
   instability; excluding it would be the carve-out the identity's totality refuses. The snapshot
   therefore states what its domains proved, and the recommendation as first written misread which
   hash was meant.
