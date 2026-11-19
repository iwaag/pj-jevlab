# 41 open-weight LLMs on zero-shot intent classification (135M-9B)

- **Sources:** https://arxiv.org/abs/2607.27421 (Ganesh, Dozier, Seals; Auburn; v1 29 Jul 2026), PDF text at https://arxiv.org/pdf/2607.27421 (accessed 2026-10-02; locators: Abstract, "Overall Model Rankings", "Instruction Tuning vs. Parameter Scale", "Benchmark Saturation Analysis")
- **Evidence type:** preprint paper (not peer reviewed as far as checked); independent of Jev
- **Model / base / checkpoint:** 41 LLMs across 15 families, 135M-9B (e.g. Mistral-7B-Instruct-v0.3, Qwen2.5-3B-Instruct); **architecture:** decoder LLMs, free-text generation, exact match, no constrained decoding; vLLM, V100
- **Task:** single-label intent classification on CLINC150, Banking77, SNIPS, MASSIVE, MTOP, and HINT3 Curekart/Powerplay11/Sofmattress; first 500 test examples (HINT3 full sets: 459/309/253); **rejection mechanism:** none described; OOS handling unclear from the text read (the HINT3 test sizes quoted appear to be in-scope only, unverified)
- **metrics:** exact-match accuracy, ECE; **raw cases:** supplementary, not inspected

## What the source reports
- Best 8-dataset zero-shot aggregate is 0.660 (Mistral-7B-Instruct-v0.3); a 3B instruct model (0.632) beats several 7B base models; instruction tuning raised the aggregate in all six matched pairs (+0.012 to +0.095); only one sub-3B model exceeded 0.5.
- No model exceeds 80% on Banking77, MASSIVE, MTOP, or the three real HINT3 sets; best on Powerplay11 is 53.7%. SNIPS (7 intents) is saturated (32/41 exceed 80%).

## Strength and caveats
- Supports: size is a weaker predictor than instruction tuning at sub-9B; real chatbot-derived label sets stay hard even for 7-9B models zero-shot (no rescue by scale); small label spaces make everything look good.
- Does not evaluate OOS rejection or adversarial text, so it speaks to Q1/Q4 only for in-scope accuracy.
- Relevant local classes: L5/L6 (not measured here); Q1, Q4, Q8.
