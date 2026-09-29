---
name: skill-retro
description: "Use only when the user or a calling skill invokes it: after a run, turn its gaps, errors and owner corrections into evidence-backed proposed edits to the skills that ran, for the owner to approve."
---

# Skill retro

The learning step for any run that used skills. Works alone after any run, or is invoked last by a chaining skill.

## Where it goes

- Post the retro as a "Skill improvements" section of the run's completion comment, in the destination confirmed at the start of the run. Write it nowhere else unless the owner names an existing destination.

## Record the signals

- Every gap, error, false claim, rework, missed proof, chunk overrun and owner correction from the run, each with its evidence (a clock time, raw output or a quote).
- Owner overrides and corrections count most: each one means a step, rule or definition was wrong or missing.
- Chain check: for a chaining skill, list each skill it was meant to invoke and whether it actually loaded and was followed.
- Any signals the calling skill asks for (for example audit disagreement rates or unverified facts left).

## Turn signals into edits

- For each item, name the skill and step that should have prevented it and classify it:
  - **missing:** nothing covers it;
  - **unclear:** it is covered, but was easy to misread;
  - **not followed:** it was clear and was skipped. Propose making it checkable (a command, a count, a required output), not repeating it more loudly.
- Propose exact edits: the skill, the step and the text to add or change, each tied to an observed incident. No speculative additions.
- Put a rule in the one skill that owns it. If the same rule is needed by several skills, propose it for the shared skill, not a copy in each.
- Deliver the edits as a diff when the skill lives in a repo. Nothing is merged or saved without the owner's approval.
- If nothing went wrong, say so and cite the evidence.
