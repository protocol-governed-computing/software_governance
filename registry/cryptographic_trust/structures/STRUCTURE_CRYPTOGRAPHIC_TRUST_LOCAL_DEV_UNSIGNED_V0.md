# STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0

## Machine

```yaml
fqdn: cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0
artifact_code: STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V0
artifact_kind: STRUCTURE
version: V0
governed_by: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0
authority: pgc.platform
concern: cryptographic_trust
trust_mode: LOCAL_DEV_UNSIGNED
artifact_signing_required: false
payload_signing_required: false
trace_signing_required: false
trust_anchor: none
```

---

## Purpose

Declares that unsigned local development is an available trust posture.

A composition built under it requires no signature over the snapshot, and none over payloads or
traces. Trust is implicit, which is right for local development and a single operator. The
constitution confines it there: a composition declaring this mode is not deployed to non-local
execution substrates.

A build reaches this mode by naming it in `trust_mode`; the structure does not mark itself active.

## Availability is not activity

This structure carries no `status`. It states that the mode is **available** to a build, never that
it is **active** in one. Activity is named by a build configuration, and the composition that
results carries this structure and no other trust structure
(`INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V0`).
