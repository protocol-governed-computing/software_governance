# CS_TEXT_ARTIFACT_V0

## Header (Mandatory)

- **Artifact Code:** CS_TEXT_ARTIFACT_V0
- **Artifact Kind:** capability_side_effect
- **Governed By:** CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Persist rendered protocol artifacts as text documents beneath a policy-declared root.

Construction renders; this writes. Rendering is a pure transformation of a design into artifacts and
must stay pure — the moment it touched a filesystem its result would depend on something the
composition cannot see, and the same design would stop producing the same output.

---

## 2. The root is policy, never an input

A caller that named its own destination could write anywhere the process can reach. Where generated
artifacts land is a governance decision, so it belongs to the runtime binding that declares the
policy rather than to whoever dispatched the workflow. A path that escapes the declared root is
refused rather than resolved.

---

## 3. One operation writes the whole construction

A capability contract is a fixed pipeline with no iteration, so persisting twenty-five artifacts one
call at a time is not expressible. `WRITE_ALL` takes the whole set, which also makes the outcome
the one that matters: either the construction was persisted or it was not.

---

## Machine

```yaml
fqdn: capability_side_effects::CS_TEXT_ARTIFACT_V0
artifact_kind: CAPABILITY_SIDE_EFFECT
version: v0
governed_by: fb.capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
core:
  summary: Persist rendered protocol artifacts as text documents beneath a declared root
  category: storage
  policy:
    operations:
    - WRITE_ALL
    - LIST
  field_types:
    documents: array
    written: integer
    paths: array
    result_status: string
  operations:
    WRITE_ALL:
      summary: Persist every rendered document in one operation
      handler: write_all
      input:
      - documents
      output:
      - result_status
      - written
      - paths
      idempotent: true
      result_status_values:
      - SUCCESS
      - VIOLATION
      - BACKEND_ERROR
    LIST:
      summary: List the documents currently persisted beneath the root
      handler: list
      input: []
      output:
      - result_status
      - paths
      idempotent: true
      result_status_values:
      - SUCCESS
      - NOT_FOUND
      - BACKEND_ERROR
implementation:
  module: capability_side_effects.implementation.CS_TEXT_ARTIFACT_V0.runtime
  callable: TextArtifactRuntime
extensions:
  cs_kind: text_document_store
  side_effect_type: persistent
  properties:
    durability: persistent
    idempotent: true
    replay_policy: overwrite
    transactional: false
    concurrent_safe: false
  constraints:
    concurrency: single_writer
    containment: paths must resolve beneath the declared root
  vocabulary:
    result_status:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
  configuration_schema:
    root:
      type: string
      required: true
      description: Filesystem root beneath which every rendered document is written
  failure_modes:
  - 'VIOLATION: documents is not a non-empty array of {path, text}'
  - 'VIOLATION: a path escapes the declared root'
  - 'BACKEND_ERROR: the root is unwritable'
```
