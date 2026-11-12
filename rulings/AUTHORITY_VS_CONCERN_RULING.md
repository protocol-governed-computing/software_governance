# Is a federation boundary an authority, or a subject?

## Ruled: authority. The platform has one governance authority, and all twenty-six declared boundaries are one modeling error.

The current `fb.*` inventory does not represent a federation of governance authorities. It conflates
governance authority with semantic concern — and in the case of `governance`, encodes the root
authority itself as though it were one concern-bound boundary among peers. Twenty-five boundaries fail
to demonstrate independent authority; `governance` fails in the opposite direction, by being the
authority from which the others would have to be distinguished. One error explains all twenty-six,
with no exception.

`CONSTITUTION_FEDERATION_BOUNDARY_V0` defines a federation boundary as "a semantic sovereignty
construct, not an implementation packaging construct" — a declaration that a distinct governance
authority holds jurisdiction over a named set of protocol semantics. It adds an anti-sprawl rule: a
boundary "exists only when a distinct governance authority exists" and "MUST NOT be created
speculatively."

The surface declares one boundary per concern. Those two facts cannot both be right.

## The two dimensions

**Authority** is *who* may decide. **Concern** is *what* is being decided about. They are
independent: one authority may govern many concerns, and a concern may be organized, classified,
indexed and reasoned about without anyone acquiring jurisdiction over it.

```
authority:  pgc
concern:    structure
artifact:   STRUCTURE_IDENTITY_V0
```

The present encoding collapses this into a single identifier, `structure::STRUCTURE_IDENTITY_V0`,
where the namespace carries a concern but asserts an authority. Nothing in the artifact distinguishes
the claim it makes about jurisdiction from the classification it makes about subject matter.

## Why this is not a naming preference

Two boundaries already govern the same subject, from opposite directions.

`artifact` holds `INVARIANT_IDENTITY_FQDN_CONSISTENCY_V0`, declared `scope: ALL_ARTIFACTS` with
`applies_to_kinds` enumerating every kind — including `STRUCTURE`. Its invariants therefore bind
`structure`'s artifacts.

`structure` holds `STRUCTURE_IDENTITY_V0`, whose summary is "the canonical identity system for all
protocol artifacts" — which necessarily includes `artifact`'s.

Each governs artifact identity. Neither holds a decision the other is excluded from. The evidence
does not establish two distinct federation authorities; therefore these two namespaces cannot
presently be treated as two sovereign boundaries.

`scope: ALL_ARTIFACTS` is the sharper problem. Jurisdiction over a *named set* of semantics is what
the constitution requires; a rule asserting universal scope is the negation of a named set. A
boundary whose rules bind everything is not sovereign over anything in particular.

## The classification — all twenty-six boundaries

Jurisdiction is read from `applies_to_kinds` and `enforcement.scope` as declared, not inferred from
directory contents.

| Boundary | Constituting act | Declared jurisdiction | Overlaps | Reading |
|---|---|---|---|---|
| `actor` | yes | `AC` | — | kind-mirror |
| `artifact` | **none** | all 16 kinds, `ALL_ARTIFACTS` | everything | universal reach, unconstituted |
| `authority` | yes | `AC CC CS CT WF` | `capability_contracts`, `execution` | cross-kind, contested |
| `capability_contracts` | yes | `CC CS CT WF` | `authority`, `execution` | cross-kind, contested |
| `capability_side_effects` | yes | `CS` | — | kind-mirror |
| `capability_transforms` | yes | `CT` | — | kind-mirror |
| `compiler` | yes | `COMPILER` | — | kind-mirror |
| `conformance` | yes | `CC CS CT INVARIANT RB TEST_DATA WF` | the CC/CS/CT/WF cluster | cross-kind, contested |
| `cryptographic_trust` | yes | `SNAPSHOT`, `ALL_ARTIFACTS` | the SNAPSHOT cluster | snapshot-scoped |
| `event` | yes | `EV` | — | kind-mirror |
| `execution` | yes | `CC CS CT WF` | `authority`, `capability_contracts` | cross-kind, contested |
| `execution_placement` | yes | `SNAPSHOT`, `ALL_ARTIFACTS` | the SNAPSHOT cluster | snapshot-scoped |
| `execution_scheduling` | yes | `SNAPSHOT`, `ALL_ARTIFACTS` | the SNAPSHOT cluster | snapshot-scoped |
| `execution_topology` | yes | `CC CS CT RB TE TI WF` | the CC/CS/CT/WF cluster | cross-kind, contested |
| `federation` | yes | none exercised | — | constitution only |
| `governance` | yes | `CONSTITUTION INVARIANT` | — | governs governance |
| `intent` | yes | `IN WF` | `workflow` | kind-mirror, slight reach |
| `lifecycle` | yes | none exercised | — | constitution only |
| `runtime_binding` | yes | `RB` | — | kind-mirror |
| `security_domain` | yes | `SNAPSHOT`, `ALL_ARTIFACTS` | the SNAPSHOT cluster | snapshot-scoped |
| `structure` | yes | `STRUCTURE`, `global` | `artifact` | kind-mirror |
| `surface_contract` | **none** | `CC CS CT RB WF`, `ALL_ARTIFACTS` | the CC/CS/CT/WF cluster | cross-kind, unconstituted |
| `trace` | yes | none exercised | — | constitution only |
| `transport` | yes | `SNAPSHOT TE TI WF` | the SNAPSHOT cluster | mixed |
| `vocabulary` | yes | all 16 kinds | everything | universal reach |
| `workflow` | yes | `WF` | `intent`, the CC/CS/CT/WF cluster | kind-mirror |

