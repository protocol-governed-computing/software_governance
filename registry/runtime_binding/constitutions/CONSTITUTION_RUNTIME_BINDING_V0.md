# CONSTITUTION_RUNTIME_BINDING_V0

## Machine
```yaml
fqdn: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: runtime_binding
core:
  enforcement_model: compiler_enforced
  governs:
  - RB
rules:
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_RB_NO_LOGIC_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_RB_CS_ONLY_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_RB_NO_LOGIC_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_RB_NO_LOGIC_V0
- applies_to: RB
  enforced_by: artifact::INVARIANT_FQDN_ONLY_REFERENCES_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_RB_BINDING_POLICY_CONFORMANCE_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_RB_PARAMETERS_DECLARED_V0
- applies_to: RB
  enforced_by: runtime_binding::INVARIANT_RB_STORAGE_SUBDOMAIN_OWNED_V0
```

---

## 1. Purpose

This constitution defines the governance and enforcement rules for Runtime Binding (RB) artifacts.

Runtime bindings map declared CS capability artifacts to their concrete host implementations. They supply the configuration that connects protocol-declared capabilities to physical storage and I/O resources at runtime.

---

## 2. Core Principles

- **Deterministic Binding:** Every binding MUST be explicit and produce the same resolution given the same input. No dynamic discovery or late binding.
- **CS-Only:** Runtime bindings bind CS artifacts exclusively. CT and WF artifacts are never bound — they resolve through different mechanisms.
- **No Behavior Extension:** A binding configures a CS capability; it MUST NOT add, remove, or alter the semantics declared in the CS artifact.
- **No Logic:** RB artifacts are mapping declarations. They MUST NOT contain conditional logic, transformations, or execution expressions.
- **FQDN Keys:** All capability references used as binding keys MUST use fully-qualified names.

---

## 2a. Storage Resolution

*Where an act finds the records it works on. Stated here for the first time: the singular below was
carried by implementation and by a field's declared type, and by no rule.*

An act resolves its records against the storage descriptions its bindings name. **Today an act
operates under one binding and a binding names one description, and that is the case of one** — the
model admits several, and what is stated here holds however many there are.

- **A record is described once.** Exactly one storage description names a given record, and it is
  written by the subdomain that owns the record. Two descriptions of one record may disagree, and
  then what the business holds depends on which a run happened to read.
- **A description stays with its owner.** No subdomain's artifact describes another subdomain's
  storage. A statement maintained by someone other than the owner of what it describes is a second
  copy, and the second copy is the one nobody maintains.
- **The owner is the only writer.** A subdomain owns what it holds. Ownership that does not include
  being the only writer is not ownership.
- **A reach reads and never writes.** An act may resolve records another subdomain owns in order to
  consult them, because a second copy of one truth can disagree with the thing it describes. It may
  never change them: two subdomains deciding what is true leaves neither answerable.
- **A reach stays inside its domain.** An act resolves only what its own domain holds. An act
  reaching across a domain boundary is correct only in the compositions that include that domain,
  and fails when it runs in the ones that do not.
- **A reach is declared by the act that reaches**, in an artifact that act owns, and an act
  distinguishes the records it owns from those it merely consults. A declaration that grants the
  reach and hides that distinction cannot be held to reading.

---

## 3. Required Fields

- `rb_code`: Unique identifier for the runtime binding.
- `version`: Version of the runtime binding artifact.
- `governed_by`: The constitution governing this runtime binding.
- `core`: Metadata including summary and bindings map.
- `bindings`: Map of CS FQDN to implementation type and configuration.

---

## 4. Validation Rules

- Every binding key MUST be a valid CS FQDN that resolves to a declared CS artifact.
- Binding configuration MUST supply all required fields declared in the CS configuration schema.
- RB MUST NOT reference CT, WF, CC, or IN artifacts as binding targets.
- A binding's `storage_structure` MUST name a structure owned by the same subdomain as the binding.
  A binding naming another subdomain's storage description restates what that subdomain declares,
  which is the copy this constitution's §2a forbids.

---

## End of Constitution

---

## Rule Statement

```yaml
core:
  description: Governs mapping of CS capabilities to concrete host implementations
rules:
- rule_id: RB_DETERMINISTIC_BINDING
  constraint: bindings MUST be deterministic and explicit; no dynamic resolution
- rule_id: RB_CS_ONLY
  constraint: RB MUST bind CS artifacts only; never CT or WF
- rule_id: RB_NO_BEHAVIOR_EXTENSION
  constraint: binding MUST NOT alter capability semantics
- rule_id: RB_NO_LOGIC
  constraint: RB MUST NOT contain execution logic; it is a mapping declaration only
- rule_id: RB_FQDN_KEYS
  constraint: all binding keys MUST be FQDN
- rule_id: RB_STORAGE_SUBDOMAIN_OWNED
  constraint: a binding names storage described by its own subdomain; never another's
- rule_id: RB_RECORD_DESCRIBED_ONCE
  constraint: exactly one storage description names a given record, written by its owner
- rule_id: RB_REACH_READ_ONLY
  constraint: an act resolving records it does not own reads them and never changes them
- rule_id: RB_REACH_WITHIN_DOMAIN
  constraint: an act resolves only records its own domain holds
```
