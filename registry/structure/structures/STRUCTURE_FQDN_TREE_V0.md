# STRUCTURE_FQDN_TREE_V0

## Header
- Artifact Code: STRUCTURE_FQDN_TREE_V0
- Tier: Sovereign Authority
- Artifact Kind: structure
- Governed By: governance::CONSTITUTION_GOVERNANCE_V0
- Version: v0
- Status: active
- Supersedes: NONE
- Dependencies: []

---

## 1. Purpose

Declare the authoritative logical package tree and the folder → namespace correspondence for the
PGC governance surface.

This document records:
- Source packages that participate in a build, and their physical roots
- The correspondence between registry folders and declared namespaces
- File patterns by which artifacts are discovered

---

## 2. Global Rules

- Physical directory layout is mapped, not inferred.
- Dependencies must be acyclic and forward-only.
- Runtime bindings, where declared, MUST be domain-scoped and SHALL NOT appear in shared registries.

### 2.1 Identity is declared, not derived

Namespace identity is **declared per artifact** in the `fqdn:` key of its `## Machine` block. It is
not computed from the folder an artifact sits in. The `namespace_mappings` below are therefore
**descriptive** — they record where artifacts of each namespace live, so that discovery and human
navigation agree. Moving a file does not change what an artifact *is*.

The registry is organized **one directory per namespace**, so the mapping is currently one-to-one:
`registry/<namespace>/<kind>/`. That correspondence is a convenience, not the source of identity —
a future layout may group or split directories without any FQDN changing. `registry/schema/` is the
sole exception: JSON schemas are a declaration substrate and carry no namespace at all.

---

## 3. Package Roles

| Role | Description |
|------|-------------|
| `governance_surface` | Normative protocol artifacts — the governance surface itself |
| `capability_pack` | Reusable capability declarations (CT / CS) |
| `workload` | Workloads that prove conformance |

### 3.1 Domain Isolation Invariant

Domain artifacts SHALL NOT appear in governance-surface packages. The platform namespace set is
reserved for protocol substrate only.

- `governance_surface` packages may contain only normative platform artifacts.
- `capability_pack` packages may contain only reusable CT/CS declarations.
- `workload` packages may contain workload artifacts and workload-scoped CT/CS.

---

## 4. Authority Levels

| Authority | Description |
|-----------|-------------|
| `sovereign` | Root authority, defines protocol semantics |
| `delegated` | Authority derived from sovereign, must comply with core |

---

## 5. Build Contract

Builder MUST:
- Resolve physical paths explicitly
- Respect `artifact_patterns` for file discovery
- Load only declared registries

Builder MUST NOT:
- Infer namespace from folder names
- Include undeclared artifacts

---

## 6. Determinism & Trace Binding

- This document is hashed as part of the build manifest.
- Any change to this file constitutes a governance-visible change.

---

## 7. Versioning

- Changes require a new version. Backward compatibility is not assumed.

---

## Machine

