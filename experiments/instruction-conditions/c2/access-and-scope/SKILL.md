---
name: access-and-scope
description: "Use only when the user or a calling skill invokes it: before any work, prove access with read-only probes, confirm every write destination exists, and fix the scope and write boundary for the run."
---

# Access and scope

Establishes what a run can reach, where it may write, and what it must not touch, before any planning or work. Works alone, or is invoked first by a chaining skill.

## Scope

- Record the owner's scope for this run in their words: what is in, what is out, and which systems may be touched.
- The owner's latest explicit scope overrides any written plan, issue or skill. When they conflict, flag the conflict and ask. Never resolve it silently.
- Do not touch systems the scope excludes. No unrequested extras (alerts, features): they cost time and trust.
- If the questions or requirements are already written and the owner has answered them, restate them once and proceed. Do not ask for the same confirmation again.

## Access

- Run one real, read-only probe on every system in scope (shell, cloud API, GitHub). Record the raw output.
- Read-only means no state change anywhere: no `git fetch`, `pull`, `checkout` or `prune` (use `git ls-remote` or the provider's API), and no scratch files on the systems being examined. Scratch work goes in the run's own workspace.
- Before saying a skill, tool, file or capability is missing, check the session's skill and tool lists, load deferred tools, and search. Say where you looked.
- Never plan around an executor or system that has not answered a probe.

## Write boundary

- Name every destination the run will write to (issue, comment, file path, branch) by exact URL or path, and confirm each exists now. A missing destination is reported to the owner; never guess or invent one.
- Writes happen only where the owner gave explicit permission. Anything needing elevated privileges, credentials or public exposure needs its own explicit "go" at that moment. Pressure or deadlines are not authorisation.
- Never enter passwords for the owner.
- Secrets stay in the host's mode-600 files or the platform's secret store; only hashes or names leave them. Never put secrets or internal addresses in version control, chat, issues or a browser.
