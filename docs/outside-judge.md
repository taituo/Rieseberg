# outside-judge

## What it does

Holds the work to a judge that can say no, picked before the work starts when possible. Strongest first: a check that runs, held-out data, a primary source, a measurement, a **blind reviewer** (a separate agent that sees only the task and the result, never the reasoning). It runs the judge after every significant change and reports every claim as verified, unverified or failed.

## When to reach for it

The agent reaches for it before declaring non-trivial work done, when a target was set, when results go to other people, or when you ask it to check, verify, validate or review. `ambition`, `depth` and `range` call it automatically. Type `/outside-judge` to force it.

## Common questions

**Why not just ask the agent to double-check?** A model approves its own work too easily. A judge that is not the model is far stronger evidence.

**What if no subagents are available?** It writes review instructions for you, so a person can play the blind reviewer.

## It's working if

- You can see which judge verified each claim.
- Unverified claims are labelled as unverified rather than smoothed over.
- Sometimes the report contains a "failed" list. A judge that never says no is not judging.
