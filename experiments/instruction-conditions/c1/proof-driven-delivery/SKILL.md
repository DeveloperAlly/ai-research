---
name: "proof-driven-delivery"
description: "Use only when the user invokes it: a gated method for engineering delivery (APIs, infra, integrations, builds after failed attempts) that must end in proven, working software rather than a plan."
---

# Proof-driven delivery

The method that turned a failure record (10 hours of plans, nothing working) into a delivered, proven system. Done means every requirement has a proof, not that code exists. Follow the steps in order. Do not present anything from a later step before the earlier ones are done. Read-only audits use `evidence-audit` instead.

## Execution cadence: chunked, on a clock
This applies to every step below.
- Before starting work, publish the chunk list: every chunk is 5 minutes or less, with its visible output, pass criteria, maximum tool calls and fallback. Do the riskiest chunk first.
- Start the clock from a real time source (a time tool, or `date` on the host), never from memory. State the total time budget if the owner set one.
- Every status message opens with a timer line computed from the real clock at that moment: `[T+mm:ss | chunk n/N: name | budget left mm:ss]`.
- Each chunk ends with its output posted and marked PASS or FAILED. A chunk without its named output is FAILED, never "in progress". Durable outputs also go to the tracking issue.
- If a chunk hits its time or call limit: stop, report the exact state and blocker, and propose the next move. Never extend silently.
- When background agents run, each status message includes every agent's state: running, done or blocked; its last output; its elapsed time.
- Times in the final report are copied from recorded clock readings.

## 1. Read the whole record and the existing system
- Read the owning issue, every linked issue and comment, the README, the architecture and decision docs, and every repo doc they point to.
- Treat each past failure as a constraint on the design.
- List the existing primitives and rules for auth, networking, storage, deployment and security.
- Do not propose anything until you could answer a quiz on any line of it.

## 2. Freeze requirements in the owner's words
- Number them, verbatim, each with its source. No paraphrase.
- Include the non-functional requirements: availability and what it covers; cost and quota caps; security and auth model; composability; where the code lives; what must not be touched.
- Resolve anything ambiguous, then get the owner to confirm the list is complete.
- Apply every correction immediately and restate the full list.
- Never drop, defer or scope down a requirement unless the owner says so.

