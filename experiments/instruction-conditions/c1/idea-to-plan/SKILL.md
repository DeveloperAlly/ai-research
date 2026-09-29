---
name: "idea-to-plan"
description: "Use only when the user invokes it: take a project from an idea to an owner-approved PRD, requirements, verified architecture and an agent-executable task plan, before any build starts."
---

# Idea to plan

Takes a project from an idea to a package that agents can deliver without guessing. Done means: one decided product, a PRD whose hero journey works for a brand-new user, testable requirements, an architecture with no unverified item on its critical path, and a task graph where every task has inputs, an output and a check. Existing docs are input, not truth: read them in full, list their claims, and verify before relying on any of them. Delivery then uses `proof-driven-delivery`.

## Execution cadence: chunked, on a clock
This applies to every step below.
- Before starting work, publish the chunk list: every chunk is 5 minutes or less, with its visible output, pass criteria, maximum tool calls and fallback. Do the riskiest chunk first.
- Start the clock from a real time source (a time tool, or `date` on the host), never from memory. State the total time budget if the owner set one.
- Every status message opens with a timer line computed from the real clock at that moment: `[T+mm:ss | chunk n/N: name | budget left mm:ss]`.
- Each chunk ends with its output posted and marked PASS or FAILED. A chunk without its named output is FAILED, never "in progress".
- If a chunk hits its time or call limit: stop, report the exact state and blocker, and propose the next move. Never extend silently.
- When background agents run, each status message includes every agent's state: running, done or blocked; its last output; its elapsed time.

## 1. Capture the idea and the constraints
- Write the owner's goal, deadline (with time zone), budget, who will build it (agents, people, both), where it must live and be hosted, and what must and must not be used. Quote the owner; do not paraphrase.
- Read every existing issue, doc and comment on the project in full. List each claim they make (capabilities, prices, limits, rules, estimates) as input to verify, not as fact.
- Confirm every destination this run will write to (repo folder, tracking issue) exists now. A missing destination is flagged to the owner; never invent one.

## 2. Close the product decision first
- If more than one product or direction is still open, write a decision record: each option, a score against the owner's stated criteria (for example a competition's judging rules), risks, build cost and a recommendation. The owner decides.
- List every other open decision (name, team, network or environment, domain, pricing) and get each closed, or deferred with a stated default.
- Nothing below starts while the product decision is open.

## 3. Verify what the plan depends on
- Every external claim (platform capability, SDK support, pricing, rate or CPU limits, content or competition rules) gets a source link and a label: VERIFIED-DOC, VERIFIED-LIVE or UNVERIFIED.
- Each UNVERIFIED claim on the critical path becomes a spike: a 5-minute live check or throwaway prototype that proves or disproves it. Run the spikes before the architecture is final and record their raw output.

## 4. PRD
- Problem, target user, the job they hire the product for, and why now.
- MVP scope and explicit non-goals.
- The hero journey and every other journey, step by step.
- **Zero-state walk:** walk the hero journey as a brand-new user with nothing set up. List every prerequisite they would lack at each step (account, wallet, funds, fees, permissions, installed app, data) and how the product supplies it. A journey with an unsupplied prerequisite is broken, however good the rest looks.
- Success metrics, each with how and when it will be measured, and whether the measurement is meaningful in the chosen environment (for example, test-network payments are not revenue).
- Business model, risks with mitigations, and the demo or launch script if there is one.

## 5. Requirements
- Number every requirement: `WHEN <trigger> THE SYSTEM SHALL <observable behaviour>`, with its source (PRD section or owner quote), priority (must / should / not this release) and an acceptance check that is a runnable command or a named check on the deployed surface.
- For each requirement, write its failure paths: empty, absent, malformed, unauthorised, too large, external service down, timeout, and for money: failed, partial and duplicate payment, and paid-but-delivery-failed.
- Non-functional requirements: performance, availability and what it covers, cost caps, security and privacy, compliance and content rules, observability.

## 6. Architecture
- Component diagram, and every journey as a sequence of hops (client, server, each external service, chain or queue).
- Trust boundaries and custody: who holds each key, secret and wallet, where it lives, and who signs what.
- Data model and API contracts.
- External services with their limits and costs from docs, and a budget count for every metered resource.
- Failure modes: what the user sees and what survives when each dependency is down.
- At least two alternatives for each major choice, each rejected by naming the requirement it fails.
- Composability test: the steps to add a second, different unit (a second product type, persona or payment mode). If they touch shared core code, the design is not composable.
- Security check: shared hostnames share cookies; duplicate auth systems; keys in the browser; credentials on hosts that do not need them.
- Label every fact. An UNVERIFIED item on the critical path means the architecture is a draft.

## 7. Independent review
- A fresh reviewer that did not write the package attacks the PRD, requirements and architecture against steps 2 to 6, and repeats the zero-state walk independently.
- Each finding is fixed, or rejected with evidence; the dispositions are published with the package.
- The owner approves the package before step 8.

## 8. Agent-executable plan
- A task graph. Each task has: id, the requirement ids it covers, inputs (files, accounts, credentials), the exact output, an acceptance check, dependencies, the agent role that runs it, and a size of one or more 5-minute chunks. Split anything bigger.
- Owner prerequisites come first and are named as owner tasks: accounts, keys, domains, funding, team registration.
- Order: spikes and riskiest tasks first; the first milestone is one real end-to-end journey on the deployed surface; parallel lanes are marked.
- Every requirement is covered by at least one task and every task cites at least one requirement.
- Build the timeline only from task sizes and compare it with the deadline, leaving a stated buffer. If it does not fit, show the owner a cut list; never cut silently.
- Write a hand-off prompt for the executing agents: where the package lives, that they deliver with `proof-driven-delivery`, and what they must not change without approval.
- If the repo uses build-lifecycle, write requirements as `spec.md`, architecture as `plan.md` and tasks as `tasks.md`.

## 9. Package
- One index file links the decision record, PRD, requirements, architecture, spike results, review dispositions and task graph, in the confirmed destination.
- The tracking issue gets a comment linking the index and listing the open owner tasks.

## 10. Close out and suggest improvements to this skill
Failures and lessons go in the tracking-issue comment; nowhere else unless the owner names an existing destination.
- Record quality signals: review findings by severity; owner changes after approval; zero-state gaps found only during build (each is a miss by this skill); requirements added during build; estimate vs actual per task, once delivery reports it.
- For each gap or correction, cite its evidence, name the step that should have prevented it and classify it as missing, unclear or not followed. For not followed, propose making the step checkable rather than louder.
- Propose exact edits tied to observed incidents, as a "Skill improvements" section; the owner approves before any change. If nothing went wrong, say so and cite the evidence.