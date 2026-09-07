# Business Problem Statement

**Project Name:** platform — runtime binding

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed platform
> requirement and the execution path a change would take. It is not a design.

## 1. Context

A subdomain owns what it holds, and declares where its own records live. That declaration is the
subdomain's, maintained by whoever answers for the records it describes.

An act performed in one subdomain routinely needs to establish something another subdomain owns. The
act does not want a copy of that fact: a second copy of one truth can disagree with the thing it
describes, and then the business holds two answers and can defend neither. So the act reuses the
owning subdomain's capability for establishing it, rather than restating what the fact is.

**That arrangement is the one the composition exists to encourage**, and it is not particular to any
domain. Wherever one part of a business must confirm something another part is answerable for —
that a party is known before it may be transacted with, that a resource exists before it may be
committed, that a permission was granted before it may be exercised — the same shape appears: an act
here, a fact owned there, and a capability already written to establish it.

---

## 2. Problem Statement

**An act may reuse a capability from another subdomain, and cannot reach the records that capability
reads.**

A runtime binding names **one** place where storage is described. Every capability the act performs
resolves its records against that one place. An act that reuses a capability belonging to another
subdomain therefore asks for a record its own binding has never heard of, and is refused at the
moment it runs.

The reuse the composition encourages is therefore the thing it cannot carry out. An act may compose
another subdomain's capability, and the moment that capability reaches for the records it was
written to read, the act stops.

**The requirement is confirmed rather than anticipated, and one composition is where it surfaced.**
The instance below belongs to a business domain this platform does not require and a later
composition may not contain. It is evidence that the shape occurs and costs what it is claimed to
cost — not the problem itself, which is a property of how any act resolves its records.

In the composition that surfaced it, an act creating a wallet for a person reuses the identity
subdomain's contract for establishing that the person exists and has been accepted. Its binding names
the wallet subdomain's storage, which describes three wallet records and no people. The act is
admissible at every phase of design, complete at every fact construction requires, compiles, verifies
and attests — and stops on its second step:

```
PROTOCOL VIOLATION: Entity 'ACTORS' not found in STRUCTURE entity_stores.
Available entities: ['WALLETS', 'WALLET_IDENTITIES', 'WALLET_OCCURRENCES']
```

**Nothing in the design language can express the intent, so nothing refuses it either.** The design
says which capability the act reuses and where the act's own records live. It has no way to say
"and this act also reads what another subdomain holds", so the omission is invisible until execution.

Two ways of avoiding the problem were examined and rejected:

- **Let the reaching subdomain describe the other's records too.** It works today and is the reason
  this is a problem worth stating rather than a defect worth patching: it puts one subdomain's
  storage description inside another's, so two subdomains declare where one record lives, and the
  second copy is the one nobody maintains.
- **Stop reusing the capability, and give the reaching subdomain its own way to establish the fact.**
  That is a second implementation of something another subdomain already owns, which is the
  duplication the composition exists to prevent.

This change shall:

- let one act reach the records of more than one subdomain, by naming each place they are described;
- keep that reach read-only, and make the platform able to tell a read from a write so it can be held;
- keep every record described exactly once, by the subdomain that owns it;
- make the reach visible in the design, so that reading across a boundary is something a reviewer
  sees rather than something a run discovers.

### What this change does not decide

- **Which acts should reuse which capabilities.** That is each domain's business, stated in its own
  change.
- **Whether one subdomain should read another at all.** Some do; this change follows that fact.
- **Which records a subdomain owns.** Ownership is settled; this change is about reach, and reach is
  now ruled read-only (§6). What it does not decide is how a subdomain's ownership is *declared*.

---

## 3. What governs this today

**Almost nothing, and the little there is says only how the field is shaped.**

`storage_structure` appears in exactly one governance artifact: `SCHEMA_RUNTIME_BINDING_V0.json`,
where it is `{"type": "string"}` with the description *"FQDN of the storage structure artifact
governing this binding's storage layout"*. No constitution mentions it. No invariant mentions it.
`entity_stores` — the declaration of where records live — is named in no constitution at all.

So the singular is a JSON type, not a governed statement. There is no clause saying an act resolves
its records against one description, and no clause saying why it should.

**This change therefore does two things at once, and they should be distinguished.** It amends a
schema, which is a shape. And it **states the storage resolution model for the first time**, which is
a governing statement the composition has been operating without: what an act may reach, whose
description is authoritative for a record, and what happens when two descriptions disagree.

---

## 4. Three shapes the answer could take

**The business author has since ruled for B (§6).** The three are kept as authored because the
choice was not obvious, all three were reachable from the problem as stated, and a design that
reopens the question should meet the alternatives and the reasons rather than the conclusion alone.
What follows is the record of what was weighed, not a question still open.

What makes the choice live is that **two** declarations are singular here, not one. A runtime binding
names one place where storage is described, and a workflow names one runtime binding — `rb_addr` is a
single value resolved once per act and handed to every step it performs. So the reach can be widened
at either level, or at neither.

### A — a binding names several places

The binding an act operates under describes storage in more than one place, and the act reaches all
of them.