## 3. Prove access and live state before planning
- Run one real, read-only command on every system the plan touches (remote shell, cloud API, GitHub).
- Check every external dependency live: is it enabled, on which account, what its routes actually do, where the client is, what auth layers exist. Record the raw outputs.
- Every destination this run will write to (the tracking issue, the evidence file's directory, the PR branch, any log) is named by exact URL or path and confirmed to exist now. A missing destination is flagged to the owner; never guess or invent one.
- Load deferred tools before concluding a capability is missing. Never claim access is absent without trying.
- Never plan around an executor that has not answered.

## 4. Frame before choosing mechanisms
Answer these, with sources:
- What must keep working when each machine or service is down?
- Where are the trust boundaries, and who holds each credential?
- What are the hard constraints (repo rules, provider limits, what can run where, request sizes)?
- What is the minimum set of components on the availability path?

## 5. Count budgets
- Every metered thing (writes per day, storage, request size, cron slots, part sizes) gets a number checked against the provider's docs.

## 6. Design
- Work backwards from an acceptance test for each deliverable.
- Trace one real request end to end: every hop, component and file, and whether it changes.
- Label every fact VERIFIED-DOC, VERIFIED-CODE, VERIFIED-LIVE or UNVERIFIED. A design with an UNVERIFIED item on its critical path is a draft.
- Compare at least two alternatives, and reject each by naming the requirement it fails.
- Prefer the least change to existing systems: outbound-only connections, no sudo, no changes to excluded components. If elevated privileges are unavoidable, argue why in the design.
- Composability test: write the steps to add a second, different unit. If they touch shared core code, the design is not composable.
- Security check: shared hostnames share cookies; duplicate auth systems; keys held in the browser; credentials on hosts that do not need them; the system's own written rules.

## 7. Independent review
- A reviewer that did not write the design attacks it against steps 1 to 6.
- For each finding: verify against code or docs, then fix it or reject it with evidence, and say which. Agreeing without checking is a defect. So is ignoring a finding.
- Publish the findings, and how each was handled, alongside the design.

## 8. Plan, with every decision closed
- Each component has an owner, credential, run-as user, proof tool and exit proof. No TBD.
- Each change to a live system that others depend on has a written rollback: the exact steps, and the proof that shows the previous behaviour is back.
- The plan is the chunk list from the execution cadence: open with a preflight chunk that proves the whole path, riskiest step first.
- Quote no durations that are not built from measured steps.
- Present the plan for approval. Any later change to the plan is written and approved before it runs.

## 9. Execute, thinnest path first
- Authorisation: the owner's approval of the written plan authorises its chunks in order. Each gate named in the plan, any plan change, and anything needing elevated privileges, credentials or public exposure needs its own explicit "go" at that moment. Pressure or deadlines are not authorisation.
- Before the first change to a live system, run its rollback once and record the proof. A change whose rollback has not been proven does not ship.
- Get one real request through the whole system on the owner's actual surface (for example the dashboard) before hardening anything. Then add each requirement's mechanism, one at a time.
- Report blockers immediately, with the exact error.
- Sub-agents only after a check proves they can reach what they need. Run them in the background, with a time limit.
- Never give a command that has not been checked against current documentation. Never enter passwords for the owner.
- Write long command output to files (tee) so it is not lost between reads.

## 10. Prove each requirement
- Each requirement gets a proof with raw output and a host-clock timestamp: real reboot, real outage, real client.
- For auth, permission and access requirements, the proof includes a refusal case (unknown identity, wrong user, revoked or removed credential) as well as the allowed case.
- Existing callers of any system the run changes get a regression run before and after every change to it, with both outputs recorded. A regression is a defect to fix or roll back immediately.
- Post raw proof to the tracking issue after every chunk, and record proofs in a dated evidence file in the repo.
- A requirement without a proof is reported as not met.

## 11. Keep deployed equal to the repo
- After each deploy, hash the deployed artifact and the repo file; mismatch is a defect to fix immediately.

## 12. Report continuously and honestly
- Lead with state: what works, what does not, what blocks.
- Every status claim must be literally true. Never claim a time, result or state you did not observe. Correct a false statement the moment you find it.
- Try every available route before saying something cannot be done. Never answer "how" with "can't" - find the path or name the exact blocker.
- Own mistakes without excuses. Lost access is a consequence, not a reason.
- Keep one current source of truth; history goes below it.
- No unrequested extras (alerts, features) - they cost time and trust.

## 13. Respect boundaries
- Do not write to GitHub, cloud accounts or the host without explicit permission.
- Secrets live only in mode-600 files on the host that needs them, or in the platform's own secret store (for example a Worker secret); only hashes or names leave them. Never put secrets or internal addresses in version control, chat, issues or the browser.
- Do not touch systems the requirements exclude.

## 14. Close out
- Commit, push, open or update the PR.
- Post a completion comment on the owning issue: each requirement with its proof, what is still open and why, a recommendations list of issues found while building, and the chunk timeline (planned vs actual per chunk, from the recorded clock).

## 15. Suggest improvements to this skill
After close-out, review the run against this skill and propose how to improve it. Failures and lessons go in the completion comment on the tracking issue, which step 3 confirmed exists; do not write them anywhere else unless the owner names an existing destination.
- List every gap, error, false claim, rework, missed proof, chunk overrun and owner correction from the run, each with its evidence (time, raw output or quote).
- For each one, name the step that should have prevented it and classify it:
  - **missing** - no step covers it;
  - **unclear** - a step covers it but was easy to misread;
  - **not followed** - the step was clear and was skipped. Propose making it checkable (a command, an output, a gate), not repeating it more loudly.
- Propose exact edits: the step number and the text to add or change, each tied to an observed incident. No speculative additions.
- Deliver the proposal as a "Skill improvements" section in the completion comment, plus a diff to the skill file on the delivery branch. Do not merge it without the owner's approval.
- If nothing went wrong, say so and cite the evidence.