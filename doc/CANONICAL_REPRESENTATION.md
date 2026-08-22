# Canonical Representation — authority and concern as separate declared carriers

Task B steps 2 and 3. **Delivered.** This document proposed the representation; §8 records what was
built and where it differed from the proposal.

`AUTHORITY_VS_CONCERN_RULING.md` establishes that authority and concern are distinct and that a
concern classification must not by itself constitute a federation boundary. It deliberately does not
settle the replacement encoding, on the grounds that "the registry representation should follow the
ontology rather than precede it." This proposes that representation, against the requirement as the
standard now states it and against the surface as it actually is.

---

## 1. The requirement is larger than the ruling assumed

The ruling names four concepts collapsed into one identifier: authority, concern, federation,
namespace. **The standard requires seven things separately determinable**, and the realization map
recorded which already have carriers:

| CA-1 dimension | Carrier today | State |
|---|---|---|
| **authority** | — | **missing** |
| **concern** | the namespace string | **collapsed into identity** |
| **ownership** | `module_path`, derived from the source directory | **derived from position** |
| scope | `applies_to_kinds` (88 invariants) | declared |
| inheritance | `governed_by` (163 artifacts) | declared |
| import | `imported_governance` on each attestation | declared |
| admission | `artifact_types` in the build configuration | declared |

Four of seven are already declared and need nothing. **Three are the work**: authority is absent,
concern rides in the namespace, and ownership is read out of a directory path.

That last one is not a Task B item by origin — it is the map's finding 19, where
`assert_rb_storage_subdomain_owned_v0` refuses a runtime binding on a subdomain derived by splitting
`module_path`. It belongs here because it is the same defect: **a fact that determines governance,
carried by something other than a declaration.**

## 2. What `fb.` actually marks, measured

The ruling classified all 26 boundaries and concluded they are "one modeling error." Measuring the
composition gives that conclusion a sharper statement.

Partitioning every namespace by whether its artifacts are **governing** elements (CONSTITUTION,
INVARIANT, STRUCTURE, SCHEMA, ASSERT) or **governed** ones:

```
24 of 26  fb.* namespaces hold governing elements ONLY
 2 of 26  are mixed — surface_contract, vocabulary
 6 of  8  plain namespaces are the domains, each mixed
 2 of  8  plain namespaces hold governed elements ONLY
```

And the two plain exceptions are the tell:

```
capability_transforms::        12 artifacts   all CT          the governed elements
capability_transforms::      6 artifacts   1 CONSTITUTION, 4 INVARIANT, 1 STRUCTURE
capability_side_effects::       6 artifacts   all CS          the governed elements
capability_side_effects::    5 artifacts   1 CONSTITUTION, 4 INVARIANT
```

**One concern, split across two namespaces by governance role.** The realization already needed the
distinction, found no field to put it in, and encoded it as a prefix.

So the finding is not that `fb.` is a bad name for a boundary. It is that:

> **`fb.` marks a governing element of concern X under the platform authority.** It is a
> governance-role marker fused to a concern name, and it denotes federation nowhere.

The two mixed `fb.` namespaces confirm rather than weaken this: `SURFACE_CONTRACT_*` and `VOCAB_*`
are platform-owned *governed* artifacts, and the platform has no bare namespace to put them in —
so they sit with their own governance. The gap is structural, not accidental.

**And the prefix is applied exactly where federation is absent.** The 26 `fb.*` namespaces are one
authority's concerns. The six candidates for genuinely distinct authorities — `blockchain`,
`ai_governance`, `book_library_mgmt`, `transformation`, `inspection`, `workload` — carry no `fb.` at
all. The marker for "distinct sovereign" is on everything that is not one, and absent from everything
that might be.

## 3. What the standard permits, which is more than expected

ID-12 forbids a namespace establishing or encoding authority, concern or federation. `4c` §5 is
narrower than it first reads:

> That two things share a namespace establishes that their names are resolved together. It
> establishes nothing about who governs them, what subject they concern, or whether they belong to
> one jurisdiction. **Where a system's namespaces coincide with its authorities, that coincidence is
> a property of that system's arrangement, not a consequence of namespaces.**

**Coincidence is permitted; encoding is not.** A namespace may *look like* a concern. What may not
happen is any mechanism reading concern out of it, or the namespace being the only place concern is
stated. The prohibition is on load-bearing, not on resemblance.

