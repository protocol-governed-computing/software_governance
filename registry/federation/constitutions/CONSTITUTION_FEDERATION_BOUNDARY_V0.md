# CONSTITUTION_FEDERATION_BOUNDARY_V0

## Machine
```yaml
fqdn: federation::CONSTITUTION_FEDERATION_BOUNDARY_V0
artifact_kind: CONSTITUTION
version: V0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: federation
core:
  enforcement_model: process_enforced
rules:
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: governance_artifact
  enforced_by: PROCESS_ENFORCED
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
- applies_to: federation_boundary
  enforced_by: PROCESS_ENFORCED
```

---

**Header Block (Documentation)**
- **Constitution ID:** CONSTITUTION_FEDERATION_BOUNDARY_V0
- **Applies To:** Every federation boundary in a PGC composition
- **Dependencies:** CONSTITUTION_GOVERNANCE_V0

---

## Foundational Doctrine

**A federation boundary represents a governance authority, never a concern.**

A federation boundary declares that a distinct governance authority exists, one with jurisdiction over
a named set of protocol semantics. The boundary is not a folder, a package, a deployment unit, a
repository or a topic. It is a declaration of authority.

An artifact states both facts separately. `authority:` names who governs it. `concern:` and the
namespace of its FQDN classify what it is about. A concern may be organized, indexed and governed
without constituting a boundary. One authority may govern many concerns.

**The anti-sprawl rule:** a federation boundary exists only when a distinct governance authority
exists.

---

## §1. Sovereignty Model

### 1.1 Root and Delegated Authority

A composition has exactly one root authority. Every other authority is delegated from it.

| Level | Authority | Description |
|-------|-----------|-------------|
| Root | `pgc.platform` | Governs the platform and every composition built on it. One only. |
| Delegated | any other declared authority | Derives from the root and governs only within its declared jurisdiction. |

A second root authority is a constitutional violation.

### 1.2 Delegated Authority Limits

A delegated authority:
- MAY declare constitutions, invariants and assertions within its jurisdiction
- MAY reference artifacts governed by another authority, by declared reference
- MAY NOT override or supersede a rule of the root authority
- MAY NOT claim authority over artifacts another authority governs without explicit delegation

### 1.3 Authority Independence

The authority that constitutes and exercises a boundary MUST be distinguishable from the authority
whose jurisdiction the boundary claims. An authority governing its own constituting artifacts is
exercising self-governance. That is a concern of that authority, not a second boundary.

---

## §2. Boundary Existence Rule

### 2.1 When A Boundary May Be Created

A federation boundary MUST NOT be created speculatively. It MUST NOT be created:
- In anticipation of future governance rules
- To scaffold empty structure
- To mirror a repository, package, or deployment unit
- To signal intent without substance

A boundary is created when and only when:

> The first governance artifact (constitution, invariant, or assertion) declaring that authority is
> authored.

The governance law creates the boundary. The boundary does not precede the law.

### 2.2 What A Boundary Must Answer

A boundary answers these questions from declared artifacts alone:
1. Who the authority is
2. What constituting act created it
3. What subjects fall within its jurisdiction
4. What governance decision it may make that no other authority may
5. How it relates to the authorities above and beside it

A purported boundary that cannot answer them has not shown a distinct governance authority, and it
MUST NOT be admitted.

---

## §3. Boundaries and Concerns

Federation boundaries are **open-ended**. No list of permitted boundaries is defined: the condition
under which a boundary may exist is defined, and the number follows from the semantics.

| Structure | Membership |
|-----------|------------|
| Federation boundaries | Open-ended — one per distinct governance authority |
| Concerns and namespaces | Open-ended — one per subject an artifact is classified by |
| Functional layers | Closed — defined in STRUCTURE_DISCOVERY_V0 |

A concern classification alone is never grounds for a boundary.

---

## §4. Governance Locality Doctrine

### 4.1 The Central/Local Rule

| Governance Type | Correct Location |
|-----------------|-----------------|
| Universal platform governance law | the governance surface |
| Reusable cross-domain governance | the governance surface |
| Domain-specific governance law | domain repository |
| Domain orchestration policy | domain repository |
| Domain execution rules | domain repository |

The test for central placement is strict: **a governance artifact belongs in the governance surface if
and only if it governs every PGC composition universally.**

If a governance rule exists because blockchain needs it, or AI governance needs it, or any specific
domain needs it — it belongs in that domain's repository.

Locality is placement, not authority. A domain repository's artifacts are governed by the authority
they declare, wherever they sit.

### 4.2 Domain Governance Capability

Domain repositories are governance-capable. A domain repository MAY contain:
- Local constitutions (domain semantic law)
- Local invariants (domain-specific constraints)
- Local assertions (domain build-time checks)

Domain governance artifacts are introduced when the first domain-specific governance law exists — not
before.

### 4.3 Domain Governance Escalation

A governance rule that begins domain-local MAY be escalated to central governance if it is determined
to apply universally. Escalation requires:
1. Evidence that the rule governs every PGC composition, not just one domain
2. Removal from the domain repository
3. Introduction into the governance surface, under the namespace of the concern it governs

Escalation is explicit and versioned. It is not automatic.

---

## §5. Cross-Boundary Reference Legality

### 5.1 What Is Permitted

A governance artifact under one authority MAY reference an artifact under another when:
- The reference is to a universally applicable governance law
- The reference direction is delegated → root (not root → delegated)
- The reference is declared explicitly in the artifact's `governed_by` or dependency fields

### 5.2 What Is Prohibited

