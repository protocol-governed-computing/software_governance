# STRUCTURE_CRYPTOGRAPHIC_TRUST_SIGNED_SNAPSHOT_V1

## Machine

```yaml
fqdn: cryptographic_trust::STRUCTURE_CRYPTOGRAPHIC_TRUST_SIGNED_SNAPSHOT_V1
artifact_code: STRUCTURE_CRYPTOGRAPHIC_TRUST_SIGNED_SNAPSHOT_V1
artifact_kind: STRUCTURE
version: V1
governed_by: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V1
authority: pgc.platform
concern: cryptographic_trust
trust_mode: SIGNED_SNAPSHOT
artifact_signing_required: true
payload_signing_required: false
trace_signing_required: false
trust_anchor: operator_key
```

---

## Purpose

Declares that a signed snapshot is an available trust posture.

A composition built under it is accepted only with a signature over its identity, made with an
operator-held key. A node executing it holds the public half of that key as its trust anchor, and
refuses a snapshot whose signature does not verify against it, or that carries none. Payloads and
traces are not signed under this mode.

## What is signed, and what verifies it

The signature is over the snapshot's identity, `snapshot_id`, and not over the manifest file. The
identity is what the composition is. The manifest describes it and sits outside what the identity
covers, so a signature over the file would bind to bytes the identity does not. The record is a
sidecar, because a sealed manifest is written once.

The key that verifies comes from the node and never from the snapshot. A snapshot carrying the key
that authenticates it authenticates nothing: whoever replaced the snapshot would replace the key
with it. Only the private half signs, and it is held by the operator on the build machine, never by
a node that executes. A node can establish that its snapshot is the one, and cannot mint one its
peers would accept.

## Availability is not activity

This structure carries no `status`. It states that the mode is **available** to a build, never that
it is **active** in one. Activity is named by a build configuration, and the composition that
results carries this structure and no other trust structure
(`INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V1`).
