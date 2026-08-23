# Business Problem Statement

**Project Name:** platform — structure

## 1. Context

Every governed artifact declares itself in a machine block, and a schema states what a declaration of
that kind may contain. A dispatch table names which schema governs which kind, and the build reads
that table: a kind the table names is validated against its schema, and a kind the table does not
name is validated against nothing.

## 2. Problem Statement

**Schema governance has the shape of the defect it exists to prevent: a surface that is declared,
unread, and rotted.**

**A third of the composition is governed by no schema.** Six artifact kinds are named by the dispatch
table nowhere — actors, events, intents, structures and both transport boundary kinds. That is 139 of
428 artifacts. Four of the six have a schema sitting beside the others, written and never named.

**The schemas that exist have rotted, and being unread is why.** Dispatching them refuses one hundred
declarations, and not one of the hundred is a defective artifact. Sixty-two expect an artifact to name
its constitution by a bare name where every artifact now carries a fully qualified one. Twenty-two
describe an actor that has a role and no attributes, which is not the actor the platform builds.
Ten forbid content an event legitimately carries. Five reject a whole number because the schema's
list of admissible types omits it. **The artifacts are current and the schemas are not.**

**Two kinds have no schema at all.** The transport ingress and egress contracts — forty-four
artifacts carrying the boundary a caller reaches the composition through — are governed by no closed
surface.

**And five schemas that are dispatched do not close their surface**, so a declaration of those kinds
may carry content nothing declared.

## 3. Why This Surfaced Now

**Closing an unrelated finding required dispatching what was already there.** A finding recorded that
five schemas left their surface open. Measuring it found the larger fact: most kinds were not
dispatched at all, and the schemas for four of them had been rotting since a namespace change moved
every artifact's constitution reference.

**Nothing reported any of it, because nothing read any of it.** This is the same failure as a
published conformance profile whose required artifacts stopped resolving: a declaration nobody
consults cannot be found wrong.

## 4. What This Is Not

**It is not a case for dispatching every kind.** A stale schema turns valid governed content into
false refusals — one hundred of them, measured. More schema coverage is not automatically more
governance; coverage by a wrong schema is worse than none, because it refuses correct work with the
authority of a rule.

**The 139 undispatched artifacts are not defects.** Nothing establishes that every artifact kind
requires a schema. What is unresolved is which kinds do, and what the current shape of each is —
and that question has to be answered before any of them is dispatched.
