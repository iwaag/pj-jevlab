# jevlike

- **Category**: open
- **Owner / org**: vinnylarouge (github.com/vinnylarouge/jevlike)
- **URLs**: https://github.com/vinnylarouge/jevlike
- **License** (code / weights): MIT / no hosted weights; example checkpoints in repo (`examples/checkpoints/*.pt`)
- **First release / last update**: created 2026-09-16, last push 2026-09-16
- **Popularity signals**: GitHub 1,338 stars

## Summary
A small research starter for Choice only: context text plus N option texts in, one probability per option out in one pass. Not an LLM fine-tune by default: byte-level encoder trained from scratch, or a frozen pretrained encoder (e.g., Qwen2.5-0.5B) plus a small option-attention scorer. Authors say explicitly it is not a reproduction of Jev or its training method. It is the origin of the "option-attention head" that Cua-S1 later reused.

## Approach / architecture
Each option becomes a query vector that attends over context-token vectors to form an option-specific context vector; a shared dot product gives one score per option; softmax across options. Default encoder: learned byte embeddings (context truncated to 192 bytes, option to 32 bytes). Optional: frozen HF encoder with `--rank` (scorer head width). Dynamic option count (min 2). No Score or Noul types; no temperature calibration step documented beyond ECE reporting in `jevlike-eval`.

## Interface
CLIs `jevlike-data`, `jevlike-train`, `jevlike-eval`, `jevlike-predict`; JSONL `{context, options, label}`. No HTTP server or `/v1/systemone` compatibility. Doom (7 buttons) and chess controller demos use the same visual scorer.

## Training & data
Cross-entropy on option index (implied; README does not name the loss). Synthetic menu generator; Wikispeedia next-click data (SNAP) script; user JSONL. No teacher models, no RLCD.

## Reported performance
Self-reported local experiments: about 98% on synthetic menus; target-disjoint Wikispeedia next-click: frozen Qwen2.5-0.5B + scorer 26% vs about 8% for shuffled/random-encoder controls; scratch model on 40k clicks 29%. At eight options the one-pass scorer was about 100x faster than a small decoder writing 400 tokens. README states these are local experiments, not the quickstart, and no equality with Jev was shown. Doom joint checkpoint: 0.60 kills average; chess-only: 4 wins/46 draws/0 losses vs random mover, 0/2/48 vs Stockfish level 0.

## Self-hosting notes
CPU/MPS/CUDA via uv; trivial.

## Assessment
Not a Jev-quality text model; value is as a minimal architecture sketch (option-as-query cross-attention). Weak language understanding by design (byte encoder). Included for completeness and because Cua-S1 builds on it.

## Sources
- https://github.com/vinnylarouge/jevlike (README)
- Cua HN thread (https://news.ycombinator.com/item?id=49767564) for the Cua-S1 lineage claim
