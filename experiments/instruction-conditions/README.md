# Instruction conditions for issue #4

Material for [#4](https://github.com/DeveloperAlly/ai-research/issues/4): which way of instructing a fresh chat gets each type of task done right. Nothing here is a live skill. Conditions are kept out of `.claude/skills` on purpose: a session opened in this repo loads every skill in that folder, which would mix conditions.

## Conditions

| Condition | Contents | What differs |
|---|---|---|
| C0 | No skill named in the prompt | Baseline |
| C1 | `c1/`: byte copies of the owner's saved skills as of 2026-09-29 | One large skill per task type |
| C2 | `c2/`: five shared single-job skills plus two chaining skills | The same rules, packaged as small skills that chain |
| C3 | C2 plus `build-lifecycle` hook enforcement (code tasks only) | Enforced order |
| C4 | Task described without naming a skill, all skills installed | Skill selection |

C1 and C2 carry the same rules; only the packaging differs. `check_dry.py` confirms no rule appears in two C2 skills. The coverage check (every C1 rule present in exactly one C2 skill) was run when C2 was written.

### C1 snapshot (sha256 prefix)

| Skill | sha256 | Saved-skill timestamp |
|---|---|---|
| `proof-driven-delivery` | `adbb1280d956` | 2026-09-29 21:54 AEST |
| `evidence-audit` | `ee07c4b37a4a` | 2026-09-29 20:38 AEST |
| `idea-to-plan` | `f80550f4467b` | 2026-09-29 20:49 AEST (owner asked to delete this version; kept here only as the C1 baseline for T3) |

### C2 skills

| Skill | Job | Chained by |
|---|---|---|
| `timed-execution` | Chunk list, real clock, timer line, PASS/FAILED, overrun stop, agent states | both chaining skills |
| `access-and-scope` | Scope, read-only probes, destinations exist, write boundary, secrets | both |
| `verify-claims` | Evidence labels, spikes for unverified critical claims, honest statements | both |
| `independent-review` | Fresh reviewer, supplied checklist, dispositions | both |
| `skill-retro` | Learning step: signals, classification, proposed edits | both |
| `delivery-chained` | Delivery steps only | - |
| `audit-chained` | Audit steps only | - |

Not built yet: a C2 version of `idea-to-plan` (needs single-job document skills: decision, PRD, requirements, architecture, task graph).

## Running a condition

1. Start a fresh Claude Code session in a clean checkout of the task's repo snapshot.
2. Copy only that condition's skill folders into the session's `.claude/skills/`. Record the sha256 of each copied file.
3. Use the prompt from #4 for the task, changing only the condition line.
4. Save the full transcript under a results folder that exists before the run starts.

## Known threat to validity

The owner's saved skills load in every session on the account, whatever condition is being run. A C0 or C2 run can therefore still see and use the saved `proof-driven-delivery` or `evidence-audit`, which contaminates the comparison. Before scored runs, either use an account or profile without those saved skills, or record for every run which skills the session listed, and treat runs that invoked an out-of-condition skill as invalid.
