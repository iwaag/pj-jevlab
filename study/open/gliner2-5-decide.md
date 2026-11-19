# GLiNER2.5-Decide (Fastino)

- **Category**: open
- **Owner / org**: Fastino (HF: fastino)
- **URLs**: https://huggingface.co/fastino/GLiNER2.5-Decide ; also GLiNER2.5-Decide-1B, GLiNER2.5-multi-Decide (287M) ; Core ML port https://huggingface.co/FluidInference/gliner2-5-decide-coreml ; LiteRT port litert-community/GLiNER2.5-Decide-LiteRT ; dataset fastino/fast-decisions
- **License** (code / weights): Apache-2.0
- **First release / last update**: HF created 2026-09-23, modified 2026-09-28. (GLiNER2 base family predates the Jev release.)
- **Popularity signals**: 38,386 HF downloads, 262 likes (GLiNER2.5-multi-Decide 7,581 downloads).

## Summary
An encoder-based (GLiNER2 lineage) 340M English classification model with a Jev-like use pattern: arbitrary label sets at call time, multiple heads in one call, one forward pass, no prompt template. It is presented as an "operational decision" specialist rather than as a Jev clone: single-label and multi-label classify, not typed Score/Noul with calibrated probabilities as the headline.

## Approach / architecture
Fine-tuned from `fastino/gliner2-large-v1` (approx 486M safetensors parameters per HF API; the card calls it 340M). API `AutoExtractor.classify_text(text, {task: [labels]})` from the `gliner2` package; multi-label returns all labels above threshold. Whether it exposes calibrated probabilities is not clear from the card text read.

## Interface
`pip install gliner2`; Python only (plus Core ML and LiteRT conversions by third parties). No `/v1/systemone` compatibility stated.

## Training & data
Trained/evaluated on `fastino/fast-decisions` (17 domains; 300 held-out examples each); training details not read.

## Reported performance (vendor-measured, on vendor's own benchmark; same text and labels for all models)
Exact-match accuracy: GLiNER2.5-Decide 60.2%, Decide-1B 59.6%, JevK5 57.6%, GLiNER2.5-multi-Decide 56.7%, SemIf (Qwen3.5-4B) 56.4%, GLiFormer large-v1 49.0%, Laya Router 46.6%. Jev itself is not in the table. JevBench placement: Von's card says Von "trails the 194M GLiNER2 (21.0)" on sealed Choice (a smaller GLiNER2 model appears on the JevBench board).

## Self-hosting notes
Small, local, CPU/GPU; `pip install gliner2`.

## Assessment
Most-downloaded encoder-based entrant; credible because of Fastino's established GLiNER lineage, but benchmark is the vendor's own and it measures labels, not calibration. Useful as a strong, simple baseline against Jev-style heads for pure classification.

## Sources
- https://huggingface.co/fastino/GLiNER2.5-Decide (card + API)
- https://huggingface.co/wfzyx/von (JevBench mention)
