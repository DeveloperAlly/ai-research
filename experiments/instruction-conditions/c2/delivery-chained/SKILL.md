---
name: delivery-chained
description: "Use only when the user invokes it: deliver engineering work (APIs, infra, integrations, builds after failed attempts) to proven, working software by chaining the shared timing, access, claim, review and retro skills."
---

# Delivery (chained)

Delivers against owner requirements until every requirement has a proof. This skill holds only the delivery steps; the shared rules live in the skills it chains.

## 0. Load the chain

- Invoke `timed-execution` and `access-and-scope` now, and follow them for the whole run. Invoke `verify-claims` and follow it for every statement in the run.
- Confirm each one loaded (the skill call succeeded and its instructions are in context). If any fails to load, stop and tell the owner which one. Never improvise its rules.
- `independent-review` is invoked at step 6 and `skill-retro` at step 12.

## 1. Read the whole record and the existing system

- Read the owning issue, every linked issue and comment, the README, and the architecture and decision docs.
- Treat each past failure as a constraint on the design.
- List the existing primitives and rules for auth, networking, storage, deployment and security.

## 2. Freeze requirements

- Number the owner's requirements verbatim, each with its source.
- Add the non-functional requirements: availability and what it covers, cost and quota caps, security and auth model, composability, where the code lives, what must not be touched.
- Resolve ambiguity, restate the full list after every correction, and get the owner to confirm it is complete. Never drop, defer or scope down a requirement without the owner.

## 3. Frame

Answer with sources: what must keep working when each machine or service is down; where the trust boundaries are and who holds each credential; the hard constraints; the minimum set of components on the availability path.

## 4. Count budgets

Every metered resource (writes per day, storage, request size, cron slots, part sizes) gets a number from the provider's docs.

## 5. Design

- Work backwards from an acceptance test for each deliverable.
- Trace one real request end to end: every hop, component and file, and whether it changes.
- Compare at least two alternatives and reject each by naming the requirement it fails.
- Prefer the least change to existing systems: outbound-only connections, no sudo, no changes to excluded components. If elevated privileges are unavoidable, argue why.
- Composability test: write the steps to add a second, different unit. If they touch shared core code, the design is not composable.
- Security check: shared hostnames share cookies; duplicate auth systems; keys held in the browser; credentials on hosts that do not need them; the system's own written rules.

## 6. Review

Invoke `independent-review` on the design, with steps 1 to 5 as the checklist.

## 7. Plan

- Every component has an owner, credential, run-as user, proof tool and exit proof. No TBD.
- Every change to a live system others depend on has a written rollback: the exact steps and the proof that the previous behaviour is back.
- The plan is the chunk list, opening with a preflight chunk that proves the whole path. Present it for approval; any later change is written and approved before it runs.

## 8. Execute, thinnest path first

- The owner's approval authorises the plan's chunks in order; each named gate and any plan change needs its own "go".
- Before the first change to a live system, run its rollback once and record the proof. A change whose rollback is unproven does not ship.
- Get one real request through the whole system on the owner's actual surface before hardening anything, then add each requirement's mechanism one at a time.
- Sub-agents only after a check proves they can reach what they need; run them in the background with a time limit. Write long output to files so it is not lost.

## 9. Prove each requirement

- Each requirement gets raw output and a host-clock time: real reboot, real outage, real client.
- Auth, permission and access requirements also get a refusal case: unknown identity, wrong user, revoked credential.
- Existing callers of any system the run changes get a regression run before and after each change. A regression is fixed or rolled back immediately.
- Post raw proof to the tracking issue after every chunk and record proofs in a dated evidence file. A requirement without a proof is reported as not met.

## 10. Keep deployed equal to the repo

After each deploy, hash the deployed artifact and the repo file. A mismatch is a defect to fix immediately.

## 11. Close out

- Commit, push, open or update the PR. Run the repo's full check suite first, not a subset.
- Completion comment on the tracking issue: each requirement with its proof, what is still open and why, and recommendations found while building.

## 12. Retro

Invoke `skill-retro`. Include the chain check: which chained skills loaded and were followed.
