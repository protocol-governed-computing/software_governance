# Business Problem Statement

**Project Name:** platform — published rules keep their meaning

## 1. Context

A composition is published, and what it publishes is fixed: each identity in it means what it meant
on the day it was sealed. A rule that changes what it requires is a new rule, with a new identity, and
the old one stays in the record as it was.

Two rules the platform published in v5 changed what they require during this cycle, under the same
identity:

- **The rule that a step routes every outcome it can produce.** In v5 it compared a step's routes with
  the outcomes the step's author listed. It now also requires that list to hold every outcome the
  capability declares, and its check enforces that. A composition v5 admitted can now be refused by the
  rule v5 named.
- **The rule that governs the run's record.** In v5 it required every line of a trace to conform to the
  first version of the trace schema. It now names the second. A trace v5 wrote no longer conforms to
  the rule that v5 says it conforms to.

Both changes were right. They were made in place.

---

## 2. Problem Statement

**Two published rules require more than they did when they were published, under the identities that
were published.**

This change shall:

- give each changed rule a new identity that says what it now requires;
- return each published identity to what it said when it was published, and stand it down;
- point everything that names a changed rule at its successor;
- keep every check enforcing what it enforces today, under the identity that now says so.

### What the business already decided

These are settled and are not reopened by this change:

- **Identity is fixed at publication.** An unpublished identity may change before release; a
  published one may not.
- **A change of meaning is a new identity.** The old one stays in the record and out of reach.
- **What the two rules now require is right.** Nothing they enforce is relaxed.

---

## 3. Clarifications answered by the business author

- **Does any composition change what it does?** No. The checks and the trace are those of today; only
  the identities that state them change.
- **Is the old check kept?** Yes. Each stood-down rule keeps the check that realized it when it was
  published, so the record says what was enforced under it.
