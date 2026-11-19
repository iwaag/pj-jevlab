# sotaaz.com: "Jeff vs Jev" and decision-confidence posts (name collision warning)

- **Sources:** https://sotaaz.com/post/jeff-vs-jev-en (author KR, 2026-09-29) and https://sotaaz.com/post/decision-confidence-en (2026-09-24); accessed 2026-10-02 via page fetch summaries (not read line by line).
- **Evidence type:** independent evaluation / blog; author independence: unknown (the author appears to run the benchmark panel).
- **Model / base / checkpoint:** the "Jeff" in the post is described as Qwen3.5-based 0.8B and 2B (v1.0, v1.1), which does not match logan-markewich/jeff (GLiFormer wrapper). Whether these are the same project is **unverified**; treat as a different model with the same name until confirmed. Also tested: Jev 1.13.0, Kev-9B; the confidence post covers openjev, laya, CLM-8B.
- **Task:** Jeff's own 4,599-question panel (BBH, Financial PhraseBank, JudgeBench, RAGTruth, WinoGrande); BANKING77 (154), TREC (500), AG News (200); **options / readout:** native probabilities.
- **Data provenance:** public datasets; **metrics:** accuracy, calibration error points, auto-accept coverage at 95% accuracy; **raw cases available:** unknown.
- **Fixed / mitigated?** v1.1 retrained for the >26-option failure. **fix evaluated?** partially (BANKING77 65-66% vs Jev 76%).
- **Relevant local classes:** L5, L8; Q1, Q3, Q8.

## What the source reports
- Jev 85.7 vs Jeff-2B 83.0 on the same questions; Jeff-2B better on Financial PhraseBank and RAGTruth, Jev on BBH, JudgeBench, WinoGrande.
- v1.0 never picked an option labelled past Z, giving 0% on 27+ option tasks; reversing option lists confirmed it was position, not content (an option-position artefact).
- Confidence post: laya on TREC could auto-accept 88.4% of answers at 95% accuracy but 0% on BANKING77; openjev's repeated wrong answers were 77-80% unanimous, so agreement across seeds did not signal correctness.

## Strength and caveats
- Useful for Q8 (position effects can be a training-range artefact fixable by retraining) and Q1 (a 2B model close to Jev on the author's panel). Not about abstention or injection.
- Second-hand summary; do not equate this Jeff with the locally tested checkpoint.
