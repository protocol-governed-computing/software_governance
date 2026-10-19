# CS_EVIDENCE_EXPIRY_V0

## 1. Intent

End the retention of evidence whose declared window has closed, and record that it was ended.

Retention has a governed consequence: the period over which a determination can be established is
the period over which its evidence is retained. A platform that lets evidence lapse without a
declared act has discarded evidence by omission — the determination becomes unestablishable and
nothing says when, by what, or under which rule.

This capability makes that act declared. It does not decide *whether* evidence should expire; a
profile decides that, and this capability carries out what the profile declared.

---

## 2. Rationale

A system that discards evidence has not made past determinations ungoverned — they were governed
when they were made. It has made them **unestablishable**, and a claim about them can no longer be
checked. Whether that is acceptable is a profile's question.

What is not a profile's question is whether the ending is an act. Expiry that happens by a cleanup
script, a log rotation, or a disk filling up is a governed consequence reached by an ungoverned
route. The window is declared here rather than supplied by the environment, so that a party reading
a sealed snapshot can read off that same snapshot how long its evidence lives. A window living
outside the snapshot is one no signature over the snapshot covers.

---

## 3. Applicability & Non-Applicability

### Valid Use Cases
- Ending retention of evidence whose declared window has closed
- Ending an attestation together with the evidence it attests to
- Establishing, at any moment, what is within its window and what is past it

### Invalid Use Cases
- Deleting evidence that is still within its window — the window is the authority, not the caller
- Deleting evidence to reclaim space, or on an operator's judgement
- Deleting the record of a deletion (see §6)
- Shortening a window at execution time — the window is declared and changing it is a recompile

---

## 4. Side-Effect Category

- **Category:** Retention
- **Side-Effect Type:** persistent, subtractive
- **Append Semantics:** NO
- **Overwrite Semantics:** NO — this capability removes; it never rewrites

---

## 5. Where the window comes from

The window is declared in `configuration.retention_window_days` and is therefore part of what a
snapshot carries and a signature over that snapshot covers. It is not read from the environment, and
this capability has no operation that changes it.

Changing the window is a change to the declarations: a recompile, a new snapshot identity, and a
declared supersession. That is the cost of the window being checkable by a party who holds only the
snapshot.

---

## 6. Why the deletion record cannot expire

The record of an expiry is written through an append-only capability, which by its own declaration
admits no deletion at all. The exemption is therefore **structural rather than a rule**: no flag
grants it and no caller can clear it, because the store holding the record has no operation that
could remove one.

Without that, a platform reaches a state where evidence is absent and nothing distinguishes evidence
that was deleted under a declared window from evidence that was never written. The first is a
platform doing what it declared. The second is a platform that lost something. A party checking the
evidence could not tell which, and the difference is exactly what retention is supposed to make
answerable.

---

## 7. Why an attestation ends with its subject

An attestation asserts something about a record. When the record is gone the attestation asserts
something about nothing, while continuing to look like evidence and carrying a signature that still
verifies.

An attestation is a claim rather than a proof, and retaining one after its subject leaves the
platform holding the most persuasive form of the thing a reader is most likely to mistake for the
evidence itself. It ends with what it attests to.

---

## 8. Properties

| Property | Value | Description |
|----------|-------|-------------|
| durability | persistent | What is removed does not return |
| reversibility | none | Expiry has no inverse; this is the point, not a limitation |
| determinism | conditional | Given the same store and the same instant, the same set expires |
| authority | declared | The window governs; the caller supplies neither it nor an exception |

---

## Machine

```yaml
fqdn: capability_side_effects::CS_EVIDENCE_EXPIRY_V0
artifact_kind: CAPABILITY_SIDE_EFFECT
version: v0
governed_by: capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
authority: pgc.platform
concern: capability_side_effects
core:
  summary: Ends retention of evidence whose declared window has closed, and records that it ended
  category: storage
  policy:
    operations:
    - SURVEY
    - EXPIRE
  field_types:
    store_path: string
    as_of: string
    window_days: integer
    examined: integer
    within_window: integer
    past_window: integer
    expired: integer
    subjects: array
    record_id: string
    result_status: string
  operations:
    SURVEY:
      summary: What is within its window and what is past it, removing nothing
      handler: survey
      effect: read
      input:
      - store_path
      - as_of
      output:
      - result_status
      - examined
      - within_window
      - past_window
      - subjects
      idempotent: true
      result_status_values:
      - SUCCESS
      - VIOLATION
      - BACKEND_ERROR
    EXPIRE:
      summary: End retention of evidence past its window, with its attestations, and record it
      handler: expire
      effect: write
      input:
      - store_path
      - as_of
      output:
      - result_status
      - examined
      - expired
      - subjects
      - record_id
      idempotent: false
      result_status_values:
      - SUCCESS
      - VIOLATION
      - BACKEND_ERROR
  configuration:
    retention_window_days:
      type: integer
      required: true
      description: >
        Days a determination's evidence is retained, measured from the close of the trace it
        belongs to. Declared here so a party holding the snapshot can read the rule governing
        its evidence off the snapshot itself. No operation changes it.
    deletion_record_stream:
      type: string
      required: true
      description: >
        Append-only stream the record of each expiry is written to. Append-only by requirement,
        not by convention — a store able to delete could delete this.
  failure_modes:
  - 'VIOLATION: as_of was not supplied by the governed clock, or precedes a record it would expire'
  - 'VIOLATION: the deletion-record stream admits deletion, so a record written there could be removed'
  - 'BACKEND_ERROR: the evidence store or the deletion-record stream could not be reached'
  architecture:
    role: Retention authority over evidence
    purpose: Makes the end of retention a declared act rather than an absence nobody recorded
    bindings:
      as_of: instant the window is measured against, from the governed clock and not a host
      subjects: identities whose evidence was examined or ended
  use_cases:
  - 'Retention: end evidence past a declared window, leaving a record that says so'
  - 'Audit: establish what is still within its window without changing anything'
implementation:
  module: capability_side_effects.implementation.CS_EVIDENCE_EXPIRY_V0.runtime
  callable: EvidenceExpiryRuntime
extensions:
  cs_kind: retention
```
