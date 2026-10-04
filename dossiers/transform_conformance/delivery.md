# Delivery — transform_conformance

**Authorized by:** Gate 1, closed at P6 against composition `54412f835e6d…`
**Delivered:** every domain build proves its transforms against their vectors once the compile
succeeds, names each transform proven, unproven or refused, and carries that result into the snapshot;
a design can state a transform's vectors, and construction renders them
**Unblocks:** the conformance workload's declared-iteration change, which supplies the first vectors
and the first molecule proven in a composition

---

## What was authored

**`CONSTITUTION_TEST_DATA_V1`.** A vector names one transform by identity and tests it as sealed. A
molecule is tested whole. A case states its bindings and expected outcome, and then either expected
outputs or shape assertions. For a molecule, a case also supplies the recorded result of every
non-deterministic step, addressed by the path the runtime uses. A non-deterministic atom on its own
is asserted by shape only. A transform that no vector tests is unproven, never passing. Vectors run in
the supplying domain's build, on every build.

**V0 was deleted, not superseded**, following the precedent in
`CONSTITUTION_EXECUTION_PLACEMENT_V1` §8. A superseded V0 would have kept its invariants enforced,
including one bound to a compiler phase that does not exist. The same holds for
`INVARIANT_CONFORMANCE_ASSERTION_MODE_VALID_V0`, replaced by V1 with a check that runs.

**`INVARIANT_TEST_DATA_RECORDS_MATCH_PURITY_V0`** is new. A molecule's case supplies a recorded
result for every non-deterministic step and for no deterministic one. A case for any other transform
supplies none. The check validates each path against the sealed molecule's steps.

**`SCHEMA_TEST_DATA_V0`** declares the Machine block of a vector: `target`, plus `cases[]` of
`{case_id, expected_outcome, bindings, expected, assertions, recorded}`. Cases are governed content,
so they live where the compiler reads them.

**The compiler reads one format.** `s7_materialize.py` reads cases from the Machine block. It now
fails hard on a vector whose target does not resolve or has no sealed form, where it used to skip. It
also carries `recorded` into each case. The output-match check now compares against the target's
declared outputs, not against the first entry of its `governed_by`. The outcome-declared check reads
the Machine block. `TEST_DATA` joined the domain-instantiated kinds in both the compiler and the
assembler.

**The runner.** `runtime conformance <domain_root>` reads cases from the domain's build output. For
each case it hands the recorded results to the executor, and it refuses the case when a
non-deterministic step had no record or when a record went unused. It names every transform the
domain owns, and separately every platform transform the domain carries. It writes the result to
`compiled/transform_conformance/result.json`, and exits 1 when anything was refused.

**The build step.** `compile_domain.sh` runs the compile, then conformance. Because it runs under
`set -euo pipefail`, conformance runs only after a successful compile. The compiler still imports no
runtime; the script composes two tools.

**The design language.** P7 gained `test_cases` and `test_case_values`. Each value row has a role:
INPUT, EXPECTED, ASSERT or RECORDED. Eight rules hold a design to proving its transforms:

- `TRANSFORM_WITHOUT_VECTOR` refuses a transform authored with no case;
- `AMENDED_TRANSFORM_WITHOUT_VECTOR` refuses one amended with no case;
- the other six check that cases and values name what they claim.

`TEST_DATA` is a companion family. Construction renders it beside its transform as
`TEST_DATA_<CT code>`, and it never appears in `new_artifacts` or the build order. A domain's
generated build manifest declares the vector layer and the conformance place only when the design has
cases. Table cells accept the `\|` escape, so a value may contain a pipe.

---

## What delivery confirmed

**Every domain is named, and none is passed over nothing.** The current baseline:

```
workload           0 proven   2 unproven   0 refused   0 carried
transformation     0 proven   6 unproven   0 refused   0 carried
inspection         0 proven   0 unproven   0 refused   0 carried
ai_governance      0 proven   3 unproven   0 refused   4 carried
book_library_mgmt  0 proven   4 unproven   0 refused   5 carried
blockchain         0 proven   1 unproven   0 refused   6 carried
```

**The build was seen to refuse, not only to pass.**

- A vector built to trip each check stopped the compile before conformance ran.
- A wrong expectation compiled cleanly and failed the build at conformance.
- A molecule was proven from recorded results, and its non-deterministic step was called zero times.

**The result is part of the snapshot's identity.** The assembler carries each result to
`transform_conformance/<domain>/` as a manifest constituent. `conformance/` still holds only
`composition.json`. Decision 4 of the delivery plan was amended to say so.

**Nothing that existed changed behaviour.** Construction reproduces 99 of 99 artifacts across four
domains with zero field differences, and lists the four vectors the fixtures now render as not yet
delivered.

```
compiler      10/10  every refusal fires on a vector built to trip it
build          4/4   clean vector proven; tampers refused at compile; wrong expectation fails at conformance
runtime        7/7   recorded results substituted, never run; missing or unused record refused
assembler     21/21  every domain's result carried, complete, and covered by the identity
design         6/6   rendered vector admitted by the schema; each of 9 rules seen to fire
regression    green but for admission_contract_fidelity (31, expected)
```

---

## What it took

**Three readers, three formats.** The case generator read prose headings, the output-match check
read the Machine block, and the outcome check pattern-matched prose. None had ever been handed a
vector, which is how they stayed in disagreement.

**The kind set is kept twice.** The compiler and the assembler each keep their own list of
domain-instantiated kinds. With `TEST_DATA` missing from the compiler's list, the new invariants
silently did not run in domain builds. With it missing from the assembler's list, assembly refused
on a provenance count. The two lists must agree, and nothing states that except the failure.

**The case place moved.** Cases written to `compiled/conformance` would have landed in the snapshot's
`conformance/`, the collision the problem statement named. They are written to
`compiled/transform_conformance` instead.

**Every design test document had to carry the two registers.** The maintained fixtures gained real
cases. The values for cr_01 and cr_02 were taken from running each implementation. The P7 corpus
gained cr_01's cases, so each document still trips only the defect it names. The delivered dossiers
were not touched.

---

## What is deliberately left open

**No transform is proven yet.** Each domain gains vectors in its own change, and the conformance
workload's declared-iteration change goes first, carrying a molecule with a non-deterministic step.

**Carried platform transforms are proven nowhere.** The platform's build runs no conformance, by
decision. Every domain that carries a platform transform names it as carried and does not test it.
Proving them needs a home that can run them — a platform workload, or a domain's vectors.

**The code is not sealed by content.** A vector proves the implementation that ran at build time.
Nothing in the snapshot records a hash of that implementation's source, so a change to the code after
assembly goes unseen until the next build.

**Two P7 refinements the design language does not yet draw.**

- A value row's case is resolved against every case in the register, not against its own transform's
  cases.
- Cell whitespace normalization reaches values, so a value that depends on repeated spaces cannot be
  stated.
