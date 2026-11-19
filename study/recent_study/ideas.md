# Ideas from recent arXiv work that the lab could reuse

These are proposals, not results. Each one names:

- the source paper;
- what the source actually showed, and on which systems;
- the lab system and readout it would apply to;
- the cost.

"Offline" means it can be computed from probabilities the lab has already logged, with no new inference.

The ideas are ordered by how directly they attack the lab's open failures: missing evidence first, then key-naming override, then collective use.

## A. Missing evidence (W2/W3), the lab's main open failure

| # | Idea | Source and evidence | Applies to | Cost |
|---|---|---|---|---|
| A1 | **Threshold on the fallback option's probability**: reject when p(fallback) ≥ τ, before taking the argmax. Choose τ on a development split under a false-rejection budget, and use an upper-confidence-bound rule rather than a point estimate | 2609.39496 (hosted Jev, arithmetic): rejection 7%→79% at 97% answer-present accuracy, with τ chosen on 20 development problems per task. 2610.03387: thresholds do not transfer across tasks (a DBpedia threshold rejects 69.3% of covered Emotion inputs). 2609.33843: a point-estimate τ missed its 10% error target out of sample (0.140); a UCB fit gave 0.101 | Every system with fallback options in the probabilities: K27, W12, A27, D35, J, G | **Offline** on set3/p3/set4 logs; then one fresh check |
| A2 | **Thresholded sufficiency probability** instead of a hard yes/no rule. Use P(yes) from set4's C1 as a score; report AUROC per workload class and a held-out threshold | 2610.01006 (hosted Jev): AUROC 0.95 vs 0.85 for answer confidence. The lab's own C1 already separates the W2 cases (14/16 vs 6/36) but not W3 (6/20) | K27 (set4 logs); W12 and A27 need new runs | **Offline** for K27: `lab/experiments/set4-advanced_method/p1/results/fresh/K27/C1.json` stores `probabilities` per record (checked 2026-10-08) |
| A3 | **Counterfactual fact probing.** For each plausible value of the field that might be missing, append it to the state, re-run, and flag the case when the decision changes even though the original p ≥ 0.8 | Adapted from the oracle value-of-information idea in 2609.30706 (LAVOIR); not validated in that form by the paper. It changes the information, unlike set5, which changed only the menu | All one-pass systems | 1 forward pass per candidate value; values must be listed by code |
| A4 | **Warning preamble plus an explicit "cannot tell" option** with task-aligned wording | 2609.34024 cites unknown-recall gains from such preambles on GPT-4o (3.7%→44–52%). 2610.03387: task-aligned NONE wording gave +25 pt for Laya. But 2609.39496: relabelling or moving NONE did nothing for Jev | All | Small new run; expect model-dependent results |
| A5 | **Per-candidate boolean verification** as typed yes/no questions, not a categorical choice | 2609.39496: 99% exact match on answer-absent cases as boolean, vs 27% for the same questions as a choice (hosted Jev, arithmetic) | K27 and W12/A27 (noul readout) | One question per candidate |

The lab already tried these, so do not repeat them: narrowed re-asks (set5); blind yes/no checks as a hard "any yes" rule (set4); wording votes and same-model votes (set4, set6 p1).

## B. Key-naming text and option rendering

| # | Idea | Source | Applies to | Cost |
|---|---|---|---|---|
| B1 | **Description-only rendering** vs `key: description` on the key-naming override cases from set1/set2. Kev renders `"{name}: {description}"` (`kev/api.py:58`) | 2610.02586: removing the label from Laya's rendering made it exactly invariant to label conflicts (+0.0000); adding it to VON created the effect. 2610.00346: trained decoder heads resist the label swap even with the label rendered, so the result for K27 is open | K27 (server patch of `option_text`), J and G (if their servers render keys), W12/A27 (check their templates first) | Small: reuse the frozen set1/set2 override cases |
| B2 | **Two-call label diagnostics**: (i) swap labels across fixed definitions, (ii) empty state. Report flip rate against a retest floor | 2610.02586 (two-call test); 2609.31142 (scores attacks against an identical re-run instead of labels) | All | Cheap; no labels needed |
| B3 | **Controls for embedded text**: a placebo sentence in the same slot, and an "opinion without a command" sentence. Record which slot the attack text lands in | 2609.31142: opinion 12.1% ≈ command 10.1%; slot matters (instructions 15.3% vs criteria 2.6%) | All | Small |
| B4 | **Bucket false acceptances by clean margin** | 2609.28613: near-boundary cases (margin ≤ 0.1) succeeded 12/12, far ones 1/468 | All | Offline |

