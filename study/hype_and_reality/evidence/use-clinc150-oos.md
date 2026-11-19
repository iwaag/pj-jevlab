# CLINC150 / "oos-eval": early benchmark showing out-of-scope rejection lags in-scope accuracy

- **Sources:** https://arxiv.org/abs/1909.02027 ; https://aclanthology.org/D19-1131/ (Larson et al., EMNLP-IJCNLP 2019); numbers read from the PDF text at https://arxiv.org/pdf/1909.02027 (accessed 2026-10-02; locator: Table 2, Table 3, Section 3.3 "Metrics", dataset section)
- **Evidence type:** peer-reviewed/preprint paper; author independence: independent of any Jev-like model (predates them)
- **Model / base / checkpoint:** FastText, SVM, CNN, MLP, BERT (fine-tuned), Google DialogFlow, Rasa NLU (spacy-sklearn); **size:** unknown per model (BERT variant size not checked); **architecture:** supervised intent classifiers; **training:** 100 queries/intent in "Full" (plus Small / Imbalanced / OOS+ variants)
- **Task:** 150-intent classification plus detecting out-of-scope (OOS) queries; **input language:** English; **options / readout:** closed set of 150 intents; **rejection mechanism:** compared (a) oos-train (extra OOS class), (b) oos-threshold (confidence threshold chosen on validation), (c) oos-binary
- **Data provenance:** crowdsourced; 22,500 in-scope + 1,200 OOS queries (1,000 OOS in test); only ~69% of prompts targeting OOS yielded valid OOS queries (so OOS is hard to author even for humans)
- **n:** test in-scope 4,500 (from dataset design, not re-verified here), OOS 1,000; **metrics:** in-scope accuracy and OOS recall; **configuration:** as above; **raw cases available:** yes (dataset public at github.com/clinc/oos-eval)
- **Fixed / mitigated?** Partly: adding more OOS training data (OOS+) raises recall; **fix evaluated?** yes, in the same tables

## What the source reports
- Fine-tuned BERT gets about 96-97% in-scope accuracy in every condition, but OOS recall is far lower: 40.3% (Full, oos-train), 59.2% (OOS+); threshold variant 52.3% (Full) (Table 2).
- Best OOS recall anywhere in Table 2 is 66.0% (Rasa, OOS+); the abstract says no system exceeded 66%.
- Threshold-based rejection was erratic for several models (Rasa 31.2% -> 1.0% -> 0.0% across Full/Small/Imbalanced; SVM 0.0% on Imbalanced).
- Adding training OOS examples helps recall but it "remains low relative to in-scope accuracy"; the authors argue false acceptance of OOS (a wrong answer) is worse than false rejection (a "try again" fallback) and therefore use recall (Section 3.3).
- A separate binary in/out classifier (oos-binary, Table 3) did not fix it (BERT OOS recall 46.5%).

## Strength and caveats
- Supports: the in-scope accuracy figure that vendors/benchmarks quote says little about rejection of out-of-scope text; BERT-size supervised encoders accepted a majority of crowdsourced OOS queries at the default operating point.
- OOS here is crowdsourced, same style as in-scope, topically "near" the domains (hard negatives). Not adversarial and not instruction-override text.
- Dated (2019 models); no LLMs or zero-shot encoders. Larger pre-trained models (BERT vs CNN) did not reliably give better OOS recall, but this is one family comparison.
- Relevant local classes: L1-L3 (rejection lag), L8; Q1, Q5 (threshold vs explicit OOS class), Q7.
