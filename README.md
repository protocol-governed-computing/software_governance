# platform

**The PGC Normative Platform Surface — namespace `pgc::`.**

This repository is the authoritative closure of protocol artifacts from which `pgc::` is
**constituted**: the constitutions, invariants, structures, schemas, surface contracts,
vocabulary, and the neutral capability transforms (CT) and side effects (CS) that every
conforming Protocol-Governed Computing system depends on.

It contains **normative artifacts only** — it declares *what the platform is allowed to
be*. It contains no reference-implementation code. The compiler and runtime that read and
execute this surface are the Reference Implementation authority (RI-0), hosted separately.

> **Orientation:** the standard and its authorities live in
> [`standards`](https://github.com/protocol-governed-computing/standards) —
> see `doc/spec/` and `doc/NAMESPACE_MODEL.md`.

---

## Contents

| Path | Contents |
|------|----------|
| `registry/FB_*/` | Governance normative surface — federation boundaries: constitutions, invariants, structures, schemas, surface contracts, vocabulary |
| `capability_transforms/registry/` | Neutral, domain-agnostic CT declarations |
| `capability_side_effects/registry/` | Neutral CS declarations (storage / registry / etc.) |
| `doc/rule_ownership.md` | Governance doctrine |

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
