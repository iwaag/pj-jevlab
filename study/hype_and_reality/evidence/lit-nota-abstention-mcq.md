# "None of the above" options and missing-answer behaviour in LLM multiple choice (L2, L3, Q1, Q5)

- **Sources:** https://arxiv.org/abs/2503.01550 (Tam, Wu, Lin, Chen; Section 5.1, Table 4, Appendix C); https://arxiv.org/abs/2409.00113 (Goral, Wisnios, Sankowski, Budzianowski; "Wait, that's not an option"; abstract/results) (accessed 2026-10-02; details via WebFetch summaries of HTML/PDF, numbers not independently re-checked in tables)
- **Evidence type:** peer-reviewed/preprint paper (first appears in ACL Findings 2025 per search result https://aclanthology.org/2025.findings-acl.1031.pdf); author independence: yes
- **Model / base / checkpoint:** 28 LLMs, 1.5B to 671B (19 open, 9 closed incl. DeepSeek-V3, Gemini 1.5 Pro) in Tam et al.; Llama 3, Qwen 2.5, DeepSeek-Math sizes in Goral et al. (exact sizes: unknown); **architecture:** decoders; **training:** instruction-tuned
- **Task:** MMLU with the correct option replaced by "None of the above" (Tam); removal of correct option (Goral); **language:** English; **options / readout:** generated answer / letter; **rejection mechanism:** NOTA as an explicit option
- **Data provenance:** MMLU, 352 of 14,042 questions already carrying NOTA options for the natural analysis; **metrics:** accuracy; **raw cases available:** unknown
- **Fixed / mitigated?** Tam: SFT 28.5 -> 52.3, DPO 28.5 -> 57.7 on NOTA-as-answer; **fix evaluated?** yes, GPQA transfer limited
- **Relevant local classes:** L2, L3, Q1, Q5

## What the source reports
- When "None of the above" is the correct answer, accuracy falls 30-50% across models "regardless of scale"; DeepSeek-V3 90.8 -> 65.7, Gemini 1.5 Pro 90.1 -> 60.3 (Tam, Section 5.1).
- Models tend to pick a plausible listed option rather than the NOTA/abstain option even when they know the content, the same shape as L3 (unavailable action -> neighbour).
- Goral et al.: when the right option is removed models usually still choose from the remaining wrong options; larger models are somewhat more robust but remain vulnerable (summary-level; no numbers extracted).
- Fine-tuning on NOTA data helps (SFT/DPO) but does not close the gap, relevant to Q3 (training matters, not only size).

## Strength and caveats
- Strong, multi-model, independent evidence that forced choice with a "none" option is a hard shape for LLMs and does not reliably improve with scale up to 671B.
- Tasks are knowledge MCQ, not intent routing with a `clarify` option; transfer to Blackout Dispatch is by analogy.
- Both papers are decoder LLMs. Nothing here about encoder zero-shot classifiers.
