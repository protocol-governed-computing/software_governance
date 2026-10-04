# CONSTITUTION_CRYPTOGRAPHIC_TRUST_V1

## Machine

```yaml
fqdn: cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V1
artifact_kind: CONSTITUTION
version: V1
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: cryptographic_trust
core:
  enforcement_model: process_and_compiler_enforced
rules:
- applies_to: compiled_snapshot
  enforced_by: cryptographic_trust::INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V1
- applies_to: compiled_snapshot
  enforced_by: PROCESS_ENFORCED
- applies_to: compiled_snapshot
  enforced_by: PROCESS_ENFORCED
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: runtime
  enforced_by: PROCESS_ENFORCED
```


---

## What an attestation contributes to a composition's identity

An attestation carries two kinds of field and the difference decides what a composition *is*.

**Constituting.** The projection the build produced, and the value taken over it. The runtime refuses
a composition whose projection does not match them, so they are enforced content and a composition's
identity is taken over them like any other constituent.

```
attestation.constitutes:  tokenized_projection_hash, attestation_hash
```

**Accompanying.** When the signing happened. It records something *about* the composition rather than
constituting it, nothing reads it, and it is excluded from the identity.

```
attestation.accompanies:  signed_at
```

**This is not a tidiness rule.** Until it was drawn, a composition's identity was a function of when
it was built: two compiles of unchanged source wrote ninety-one files each, ninety byte-identical,
and the ninety-first differed only in a microsecond timestamp. Every pin in the workspace expired on
the next rebuild — twenty of twenty-two could not be verified — and a genuine alteration was
indistinguishable from a no-op recompile, which is the one thing an identity over bytes exists to
prevent.

**Excluding the file was refused for the same reason.** The two constituting fields are enforced at
boot; dropping them from the identity would weaken it in the direction opposite to the fix. The
exclusion is of a field, and the platform already excludes two whole files on exactly this ground —
the self-description doing the enumerating, and material written after the composition was
constituted. This is that distinction at a finer grain.

## Building unchanged source twice yields one identity

A rebuild of source that has not changed produces the composition it produced before. A record naming
a composition nobody can reproduce makes every claim resting on it unverifiable, and nothing reported
that for as long as it was true.

**The claim is stability, not reproducibility.** What was measured is two builds on one machine
minutes apart. That the remaining ninety files matched establishes nothing about another machine,
another interpreter or another day, and a further instability is a further change.

---

## Purpose

This constitution governs the cryptographic trust posture under which PGC execution is
authorized. It answers: *what cryptographic guarantees are required for this snapshot to
be considered trustworthy and legally executable?*

Trust posture is a governance declaration, not a runtime configuration. The compiler
validates the declared trust mode; runtimes execute under it passively. This ensures
that moving from unsigned local development to signed, attested, or encrypted deployment
is a governance change, not a code change.

## §1. Authorized trust modes

Two trust modes are authorized. The surface declares a structure for each, and a build names one in
its `trust_mode`.

| Mode | Structure | What it requires |
|---|---|---|
| `LOCAL_DEV_UNSIGNED` | `STRUCTURE_CRYPTOGRAPHIC_TRUST_LOCAL_DEV_UNSIGNED_V1` | nothing: no signature over the snapshot, payloads or traces |
| `SIGNED_SNAPSHOT` | `STRUCTURE_CRYPTOGRAPHIC_TRUST_SIGNED_SNAPSHOT_V1` | a signature over the snapshot's identity, verified by every executing node against a trust anchor it holds |

`LOCAL_DEV_UNSIGNED` is the posture for local development and a single operator. It is explicitly
declared, not assumed, which is the important distinction. `SIGNED_SNAPSHOT` is the posture for a
composition executed where its snapshot could be replaced: across nodes, or anywhere the party
executing it is not the party that built it.

## §1a. Trust belongs to a composition, not to a surface

One governance surface serves compositions with different postures. A multi-node composition
executed from a signed snapshot and a local one built for development come from the same surface,
and neither may change what the other is permitted. So the surface declares every authorized mode,
and a build configuration selects one. The compiler materializes only the selected structure, and
the composition carries exactly one (`INVARIANT_CRYPTOGRAPHIC_TRUST_DECLARED_V1`).

## §2. What "Trust" Means in PGC

Cryptographic trust governs confidence in the integrity and provenance of execution
artifacts: the snapshot, the payload, the runtime process, and the transport channel.
It does not govern identity trust (`actor`) or authority delegation (`authority`).

| Concern | Governed By |
|---------|-------------|
| Snapshot integrity | `cryptographic_trust` |
| Payload confidentiality | `cryptographic_trust` |
| Runtime process attestation | `cryptographic_trust` |
| Transport channel security | `cryptographic_trust` |
| Identity legality | `actor` |
| Authority delegation | `authority` |

