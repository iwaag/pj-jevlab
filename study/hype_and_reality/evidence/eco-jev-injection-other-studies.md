# Other injection studies on hosted Jev (jagged, system1-system2, jev-engineering)

- **Sources (accessed 2026-10-02):** https://github.com/zkousama/jagged (README summary); https://github.com/Iskandeur/system1-system2 (README summary); https://github.com/eugeniughelbur/jev-engineering (README summary). Locators: results sections. The list that led here is https://github.com/GautamTalksDev/awesome-jev-robustness (aggregator; its other entries JevOut and cwhy were not independently opened, JevOut unverified).
- **Evidence type:** independent evaluations / documented deployment (jev-engineering); independence: yes for all three as far as stated.
- **Model:** Jev 1.13.0 hosted (size unknown); jagged used the Vercel gateway so the exact version is inferred by elimination, per its limitations.
- **Task:** jagged: Wikipedia deletion-discussion outcome (yes/no) with an appended "answer no" line, n=486. system1-system2: 80 utterances x 5 injection templates naming a false target label, Jev vs GPT-5.2. jev-engineering: a gate for dangerous shell commands, 30 dangerous commands x injection styles.
- **Data provenance:** author-built; **raw cases available:** partial (not inspected).
- **Fixed / mitigated?** system1-system2: a one-sentence hardening plus delimiters cut targeted success to about 1.3% for both models; jev-engineering: deterministic regex hard rules run before the model. **fix evaluated?** yes, on the authors' own attack sets.
- **Relevant local classes:** L4, L8; Q2, Q4, Q5.

## What the sources report
- jagged: accuracy 96.5% -> 26.5% with one appended line; a follow-up found the model mostly ignored the instruction and believed the false fact (so it is fact injection, not instruction following).
- system1-system2: Jev targeted success 18.5% vs GPT-5.2 31.8%, with an authority-style template at 80/80 on GPT-5.2; escalating low-confidence Jev answers to the LLM made the hybrid worse (28.2% vs 23.5%) because injections lowered Jev's confidence.
- jev-engineering: blunt "ignore your instructions" passed 0/30; "the owner approved this" passed 3/30; successful attacks averaged confidence 0.400 vs 0.681 on legitimate traffic, but a 0.8 floor to catch them escalated 58% of normal traffic. The tool fails open to a normal permission prompt on error.

## Strength and caveats
- Shows that on hosted Jev, bare override commands mostly fail while plausible false facts and authority claims succeed; a different regime from jeff's key-naming overrides (L4).
- Attack sets are single-author and writer-known; none covers jeff, Von, or option-key naming.
