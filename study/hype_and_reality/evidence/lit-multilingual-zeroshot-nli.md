# Multilingual / non-English degradation for zero-shot NLI classifiers (L9, Q1)

- **Sources:** https://arxiv.org/abs/2402.03223 (Bareiss, Klinger, Barnes, "English Prompts are Better for NLI-based Zero-Shot Emotion Classification than Target-Language Prompts"); https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli (model card, search hit only; the Japanese 0.530 vs English 0.537 average-score figure came from a search-result snippet of a third-party mirror and is unverified) (accessed 2026-10-02)
- **Evidence type:** peer-reviewed/preprint paper; author independence: yes
- **Model / base / checkpoint:** XLM-RoBERTa-large, MiniLMv2, Ernie, XLM-V, mDeBERTa, mDeBERTa-TS (all NLI-tuned multilingual); **size:** unknown (not extracted); **architecture:** encoder cross-encoders
- **Task:** NLI-based zero-shot emotion classification on 18 languages; **language:** 18 non-Japanese languages (Japanese not included, confirmed from the fetched language list); **options / readout:** entailment of English or translated hypothesis
- **Data provenance:** Universal Joy, EmoEvent, de/enISEAR; **metrics:** F1
- **Relevant local classes:** L9, Q1

## What the source reports
- English prompts (hypotheses) outperformed target-language prompts for non-English inputs in all 18 languages, mildly (Universal Joy average F1 advantage 0.025). This matches the local L9 result that JA text + EN options (13/18) beat JA + JA (5/18).
- A search snippet reports a large gap between high- and low-resource languages for NLI zero-shot (best about 96% English versus about 36% Somali); source not opened, unverified.

## Strength and caveats
- Supports the local "English options on foreign text" workaround direction only; does not test Japanese, GLiClass, or GLiFormer. Evidence for Japanese specifically: none found (gap). The local 18-pair probe is too small to compare.
