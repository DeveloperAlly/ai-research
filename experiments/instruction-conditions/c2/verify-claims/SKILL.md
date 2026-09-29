---
name: verify-claims
description: "Use only when the user or a calling skill invokes it: give every factual claim a source and a verification label, and turn unverified claims on the critical path into quick live checks."
---

# Verify claims

Makes every statement in a run traceable to evidence. Works alone on any document or answer, or is invoked by a chaining skill for its whole run.

## Label every claim

- Each fact carries one label: VERIFIED-LIVE (observed now, raw output recorded), VERIFIED-CODE (file and line), VERIFIED-DOC (link, checked on a stated date) or UNVERIFIED.
- Published sources are fetched and read before they are cited, never cited from memory.
- Internal evidence links to the exact issue, comment, commit, file or transcript.

## Critical-path claims

- A decision, design or recommendation that rests on an UNVERIFIED claim is a draft.
- Turn each UNVERIFIED claim on the critical path into a spike: a check of 5 minutes or less (a read-only command, a doc lookup, a throwaway prototype) that proves or disproves it. Record the raw output.
- An UNVERIFIED claim can never justify closing, deleting, merging or shipping anything.

## Honest statements

- Every status claim must be literally true. Never state a time, result or state that was not observed. Timestamps are copied from an output line or a clock reading.
- When two sources disagree, record both and say which the evidence supports.
- Correct a false statement the moment it is found, in the same place it was made. Own mistakes plainly, without excuses; lost access is a consequence, not a reason.
- Never give a command or instruction that has not been checked against current documentation.
- Never say something cannot be done until every available route has been tried. Name the exact blocker instead of answering "how" with "can't".
