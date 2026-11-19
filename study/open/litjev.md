# LitJev

- **Category**: open
- **Owner / org**: zhengxuyu (ZhengxuYu)
- **URLs**: https://github.com/zhengxuyu/litjev (not on PyPI per README); docs in `docs/` (api, how-it-works, system-two, benchmarking)
- **License** (code / weights): Apache-2.0 (some adapted jevlike examples MIT) / no weights
- **First release / last update**: created 2026-09-17 / last push 2026-10-01 (SGLang backend added same day)
- **Popularity signals**: ~45 stars

## Summary
"A reproduction of Jev" for the Qwen family (default Qwen3.8-27B on one H100 80 GB), with the closest wire fidelity among the self-built servers, and the only one in this batch that scores whole option text by sequence likelihood by default. Also includes an experimental "System Two" routing head, outside the training-free scope.

## Approach / architecture
- Two readouts. Default **content readout**: prefill the shared state, then for each option append the option's own words after `Answer:`, teacher-force them and sum token log-probabilities; softmax over summed option scores (full-sequence likelihood, no length normalisation is mentioned in the README). `--readout coded` restores single-token letter codes. Rationale: no label-token prior pulling toward positions.
- Parallelism: on SGLang the radix prefix cache shares the state prefill (`input_token_logprobs` for options / `token_ids_logprob` for codes); on transformers each question's option rows share one batched pass. Questions cannot see each other. `--sglang-batch-questions` is off by default because of open SGLang issues that can attach a hidden state to the wrong request in a batch.
- `score` = probability-weighted level index; `noul` = P(yes); `confidence` field returned for choice/score.
- Calibration: optional post-hoc temperature fitting (docs/how-it-works.md#calibration); "Probabilities are not calibrated by default."
- System Two (experimental, `/v1/systemtwo`): a small trained head routes questions to the backbone's slow thinking; backbone frozen.

## Interface
Claims "exactly the schema defined in the Jev documentation": `POST /v1/systemone`, `model/state/questions`, `choice/score/noul`, `answers` + `usage`; up to ten questions per request; playground UI at `/`; Swagger at `/docs`. Differences: no auth locally, `model` = `litjev`; usage reports `input_tokens: 0` under content readout on SGLang. Backends: HF transformers, SGLang. Vision checkpoints for screenshot decisions (transformers only).

## Training & data
None for System One readout. Benchmarks in repo: MMLU-Pro direct answer scoring, Doom and chess from screenshots.

## Reported performance
README gives no headline accuracy/latency numbers in the part retrieved; benchmarking is delegated to docs/benchmarking.md (not read). Nothing independently verified.

## Self-hosting notes
`uv run --locked litjev --model Qwen/Qwen3.8-27B` (27B needs ~H100 class); any Qwen size works; `inference.verify` script compares transformers vs SGLang outputs.

## Assessment
Good wire-contract fidelity and a principled option-text likelihood readout (avoids letter bias, but costs tokens per option and no length normalisation documented, so long options may be penalised). Lack of published numbers and uncalibrated default are the main gaps. Worth testing as a comparison point against letter-logit readers.

## Sources
- https://github.com/zhengxuyu/litjev (README, metadata)
