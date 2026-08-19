# Architecture — `software_governance`

This document describes what this repository is, what it owns, and what it must never do. It is
written to be read before any code, and assumes no prior familiarity with Protocol-Governed
Computing.

For the big picture — what PGC is and how the repositories compose — see
**https://github.com/protocol-governed-computing**.

---

## 1. What this repo is

This is the **governance surface**: the set of rules a platform is governed by, and the small,
fixed set of things a platform is allowed to do.

Two kinds of thing live here, and the difference between them is the most important idea in the
repository.

- **Rules** — constitutions, invariants and vocabularies. These say what may exist and what may
  never exist. They are enforced when a platform is compiled, before anything runs.
- **Capabilities** — the operations a business is permitted to perform. There is a **closed set** of
  them. A business domain composes capabilities; it may not invent one.

**What this repo is not.** It is not an application, and it declares no business behaviour. Nothing
here knows what a customer, an order or a wallet is. It defines the *alphabet* a business writes in,
never the sentences.

## 2. Where it sits

Every other repository depends on this one. Nothing here depends on them.

```
   ┌──────────────────────────────────────────────────────────┐
   │  software_governance   ← YOU ARE HERE                    │
   │  the rules, and the closed set of things a platform can do│
   └───────────────────────────┬──────────────────────────────┘
                               │  is compiled together with
                               ▼
      business domains ──▶ protocol_compiler ──▶ projections
                               │
                               ▼
                       snapshot_assembler ──▶ sealed snapshot
                               │
                               ▼
                       protocol_runtime ──▶ execution + evidence
```

A business domain says *"I want to record a decision."* That sentence is only admissible if every
word in it is defined here. If it is not, the platform does not fail at run time — **it does not
compile**.

## 3. What it owns, and what it must never do

**It owns:**

- the **constitutions** — the rules each kind of artifact is governed by;
- the **invariants** — properties the compiler checks and refuses to build without;
- the **closed capability surface** — six side effects and a set of pure transforms;
- the **implementations** of those capabilities, in ordinary Python.

**It must never:**

- **contain business meaning.** No artifact here may mention a business concept. The test is
  mechanical: search this repository for any business noun and find nothing.
- **grow a capability because one domain wants it.** The set is closed on purpose. Adding to it is a
  deliberate act with consequences for every platform, not a convenience for one caller.
- **depend on any other repository in the composition.** Dependencies point *toward* governance,
  never away from it.

## 4. The two kinds of capability

This is the distinction a newcomer most needs, and it is enforced structurally rather than by
convention.

```
   ┌───────────────────────────────┬───────────────────────────────┐
   │  CAPABILITY TRANSFORM  (CT)   │  CAPABILITY SIDE EFFECT  (CS) │
   ├───────────────────────────────┼───────────────────────────────┤
   │  pure computation             │  governed mutation            │
   │                               │                               │
   │  inputs → outputs             │  changes something outside    │
   │  same input, same output      │  itself: a store, the clock   │
   │  no files, no network,        │                               │
   │  no clock, no randomness      │  every change the platform    │
   │                               │  can make is one of these     │
   └───────────────────────────────┴───────────────────────────────┘
              open to extension              CLOSED — six of them
```

**Why the asymmetry?** A pure transform can do no harm outside itself, so the set may grow. A side
effect is how the platform touches the world, so the set is finite, enumerable, and reviewable. If
you want to know everything a PGC platform can *do to anything*, you read six declarations — not the
whole codebase.

The six, and what each is for:

| capability | what it does |
|---|---|
| `CS_MUTABLE_JSON_V0` | holds records that change — write, read, update, delete |
| `CS_APPENDONLY_JSONL_V0` | holds a trail that is added to and never rewritten |
| `CS_REGISTRY_V0` | claims a key so two things cannot share one identity |
| `CS_CLOCK_V0` | supplies the current time |
| `CS_SNAPSHOT_QUERY_V0` | reads the sealed platform itself |
| `CS_TEXT_ARTIFACT_V0` | reads and writes text artifacts |

The closure is not a comment — it is an invariant (`INVARIANT_CS_SURFACE_CLOSED_V1`) that names all
six explicitly, and the compiler refuses a platform using anything else.

## 5. Layout

Only the parts that carry meaning:

```
registry/                     the rules, grouped by what they govern
    governance/               constitutions over constitutions
    workflow/  intent/        what a business act may look like
    capability_contracts/     how capabilities may be composed
    execution/  trace/        how execution and evidence must behave
    transport/                how the platform may be reached
    actor/  authority/        who may act
    …                         27 concern areas in total

capability_transforms/
    registry/                 the declaration of each transform
    implementation/           its Python — pure functions, no I/O

capability_side_effects/
    registry/                 the declaration of each side effect
    implementation/           its Python — the only code that mutates anything

doc/                          the governance surface map
```

A declaration and its implementation are separate on purpose: the declaration is what the compiler
governs, and the implementation is replaceable without governance changing.

## 6. Rules this repo enforces

Stated as checkable claims rather than intentions.

1. **No business meaning appears here.** Searching for a business noun returns nothing.
2. **The side-effect surface is exactly six.** An invariant names them; a seventh does not compile.
3. **A transform is pure.** No file access, no network, no clock, no unseeded randomness, no global
   state. A transform that needs any of those is a side effect and must be declared as one.
4. **Every mutation is one of the six.** There is no other write path into a governed system.
5. **Governance depends on nothing.** This repository imports no other repository in the
   composition.

## 7. How to know it works

This repository is compiled, not run. It is correct when a platform composed from it compiles and
seals:

```bash
./protocol_compiler/compile.sh      # governance compiles
./snapshot_assembler/assemble.sh    # a platform seals, and reports conformance
```

A failure here is a governance failure, and it is reported as a named invariant refusing a named
artifact — never as a crash at run time.

## 8. Where the architecture is explained

This document describes *this repository*. The architecture it realizes is developed in the papers
indexed at **https://github.com/protocol-governed-computing**:

- **A Conceptual Model** — the snapshot, admissibility, constitutional invariants, and the evidence
  model. The closest companion to this repository.
- **An Architecture for Deterministic Declarative Execution** — why the runtime that consumes what
  is governed here decides nothing.
- **Realizing the Normative Platform and Its Governed Transformation** — why the capability surface
  is closed, and what it costs when a domain needs something the surface lacks.
