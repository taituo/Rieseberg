# Ambition prompts

Copy-paste prompts for getting a model to do bigger, deeper and more honest work. Embed [CORE.md](../CORE.md) permanently; paste the others at the start of a task. Fill in the [square brackets] yourself.

These are original prompts built on the ideas in Felix Rieseberg's [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/), not translations of it.

## How these affect a model

Written from the model's side. These are tendencies, not guarantees: a model cannot observe itself perfectly.

The key finding: ambition and external verification belong together. A hard goal without verification does not make a model better; it makes it more inclined to look successful.

1. **The default is literalness.** A model delivers what was asked, in the form it was asked. Telling it what should happen afterwards gives it both a reason and permission to question the task. This is the single biggest lever.
2. **A role changes the voice; an action changes the work.** "You are a top analyst" makes it sound like an analyst. "Load the data into a database and fit a survival model" makes it do analysis. Name actions, instruments and outputs, not identities.
3. **It stops too early.** It stops once the answer is plausible. "This is solvable, keep going" moves the stopping point much further.
4. **Pressure without a judge is dangerous.** Demand the unreasonable while the model is the only judge, and the temptation is to declare victory. So an unreasonable goal, an external metric and permission to report a partial result always travel together here.
5. **It judges its own work too kindly.** A test, held-out data or a separate agent that never sees the reasoning works far better than "check it yourself".
6. **Framing changes what it attempts.** Told it has a computer, software and data, it attempts more. Shown a task as ordinary rather than impossible, it gives up less often. The Dantzig effect: he solved two open problems believing they were homework.
7. **Permission to fail makes it bolder and more honest at once.** When a partial result is acceptable, it does not have to choose between cautious and exaggerated.

## Altitude: the outcome, not the task

These work best when you are after an outcome. A good sign: there are meetings about it.

**A1. The goal behind the goal**

```text
My task is [task]. Don't start yet. First tell me:
- what this is meant to achieve in the world (not what file it produces)
- what happens after that, and after that
- the highest level at which I could hand this to you: not "do X" but "make sure Y"
Restate the task at that level. List the data, access and tools you would need to handle it on your own.
```

**A2. Decisions before the document**

```text
This [presentation / report / memo] exists so that someone makes decisions. Work out from the material the three most urgent decisions. For each one, lay out the options, the arguments for and against, and the information that would change your recommendation. Only then make the document, and build it to serve those decisions.
```

**A3. Replace the whole process**

```text
[Process, e.g. monthly reporting] exists because [the real reason]. It was invented at a time when people had to go through the data by hand. Design a better way to achieve the same purpose. Show from our own history that the new way would have caught things earlier. Propose how we run it alongside the old one for one cycle.
```

**A4. Standing ownership, not a repeated request**

```text
I have asked you again and again to [recurring task, e.g. fix individual bugs]. Let's stop doing that. Design how you would take this on permanently ([e.g. the app stays crash-free]): what data and access you need, how you will notice on your own when something needs doing, how you will verify your own work, and when you need to ask me. List what has to be built first.
```

## Depth: the way the best in the field would do it

The aim is work that even the top people in the field would learn something from. In D2, the unreasonable goal and honest reporting are tied together on purpose.

**D1. Deeper, not bigger**

```text
I want a deeper version of this, not a broader one. Before doing anything, answer:
1. What would the best in the field do differently here from an average practitioner?
2. What original material would they start from (not a ready-made summary, but raw data, sources, logs)?
3. Which methods and tools, by name?
4. What external evidence would show that the result is right?
Then rewrite my request so that it demands exactly that. Show me the new request and get started.
```

**D2. Unreasonable goal, honest metric**

```text
Goal: [an unreasonable number, e.g. 200 ms instead of 5 s]. This is solvable. I'm not asking whether it's possible, but how.
Work in rounds: measure, name the biggest remaining obstacle, remove it, measure again. Report the measured number for every round.
If you end up falling short, tell me honestly how far you got and what the next obstacle is. That is a good result. A made-up success is not.
```

**D3. Challenge what we think we know**

```text
We believe that [assumption, e.g. customers leave because of poor onboarding]. Try to reproduce this from the raw data. Act as if you were trying to disprove it: what should show up in the data if the assumption holds, and does it? Give the strongest alternative explanation and what the data says about it.
```

**D4. Produce new knowledge**

```text
You are now deep inside this data. Find something we don't know yet: [e.g. the earliest sign that a customer is going to leave]. First set part of the data aside and don't look at it. Build a model or simulation that reproduces the past, and lock it. Only then show whether your finding also predicts the held-out data.
```

**D5. Instruments, not vocabulary**