## What the table shows

**Nine boundaries are kind-mirrors.** `actor` governs `AC`, `event` governs `EV`,
`workflow` governs `WF`, and so on — the boundary name is the artifact kind, and the jurisdiction
is that kind alone. "`fb.X` contains X artifacts" is a concern partition. No governance decision is
reserved to these that follows from authority rather than from subject matter.

**Six boundaries contest one jurisdiction.** `authority`, `capability_contracts` and
`execution` declare *the same four kinds* — `CC CS CT WF`. `execution_topology`,
`surface_contract` and `conformance` declare supersets of it. Six boundaries reaching the same
subjects is not six sovereignties; none of them can show a decision the others are excluded from.

**Four boundaries contest the snapshot.** `cryptographic_trust`, `execution_placement`,
`execution_scheduling` and `security_domain` each declare `applies_to_kinds: SNAPSHOT` with
`scope: ALL_ARTIFACTS`. Their subject is the same object.

**Two claim universal reach.** `artifact` and `vocabulary` both enumerate all sixteen kinds.
Two boundaries with total jurisdiction cannot both be bounded, and bounded jurisdiction is what the
constitution requires.

**Two have no constituting act.** `artifact` and `surface_contract` declare no constitution.
`artifact` is also one of the two universal-reach boundaries: seven invariants binding every
artifact in the composition, under no constituting authority. That is not a gap to be filled by
writing two constitutions — it is evidence that the boundaries were created as organizational
partitions, and that the constituting act was never the thing that produced them.

**Three exercise no jurisdiction at all.** `federation`, `lifecycle` and `trace` declare no
`applies_to_kinds`. `federation` and `trace` hold a single artifact each — their own
constitution. A boundary whose only content is the declaration that it exists has no governed
subject.

The retirement of the `fb.constitution` and `fb.topology` composites points the same way. Splitting
them yielded *more* boundaries. Splitting a concern into finer concerns is ordinary; splitting an
authority into more authorities is a constitutional act, and nothing distinguished the two operations
because the encoding does not distinguish the two dimensions.

## The independence test, applied to the apparent survivor

`governance` governs `CONSTITUTION` and `INVARIANT` — a jurisdiction no other boundary claims, and
a decision no other boundary makes. It is the single row where the declarations satisfy the boundary
test on its face.

It fails the independence clause. `CONSTITUTION_GOVERNANCE_V0` states:

> This constitution is the root authority for the OmniBachi governance system.
>
> This constitution is supreme. All other constitutions derive authority from this document.

Its own tier table names the level: `Sovereign | Root authority, defines protocol semantics | This
constitution`.

So `governance` is not a peer authority sitting beside the platform authority. It **is** the root
authority, and every other boundary's constitution derives from it. It fails in the opposite
direction from the other twenty-five: not by having no authority to distinguish, but by being the
authority from which the rest would have to be distinguished. It is not a federation boundary at all
— it is the platform authority, encoded as though it were one boundary among peers.

Notably, `federation` — the boundary that defines what a federation boundary *is* — exercises no
jurisdiction, while `governance` does the governing.

## The ruling

1. **A federation boundary represents authority, never concern.** It is not a folder, a package, a
   deployment unit, or a topic. This restates the constitution and is not new.

2. **A concern may be governed without constituting a boundary.** Classification, organization and
   indexing by subject are legitimate and require no jurisdiction. A concern classification MUST NOT
   by itself constitute a federation boundary.

