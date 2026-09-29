---
name: independent-review
description: "Use only when the user or a calling skill invokes it: have a fresh reviewer that did not produce the work attack it against a supplied checklist, then dispose of every finding with evidence."
---

# Independent review

Work is checked by something that did not produce it, before anyone accepts it. Works alone on any artifact, or is invoked by a chaining skill at its review point.

## Inputs from the caller

- The artifact, the checklist to attack it against, and the sampling rule if the artifact is a list of verdicts (default: at least 10% and at least 10 items, plus every destructive recommendation).
- The producer also writes a short confidence note: where it guessed, what it assumed without checking, and what it would attack first. The note can only widen the review, never narrow it.

## Running the review

- Run the reviewer as a fresh background agent with a time limit, after checking that it can reach the artifact and its sources.
- Give it the artifact, the checklist, the confidence note and the sources. Do not give it the producer's reasoning or rationale.
- The reviewer returns findings, each with the claim, the evidence and what it breaks, and a severity: blocking or non-blocking.

## Disposing of findings

- Every finding gets a disposition: fixed, or rejected with evidence. Agreeing without checking is a defect; so is ignoring a finding.
- No blocking finding may stay unresolved. After three rounds without clearing, take it to the owner.
- Publish the findings and their dispositions with the artifact.
