# ambitious-prompt

## What it does

Takes a prompt you are about to give a model and rewrites it to ask for **altitude**, **depth**, **range** and an **outside judge**. It names actions and instruments instead of personas, pairs every hard target with a check and an honest exit, and states only the capabilities the receiving model really has. You get the new prompt in a code block plus three bullets on what changed.

## When to reach for it

When you are writing a prompt for another agent, a scheduled task, a subagent, or a model you use elsewhere, and you want more than the literal request.

## Common questions

**Will it make my prompt long?** It keeps the rewrite as short as the task allows and adds a shorter variant when the rewrite passes about 200 words.

**Why does it ask what tools the model has?** A model told it has tools it lacks stalls or pretends. The rewrite states only real capabilities.

## It's working if

- The rewrite contains no "you are a world-class ..." line, but does name a method or instrument.
- Every target in it comes with a measurement and permission to report falling short.
- You can paste it as-is.
