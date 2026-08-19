# May a business domain author an invariant?

## Ruled: yes — but authorship is not the gate, and granting it alone would make things worse.

The conclusion is right and the framing that produces it is not. A domain is the authority for the
subjects it introduces; if it cannot state a constraint over them, PGC has no first-class way to
express domain correctness and the platform ends up owning rules about subjects it does not own.
That much stands.

What does not stand is the premise that the capability is missing from the ontology.

## It is not missing. It is already exercised, and it is ungoverned.

`conformance_workloads/workloads/collatz` lists `INVARIANT` in its `artifact_types` and authors
`workload::INVARIANT_CT_SURFACE_CLOSED_WORKLOAD_V0`. It compiles, its ASSERT derives, its handler
resolves, and the build is green. The mechanism exists and works.

Now ask what governs it:

```
named by a constitution rule                    no constitution anywhere names it
INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0    applies_to_kinds [CONSTITUTION, INVARIANT]
INVARIANT_ASSERT_PARITY_V0                      applies_to_kinds [INVARIANT]
_DOMAIN_INSTANTIATED                            {WF, CC, CS, CT, RB, AC, IN, EV, TI, TE}
```

Neither `CONSTITUTION` nor `INVARIANT` is a domain-instantiated kind, so **neither check is ever
imported into a domain build**. The reverse-closure rule that refuses an invariant no constitution
declares cannot run where domain invariants live. The parity rule that pairs an invariant with its
ASSERT cannot run there either.

So the one domain invariant in the workspace is an orphan by the platform's own definition, and the
mechanism that exists to say so is structurally absent from the only build that could see it. That is
not a permission problem. **Adding `INVARIANT` to three more `artifact_types` lists is one line per
domain and would produce three more ungoverned invariants.**

## The precondition

Authorship is granted **with** the closure that makes an authored invariant governed, not before it:

1. **A domain-authored invariant must be named by a constitution rule.** Which means a domain must be
   able to author or extend a constitution — `CONSTITUTION` becomes a domain-authorable kind, or the
   governance chain gets an explicit domain form. Today a domain build carries no constitutions at
   all, so there is nothing for a domain invariant to be declared by.
2. **`GOVERNANCE_DECLARATION_RESOLVES` and `ASSERT_PARITY` must reach domain builds.** Their
   admission turns on `applies_to_kinds ∩ _DOMAIN_INSTANTIATED`, and the kinds they govern are
   exactly the two the set omits. Whatever the encoding, the rule is: *the checks that make an
   invariant authoritative must run wherever an invariant may be authored.*
3. **Only then, `INVARIANT` in a business domain's `artifact_types`.**

Granting 3 without 1 and 2 creates a second governance surface that nothing checks — which is the
defect dev/7 spent itself deleting from 14 invariants. A rule the compiler does not prove is a rule
the compiler does not have, wherever it is written.

## On redefining `scope.applies_to`

The proposal is that `scope.applies_to` should describe applicability rather than determine
authorship. It never determined authorship. It determines **import admission**, and what it names is
*the surface whose allow-list the invariant carries* — which is why three of the four invariants that
declare it carry an `allowed_*` list, and why stripping it from a real one asserts the platform's
allow-list against a domain that never declared it (7 violations, measured).

Ownership and applicability may well deserve to be first-class. If so they want **their own field**.
Re-reading an existing one into the meaning its name suggests is the move that has now been wrong
twice in this investigation.

## The sequencing principle, and why it cannot be a coverage count

The general form proposed is: *never expand an artifact authoring surface until the governance
machinery for that surface is demonstrably complete* — AUTHOR → DECLARE → RESOLVE → CONFORM →
ENFORCE. The substance is right and it is the rule this ruling applies.

But "demonstrably complete" has to mean something a build can refuse, or it joins the class of
doctrine dev/7 exists to delete. The obvious encoding — *every kind a build may author is covered by
at least one governing invariant admitted to that build* — was measured, and it does not
discriminate:

```
ungoverned kinds, per domain build config
  ai_governance  []   blockchain  []   book_library_mgmt  []
  collatz        []   snapshot_inspector  []   transformation  []
```

Zero gaps everywhere, including for `INVARIANT` itself, which 8 admitted invariants list among their
kinds. Read what those 8 are:

```
FQDN_NAMESPACE_AUTHORIZED   FQDN_ONLY_REFERENCES   IDENTITY_FQDN_CONSISTENCY
NO_SHORT_NAME_REFERENCE     SCHEMA_CONFORMANCE     SUPERSEDED_NOT_REFERENCED
UNIQUE_ARTIFACT_ID          VOCABULARY_SYMBOLS_WELL_FORMED
```

Every one is a **universal well-formedness** check that happens to enumerate every kind. Not one asks
whether a constitution declares the invariant or whether its ASSERT exists. So a domain-authored
invariant today is checked for *shape* — FQDN valid, id unique, schema conformant — and not at all
for *authority*.

A census by kind therefore reports a complete governance surface over an authority chain that is
entirely absent. It is the same failure as the dimension that does not discriminate: a measurement
with full coverage and no consequential distinction.

**The check that would work names the chain, not the count:** for each kind a build may author,
DECLARE, RESOLVE and PARITY must each be present by name in that build.

## The check, and what it says today

`standards/process/governance_chain_closure.py` proves two relations:

1. **Every invariant authored outside the platform surface is named by a constitution rule.**
   Checked across the workspace rather than within a build, because the build cannot — a domain
   build carries no constitutions, so there is nothing there to declare a domain invariant.
2. **Any build whose `artifact_types` admits `INVARIANT` or `CONSTITUTION` can reach the chain
   checks** — by name, `INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0` (DECLARE, RESOLVE) and
   `INVARIANT_ASSERT_PARITY_V0` (PARITY).

It reads `_DOMAIN_INSTANTIATED` by importing it from `s1_extract` rather than restating it. A second
spelling of the admission rule inside the checker would be the same defect the rest of this document
is about.

**It fails on the workspace as it stands, and that is the correct verdict:**

```
ORPHAN     workload::INVARIANT_CT_SURFACE_CLOSED_WORKLOAD_V0 — named by no constitution rule
UNCHAINED  STRUCTURE_BUILD_WORKLOAD_CONFIG_V0 may author INVARIANT
             unreachable: DECLARE (INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0)
             unreachable: RESOLVE (INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0)
             unreachable: PARITY  (INVARIANT_ASSERT_PARITY_V0)
```

The workload already holds the permission this ruling says must come last, and holds it without any
of the three relations. There are exactly two ways to green: build the governance, or withdraw the
authorship. Both are decisions, so the check is **deliberately not in the runbook** until one is
taken — a gate that is red on arrival teaches people to skip gates.

### Probes G and H

```
G  grant INVARIANT to book_library_mgmt's artifact_types
     → 3 relations do not close; the new UNCHAINED names the config that changed.
       Permission without governance is detected at the moment it is granted.

H  withdraw the workload's INVARIANT authorship and its one authored invariant
     → GOVERNANCE CHAIN PASSED, exit 0.
```

H is the one that makes the check trustworthy. Without it, a gate that is red on real state cannot be
distinguished from a gate that is red on everything.

## Issue 36, restated

Not *"the wiring check has no reachable subject in any business domain"* — that is the symptom.

**A domain cannot express a governed constraint over the subjects it owns: it may author an invariant
only where nothing can check that the invariant is declared, so a domain invariant is authored
outside the governance chain rather than inside it.** The unreachable wiring check is one consequence.
