# CONSTITUTION_STRUCTURE_V0

## Machine
```yaml
fqdn: structure::CONSTITUTION_STRUCTURE_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: structure
core:
  enforcement_model: process_and_compiler_enforced
  governs:
  - STRUCTURE
rules:
- applies_to: STRUCTURE
  enforced_by: structure::INVARIANT_STRUCTURE_PATHS_WELL_FORMED_V0
- applies_to: STRUCTURE
  enforced_by: structure::INVARIANT_STRUCTURE_PATHS_WELL_FORMED_V0
- applies_to: STRUCTURE
  enforced_by: structure::INVARIANT_STRUCTURE_PATHS_WELL_FORMED_V0
- applies_to: STRUCTURE
  enforced_by: structure::INVARIANT_STRUCTURE_PATHS_WELL_FORMED_V0
- applies_to: STRUCTURE
  enforced_by: structure::INVARIANT_SCHEMA_DESCRIPTION_WELL_FORMED_V0
- applies_to: STRUCTURE
  enforced_by: PROCESS_ENFORCED
- applies_to: STRUCTURE
  enforced_by: PROCESS_ENFORCED
- applies_to: STRUCTURE
  enforced_by: artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0
```


---

## What makes a description a description

A schema governing an artifact kind **names at least one required field and closes its surface**. One
that does neither admits every declaration of its kind and refuses none, and a kind dispatched to it
reads as governed by any reader counting dispatched kinds. **Coverage is not governance**, and the
count of dispatched kinds measures neither.

That was not a hypothetical. One kind was dispatched to a description requiring no field and closing
no surface, and thirty-three declarations passed it because everything passes it.

## Every kind carries a disposition

An artifact kind is **described** or **exempt**, drawn from `structure::VOCAB_SCHEMA_DISPOSITION_V0`,
and a kind carrying neither is refused. An exemption states its ground beside it.

A kind absent from the dispatch table was absent for three different reasons and one representation:
nobody wrote a description, one exists and nobody named it, or the kind needs none. A reader could not
tell a decision from an oversight, and neither could a check.

## A description matches what it describes

A description states the shape the platform currently builds. One that has drifted refuses correct
work **with the authority of a rule**, which is worse than describing nothing, so a description is
measured against every artifact of its kind before it is dispatched — never dispatched to find out.

Drift is continuous rather than episodic. Three descriptions were found to have diverged at three
separate undated points, and every one was found by dispatching it and reading what it refused: a
method that only works while nobody relies on the description. `INVARIANT_SCHEMA_DESCRIPTION_WELL_FORMED_V0`
is what reports the next one before a build does.

---

## 1. Purpose

This constitution governs STRUCTURE artifacts — the configuration authority for the entire protocol system.

A STRUCTURE artifact declares how the protocol discovers, loads, and routes artifacts. It is the sole source of path governance, layer resolution, and artifact discovery configuration.

For structural field definitions see: `registry/schema/SCHEMA_STRUCTURE_V0.json`
For usage examples and path patterns see: `doc/STRUCTURE_GUIDE.md`

---

## 2. Core Principles

- **Explicit Declaration:** All paths and layers MUST be explicitly declared. No implicit defaults.
- **Layer-Relative Paths:** All paths are relative to a declared layer root. Absolute paths are forbidden.
- **Layer Isolation:** Subpaths MUST NOT use `..` to escape layer boundaries.
- **Deterministic Resolution:** Same STRUCTURE artifact MUST produce identical resolution output.
- **Bootstrap Eligibility:** Runtime STRUCTURE artifacts MUST be loadable without the compiler.

---

## 3. Relationship to Other Constitutions

- `CONSTITUTION_COMPILER_V0` — compiler consumes STRUCTURE for artifact discovery (STRUCTURE_FQDN_TREE_AUTHORITY rule)
- `STRUCTURE_LAYER_AUTHORITY_V0` — declares valid layer codes that STRUCTURE artifacts may reference
- `CONSTITUTION_GOVERNANCE_V0` — root authority

---

## End of Constitution

---

## What this realizes
```yaml
core:
  description: Governs STRUCTURE artifacts — system configuration and artifact discovery declarations
rules:
- rule_id: STRUCTURE_EXPLICIT_PATHS
  constraint: all paths MUST be explicitly declared; no implicit defaults, heuristics, or fallback
- rule_id: STRUCTURE_NO_ABSOLUTE_PATHS
  constraint: absolute filesystem paths are forbidden; all paths MUST be layer-relative
- rule_id: STRUCTURE_NO_ESCAPE
  constraint: subpaths MUST NOT contain ".." layer escapes
- rule_id: STRUCTURE_LAYER_DECLARED
  constraint: every path declaration MUST reference a valid declared layer code
- rule_id: STRUCTURE_DETERMINISTIC_RESOLUTION
  constraint: given identical STRUCTURE artifact, path resolution MUST be deterministic
- rule_id: STRUCTURE_BOOTSTRAP_ELIGIBLE
  constraint: runtime STRUCTURE artifacts MUST be loadable without compiler
- rule_id: STRUCTURE_FQDN_REFERENCES
  constraint: all artifact references in STRUCTURE MUST use FQDN
```
