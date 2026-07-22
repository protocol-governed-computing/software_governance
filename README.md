# platform

**The PGC Normative Platform Surface — namespace `pgc::`.**

This repository is the authoritative closure of protocol artifacts from which `pgc::` is
**constituted**: the constitutions, invariants, structures, schemas, surface contracts,
vocabulary, and the neutral capability transforms (CT) and side effects (CS) that every
conforming Protocol-Governed Computing system depends on.

It contains **normative artifacts only** — it declares *what the platform is allowed to
be*. It contains no reference-implementation code. The compiler and runtime that read and
execute this surface are the Reference Implementation authority (RI-0), hosted separately.

> **Orientation:** the standard, its authorities, and the harvest strategy live in
> [`pgc-charter`](https://github.com/protocol-governed-computing/pgc-charter) —
> see `doc/NORMATIVE_PLATFORM_SURFACE.md`, `doc/HARVEST_LEDGER.md`,
> `doc/ORGANIZATION_TOPOLOGY.md`.

---

## Contents

| Path | Contents |
|------|----------|
| `registry/FB_*/` | Governance normative surface — federation boundaries: constitutions, invariants, structures, schemas, surface contracts, vocabulary |
| `capability_transforms/registry/` | Neutral, domain-agnostic CT declarations |
| `capability_side_effects/registry/` | Neutral CS declarations (storage / registry / etc.) |
| `doc/rule_ownership.md` | Governance doctrine |

## What this repository is **not**

- Not a code repository — no compiler, runtime, handlers, executors, or tests.
- Not a place for domain artifacts — `blockchain`, `ai_governance`, and any
  `fb.blockchain` / `fb.ai_governance` boundary belong to `pgs::`, not here.

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
