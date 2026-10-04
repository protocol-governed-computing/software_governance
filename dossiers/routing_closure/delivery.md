# Delivery — routing_closure

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `f8356d9c8938…` (v5)
**Delivered:** the platform holds every domain to routing closure. A step that answers fewer outcomes
than its capability declares is refused at build. So is a reachable workflow place that leaves an
outcome of its contract without a route. At run time, a step outcome nothing answers refuses the
request. Every step record carries its outcome and the continuation it selected.
**Validated:** `test_routing_closure.py` 11/11, `test_step_outcome.py` 3/3; full regression `--all`
64/64 as expected; standards guards pass

---

## What this change closed

The open standard's `v1` Changes 3 and 4 name four obligations. The realization map recorded all four
as Violated. Each is now Demonstrated:

- **CP-13.** `INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V0` compared a step's routes with the outcomes its
  author listed. It now also compares that list with what the capability declares. For a side
  effect, that is the operation's `result_status_values`. For a transform, it is SUCCESS, and
  VIOLATION unless the transform never refuses. A domain build reads them from the platform surface
  it is built against.
- **GC-15.** The new `workflow::INVARIANT_WF_ROUTING_CLOSED_V0` refuses a node reachable from the
  start whose `next` misses an outcome of the contract or intent it runs. A superseded workflow has
  no dispatch entry (SU-7). Execution cannot reach it, so it is not checked.
- **EX-18.** The runtime looked up a step's continuation with a default of `continue`. It now has no
  default. Where there is none, it records an `ERROR`, completes the run refused, and runs nothing
  after the step.
- **EV-19.** A `CC_STEP` line carries `outcome` and `continuation`, and `SCHEMA_TRACE_EVENT_V1`
  requires both. An admission's continuation is `route`, because the WF_ROUTE that follows records
  it. A refused step's continuation is null.

A step narrowed by hand, and a route removed by hand, each fail the ai_governance build.

---

## What it took

**The domains went first.** Blockchain `cr_06`, the transformation generator and ai_governance
`cr_02` closed every gap the survey found. So arming the checks failed no build, and every
composition the domains hold builds and runs as it did.

**The pin is v5.** A CR pins the composition without its own output. The working snapshot already
held this change's governance, so the design was judged against the published v5 composition, whose
governance surface this change amends. The phase checks read it. Nothing was assembled into it.

**Nothing was rendered.** The governance surface is authored, so the amended obligation, the two
amended constitutions, the schema and the new obligation were written by hand and cited as REVIEW.
Construction measured 0 of 0 facts, which is a count over nothing rather than a pass. No invariant
family exists in the design language, so the new obligation is named in prose, not scheduled.

**The refusals are deferred to what this change writes.** The design pipeline cannot cite a rule its
own change adds. So each refusal the seed states is handed to the obligation or the runtime loop
that carries it, and is armed here.

**The platform code it touched:**

- `protocol_compiler`: the import-surface reader in `s2_canonicalize.py` and its context entry in
  `s4_govern.py`; the CP-13 comparison in `assert_topology_routing_complete_v0.py`; the new
  `assert_wf_routing_closed_v0.py`, registered; the scope entry in `author_invariant_scope.py`.
- `protocol_runtime`: `dispatcher.py`, `evidence.py`, `scheduler.py`.
- Two new suites, both in the regression.

---

## What is carried

- **A superseded workflow keeps its gaps.** `WF_RECORD_VERIFICATION_DECISION_V0` keeps three
  unrouted BACKEND_ERROR outcomes. It cannot be dispatched, and SU-8 forbids deleting it.
- **A transform that cannot load answers VIOLATION.** The runtime's validation of this change found
  it: without the domain roots on the path, an inactivity check answered VIOLATION and the reclaim
  ended as still active. That is how a load failure was routed before this change. It is noted, not
  changed.
- **Evaluation targets are not executed.** `on_result` may name one, and the runtime proceeds past
  it as it did before. No contract in the composition uses one.
