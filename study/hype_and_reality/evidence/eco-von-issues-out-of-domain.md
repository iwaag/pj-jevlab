# Von (395M encoder): out-of-domain confident misses, non-English, and benchmark gaps

- **Sources:** https://github.com/wfzyx/von/issues/21 (Hagetino, 2026-09-28, with maintainer reply 2026-09-30), /issues/22 (maintainer, 2026-09-30), /issues/3 (jabr, 2026-09-19 to 09-21); accessed 2026-10-02. Locators: tables in issue bodies and maintainer comments. Hagetino's repo https://github.com/Hagetino/von-shadow and jabr's https://github.com/jabr/classifier-benchmark were not opened.
- **Evidence type:** reproducible bug report (#21, #22; maintainer reproduced the numbers) and user benchmark (#3, LLM-generated synthetic cases); independence: yes for the reporters; the maintainer is the model author.
- **Model / base / checkpoint:** von-sdk 1.3.1 / 1.3.3 (von-1.3.0 weights); **size:** 395M (stated in JevBench issue #143, https://github.com/fstandhartinger/jevbench/issues/143, title); **architecture:** NLI-style encoder with option-marker head, English only per the maintainer; **training:** public HF datasets plus a synthetic operational-decision corpus (maintainer statements, not verified).
- **Task:** #21: coding-agent triage (noul evidence check n=49; described choices n=7-12); **input language:** English plus one German item; **options / readout:** snake-case-like keys with descriptions; **rejection mechanism:** none.
- **Data provenance:** author-written (#21), LLM-generated (#3, 78 and 869 cases); **n:** see above; **raw cases available:** yes (linked scripts).
- **Fixed / mitigated?** `von calibrate` shipped in 1.3.4 (fixes confidence, not argmax); training gap tracked in #22; README now says English-only and to prefer described Choice. **fix evaluated?** calibrate: ECE 0.21 -> 0.11 on 38 labels (maintainer's run).
- **Relevant local classes:** L2, L3 (partly), L9; Q1, Q3, Q8.

## What the sources report
- #21: noul evidence check 0.53 accuracy vs 0.78 for a regex; choices 0.43-0.80. Confident misses: "Invalid API key - Please run /login" -> `code_error` 0.87 over an `auth` option described as "Login, token, credentials"; a German approval phrase -> `capability_gap` 0.92.
- Maintainer reproduced the choice numbers exactly, said noul without criteria is "weak by construction", the German case is unearned token matching, and shipped calibration does not transfer; temperature never flips an argmax.
- #3: on 78 LLM-written cases Von initially scored 0.654 micro vs 0.974 for Jev; after maintainer fixes and a second training run, 0.923 (v1) but 0.666 on a new 869-case/49-task suite vs Jev 0.964 (comment 2026-09-20, jabr). The 78-case jump followed training on the same domains and is not independent.
- Maintainer attributes losses to training-data coverage, not capacity.

## Strength and caveats
- Concrete evidence that a trained ~400M Jev-like encoder still maps unlisted situations to a lexically close option with high confidence (L3 analogue). Reporter sets are small; #3's v1 recovery is self-fit.
- Supports Q3 (training coverage matters) more than Q1 (size) because no larger Von exists in these reports.