## §3. Compiler Behavior

The compiler MUST:
- Read the trust mode the build configuration names in `trust_mode`, and refuse a build naming none
- Resolve it to exactly one structure declaring that mode, and refuse a mode no structure declares
- Materialize that structure alone, so the composition carries exactly one trust structure

The composition's trust mode is the `trust_mode` of the structure it carries. A reader holding the
snapshot reads the posture off the snapshot.

## §4. Runtime Behavior

The runtime MUST NOT branch on the trust mode. It reads no mode to decide what to do.

Verification is a condition a node takes on. A node that holds a trust anchor verifies the
snapshot's signature against it before executing anything, and refuses a snapshot whose signature
does not verify or that carries none. A composition declaring `SIGNED_SNAPSHOT` is one that is
deployed only to nodes holding an anchor; that deployment is a process obligation, as the
confinement of `LOCAL_DEV_UNSIGNED` to local substrates is.

The runtime performs no decryption and no attestation. No authorized mode requires them.

## §5. Future Expansion Path

```
LOCAL_DEV_UNSIGNED         ← authorized
  → SIGNED_SNAPSHOT        ← authorized (snapshot carries a verifiable signature)
  → SEALED_PAYLOAD         (payload encrypted; signing required)
  → ATTESTED_RUNTIME       (runtime process attested; sealing required)
  → ENCRYPTED_TUNNEL       (transport encrypted; attestation required)
```

Each further step is authorized by amendment, with a structure declaring it. A mode no structure
declares resolves to nothing when a build names it, and the build is refused.

## §6. Versioning

Changes to trust semantics require a new constitution version and migration rationale.

## §7. What became of V0

**V0 was deleted, not superseded**, as the placement constitution's V0 was. Its invariant and its
one structure are gone from this surface, replaced by V1 counterparts. A superseded structure would
stay in the composition beside its successor, two structures declaring one mode, and a superseded
invariant would go on requiring the `status: active` that V1 structures do not carry. The V0
declarations are carried by the compositions built under them and by this repository's history.

**What V1 changes.** V0 authorized one mode and marked its structure active, so the trust mode was a
property of the surface. A composition executed across nodes from a signed snapshot declared
`LOCAL_DEV_UNSIGNED`, because that was the only mode there was, and so contradicted its own
`UNSIGNED_SNAPSHOTS_LOCAL_ONLY` rule. V1 authorizes `SIGNED_SNAPSHOT` beside it and moves selection
to the build configuration. `LOCAL_DEV_UNSIGNED` means what it meant before.

**What V1 does not change.** The runtime still does not branch on the mode, and verification is
still what an anchored node does. The difference is that a signed composition now says it is one.

---

## What this realizes
```yaml
core:
  description: 'Declares the cryptographic trust regime active for a compiled snapshot.

    Governs whether snapshots must be signed, payloads sealed, runtimes attested,

    and transport encrypted. Trust mode is a compile-time declaration — runtimes

    execute under the declared trust posture rather than negotiating it.


    V1 authorizes LOCAL_DEV_UNSIGNED and SIGNED_SNAPSHOT, and a build configuration

    selects one for the composition it builds.

    '
  summary: Governs snapshot signing, payload sealing, runtime attestation, encrypted transport, and trust
    admissibility
rules:
- rule_id: TRUST_MODE_MUST_BE_DECLARED
  constraint: 'Every composition MUST carry exactly one trust structure, the one its build configuration
    selects. A composition with no trust declaration is a compiler validation failure.

    '
- rule_id: TRUST_MODES_ARE_ADDITIVE
  constraint: 'Trust modes are cumulative. SIGNED_SNAPSHOT requires signing but not payload encryption.
    SEALED_PAYLOAD requires both signing and payload encryption. ATTESTED_RUNTIME additionally requires
    runtime attestation. Each mode is a superset of the previous.

    '
- rule_id: UNSIGNED_SNAPSHOTS_LOCAL_ONLY
  constraint: 'Snapshots compiled with LOCAL_DEV_UNSIGNED trust mode MUST NOT be deployed to non-local
    execution substrates. This is enforced by governance process; future compiler validation may
    assert this mechanically.

    '
- rule_id: TRUST_IS_NOT_TRANSPORT
  constraint: '`cryptographic_trust` governs cryptographic trust posture only. It MUST NOT govern transport
    protocols, network routing, or TLS configuration. Transport security is an infrastructure concern;
    trust posture is a governance concern.

    '
- rule_id: RUNTIME_READS_TRUST_PASSIVELY
  constraint: 'Runtime MAY read the active trust contract for trace metadata emission. Runtime MUST NOT
    branch on trust mode. A node holding a trust anchor verifies the snapshot signature against it; that
    is a condition of the node, not a decision on the mode. Payload decryption and attestation are absent.

    '
```
