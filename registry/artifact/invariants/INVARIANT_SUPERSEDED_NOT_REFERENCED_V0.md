# INVARIANT_SUPERSEDED_NOT_REFERENCED_V0

Architectural Invariant

## Machine

```yaml
fqdn: fb.artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0
artifact_kind: INVARIANT
version: V0
governed_by: fb.governance::CONSTITUTION_INVARIANTS_V0
core:
  enforcement_stage:
  - compiler_assertion
  violation_response: FAIL_IMMEDIATELY
assert_projection:
  applies_to_kinds:
  - WF
  - CC
  - CS
  - CT
  - RB
  - AC
  - IN
  - EV
  - TI
  - TE
  - INVARIANT
  - CONSTITUTION
  - STRUCTURE
  - SURFACE
  - VOCAB
```

---

## Purpose

Make supersession mean something.

An artifact declares `superseded_by` and stops being reachable. Without this invariant that
declaration is a comment: the artifact stays in the composition, stays compiled, stays dispatchable,
and everything that referenced it goes on reaching it. A change can then stand a workflow down,
report success, and leave the composition executing the workflow it retired.

That is not hypothetical. A change split one deciding workflow into an accept path and a reject path,
marked the original superseded, compiled, verified and attested — while three artifacts still routed
to it. A caller crossing either boundary would have reached the workflow the design had stood down.

---

## Validation Rules

### Rule: nothing live references a superseded artifact

Where `X` declares `supersedes: Y` — equivalently, where `Y` declares `superseded_by` — no artifact
in the composition may reference `Y`.

**Violation**:

```yaml
# WF_RECORD_VERIFICATION_DECISION_V0 declares superseded_by: [WF_ACCEPT_ACTOR_V0, WF_REJECT_ACTOR_V0]
fqdn: blockchain::TI_ACCEPT_ACTOR_V0
handler:
  workflow: blockchain::WF_RECORD_VERIFICATION_DECISION_V0   # reaches a retired artifact
```

### Rule: a superseded artifact may reference another

The closure binds **live** artifacts. A retired artifact naming another retired one is coherent
history — an entry intent and the workflow it dispatched are stood down together, and each still says
what it said. Refusing that would oblige a change to rewrite the records it is retiring, which is the
opposite of retaining them.

### Rule: a successor exists

`superseded_by` carries at least one identity. "Superseded" with nothing standing in the artifact's
place is a deletion wearing a softer word, and deletion is a human act with a `git rm`, not something
a design declares.

---

## What this does not do

It does not remove the artifact. A superseded artifact is **unreachable, not absent**: excluded from
the executable projections, retained in the canonical set and visible through `si.*`, because the
record of what a composition once executed is evidence and deleting it destroys what dossiers exist
to preserve.

It does not resolve references. A reference names an exact, versioned identity and continues to; this
invariant refuses a reference to a retired identity rather than quietly re-pointing it at a successor.
Re-authoring the referrers is the work that makes a retirement legible, and doing it automatically
would convert visible work into invisible work.
