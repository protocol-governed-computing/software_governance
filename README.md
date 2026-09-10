# software_governance

**The normative platform surface — what a conforming PGC system is allowed to be.**

Every governed behavior in a PGC composition resolves, eventually, against a declaration in this
repository. It holds the constitutions, invariants, structures, schemas, surface contracts,
reserved vocabulary, and the neutral capability transforms and side effects that no single domain
owns and every domain depends on.

It is **declaration first**: constitutions, invariants, structures, schemas and vocabulary that
the sibling toolchain reads. It also carries the capability transform and side-effect
implementation modules a sealed snapshot binds by fully qualified module path at execution —
the only executable code here, and it exists because a snapshot names it.

## Install

```bash
pip install pgc-governance
```

This package carries declarations and the implementation modules a sealed
snapshot binds at execution. It provides no command of its own — the toolchain
packages read it.

## Where it fits

A composition is assembled from repositories that each own one concern:

```
software_governance    the normative surface every composition rests on   (this repo)
conformance_workloads  workloads that prove conformance
business_domains       domains built on the surface

protocol_compiler      source      → compiled projections
snapshot_assembler     projections → assembled snapshot
protocol_runtime       snapshot    → execution
snapshot_inspector     snapshot    → inspection
```

This repo is the **floor** of that stack. A domain does not import it — a domain *resolves against*
it, and the compiler is what performs the resolution. If a reference in any domain fails to resolve,
either the platform is missing an artifact or the domain leaked one it should have declared itself.

**A platform is a composition, never a repository.** A Profiled Normative Platform is this surface
plus selected workloads plus an optional business domain, per a conformance profile. There are as
many platforms as there are profiles.

## What it holds

| Path | Contents |
|------|----------|
| `registry/<namespace>/` | The governance surface, one directory per namespace — `actor`, `artifact`, `authority`, `conformance`, `execution`, `governance`, `lifecycle`, `structure`, `transport`, `vocabulary` and others. Each holds its own constitutions, invariants, structures, surface contracts and reserved vocabulary |
| `registry/schema/` | `SCHEMA_*.json` — the declaration substrate, not a namespace of its own |
| `capability_transforms/registry/` | Neutral, domain-agnostic capability transform declarations |
| `capability_side_effects/registry/` | Neutral capability side-effect declarations |
| `surface_map/` | The generated map of the governance surface — `governance_surface_map.yaml` is emitted from the registry tree, and `GOVERNANCE_SURFACE_MAP.md` reads it. Documentation *about* the registry, never a second source of truth for it |
| `dossiers/` | The governed changes that produced this surface, one directory per change — the P0–P8 phase documents and a `closure.md` recording which phases were reached, against which composition, and who closed the gate. The record of how the registry came to say what it says |
| `rulings/` | Questions that were contested and are now settled, kept with the evidence that settled them: the authority-versus-concern ruling and the cycle finding behind it, and `rule_ownership.md`, which states which mechanism carries which class of rule |

Artifacts declare namespaces of the form `fb.<concern>` — `structure::STRUCTURE_IDENTITY_V0`,
`authority::…`. **`fb` is a federation boundary**: a declaration that a distinct governance
authority has jurisdiction over a named set of protocol semantics. It is not a folder, a package, or
a deployment unit — see `registry/federation/constitutions/CONSTITUTION_FEDERATION_BOUNDARY_V0.md`.
Domains declare their own namespaces (`blockchain::`, `book_library_mgmt::`) and never declare into a
platform boundary.

## What binds a contributor

**Identity is declared, not located.** An artifact's namespace comes from the `fqdn:` key in its own
`## Machine` block, never from the directory it sits in. The registry is organised one directory per
namespace, so the correspondence is currently one-to-one — a navigation convenience, not the source
of identity. A file may move without changing what the artifact *is*.

