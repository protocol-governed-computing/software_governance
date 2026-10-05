# Delivery — reference_semantics

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `c55dbfd7d1ae…`
**Delivered:** `artifact::VOCAB_DECLARATION_REPRESENTATION_V1`, which stands down V0. It names the
parts of a declaration that name another artifact, beside those that carry no meaning, and the two
rules a comparison applies. The compiler's record of references and both reference checks read it.
**Validated:** construction 73/73; construction acceptance 169/169 with 0 field differences;
`test_reference_semantics` 14/14; full regression `--all` as expected

---

## What this change closed

Four places decided what a reference is, and they disagreed:

- **The record of references** read nine fixed parts. Inspection reported
  `conformance::CONSTITUTION_ASSERT_V0` referred to by 1 artifact, while 138 name it under
  `enforced_by`, and `transformation::AC_SEED_AUTHOR_V0` by none of the 39 that name it.
- **The reach check** read every value of a live declaration.
- **The FQDN-only check** kept a list of four parts, and the record refused short codes in its own
  nine, so one rule was enforced twice from two lists.
- **Comparison** had no notion of a reference.

V1 keeps V0's two groups and adds five:

- **`reference`:** 23 parts. A full name at or beneath one is a reference.
- **`reference_keyed`:** `bindings`. A full-name key is a reference.
- **`full_name_required`:** `consults`, `governed_by`, `runtime_binding`, `side_effects`,
  `structure`, `transform`, `transforms` and `vocabulary_id`. A short code there is refused.
- **`supersession`:** `supersedes` and `superseded_by`. They name an artifact without reaching it.
- **`sameness_rules`:** `explanation_only_as_text` and `reference_to_declared_successor`. A comparison
  applies exactly these, and can refuse to run when the declaration names one it does not apply.

Each `documentation` entry's meaning now states that it is exempt only where its value is text. Test
data writes a model's settings under `description` and a count under `summary`; those carry meaning.

The compiler reads V1 by its exact identity, from the platform build or the imported platform
surface, and refuses a build that cannot see it or sees it stood down. S1 records every declared
reference and refuses a full name anywhere else (`E105_UNDECLARED_REFERENCE`). It no longer refuses
short codes; `artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0` does, once, from `full_name_required`.
`artifact::INVARIANT_SUPERSEDED_NOT_REFERENCED_V0` reads full names from the declaration and still
finds a stood-down artifact's short code anywhere, so it sees no less than before.

---

## What it took

**`bindings` could not require a full name.** A key name is declared wherever it appears, and
`bindings` keys three kinds of map: a binding's capabilities by full name, a test case's inputs by
field name, and a workflow admission's events by short code. So `bindings` is a keyed reference
part, and does not require a full name. Removing that row was re-checked without a composition,
because the failed rebuild had removed the pinned snapshot; the row sits in a register no grounded
rule reads.

**A test's target is now a reference.** A target nothing declares is refused as a dangling
reference when references are resolved, before any assertion reads it. `test_vector_build` now
expects that refusal.

**Construction sealed every rendered artifact as version `v0`.** The renderer wrote a literal, so the
new declaration was sealed `v0`, and so were two book_library_mgmt `_V1` artifacts from `cr_05`.
`transformation/build/render.py` now takes the version from the identity's `_V<n>` suffix.
`cr_05_catalog` was re-emitted; the two version lines are its only difference.

**The platform code it touched:**

- `protocol_compiler`: `atoms/representation.py` (new), `atoms/error_codes.py`,
  `stages/s1_extract.py`, `stages/s4_govern.py`, `assert_fqdn_only_references_v0.py` and
  `assert_superseded_not_referenced_v0.py`.
- One new suite in the regression; one suite's expectation changed.

---

## What is carried

- **Short-code references are not declared.** A workflow names its places, its start and its
  contracts by short code; an intent names its workflow, and an admission its events, the same way.
  The reach check still finds them. A short-code key of a binding is no longer refused, because
  `bindings` cannot require a full name by key name.
- **The FQDN-only invariant's text is wider than what is enforced.** It says every reference is
  written in full; 39 intents name their workflow by short code.
- **The compiler names V1 exactly.** When V1 is replaced, `compiler/atoms/representation.py` is
  re-pointed by hand. It is the only caller outside the composition.
- **A vocabulary's meanings are not sealed.** The rules are entries for that reason.
