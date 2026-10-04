# VOCAB_HUMAN_BLOCK_CONSTRAINTS_V0

## Machine

```yaml
fqdn: vocabulary::VOCAB_HUMAN_BLOCK_CONSTRAINTS_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: vocabulary
forbidden_section_names:
  casing: lower_snake
  domain_extensible: false
  entries:
  - header
  - header (mandatory)
  - rule
  - rule statement
  - rules
  - requirements
  - validation rules
  - enforcement scope
  - version history
  - status
restated_machine_keys:
  casing: lower_snake
  domain_extensible: false
  entries:
  - artifact code
  - artifact kind
  - governed by
  - version
  - status
  - supersedes
  - superseded by
  - fqdn
  - authority
  - concern
  - namespace
```

---

## Intent

The two closed name sets that decide whether an artifact's prose has started declaring something.

`forbidden_section_names` are section headings that announce a rule is being stated. The prose beside
a machine block is a realization document — it explains how declarations realize what the standard
requires — and a section called `Rule Statement` in such a document is a second specification with no
authority behind it.

`restated_machine_keys` are prose field labels naming a fact the machine block already declares.
A label alone is not a violation: a glossary may legitimately define *Namespace*. What makes it one
is the prose carrying the same **value** the machine block carries, because two copies of one fact
can disagree — and when this was first measured the prose copy was already the weaker one, a short
name where the declaration carried an identity.

---

## Where this is read

`.github/process/human_block_fidelity.py` reads both sets from the sealed composition and carries no
copy of its own. The check is a mechanism; this artifact is the policy. Adding a forbidden name is an
authoring act here, sealed and attested, rather than an edit to a script.

---

## What is not claimed

These two sets are what is mechanically decidable. They do not decide whether a sentence **cites** a
normative requirement or **restates** it — that is a reading rather than a pattern, and it is the
rule most likely to be broken. It is a review obligation, stated as one.

The doctrine these sets serve, and the reasoning behind it, is the Field Manual section *The human
block*. That is where it is explained; this artifact is where it is governed.