```yaml
fqdn: structure::STRUCTURE_FQDN_TREE_V0
artifact_kind: STRUCTURE
version: V0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: structure
core:
  summary: Logical package tree and folder-to-namespace correspondence
  description: 'Declares source packages and their physical roots, and records which namespaces are
    declared by artifacts in each registry folder. Namespace identity is declared per artifact; the
    folder mapping is descriptive.

    '
packages:
- package: software_governance
  role: governance_surface
  authority: sovereign
  build_order: 0
  physical_root: .
  module_root: registry
  contains:
  - registry
  - capability_transforms
  - capability_side_effects
  registries:
  - path: registry/actor
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace actor
  - path: registry/artifact
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace artifact
  - path: registry/authority
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace authority
  - path: registry/capability_contracts
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace capability_contracts
  - path: registry/capability_side_effects
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace capability_side_effects
  - path: registry/capability_transforms
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace capability_transforms
  - path: registry/compiler
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace compiler
  - path: registry/conformance
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace conformance
  - path: registry/cryptographic_trust
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace cryptographic_trust
  - path: registry/event
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace event
  - path: registry/execution
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace execution
  - path: registry/execution_placement
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace execution_placement
  - path: registry/execution_scheduling
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace execution_scheduling
  - path: registry/execution_topology
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace execution_topology
  - path: registry/federation
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace federation
  - path: registry/governance
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace governance
  - path: registry/intent
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace intent
  - path: registry/lifecycle
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace lifecycle
  - path: registry/runtime_binding
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace runtime_binding
  - path: registry/security_domain
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace security_domain
  - path: registry/structure
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace structure
  - path: registry/surface_contract
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace surface_contract
  - path: registry/trace
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace trace
  - path: registry/transport
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace transport
  - path: registry/vocabulary
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace vocabulary
  - path: registry/workflow
    artifact_types:
    - constitutions
    - invariants
    - structures
    - surface_contracts
    - vocabulary
    notes: Namespace workflow
  - path: registry/schema
    artifact_types:
    - schemas
    notes: Declaration substrate — JSON schemas, not an fb.* namespace
  depends_on: []
- package: capability_transforms
  role: capability_pack
  authority: delegated
  build_order: 1
  physical_root: ./capability_transforms
  module_root: capability_transforms
  contains:
  - registry
  registries:
  - path: registry/capability_transforms
    artifact_types:
    - capability_transforms
  depends_on:
  - software_governance
- package: capability_side_effects
  role: capability_pack
  authority: delegated
  build_order: 2
  physical_root: ./capability_side_effects
  module_root: capability_side_effects
  contains:
  - registry
  - implementation
  registries:
  - path: registry/capability_side_effects
    artifact_types:
    - capability_side_effects
  depends_on:
  - software_governance
namespace_mappings:
  registry/actor:
  - actor
  registry/artifact:
  - artifact
  registry/authority:
  - authority
  registry/capability_contracts:
  - capability_contracts
  registry/capability_side_effects:
  - capability_side_effects
  registry/capability_transforms:
  - capability_transforms
  registry/compiler:
  - compiler
  registry/conformance:
  - conformance
  registry/cryptographic_trust:
  - cryptographic_trust
  registry/event:
  - event
  registry/execution:
  - execution
  registry/execution_placement:
  - execution_placement
  registry/execution_scheduling:
  - execution_scheduling
  registry/execution_topology:
  - execution_topology
  registry/federation:
  - federation
  registry/governance:
  - governance
  registry/intent:
  - intent
  registry/lifecycle:
  - lifecycle
  registry/runtime_binding:
  - runtime_binding
  registry/security_domain:
  - security_domain
  registry/structure:
  - structure
  registry/surface_contract:
  - surface_contract
  registry/trace:
  - trace
  registry/transport:
  - transport
  registry/vocabulary:
  - vocabulary
  registry/workflow:
  - workflow
  capability_transforms/registry/capability_transforms:
  - capability_transforms
  capability_side_effects/registry/capability_side_effects:
  - capability_side_effects
role_artifact_rules:
  governance_surface:
  - constitutions
  - invariants
  - structures
  - schemas
  - vocabulary
  - surface_contracts
  capability_pack:
  - capability_transforms
  - capability_side_effects
  workload:
  - capability_contracts
  - capability_transforms
  - capability_side_effects
  - intents
  - workflows
  - events
  - actors
  - runtime_bindings
  - transport_intents
  - transport_egress
artifact_patterns:
  constitutions:
    file_pattern: CONSTITUTION_*.md
    code_key: artifact_code
  invariants:
    file_pattern: INVARIANT_*.md
    code_key: artifact_code
  structures:
    file_pattern: STRUCTURE_*.md
    code_key: artifact_code
  vocabulary:
    file_pattern: VOCAB_*.md
    code_key: artifact_code
  surface_contracts:
    file_pattern: SURFACE_CONTRACT_*.md
    code_key: artifact_code
  schemas:
    file_pattern: SCHEMA_*.json
    code_key: $id
  capability_transforms:
    file_pattern: CT_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  capability_side_effects:
    file_pattern: CS_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  capability_contracts:
    file_pattern: CC_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  intents:
    file_pattern: IN_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  workflows:
    file_pattern: WF_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  events:
    file_pattern: EV_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  actors:
    file_pattern: AC_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  runtime_bindings:
    file_pattern: RB_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  transport_intents:
    file_pattern: TI_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
  transport_egress:
    file_pattern: TE_*.md
    code_key: artifact_code
    exclude_patterns:
    - CONSTITUTION_*.md
output_configuration:
  _type: metadata
```
