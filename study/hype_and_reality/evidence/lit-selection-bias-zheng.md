# Selection bias in multiple-choice LLMs: Zheng et al. and companions (L5, L6)

- **Sources:** https://arxiv.org/abs/2309.03882 (Zheng, Zhou, Meng, Zhou, Huang; Table 3, 0-shot MMLU; section on PriDe); https://arxiv.org/abs/2308.11483 (Pezeshkpour & Hruschka; abstract); https://arxiv.org/abs/2406.03009 (Wei, Wu, Huang, Chen; abstract/results) (accessed 2026-10-02; figures extracted via WebFetch of the arXiv HTML pages, not read from a PDF directly)
- **Evidence type:** peer-reviewed/preprint paper (3 papers); author independence: yes (unrelated to Jev/jeff)
- **Model / base / checkpoint:** 20 decoder LLMs in Zheng (Llama 7B-65B, Llama-2 7B/13B/70B, Vicuna 7B-33B, Falcon 7B/40B, gpt-3.5-turbo); Wei et al.: PaLM 2, Gemini Pro, gpt-3.5, Llama-2 7B/13B/70B; **size:** as listed (verified from fetched paper text); **architecture:** autoregressive decoders, not encoders; **training:** base and chat variants
- **Task:** MMLU/ARC/CSQA multiple choice with letter IDs (A/B/C/D); **input language:** English; **options / readout:** option-ID token probability; **rejection mechanism:** none
- **Data provenance:** public benchmarks; **n:** benchmark-sized; **metrics:** RStd (std of per-option recall), accuracy; **configuration:** 0-shot and few-shot; **raw cases available:** partial
- **Fixed / mitigated?** PriDe (permutation-estimated prior) debiasing; **fix evaluated?** yes (MMLU +2.6, ARC +2.9, CSQA +4.0 accuracy at 5% estimation cost, per fetched summary)
- **Relevant local classes:** L5, L4 (partly), Q8

## What the source reports
- Zheng et al. attribute selection bias mainly to token bias: models give prior mass to particular option-ID tokens (A/B/...), with position bias "present but irregular".
- Table 3 (0-shot MMLU) RStd, default option IDs: Llama-2 7B 23.0, 13B 7.5, 70B 4.1; Llama 7B 18.5, 13B 17.4, 30B 8.5, 65B 8.3; Vicuna-1.3 7B 5.3, 13B 10.5, 33B 8.2. So bias shrinks with size in the Llama/Llama-2 lines but is non-monotonic for Vicuna; the authors themselves say no consistent pattern within a family.
- Removing option IDs (cloze-style scoring) lowered RStd for most small models (Llama-13B 17.4 -> 2.6) but not all (Llama-2-13B 7.5 -> 9.6).
- Pezeshkpour & Hruschka: reordering options changes accuracy by roughly 13% to 75% across benchmarks; sensitivity arises when the model is uncertain between its top-2/3 options.
- Wei et al.: stronger commercial models were more order-sensitive than token-sensitive; Llama-2 sizes show inconsistent patterns; sensitivity is lower on easy questions.

## Strength and caveats
- Supports "order sensitivity exists in LLMs and is largest in small ones" (Llama/Llama-2), consistent with L5 (17-27% top-1 flips) as a general phenomenon, not a jeff quirk. Does NOT show it for encoder NLI/GLiClass readouts.
- Scale evidence is mixed: monotone in Llama-2, non-monotone for Vicuna and in Wei et al. Do not claim "scale fixes it".
- The Zheng mitigation (cloze-style / removing IDs) is relevant to Q2 only by analogy: here the bias is on ID tokens, not on keys appearing in input.
- Wide ranges in the Pezeshkpour abstract (13%-75%) depend on benchmark and model; not verified per model.
