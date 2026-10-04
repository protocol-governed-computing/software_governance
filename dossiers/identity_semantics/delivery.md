# Delivery — identity_semantics

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `53acd1c4879c…`
**Delivered:** `artifact::VOCAB_DECLARATION_REPRESENTATION_V0`. It names the parts of a declaration
that only explain, and the lists whose order carries no meaning. Everything it does not name carries
meaning.
**Validated:** construction 30/30; construction acceptance 168/168 with 0 field differences; full
regression `--all` 64/64 as expected; composition `c55dbfd7d1ae…`

---

## What this change closed

Nothing declared which parts of an artifact's declaration carry its meaning. A comparison of two
declarations could not ignore wording, or the order of a list read as a set. So nothing could tell a
change of meaning from a change of wording, and the open standard's SU-11 could not be checked.

The vocabulary has two groups:

- **`documentation`:** `summary`, `description`, `notes`, `purpose`, `use_cases`,
  `failure_modes`, `intent`, `detail` and `admission_rules`.
- **`unordered`:** `allowed`, `result_surface`, `result_status_values`, `canonical_surface`,
  `applies_to_kinds`, `governs`, `superseded_by`, `requires`, `forbids`, `consults`,
  `allowed_capability_transforms` and `allowed_capability_side_effects`.

Each name was surveyed across all 501 artifacts of the pin, and each qualifies wherever it appears.
Some prose is data, and stays out: a test case's question, its supporting material and its model
prompt, and an invariant's subject. So does every list whose order decides, such as the moments an
ending announces and a contract's steps.

---

## What it took

**The first emission sealed both groups as one.** The vocabulary renderer read the group from the
first row and placed every entry under it. Construction still measured 100%, because the measure
reads whether each value is present, not where it sits.
`transformation/build/render.py` now renders each row under the group it states. A vocabulary of
one group renders as before. The second group's casing is now a fact, so the measure counts 30
facts, not 29. Construction acceptance reproduces the vocabulary with no field difference.

---

## What is carried

- **The vocabulary names keys.** A key named here and later reused for data would be misread. The
  comparison that reads this vocabulary exempts a documentation key only where its value is text,
  and adding to the vocabulary is a reviewed change.
- **The measure cannot see where a value sits.** A value rendered under the wrong key still counts as
  determined. This change found that limit, and construction acceptance is what caught it.
