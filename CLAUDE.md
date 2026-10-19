## Response Style

Keep responses under ~400 output tokens. Prefer terse bullet summaries over prose narration. When a full document is needed, Write it to a file instead of printing it in chat.

## Document Authoring Rules

- Never include internal review notes, meta-scaffolding, work-order framing, cross-reference stubs, or 'Status:' metadata in deliverable docs or figures.
- Do not add dates to papers or appendices.
- An 'outline' means a clean reader-facing outline of the paper, not an execution plan.

# CLAUDE.md — `protocol-governed-computing/software_governance`

Guidance for Claude Code working in this repository.

---

## What this repository is

This is the **PGC Normative Platform Surface** — the authoritative closure of protocol
artifacts from which `pgc::` is **constituted**. It is a repository of **normative
artifacts only**: it declares *what the platform is*, not *how it runs*.

- **Namespace:** `pgc::`. The GitHub org (`protocol-governed-computing`) provides the
  namespace; artifacts are not prefixed.
- **Authority:** derived by discovery — the compiler reads this surface; membership is whatever it
  resolves to a closed snapshot, mapped folder-by-folder in `doc/GOVERNANCE_SURFACE_MAP.md` §6. A
  hand-maintained tally of a surface that grows is guaranteed to drift, so there isn't one.
- **This repo contains no compiler, runtime, executor or testbed.** It does hold one kind of code:
  the implementations of the platform's own capabilities —
  `capability_transforms/implementation/` and `capability_side_effects/implementation/` — the pure
  functions and store handlers the runtime and its workers invoke by the `machine.implementation`
  each artifact declares. They are leaves: they import nothing from the compiler, the runtime or a
  domain, and they are shipped in the package so an installed runtime can reach them. The
  clean-break rule still holds: *no PGC-org repo may take a code dependency on a `pgs_*` repo.*

## Layout

```
registry/                     # governance normative surface — one directory per namespace
  actor/  artifact/  authority/  capability_contracts/  capability_side_effects/
  capability_transforms/  compiler/  conformance/  cryptographic_trust/  event/
  execution/  execution_placement/  execution_scheduling/  execution_topology/
  federation/  governance/  intent/  lifecycle/  runtime_binding/  security_domain/
  structure/  surface_contract/  trace/  transport/  vocabulary/  workflow/
      constitutions/*.md  invariants/*.md  structures/*.md
      surface_contracts/*.md  reserved/VOCAB_*.md
  schema/                     # SCHEMA_*.json — declaration substrate, not an fb.* namespace
capability_transforms/registry/capability_transforms/CT_*.md    # neutral CT declarations
capability_side_effects/registry/capability_side_effects/CS_*.md # neutral CS declarations
doc/GOVERNANCE_SURFACE_MAP.md # concern taxonomy + folder ≡ namespace map
doc/rule_ownership.md         # governance doctrine
```

**Folders are discovery-only; identity is declared.** An artifact's namespace comes from the
`fqdn:` key in its own `## Machine` block, never from the folder it sits in. The registry is
organized one directory per namespace, so the correspondence is currently one-to-one — but that
is a navigation convenience, not the source of identity. A file may move without changing what
the artifact *is*.

**Namespaces are architectural ownership boundaries.** Create one only for a first-class concern
that can evolve independently and owns a coherent contract — never because several artifacts
reference the same artifact kind. `applies_to_kinds` is orthogonal to namespace ownership.

Only normative declarations live here (`.md` protocol source + `.json` schemas). If a
directory would hold `.py`, it does not belong in this repo.

## Core doctrine

| Principle | Statement |
|-----------|-----------|
| Constituted, not authored | `pgc::` is what the compiler already proves the platform to be; this surface is discovered, then documented. Do not "design" membership by hand. |
| Normative artifacts only | Protocol declarations + schemas. No engine, no execution, no tests. |
| `pgc::` / `pgs::` separation | Platform artifacts only. Domain artifacts (`blockchain`, `ai_governance`, `fb.blockchain`, `fb.ai_governance`, domain CT/CS) belong in `pgs::` and MUST NOT appear here. |
| PLATFORM_IMMUTABILITY | A domain extends the platform by adding artifacts in its own namespace; it never modifies artifacts in `pgc::`. |
| Transforms placed by kind and purity | Three constitutions govern capability transforms: deterministic atoms (`CONSTITUTION_DETERMINISTIC_ATOMS_V0`), molecules (`CONSTITUTION_MOLECULES_V0`) and non-deterministic atoms (`CONSTITUTION_NONDETERMINISTIC_ATOMS_V0`). Every transform is governed by exactly one, decided by what it declares. The rules common to all three — surface closure, closure by derivation, implementation admissibility — are in `CONSTITUTION_CAPABILITY_TRANSFORMS_V0`, which no transform names as `governed_by`. A transform is deterministic unless it declares otherwise, and never has side effects. |
| VERSION-IMMUTABLE | `pgc::` is immutable within a PGC spec version. A behavior change requires a new version, never an in-place edit. |
| Compiler is external | Completeness and closure are proven by pointing the external compiler at this surface — not by any code inside this repo. |

## How completeness is verified

The surface is "complete and self-supporting" **iff the external compiler compiles it to
a closed snapshot** — every reference resolves, zero unresolved FQDNs, `VALID`. The
engine is a tool pointed *at* this repo; it is never vendored into it. To test:

1. Run the compiler (`protocol_compiler/compile.sh`) against this `registry/` + capability surface.
2. Diff the resulting artifact closure against `doc/GOVERNANCE_SURFACE_MAP.md` §6.
3. Any unresolved reference = a missing platform artifact **or** a leaked domain
   reference. Resolve by adding the platform artifact, or by moving the reference to
   `pgs::`.

## Rules

**MUST:**
- Keep this repo to normative declarations only (`.md` + schema `.json`).
- Use FQDN identity everywhere; versions immutable.

**MUST NOT:**
- Add code other than capability implementations — no compiler, runtime or executor code, no
  testbeds, no build cruft.
- Add domain (`pgs::`) artifacts of any kind.
- Hand-edit an artifact to change behavior in place (version instead).
- Introduce new terminology or rename concepts without explicit approval — use the exact
  terms in `standards/doc/` (`NAMESPACE_MODEL.md`, `spec/`) and `doc/GOVERNANCE_SURFACE_MAP.md`.

## Provenance

Sourced from RI-0: governance artifacts from `pgs_governance/registry/`, neutral CT/CS
declarations from `pgs_capabilities/`. This is a **one-way, informative** lift of the
normative surface — not a fork of the implementation.
