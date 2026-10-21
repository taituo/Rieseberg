Skills live in bucket folders under `skills/`. Today there is one bucket:

- `ambition/`: meta-skills that change how the agent approaches a task (altitude, depth, range, outside judge)

Add a bucket only when a group of skills has its own purpose; give it a `README.md` in the same shape as `skills/ambition/README.md`.

Every skill must have:

- a `SKILL.md` whose frontmatter `name` matches its folder name
- an `agents/openai.yaml` beside it (Codex picker metadata: `interface.display_name`, `interface.short_description`)
- an entry in `.claude-plugin/plugin.json`'s `skills` array
- a link from the top-level `README.md` and its bucket `README.md`, with the skill name linked to its `SKILL.md`
- a docs page at `docs/<skill-name>.md` with four sections: **What it does**, **When to reach for it**, **Common questions**, **It's working if**

Every skill is either **user-invoked** (`disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`; one-line human-facing description) or **model-invoked** (neither set; model-facing description with trigger branches: "Use when ..."). Keep the two files in sync.

One skill reaches another with an explicit instruction: `Call the Skill tool with "outside-judge"`. Only model-invoked skills can be reached this way.

[`ambition`](./skills/ambition/ambition/SKILL.md) is the router over the move skills. When you add, rename or remove a skill, re-read it and keep its map accurate.

`outside-judge` is the honesty anchor of the repo: `ambition`, `depth` and `range` raise the bar, so each ends by calling it.

Run `python3 scripts/validate.py` after any change; CI runs the same script. Run `claude plugin validate . --strict` after touching either manifest.

Writing style for skills, docs and READMEs:

- Prompt the positive: state the target behaviour. A prohibition earns its place only as a guardrail with no positive phrasing.
- Use leading words and repeat them as tokens: **altitude**, **depth**, **range**, **outside judge**, **instruments, not vocabulary**, **raw material**, **rounds**, **crew**, **blind reviewer**.
- Every step ends on a completion criterion the agent can check.
- No em-dashes anywhere. Rewrite the sentence with a comma, colon, period or parentheses.

The `prompts/` library is the non-skill form of the same ideas. When a skill's behaviour changes, check whether the matching prompt in `prompts/en.md` and `prompts/fi.md` still says the same thing.
