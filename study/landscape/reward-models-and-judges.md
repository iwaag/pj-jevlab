# Reward models, LLM judges, and guard classifiers as "typed decision" ancestors

Items marked (verified) came from search results this session; others are background knowledge.

## Overview
Models that return a *decision with a score* rather than prose are not new; they exist wherever downstream code must branch:
- **Reward models (RMs)**: LM backbone + scalar head trained with Bradley-Terry on preference pairs (InstructGPT). Output is a Score with arbitrary scale and, notably, not a calibrated probability.
- **Generative RMs / verifiers / LLM-as-judge**: prompt an LLM for a verdict; "P(Yes)" or expected rating from token logprobs gives a probability (G-Eval, Generative Verifiers). Position and verbosity biases are well documented.
- **Guard / moderation classifiers**: decoder LLMs fine-tuned to output "safe/unsafe + category" (Choice + Noul) with probability read off the first token. They are the most direct product-level precedent: fixed schema, single short output, threshold-based routing.
- **Encoder guard models** (e.g., GLiNER Guard, PromptGuard, ModernBERT-based detectors) show the encoder route at ~10 ms.
Jev generalizes these: arbitrary user-defined typed questions (Choice/Score/Noul) over arbitrary state, with calibration as a first-class training objective.

## Key works
Reward models and judges
- InstructGPT (RM + RLHF) - https://arxiv.org/abs/2203.02155
- RewardBench - https://arxiv.org/abs/2403.13787 ; RewardBench 2 - https://arxiv.org/abs/2506.01937
- Zheng et al., Judging LLM-as-a-Judge (MT-Bench) - https://arxiv.org/abs/2306.05685
- Generative Verifiers (reward modeling as next-token prediction) - https://arxiv.org/abs/2408.15240
- G-Eval (logprob-weighted scores) - https://arxiv.org/abs/2303.16634
- Prometheus 2 (open judge LM) - https://arxiv.org/abs/2405.01535
- Skywork-Reward / ArmoRM (multi-objective RM) - https://arxiv.org/abs/2406.12845
- Calibration of RMs/judges is an open gap; RLCR-style Brier rewards (https://arxiv.org/abs/2507.16806, verified) are the training analogue.

Guard / moderation classifiers
- Llama Guard (original) - https://arxiv.org/abs/2312.06674 ; Llama Guard 3-1B-INT4 - https://arxiv.org/abs/2411.17713 (verified) ; Llama Guard 4 (12B multimodal, derived from Llama 4 Scout; verified via search)
- ShieldGemma - https://arxiv.org/abs/2407.21772 (4 harm categories; scores via P(Yes) of "violates policy?")
- WildGuard - https://arxiv.org/abs/2406.18495
- Qwen3Guard Technical Report - https://arxiv.org/abs/2510.14276 (verified)
- AprielGuard - https://arxiv.org/abs/2512.20293 (verified); GuardReasoner-Omni https://arxiv.org/abs/2602.03328 (verified); X-Guard https://arxiv.org/abs/2504.08848 (verified)
- Constitutional Classifiers - https://arxiv.org/abs/2501.18837
- GLiNER Guard (encoder family for safety/privacy) - https://arxiv.org/abs/2605.05277 (verified, search hit)
- Benchmarking open-source guard models - https://arxiv.org/abs/2605.28830 (verified); robustness against adversarial attacks https://arxiv.org/abs/2511.22047 (verified)
- LatentGuard / "LLM Safety From Within" (probe internal representations) - https://arxiv.org/abs/2608.03838 and https://arxiv.org/abs/2604.18519 (verified) - linear probes as cheap typed heads.

## Jev-relevant parallels
- Guard models use exactly the "first-token Yes/No logit -> probability -> threshold" pattern; Jev's Noul is that primitive with calibration training and a faster architecture.
- Reward-model overoptimization (Gao et al. https://arxiv.org/abs/2210.10760) is the analogue of Jev-style models being used as RL verifiers: a poorly calibrated or gameable typed decision model is a bad reward.
- Guard benchmarks repeatedly show brittleness to paraphrase and adversarial rewrites - consistent with clone audits (Verdict: abstention recall 75.5% -> 18% under hard-negative siblings; 10% on held-out synonyms).
- Probing/linear-head work shows a small head on frozen hidden states is often enough for binary decisions; clones CLM/SemIf (frozen encoder plus small heads) take this route.

## Relevance to Jev-style models
- Natural evaluation suites: RewardBench (pairwise Choice), JudgeBench / MT-Bench agreement (Score), ToxicChat / OpenAI-moderation / WildGuardTest / Aegis (Noul), with ECE and abstention added; few of these report calibration.
- Position-bias and verbosity-bias tests from the LLM-judge literature map onto option-order and label-length tests that clone authors already run.
- A Jev-style model can serve as a fast pre-filter / router in front of heavier judges or guards (cascade: Noul probability gate -> escalate uncertain cases), with conformal thresholds for coverage guarantees (see calibration.md).
- Open question: do typed-decision models trained on synthetic data inherit generator-LLM judging biases? Compare to human-labeled sets.
