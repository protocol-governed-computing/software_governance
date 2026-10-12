# Closure — data_parts

**Phases reached:** P0 – P6, every one admissible
**Status:** COMPLETE. P6 is this dossier's terminal phase, by ruling
**Delivery:** authored, by a person, under this dossier
**Gate 1:** CLOSED at P6 by the business author, against composition `87c838e390b2…`
**Unblocks:** vectors for the transforms that render a design and attribute what it renders

---

## Why P6 is terminal

The governance surface is authored, not constructed. This change gives the vocabulary that declares
how a declaration is read a new version, and a vocabulary of the platform is not an artifact the
design language can author or the renderer can build.

## What the phase run established that the problem statement did not

- **A data part needs no new mechanism.** The supersession parts already name without reaching, and
  the one walk that finds references already passes over them. A data part is a new group of an
  existing vocabulary, read the same way.
- **The natural name was the wrong one.** A part is declared by name across every kind. `bindings`
  reads most naturally for what a case hands a transform, but a runtime binding's `bindings` name
  the capabilities it binds. Declaring it data would have stopped every binding's references being
  checked. `cases` is used by vectors alone.
- **Versioning is part of the change.** The build and the sameness comparison each read the
  vocabulary by its exact identity, so both name the new version, and the old one stands down.

## What delivery looks like

- `artifact::VOCAB_DECLARATION_REPRESENTATION_V1` supersedes V0 and adds the `data` group, holding
  `cases`.
- The compiler's representation reads V1, and its walk passes over a data part as it passes over a
  supersession part.
- The sameness comparison names V1.
- The reference semantics test proves a full name under `cases` is not a reference, and `target`
  still is.

## What is deliberately left open

- **Any other data part.** Nothing needs one today. Each is declared, by name, when it is needed.
