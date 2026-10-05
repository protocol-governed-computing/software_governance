# Business Problem Statement

**Project Name:** platform — routing is a lookup

## 1. Context

A contract is built from steps. Each step runs one capability and, for each outcome it can produce,
says what happens next: go on to the next step, or end the contract with that outcome. The rule that
governs how contracts are built says routing is exactly that, a finite table from outcome to one of
two answers, and never a condition or an expression.

The rule that a contract's outcomes are all reachable says otherwise. It admits a third answer: an
evaluation target, a named condition over the step's result that ends the contract with one outcome
when it holds and another when it does not. The compiler follows the invariant, so a contract may be
built that routes to a condition.

Nothing runs a condition. Execution reads any answer it does not know as "go on", so a contract that
routes to one ends with the outcome of its last step, whatever the condition would have said. Two
contracts the platform holds route to a condition today:

- The licence cap contract routes the count of licences assigned to "is the count below the cap".
  Nothing runs it: the contract is named by no workflow, and the cap is enforced by the eligibility
  check instead.
- The Collatz gate cannot fail. Checking termination routes to "did every sequence terminate"; the
  contract succeeds even when one did not.

---

## 2. Problem Statement

**The platform's two rules disagree about what routing may say, and the one the compiler follows
admits an answer nothing performs, so a contract succeeds where its declaration says it fails.**

This change shall:

- make the rule that a contract's outcomes are all reachable agree that routing has two answers;
- refuse, when a composition is built, routing to anything but going on or ending;
- refuse, when a contract runs, a routing answer it does not know, rather than go on.

### What the business already decided

These are settled and are not reopened by this change:

- **Routing is a lookup.** It maps each outcome a step can produce to going on or ending, and nothing
  else. A decision is made by a capability, which answers with an outcome.
- **A continuation the contract does not declare is refused, never assumed.**
- **A change of meaning is a new identity.** The invariant is replaced by a new version, and the old
  one stays in the record and out of reach.

---

## 3. Clarifications answered by the business author

- **Are the two contracts changed here?** No. Each is replaced by a change in its own domain, where a
  capability makes the decision the condition stated.
- **Is execution given a way to run conditions?** No. That would put an expression into routing,
  which the governing rule forbids.

---

## Amended before build

The first version of this statement said the licence cap is never enforced, and Stage 2 said both
contracts run on live routes. Both were counted from the compiled routing answers without asking
whether anything runs the contract. It does not: `ai_governance::CC_ENFORCE_LICENSE_CAP_V0` is named
by no artifact, and the cap is enforced by `ai_governance::CC_VALIDATE_ELIGIBILITY_V0`, whose quota
check refuses at the cap. The business deleted the unreachable contract by hand, so the composition
holds one contract routing to a condition, the Collatz gate, which its own change replaced. Where a
later stage says the licence cap contract is replaced by its own change, it was deleted instead.