**No code, ever.** Normative declarations only: `.md` protocol source and `.json` schemas. A
directory that would hold `.py` does not belong in this repository. The compiler, assembler, runtime
and inspector that read this surface are siblings, and none of them is vendored here.

**Immutable within a spec version.** A domain extends the platform by adding artifacts in its own
namespace; it never modifies one here. A behavior change is a new version, never an in-place edit.

**A namespace is an ownership boundary.** Create one only for a first-class concern that can evolve
independently and owns a coherent contract — never because several artifacts happen to reference the
same artifact kind.

## How completeness is verified

The surface is complete and self-supporting **iff the external compiler compiles it to a closed
snapshot** — every reference resolves, zero unresolved FQDNs. Nothing inside this repository can
establish that, which is the point: the engine is pointed *at* the surface and never lives inside it.

```bash
protocol_compiler/compile.sh <this repo>
```

Then diff the resulting closure against `surface_map/GOVERNANCE_SURFACE_MAP.md` §6. An unresolved reference
is either a missing platform artifact or a leaked domain reference — resolved by adding the former
or moving the latter into the domain that owns it.

## License

See `LICENSE` and `NOTICE`.

---

## The package family

| Package | Repository | Role |
|---|---|---|
| `pgc-compiler` | `protocol_compiler` | declarations → compiled projections |
| `pgc-assembler` | `snapshot_assembler` | projections → sealed snapshot |
| `pgc-runtime` | `protocol_runtime` | snapshot → governed execution |
| `pgc-inspector` | `snapshot_inspector` | snapshot → read-only inspection |
| `pgc-transformation` | `transformation` | change request → protocol artifacts |
| `pgc-governance` | `software_governance` | the governance surface and its capability implementations |
| `pgc-workloads` | `conformance_workloads` | the workloads that make conformance observable |
| `pgc-domains` | `business_domains` | the business domain implementations the composed snapshot binds |

`pip install protocol-governed-computing` brings in the whole family.

**Installing the toolchain is one of two steps.** The compiler resolves the governance surface from
`PGC_PLATFORM_ROOT` — fail-hard, cwd-independent, zero inference — so the *declarations* come from a
repository you point at, never from a wheel. A registry inside a package would be a second governance
surface competing with the repository's, and a build could then be governed by a stale copy.

```bash
git clone https://github.com/protocol-governed-computing/software_governance
export PGC_PLATFORM_ROOT=$PWD/software_governance
pgc            # reports what is installed and whether the anchor resolves
```

`PGC_DOMAIN_ROOTS` names an additional domain contributing its own `registry/structures` — the
directory that *directly contains* it, not the repository above it; pointing one level too high is a
silent no-op. `PGC_SNAPSHOT_ROOT` is where compiled output is written, and each domain build needs
its own: every layer's output consolidates into one root, and verification rejects any file in that
root the current build did not declare. `PGC_SNAPSHOT_PROFILES` is the directory holding snapshot
profiles, required by the assembler and the runtime alike.

`PGC_BUILD_ROOT` is accepted and reported and **nothing reads it** — `PGC_SNAPSHOT_ROOT` is the
anchor that controls output.

The full sequence, with the repositories it needs, is in
[`pgc_install`](https://github.com/protocol-governed-computing/pgc_install).

**Versioning.** Two schemes, and the published version follows the second.

- **Internal** — each repository's `VERSION` file, a monotonic composition ordinal. PGC versions the
  composition rather than each repo: they release together and the governance closure forces lockstep,
  so the ordinal names which composition a repo belongs to. Development happens on `dev/<N>` and each
  cycle is tagged `release-<N>`. This is not published.
- **Public** — `PUBLIC_VERSION`, tagged on every component repository. The platform is at **`v3`**.

**The published version is the public one: `v4` is `4.0.0`.** The standard the packages implement is a
separate artifact on its own track and is not this number.

The standard these packages implement is published separately: https://doi.org/10.5281/zenodo.22150616
