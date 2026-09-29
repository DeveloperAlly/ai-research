---
name: timed-execution
description: "Use only when the user or a calling skill invokes it: run work as short timed chunks against a real clock, with a visible timer on every status message and PASS or FAILED per chunk."
---

# Timed execution

Runs any piece of work as a sequence of short, visible, timed chunks. Works alone, or is invoked by a chaining skill for the whole of its run.

## Before work starts

- Publish the chunk list. Every chunk takes 5 minutes or less and names its visible output, pass criteria, maximum tool calls and a fallback.
- Put the riskiest chunk first.
- Read the start time from a real time source (a time tool, or `date` on the host). Never estimate a time.
- State the total time budget if the owner set one.

## During work

- Status messages lead with state: what works, what does not, what blocks. Keep one current source of truth for status; history goes below it.
- Every status message opens with a timer line computed from the real clock at that moment: `[T+mm:ss | chunk n/N: name | budget left mm:ss]`.
- Each chunk ends with its output posted and marked PASS or FAILED. A chunk without its named output is FAILED, never "in progress".
- When a chunk hits its time or call limit: stop, report the exact state and the blocker, and propose the next move. Never extend a chunk silently.
- When background agents run, every status message includes each agent's state (running, done or blocked), its last output and its elapsed time.

## At the end

- Report planned against actual time for every chunk.
- Every time in any report, comment or commit message is copied from a clock reading taken at that moment. A time written from memory is a false claim.
