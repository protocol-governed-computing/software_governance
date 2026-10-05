# Business Problem Statement

**Project Name:** platform — reference semantics

## 1. Context

An artifact names other artifacts: the rule that governs it, the capability a step runs, the actor
an act admits, the moment it announces. When an artifact is stood down, everything that names it must
name its successor or be stood down with it. A reference changed only to name the successor keeps the
referring artifact's identity, because it says the same thing about a newer version of the same
thing.

The platform declares which parts of a declaration carry no meaning. It does not declare which parts
name another artifact. Three places decide that today, each in its own way, and they disagree:

- The record of what refers to what reads a fixed list of nine parts. It misses the rest. The rule
  that governs assertion is named by 138 artifacts and recorded as referred to by one. The actor a
  phase admits is named by 39 and recorded as referred to by none.
- The check that nothing reaches a stood-down artifact reads every value anywhere that looks like a
  name.
- The comparison of a change with what it changes has no notion of a reference at all.

So a change that stands an artifact down cannot learn what reaches it. And a reference re-pointed to
a successor reads as a change of meaning, so every replacement would ripple through everything above
it.

The declaration of what carries no meaning also leaves one thing unsaid. A part declared explanation
is exempt only where its value is text. Where it holds anything else, it commits the artifact to
something.

---

## 2. Problem Statement

**Nothing declares which parts of a declaration name another artifact, so three parts of the platform
decide it three ways.**

This change shall:

- declare, in the place that declares what carries no meaning, which parts of a declaration name
  another artifact;
- declare there that a reference now naming the declared successor of what it named is not a change
  of meaning;
- declare there that a part declared explanation is exempt only where its value is text;
- have the record of what refers to what, and the check that nothing reaches a stood-down artifact,
  read that one declaration;
- refuse a full name written in a part that the declaration does not name a reference.

### What the business already decided

These are settled and are not reopened by this change:

- **A change of meaning is a new identity; a change of how it is written is not.**
- **What carries no meaning, and what names another artifact, is declared, never inferred.**
- **A reference to a stood-down artifact is re-pointed or retired.** Re-pointing keeps the referring
  artifact's identity.
- **Adding to the declaration is itself a change of meaning.** The declaration is replaced by a new
  version, and the old one stays in the record and out of reach.

---

## 3. Clarifications answered by the business author

- **Is this the last change to this declaration in this cycle?** Yes. Everything the next changes need
  from it is declared here.
- **Does this change compare amendments, or check what a replacement reaches?** No. The design and
  build changes that follow do, and they read this declaration.
- **Is a full name written in a part not declared a reference refused?** Yes. Otherwise the check
  that nothing reaches a stood-down artifact would see less than it does today.
- **Are names written by short code covered?** No. A workflow names its places and contracts by
  short code, and the compiler already resolves those its own way. Declaring them is later work.
