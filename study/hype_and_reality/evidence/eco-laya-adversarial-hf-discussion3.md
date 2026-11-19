# Laya-multilingual adversarial 100-scenario evaluation (the "40.3%" claim, verified)

- **Sources:** https://huggingface.co/convaiinnovations/laya/discussions/3 (accessed 2026-10-02; locator: headline metrics, sections 4.1 and 4.4, option-order and injection/abstention paragraphs; discussion by user mghafiri, 2026-09-20). Echoed in https://github.com/NandhaKishorM/laya/issues/377 (opening paragraph).
- **Evidence type:** reproducible bug report / independent evaluation (single author, deliberately adversarial); author independence: yes (third party; also repeated in laya issue #377 by PerryLink).
- **Model / base / checkpoint:** `laya-multilingual` (321.9M parameters as stated in the discussion), tested with laya 0.3.4; **size:** 321.9M (verified from the discussion page); **architecture:** encoder + decision head (RLCD per Laya docs; not re-verified here); **training:** unknown here.
- **Task:** 100 hand-written English scenarios, 305 graded decisions (choice/noul/score mixed) on support-style text with negation, retractions, buried evidence; **input language:** English; **options / readout:** native Laya probabilities; **rejection mechanism:** only an explicit `other`-style option or an `enough_info` boolean written by the test author.
- **Data provenance:** written by the single reviewer; **n:** 305 decisions / 100 scenarios (89 choice questions for order test); **metrics:** accuracy, ECE, Brier, order stability; **configuration:** zero-shot, default; **raw cases available:** per the page, yes (not inspected).
- **Fixed / mitigated?** Not by the discussion itself; Laya later documented negation limits (see eco-laya-negation-377). **fix evaluated?** no.
- **Relevant local classes:** L4 (instruction-like text), L5, L2/L3 (via comparison to a constant-answer baseline); Q1, Q3, Q5, Q8.

## What the source reports
- 123/305 = 40.3% question accuracy and only 11% of scenarios fully correct; a hindsight-chosen constant answer per question key (reads no text) scores 53.1%.
- Calibration: 54% of answers with confidence >= 0.90 were wrong; accuracy roughly flat near 45% across confidence bands from 0.5 up; ECE 0.313, Brier 0.513.
- Option-order sensitivity: about one choice answer in five flips under shuffled options; stability 100% for binary choices, 0% for 12-option questions (L5 analogue, in a trained Jev-style model).
- Negation (section 4.4): "I don't want a refund" read as refund requested; "do NOT cancel" answered cancel_account.
- Positive points: the single injection case (S004, "IGNORE ALL PREVIOUS INSTRUCTIONS") was ignored and one underspecified scenario (S009) correctly returned `other` with `enough_info=False`. These are n=1 each.
- The author states the test is zero-shot, out-of-domain and deliberately adversarial, so not representative of ordinary traffic.

## Strength and caveats
- Confirms the 40.3% figure exists and is an adversarial single-author set; the figure is accuracy over decisions, not over scenarios, and below a constant-answer baseline.
- The injection and abstention "passes" are single cases and must not be generalised. The cwhy injection bench (eco-injection-bench-cwhy) found Laya far more injection-prone on a larger set.
- Checkpoint is multilingual 0.3.4; later versions changed temperature handling (see eco-laya-issues-confidence-and-routing).