That separates the work into two independent changes, and only one of them is large:

| | What it does | Identity | Scale |
|---|---|---|---|
| **A — declare the facts** | add the three missing carriers to the machine block | moves the snapshot id | additive, no reference re-pointing |
| **B — stop asserting federation in the name** | `fb.<x>` → `<x>` | moves the snapshot id | 1,407 occurrences, 532 files, 6 repos |

**A is step 2 and is what the ruling's ordering requires** — a predicate needs a declared field to
test. **B is step 4** and is not required for conformance with ID-12 once A lands and nothing reads
the namespace. It is required for conformance with the ruling's clause 3: a name that asserts a
federation boundary the artifact cannot demonstrate is a claim the surface should stop making.

## 4. The proposed carriers

Three fields in the machine block's envelope, alongside `fqdn`, `artifact_kind`, `version`,
`governed_by`.

### 4.1 `authority` — from whom jurisdiction derives

```yaml
authority: pgc.platform          # or: pgc.domain.blockchain
```

- Declared by every artifact. Not inferred from namespace, path, or kind.
- Its admissible values are the authorities the system declares — today one platform authority and
  the domains, per CA-2's requirement of a declared constituting act.
- **This is the field that makes the ruling's predicates writable.** A purported boundary is now a
  claim about `authority`, testable against CA-3's five questions, rather than a substring.

**Deliberately not decided here:** whether a business domain *is* a distinct authority. The ruling
left it open and the map did not settle it; DP-4 requires a domain profile to state it, and no domain
profile exists (map finding 36). The field is shaped to carry either answer — a domain declaring
`authority: pgc.platform` is a concern of the platform; declaring `pgc.domain.<x>` is a claim that
must answer CA-3. **Until domain profiles exist, every artifact declares `pgc.platform`**, which is
true and refusable rather than absent.

### 4.2 `concern` — the semantic subject

```yaml
concern: transport
```

- The subject an artifact is about: `transport`, `actor`, `execution_topology`, `capability_transforms`.
- **Its vocabulary is exactly the 26 concern names `fb.*` already carries**, minus the prefix. No new
  taxonomy is invented; the existing one is moved out of the identifier into a field.
- A concern classification confers nothing (ruling clause 2). It exists for organization, indexing
  and human navigation, and no determination may rest on it alone.

### 4.3 `owner` — which subdomain owns this artifact

```yaml
owner: wallet          # or omitted where the artifact belongs to the domain, not a subdomain
```

- Replaces `_owner_subdomain(module_path)` in both `projections/artifact_index.py` and
  `assertions/handlers/assert_rb_storage_subdomain_owned_v0.py`.
- **Closes map finding 19.** A governance determination stops being made from a directory name, and
  MB-1 stops being breached — nothing outside the declaration surface determines anything.
- Absent means domain-owned, declared as an explicit sentinel rather than by omission, per MB-10's
  rule that omission must not be indistinguishable from a decision.

### 4.4 What is *not* added

**Governance role** — whether an element governs or is governed — needs no field. It is already
declared per kind as `semantic_category` in the kind registry, and GO-1 makes it a property of the
kind rather than of the artifact. What the `fb.` prefix was doing, the kind already answers.

**This is the whole reason the prefix can be dropped without loss.** Removing `fb.` does not discard
a fact; it stops duplicating one the kind already carries.

## 5. Consequences worth stating before deciding

- **The snapshot id moves and every domain recompiles.** Change A alone does that, because a
  machine-block field changes each artifact's content hash. Sixteen pinned baselines go stale and
  each owes a re-pin and a re-approval. Release 10's scope already anticipates this.
- **`STRUCTURE_IDENTITY_V0` carries a dead field.** Its `identity.fqdn.namespace.derivation.method:
  module_path` is read by nothing — `s1_extract` says of the same structure that these are "the
  identity rules repurposed from derivation to authorization," and only `rules[].namespace` is
  consumed, to build the authorized-namespace allowlist. **This settles the plan's open
  prerequisite: migration edits declarations only and moves no directories.** The dead key should be
  deleted with change A, the third declared-but-unread field this surface has shed.
- **The `authorized_namespaces` allowlist survives change A and should not survive change B.** The
  ruling is explicit that it "is also the whitelist clause 5 declines to define, which is why it
  cannot become the enforcement mechanism." Once `authority` is declared, the allowlist's job passes
  to the CA-3 predicate and the allowlist should be retired rather than re-pointed.
