# dlm-jev and the DiffusionGemma Jev family

- **Category**: open
- **Owner / org**: seongyeon1 (dlm-jev); related independent projects listed below
- **URLs**: https://github.com/seongyeon1/dlm-jev ; adapter https://huggingface.co/seongyeon1/dlm-jev-tickets-lora ; base https://huggingface.co/google/diffusiongemma-26B-A4B-it (NVFP4 variant by NVIDIA); siblings: github.com/razorback16/openjev (562 stars), mmastrac/djev (110), JoshuaSP/open-jev (41), Hangzhi/diffusion-jev-sglang (5), kidzik/jiffy (9), Saik0s/diffusiongemma-jev-macos (3), artalis-io/jev-bush (4), dglazkov/gev (1), kenlkehl/clinical-djev (0)
- **License** (code / weights): Apache-2.0 (dlm-jev code); DiffusionGemma weights Apache-2.0 per OpenJev's README
- **First release / last update**: dlm-jev created 2026-09-30; siblings 2026-09-16 to 2026-10-01
- **Popularity signals**: dlm-jev 1 star; openjev 562 stars

## Summary
Almost all DiffusionGemma-based Jev-likes are UNTRAINED: they read label-token logits at slots on the diffusion canvas of Google's DiffusionGemma 26B-A4B (block-diffusion MoE built on Gemma 4) in a single decoder pass. dlm-jev is the one I found that goes further with a trained domain LoRA (CE on slot-label distribution) and a per-question temperature. openjev (razorback16) is the largest and ships vLLM and MLX servers with image support, but its README documents no training.

## Approach / architecture
Each question gets a label-token slot in the diffusion canvas; one pass gives every question's distribution; only label tokens are read, so output is always in-schema. Findings in dlm-jev docs: the canvas must be padded to at least 64 tokens (an exact-length ~6-token canvas read at chance, SST-2 0.50 vs 15/16); the reply must start with an empty thought channel; encoder KV caches are written in place and need cloning when reused. Re-reads (4-read average) changed 0/100 answers on AG News and were turned off by default. Multi-question bundling changes distributions for uncertain items, so calibration should be fitted in the same bundle the service asks.
OpenJev extras: `steps` (1-8 denoise steps), `samples` (average N noisy reads), `think` (write a thought first), `sequential`; reads chunks of about 12 questions in parallel.

## Interface
dlm-jev: FastAPI `POST /v1/decide` (own schema). OpenJev: TypeSafe SDK-compatible `/v1/systemone` plus text generation; also serves Laya, Verdict, CLM and JevK5 as alternate models. vLLM PR 57250 provides the example server these derive from.

## Training & data
dlm-jev only: LoRA with CE on slot-label distribution, router patched to stop gradients through top-k indices (MLX, 48 GB Mac); 400 synthetic Korean support tickets (exact ground truth by construction), 1 epoch. No teacher model, no RLCD. OpenJev and the others: no training.

## Reported performance
dlm-jev (author, M4 Pro 48 GB, 4-bit, n=100 per half): SST-2 0.97, AG News 0.83, Yelp 0.54; raw T fitted noul 2.59, choice/score 3.34 (all >1, i.e. overconfident); ECE after fit 0.023/0.082/0.110 (before 0.028/0.184/0.380). p50 307-587 ms. Synthetic ticket triage (300 test): policy written into the question lifted urgency 0.52 -> 0.79, LoRA to 0.89; on re-rendered text the LoRA still helped urgency (0.757 -> 0.853) but category fell (0.953 -> 0.920) and public tasks lost 4-5 points (AG News 0.79 -> 0.75), i.e. forgetting. Autoregressive Qwen3-4B baseline: latency 1,267 ms vs 498 ms for 4 questions, AR probabilities far more overconfident. All author-run, small n.
OpenJev: claims "tens of milliseconds" per answer; no table in what I read.

## Self-hosting notes
DiffusionGemma 26B-A4B: MLX 4-bit (~15 GB, 32 GB+ Mac) or vLLM on NVIDIA GPU (NVFP4 variant).

## Assessment
Shows one-pass reading from a diffusion canvas works zero-shot and gives a real latency advantage over sequential AR slot-filling at equal active params, but a naive fine-tune forgets quickly. No published diffusion-LM RLCD reproduction found. Compare kotoba-lang/typed-decisions for LLaDA-MoE with LoRA.

## Sources
- https://github.com/seongyeon1/dlm-jev (README; docs/DESIGN.md via gh api)
- https://github.com/razorback16/openjev (README); https://github.com/Hangzhi/diffusion-jev-sglang (README)
- GitHub search results listing the sibling repos and star counts (gh api search/repositories)
