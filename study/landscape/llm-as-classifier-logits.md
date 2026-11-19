# LLM as classifier via option-token logits

Items marked (verified) were fetched this session; others are from background knowledge, spot-check IDs before citing.

## Overview
The most common "poor man's Jev" is: put the options in a prompt as letters/numbers (A/B/C...), run **one** forward pass, read the next-token logprobs restricted to the option tokens, softmax them. This gives a categorical distribution without generation. Variants:
- **Option-token scoring (MCQ / "cloze" vs "symbol" formats)**: read logprobs of "A", "B"... (Robinson & Wingate).
- **Sequence likelihood scoring**: score each full option string; needs length normalization (per-token mean, as in GPT-3) or PMI/domain-conditional normalization (Holtzman) because of "surface form competition".
- **Yes/No logit for binary**: P(yes) / (P(yes)+P(no)); standard in LLM-judge and reward-by-logit setups.
- **Verbalized confidence**: model writes "Confidence: 85%". Often poorly calibrated, but RL-trained variants (see calibration.md) can fix it. Costs autoregressive tokens.
Known weaknesses: position/selection bias, label-token priors, overconfidence after RLHF, sensitivity to option order. All visible in clone audits (Verdict: 4.5% flips on reorder; OpenJev claims "100% option-order invariance" via permutation averaging).

## Key works
- Robinson & Wingate 2022, "Leveraging LLMs for Multiple Choice Question Answering" - https://arxiv.org/abs/2210.12353 - symbol-binding (MCSB) vs cloze scoring.
- Holtzman et al. 2021, "Surface Form Competition: Why the Highest Probability Answer Isn't Always Right" - https://arxiv.org/abs/2104.08315 - PMI_DC scoring.
- Zhao et al. 2021, "Calibrate Before Use" (contextual calibration) - https://arxiv.org/abs/2102.09690 - estimate bias with content-free input ("N/A"), divide it out.
- Batch Calibration (Zhou et al. 2023) - https://arxiv.org/abs/2309.17249 - estimate contextual bias from the batch mean; unsupervised, zero-shot and ICL.
- Min et al. 2022, noisy channel prompting - https://arxiv.org/abs/2108.04106 - score P(input | label) instead.
- Zheng et al. 2023, "LLMs Are Not Robust Multiple Choice Selectors" (PriDe debiasing for selection bias) - https://arxiv.org/abs/2309.03882
- Kadavath et al. 2022, "Language Models (Mostly) Know What They Know" (P(True), P(IK)) - https://arxiv.org/abs/2207.05221 - base models are well calibrated on MCQ logits; RLHF damages it.
- Tian et al. 2023, "Just Ask for Calibration" (verbalized beats token probs for RLHF models) - https://arxiv.org/abs/2305.14975
- Xiong et al. 2023, "Can LLMs Express Their Uncertainty?" - https://arxiv.org/abs/2306.13063
- OpenAI GPT-4 technical report calibration figure (pretrained calibrated, post-trained not) - https://arxiv.org/abs/2303.08774
- Zheng et al. 2023, MT-Bench / LLM-as-judge (position bias, logprob-weighted scores) - https://arxiv.org/abs/2306.05685
- G-Eval (probability-weighted scoring of 1-5 ratings) - https://arxiv.org/abs/2303.16634 - exactly a "Score" primitive via expected value over level tokens.

## Clones / repos using this route (verified via awesome-jev-alternatives)
- Allan Boll, "A Jev-like wrapper for LLMs including llama.cpp" - letter-logprob wrapper: https://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html
- decider (Qwen3.5 0.8B-35B), Kev (Qwen3.5/3.8), NanoJev (Qwen3-0.6B), openjev/daseinlabs (Gemma 3 4B), JEV-CPU (GGUF), OpenJev zhangcy122 (open LLMs + Laya, logprob calibration + permutation invariance).
- Calibrated confidence demo (score distribution from logprobs): https://github.com/WestdeutscherRundfunkKoeln/calibrated-confidence-demo

## Why this differs from Jev
- Still one decoder forward pass per *question* (or per option-order permutation); Jev claims all questions answered in a single pass over a shared state. Prefix/KV caching of the state narrows the gap: SCX Router (https://arxiv.org/abs/2609.02292, search hit) uses a decoder-KV classifier for exactly this.
- Probabilities from logits are a by-product of a language-modeling objective, not trained to be calibrated; they need post-hoc temperature/contextual calibration.
- Score primitive: expected value over level-token probabilities (G-Eval) is a natural implementation but is not guaranteed ordinal-consistent.

## Relevance to Jev-style models
- Gives the strongest cheap baseline for lab evaluation: same decoder, same state, letter-logprob readout, plus contextual/batch calibration and temperature scaling. If Jev cannot beat this at equal latency, its architecture claim is weak.
- Order-invariance test: permute options, compare flips (Verdict reports 4.5%). Permutation averaging (PriDe-style) costs k passes.
- Measure RLHF-vs-base calibration gap: Kadavath/GPT-4 evidence suggests the base checkpoint is the better logit classifier; RLCD-like training is aimed at fixing this for post-trained models.
- Verbalized confidence is irrelevant to Jev's latency budget but is a useful *contrast* arm.