- Circular cross-boundary governance references
- Implicit authority inheritance across boundaries
- A delegated authority overriding a rule of the root authority
- Ambient governance (rules that apply across boundaries without explicit declaration)

---

## §6. Anti-Sprawl Doctrine

Federation boundaries MUST NOT proliferate to mirror:

- **Organizational structure** — teams, squads, or product groups do not constitute governance authorities
- **Repository topology** — a separate repository does not entitle a domain to a separate boundary
- **Deployment units** — service boundaries, microservices, or infrastructure boundaries are not governance boundaries
- **Runtime packaging** — how code is packaged or deployed is irrelevant to governance placement
- **Concerns** — a subject several artifacts share is a classification, not a jurisdiction
- **Implementation convenience** — grouping artifacts for discoverability or tooling reasons is not a governance justification

The question to ask before creating a boundary is:

> **Does a distinct governance authority exist here — one with jurisdiction over a named set of
> protocol semantics that no existing authority holds?**

If the answer is no, the boundary MUST NOT be created.

---

## §7. Boundary Evolution Doctrine

### 7.1 Boundaries Are Stable Once Created

A federation boundary that has been created with governance content is stable. Its governance
artifacts are immutable (new versions for changes). The boundary itself persists.

### 7.2 Artifacts Are Not Reorganized Freely

Moving a governance artifact to another namespace changes its FQDN, which artifacts across the system
reference. Such a move is a new identity that supersedes the old one, and every reference to the old
identity is accounted for. Invest in correct placement at authoring time.

### 7.3 Future Boundaries Are Anticipated But Not Pre-Created

A new authority may emerge as compositions grow — for example, a party governing a domain under its
own jurisdiction. Such a boundary MUST NOT be pre-created. It comes into existence when governance law
declaring that authority is authored.

---

## §8. Current Boundaries

Every artifact in the composition declares `authority: pgc.platform`. The composition therefore has one
federation boundary: the root authority. It governs every concern and namespace in the composition,
the platform's and each domain's.

The namespaces (`execution`, `capability_transforms`, `lifecycle`, `blockchain`, `ai_governance` and
the rest) are concerns. They organize the registry, and none is a boundary.

---

## §9. Closing Principle

Federation boundaries are not discovered by looking at the filesystem.
They are not inferred from repository structure or from namespaces.
They are not assigned by organizational mandate.

They emerge when governance authority emerges.

Governance authority justifies boundaries.
Boundaries do not justify governance authority.

---

## End of Constitution

---

## What this realizes
```yaml
doctrine: 'A federation boundary represents a governance authority, never a concern. A boundary exists
  only when a distinct governance authority exists.

  '
core:
  description: 'Governs the existence, semantics, and placement rules of federation boundaries. Defines
    root and delegated authority, governance locality doctrine, cross-boundary legality, and the anti-sprawl
    rule that prevents boundary proliferation.

    '
rules:
- rule_id: BOUNDARY_SEMANTIC_SOVEREIGNTY
  constraint: 'A federation boundary MUST correspond to a distinct, named governance authority. A boundary
    MUST NOT be introduced to represent a concern, a packaging unit, a deployment boundary, a runtime unit,
    or a repository boundary. The existence of a boundary is justified only by the existence of governance
    authority, not by implementation convenience.

    '
- rule_id: BOUNDARY_EXISTS_WHEN_AUTHORITY_EXISTS
  constraint: 'A federation boundary MUST NOT be created unless at least one governance artifact (constitution,
    invariant, or assertion) declares its authority. Empty or placeholder boundaries are constitutional
    violations. The first governance law triggers boundary creation; boundary creation does not precede
    governance law.

    '
- rule_id: BOUNDARY_SOVEREIGNTY_LEVELS
  constraint: 'Exactly one root authority exists: pgc.platform. Every other authority is delegated from
    it and MUST NOT exceed that delegation. The authority that constitutes a boundary MUST be distinguishable
    from the authority whose jurisdiction it claims. A second root authority is a constitutional violation.

    '
- rule_id: BOUNDARY_OPEN_ENDED
  constraint: 'Federation boundaries are open-ended. New boundaries MAY be introduced as distinct governance
    authorities emerge. No list of permitted boundaries is defined. A concern classification alone is
    never grounds for a boundary.

    '
- rule_id: BOUNDARY_GOVERNANCE_LOCALITY
  constraint: 'A governance artifact belongs in the governance surface (central) if and only if it governs
    every PGC composition universally. A governance artifact belongs in a domain repository (local) if it exists
    because of domain-specific semantics. Placing domain-specific governance centrally is a governance
    locality violation. Placing universal governance locally is also a violation.

    '
- rule_id: BOUNDARY_NO_CROSS_OWNERSHIP
  constraint: 'No authority MAY declare governance over artifacts another authority governs without explicit
    delegation. Cross-boundary references MUST be declared. Implicit authority inheritance and ambient
    cross-boundary governance are prohibited.

    '
- rule_id: BOUNDARY_ANTI_SPRAWL
  constraint: 'Boundaries MUST NOT be introduced to mirror: organizational structure, repository topology,
    deployment units, runtime packaging, concerns, or implementation convenience. The only valid justification
    for a new boundary is a new distinct governance authority that no existing authority holds.

    '
- rule_id: BOUNDARY_ADMISSION_REQUIRED
  constraint: 'A new boundary is admitted only when declared artifacts answer: who the authority is; what
    constituting act created it; what subjects fall within its jurisdiction; what governance decision it
    may make that no other authority may; and how it relates to the authorities above and beside it. A
    purported boundary that cannot answer these MUST NOT be admitted.

    '
```
