# Julia 1 (Supersonic Labs)

- **Category**: open (weights Apache-2.0; a proprietary hosted API is also planned)
- **Owner / org**: Supersonic Labs (Brazil; domain supersoniclabs.ai, formerly .ia.br)
- **URLs**: https://supersoniclabs.ai/julia-1 ; HF https://huggingface.co/SupersonicLabs/Julia-1
- **License** (code / weights): Apache-2.0 for weights and code (HF metadata + site). No GitHub repo found under SupersonicLabs/Julia-1.
- **First release / last update**: HF created 2026-09-23, modified 2026-09-26; evaluations dated 2026-09-24/25.
- **Popularity signals**: HF 2,556 downloads, 327 likes.

## Summary
A 144.3M multilingual decision model built on `jhu-clsp/mmBERT-small`, trained on a stated ~R$540 (US$104) of cloud GPU. Claims parity with Jev's published typed-decisions accuracy and large wins on DAIR Emotion, but concedes a big loss on high-cardinality Banking77. The only encoder-based project here with an explicit Portuguese focus.

## Approach / architecture
mmBERT-small encoder, 144.3M params, 550.5 MiB weights, 1,024-token combined context (state + question + options); one forward pass selects among supplied answers for Choice / Score / Noul. A "Router" component narrows long option lists (e.g., Banking77 72 labels) to a shortlist and "can lose the correct answer". Site states "Julia 1 is not a fine-tuned Qwen model." Details of the head and calibration were not given in the page text I could fetch; no ECE reported.

## Interface
Hugging Face weights with a "Python interface, metrics, provenance and instructions". HF library tag is pytorch (custom code), not a transformers pipeline. Jev wire-compat not stated. Planned proprietary API: $0.025 / 1M input tokens, $0 output (not launched).

## Training & data
Budget-constrained training from mmBERT-small ("first released test of our training system"); training-data details were not extractable from the page. Roadmap mentions Julia 2 with custom foundation architecture.

## Reported performance (author-measured on 2026-09-24, H200 BF16, strict encoding; Jev figures are "Jev reference" values, source not shown beyond the table)
- Typed decisions: 1,463/2,000 = 73.15% vs Jev ref 72.70% (Choice 71.33%, Noul 80.67%, Score 68.88%).
- AG News 94% vs 91%; DAIR Emotion 86% vs 48%; Banking77 pilot (72 labels) 64% vs 87% (n=100 each, so small samples).
- MASSIVE 52 locales: 71.50% overall (pt-PT 86.25%, en-US 86.75%).
- CPU run (09-25): typed 72.55%; Banking77 60/100 with 3 abstentions.
- Latency: Apple M4 33.15 ms median (44.23 p95); Intel i5-1235U 294.8 ms (Banking77 3.7 s average); Samsung SM-X510 tablet via ONNX 203 ms median.
- No independent verification found. No ECE/calibration numbers.

## Self-hosting notes
CPU-capable and runs on phone/tablet-class hardware per the author; ~550 MB weights.

## Assessment
Strengths: small, multilingual, CPU/edge-friendly, Apache-2.0, candid weaknesses (long option lists, outside knowledge, multi-step reasoning). Weaknesses: n=100 sub-benchmarks; benchmark overlaps with Laya's and Verdict's chosen sets (typed-decisions; AG News; DAIR; Banking77), so the comparison reflects those benchmarks' definitions of "Jev reference"; no calibration metrics, which is central to Jev; no repo/training code seen.

## Sources
- https://supersoniclabs.ai/julia-1 (WebFetch; .ia.br 301 redirects to .ai)
- https://huggingface.co/SupersonicLabs/Julia-1 (card head + API)
