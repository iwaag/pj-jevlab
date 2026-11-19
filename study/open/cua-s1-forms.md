# CUA-S1-FORMS (Cua)

- **Category**: open
- **Owner / org**: Cua (trycua; HF org cua-ai)
- **URLs**: HF https://huggingface.co/cua-ai/cua-s1-forms ; code https://github.com/trycua/cua/tree/main/libs/cua-s1 ; Core ML port https://huggingface.co/FluidInference/cua-s1-forms-coreml ; app https://github.com/FluidInference/FluidUse ; browser port https://github.com/ai-ecoverse/cua-s1.js
- **License** (code / weights): MIT / MIT (cua-s1-forms); repo notes the MIT code license does not cover "future official model weights"
- **First release / last update**: HF created 2026-09-18, modified 2026-09-26.
- **Popularity signals**: HF cua-ai/cua-s1-forms 114 likes (HF download count shows 0); FluidInference Core ML port 304 downloads / 15 likes; FluidUse 215 stars; trycua/cua 27,651 stars (parent monorepo).

## Summary
A tiny (706,048-parameter), from-scratch "option-attention" scorer for GUI form filling, from the Cua-S1 family of small specialist computer-use models. It is not a general Jev replacement: it picks among document entities (`fill ...`) or `check` / `click` / `skip` for one UI element at a time, with the same input/output contract as Jev (context + typed options in, one probability per option, single forward pass).

## Approach / architecture
Byte-level embedding, 2-layer Transformer encoder (width 128, 4 heads) encoding context and each option separately; an option-attention head uses each option as a query over context tokens, shared dot product to a logit, softmax over live option count. Context truncated to 224 bytes, options to 96 bytes. Every actionable element scored independently in a parallel batch; downstream code orders execution. Not a pretrained encoder (no ModernBERT); related family members: `cua-s1-nano-0.1` (~855K params, from scratch) and `cua-s1-4b-0.1/0.2` (LoRA on frozen Qwen3.5-4B).

## Interface
Python package `cua_s1` (source only; loads safetensors + JSON config with SHA-256 signature; pickle checkpoints deliberately refused after a security issue, trycua/cua#3977); integrates with the Cua Driver (`set_value` / `click`). Core ML conversion by FluidInference: 0.9 ms per decision on Neural Engine (FluidUse README, author-measured). ONNX/browser community ports exist.

## Training & data
10,000 synthetic episodes (2-16 field forms from a 55-concept catalogue with synonyms and forced look-alike confuser pairs; fictional people and reserved/invalid identifiers); AdamW, cosine schedule, 6 epochs, batch 128, CE over live options. Form-disjoint splits. Generator code released; weights released.

## Reported performance (author-reported at publication; the card notes the supporting results document is not in the repo and `libs/cua-s1` does not reproduce them)
- Synthetic test (~15k decisions, form-disjoint): 99.95%; real demo eval (3 forms + 3 PDFs, 196 decisions): 100%; shuffled-context control 37%.
- Head-to-head vs hosted Jev API (`jev-latest`, no fine-tuning): 99.7% vs 83.6%; Jev 96% on judgement decisions, 74% on recognizing already-filled fields (a convention the specialist was trained on). Not independently verified.

## Self-hosting notes
Trivial: ~700K params (few MB), runs on CPU; Core ML path for ANE.

## Assessment
Illustrates that for a narrow, structured domain a sub-1M-param specialist can beat a general hosted Jev; not a general decision model and trained wholly on synthetic data with a very small real eval. Relevant as the "specialist beats generalist" data point and for its Jev-style contract at tiny scale.

## Sources
- https://huggingface.co/cua-ai/cua-s1-forms (card + API)
- https://github.com/trycua/cua (libs/cua-s1/README.md via gh api)
- https://github.com/FluidInference/FluidUse (README via gh api)
