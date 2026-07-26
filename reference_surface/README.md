# PGC Platform Reference Surface

**Version: 1.0.0** — locked reference. A stable, externally observable surface that exercises the
**platform execution path** end-to-end against a known warm-boot snapshot.

## Scope (v1.0.0)

One reference workload, surfaced through the governed transport boundary:

```
HTTP  →  HTTP Adapter  →  Canonical Transport  →  TI_COLLATZ_COMPUTE  →  WF_COLLATZ_CONJECTURE  →  Runtime  →  TE  →  HTTP
```

- **Collatz Conjecture** (`collatz.compute`) — compute a sequence through the boundary; view the
  live trace (evidence) and the compiled workflow DAG projection.

Inspection (the Protocol Inspector, `pi`) is **not** part of this surface: it is a *downstream
consumer* of the assembled snapshot and lives in the separate `protocol_inspector` component, not
in the platform. This surface demonstrates **execution**, not inspection.

## Layout

```
reference_surface/
  serve.sh              composition launcher — points the domain-neutral transport engine at platform roots
  bindings/http.json    HTTP External Protocol Binding (route → operation identity)
  client/web/
    index.html          landing (Collatz)
    css/base.css
    collatz/            the Collatz client (screen + rewired canonical-transport bridge)
```

Boundary declarations (`TI`/`TE`) live with the workload at
`reference_workloads/collatz/transport/`, not here.

## Run

```bash
./serve.sh                 # http://127.0.0.1:8000  (override: PGC_HTTP_PORT / PGC_DATA_ROOT)
```

Requires the sibling `protocol_runtime` (execution), the assembled `snapshot/` (read-only), and
the domain-neutral `transport/` engine — all env-provisioned by `serve.sh`.

## What it proves

- One governed **Operation Identity** (`collatz.compute`) is stable while the bound workflow is an
  implementation detail.
- The transport engine is **domain-neutral** — no workload knowledge in `transport/`.
- Recursion/unbounded iteration is governed as a **finite, acyclic DAG** with no `loop` primitive
  (see the Collatz screen's "recursion without a loop" note).

## Locking

v1.0.0 is prepared for locking as an immutable reference. Subsequent changes are a new version,
not an in-place edit.
