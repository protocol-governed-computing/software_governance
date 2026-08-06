# CS_SNAPSHOT_QUERY_V0

## Header (Mandatory)

- **Artifact Code:** CS_SNAPSHOT_QUERY_V0
- **Artifact Kind:** capability_side_effect
- **Governed By:** CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Observe an assembled snapshot through the governed inspection surface.

**This capability exists so that observation is never ad hoc.** Whenever any workflow needs a fact
about the composition it runs inside — which artifacts exist, what a store contains, what a
vocabulary resolves to — it asks through this capability. It does not read projection files, and it
does not import the compiler that produced them.

The capability is deliberately general. It is not named for, or shaped around, any one consumer:
the phases of the transformation pipeline are simply the first workflows to need it, and any future
domain that must observe the assembled system uses the same governed route.

## 2. Why observation is a side effect

Reading a snapshot is not pure. The same query yields different answers against different
compositions, so a transform that consulted a snapshot would be neither deterministic nor
replayable from its declared inputs alone. Observation therefore belongs on the side-effect side of
the boundary, where the thing being read is bound explicitly by a runtime binding rather than
discovered.

That the result is *stable for a given snapshot* is what makes it usable as evidence; that it
varies *across* snapshots is what makes it a side effect.

## 3. Why it delegates to the inspection surface

The operations this capability exposes are the published `si.*` inspection operations, and nothing
else. It resolves them through `inspector.api.query` — the same interface any external reader uses.

The alternative, reaching into compiled projections directly, is precisely the coupling the
inspection boundary was built to remove: a consumer that reads projection layout is bound to the
compiler's internals and breaks whenever they change. A capability that reads through the published
surface is bound only to the operation catalogue, which is itself governed.

## 4. Read-only by construction

Every operation is a read. There is no write, no delete, no mutation of any kind — a capability
that could alter the composition it observes would make its own evidence unreliable, and would let
a workflow modify the sealed snapshot it is executing from.

---

## Machine

```yaml
fqdn: capability_side_effects::CS_SNAPSHOT_QUERY_V0
artifact_kind: CAPABILITY_SIDE_EFFECT
version: v0
governed_by: fb.capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
core:
  summary: Read-only observation of an assembled snapshot through the governed inspection surface
  category: inspection
  policy:
    operations:
    - QUERY
    - CATALOG
  field_types:
    operation: string
    params: object
    result: object
    operations: array
    result_status: string
  operations:
    QUERY:
      summary: Execute a published si.* inspection operation against the bound snapshot
      handler: query
      input:
      - operation
      - params
      output:
      - result_status
      - result
      idempotent: true
      result_status_values:
      - SUCCESS
      - NOT_FOUND
      - VIOLATION
      - BACKEND_ERROR
    CATALOG:
      summary: List the inspection operations the bound snapshot answers
      handler: catalog
      input: []
      output:
      - result_status
      - operations
      idempotent: true
      result_status_values:
      - SUCCESS
      - BACKEND_ERROR
  semantics:
    durability: read_only
    idempotent: true
    replay_policy: safe_replay
    transactional: false
    concurrent_safe: true
  constraints:
    mutates_snapshot: false
    resolves_through: inspector.api.query
  vocabulary:
    result_status:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
  configuration_schema:
    snapshot_root:
      type: string
      required: true
      description: Filesystem path to the assembled snapshot to observe
  failure_modes:
  - 'VIOLATION: operation is not a published inspection operation, or params are malformed'
  - 'NOT_FOUND: the operation ran but the requested subject does not exist in the snapshot'
  - 'BACKEND_ERROR: snapshot root missing, unreadable, or not an assembled snapshot'

implementation:
  module: capability_side_effects.implementation.CS_SNAPSHOT_QUERY_V0.runtime
  callable: SnapshotQueryRuntime
```
