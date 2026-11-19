# Liquid d1 (Liquid AI)

- **Category**: close (open weights were reportedly promised; none exist as of 2026-10-01)
- **Owner / org**: Liquid AI
- **URLs**: https://docs.liquid.ai/lfm/models/decision-models ; https://docs.liquid.ai/guides/decision-model-guide ; https://vercel.com/ai-gateway/models/d1
- **License** (code / weights): proprietary; model library says "API only and not trainable, no GGUF/MLX/ONNX weights" (MarkTechPost). An X summary (AGTP) said "open weights promised soon"; I could not confirm that from Liquid's own thread.
- **First release / last update** (as seen 2026-10-01): 2026-09-29
- **Popularity signals**: coverage by MarkTechPost, DataNorth, AlphaSignal; on Vercel AI Gateway as `liquid/d1`; community repos (liquid-D1-test, decide)

## Summary
Liquid's first decision model, exposing the TypeSafe-compatible System One API with zero output tokens. Liquid claims it is the first to beat Jev on Hugging Face's Decision Index.

## Approach / architecture
Base model, size, training: undisclosed (MarkTechPost). Single call, parallel evaluation of all questions.

## Interface
`POST https://api.liquid.ai/decisions/v1/systemone`, bearer `LIQUID_API_KEY` (prefix `liquid_`). Model `d1:free`. Python: `TypeSafeClient(api_key=..., base_url="https://api.liquid.ai")`, `client.system_one(model="d1:free", state=..., questions={...})` via `typesafe-sdk`. Response: `{"model":"d1:free","answers":{"is_complaint":{"type":"noul","noul":0.999}},"usage":{"input_tokens":84,"output_tokens":0}}`. Noul/Choice/Score identical to Jev.

## Training & data
Not disclosed.

## Reported performance
Vendor claims: Decision Index 0.2.1 score 58.9 vs Jev 1.13 at 57.9 (Hugging Face index; Liquid-reported, via baobab-tech repo); better multilingual, prompt-injection resistance, long-input handling (no numbers given in the thread). Respan's third-party table ranks Jev above others on its own tests; not specific to d1.

## Self-hosting notes
Not possible currently.

## Assessment
Free during experimental phase (`d1:free`); Vercel lists $0.04/MTok input and 65,536 context, while MarkTechPost/DataNorth mention 32K context: conflicting. Useful as a second hosted reference for Jev-compatibility. A one-point Decision Index margin is small and vendor-announced.

## Sources
- https://docs.liquid.ai/lfm/models/decision-models
- https://docs.liquid.ai/guides/decision-model-guide
- https://vercel.com/ai-gateway/models/d1
- https://www.marktechpost.com/2026/09/29/liquid-ai-releases-d1-a-decision-model-that-returns-calibrated-probabilities-with-zero-output-tokens/
- https://threadreaderapp.com/thread/2105003472332693869.html
- https://github.com/baobab-tech/decision-models-experiments
