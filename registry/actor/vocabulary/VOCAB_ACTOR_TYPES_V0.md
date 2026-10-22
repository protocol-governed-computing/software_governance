# VOCAB_ACTOR_TYPES_V0

## Machine

```yaml
fqdn: actor::VOCAB_ACTOR_TYPES_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: actor
extends: ''
actor_type:
  casing: lower_snake
  entries:
  - agent
  - human
  - system
```

---

## Intent

The governed actor type vocabulary that `actor::CONSTITUTION_ACTOR_IDENTITY_V0` requires
(`AC_TYPE_REQUIRED`). Every actor declares one of these as its `core.type`.

- `human`: a person who acts through the boundary, such as a participant, a member of staff, a
  requester or an author of record.
- `agent`: an AI agent. It emits intents probabilistically, so a governance domain must be able to
  tell it from a person.
- `system`: software that acts on its own account, such as a runtime, a governor or a model host.

A type says what kind of participant an actor is. It confers no authority: what an actor may do is
governed elsewhere (`AC_NO_AUTHORITY_SEMANTICS`). The vocabulary is closed. A domain cannot extend
it, so every composition sorts its actors the same way.
