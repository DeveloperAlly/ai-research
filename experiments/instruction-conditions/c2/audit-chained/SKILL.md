---
name: audit-chained
description: "Use only when the user invokes it: run a read-only audit of a repo, issue tracker, docs set or system state to evidence-backed dispositions the owner approves, by chaining the shared timing, access, claim, review and retro skills."
---

# Audit (chained)

An audit is an assessment, not a build. It ends in a report of dispositions the owner approves. This skill holds only the audit steps; the shared rules live in the skills it chains.

## 0. Load the chain

- Invoke `timed-execution` and `access-and-scope` now, and follow them for the whole run. Until the owner's gate the write boundary is: the report comment only. Invoke `verify-claims` and follow it for every verdict.
- Confirm each one loaded. If any fails to load, stop and tell the owner which one. Never improvise its rules.
- `independent-review` is invoked at step 6 and `skill-retro` at step 11.

## 1. Freeze the questions

Number the owner's audit questions verbatim. Each question becomes one report section.

## 2. Define and count the population

- For each question, name the population it covers (open issues, Markdown files, branches, services).
- Count it from the source with a command, and record the command, its output and the time.
- The report must account for every item exactly once.

## 3. Fix the disposition list before reading

- Define the allowed verdicts up front (for example: keep, close completed, close superseded, close not planned, merge into #N; canonical, outdated, redundant, orphan).
- Every item gets one verdict, a one-line reason and an evidence link.

## 4. Read every item in full

- Split the population across background agents in batches that fit one chunk; each writes its table to a file in the run's own workspace.
- Read bodies and comments, whole files and full command output. A verdict from a title or filename alone is a defect.

## 5. Check claims against live state

Where a doc or issue says something is deployed, done or running, check it read-only against the live system. If the system is out of scope, the claim stays UNVERIFIED and is listed as needing access.

## 6. Review

Invoke `independent-review` on the verdicts, with steps 2 to 5 as the checklist and the default sampling rule (at least 10% and at least 10 items, plus every destructive recommendation).

## 7. Reconcile

- Item counts per section equal the population counts from step 2. No duplicates, no gaps.
- Every unmet requirement found has a named owning issue, existing or proposed.

## 8. Report and gate

- One section per question, as tables. Every destructive action is a checkbox the owner can approve individually.
- Decisions that need the owner are listed separately, each with a recommendation and its trade-off. Improvement ideas are kept separate from findings.
- Stop. Nothing changes until the owner approves specific items.

## 9. Execute approved items only (when asked)

- Prefer reversible actions: close rather than delete, move rather than rewrite, and link the replacement in a comment.
- Record before and after counts, and run the repo's full check suite.
- Add a guard so the cleaned state does not rot (for example a check that fails on orphaned docs or unlabelled issues).

## 10. Close out

Completion comment on the tracking issue: each question with its answer and evidence, what was executed, what remains.

## 11. Retro

Invoke `skill-retro`, adding the audit signals: population size per question and items missed or duplicated before step 7 caught them; reviewer disagreement rate and how many went against the original verdict; every owner override at the gate with its reason; verdicts later found wrong; UNVERIFIED facts left and why.
