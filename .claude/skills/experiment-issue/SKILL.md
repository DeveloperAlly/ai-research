---
name: experiment-issue
description: "Use only when the user invokes it: turn a given problem into a pre-registered experiment issue in a GitHub repo, filling the repo's experiment issue template, then capture what the template or this skill should change."
---

# Experiment issue

Turns a problem the owner states into one experiment issue that another chat can run without guessing. Invoking this skill is the owner's permission to create that one issue; nothing else is written.

## 1. Confirm the destination and the template

- The target repo is the one the owner names; default `DeveloperAlly/ai-research`.
- Read `.github/ISSUE_TEMPLATE/experiment.yml` from the repo's default branch. If the repo or the template does not exist, stop and tell the owner. Never invent a template or a destination.
- The issue's sections are the template's fields, in the template's order, with the template's labels as headings.

## 2. Check for an existing issue

- List the repo's open and closed issues. If one already covers the problem, link it and ask whether to extend it instead of creating a duplicate.

## 3. Capture the problem in the owner's words

- Quote the owner's problem statement verbatim under Purpose, then state the one question it reduces to.
- Anything the owner has not decided (scope edges, models, budget) is written as `OPEN: needs owner - <question>`. Never fill a gap with a guess.

## 4. Fill each field to its standard

- **Hypotheses:** each has a predicted outcome and the observable result that would falsify it.
- **Background:** every published source is fetched and read before it is cited, with the date checked. Internal evidence links to the issue, commit or transcript. Keep the two lists separate. Unverified claims are labelled UNVERIFIED.
- **Design:** conditions, tasks and a fixed baseline, each measure with an exact definition, and what is held constant.
- **Success criteria:** thresholds and the decision each result leads to, set now.
- **Protocol:** numbered steps, runs per condition (at least 3 for LLM runs), randomised order, blinding where possible, a grader that is not the tested chat, stop rules and a time and token budget.
- **Reproducibility:** where prompts, transcripts and results will be stored. Confirm each location exists, or list creating it as the first protocol step.
- **Answer keys:** if the experiment uses known answers, never put them in the issue, the repo or anywhere a tested chat can read. Deliver them to the owner privately and state in the issue who holds them.
- Leave the "after the run" block as the template provides it.

## 5. Create and report

- Create the issue with the title `[Experiment] <short question>`.
- Reply with the link, the list of `OPEN` items for the owner, and anything held privately (answer keys).

## 6. Learn from the run

After the issue exists, post one comment on it headed "Template and skill feedback":

- Fields that were hard to fill, left `OPEN`, or did not fit this problem, each with the reason.
- Anything the problem needed that the template has no field for.
- For each gap, name the template field or skill step that should cover it and classify it: **missing** (nothing covers it), **unclear** (covered but easy to misread) or **not followed** (clear but skipped; propose making it checkable rather than louder).
- Exact proposed edits to `experiment.yml` or this skill, each tied to what happened in this run. No speculative additions. The owner approves before either file changes.
- If nothing went wrong, say so and name the evidence (no `OPEN` items, every field filled to standard).

When the owner later edits or overrides the issue, those edits are the strongest signal: add them to the feedback comment and propose the matching template or skill change.
