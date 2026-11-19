# Calibration, abstention, and RL for calibration

Items marked (verified) were returned by search this session; others are background knowledge.

## Overview
A classifier is calibrated if, among predictions with confidence p, a fraction p are correct. For Jev, calibration is a headline feature ("higher confidence should mean higher accuracy, and similar inputs should return similar answers" - RLCD). Standard toolkit:
- **Metrics**: ECE (binned; sensitive to bin scheme - equal-width vs equal-mass), MCE, adaptive/classwise ECE, **Brier score** (proper, decomposes into calibration + refinement), **log loss / NLL** (proper, punishes confident errors), reliability diagrams, AUROC of confidence for error detection, selective-prediction risk-coverage curves.
- **Post-hoc**: temperature scaling (Guo et al.), vector/matrix scaling, Platt, isotonic, histogram binning, Dirichlet calibration; contextual/batch calibration for prompts.
- **Distribution-free guarantees**: conformal prediction (prediction sets with coverage 1-alpha), selective classification / abstention.
- **Training-time**: label smoothing, focal loss, proper scoring rule losses (Brier), RL with proper-scoring rewards.

## Key works
- Guo et al. 2017, "On Calibration of Modern Neural Networks" (temperature scaling, ECE) - https://arxiv.org/abs/1706.04599
- Brier 1950; Gneiting & Raftery 2007, strictly proper scoring rules (JASA) - theoretical basis for why Brier/log-score rewards induce honest probabilities.
- Minderer et al. 2021, "Revisiting the Calibration of Modern Neural Networks" - https://arxiv.org/abs/2106.07998
- Angelopoulos & Bates, "A Gentle Introduction to Conformal Prediction" - https://arxiv.org/abs/2107.07511 ; MAPIE https://github.com/scikit-learn-contrib/MAPIE
- Quach et al., "Conformal Language Modeling" - https://arxiv.org/abs/2306.10193
- Geifman & El-Yaniv, "Selective Classification for Deep Neural Networks" - https://arxiv.org/abs/1705.08500
- Kadavath et al. 2022 - https://arxiv.org/abs/2207.05221 ; OpenAI GPT-4 report (RLHF hurts calibration) - https://arxiv.org/abs/2303.08774
- **RLCR**: Damani et al. 2025, "Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty" - https://arxiv.org/abs/2507.16806 (verified). Reward = correctness + Brier term -(q - 1[correct])^2 on a verbalized confidence q; proven that it jointly incentivizes accuracy and calibration; RLVR with binary reward degrades calibration, RLCR improves it, and confidence can be used for test-time weighting.
- Decoupling reasoning and confidence in RLVR - https://arxiv.org/abs/2603.09117 (verified, search hit)
- Reward-function comparison for RL confidence calibration - https://arxiv.org/abs/2607.04332 (verified, search hit)
- Process supervision of confidence margin - https://arxiv.org/abs/2604.23333 (verified, search hit)
- Linguistic calibration of LLMs (RL, forecasts) - https://arxiv.org/abs/2404.00474
- Verbalized confidence / teaching models to express uncertainty (Lin et al. 2022) - https://arxiv.org/abs/2205.14334
- Reaching Beyond the Mode: RL for distributional reasoning - https://arxiv.org/abs/2603.24844 (verified, search hit) - related to "mode dropping" that TypeSafe cites.
- Tools: net:cal https://github.com/EFS-OpenSource/calibration-framework ; temperature_scaling https://github.com/gpleiss/temperature_scaling (both via awesome-jev-alternatives).

## RLCD vs prior art
TypeSafe describes RLCD as RL for "calibrated decisions": calibration (confidence matches accuracy) plus *consistency* (similar inputs -> similar answers) and anti-mode-dropping (preserve distributional spread). Details are undisclosed. Closest public analogues:
- RLCR: same idea (proper scoring-rule reward), but on verbalized confidence after chain-of-thought. RLCD plausibly rewards the output *distribution itself* (log score or Brier on the typed probability head), which can be done in one pass without generation; with a closed output space the "RL" can degenerate to supervised proper-scoring-rule training (expected-reward gradient is exactly computable), so whether RL is needed at all is an open question worth testing.
- Clone interpretation (Verdict, Laya): loss = CE + 1.0 x Brier, then L-BFGS temperature scaling per (type, option count). This is *not* RL; "RLCD" naming in clones is borrowed. Verdict reports ECE 2.87% (equal-mass) on in-distribution test, but ECE 0.298 -> 0.118 on a hard tier and abstention recall collapsing from 75.5% to 18% under hard-negative siblings: calibration is distribution-shift fragile.
- Laya ships temperatures clamped to [0.5, 5.0] and states checkpoints are over-confident out of the box.

## Relevance to Jev-style models
- Evaluation plan: report ECE (both equal-width and equal-mass, 10-15 bins), Brier, NLL, reliability diagrams, risk-coverage curves, and calibration *under shift* (paraphrase, option reorder, added distractors). Single in-distribution ECE is easy to game.
- Test the "RLCD is just proper-scoring-rule training + temperature scaling" hypothesis: train identical heads with (a) CE, (b) CE+Brier, (c) log score + TS, (d) a policy-gradient variant, and compare.
- Consistency property: measure answer/probability variance across paraphrases and option permutations; this is separate from ECE.
- Conformal prediction on top of Jev probabilities gives guaranteed-coverage option sets and a principled abstain/escalate rule; a cheap add-on for hosted-only black-box APIs.
- Beware proper-scoring-rule training on synthetic labels: calibrated w.r.t. the synthetic label distribution, not real-world frequencies.