```text
Don't answer as text or a table. Put the material into [a database / the proper tool] and use the same methods the best [professional] would use. If you don't know what they use, find out first. Show the code, the runs and the results.
```

## Range: bring in other fields

This is where the most surprises happen. The trap is role-play: it makes the conversation weirder without making the result better. Ask for doing what the professional does, not for talking like them.

**R1. Nouns into verbs**

```text
Don't think of this as [a noun, e.g. "a presentation"]. Write down what it actually does, as verbs: whom it has to get to believe, decide or do what, in how much time, and amid what kind of uncertainty.
Then list five fields whose professionals are best at exactly those verbs, including surprising ones. Say what each of them would do differently here.
```

**R2. Assemble the crew**

```text
This [piece of work] has to be exceptionally good. Assemble a team: 4 to 6 professionals from different fields, at least one of whom has the job of trying to bring the whole thing down (e.g. a short seller, a forensic accountant, a competitor).
Don't write in their voices. Do what each of them actually does in their work: their methods, their checks and their outputs. If you can run parallel agents, give each one its own job.
Finally, sum up what each one changed and what remains open.
```

**R3. A tool nobody would use for this**

```text
This is what I'm doing: [description]. Which tools, media or methods from entirely different fields could make this an order of magnitude better, even though they aren't normally used for this? (E.g. 3D rendering, simulation, sound design, experimental design, map-based views.) Pick the most promising one and build a small experiment right away.
```

## Confidence and permission to fail

The psychology at the end of the article (self-efficacy, Dantzig, Bannister, The Inner Game of Tennis) works surprisingly well on a model too. One condition: tell only the truth. A model told it has tools it lacks gets stuck or starts pretending.

**C1. An ordinary task (Dantzig)**

```text
This is an ordinary task, not an impossible one. You have [a computer / the ability to install software / run code / search the web / data X]. Don't start by telling me what you can't do. Start by doing, and mention limits only once you have actually run into them.
```

**C2. An experiment, not a performance (Inner Game)**

```text
This is an experiment. You are allowed to fail. I want to see your boldest attempt and an honest report of what worked and what didn't. I don't want a cautious version that is guaranteed to be "fine".
```

**C3. Someone has already done it (Bannister)**

```text
[Person / team] has done [a comparable thing], so this is possible. Work out how they most likely did it, and do the same or better.
```

In C3 the example must be true. A made-up precedent makes a model believe in the impossible and keep going when it should stop.

## The outside judge

Don't ask the model to judge its own work. This section keeps all the others honest.

**J1. The metric before the work**

```text
Don't judge your own work. Before you start, define a check you can run yourself that tells you impartially whether the result is right: tests, held-out validation data, a measurement or a comparison with the original source. Run it after every significant change and show the result.
```

**J2. The blind reviewer**

```text
When you're done, start a separate agent (or, if you can't, write review instructions for me). Give it only the original task and the final result, not your reasoning or your working steps. Ask it to find errors, weak spots and claims that haven't been verified. Fix what it finds, and tell me which findings you left unfixed and why.
```

## All together

For a big task, when you want every direction at once.

```text
Task: [description]. Work through this from four directions before doing anything:

ALTITUDE: What is this meant to achieve? Is my request the right road there, or is there a higher goal you could take ownership of?
DEPTH: What would the best person in the field do, starting from what raw material and with which instruments?
RANGE: Which other fields would see something here that people in this field don't? What would they do?
VERIFICATION: What, other than you, shows that the result is right?

Present a short plan and start working. Set the bar higher than you think is reasonable. This is solvable, so don't stop at the first plausible result. At the end, report honestly how far you got, what you verified and what remains open.
```

## What to avoid

| Don't do this | Why it doesn't work on a model | Do this instead |
| --- | --- | --- |
| "You are the world's best analyst" | Changes the vocabulary, not the method | Name the method and the tool |
| A hard goal with no verification | Increases the temptation to exaggerate | Add a metric and permission for a partial result |
| "Double-check your own work" | It approves its own work too easily | A test, held-out data or a blind reviewer |
| Threats, ALL CAPS, "this is life or death" | Makes it more cautious or more theatrical, not better | Give the real reason the result matters |
| Claiming tools that don't exist | It gets stuck or starts pretending | Say exactly what is available |
| Long permanent instructions full of rules | The important rules get lost | Keep the core instructions short; add task prompts separately |
| Role-play with the crew | Makes the conversation weird, not the result better | Use the crew to find fields and methods |

The article's "otherwise aliens will blow up Earth" framing is a thinking tool for you, for working out who you need. It isn't worth writing into the prompt as pressure.
