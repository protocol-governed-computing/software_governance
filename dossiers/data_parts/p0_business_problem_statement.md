# Business Problem Statement

**Project Name:** platform — artifact

## 1. Context

The platform reads every declaration the same way. A name written in a part the platform declares a
reference is a reference: the compiler resolves it, and refuses the declaration when it resolves to
nothing. A name written in any other part is refused as undeclared, because what names another
artifact is declared, never inferred. One kind of part is the exception today: a supersession part
names the artifact one replaced without reaching it, and is not read for references.

A test vector states what a transform must return. Its cases hold the values a transform is handed
and the values it must give back. They are data.

## 2. Problem Statement

**A test vector cannot hold a value that looks like a name.** The platform reads a vector's cases the
way it reads any declaration. A value written as a full name, inside the data a case hands a
transform or expects back, is read as a reference. It resolves to nothing the vector meant to point
at, and the declaration is refused.

**The transforms that most need vectors are the ones that cannot have them.** A transform that turns
a design into artifacts is handed designs that name artifacts, and returns artifacts that name the
constitutions that govern them. Every input and output it has carries names. No vector can state
what it is handed or what it returns, so the transform is never proven, and the rule that every
transform carries a vector cannot be met by the transforms that build the platform's own changes.

## 3. Requested Outcome

The platform declares that a vector's cases are data. A value inside them is a value, whatever it
looks like, and is never read as a reference. Everything outside them is read as it is today, so the
transform a vector tests is still a reference the compiler resolves.

## 4. Scope

In scope: the declaration of what is data, and the readers that find references, which read it.

Out of scope: what any vector states, which vectors any domain carries, and any other part of how a
declaration is read.

## Clarifications answered by the business author

- **Why not make every unrecognised name a value?** Because then a misspelled reference would pass
  as a value, and the rule that a reference is declared would stop catching anything. The data parts
  are declared, one by one, as references are.
- **Which part is data?** The cases of a vector, and nothing else today. The transform a vector
  tests is outside its cases and stays a reference.
