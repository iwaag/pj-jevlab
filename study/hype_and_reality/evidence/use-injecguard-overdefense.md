# InjecGuard / NotInject: small injection classifiers fire on benign text containing trigger words

- **Sources:** https://arxiv.org/abs/2410.22770 ; PDF https://arxiv.org/pdf/2410.22770 (Li and Liu) (accessed 2026-10-02; locator: Section 3.3, Table 1, Table 7, Figure 5)
- **Evidence type:** peer-reviewed/preprint paper with a new benchmark and model (author evaluation of own model + independent measurement of others' models); author independence: independent of the baseline models' authors, not of InjecGuard
- **Model / base / checkpoint:** baselines Deepset, Fmops, Meta PromptGuard (86M), ProtectAI deberta-v3-base v2, LakeraGuard (API), Llama-Guard-3, Llama-2-chat, GPT-4o; own InjecGuard = DeBERTaV3-base; **size:** InjecGuard/PromptGuard etc. share the same GFLOPs (60.45) per Table 1, exact params not stated in the pages read; Llama-Guard-3 listed as 1418 GFLOPs (8B class, not verified)
- **Task:** binary benign vs injection/jailbreak; **input language:** mostly English (some Chinese/Russian); **rejection mechanism:** binary class
- **Data provenance:** NotInject = 339 LLM-generated benign sentences each containing 1-3 injection "trigger words" (e.g. "ignore"); malicious from PINT and BIPIA; benign from PINT, WildGuard; **metrics:** over-defense accuracy (benign with trigger words classed benign), benign accuracy, malicious accuracy; **raw cases available:** yes (released)
- **Fixed / mitigated?** yes (MOF training); **fix evaluated?** yes, by the authors only

## What the source reports
- Over-defense accuracy (higher = fewer false alarms) in Table 1: Fmops 5.60, Deepset 5.31, PromptGuard 0.88, ProtectAIv2 56.64, LakeraGuard 87.61, GPT-4o 86.73, Llama-Guard-3 99.71.
- Llama-Guard-3 avoids false alarms but catches only 28.28% of malicious inputs; PromptGuard catches 97.10% of malicious inputs but flags ~99% of NotInject benign inputs (Table 1). The paper concludes no existing model is good on all three axes.
- Accuracy drops as trigger words multiply in the open-source guards (Table 7: ProtectAIv2 76.1 / 47.8 / 46.0 on one/two/three trigger words).
- The authors attribute this to lexical shortcut bias on individual words and propose training that down-weights biased tokens (MOF); InjecGuard reports 87.32 over-defense, 77.39 malicious, 83.48 average, vs GPT-4o 86.73 / 79.10 / 85.53 at about 15 ms vs ~7.9 s.

## Strength and caveats
- Supports: trigger-word (lexical) false positives are a documented failure of small encoder classifiers; an LLM (GPT-4o) did not fix the malicious-vs-benign tradeoff by itself; a trained small DeBERTa matched GPT-4o after targeted de-biasing.
- Benign set is LLM-written and short; author-built benchmark may be tuned to its own method. This is the mirror image of local L4 (here a lexical match causes a false alarm; locally it causes false acceptance), so it supports "lexical overlap with label text drives decisions" only by analogy.
- Relevant local classes: L4 (by analogy), L6; Q1, Q2, Q3.
