# Business Problem Statement

**Project Name:** platform — capability side effects

> **This dossier records a change that has already been made.** The capability gained an operation
> before the boundary that governs such a change was stated, and this is the record it should have
> had. It is retrospective by construction and by admission.

## 1. Context

A capability side effect is the platform's offer of a thing the business cannot do for itself:
holding a record, appending to a trail, reading a clock. A domain composes what a capability offers.
It does not decide what is on offer, because every domain reaches the same capability and a change to
one is a change for all of them.

`CS_MUTABLE_JSON_V0` holds durable records addressed by key. It offered writing a record, reading one
back, listing the keys it holds, updating in place and deleting.

## 2. Problem Statement

**The capability gained an operation, and no dossier records it.**

A domain needed to search what it held. Answering a question about a collection means seeing the
records themselves and selecting among them by content; the capability offered a way to list the
keys records are filed under, and no way to read the records. That need is not particular to any
domain — any subdomain holding a collection reaches it the moment it must answer a question about
the collection rather than about one member of it.

So `SELECT` was added — *read every record in storage, for a caller that selects among them by
content*. It is declared on the capability today, published on the capability surface, reached by
two contracts of the domain that needed it, and running.

**It was a platform change made inside a business change request.** The design that needed the
operation inventoried the capability as an artifact it extends, and that is how the extension was
carried: a domain declaring an amendment to something it does not own. Every check in the workspace
passed, because nothing asked whether a business change request may amend a platform capability. The
platform's own rule says it may not — *a domain extends the platform by adding artifacts in its own
namespace, and never modifies one in the platform's*.

**The domain that needed it is one this platform does not require**, and a later composition may not
contain it. That is the point rather than a caveat: the operation is part of the platform's offer for
good, and the reason it is offered is currently recorded in a change request that may not be present
to read.

Two facts make this worth a dossier rather than a note:

- **The operation is right and nothing is being undone.** A read that answers with records is what a
  search needs, it is declared as a read, and it is in use. This change does not propose to remove
  it.
- **The record of why it exists lives in another domain's change request.** The reason a platform
  capability offers `SELECT` is written down in the dossier of the domain that first needed it, which
  is the wrong place: the next domain that reaches for it finds an operation whose justification
  belongs to somebody else's change, in a domain it may not have.

This change shall:

- record the operation as a platform change, with the business reason it was added;
- state what the capability offers as a whole, so a reader learns the surface from the capability
  rather than from the first domain that needed it;
- record that the change crossed an authority boundary, and that the boundary is now stated.

### What this change does not decide

- **Whether `SELECT` should exist.** It exists, it is correct, and it is in use.
- **Whether the domain that needed it was wrong to need it.** The need was real and the operation
  answers it.
- **What other capabilities should offer.** Each is its own question.

---

## 3. What governs this today

The platform surface is closed: a capability side effect is admitted only where the closed set names
it, and the compiler refuses an undeclared one. What the closed set does not say is **who may change
what an admitted capability offers**. The rule that a domain never modifies a platform artifact is
stated as platform doctrine and was, until now, enforced by nothing a design could fail.

That is what changed. A design may no longer claim to amend an artifact whose family it cannot
author, so the act this dossier records could not be performed the same way again.

---

## 4. Clarifications — answered

### Answered

- **Is a retrospective dossier worth opening for a change already delivered and working?**
  **Yes.** The operation is part of the platform's offer and will be read by every domain that comes
  after — including domains not yet written, and compositions that do not contain the one that
  needed it. A capability whose surface is explained in another domain's change request is a
  capability whose reasons are unfindable, and the next person to need one of its operations has no
  way to know which are load-bearing and which were added for one caller.

- **Should the change be re-delivered through the pipeline?**
  **No.** There is nothing to deliver: the operation is declared, compiled and in use. What was
  missing is the record, and the record is what this dossier is.

- **Does recording it retrospectively weaken the boundary it violates?**
  **No — the opposite.** The boundary was stated after the act, so the act was not a breach of a rule
  in force. Recording it is what makes the boundary's first instance visible rather than absorbed,
  and this dossier is the evidence that the rule now has something to point at.
