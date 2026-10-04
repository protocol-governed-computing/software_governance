# Business Problem Statement

**Project Name:** platform — identity semantics

## 1. Context

An artifact's identity names what it means. The open standard requires that a change to what an
artifact means is a new identity, and that a change to how it is written keeps the identity it has.
How it is written covers its wording, its layout, and the order of a list whose order says nothing.

The platform cannot tell the two apart. Every part of an artifact's declaration looks the same to
it: a sentence that explains, a route that decides, and the order in which a set happens to be
written. So nothing can say whether a change kept an artifact's meaning, and a change of meaning has
been written under an old identity again and again. A composition cited under one version then means
something different from the next composition, under the same names.

---

## 2. Problem Statement

**Nothing declares which parts of an artifact's declaration carry its meaning.**

This change shall:

- declare, in one place, which parts of a declaration explain and never carry meaning;
- declare, in the same place, which lists carry no meaning in their order;
- leave every other part of a declaration as carrying meaning.

### What the business already decided

These are settled and are not reopened by this change:

- **A change of meaning is a new identity; a change of how it is written is not.**
- **What carries no meaning is declared, never inferred.** A part is not explanation because it
  reads like prose.
- **Adding to the declaration is itself a reviewed change.**

---

## 3. Clarifications answered by the business author

- **Is everything not declared taken to carry meaning?** Yes. The declaration lists what is exempt,
  and anything it does not list counts.
- **Does this change decide which past changes altered meaning?** No. That is the next change, and it
  reads this declaration.
