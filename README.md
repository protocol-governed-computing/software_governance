# software_governance

**The normative platform surface — what a conforming PGC system is allowed to be.**

Every governed behavior in a PGC composition resolves, eventually, against a declaration in this
repository. It holds the constitutions, invariants, structures, schemas, surface contracts,
reserved vocabulary, and the neutral capability transforms and side effects that no single domain
owns and every domain depends on.

It contains **no code of any kind**. It declares; the sibling toolchain reads.

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
| `doc/` | The surface map, the governance doctrine, and the rulings that settled contested questions |

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

Then diff the resulting closure against `doc/GOVERNANCE_SURFACE_MAP.md` §6. An unresolved reference
is either a missing platform artifact or a leaked domain reference — resolved by adding the former
or moving the latter into the domain that owns it.

## License

See `LICENSE` and `NOTICE`.
