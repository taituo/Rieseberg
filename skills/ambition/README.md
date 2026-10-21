# Ambition

Meta-skills: they change how the agent approaches a task rather than what domain it works in. Speed comes free; these spend effort on **altitude**, **depth** and **range**, and hold the result to an **outside judge**.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[ambition](./ambition/SKILL.md)**: Plan a task through altitude, depth and range, then hold the result to an outside judge. The entry point and router.
- **[ambitious-prompt](./ambitious-prompt/SKILL.md)**: Rewrite a prompt so it asks for altitude, depth, range and an outside judge.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[altitude](./altitude/SKILL.md)**: Raise a task to the outcome it serves: decisions over documents, process replacement, standing ownership.
- **[depth](./depth/SKILL.md)**: Do a task the way the field's best practitioner would: raw material, instruments, assumption checks, target rounds.
- **[range](./range/SKILL.md)**: Bring methods and tools from other fields into a task: verbs, a crew with an adversary, one foreign instrument.
- **[outside-judge](./outside-judge/SKILL.md)**: Verify work with something other than your own judgment: a check that runs, held-out data, a blind reviewer.
