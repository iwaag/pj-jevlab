# mini-jev

- **Category**: open
- **Owner / org**: r-ms (HF dataset by "Mikhail")
- **URLs**: https://github.com/r-ms/mini-jev ; run records https://huggingface.co/datasets/Mikhail/mini-jev-runs
- **License** (code / weights): MIT / uses Qwen3-4B-Instruct-2507 (Apache-2.0); CLINC150 CC BY 3.0
- **First release / last update**: created 2026-09-17 / last push 2026-09-18
- **Popularity signals**: ~57 stars

## Summary
A preregistered experiment (PREREG.md with four amendments) asking how much of the Jev interface a frozen Qwen3-4B already provides: replace grammar-constrained JSON generation of closed-choice fields with reading option-letter logits. It is a measurement study plus a teaching bench, not a service.

## Approach / architecture
- Each enum/boolean field becomes a lettered multiple-choice question; one forward pass; scores of the option letters at the answer position are normalised.
- Shared-prefix KV cache across several questions on one text (text first, question last; prefix must be byte-identical).
- Compared against xgrammar-constrained JSON generation (arms A1joint/A1split/A1letter/A1label/A1prob/B1perm...).
- Explicit statement: the letter "shares are normalized candidate scores, not calibrated probabilities"; use the confidence gap for abstention. Calibration is deliberately deferred (DEFERRED.md).

## Interface
No server. Local teaching bench (`demo/server.py`) that runs both methods side by side on a flat JSON schema. README maps Jev's Choice and Noul to letter read / boolean read and notes Score was not measured; no wire compatibility.

## Training & data
None. CLINC150 sample (pinned revision, manifest with hashes), 450 texts, 6,750 paired observations; 27,900 decisions with full candidate logits published on the Hub.

## Reported performance
Author-measured, one model, one dataset, English short utterances, one GPU (RTX 4090) or MPS:
- Accuracy letters vs JSON: 0.907 vs 0.909 (delta -0.22 pp, 95% CI [-1.44, +1.04]); equal across k=2..16.
- Letter vs option name as answer token: +10.0 pp on intent, +13.2 pp domain, +1.2 pp (ns) on boolean.
- Speed: 4x faster than JSON on 32-token texts; with shared-prefix cache 1.4x/1.8x/2.4x on 2048-token texts for 1/2/3 fields; naive re-read per field loses (1.10-1.16x slower).
- Shared KV vs separate: same accuracy (0.8484 vs 0.8483); 59/13,500 answers flip near ties. Bit-identical across two RTX 4090s.
- Where reading loses: out-of-scope texts (41/50 vs 47/50 "none"), dependent fields (-5 pp). Writing probabilities as numbers: 0.346 vs 0.896 for letters.
- Next-token is an option letter in 13,600/13,600 questions; candidate mass min 0.99999624.

## Self-hosting notes
Python 3.11, uv, ~9 GB weights, ~8.5 GB memory for 4B; CUDA or MPS.

## Assessment
Rigorous and cautious; the most useful methodological point is that single-token letter identifiers (not option names) are what lifts accuracy, and that shares are not calibrated. Limited scope (one model, one dataset). Good template for a lab wanting preregistered comparisons and the raw logit dataset for calibration work.

## Sources
- https://github.com/r-ms/mini-jev (README, metadata)
