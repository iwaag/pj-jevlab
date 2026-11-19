# Non-autoregressive decoding and diffusion language models

Items marked (verified) came from fetches/searches this session; others are background knowledge.

## Overview
Autoregressive (AR) LMs factor p(x) left-to-right: one forward pass per token, sequential. Non-autoregressive (NAR) approaches predict many positions at once. Lineage:
1. **NAT for MT** (Gu et al. 2017) and iterative refinement (Mask-Predict, Insertion Transformer): parallel decoding with a conditional-independence approximation ("multi-modality problem").
2. **Speculative decoding / multi-token prediction (Medusa)**: keep AR semantics, draft in parallel, verify.
3. **Discrete diffusion / masked diffusion LMs**: iteratively unmask tokens; bidirectional attention; any-order. Scaled up from 2025 (LLaDA, Dream, Mercury, Gemini Diffusion, DiffusionGemma).
4. **Classification heads** are the degenerate NAR case: output length 1 (or a fixed set of heads), all dependencies handled by a bidirectional encoder.

Jev (undisclosed architecture, "parallel sampler", "all questions answered in one pass", "no text") sits between 3 and 4: a transformer reading one state plus K typed questions and emitting K distributions simultaneously. Since there is no free-form text, the NAR multi-modality problem is mostly avoided if questions are treated as conditionally independent given the state; joint consistency across questions is where a "parallel sampler" would matter (sampling joint outcomes rather than independent marginals).

## Key works
- Gu et al., Non-Autoregressive Neural MT - https://arxiv.org/abs/1711.02281
- Ghazvininejad et al., Mask-Predict - https://arxiv.org/abs/1904.09324
- Leviathan et al., Speculative Decoding - https://arxiv.org/abs/2211.17192 ; Medusa https://arxiv.org/abs/2401.10774
- D3PM (Austin et al.) - https://arxiv.org/abs/2107.03006 ; MDLM (Sahoo et al.) - https://arxiv.org/abs/2406.07524 ; SEDD - https://arxiv.org/abs/2310.16834
- LLaDA (8B masked diffusion LM) - https://arxiv.org/abs/2502.09992 ; LLaDA-MoE https://arxiv.org/abs/2509.24389 (verified)
- Dream 7B - https://arxiv.org/abs/2508.15487
- Block Diffusion (BD3-LM, interpolating AR and diffusion) - https://arxiv.org/abs/2503.09573
- Mercury (Inception Labs; commercial diffusion LLM, 700+ tok/s coding) - https://arxiv.org/abs/2506.17298 (verified)
- Gemini Diffusion (Google DeepMind, experimental demo, May 2025) - https://deepmind.google/models/gemini-diffusion/
- **DiffusionGemma Technical Report** (Google DeepMind) - https://arxiv.org/abs/2608.00146 (verified): open-weight (Apache 2.0) MoE, 25.2B total / 3.8B active, derived from Gemma 4; refines blocks of 256 tokens in parallel; ~1,500 tok/s on one H100; converted from AR with <10% of original training tokens via two-stage SFT+RL.
- Survey: "A Survey on Diffusion Language Models" - https://arxiv.org/abs/2508.10875 (verified) ; curated list https://github.com/AIDASLab/Awesome-Diffusion-LLM (verified)
- Efficient-DLM (AR -> diffusion conversion for speed) - https://arxiv.org/abs/2512.14067 (verified)

## Diffusion-based Jev clones
- OpenJev (razorback16): DiffusionGemma-based - https://github.com/razorback16/openjev (via awesome-jev-alternatives). The Verdict audit cites a 26B DiffusionGemma scoring 88.43% on TypeSafe's external 337-case eval versus 48.07% for the 151M encoder: scale buys a large gain on complex state.
- Von (wfzyx/von): custom non-autoregressive model.
- open-jev-typed-decision-engine (intikhab49): 150M NAR model.

## Differences to keep straight
- Diffusion LMs generate *text* in parallel across positions and need many denoising steps (iterations); latency still depends on output length and step count. Jev's output is typed distributions, so it needs ~one step.
- Diffusion LMs give no calibrated probability by default: per-token marginals at a masked step are not sequence-level probabilities; any-order training makes likelihoods only bounds (ELBO).
- A diffusion LM used as a classifier (read the masked-slot distribution over option tokens in one step) is a legitimate cheap Jev-like readout; this is what a DiffusionGemma clone probably does (verify in repo).
- TypeSafe's "parallel sampler" wording suggests sampling a joint over multiple typed slots in parallel; unclear whether iterative.

## Relevance to Jev-style models
- Gives the architecture family to hypothesize for Jev: bidirectional transformer with typed slot heads, possibly initialized from an AR or diffusion LM (like the AR->diffusion conversions above, cheap at <10% of tokens).
- Experiment: single-step masked-slot readout from LLaDA/Dream/DiffusionGemma vs AR letter-logprob, at matched size, measuring accuracy, ECE, latency, and order sensitivity.
- Bidirectional attention over options removes the causal-order asymmetry that creates position bias in AR MCQ prompts; a testable explanation for improved order-invariance.
- Joint consistency across multiple questions on one state (e.g., Choice and Noul that logically entail each other) is a property AR-per-question baselines lack unless prompts are batched; worth a dedicated metric.
