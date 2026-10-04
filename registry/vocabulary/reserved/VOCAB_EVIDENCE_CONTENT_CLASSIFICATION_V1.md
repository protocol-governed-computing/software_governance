# VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V1

## Machine

```yaml
fqdn: vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V1
artifact_kind: VOCABULARY
version: v1
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: vocabulary
determinative_fields:
  casing: lower_snake
  domain_extensible: false
  entries:
  - trace_schema_version
  - event_type
  - domain
  - wf_addr
  - cc_addr
  - step_addr
  - step_op
  - result_status
  - detail
observational_fields:
  casing: lower_snake
  domain_extensible: false
  entries:
  - trace_id
  - ts_ns
observational_keys:
  casing: lower_snake
  domain_extensible: false
  entries:
  - record_id
```

---

## Intent

Which content of an execution trace is **determinative** and which is **observational**, declared so
that a checker can compare the first and disregard the second.

`3e` §5 settles what earlier documents left open, and EV-5 requires the distinction be *declared
rather than inferred*. Without it, replay comparison is impossible in both directions: a checker
comparing everything fails on every timestamp and learns nothing; one comparing nothing established
nothing; one guessing which fields look stable is deciding for itself what governance meant.

**Determinative content MUST be identical** for the same state, proposal and closure (EV-6). It is
what establishes the path taken and the outcome reached: which act, which contract, which step, what
that step reported.

**Observational content MAY differ** between two executions of the same transition, and **MUST NOT
participate in any determination** (EV-7). `ts_ns` is a monotonic reading; `trace_id` carries a
timestamp prefix and is documented as "not purely deterministic".

**Observational keys are observational wherever they appear**, including inside a determinative
field. A determinative field such as `detail` carries values a caller returned, and some of those
are assigned by a store at the moment it writes: the identity an append-only store gives a record is
read from the clock. Two faithful executions of one transition differ on it, and it determines
nothing about the path or the outcome. Declaring the key here, rather than leaving each checker to
skip it, is EV-5 applied inside a field.

---

## Where this is read

`protocol_runtime/runtime/evidence.py` reads both sets from the sealed composition and writes a
`trace_classification` header as the first record of every trace. The trace therefore carries the
classification it was written under, so a party holding the trace and the snapshot can compare
determinative content **without access to the producing system** (EV-16, AI-16).

`.github/process/evidence_determinism.py` executes one workflow twice and asserts that determinative
content is identical and that observational content is what differs.

---

## What is not claimed

**That a field classified determinative carries only determinative content.** `detail` is
caller-filled: a step that put a duration or a hostname in it would place observational content on
the determinative side, and no check here would see it. The rule is that observational content goes
in a declared observational field, or is named by a declared observational key; the rule is stated
and is not enforced per value. A new store-assigned value is a new key here, never a checker's
exception.

**That the classification is complete for evidence other than execution traces.** Construction
produces no evidence record at all today, so it has none to classify — a separate finding, and this
artifact does not pretend to cover it.

---

## Change from V0

V0 classified trace content by top-level field only, so a store-assigned value inside `detail` was
determinative by default. A replay of any act that appends a record disagreed with its original on
that one value. The only way to accept such a replay was a checker that skipped the value by name:
an exception held in a test, not in the composition. V1 adds `observational_keys`. The runtime
writes the keys into each trace's classification header, and a replay comparison removes them from
determinative content, reading them from the trace itself.

