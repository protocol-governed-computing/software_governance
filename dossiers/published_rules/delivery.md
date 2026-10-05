# Delivery — published_rules

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `06dbbb2227ad…`
**Delivered:** two published rules mean again what v5 published, and their widened forms have their
own identities. `execution_topology::INVARIANT_TOPOLOGY_ROUTING_COMPLETE_V1` states CP-13 and is
enforced by today's check. `trace::CONSTITUTION_TRACE_EXECUTION_V1` names `SCHEMA_TRACE_EVENT_V2`. Both
V0s carry their v5 text and are stood down.
**Validated:** both V0s differ from v5 only by `superseded_by`; `assert_topology_routing_complete_v0`
is identical to v5; a workload copy with a narrowed step surface refused by the V1 check;
`test_routing_closure` 12/12; full regression `--all` 68/68 as expected

---

## What this change closed

- **The routing rule.** v5 required a step to route every outcome it lists. During dev/18 it came to
  require the list to hold every outcome the capability declares, and its check gained that
  comparison, under the published identity. A composition v5 admitted could be refused by the rule v5
  named. The widened rule is now V1, and V0 says and checks what v5 published.
- **The record rule.** v5 required every trace line to conform to `SCHEMA_TRACE_EVENT_V1`. It came to
  name V2. It is now V1 naming V2, and V0 names V1 as published.

Nothing a composition does changed: the checks that run and the traces written are those of before.

---

## What it took

**Everything was written by hand.** The design language has no family for a constitution or an
invariant. Both successors were authored by hand, and both V0s restored from the `v5` tags with their
stand-down added.

**The check moved with its rule.** A check is bound to its invariant by identity, so today's check
became `assert_topology_routing_complete_v1`, and the v0 module was restored from the `v5` tag. Both
stay registered; a stood-down invariant derives no assertion, so v0 runs nowhere.

**Only unpublished artifacts were edited in place.** `CONSTITUTION_EXECUTION_TOPOLOGY_V1` names the
routing rule's successor, and `INVARIANT_WF_ROUTING_CLOSED_V0` mentions it; both were added this
cycle.

**The code it touched:**

- `protocol_compiler`: `assert_topology_routing_complete_v1.py` (new), registered;
  `assert_topology_routing_complete_v0.py` restored to v5; the scope entry in
  `author_invariant_scope.py`; `test_routing_closure.py` imports V1.
- `.github/process`: `trace_schema_conformance.py`'s docstring; 513 artifacts, 15 supersession
  relations.

---

## What is carried

- **The other published breaches belong to their domains.** Blockchain (8), ai_governance (1) and
  transformation (9), per `.github/process/notes/su11-recut-sweep.md`.
- **Prose elsewhere mentions the stood-down record rule.** `CONSTITUTION_EXECUTION_V0` and
  `CONSTITUTION_CONSTRUCTION_V0` name it in explanation; both are published, and explanation names
  nothing.
