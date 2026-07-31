# STRUCTURE_CT_IR_CONTRACT_V0

## Purpose
Defines the canonical execution contract for Capability Transform IR (CT-IR).
All CT artifacts MUST conform to this structure at compile time.

---

## Machine

```yaml
fqdn: fb.capability_transforms::STRUCTURE_CT_IR_CONTRACT_V0
artifact_kind: STRUCTURE
version: V0
governed_by: fb.structure::CONSTITUTION_STRUCTURE_V0
contract:
  name: CT_IR
  version: V0
required_fields:
- artifact_code
- atom_stream
- ct_composition_version
- inputs
- outputs
field_types:
  artifact_code: string
  atom_stream: list
  ct_composition_version: string
  inputs: dict
  outputs: dict
invariants:
- atom_stream MUST NOT be empty
- ct_composition_version MUST be "V0"
```

---

## ONE-LINE
```text
Compiler MUST produce CT-IR matching this contract — runtime only enforces it
```