3. **A boundary must be able to answer, from declared artifacts alone:** who the authority is; what
   constituting act created it; what subjects fall within its jurisdiction; what governance decision
   it may make that no other boundary may; and how it relates to the authorities above and beside it.
   A purported boundary that cannot answer these has not demonstrated distinct governance authority,
   and therefore MUST NOT be admitted as a federation boundary.

4. **Authority independence.** Passing the questions above is necessary and not sufficient. The
   authority that constitutes and exercises a boundary MUST be distinguishable from the authority
   whose jurisdiction the boundary claims to govern. An authority governing its own constituting
   artifacts is exercising self-governance, which is a concern of that authority and not a second
   sovereign.

5. **No list of permitted boundaries is defined.** The standard defines the condition under which any
   boundary may exist; the number follows from the semantics. A ceiling or whitelist would be the
   same error in a different place.

## The obligation this ruling creates

This repository's recurring failure is doctrine that nothing can fail. The anti-sprawl rule has been
in force throughout, plainly written, and the surface accumulated boundaries against it because no
predicate could refuse one.

**This ruling therefore creates an enforcement obligation.** The semantic ruling may be accepted
independently of its implementation, but the repository is not fully conformant with the ruling until
the following predicates exist:

- a boundary that cannot demonstrate distinct authority and bounded jurisdiction is refused;
- a concern classification alone is refused as grounds for a boundary.

These predicates are normative consequences of this ruling, not preconditions for accepting it.

## The order the follow-on work must take

The sequence is not free — each step supplies what the next one needs.

```
1  ruling                    establish that authority and concern are distinct
2  canonical representation  give authority and concern separate declared carriers
3  enforcement predicates    refuse what the ruling forbids
4  migration                 re-declare the surface under the representation
```

**Step 2 precedes step 3, and this is the correction to the obvious ordering.** A predicate needs a
declared field to test. Today every candidate reads the collapsed identifier, so neither obligated
predicate can be written before authority and concern have separate carriers. The existing
`ASSERT_FQDN_NAMESPACE_AUTHORIZED_V0` shows the ceiling: it checks a declared namespace against an
`authorized_namespaces` allowlist, which can refuse an *unlisted* namespace but never an
*illegitimate boundary* — the two are indistinguishable to it. That allowlist is also the whitelist
clause 5 declines to define, which is why it cannot become the enforcement mechanism.

**Step 4 is mechanical and large.** `fb.` appears 1,407 times across 532 files in six repositories —
759 in `software_governance`, 228 in `transformation`, 211 in `business_domains`, 152 in
`protocol_compiler`, 41 in `snapshot_inspector`, 16 in `conformance_workloads`. It is not confined to
declarations: assertion handlers under `protocol_compiler/compiler/governance_engine/assertions/`
carry `RULE = "fb.<x>::INVARIANT_…"` constants, so the statically enumerated `HANDLER_REGISTRY` is in
scope. Sixteen pinned baselines go stale when the composition's identity changes, and each owes a
re-pin and a re-approval.

One prerequisite is unresolved and affects the cost of step 4: `STRUCTURE_IDENTITY_V0` declares
namespace derivation `method: module_path`, while `assert_fqdn_namespace_authorized_v0.py` states
that path-derivation was replaced by authorization. Which is true determines whether migration edits
declarations only, or moves directories as well.

## What this ruling does not decide

It does not settle the replacement encoding. `pgc::` with concern as declared metadata is the obvious
candidate, but the registry representation should follow the ontology rather than precede it.

It does not define the ontology that must come next. At least four concepts are expressed here
through one identifier — **authority** (the entity from which jurisdiction derives), **concern** (the
semantic subject governed), **federation** (the relation among distinct authorities), and
**namespace** (the name-resolution mechanism). That `federation` exercises no jurisdiction while
defining what a boundary is suggests federation may be a relation rather than a governed subject.
That is a hypothesis the evidence supports, not a ruling.

It does not resolve whether a business domain is a distinct governance authority. Domains declare
their own namespaces and are the elements *not* encoded as federation boundaries; if platform↔domain
is the relation federation describes, federation has instances there and none within one authority's
own concerns.

It does not rule on `governed_by`, whose two possible meanings are recorded separately in
`GOVERNED_BY_AUTHORITY_CYCLE_FINDING.md`.

It does not authorize a migration. Renaming before the model is settled would move the collapse into
new identifiers rather than remove it.
