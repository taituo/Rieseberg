# Rieseberg: Skills for Ambitious Work

Meta-skills that change *how* an agent approaches a task, so it aims higher and stays honest about what it reached. They work with any model and any domain.

[Suomeksi](./README.fi.md)

"We're not ambitious enough" is easy to say and hard to follow. Felix Rieseberg's [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) turns it into technique. He splits ambition into four directions: **speed**, **altitude**, **depth** and **range**. Speed comes free with a model. These skills turn the other three into steps an agent runs, and add the piece that keeps them honest: an **outside judge**.

## Installation

A plugin updates itself. [skills.sh](https://skills.sh) copies editable files into your project, and you update them by hand. Pick one per agent, because installing both gives you every skill twice.

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add taituo/rieseberg
claude plugin install rieseberg@taituo
```

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add taituo/rieseberg
codex plugin add rieseberg@taituo
```

</details>

<details>
<summary><strong>Any other agent, or editable files</strong></summary>

```bash
npx skills@latest add taituo/rieseberg
```

</details>

<details>
<summary><strong>From a clone</strong> (symlinks, so <code>git pull</code> updates them)</summary>

```bash
git clone https://github.com/taituo/rieseberg
./rieseberg/scripts/link-skills.sh
```

Links every skill into `~/.claude/skills` and `~/.agents/skills`.

</details>

Then type `/ambition` before your next real task.

## Why these skills exist

These fix failure modes that show up when you push a model on a task it could do far better.

### #1: The agent does exactly what you asked

**The problem.** A request is your best guess at a road to an outcome. The agent takes the road and never asks where it leads, so you get the deck you asked for instead of the decision you needed.

**The fix.** **[altitude](./skills/ambition/altitude/SKILL.md)** climbs from the task to the goal behind the goal and checks whether the requested road is the best one: decisions over documents, replacing a process built for reading data by hand, or taking standing ownership of a state ("the app stays crash-free") instead of fixing one crash at a time.

### #2: The agent sounds like an expert without working like one

**The problem.** Tell a model it is a world-class statistician and it switches vocabulary, not methods. You get a markdown table where a statistician would fit a model.

**The fix.** **[depth](./skills/ambition/depth/SKILL.md)** names the best practitioner and makes the agent use their raw material and their instruments, by name. It challenges the belief the task rests on, works hard targets in measured rounds, and tests new findings on data set aside before looking.

### #3: Everything comes from one field

**The problem.** A task draws on the one discipline it needs on the surface, so the result looks like every other result from that discipline.

**The fix.** **[range](./skills/ambition/range/SKILL.md)** rewrites the task's noun into verbs, assembles a crew of fields that are best at those verbs (always including an adversary such as a short seller or a forensic accountant), has each one *do* their job rather than imitate their voice, and builds one small experiment with an instrument from outside the field.

### #4: Ambition without a judge turns into theatre

**The problem.** This is the one the other three create. Push a model with a hard target and let it grade its own work, and you raise the pressure to declare success. Models approve their own work too easily.

**The fix.** **[outside-judge](./skills/ambition/outside-judge/SKILL.md)** picks a judge that can say no before the work starts (a check that runs, held-out data, a primary source, a blind reviewer that never sees the agent's reasoning) and reports every claim as verified, unverified or failed. Every other skill here calls it before calling the work done.

## Reference

### User-invoked

Reachable only when you type them.

- **[ambition](./skills/ambition/ambition/SKILL.md)**: Plan a task through altitude, depth and range, then hold the result to an outside judge. Start here.
- **[ambitious-prompt](./skills/ambition/ambitious-prompt/SKILL.md)**: Rewrite a prompt so it asks for altitude, depth, range and an outside judge.

### Model-invoked

The agent reaches for these on its own when a task fits, and you can type them too.

- **[altitude](./skills/ambition/altitude/SKILL.md)**: Raise a task to the outcome it serves.
- **[depth](./skills/ambition/depth/SKILL.md)**: Do a task the way the field's best practitioner would.
- **[range](./skills/ambition/range/SKILL.md)**: Bring methods and tools from other fields into a task.
- **[outside-judge](./skills/ambition/outside-judge/SKILL.md)**: Verify work with something other than your own judgment.

### Without skills

- **[CORE.md](./CORE.md)**: six short always-on instructions to paste into `CLAUDE.md`, `AGENTS.md`, project instructions or a system prompt.
- **[prompts/en.md](./prompts/en.md)** and **[prompts/fi.md](./prompts/fi.md)**: the same ideas as copy-paste prompts, in English and Finnish, with notes on what each one changes in a model's behaviour.

## Credits

The four directions of ambition and the techniques behind them come from [Felix Rieseberg's post](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). The skills are original writing, not a copy of it. Repo structure and skill-writing conventions follow [mattpocock/skills](https://github.com/mattpocock/skills).

MIT licensed.
