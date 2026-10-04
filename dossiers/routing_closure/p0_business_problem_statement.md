# Business Problem Statement

**Project Name:** platform — routing closure

## 1. Context

A contract is built from steps. Each step dispatches a capability, and the capability declares the
outcomes it can answer with. For each outcome, the step says what happens next: the contract carries
on, or it ends. A workflow runs contracts, and for each outcome a contract can end with, the
workflow says where it goes next.

The platform checks a step's answers against the outcomes the step's author listed, not against the
outcomes the capability declares. So an author can leave an outcome out, and the check passes. When
that outcome arrives, the platform carries the contract on as if the step had succeeded. And the
platform's record of a step names what it produced, never the outcome it ended with or what the
contract did next.

A study of the published composition found both. Fourteen steps in three domains listed fewer
outcomes than their capability declares, and eleven workflow places had no route for an outcome
their contract could end with. In one case a lookup failed, the contract carried on, and a person
was accepted. The record showed nothing wrong.

The open standard now requires the closure, in `v1` Changes 3 and 4. The three domains closed their
own gaps in their own changes. This change makes the platform hold every domain to it.

---

## 2. Problem Statement

**The platform lets a step leave an outcome unanswered, carries execution on past it, and records
nothing of the decision.**

This change shall:

- refuse, when a composition is built, a step that answers fewer outcomes than its capability
  declares;
- refuse, when a composition is built, a workflow place execution can reach that leaves an outcome
  of its contract without a route;
- refuse, when a request runs, a step outcome for which nothing says what happens next, and run
  nothing after it;
- record, for every step that runs, the outcome it ended with and what happened next.

### What the business already decided

These are settled and are not reopened by this change:

- **A missing answer is never a default.** An outcome nothing answers refuses.
- **A refusal at build time comes first, and a refusal at run time stays as the safeguard** for
  anything the build did not reach.
- **A superseded workflow is evidence, not behaviour.** It cannot be run and stays in the record.
  It is not checked, because nothing can reach it.

---

## 3. Clarifications answered by the business author

- **Does a step have to answer an outcome its capability declares but never produces in practice?**
  Yes. What the capability declares is what the step answers for. Whether it occurs is not the
  step's to decide.
- **What does the record say for an admission check?** Its outcome, and that the workflow's route
  decides what happens next. The route is already recorded.
