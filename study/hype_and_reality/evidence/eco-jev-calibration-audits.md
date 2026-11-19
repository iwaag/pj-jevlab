# Jev calibration and selective-risk audits (jev-baselines-eval, ood-calibration, Sophos)

- **Sources (accessed 2026-10-02):** https://github.com/ickma2311/jev-baselines-eval (README tables); https://github.com/scienthoon/jev-ood-calibration (README headline table); https://www.sophos.com/en-us/blog/jevs-paradox-hidden-cost-of-cheap-ai-decisions (seen only through a search result snippet; the page was not fetched, so figures about it are second-hand).
- **Evidence type:** independent evaluations; independence: yes (Sophos blog authorship/vendor relation unknown).
- **Model:** Jev 1.13.0 hosted; size unknown. Comparators: gpt-5.4-nano, GPT-5.6 Terra, bge-small + logistic regression.
- **Task:** Banking77 (n=208), CLINC150 (n=200) zero-shot; OpenBookQA/CommonsenseQA/HellaSwag (3,721 items) and 900 synthetic tickets; **input language:** English; **rejection mechanism:** confidence only.
- **Data provenance:** public benchmarks plus synthetic; **metrics:** accuracy, ECE, AUROC for error ranking; **configuration:** gateway, default; **raw cases available:** yes per READMEs.
- **Fixed / mitigated?** n/a. **fix evaluated?** n/a.
- **Relevant local classes:** L8 (confidence does not separate costly errors); Q4, Q5.

## What the sources report
- Accuracy: Banking77 Jev 0.832 vs nano 0.793, Terra 0.875, supervised encoder 0.933; CLINC150 Jev 0.870 vs 0.795 vs 0.915.
- Error-ranking AUROC: Banking77 Jev 0.853 vs 0.795; CLINC150 Jev 0.734 vs nano 0.816; the study calls neither direction established.
- Public benchmarks likely in training mix show ECE 0.024-0.032; on unseen synthetic tickets overall ECE is 0.107, wrong queue answers often receive 1.00, and a later correction showed the refit-temperature figures depended on how exact zeros were floored.
- Sophos snippet: confidence 1.0 on 102/200 CLINC150 answers, 6 wrong; this matches the ickma2311 data (same n=200), so it likely cites that study.

## Strength and caveats
- Gives a quantified analogue of the local "margin does not separate errors" finding for the hosted model (AUROC 0.73 here vs 0.73 locally, coincidentally comparable but different tasks and metrics).
- Sophos is unverified beyond the snippet.
