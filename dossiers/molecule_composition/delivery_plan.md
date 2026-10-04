# Delivery plan — molecule_composition

Authorized by Gate 1, closed at P6 against composition `1b0cfbd3d094…`. Everything below lands on
`dev/17` as one delivery, in dependency order. Nothing existing changes: every transform in the
composition stays an atom under the existing constitution.

## 1. `software_governance` — the rules

| Item | Content |
|---|---|
| `registry/capability_transforms/constitutions/CONSTITUTION_MOLECULES_V0.md` | Steps run in declared order; a loop runs its body once per member of its collection, every pass; no molecule contains itself; a molecule's declared purity agrees with its steps; every step leaves one evidence record. States the partition with the existing constitution explicitly. |
| `registry/capability_transforms/constitutions/CONSTITUTION_NONDETERMINISTIC_ATOMS_V0.md` | An atom may declare its result is not determined by its inputs; it has no side effects; every result is recorded when produced; replay substitutes the recorded result; its results are offered, never decided. |
| Invariants (new, each with a compiler handler) | `INVARIANT_CT_GOVERNED_BY_KIND_V0` (placement by kind and purity) · `INVARIANT_MOLECULE_RUNNABLE_V0` (every step and loop body resolves to something runnable; no molecule contains itself) · `INVARIANT_MOLECULE_PURITY_CONSISTENT_V0` · `INVARIANT_NONDETERMINISM_NOT_ROUTED_V0` |
| `registry/schema/SCHEMA_CAPABILITY_TRANSFORM_V0.json` | Reconcile with the compiler: a molecule's steps and its emission are declared fields of `machine`. Edited in place as `multi_emission` edited `SCHEMA_WORKFLOW_V0`; admits every existing transform unchanged. |

## 2. `protocol_compiler` — build

| Item | Content |
|---|---|
| `stages/s5_construct.py` | Lower a molecule step and a loop body by inlining the body's own lowered stream, so the sealed form carries everything the runtime runs and no reference is resolved at run time. Carry each step's declared purity into the sealed form. |
| Four assertion handlers | One per invariant above, registered as `multi_emission` registered its handler. |
| Tests | Each refusal: unrunnable body, self-containment, purity mismatch, routing on a non-deterministic result, wrong constitution. Existing transforms compile byte-identically. |

## 3. `protocol_runtime` — execution, evidence, recording, replay

| Item | Content |
|---|---|
| `ct_executor.py` | Run an inlined molecule as its own stream, at the top of a transform or as a loop's body, carrying the loop's values between passes. |
| Evidence | One record per step a molecule runs, naming its results and not their values. For a non-deterministic step, one record carrying the result's values as determining evidence. |
| Replay | Given a trace, re-run the act from the sealed composition and inputs, substituting each recorded non-deterministic result for the atom and running nothing non-deterministic. A new `runtime replay` command. |
| Tests | Loop over N members runs N passes, a finished loop's remaining passes change nothing, nested molecules, per-step evidence count, replay reproduces the result without calling the atom. |

## 4. `transformation` — design and construction

| Item | Content |
|---|---|
| P7 template and `design/p7_design_intent/rules.py` | A `molecule_steps` register: CT code, step, kind (atom, molecule, loop), target, loop collection, carried values and their update, and the emission. |
| `build/render.py`, `build/completeness.py` | Render a molecule's steps and emission; count their facts in determinacy. |
| Re-seal | `scripts/emit_rule_sets.py`, recompile the transformation domain, rebuild fixtures and payloads, `tc phase meta` and `tc phase emit --check` green. |

## 5. Guidance and record

- `business_domains/CLAUDE.md`, `software_governance/CLAUDE.md`: the "CTs are pure" line becomes "deterministic unless declared otherwise, never with side effects".
- `delivery.md` and `closure.md` in this dossier.

## 6. Acceptance for this delivery

- `regression.sh --all` green; every existing domain's criteria hold; construction reproduces every existing artifact with zero field differences.
- The compiler and runtime tests above pass.
- The end-to-end proof — a molecule designed through the extended language, constructed, compiled and run — is the conformance workload's own change, which this delivery unblocks.

## 7. Decisions needed before editing

1. **Schema spelling.** Keep the schema's declared name `atom_stream` and teach the compiler to read it (the compiler adapts to the declaration), or rename to `steps` (the declaration adapts to the compiler). Recommended: the schema's name, since it is the declaration.
2. **What counts as routing on a non-deterministic result.** Recommended: a contract step may not invoke a non-deterministic atom directly, and a molecule's emission must come from a deterministic step.
3. **Replay scope.** Recommended: replay of one act from its trace, deterministic comparison of the result; no federated or batch replay in this delivery.
