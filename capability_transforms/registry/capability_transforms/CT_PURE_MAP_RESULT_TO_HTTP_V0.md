# CT_PURE_MAP_RESULT_TO_HTTP_V0

## Header

- **Artifact Code:** CT_PURE_MAP_RESULT_TO_HTTP_V0
- **Artifact Kind:** atom
- **Governed By:** fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** v0
- **Status:** draft
- **Dependencies:** NONE

---

## Machine

```yaml
fqdn: capability_transforms::CT_PURE_MAP_RESULT_TO_HTTP_V0
artifact_kind: CAPABILITY_TRANSFORM
version: V0
governed_by: fb.capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
core:
  summary: Map result status to HTTP
  description: Maps an execution result status code to a corresponding HTTP status code and response body
    using a provided mapping object.
  inputs:
    execution_result:
      type: object
      required: true
      description: The workflow execution result object
    mapping:
      type: object
      required: true
      description: Status code mapping (e.g., SUCCESS -> 200)
  outputs:
    http_status:
      type: integer
      required: true
      description: Resulting HTTP status code
    response_body:
      type: object
      required: true
      description: Composed response body
    result_status:
      type: string
      required: true
      description: Original execution status
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: MAP_RESULT_TO_HTTP
  implementation:
    module: pgs_transforms.implementation.transforms.atoms.ct_pure_map_result_to_http_v0
    callable: execute
```