*For:* the smallest change, and the act's whole storage surface is visible in one artifact.
*Against:* the reaching subdomain's binding would name where the other's records live, so an artifact
one subdomain owns carries a statement about another's storage. Ownership survives in principle and
is harder to see in practice.

### B — an act operates under several bindings

The act names the other subdomain's binding as well as its own, and each binding stays owned and
maintained by the subdomain that wrote it.

*For:* no subdomain's artifact makes a statement about another's storage; the reach is declared as a
relationship between subdomains rather than absorbed into one.
*Against:* a binding carries capability policy as well as storage, so two bindings raise the same
disagreement question one level up — and the runtime resolves one binding per act today, which is a
deeper change than widening a field.

### C — a reused capability resolves against its owner's binding *(pruned by §7)*

Nothing is declared. A capability belonging to another subdomain resolves its records the way that
subdomain resolves them, because the composition already knows who owns it.

*For:* nothing to state, nothing to keep in step, and no disagreement is possible — each record is
resolved by exactly the binding its owner wrote. It answers the "must the owner agree" clarification
by construction: the owner's own binding is what governs the read.
*Against:* it is resolution by inference rather than declaration, which is the opposite of how this
platform decides everything else. The act would reach across a boundary with nothing in its design
saying so, which is the visibility this change set out to gain. It also removes the caller's ability
to bind a capability differently, and whether any caller should have that ability is itself unsettled.

---

## 5. The execution path a change would take

Four repositories, in dependency order. Recorded so the scope is visible before anyone begins.

| # | Repository | What changes |
|---|---|---|
| 1 | `software_governance` | States the resolution model for the first time: what an act may reach, whose description is authoritative for a record, and what happens when two disagree. Amends the workflow schema, which is the declaration B widens — an act names the bindings it operates under, and each stays owned by the subdomain that wrote it. Adds the invariant that holds the model, because a resolution rule nothing checks is a sentence. |
| 2 | `protocol_compiler` | Resolves each named description and seals the composed result into the binding policy. Today it looks up one (`projections/handlers.py`), and `ASSERT_RB_BINDING_POLICY_CONFORMANCE_V0` checks the one it finds. |
| 3 | `protocol_runtime` | Nothing, if the compiler seals a composed description. The runtime reads what it is handed and never resolves for itself, and that property should survive this change rather than be spent by it. |
| 4 | `transformation` | The design register that declares a binding's storage, so a design can name several and a reviewer can see which boundaries an act reaches across. |

**Amending only the fourth would be a defect, not a partial fix.** A design could declare that an act
reaches two subdomains while the running system resolves one, silently — the same class of failure as
a field that is declared and read by nothing.

**Amending only the first two would leave it unsayable.** The reach would work and no design could
state it, which is how it came to be discovered at execution in the first place.

Under shape C the fourth row would be empty by design, and that was the strongest argument against
it: a reach nothing declares is a reach no reviewer sees.

---

## 6. Clarifications — answered

All five are answered by the business author. No clarification blocks the phase run.

### Answered

- **Does reaching another subdomain's records permit changing them, or only reading them?**
  **Read-only, never write.** A subdomain owns what it holds, and ownership that does not include
  being the only writer is not ownership. An act may consult what another subdomain holds because a
  second copy of one truth can disagree with the thing it describes; it may not change it, because
  then two subdomains decide what is true and neither is answerable for the result.

  **The consequence, accepted deliberately:** the reach must be scoped, not merely granted. Whatever
  shape §4 takes, naming another subdomain's storage cannot be the same act as being permitted to
  write to it.

- **When two descriptions name the same record differently, what happens?**
  **The composition is refused, when it is assembled.** Not a precedence rule: this change already
  requires every record to be described exactly once by the subdomain that owns it, so two
  descriptions of one record is the state the change exists to prevent, and a rule for choosing
  between them would license it. Refusal is not conflict resolution — it is the check that
  once-only held.

  The composition already answers the same question one level up and answers it this way: a platform
  artifact is copied into every domain's compiled output, the copies can disagree, and the assembler
  compares every copy of an identity and refuses the composition rather than answering from whichever
  the index resolved. Refusal belongs at assembly for the same reason: descriptions are sealed, so
  two descriptions of one record is a property of the composition, not of a run.

- **May an act reach across domains, or only across subdomains of its own domain?**
  **An act may reach what its own domain holds, and no further.** A domain is what a profile selects,
  so an act reaching another domain's records is correct only in the compositions that happen to
  include it: it would compile, verify and attest in one and fail at execution in another, with
  nothing in the design showing why. That is this change's own founding defect, one level up.

  A dependency on another domain is not forbidden — it is a different kind of thing, and it goes
  through that domain's capability, which is declared and resolvable, rather than through its
  storage, which is a private arrangement. Whether a domain may depend on another at all is a
  question about composition profiles and is answered there.

