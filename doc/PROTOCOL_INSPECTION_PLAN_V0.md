# Protocol Inspection (PI) — Phase 2 Plan V0

**Status:** greenlit (hybrid, phased). Design plan, not authorization to build all phases.
**Scope:** an educational, read-only inspection surface over the Reference Platform Snapshot,
exposed through the same governed transport boundary as the Collatz workload.
**Supersedes casual language:** "direct reads" from the initial proposal — see Rule 1.

---

## 1. Decision

Build PI as a **hybrid**: a thin, educational **Snapshot Explorer** first (Phase 2a), reserving
governed **computed inspection** for genuinely derived answers (Phase 2b). PI rides the existing
Canonical Transport boundary; it introduces new **handler kinds**, not a new boundary.

```
                    REFERENCE SURFACE
                  ┌────────┴────────┐
             Collatz UI         PI Explorer
                  ▼                 ▼
             HTTP /collatz      HTTP /pi
                  └────────┬────────┘
                    HTTP Adapter → Canonical Transport → TI (by handler kind)
              ┌──────────────┼───────────────┐
        WF_INVOCATION   SNAPSHOT_READ    SNAPSHOT_QUERY  [2b]
              ▼               ▼                ▼
        runtime.api      inspector.api    inspector.api
        run_workflow       (read)           (compute)
```

## 2. Architectural rules (baked in from review)

1. **Explorer ≠ engine.** Phase 2a is a *read-only projection of published snapshot artifacts*
   (`SNAPSHOT_READ`), not "direct reads" and not computed inspection. **Client rule:** the browser
   may **select, fetch, format, filter, and navigate** published snapshot data; it **must not
   derive PGC semantic relationships** (refs, closures, impact). Semantic computation stays
   server-side. The browser is an inspector, never a second PI engine.
2. **One route, many governed identities.** A single external binding `POST /pi` carries the
   Operation Identity **in the body** — but each is a **distinct, governed Operation Identity**
   with its **own TI/TE** (`pi.snapshot.summary`, `pi.artifact.show`, …). Do **not** create one
   generic `pi.query` TI that internally routes arbitrary operation strings — that would be a
   hidden RPC router inside the resolver. Operation names are full dotted identities
   (`pi.artifact.show`), never bare verbs (`show`).
3. **Three handler kinds** (the generalization, preserved from day one):
   - `WF_INVOCATION` — execute a workflow → `runtime.api.run_workflow` *(exists)*
   - `SNAPSHOT_READ` — retrieve published snapshot material → `inspector.api` *(Phase 2a)*
   - `SNAPSHOT_QUERY` — derive a result by traversing/evaluating snapshot state → `inspector.api` *(Phase 2b)*
4. **Resolver routes by kind to a static entry point; the inspector dispatches internally.** The
   transport resolver adds a `SNAPSHOT_READ` branch calling `inspector.api.query(operation, input,
   snapshot_root)` — exactly analogous to the `WF_INVOCATION → run_workflow` branch. The inspector
   maps operation identity → registered read/query behavior. Transport never interprets the
   operation string beyond selecting the handler kind. (Extends the transport CLAUDE.md rule:
   `runtime.*` and `inspector.*` are the permitted cross-repo execution/inspection interfaces.)
5. **Execution ≠ inspection.** `protocol_runtime` executes governed workflows; a new
   `protocol_inspector` inspects published snapshots. `SNAPSHOT_READ`/`SNAPSHOT_QUERY` resolve to
   `protocol_inspector`, **never** to runtime logic.
6. **Direct `/snapshot` fetch is for binary assets only** (e.g. behavior_logic `.projection.png`,
   as Collatz already does). Catalog inspection queries go through governed `SNAPSHOT_READ`
   operations so identities stay governed and the handler-kind abstraction is exercised immediately.

## 3. Phase 2a — Snapshot Explorer

**Handler kind:** `SNAPSHOT_READ`. **No computed engine.** Only queries that render generically
and are already materialized in the snapshot.

**Operations (each a distinct Operation Identity + TI/TE pair):**

| Operation | Input | Snapshot source |
|---|---|---|
| `pi.snapshot.summary` | — | `manifest.json`, `artifact_index/index.json` (domains, counts, hash, validity) |
| `pi.snapshot.topology` | — | domain → subdomain → WF map |
| `pi.artifact.list` | `{kind?, domain?}` | `artifact_index/index.json`, `pps/index.json` |
| `pi.artifact.show` | `{artifact: FQDN}` | `canonical/<domain>/<kind>/…json` |
| `pi.vocab.search` | `{term}` | `vocabulary/<domain>/forward.json` |
| `pi.vocab.resolve` | `{artifact: FQDN}` | `vocabulary/*` (FQDN → structure, paths, addresses) |
| `pi.behavior_logic.list` | `{domain?}` | `behavior_logic/*` |
| `pi.behavior_logic.show` | `{wf: FQDN}` | `behavior_logic/<domain>/<WF>/*.graph.json` (+ PNG via `/snapshot` mount) |