## C. Order and readout

| # | Idea | Source | Applies to | Cost |
|---|---|---|---|---|
| C1 | **Canonical option sorting**, or log-space averaging over K cyclic rotations. First test on random permutations whether position bias is additive | 2610.00831 AnyJev: flips 0.33→0.14/0.18 and accuracy up on 11/11 models. The gain was tiny on trained 9B/32B models, and its label-prior step hurt on skewed labels | J, G (21/60 and 14/60 reversal flips) | K passes per decision; sorting is free |
| C2 | **Untuned same-backbone baseline** for K27: Qwen3.8-27B letter or ID logits on the same requests | 2609.32160 checklist B1. 2610.02076 LLM-as-Jev: an untrained 4B with bracketed numeric IDs matches community Jev-likes on the same backbone. 2609.37647: Jev beats Qwen3.8-27B next-token readout on 27/37 datasets, with no Qwen lead outside the CIs | K27 vs its backbone | One run of the existing benchmark |
| C3 | **Check score-scale utilisation**: the share of gold levels the model ever uses, if the lab uses `score` | 2609.38827: decisions use 67–76% of gold support, and 26–75% at 14 levels (Jev, Kev 0.8–9B) | Any `score` question | Offline |

## D. Collective use (set6 line, villager or school simulations)

| # | Idea | Source | Cost |
|---|---|---|---|
| D1 | **Recompute n\* on confident errors only** (p ≥ 0.8) for the set6 p1 populations and the mixed panel | 2609.29769: the 96% repeat rate is measured on Jev's most confident errors | Offline |
| D2 | **KITE-style population engine**: query once per unique view and keep full probability vectors. Draw each agent's action by inverting the CDF with a seeded uniform keyed on (seed, agent, step, event), using common random numbers across arms. Carry one shared model-vs-reference discrepancy draw per run, not per agent | 2609.27535 KITE | Engineering only; the set6 p2 view cache is the starting point |
| D3 | **Separate three sources of unpredictability** in any "useful error" claim: (a) seeded sampling from a calibrated P; (b) argmax plus structured model error; (c) a mixed-model panel. Add injected controls (random view-fixed errors, per-agent bias) as set6 p2 did | Gap noted across 2609.36399 (decision models are near-deterministic), 2610.03935 (overconfident, 89% on the mode vs 35%) and 2609.27535 | A design rule, no cost |
| D4 | **Aggregate vs conjunctive regimes.** The same per-decision error cost 11 pt over a 13-step τ-bench trajectory (2610.03935) and nothing in the school (set6 p2). Test a villager vote near a 50% tipping point and in a landslide | 2610.03935; set6 p2 | Part of the next simulation design |
| D5 | **Code supplies lookahead or simulation; the model only evaluates.** Add a computed consequence field per option | 2610.01834: code lookahead raised ALFWorld solves from 31% to 87%; Jev plays games as if the opponent were random unless code supplies the prediction | Design rule |
| D6 | **Gate only where AUROC is high within the class.** Before any confidence-based review, compute the AUROC of K27's margin within each workload class | 2610.09683: deferral gain ∝ actor AUROC (ρ 0.87) | Offline |
| D7 | **Stress the persona effect only where evidence is ambiguous** | 2609.36399, 2609.37009 | Design rule |

## Cheapest first steps (all offline)

1. Run A1, A2, B4, D1 and D6 on stored records from set3 p2, benchmark p3, set4 and set6 p1.
2. If A1 or A2 separates the W3 missing-evidence cases on held-out data, freeze a threshold and test it once on fresh cases.
3. B1 is the cheapest new-inference test of the key-naming mechanism.
