# HINT3: real chatbot traffic exposes OOS and spurious-pattern failures across NLU platforms and BERT

- **Sources:** https://arxiv.org/abs/2009.13833 ; PDF text https://arxiv.org/pdf/2009.13833 (Arora, Jain, Chaturvedi, Modi; EMNLP 2020 Insights workshop) (accessed 2026-10-02; locator: Table 2, Section 4.1, Table 3, Table 5, Figure 2)
- **Evidence type:** peer-reviewed/preprint paper (authors from a chatbot vendor, Haptik, one of the evaluated platforms); author independence: independent of Jev-likes; partly not independent of Haptik platform
- **Model / base / checkpoint:** Dialogflow, LUIS, Rasa, Haptik, fine-tuned BERT; **size:** unknown; **training:** 180-413 (Subset) or 328-600 (Full) train queries per dataset
- **Task:** intent detection on 3 real e-commerce/gaming bot datasets with in-scope and out-of-scope test queries; **input language:** English incl. slang, typos, code-mixing; **options / readout:** 21-59 intents; **rejection mechanism:** probability threshold 0.1-0.9 swept
- **Data provenance:** real user first messages to live bots, annotated; **n:** test in-scope/oos = SOFMattress 231/166, Curekart 452/539, Powerplay11 275/708 (Table 2); **metrics:** accuracy, Matthews correlation, OOS recall; **raw cases available:** yes (open-sourced datasets)
- **Fixed / mitigated?** no; **fix evaluated?** no

## What the source reports
- Even at a very low threshold (0.1, where OOS false positives would not matter) in-scope accuracy on Full training data is far below the 90%+ reported on CLINC150 (Table 3; exact values not transcribed here).
- Dropping semantically redundant training queries (Subset) cut in-scope accuracy by up to 22.3% (BERT, SOFMattress) (Table 5), which the authors read as spurious-pattern learning.
- A significant share of OOS queries get high confidence on all platforms except LUIS, where OOS recall comes at the cost of in-scope accuracy (Figure 2 discussion).
- Example failures (Table 4) are near-neighbour confusions between product intents that all platforms share.

## Strength and caveats
- Supports: confidence-threshold rejection fails on realistic off-topic traffic for supervised classifiers too, not just zero-shot ones; synthetic/crowdsourced benchmarks overstate performance.
- Caveat: small training sets, 2020 models; per-cell numbers not extracted (read only text of Tables 2 and 5, Figure not inspected).
- Relevant local classes: L2, L3, L6; Q7 (real vs written inputs), Q5.
