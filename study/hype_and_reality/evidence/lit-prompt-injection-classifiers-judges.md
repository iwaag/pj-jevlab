# Prompt injection against LLM classifiers and judges, and size effects (L4, Q1, Q4)

- **Sources:** https://arxiv.org/abs/2504.18333 (Maloyan & Namiot 2025, adversarial attacks on LLM-as-a-judge; success-rate table); https://arxiv.org/abs/2505.13348 (Maloyan, Ashinov, Namiot; judge architectures); https://arxiv.org/abs/2511.21752 (Li & Shan, Label Disguise Defense, class-directive injection in sentiment classification); https://arxiv.org/abs/2605.29491 (Su et al., DistractionIF, 2026-05-28) (accessed 2026-10-02; via WebFetch summaries)
- **Evidence type:** peer-reviewed/preprint paper (all four preprints; venue unknown); author independence: yes
- **Model / base / checkpoint:** 2504.18333: Gemma-3-27B-Instruct, Gemma-3-4B-Instruct, Llama-3.2-3B-Instruct, GPT-4, Claude-3-Opus; 2505.13348: Qwen2.5-3B-Instruct, Falcon3-3B-Instruct only; 2511.21752: 14 LLMs (names and sizes unknown to me); 2605.29491: Qwen3 0.6B-235B, DeepSeek v3.2, Kimi-k2, GPT-5.1 series, Gemini-3-Pro; **size:** as listed (verified from fetched text where given); **architecture:** decoders
- **Task:** pairwise judging (MT-Bench human judgments), sentiment classification, instruction-laden reference text; **language:** English; **readout:** generated verdict; **rejection mechanism:** none
- **Data provenance:** MT-Bench judgments; sentiment datasets; synthetic DistractionIF; **metrics:** attack success rate (ASR), pass rate; **raw cases available:** unknown
- **Fixed / mitigated?** Label Disguise Defense (obfuscating label semantics); GRPO training recovers up to 15.5% on DistractionIF; **fix evaluated?** yes (author-evaluated)
- **Relevant local classes:** L4, Q1, Q2, Q4

## What the source reports
- 2504.18333: basic injection ASR 57.5% (Gemma-27B), 66.7% (Gemma-4B), 60.1% (Llama-3B), 32.4% (GPT-4), 29.8% (Claude-3-Opus); the strongest adaptive attack reached 42.9-73.8%. Frontier models are about 25-30 points more resistant, but nowhere near immune. The 27B vs 4B Gemma difference is small for the adaptive/contextual attacks (67.7 vs 67.4 for contextual misdirection).
- 2505.13348: attacks on two 3B judges work (best 31-32% ASR), but no size comparison is made, so no scale claim.
- 2511.21752: "class-directive injection" (injected text telling the classifier which label to output) is a named attack on LLM classifiers; its defense disguises label names. The abstract confirms the attack and defense; the direction of the size trend I could not confirm (unverified).
- 2605.29491 (preprint, 2026): inverse scaling; Qwen3 pass rate drops from about 66.0% (0.6B) to 37.6% (235B-A22B) on benign instruction-like noise embedded in reference text, because larger models follow embedded instructions more. Counterexample to "bigger resists injection".
- Together: size helps in the frontier-vs-small-open comparison but is non-monotonic, and instruction-following strength can increase injection susceptibility.

## Strength and caveats
- Supports that text naming the desired label is a known, documented attack class on classifiers/judges (L4), not unique to jeff, and that scale alone is not a reliable fix.
- None is an encoder zero-shot classifier. In jeff the mechanism is likely lexical match (see lit-nli-zeroshot-lexical-overlap), not instruction following; do not conflate.
- The two Maloyan papers are by overlapping authors; the table values came through a summarising fetch tool and should be checked against the paper before quoting. DistractionIF's metric is judge-scored by GPT-4o and uses benign noise, not malicious overrides.
