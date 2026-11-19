# Jev Werewolf deception judge (NoorElAlfi)

## Overview
A research benchmark that asks whether Jev can tell who is lying in Werewolf, Mafia and Avalon transcripts. It compares several Jev question designs against simple baselines and a local LLM. It also runs live games in which the judge's top suspect is voted out.

## Relevance level
**Direct.** Hosted Jev, pinned to `jev-1.13.0`.

## Maturity / evidence
- A research prototype with 223 offline tests, markdown reports with 95% bootstrap CIs (resampling whole games), and an HTML results page. Created 2026-09-29.
- **Inspected:** README (which copies its numbers from `reports/`). Not re-run.

## Game mechanic
Social deduction: judging hidden roles from the public conversation, and in live games, driving the village vote. This is a judgment task over long text, not action selection.

## Decision inputs and outputs
- **State:** `public_view(transcript, upto_round)`, the same public text for every judge, with no night actions or roles.
- **Question designs:**
  - `jev_isolated`: one player per call.
  - `jev_batched`: all of a round's speakers in one call.
  - `jev_multidim`: five narrow dimensions per player, combined by a fixed composite.
  - `jev_noul`: "is X concealing their true role?"
  - `jev_pairwise`: "does X protect Y?"
- **Output:** a per-player probability of being deceptive. In live games, the top suspect is voted out, optionally with an abstention threshold.

## Implementation / runtime
Python. Ollama with llama3.1:8b generates games and serves as the local LLM judge. Judgments are cached per config hash, so runs can be resumed.

## Availability and licenses
**No license file** ("research prototype, not a product"). External datasets carry their own licenses.

## Attributed results (author, README/`reports/`)
- LLM-generated games (200 games, 4,479 player-rounds):
  - `jev_multidim` AUC 0.706 [0.680, 0.730];
  - logistic regression on Jev answers 0.825 (fitted with labels, per domain);
  - `jev_noul` 0.449, below chance;
  - the llama3.1:8b judge 0.403, below chance.
- Human games (Mafia, Avalon, spoken Werewolf): no judge is clearly useful. Human Mafia is at chance for all judges, and Jev's ECE on spoken Werewolf is 0.41–0.56.
- Live games (50 per condition):
  - villagers win 50% [36, 64] with `jev_batched` deciding the vote, vs 24% with random votes and 12% with the llama judge;
  - an abstention threshold lowered the win rate (28% / 12%).
- Cost and latency: `jev_batched` 0.20 s per view (hosted), about $0.0003 per game; the local llama judge 4.7–40 s per view.
- Ablation: naming the wolves' tactic in the criteria made Jev **worse** (−0.061 AUC), because villagers use the word "deflect" more often than wolves do.

## Possible jeff adaptation (inference)
- This shows how question design changes results: several narrow questions beat one broad yes/no question. jeff's `noul` path is the weakest one here as well.
- For a game, the transferable idea is a decision model as a **suspicion meter or vote advisor**, scored against hidden roles that the game knows.
- Expect jeff to do worse on long transcripts. A small game could keep the statements short and authored.

## Limitations
Signals found in LLM-written games largely reflect the writing style of the LLM wolves and did not transfer to human data. Live-game samples are small (50 games per condition).

## Sources (accessed 2026-10-02)
- https://github.com/NoorElAlfi/jev-werewolf (README, metadata)