- **Is naming another subdomain's storage enough, or must that subdomain agree?**
  **Naming is enough, and the naming is done by the act that reaches.** Consent would have to live in
  the owner's artifact as a list of who may read, so every new reader would amend an artifact it does
  not own, and that list would accumulate readers nothing keeps in step with the readers themselves —
  the second-copy problem this change exists to remove, pointing the other way. A domain already
  extends the platform by adding artifacts in its own namespace and never modifying what it does not
  own; a reach declared by the reacher is that same shape.

  Two things make this a boundary rather than a courtesy: the reach is read-only, so the owner stays
  the only writer, and the reach is declared where a reviewer reads it.

  **Not decided here:** whether a subdomain may hold records that only some readers may see. That is
  access control, it needs its own mechanism, and no act in the composition needs it.

- **Does an act's own records need to be distinguishable from those it merely reaches?**
  **Yes, and the read-only ruling is what forces it.** If reach is read-only and ownership is write,
  a declaration that lists places without saying which of them it owns has granted the permission and
  hidden the distinction the permission rests on. Nothing downstream could refuse a write to a
  reached store, because nothing downstream could tell which store was reached.
  `CROSS_SUBDOMAIN_REACH_READ_ONLY` holds this at design time today; its runtime counterpart cannot
  exist without the distinction.

- **Which of §4's shapes shall the declaration take?**
  **Shape B — an act operates under several bindings, each owned by the subdomain that wrote it.**

  This is a business constraint rather than a design preference, and it is the same constraint stated
  three times over: a subdomain's storage description stays in that subdomain's own artifact,
  maintained by the people answerable for it. Shape A puts a statement about where one subdomain
  keeps its records inside an artifact another subdomain owns, and the maintainer of that statement
  is then not the owner of what it describes — which is the second-copy problem in §2's first rejected option,
  arriving by a different route.

  It also makes the distinction the previous ruling requires free rather than added: the binding an
  act owns is its own, every other binding it names is reach, and no marker has to be invented to
  tell them apart.

  **The cost is accepted, and it is stated in §4:** the runtime resolves one binding per act today,
  so this is a deeper change than widening a field. The reach is a relationship between two
  subdomains, B is the only shape that declares it as one, and paying for that in the runtime is
  preferred to recording it in a shape that reads as one subdomain describing another's storage.

---

## 7. What the answer requires that does not exist yet

**The composition cannot tell a reading operation from a writing one.** The ruling above is therefore
correct and, today, unenforceable — which is a finding rather than an objection, and it belongs in
this dossier because it is now part of the change.

What was looked for and is not there:

- **`core.semantics.durability`** is declared by exactly one capability, the inspection one, as
  `read_only` — and `INVARIANT_INSPECTION_CAPABILITY_READ_ONLY_V0` enforces it. `CS_MUTABLE_JSON_V0`
  and `CS_APPENDONLY_JSONL_V0` declare no durability at all. It is also capability-grained, and
  `CS_MUTABLE_JSON_V0` offers `READ` and `WRITE` from the same capability, so a capability-level
  answer cannot scope a step.
- **`idempotent`** is declared per operation and is not the same question. On `CS_MUTABLE_JSON_V0`,
  `READ`, `WRITE`, `UPDATE` and `DELETE` are all `idempotent: true` — a last-write-wins write is
  perfectly idempotent and still a write.
- **The operation names read as reads and writes** — `READ`, `LIST`, `SELECT`, `EXISTS` against
  `WRITE`, `UPDATE`, `DELETE`, `APPEND`, `REGISTER` — and reading intent out of a name is inference,
  not governance. A rule resting on it would be a convention nobody declared and anybody could break
  by naming an operation well.

**So the change gains a third obligation**, alongside stating the resolution model and widening the
declaration: **each operation declares its effect.** Without it, "read-only across a boundary" is a
sentence rather than a rule, and this dossier would ship the same defect it exists to close — a
statement nothing checks.

There is precedent for the shape: `durability` already exists as a declared semantic, and an
invariant already enforces it for one capability. This extends it from the capability to the
operation, and from one capability to all.

**And it prunes §4.** Shape C — a reused capability resolving against its owner's binding — declares
nothing at all, so there is nowhere to state that the reach is read-only and nothing to check it
against. A *writing* contract reached across a boundary would resolve and run exactly as a reading one
does. Under this ruling, C is no longer a live option unless the effect declaration alone is
considered sufficient scoping, which it is not: it would say what a capability does, never what this
act is permitted to do with it.

---

## 8. What the answers settle, and what they leave to design

The rulings bound the change without designing it.

- **Reach is read-only, stays inside a domain, is declared by the act that reaches, and distinguishes
  what the act owns from what it consults.** Those four bound any realisation of the ruled shape.
- **Two descriptions of one record refuse the composition at assembly**, which places one obligation
  outside the design layer entirely.
- **Every operation declares its effect** — delivered, and the read-only ruling rests on it.

**The shape is ruled: B**, an act operating under several bindings, each owned by the subdomain that
wrote it. What design still decides is everything about how B is realised — how an act names the
bindings it operates under, how the runtime resolves more than one, which of them a step's records
resolve against, and what a binding must say for the distinction between owned and consulted to be
readable. The constraint is that no subdomain's artifact describes another's storage; the mechanism
is design's.
