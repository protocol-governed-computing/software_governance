# Delivery — routing_lookup

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `d880845e3b18…`
**Delivered:** routing is a lookup with two answers. `execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V1`
says so in every section, and `execution_topology::INVARIANT_TOPOLOGY_CONTRACT_CLOSED_V1` refuses, on
every contract in force, a routing answer other than `continue` or `exit` and an `evaluation` block.
Execution refuses an unknown answer rather than read it as going on. Both V0s are stood down, and the
twenty artifacts that named the constitution name its successor.
**Validated:** `test_routing_lookup` 5/5; `test_unknown_continuation` 3/3; a workload copy with a planted
evaluation target refused by the V1 check; full regression `--all` 68/68 as expected

---

## What this change closed

- **The constitution contradicted itself.** §4 allowed two routing answers; §1 and §3 admitted an
  evaluation target and counted its outcomes as exits. V1 states two answers throughout and forbids a
  condition on a contract.
- **The build admitted a condition nothing runs.** The V0 check counted an evaluation's `on_true` and
  `on_false` as exits. The V1 check refuses the answer by contract, step and answer, refuses the
  block, and counts exits only from `exit` and the last step's `continue`.
- **Execution went on past an answer it did not know.** The dispatcher ended on `exit` and read
  everything else as `continue`. It now raises `UnknownContinuationError`, records where, and the
  workflow ends refused, as for an unlisted outcome.

A contract not in force is not checked: the stood-down Collatz gate still carries
`evaluate_conjecture`, compiled and run nowhere.

---

## What it took

**Two domains went first.** The Collatz gate was replaced by `conformance_workloads` cr_01, which
decides with the platform's set-membership check. The licence cap contract turned out to be named by
nothing, with the cap enforced by the eligibility check; it was deleted by hand, and this dossier's
P0 statement and P2 were amended before build. So arming the check failed no build.

**The governance surface was written by hand.** The design language has no family for a
constitution or an invariant, so both V1s were authored by hand and both V0s marked stood down by
hand. Construction performed the twenty re-points; each moved only `governed_by`.

**Construction measured 0 of 0 facts,** which its threshold reads as 0%. Nothing was rendered, so
emit ran with `--require 0`; the re-points are compared by the declaration, not counted as facts.

**The platform code it touched:**

- `protocol_compiler`: `assert_topology_contract_closed_v1.py` (new), registered; the scope entry in
  `author_invariant_scope.py`; `scripts/testbed/test_routing_lookup.py` (new).
- `protocol_runtime`: `dispatcher.py` (`UnknownContinuationError`);
  `testbed/pgc/test_unknown_continuation.py` (new).
- `.github/process`: both suites in the regression; 511 artifacts, 13 supersession relations.

---

## What is carried

- **No family for governance artifacts in the design language.** A change to a constitution or an
  invariant is written by hand, and construction's completeness reads it as 0%.
- **The assertion coverage record is not persisted** for a domain build, so which checks ran is shown
  by refusal, not read from the build.