**Components:**
- **`protocol_inspector`** (new, thin, read-only): `inspector.api.query(operation, input,
  snapshot_root) -> result`. Internally dispatches the operations above as published-material
  projections. No graph traversal, no evaluation.
- **transport** (`resolver/`): add the `SNAPSHOT_READ` handler-kind branch → `inspector.api.query`.
- **External Protocol Binding:** extend the binding data so a route may admit an operation from the
  body against a **declared allowlist/namespace** (not an open RPC). `POST /pi` → `{pi.*}`.
- **platform `reference_surface/transport/pi/`**: one `TI_`/`TE_` pair per operation
  (`SNAPSHOT_READ`; TE output/evidence policy per query).
- **platform `reference_surface/client/web/pi/`**: the Protocol Inspection Surface (see §5).
- **platform `reference_surface/bindings/http.json`**: add the `POST /pi` binding.

## 4. Phase 2b — Computed Inspection

**Handler kind:** `SNAPSHOT_QUERY`. Governed operations that derive results:
`pi.artifact.refs` / `pi.artifact.deps` / `pi.artifact.lineage`, `pi.topology.impact` /
`pi.topology.path`, `pi.snapshot.validate` / `pi.snapshot.violations`.

- `protocol_inspector` gains the traversal/evaluation engine over the artifact graph.
- resolver adds the `SNAPSHOT_QUERY` branch (same static entry point, compute semantics).
- **Standard §6 amendment (when 2b lands):**
  > A TI binds an Operation Identity to a **compiled handler target**. The handler target may be a
  > workflow invocation, a snapshot read, a snapshot query, or another standardized PGC boundary
  > handler.
  This replaces the current "operation → WF" phrasing with the stronger handler-target abstraction.

## 5. UI — Protocol Inspection Surface (vanilla JS, no frameworks)

Not a dashboard, not a file browser, not 30 commands dumped on one screen. A **catalog-like
navigation** of the formal inspection vocabulary with **progressive disclosure**:

```
Protocol Inspection — read-only inspection of the PGC snapshot
  SNAPSHOT      Overview · Status · Counts · Topology
  ARTIFACTS     Browse · Show
  VOCABULARY    Search · Resolve · Stats
  BEHAVIOR      Workflows · Logic Graphs
  COMPUTED INSPECTION  [Phase 2b]  References · Dependencies · Impact
```

Interaction: **Query → small parameter selector → result panel.** Results open in **floating,
draggable, closable panels** (a ~100-line vanilla-JS panel manager: create / drag / focus by
z-index / close). Open several and arrange them to **compare** without navigating away. Rendering:
collapsible JSON tree (artifacts), simple table (lists), `<img>` for behavior_logic PNGs (reuse the
fail-soft pattern). The client only presents — Rule 1 holds.

## 6. Deferred (out of Phase 2)

- `artifact refs/deps/lineage`, `topology impact/path`, `validate/violations` → Phase 2b (computed).
- `behavior_logic render --mermaid/--dot` → the browser must not become a graph compiler; only if
  the server gains a clean generic rendering capability.
- `trace list/explain` → traces are **runtime output** (`data/…/traces`), not snapshot; `explain`
  delegates to `runtime examine`. Separate integration (Collatz already links raw traces).
- `store` category → after the core snapshot walk, if `artifact_index/stores.json` is present.

## 7. Guiding directive

> Proceed with Phase 2a first, but **preserve the handler-kind abstraction from the beginning.**
> That single decision (`TI → handler kind → handler target`) prevents the PI implementation from
> forcing a later transport redesign.

## 8. Decisions

**Confirmed:**
- **Rule 6** — catalog queries go through governed `SNAPSHOT_READ` operations; direct `/snapshot`
  fetch is reserved for binary assets (behavior_logic PNGs). ✅
- **`protocol_inspector`** — a **new sibling component** under the `protocol-governed-computing`
  org (package `inspector`, invoked via `inspector.api.query`). Not inside `protocol_runtime`. ✅
- **2a operation set** — **all eight** operations in §3. ✅

**Binding extension shape (confirmed).** Two data forms coexist in `http.json`, both governed (an
operation resolves only if a matching TI/TE is registered):
- *fixed operation* (Collatz today): `{ "method", "path", "operation" }`
- *namespaced operation-in-body* (PI): `{ "method": "POST", "path": "/pi", "operation_in_body":
  true, "namespace": "pi." }` — the adapter reads `operation` from the body and admits it only if it
  starts with `namespace` **and** resolves in the registry; otherwise `NOT_FOUND`.

> **`operation_in_body` is an external protocol binding feature. It does not introduce an operation
> dispatch mechanism into the adapter.** The extracted value is an Operation Identity and is resolved
> through the same governed operation registry as fixed operations. The adapter extracts the value
> and verifies the namespace admission constraint; it MUST NOT branch on operation semantics
> (`if operation == "pi.artifact.show"` is forbidden). The `pi.` namespace is an admission
> constraint, not a semantic dispatcher.
