# Entailment-based zero-shot classifiers: lexical overlap, label-name sensitivity, calibration (L4, L1, Q2)

- **Sources:** https://aclanthology.org/2021.acl-short.99/ (Ma, Yao, Lin, Zhao, ACL-IJCNLP 2021 short, pp. 786-796); https://arxiv.org/abs/2104.08315 (Holtzman et al., surface form competition); https://arxiv.org/abs/2102.09690 (Zhao et al., Calibrate Before Use, ICML 2021); https://arxiv.org/abs/1909.00161 (Yin et al. 2019, NLI as zero-shot; cited, only as background) (accessed 2026-10-02; locator: abstracts plus WebFetch summary of the Ma PDF)
- **Evidence type:** peer-reviewed/preprint paper; author independence: yes
- **Model / base / checkpoint:** BERT-based NLI models (Ma; exact checkpoints unknown); GPT-2 / GPT-3 (Holtzman, Zhao); **size:** unknown for Ma; GPT-2 family and GPT-3 sizes for the others (not extracted)
- **Task:** zero-shot text classification via NLI hypotheses (Ma); zero-shot / few-shot multiple choice (Holtzman, Zhao); **language:** English; **readout:** entailment probability / answer-token probability; **rejection mechanism:** none
- **Data provenance:** public text classification benchmarks; **metrics:** accuracy; **raw cases available:** no
- **Fixed / mitigated?** Holtzman: domain-conditional PMI scoring; Zhao: contextual calibration using content-free inputs such as "N/A" (up to 30% absolute accuracy gain); Ma: robustness attempts "in general negative"; **fix evaluated?** yes
- **Relevant local classes:** L4, L1, L5, Q2, Q5

## What the source reports
- Ma et al. note that entailment-based zero-shot classifiers are inconsistent across datasets, rely on shallow lexical cues, and that an untuned pre-trained BERT can match NLI fine-tuned BERT; their attempts to make the models more robust to lexical cues largely did not work. The fetched summary also says label wording and overlap with the text sway accuracy; I could not confirm those specific claims in the abstract itself (the abstract confirms lexical-cue reliance and the negative robustness results).
- Holtzman et al.: probability for an answer is divided among surface forms, so highest-probability scoring misranks options; reweighting by domain-conditional prior helps across GPT-2/GPT-3.
- Zhao et al.: models are biased toward answers that are common or late in the prompt; calibrating with a content-free input removes much of it.
- Together these explain why raw score margins are not confidence: scores reflect label string prior plus lexical match, which matches the local L4 observation that key-naming overrides get typical margins.

## Strength and caveats
- Good independent support for "label string and surface overlap, not meaning, drive zero-shot scores" and for content-free calibration as a known mitigation. Not about GLiClass or GLiFormer, nor about temperature-scaled sigmoid heads.
- Holtzman and Zhao study decoder LMs; Ma studies BERT-NLI. Transfer to a GLiNER-style encoder is by analogy.
- Calibration with "N/A" is a candidate test for Q2/Q5 (a content-free input score as a baseline), not shown to fix instruction-override text.
