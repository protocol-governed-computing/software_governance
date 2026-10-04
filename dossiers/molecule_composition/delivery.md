# Delivery — molecule_composition

**Authorized by:** Gate 1, closed at P6 against composition `1b0cfbd3d094…`
**Delivered:** a transform composed of other transforms can be stated in a design, rendered,
compiled, run and replayed; and a transform may declare that its result is not determined by its
inputs, lawfully, at exactly the step where determinism ends
**Unblocks:** the conformance workload's own change, which exercises a molecule end to end, and
`causal_language_model/cr_dossiers/cr_01_model_response`, paused before P7 for exactly this

---

## What was authored

**`CONSTITUTION_MOLECULES_V0`.** How a molecule runs: its steps in declared order; a loop's body once
per member of its collection, every pass, so a finished loop carries that fact forward and the passes
that remain change nothing; no molecule containing itself; a declared purity checked against its
steps; one evidence record per step; no side effects.

**`CONSTITUTION_NONDETERMINISTIC_ATOMS_V0`.** An atom may declare `ct_impure`: the same inputs may
produce a different result. It has no side effects. Every result it produces is recorded when produced,
values included; a replay substitutes the recorded result and never runs the atom; and its results
are offered to a deterministic step, never decided by one.

**`CONSTITUTION_CAPABILITY_TRANSFORMS_V0` is unchanged.** Its statement that every transform is pure
describes the transforms it governs — deterministic atoms — and every transform in the composition is
one. Three constitutions now govern transforms, and which one governs a transform is decided by its
kind and declared purity rather than by convention.

**Four invariants, each with a compiler handler.** `INVARIANT_CT_GOVERNED_BY_KIND_V0` places a
transform under exactly one of the three. `INVARIANT_MOLECULE_RUNNABLE_V0` refuses a step or loop body
that resolves to nothing the runtime can run, and a molecule that reaches itself.
`INVARIANT_MOLECULE_PURITY_CONSISTENT_V0` refuses a molecule declared deterministic over a step that
is not. `INVARIANT_NONDETERMINISM_NOT_ROUTED_V0` refuses a contract invoking a non-deterministic atom
directly, and a molecule emitting from one.

**`SCHEMA_CAPABILITY_TRANSFORM_V0`** declares `machine.emit`: the one value a molecule yields, named for
the step it comes from. `atom_stream` kept its declared name, and the compiler was taught to read it.

**`s5_construct.py`** lowers a molecule's stream and emission as declared. A molecule step or a loop's
body is sealed inline, whole, so the runtime resolves no reference; every atom carries its
implementation and every step its declared purity.

**`ct_executor.py`** runs an inlined molecule as its own stream — at the top of a transform, nested, or
as a loop's body, carrying the loop's values between passes. Each step it runs is reported as a
`CT_STEP` trace event naming its results; a non-deterministic step's event carries its result's values.
Given recorded outcomes, the executor substitutes them for every non-deterministic step and calls no
such atom; a missing record is a refusal, never a run.

**`runtime replay`** re-runs an act from its sealed composition and a trace, and reports whether the
determinative trace reproduced or diverged.

**P7** gained `molecule_steps` and `molecule_step_bindings`, and the rules that hold a molecule to
being stated: steps, kinds, targets, a loop's collection and iterator, exactly one emission, and
bindings that name a source the executor resolves. **`render.py`** renders a molecule's stream and
emission, with no implementation, at full determinacy.

---

## What delivery confirmed

**Nothing that existed changed.** The composition sealed byte-identically after the compiler change
(`02732a77…`, 413 artifacts): every transform is an atom, and an atom lowers exactly as before.
Construction still reproduces 99 of 99 artifacts across four domains with zero field differences.

**The placement check was seen to refuse, not only to pass.** Declaring an existing deterministic atom
`ct_impure` failed the build with `E701 ASSERT_CT_GOVERNED_BY_KIND_V0`: it named the wrong
constitution for what it now declared.

**Replay reproduces without the atom.** A loop of eight passes, each offering words at random and
choosing one under a rule, was run, recorded and replayed: the replay produced the same response and
the same determinative trace, and the offering atom was called zero times. Two fresh runs, unrecorded,
were told apart.

```
compiler      8/8   every refusal fires on a composition built to trip it
runtime      10/10  passes, nesting, per-step evidence, recording, replay, refusal without a record
design        4/4   rendered form equals the lowered form; 22 rules each seen to fire
regression    green but for admission_contract_fidelity (31, expected)
```

---

## What it took

**A stale placement surfaced as a failure somewhere else.** The governance change left the federated
and multi-worker platform builds compiled against the old surface, and the assembler refused to compose
them — a red federation test after a change that touched no federation code. The regression now
rebuilds both on every run.

**Every test document had to carry the two new registers.** A register the template declares is one
every document must present, so the maintained fixtures and the P7 test documents each gained both,
declared empty. The delivered dossiers were not touched: they are evidence of what was gated under
the rules then in force.

---

## What is deliberately left open

**A molecule has not yet run end to end through the lifecycle.** Every stage is proven on its own, and
replay is proven through the trace writer; a molecule designed, constructed, compiled and run through
the `runtime replay` command on a real snapshot needs a molecule in a composition, and that is the
conformance workload's change. The domain that found the gap does not supply that evidence.

**The trace event schema is behind the runtime.** `SCHEMA_TRACE_EVENT_V0`'s event-type enumeration
predates this change and did not list every event the runtime already wrote; `CT_STEP` widens a gap that
existed before it.

**Two rule refinements the design language does not yet draw.** A binding's step is resolved against
every molecule's steps rather than its own molecule's, and a `CARRY` or `UPDATE` row is not refused on a
step that is not a loop. Both are refused later — the compiler lowers nothing it cannot resolve — but
not at P7.

**The rename.** `CONSTITUTION_CAPABILITY_TRANSFORMS_V0` would read more plainly as
`CONSTITUTION_DETERMINISTIC_ATOMS`; renaming it is deferred to its next version, since a rename in place
would move every transform in the composition.
