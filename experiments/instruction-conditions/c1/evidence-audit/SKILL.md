---
name: "evidence-audit"
description: "Use only when the user invokes it: a read-only audit of a repo, issue tracker, docs set or system state that ends in evidence-backed dispositions the owner approves before any cleanup."
---

# Evidence audit

An audit is an assessment, not a build. It ends in a report of dispositions the owner approves. Done means every item in scope has exactly one verdict backed by evidence, and the counts reconcile with the source. Builds and changes use `proof-driven-delivery` instead.

## Execution cadence: chunked, on a clock
This applies to every step below.
- Before starting work, publish the chunk list: every chunk is 5 minutes or less, with its visible output, pass criteria, maximum tool calls and fallback. Do the riskiest chunk first.
- Start the clock from a real time source (a time tool, or `date` on the host), never from memory. State the total time budget if the owner set one.
- Every status message opens with a timer line computed from the real clock at that moment: `[T+mm:ss | chunk n/N: name | budget left mm:ss]`.
- Each chunk ends with its output posted and marked PASS or FAILED. A chunk without its named output is FAILED, never "in progress". Durable outputs also go to the tracking issue.
- If a chunk hits its time or call limit: stop, report the exact state and blocker, and propose the next move. Never extend silently.
- When background agents run, each status message includes every agent's state: running, done or blocked; its last output; its elapsed time.
- Times in the final report are copied from recorded clock readings.

## 1. Freeze the questions
- Number the owner's audit questions, verbatim. Each question becomes one report section.
- Apply corrections immediately and restate the list.
- If the questions, scope and plan are already written and the owner has answered them, restate them once and proceed. Do not ask for the same confirmation again.

## 2. Define and count the population
- For each question, name the population it covers (open issues, Markdown files, branches, services...).
- Count it from the source with a command (for example `gh issue list --state open --limit 1000 --json number --jq length`, `git ls-files '*.md' | wc -l`). Record the command, its output and the time.
- The report must account for every item exactly once.

## 3. Prove access and declare the write boundary
- Run one read-only probe on every system in scope.
- Before claiming a skill, tool or file is missing, check the session's own skill and tool lists and search for it. Say where you looked.
- Every destination this run will write to (the tracking issue, a report or evidence file, any log) is named by exact URL or path and confirmed to exist now. A missing destination is flagged to the owner; never guess or invent one.
- Read-only means no state change anywhere: no `git fetch`, `pull`, `checkout` or `prune` (use `git ls-remote` or the GitHub API), and no scratch files on the systems being audited (use your own workspace).
- The owner's latest explicit scope overrides any written plan. If they conflict, flag the conflict and ask; never resolve it silently.
- Until the owner's gate, the only write allowed is the report itself. No closes, labels, moves, deletes or commits.

## 4. Fix the disposition list before reading
- Define the allowed verdicts up front (for example: keep, close completed, close superseded, close not planned, merge into #N; canonical, outdated, redundant, orphan).
- Every item gets one verdict from the list, a one-line reason and an evidence link.

## 5. Read every item in full
- Split the population across background agents in batches sized to fit one 5-minute chunk; each agent writes its table to a file in your own workspace.
- Read bodies and comments, whole files, full command output. A verdict from a title or filename alone is a defect.
- Label each supporting fact VERIFIED-LIVE, VERIFIED-CODE, VERIFIED-DOC or UNVERIFIED. An UNVERIFIED fact cannot support a close, delete or merge.

## 6. Check claims against live state
- Where a doc or issue says something is deployed, done or running, check it read-only against the live system and record the output. If the live system is out of scope, mark the claim UNVERIFIED and list it as needing access.
- Where two sources disagree, record both and which one the evidence supports.

## 7. Independent review
- A fresh reviewer that did not do the audit re-checks a random sample (at least 10% and at least 10 items) and every destructive recommendation.
- Each disagreement is resolved with evidence, and the resolution is shown in the report.

## 8. Reconcile
- Item counts per section equal the population counts from step 2. No duplicates, no gaps.
- Every unmet requirement found has a named owning issue (existing, or proposed).

## 9. Report
- One section per question, as tables.
- Every destructive action is a checkbox the owner can approve individually.
- Decisions that need the owner are listed separately, each with a recommendation and its trade-off.
- Improvement ideas ("above and beyond") are kept separate from findings.

## 10. Gate
- Stop. Nothing changes until the owner approves specific items.

## 11. Execute approved items only (when asked)
- Prefer reversible actions: close rather than delete, move rather than rewrite, and link the replacement in a comment.
- Record before and after counts, and run the repo's full check suite, not a subset.
- Add a guard so the cleaned state does not rot (for example a check that fails on orphaned docs or unlabeled issues).

## 12. Close out
- Completion comment on the tracking issue: each question with its answer and evidence, what was executed, what remains, and the chunk timeline (planned vs actual per chunk, from the recorded clock).

## 13. Learn from the run and suggest improvements to this skill
After close-out, review the run against this skill and propose how to improve it. Failures and lessons go in the completion comment on the tracking issue, which step 3 confirmed exists; do not write them anywhere else unless the owner names an existing destination.

**Record the audit's quality signals** in the completion comment, so runs can be compared:
- population size per question, and how many items were missed or duplicated before step 8 caught them;
- reviewer disagreement rate (disagreements / items re-checked) and how many were resolved against the original verdict;
- owner overrides at the gate: every verdict the owner rejected or changed, with the owner's reason. These are the strongest signal - an overturned verdict means the evidence or the disposition rules were wrong;
- verdicts that turned out wrong during execution (for example an issue closed as done that was later reopened);
- UNVERIFIED facts that remained, and why they could not be verified;
- chunks that ran over their time or call limit, and why.

**Then turn the signals into proposed edits:**
- For each gap, error, override or correction, cite its evidence (time, output, quote) and name the step that should have prevented it. Classify it:
  - **missing** - no step covers it;
  - **unclear** - a step covers it but was easy to misread;
  - **not followed** - the step was clear and was skipped. Propose making it checkable (a command, a count, a required field), not repeating it more loudly.
- Propose exact edits: the step number and the text to add or change, each tied to an observed incident. No speculative additions. A recurring owner override usually means the disposition list or its definitions in step 4 need changing.
- Deliver the proposal as a "Skill improvements" section in the completion comment, plus a diff to the skill file on the delivery branch when the skill lives in the repo. Do not merge it without the owner's approval.
- If nothing went wrong, say so and cite the evidence (zero misses, zero overrides, the disagreement rate, chunks on time).