- **Two concerns are currently split across a bare and a prefixed namespace**
  (`capability_transforms`, `capability_side_effects`). Change B merges each into one namespace with
  the split re-expressed as the kind's own category. That merge is the visible proof that the prefix
  was carrying governance role.

## 6. What this proposal does not decide

- **Whether a domain is a distinct authority** (ruling; DP-4; map finding 36). Deferred to domain
  profiles, and the `authority` field is shaped to carry either answer.
- **Whether federation has any instances at all.** The ruling's hypothesis is that federation
  describes the platform↔domain relation and has no instances within one authority's concerns. If
  that holds, no artifact should ever declare a federation boundary and the concept belongs to the
  relation between authorities, not to a field. **Nothing here creates a `federation` carrier**, and
  that is deliberate: a carrier for a relation nothing instantiates would repeat the original error.
- **The enforcement predicates** (step 3). They are the ruling's obligation and become writable once
  `authority` exists; their specification is not attempted here.

## 7. What would make this proposal wrong

Stated so it can be checked rather than argued:

- If any mechanism turns out to read the namespace for something other than name resolution, change B
  is not additive-then-mechanical and the estimate is wrong. **Measured:** `authorized_namespaces` is
  the only consumer found, and it consumes the namespace as an opaque string.
- If `semantic_category` turns out not to separate governing from governed cleanly for every kind,
  §4.4's claim fails and a governance-role field is needed after all. **Measured:** 24 of 26 `fb.*`
  namespaces are governing-only and the 2 exceptions are explained by the platform having no bare
  namespace, not by the category being wrong.
- If a domain is ruled a distinct authority, `authority` values multiply and CA-3 must be answered
  for each. That is a larger change to what the field *means*, not to its shape.

---

## 8. What was built, and where it differed

**Two carriers, not three.** The proposal named `authority`, `concern` and `owner`. Measurement
showed `owner` and `concern` would hold the same string on every artifact that has both — for the
platform `registry/<concern>/`, for domains `registry/<subdomain>/`, and `_owner_subdomain` already
returned exactly the concern name. A third field would have declared one fact twice, which is the
defect this task exists to remove. **`concern` carries both**, and the three derivation sites read it.

**The migration was behaviour-preserving, and that was checked rather than assumed.** `concern` was
populated from exactly what `module_path` derived, so `artifact_index.owner_subdomain` was compared
before and after: **no artifact changed from one value to another.** 74 changed from `None` to a
value — the flat-registry artifacts (`inspection`, `workload`, the bare capability namespaces), which
had no derived owner and now state their concern. One RB is affected, `workload::RB_COLLATZ_V0`, and
its assertion passes because both sides moved together.

**What now reads a declaration instead of a directory** — map finding 19 closed:

```
protocol_compiler/compiler/projections/artifact_index.py       _owner_subdomain deleted
snapshot_assembler/assembler/indexes.py                        _owner_subdomain deleted
.../assertions/handlers/assert_rb_storage_subdomain_owned_v0.py  reads declared `concern`
```

**Generators, not artifacts.** Three generators emit envelopes and all three were changed at the
declaration rather than the output — `author_transport_contracts.py` (36 contracts),
`build/render.py::_render` (rendered domain artifacts), and `build/render.py::build_manifest` (the
build configs). `construction_acceptance` caught the last two: 0/93, then 91/93, then 93/93.

**`STRUCTURE_IDENTITY_V0`'s `method: module_path` is deleted.** Read by nothing; `s1_extract` calls
the same rules "repurposed from derivation to authorization" and consumes only `rules[].namespace`.
This settles the plan's open prerequisite: **migration edits declarations only and moves no
directories.** Third declared-but-unread field this surface has shed.

## 9. Step 3 — the predicates, and why they are platform-scoped

Both obligations the ruling created are built, and **each was observed to refuse before being
counted as built** (CD-4, TR-3a).

| Invariant | Refuses | Probed |
|---|---|---|
| `federation::INVARIANT_AUTHORITY_CONSTITUTED_V0` | an `authority` no constituting act declares (CA-2) | `authority: pgc.invented` → 1 violation |
| `federation::INVARIANT_CONCERN_NOT_AUTHORITY_V0` | a value declared as both concern and authority (CA-6) | `authority: transport` → 1 violation, both rules |

