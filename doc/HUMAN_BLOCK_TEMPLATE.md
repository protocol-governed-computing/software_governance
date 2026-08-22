# The human block — a realization document, not a specification

Task C. What the non-normative prose alongside a machine block is for, what it may not become, and
the rules that keep it there.

## 1. Three layers, and the middle one is this document's subject

```
Normative Standard                 what PGC requires
        ↓                          standards/spec — cited here, never restated
Human-Consumable Realization       how this artifact realizes it
        ↓                          the prose in an artifact — this template
Machine Block                      what the implementation actually consumes
                                   the sole normative declaration surface (MB-1)
```

Each layer answers a different question, and the value of the middle one is that **neither of the
others can answer it.** The standard says what must be true of any realization and deliberately
declines to name a mechanism. The machine block names the mechanism and deliberately says nothing
about why. A reader holding both still cannot see how one becomes the other, and reconstructs it
every time — which is the same rediscovery the realization map exists to spare an implementer, at
artifact scale.

**The failure this template exists to prevent is the middle layer growing into the top one.** Prose
that explains a mechanism drifts easily into prose that requires it; the requirement is then stated
in two places, one of them ungoverned, and readers trust the one they can read. `2c` MB-1 forbids the
outcome — everything outside the machine block "MUST NOT determine anything" — and forbidding an
outcome has never been sufficient here. §3 gives the rules that make it structural.

## 2. Shape

```markdown
# <ARTIFACT_CODE>

## Machine

```yaml
fqdn: <namespace>::<ARTIFACT_CODE>
artifact_kind: <KIND>
version: <V>
governed_by: <namespace>::<CONSTITUTION>
authority: <authority>
concern: <concern>
core:
  ...
```

---

## Realization

### What this realizes

<The normative requirement, by citation. `3b` SN-4, `2c` MB-1, `2e` CA-2 — document and invariant,
named. One or several. Where an artifact realizes no normative requirement directly, say so: many
domain artifacts realize a business need under governance rather than a family invariant.>

### How

<How the declarations in the Machine block above realize it. This is the section with actual content:
which declared field does what, why the shape is what it is, what a reader would otherwise have to
infer from the code.>

### What is not claimed

<The bound. What this artifact does not establish, what the check is not strong enough to catch, what
a reader might reasonably assume and should not. Omit only when there is genuinely nothing to bound.>
```

**The Machine block comes first**, immediately after the title. The normative surface leads and the
prose follows it as commentary, which is the actual relationship between them.

## 3. Three rules, each of which can be checked

### 3.1 Cite, never restate

**Every normative claim in the human block is a citation to a named document and invariant.** A
sentence that asserts a requirement without one is a second specification, however true it is.

> ✗ "A transport ingress must have a verified, static invocation target."
> ✓ "`5a` IB-5 requires operation-to-target resolution to be determined before interaction time.
>    This artifact realizes that by …"

The difference is not stylistic. The first sentence is a requirement with no authority behind it and
no way to be wrong; the second points at the thing that can be checked and then explains a mechanism.

### 3.2 Never restate a machine-block value

**If a fact is in the machine block, the prose refers to it and never repeats it.** Two copies can
disagree; one cannot.

This is not hypothetical. Two hundred and sixteen artifacts carried a `## Header (Mandatory)` block
restating `Artifact Code`, `Artifact Kind`, `Governed By`, `Version`, `Status` and `Supersedes` —
about 1,265 duplicated lines — and the copies were already weaker than the originals:
`**Governed By:** CONSTITUTION_WORKFLOW_V0` beside a machine block declaring
`governed_by: workflow::CONSTITUTION_WORKFLOW_V0`, a short name where the declaration carries an
identity. A reader who trusted the prose had a name that resolves to nothing.

**`Status:` and `Version History` go with it.** Supersession is a declared relation (`4e` SU-1, SU-3);
a prose changelog is a second record of a governed fact, and `Status: draft` on a delivered artifact
is that record already wrong.

### 3.3 Say what is not claimed

The strongest guard against over-claiming is an explicit bound, and the surface already contains the
model. `INVARIANT_TRANSPORT_TARGET_EXISTS_V0` distinguishes what its check enforces per handler kind
and then writes:

> For those kinds the enforced check is that the target is **declared and static**; nothing stronger
> is claimed.

That sentence does more for a reader than any restatement of the rule would. It is also the sentence
a second specification never contains, because a specification states what must be true and has no
reason to bound its own enforcement.

## 4. Section vocabulary

Prose sections are named for the question they answer, and **the names must not read as normative.**
The surface currently carries 189 sections named `Rule Statement`, `Rule`, `Validation Rules` and
`Enforcement Scope` — names that announce a rule is being stated, in a document that may not state
one.

| Use | Not |
|---|---|
| **What this realizes** | Rule, Rule Statement, Requirements |
| **How** | Validation Rules, Enforcement Scope |
| **What is not claimed** | Limitations, Caveats *(these invite apology; this is a bound)* |
| *(nothing — it is in the machine block)* | Header, Status, Version History |

`Intent`, `Purpose`, `Rationale` and `Scope` are admissible where they carry genuine content, and
`Rationale` in particular is worth keeping — why a shape was chosen is exactly what neither other
layer records.

**Terminology comes from Part I.** `1a` is the family's terminology authority and its distinctions
bind documents; an artifact's prose should call things what the specification calls them, so that
reading an artifact and reading the standard do not require translation. Where an artifact's prose
uses a term Part I defines otherwise, Part I wins and the prose is corrected.

## 5. What the human block may never do

- **Determine anything.** No value in it is read by any mechanism, and none may become read. `2c`
  MB-1 makes the machine block the sole normative declaration surface.
- **Disagree with the machine block.** The question "what if they disagree?" does not arise, because
  under §3.2 the prose states no value that could disagree.
- **Carry governed content in a second fenced block.** One artifact class currently does — TEST_DATA
  declares its cases in per-case yaml blocks that `assert_ct_test_data_outcome_declared_v0` parses
  out of the body. **That is a governance determination reading a surface other than the machine
  block**, and it is the one place the condition "nothing outside a machine block is read by any
  mechanism" does not hold. It is recorded rather than fixed here: moving TEST_DATA's cases is a
  change to governed content, not to prose, and belongs to its own change.

## 6. How this is enforced

`software_governance/doc/` doctrine has failed before by being written and never made refusable —
the anti-sprawl rule was in force throughout while the boundary count grew to twenty-six, because no
predicate could refuse one.

**`.github/process/human_block_fidelity.py` checks what is mechanically checkable:** that no artifact
carries a `## Header` block, that no prose line restates a machine-block key, and that no section
name comes from the closed list of normative-sounding names in §4.

What it cannot check is §3.1 — whether a sentence is a citation or a restatement is a reading, not a
pattern. That one is a review obligation, and stating plainly which rules are enforced and which are
not is itself an application of §3.3.
