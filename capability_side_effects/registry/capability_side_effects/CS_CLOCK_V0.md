# CS_CLOCK_V0

## Human

### 1. Intent

Answers the time now.

A record that states when something happened is evidence; one that states when something was
*claimed* to have happened is a claim about a claim. The difference is who determines the value. A
caller supplying a time can supply any time, including the same time twice, and a trail whose times
do not advance is not a trail. So the time is determined where the occurrence is recorded, not
where it is requested.

### 2. Why this is a side effect and not a transform

A capability transform is pure by declaration: the same inputs give the same outputs, no I/O, no
hidden state. A clock is the opposite of all three — it takes no inputs, gives a different answer
every time it is asked, and reads something outside the composition. No transform can supply a
time however it is written, which is why domains that needed one had to accept it from their
caller and hope.

### 3. What it does not do

It does not format, parse, compare or advance a time, and it holds none. Those are pure operations
on a value, and a value it has already answered is an ordinary input to an ordinary transform.

---

## Machine

```yaml
fqdn: capability_side_effects::CS_CLOCK_V0
artifact_kind: CAPABILITY_SIDE_EFFECT
version: v0
governed_by: capability_side_effects::CONSTITUTION_CAPABILITY_SIDE_EFFECTS_V0
authority: pgc.platform
concern: capability_side_effects
core:
  summary: Answers the current instant, so a record states when something happened rather than when it was claimed to
  category: external
  policy:
    operations:
    - NOW
  operations:
    NOW:
      summary: The current instant, as an ISO-8601 timestamp in UTC
      handler: now
      effect: read
      input: []
      output:
      - result_status
      - timestamp
      idempotent: false
      result_status_values:
      - SUCCESS
      - BACKEND_ERROR
  configuration:
    precision:
      type: string
      required: false
      description: Resolution of the answer — `seconds` or `milliseconds`; defaults to seconds
  failure_modes:
  - 'BACKEND_ERROR: No clock is available to the runtime'
  architecture:
    role: Neutral temporal capability
    purpose: Determines a time at the moment of occurrence, so no caller may assert one
    bindings:
      timestamp: ISO-8601 instant in UTC, always advancing
  use_cases:
  - 'Audit trail: stamp an appended occurrence with when it occurred'
  - 'Lifecycle: record when a state transition was made, by the party that made it'
implementation:
  module: capability_side_effects.implementation.CS_CLOCK_V0.runtime
  callable: ClockRuntime
extensions:
  cs_kind: clock
  side_effect_type: ambient
  properties:
    durability: none
    idempotent: false
    replay_policy: never
    transactional: false
    concurrent_safe: always
```