`CONSTITUTION_GOVERNANCE_V0` — which declares itself the root authority — now declares
`constitutes_authority: pgc.platform`, and `SCHEMA_CONSTITUTION_V0` carries the property.

**They are scoped `applies_to: [PLATFORM]`, and the reason is a real limit rather than a
convenience.** A domain build materializes only its own artifacts — collatz compiles 15 and no
constitution among them — so a domain genuinely cannot answer "is this authority constituted
anywhere." That is a composition obligation (GC-11), and the first attempt refused 91 artifacts in
every domain, correctly, for a question the build could not answer.

**The residue is honest and recorded**: a domain artifact declaring an unconstituted authority is
caught at the platform build only if the platform sees it, which it does not. The composition
conformance phase is where this belongs — its `composition_check` vocabulary is cardinality over a
selector and cannot yet express a relational rule, and extending it is "a declaration act in
`SCHEMA_INVARIANT_V0` plus one entry" by that module's own note. **Not attempted here; recorded as
the next enforcement item.**

## 10. Step 4 — delivered

**1,402 occurrences across 490 files**, matching the ruling's estimate of 1,407. Zero `fb.*`
namespaces remain in the composition; 34 namespaces became 32, because the two split concerns merged
exactly as predicted — `capability_transforms` 12 + 6 = **18**, `capability_side_effects` 6 + 5 =
**11**. That merge is the visible proof that the prefix was carrying governance role: nothing was
lost, because `semantic_category` already carried it.

**What was deliberately not renamed.** `standards/doc/realization_map.md` and `.github/doc/` quote
`fb.<concern>` as the defect under examination — rewriting them would make the record describe
something that never happened. `fb.constitution` and `fb.topology` were left too: they are retired
composite namespaces that no live artifact carries, and they survive only in prose and in the
**already-dead baseline profile** (map finding 33). `fb.py` is a filename and was excluded by
matching only the 26 live namespace tokens, longest-first.

**Two checks caught real things during the migration.** `_check_undeclared_files` refused the build
while stale `fb.X__*.json` outputs from the previous compile were still on disk — a failed build
writing nothing, working. And the authorized-namespace list needed deduplication once the two pairs
merged, which the compile surfaced immediately.

## 11. The baselines — the plan's expectation was wrong

The ruling states that "sixteen pinned baselines go stale when the composition's identity changes,
and each owes a re-pin and a re-approval." **All sixteen are stale and almost none of them owes a
re-pin.**

A dossier is judged against the composition it was designed against. Re-pinning a *delivered* dossier
forward destroys its record — the workspace's own pin discipline says so, and `4d` TR-15 requires
validation "against a named frozen baseline, and never against one containing its own output."
Judging a delivered CR's P7 or P8 against the current snapshot is meaningless by construction.

| Disposition | Dossiers |
|---|---|
| **Never re-pin — completed** | `book_library_mgmt` cr_01–03, `rule_expressiveness` |
| **Never re-pin — closed unbuilt** | `register_coverage` |
| **Never re-pin — delivered** | `declared_reach`, `cr_04_wallet`, `cr_03_catalog`, `refusal_discharge`, `generated_artifacts`, `multi_emission`, `multi_structure_binding`, `select_operation`, `cr_01`–`cr_03_identity` |
| **Legitimately re-pinned — in flight** | `rule_effectivity` |

**Nothing is broken by the stale pins**, and that was verified rather than assumed: the differential,
the e2e phase suite and construction acceptance all pass, because each carries its own pin and reads
the sealed rule set the dossier names rather than the working tree.

**One dossier is a decision rather than an edit:** `rule_effectivity` is in flight, so re-pinning it
forward is legitimate — and re-pinning is a governance act with a gate behind it, not a file change.
That is the boundary this task stops at.

The prefix is now redundant: `concern` carries the subject, `semantic_category` carries the
governance role, and `authority` carries what `fb.` falsely asserted. Removing it is mechanical —
1,407 occurrences, 532 files, six repos — and **merges the two split namespaces**
(`capability_transforms` + `capability_transforms`), which is the visible proof that the prefix
was carrying governance role rather than federation.

**What step 4 did not close:** `REFERENCE_PLATFORM_PROFILE_V1` was migrated with everything else, so
it still names live FQDNs — but nothing checks that, and map finding 33 stands. The three-line
resolution check belongs in the runbook.
