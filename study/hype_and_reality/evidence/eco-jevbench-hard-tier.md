# JevBench: hard tier and where jeff, Laya, Von, GLiNER2 sit

- **Sources:** https://github.com/fstandhartinger/jevbench (README; accessed 2026-10-02; locators: tiers, scoring axes, leaderboard; read through a fetch summary). The ecosystem note's top-5 table (Jev 1.13.0 ranked 4th at 63.29) was not re-verified in this pass.
- **Evidence type:** author evaluation (benchmark run by an unaffiliated party, with submissions by model authors); independence: yes of TypeSafe, not of submitters.
- **Task:** 220 adversarial hard-tier decisions (111 public, 109 held out) written by two LLMs; four axes (intelligence, calibration, speed, cost); 20% weight on 308 sealed items. No dedicated abstention, injection or out-of-scope component per the summary.
- **Rankings reported in the fetched summary (versions differ per row):** Jeff (GLiFormer 400M) 63.5 at v1.2.2; Laya 64.3; Kev 0.6B 66.7; GLiNER2 base 63.1; SemIf 73.1 at v1.2; v1.4.2.2 top: Imajev-4B 67.37, Plumb-4B 65.84. Scores are composites of unlike axes.
- **Relevant local classes:** none directly; Q1, Q3.

## What the source reports
- Hard-tier intelligence is chance-corrected accuracy on LLM-written items; the composite mixes calibration, speed and cost, so rank differences between jeff (~400M zero-shot) and Laya are 1 point.
- Held-out items are sent to services during evaluation, so sealed items are not fully blind.

## Strength and caveats
- Cannot support claims about rejection, injection or off-topic input. Also a warning: the board ranks jeff and trained clones almost equal while independent adversarial tests (eco-injection-bench-cwhy) separate them widely.
