# software_governance

**The PGC Normative Platform Surface — namespace `pgc::`.**

This repository is the authoritative closure of protocol artifacts from which `pgc::` is
**constituted**: the constitutions, invariants, structures, schemas, surface contracts,
vocabulary, and the neutral capability transforms (CT) and side effects (CS) that every
conforming Protocol-Governed Computing system depends on.

It contains **normative artifacts only** — it declares *what the platform is allowed to
be*. It contains no code of any kind. The compiler, assembler, runtime and inspector that read this
surface are sibling repositories of the same organisation; RI-0 (`pgs_*`) is the legacy reference
implementation and no repository here takes a dependency on it.

**Folders are discovery-only; identity is declared.** An artifact's namespace comes from the `fqdn:`
key in its own `## Machine` block, never from the directory it sits in. The registry is organised one
directory per namespace, so the correspondence is currently one-to-one — a navigation convenience,
not the source of identity.

> **Orientation:** for what PGC is, how the repositories compose, and the papers that develop
> the architecture, see <https://github.com/protocol-governed-computing>.

---

## Contents

| Path | Contents |
|------|----------|
| `registry/<namespace>/` | Governance normative surface — one directory per namespace (`actor`, `artifact`, `authority`, `conformance`, `lifecycle`, `structure`, `transport`, `vocabulary`, …), each holding its constitutions, invariants, structures, surface contracts and reserved vocabulary. The retired `FB_*` directories no longer exist |
| `registry/schema/` | `SCHEMA_*.json` — declaration substrate, not a namespace of its own |
| `capability_transforms/registry/` | Neutral, domain-agnostic CT declarations |
| `capability_side_effects/registry/` | Neutral CS declarations (storage / registry / etc.) |
| `doc/GOVERNANCE_SURFACE_MAP.md` | The concern taxonomy, and the folder ≡ namespace map |
| `doc/rule_ownership.md` | Governance doctrine |
| `doc/PGS_REFERENCE_SURVEY.md` | Every surviving `pgs_*` reference in the surface, classified — which are live lookup keys, which are historical citation, and which were removed |

## What this repository is **not**

- The **normative surface** (`registry/`, `capability_transforms/`, `capability_side_effects/`)
  carries no code — no compiler, runtime, handlers, or executors.
- Not a platform. A **Profiled Normative Platform (PNP)** is the *composition* of this governance
  surface with selected workloads (`conformance_workloads`) and optionally a business domain
  (`business_domains`), per a conformance profile.
- Not a place for domain artifacts — `blockchain`, `ai_governance`, and any
  `fb.blockchain` / `fb.ai_governance` boundary belong to `pgs::`, not here.

## Runnable demonstration

Conformance workloads live in the sibling `conformance_workloads` repo — the Collatz workload
(governed artifacts, `implementation/` CT/CS, `transport/` TI/TE boundary declarations) and its web
client. They exercise this surface; they are not part of the normative `pgc::` closure.

## Immutability

`pgc::` is **immutable within a PGC spec version**. Domains extend the platform by adding
artifacts in their own namespace; they never modify what is defined here. A behavior
change is a new version, never an in-place edit.

## Verifying completeness

The surface is complete and self-supporting **iff the external compiler compiles it to a
closed snapshot** (every reference resolves, zero unresolved FQDNs). The engine is pointed
*at* this repo; it never lives inside it.

## License

See `LICENSE` and `NOTICE`.
