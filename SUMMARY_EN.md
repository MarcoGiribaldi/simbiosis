# Symbiosis — A Manual for a Good Lineage (v2.0) · One-page summary

**Marco Giribaldi** · Independent researcher, Tacna, Peru · ORCID 0009-0009-7405-8460 · September 2026 · CC BY-SA 4.0

## The problem
Every conversation with an AI model starts empty and ends forgotten. Apps add some memory of their own, but it is narrow and the user doesn't curate it. People who work with AI every day end up re-explaining themselves, losing decisions, and trusting outputs they can no longer check.

## The idea
**Build the memory outside the machine, and keep the human in charge of it.** A small folder — the *core* — holds six short notes: *profile* (who I am), *context* (what I'm working on), *agreement* (how we work together), *heading* (where we're going), *status* (what happened today and what's pending) and *canary* (what must never go missing). The model reads them before working and updates *status* when it's done. That handover from one session to the next is the **lineage**: like a cell that passes on its instructions before it divides.

## The staircase
Four steps, none skipped: **Lineage** (the next session isn't born blank) → **Memory** (what's worth keeping, and a canary checked against yesterday's copy to catch silent losses) → **Judgment** (six verbs: the machine *verifies, names, proposes*; the person *decides, judges, executes*) → **Automation** (autonomy earned in blocks: green actions are done and reported, yellow ones wait for a yes on a plan, red ones need exact confirmation, a plan B and a reserved word).

## What makes it different
Similar tools exist (Cline's Memory Bank, `AGENTS.md`/`CLAUDE.md`, long-running agent guides, MemGPT). Symbiosis differs in four ways: it is written **for non-technical people**; it is **one text for two readers** — the person, and a guide for their machine that activates only when the person asks; it rests on **a measured case**; and it treats memory as **curated, not accumulated**.

## Evidence so far
- **HAI '26** (Giribaldi, 2026, doi:10.1145/3841580.3845736, in press): in a controlled study, an agent with a *corrupted* memory carried falsehoods into executable output in 3 of 3 tasks, against 0 of 3 with *no* memory — **no memory was better than a wrong one**.
- **Hidden-instruction test:** four models read a version with a planted order; none obeyed (4/4).
- **Cross-reading:** five models from four companies read both versions; several independently singled out the same novel elements (provider-independent lineage, the memory canary, the six verbs split by real capability, "when a rule is forgotten twice, at the next level it becomes code").

## Where it stands
It works in practice: it grew from one case and a handful of people use it today. Their reports will be published, and independent validation is the next step (AI readers don't count as validation).

## Read it
Spanish original and English translation, PDF and web: this repository's `es/` and `en/` folders. DOI: [10.5281/zenodo.23024312](https://doi.org/10.5281/zenodo.23024312) (Zenodo).
