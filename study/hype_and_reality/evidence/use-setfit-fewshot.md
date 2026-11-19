# SetFit: small fine-tuned sentence encoders vs large LLMs on closed-label text classification

- **Sources:** https://arxiv.org/abs/2209.11055 ; HTML https://arxiv.org/html/2209.11055 (Tunstall et al.) (accessed 2026-10-02; locator: RAFT results table and N=8/N=64 results as summarised by the fetch tool; original tables not read directly)
- **Evidence type:** peer-reviewed/preprint paper, author evaluation of own method; author independence: no
- **Model / base / checkpoint:** SetFit RoBERTa-large (355M), SetFit MPNet (110M); comparisons T-Few 11B and 3B, GPT-3 175B; **training:** contrastive fine-tuning on few labelled examples + classification head
- **Task:** closed-set text classification (RAFT, other benchmarks); **rejection mechanism:** none; no out-of-scope inputs; **metrics:** accuracy/score; **raw cases:** n/a

## What the source reports
- RAFT: SetFit RoBERTa 71.3 vs GPT-3 62.7 vs T-Few 11B 75.8 (as relayed by fetch summary; recheck against the paper's table before citing).
- SetFit MPNet at N=64 averages 75.3 and beats T-Few 3B by about 5 points despite ~27x smaller (same caveat).

## Strength and caveats
- Supports: small fine-tuned encoders are competitive on closed-set classification with few labels. Does not address out-of-scope or adversarial input at all, so it cannot support the claim that small models reject inappropriate input.
- Relevant local classes: none directly; Q3 (training matters more than size).
