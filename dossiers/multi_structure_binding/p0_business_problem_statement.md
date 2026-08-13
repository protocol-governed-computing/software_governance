# Business Problem Statement

**Project Name:** platform — runtime binding

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed platform
> requirement and the execution path a change would take. It is not a design.

## 1. Context

A subdomain owns what it holds. The catalog owns its books, identity owns its people, and each
declares where its own records live.

An act performed in one subdomain may need to read what another holds. Creating a wallet for a person
means first establishing that the person exists and has been accepted — a fact identity owns and
identity alone should state. The wallet does not want to keep its own copy of who exists; a second
copy of one truth can disagree with the thing it describes.

So the wallet reuses identity's capability for resolving a person, rather than restating what a
person is. That is the arrangement the composition is meant to encourage.

---

## 2. Problem Statement

**An act may reuse a capability from another subdomain, and cannot reach the records that capability
reads.**

A runtime binding names **one** place where storage is described. Every capability the act performs
resolves its records against that one place. An act that reuses a capability belonging to another
subdomain therefore asks for a record its own binding has never heard of, and is refused at the
moment it runs.

**The requirement is confirmed, not hypothetical.** `blockchain::WF_CREATE_WALLET_V0` reuses
identity's `CC_RESOLVE_ACTOR_V0` to establish that the holder exists. Its binding names the wallet's
storage, which describes three wallet records and no people. The act is admissible at every phase of
design, complete at every fact construction requires, compiles, verifies and attests — and stops on
its second step:

```
PROTOCOL VIOLATION: Entity 'ACTORS' not found in STRUCTURE entity_stores.
Available entities: ['WALLETS', 'WALLET_IDENTITIES', 'WALLET_OCCURRENCES']
```

**Nothing in the design language can express the intent, so nothing refuses it either.** The design
says which capability the act reuses and where the act's own records live. It has no way to say
"and this act also reads what identity holds", so the omission is invisible until execution.

Two ways of avoiding the problem were examined and rejected:

- **Let the wallet describe identity's records too.** It works today and is the reason this is a
  problem worth stating rather than a defect worth patching: it puts one subdomain's storage
  description inside another's, so two subdomains now declare where people live, and the second copy
  is the one nobody maintains.
- **Stop reusing the capability, and give the wallet its own way to resolve a person.** That is a
  second implementation of a fact identity already owns, which is the duplication the composition
  exists to prevent.

This change shall:

- let one act reach the records of more than one subdomain, by naming each place they are described;
- keep every record described exactly once, by the subdomain that owns it;
- make the reach visible in the design, so that reading across a boundary is something a reviewer
  sees rather than something a run discovers.

### What this change does not decide

- **Which acts should reuse which capabilities.** That is each domain's business, stated in its own
  change.
- **Whether one subdomain should read another at all.** Some do; this change follows that fact.
- **Anything about writing across a boundary.** See the clarifications: whether reach implies the
  right to change what is reached is the sharpest question here, and it is not assumed.

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

**P0 does not choose between these.** They are recorded because the choice is not obvious, all three
are reachable from the problem as stated, and discovering the second and third at P7 would be
discovering them too late.

What makes the choice live is that **two** declarations are singular here, not one. A runtime binding
names one place where storage is described, and a workflow names one runtime binding — `rb_addr` is a
single value resolved once per act and handed to every step it performs. So the reach can be widened
at either level, or at neither.

### A — a binding names several places

The binding an act operates under describes storage in more than one place, and the act reaches all
of them.

*For:* the smallest change, and the act's whole storage surface is visible in one artifact.
*Against:* the wallet's binding would name where identity's records live, so a wallet-owned artifact
carries a statement about another subdomain's storage. Ownership survives in principle and is harder
to see in practice.

### B — an act operates under several bindings

The act names identity's binding as well as its own, and each binding stays owned and maintained by
the subdomain that wrote it.

*For:* no subdomain's artifact makes a statement about another's storage; the reach is declared as a
relationship between subdomains rather than absorbed into one.
*Against:* a binding carries capability policy as well as storage, so two bindings raise the same
disagreement question one level up — and the runtime resolves one binding per act today, which is a
deeper change than widening a field.

### C — a reused capability resolves against its owner's binding

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
| 1 | `software_governance` | States the resolution model for the first time: what an act may reach, whose description is authoritative for a record, and what happens when two disagree. Amends whichever declaration §4's chosen shape widens — the runtime-binding schema under A, the workflow schema under B, neither under C. Adds the invariant that holds the model, because a resolution rule nothing checks is a sentence. |
| 2 | `protocol_compiler` | Resolves each named description and seals the composed result into the binding policy. Today it looks up one (`projections/handlers.py`), and `ASSERT_RB_BINDING_POLICY_CONFORMANCE_V0` checks the one it finds. |
| 3 | `protocol_runtime` | Nothing, if the compiler seals a composed description. The runtime reads what it is handed and never resolves for itself, and that property should survive this change rather than be spent by it. |
| 4 | `transformation` | The design register that declares a binding's storage, so a design can name several and a reviewer can see which boundaries an act reaches across. |

**Amending only the fourth would be a defect, not a partial fix.** A design could declare that an act
reaches two subdomains while the running system resolves one, silently — the same class of failure as
a field that is declared and read by nothing.

**Amending only the first two would leave it unsayable.** The reach would work and no design could
state it, which is how it came to be discovered at execution in the first place.

Under shape C the fourth row is empty by design, and that is the strongest argument against it: a
reach nothing declares is a reach no reviewer sees.

---

## 6. Clarifications for the business author

> **These are unanswered.** No phase may proceed on a guess about them.

- **Does reaching another subdomain's records permit changing them, or only reading them?** The act
  that raised this only reads. A binding that grants reach without distinguishing the two would let
  one subdomain write into another's records, which is the boundary the composition holds most
  firmly.

- **When two descriptions name the same record differently, what happens?** A precedence rule — first
  named wins, or nearest wins — makes the composition depend on the order someone wrote a list in. A
  refusal makes a genuine conflict visible. Refusing is the stricter answer and this change should
  not assume it.

- **May an act reach across domains, or only across subdomains of its own domain?** The case in hand
  is one domain, two subdomains. Reaching into another domain entirely is a different question about
  what a domain boundary means.

- **Is naming another subdomain's storage enough, or must that subdomain agree?** The owner of a
  record may reasonably expect to say who reads it. The alternative is that any binding may name any
  description, and ownership becomes a convention rather than a boundary.

- **Does an act's own records need to be distinguishable from those it merely reaches?** A reviewer
  reading a binding should be able to tell what the act is responsible for from what it consults, and
  a flat list of places does not say which is which.
