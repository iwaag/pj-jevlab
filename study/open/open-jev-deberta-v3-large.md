# open-jev-deberta-v3-large (Kotoba Labs)

- **Category**: open
- **Owner / org**: com-kotobalabs / kotoba-lang (Jun Kawasaki per ADR path hints; unverified)
- **URLs**: https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large ; code https://github.com/kotoba-lang/typed-decisions
- **License** (code / weights): Apache-2.0 (HF); GitHub repo license NOASSERTION
- **First release / last update**: HF created 2026-09-18, modified 2026-09-24.
- **Popularity signals**: HF 2,851 downloads, 70 likes; GitHub kotoba-lang/typed-decisions 8 stars.

## Summary
A small, careful reproduction of the Jev "shape" on `microsoft/deberta-v3-large` (434M), trained on only 18,000 states of public gold-labelled data (Banking77, SST-5, BoolQ), no teacher model or synthetic labels. The card has an explicit in-domain vs out-of-domain gap analysis.

## Approach / architecture
Marker tokens `[STATE] [Q] [OPT]` added to the tokenizer; DeBERTa reads state and all questions at once; a 3-layer scoring head scores each option from `[mean(question tokens); mean(option tokens); product]`; softmax within each question's option group; post-hoc temperature. Loss CE + Brier; gold-preserving augmentation (option shuffling, paraphrase templates, distractor dropping, level relabelling, noul negation). Up to 255 options, 512-token context (state cut to 256). Author found a fresh marker-token head does not learn but the span head does.

## Interface
Python `OpenJev.from_pretrained(...).decide(state, questions)` (via the kotoba-lang package). No HTTP server stated.

## Training & data
mteb/banking77, SetFit/sst5, google/boolq; 42,000 questions, 1 epoch, one H100, 229 s (~$0.25). Code and corpus builder released.

## Reported performance (author-measured on public gold labels; explicitly "not comparable to" TypeSafe's numbers)
In-domain accuracy 0.854 / Brier 0.213 / ECE 0.022 (banking77 intent 0.916, boolq 0.879, sst5 0.599). Out-of-domain (new instructions/option sets) 0.690 / Brier 0.399 / ECE 0.035; unseen ordered scales barely above majority (0.45 vs 0.26). Latency: H100 bf16 28 ms for 10 questions; M1 Max CPU fp32 1.8 s for 4 questions. JevBench: jeff's README places it #13 of 18 on v1.2.2.

## Self-hosting notes
~1.7 GB fp32; GPU recommended, CPU slow (seconds).

## Assessment
Valuable as a minimal, cheap training recipe with a frank generalization gap (0.85 vs 0.69) - a useful warning for any lab that trains on a few public datasets. Not competitive generally.

## Sources
- https://huggingface.co/com-kotobalabs/open-jev-deberta-v3-large (card + API)
- https://github.com/logan-markewich/jeff (bench/RESULTS.md, JevBench rank)
