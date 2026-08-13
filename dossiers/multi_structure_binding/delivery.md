# Delivery — multi_structure_binding, first pass

**Authorized by:** Gate 1, closed at P6 against composition `dd8da7a04010…`
**Delivered:** the governance surface, and the mechanism — an act may declare a reach, the
composition resolves it, and a write through it is refused
**Not adopted:** no act declares one yet. The first adoption is `cr_05_wallet_reach` in `blockchain`

---

## What was authored

**`CONSTITUTION_RUNTIME_BINDING_V0` §2a — Storage Resolution.** The model, stated for the first
time: a record is described once by its owner; a description stays with its owner; the owner is the
only writer; a reach reads and never writes; a reach stays inside its domain; a reach is declared by
the act that reaches, which distinguishes what it owns from what it consults.

The clause says plainly that **an act operates under one binding today and that is the case of one**.
The model admits several; what it states holds however many there are. Four rule statements were
added alongside, and §4 gained the validation rule the invariant enforces.

**`INVARIANT_RB_STORAGE_SUBDOMAIN_OWNED_V0`** — a binding names the storage description its own
subdomain wrote. This is the narrow, checkable half of the model, and it is the half that matters
first: the workaround an act reaches for today is to describe another subdomain's records in its
own description, which works, needs nothing from the platform, and passed every check. The invariant
closes that route while the wider change is still being made.

**`assert_rb_storage_subdomain_owned_v0`** in the compiler, with its registry entry. An invariant
derives its assertion automatically, so an invariant without a handler fails the build — the two are
one delivery.

## What it cost to make the rule real, which is the part worth reading

The invariant was declared, the build passed, and **it was checking nothing.** Three separate
reasons, found in order, each the same shape:

1. **The handler could not see ownership.** Subdomain ownership is derived from `module_path` and
   nothing else, and the artifact projection handed to assertions dropped it. Both sides read
   `None`, compared equal, and passed. Fixed by carrying the fact the node already holds into the
   handler view — `s4_govern._project_single_node`.
2. **The handler could not see storage descriptions.** It indexed them by artifact kind, and a
   storage description does not reach that stage as a `STRUCTURE` — the kinds present are the
   executable families plus `GOVERNANCE`. The index was empty, every binding took the
   "another assertion's business" skip, and the rule passed on everything. Fixed by indexing on
   identity, which is what a binding names.
3. **The skip itself was unfounded.** Nothing else asserts that a binding's `storage_structure`
   resolves. The skip now reports.

A fourth thing was got wrong and corrected by the composition rather than by reasoning: treating an
absent subdomain as indeterminate. The conformance workload declares no subdomains at all, so its
binding and its description are both domain-owned and agree — `None` is a value, and refusing it
would have refused a composition for being simple. Ownership is now compared as `(domain, subdomain)`,
which also catches a binding naming another *domain's* description.

**Proved by tampering, both ways.** Pointing the wallet binding at identity's storage:
`E701_ASSERTION_FAILURE: ASSERT_RB_STORAGE_SUBDOMAIN_OWNED_V0 — 1 violation(s)`. Pointing it at a
description nothing declares: refused, and by this assertion as well as the surface-closure one.

## The mechanism — second pass

**What an act declares.** `SCHEMA_WORKFLOW_V0.json` gains `consults`: the bindings an act reads and
never writes, alongside the one it owns. Exactly one owned binding, because an act writes what it
owns and ownership that is shared is not ownership. Absent from an act that reads only its own
records, which is every act today.

**What the composition seals.** The compiler composes, per act, one storage description from the
bindings it operates under, and marks every entity:

```
ACTORS                   reach=consulted  described_by=blockchain::RB_IDENTITY_BINDINGS_V0
CONTACT_ADDRESS_REGISTRY reach=consulted  described_by=blockchain::RB_IDENTITY_BINDINGS_V0
ACTOR_OCCURRENCES        reach=consulted  described_by=blockchain::RB_IDENTITY_BINDINGS_V0
WALLETS                  reach=owned      described_by=blockchain::RB_WALLET_BINDINGS_V0
WALLET_IDENTITIES        reach=owned      described_by=blockchain::RB_WALLET_BINDINGS_V0
WALLET_OCCURRENCES       reach=owned      described_by=blockchain::RB_WALLET_BINDINGS_V0
```

Keyed by act rather than by binding, because a binding is shared: two acts may own the same one and
consult different others, and composing into the binding would hand each act the other's reach.

**What the runtime does.** It is handed the composed description instead of the single one, and
refuses a write where the entity reads `consulted` and the operation declares `effect: write`. **Two
declared facts and no inference** — and the second of them is the `effect` declaration delivered
earlier in the same session, which is what makes the refusal exact rather than a guess from an
operation's name.

**Where the owned binding comes from.** The declaration, not the edge graph. An edge kind is derived
from the two node kinds, so a consulted binding produces a `WF_BINDS_RB` edge indistinguishable from
the owned one — and which binding an act wrote through would have depended on edge order.

**A projection key is written where the materializer names it.** The composition was built, sealed
into the projection, and written nowhere: `s7_materialize` enumerates the keys it writes. A key
absent from that list is sealed nowhere and read by nothing, and the build stays green.

## Proven against the real composition, then reverted

The wallet act was given its declaration by hand, and the composition ran:

```
CREATE WALLET for an accepted actor                    SUCCESS
  wallets.json, wallet_identity_registry,
  wallet_occurrences                                   written
  actors.json, contact_address_registry,
  actor_occurrences                                    read, never written
```

And the refusal, by pointing a wallet step's write at a consulted store:

```
CREATE WALLET for an accepted actor                    VIOLATION
```

**The hand edit was then reverted.** The act's declaration is a change to a domain artifact, and a
domain change goes through the lifecycle this mechanism exists to enable — it is raised as
`blockchain/cr_dossiers/cr_05_wallet_reach`. The run above is evidence that the platform capability
works, not a delivery of the domain's adoption of it. With the edit reverted the act stops again, at
the same step, with the same message, which is correct until that change request lands.

## What remains

**The design language.** `transformation`'s P7 register states where an act's records live and
cannot yet state a reach, so `cr_05` will declare its reach in a document the phase rules cannot
check and construction cannot render. That is the last piece, and it is the one the wallet's change
request will run into.

**The runtime property held.** The dossier's §5 predicted `protocol_runtime` would need nothing if
the compiler sealed a composed description. It needed two things: to carry the composed description
to the step, and to refuse the write. Neither resolves anything — the runtime still reads what it is
handed — but the prediction was not free, and it is worth recording that it cost two changes rather
than none.

**Two obligations of the model are stated and not yet enforced**, deliberately and visibly: that a
record is described exactly once across the composition, which belongs at assembly where descriptions
meet, and that a reach is read-only at run time, which needs the mechanism before there is a reach to
hold. Both are in the clause. Neither has a rule yet, and the dossier says so rather than leaving the
reader to discover it.
