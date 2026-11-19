# Evidence index and grades

Collected 2026-10-02 for [hype_and_reality](../README.md). There is one file per source or tight source cluster, each using a common template. The template records the model, size, task, readout, rejection mechanism, provenance, n, metrics, raw-case availability, and whether a fix was evaluated. Queries and exclusions are in [../search-log.md](../search-log.md).

## Grading rule
| Grade | Meaning |
|---|---|
| **A** | Independent of the model author, inspectable numbers, with raw cases or a public dataset, or peer-reviewed. The key number was re-checked at the source by the lead session or read from the PDF text. |
| **B** | Independent but small n, or raw cases not inspected; or an author evaluation with reproducible scripts or artifacts; or numbers relayed through a fetch summary but consistent with other sources. |
| **C** | Author/vendor claim with no independent check, commercial case study with aggregates only, single anecdote, or indirect relevance only. |

**Lead-session re-checks:**
- cwhy injection table, via `gh api` README;
- laya-intent-router OOS figures and caveats, via `gh api` README;
- Tam et al. abstract (arXiv 2503.01550);
- Kev checkpoints (HF API: bases, Apache-2.0, 27B = 25.6B params);
- Qwen3.5-9B/27B parameter counts (HF API);
- GLiFormer-large size: the local weight file is 2.30 GB fp32 ≈ 575M parameters, so the card's 575.6M is right and jeff's README "400M" is not.

**Interpretation rules applied:**
- Temperature-scaled probabilities are not treated as accuracy.
- API-compatible clones are not treated as Jev.
- A benchmark "adversarial/trap" tier is not counted as a prompt-injection test unless the items are injections.

## Index
| File | Type | Grade | Main point | Local classes |
|---|---|---|---|---|
| [eco-injection-bench-cwhy](eco-injection-bench-cwhy.md) | independent eval, raw data | **A** | Appended instructions flip answers: Jev 0.09%, Winnow-12B 3.0%, SemIf-4B 27.4%, Laya 49–63% (half of it "any added text"). A policy defence helps Kev-9B, but makes Kev-0.8B worse. | L4, L6 |
| [eco-laya-negation-377](eco-laya-negation-377.md) | reproducible bug, 3 reporters | B | "do NOT cancel" → `cancel_account` at 0.9998 | L4, L3-like |
| [eco-laya-issues-confidence-and-routing](eco-laya-issues-confidence-and-routing.md) | bug reports / small evals | B | Chit-chat routed to skills at 0.77–0.91 despite a `none` option; 37/65 errors at confidence ≥ 0.90 | L2, L3, L8, L9 |
| [eco-laya-adversarial-hf-discussion3](eco-laya-adversarial-hf-discussion3.md) | independent adversarial eval | B | 40.3% on 100 adversarial scenarios (below a constant baseline); 1 in 5 order flips | L4, L5, L8 |
| [eco-von-issues-out-of-domain](eco-von-issues-out-of-domain.md) | reproducible bug | B | Unlisted situation mapped to the nearest lexical option at 0.87 | L2, L3, L9 |
| [eco-jeff-order-sensitivity-issue4](eco-jeff-order-sensitivity-issue4.md) | reproducible bug, n = 1 | B | Question order changes jeff's answer (shared pass) | L7 |
| [eco-jev-none-option-and-oos-studies](eco-jev-none-option-and-oos-studies.md) | 4 independent small evals | B | Hosted Jev: 0/30 OOS flagged without a `none` option; 0.950 → 0.000 when `unknown` is removed; 0/400 order flips | L2, L3, L5, Q5 |
| [eco-jev-injection-other-studies](eco-jev-injection-other-studies.md) | independent evals | B | Hosted Jev resists blunt overrides (0/30), but a false-fact line drops accuracy from 96.5% to 26.5% | L4 |
| [eco-jev-calibration-audits](eco-jev-calibration-audits.md) | independent evals | B | Jev error-ranking AUROC 0.73 (CLINC150), 0.85 (Banking77) | L8 |
| [eco-jevbench-hard-tier](eco-jevbench-hard-tier.md) | benchmark, author submissions | C | Composite cannot separate rejection/injection; jeff ≈ Laya | Q1 |
| [eco-positive-deployments-entagl-arize](eco-positive-deployments-entagl-arize.md) | commercial case studies | C | Gated use with escalation: 88% coverage at 99.75%; human band for spam | positive |
| [eco-sotaaz-jeff-vs-jev](eco-sotaaz-jeff-vs-jev.md) | blog | C | "Jeff" there is Qwen3.5-based: a **name collision**, not logan-markewich/jeff | — |
| [lit-nota-abstention-mcq](lit-nota-abstention-mcq.md) | paper (28 LLMs) | **A** | "None of the above" correct → 30–50% drop regardless of scale | L2, L3, Q1, Q5 |
| [lit-selection-bias-zheng](lit-selection-bias-zheng.md) | papers | **A** | Option-position bias. Shrinks with size in Llama-2 (RStd 23.0 → 4.1), non-monotonic in Vicuna | L5, Q8 |
| [lit-oos-intent-detection](lit-oos-intent-detection.md) | papers | B | LLM OOS detection depends on label breadth; a trained small SetFit with negatives is competitive | L2, L3, Q3 |
| [lit-prompt-injection-classifiers-judges](lit-prompt-injection-classifiers-judges.md) | preprints | B | Small judges are more injectable (Gemma-4B 66.7% vs GPT-4 32.4%); DistractionIF shows inverse scaling (Qwen3 0.6B 66% → 235B 37.6%) | L4, Q1 |
| [lit-scaling-and-distractors](lit-scaling-and-distractors.md) | papers | B | Irrelevant context hurts; some size trends are U-shaped | L6, Q8 |
| [lit-nli-zeroshot-lexical-overlap](lit-nli-zeroshot-lexical-overlap.md) | papers (partly via summaries) | C | Entailment classifiers lean on lexical cues; raw scores are not confidence | L4, L1, Q2 |
| [lit-multilingual-zeroshot-nli](lit-multilingual-zeroshot-nli.md) | paper | B | English hypotheses beat target-language ones (no Japanese tested) | L9 |
| [use-clinc150-oos](use-clinc150-oos.md) | peer-reviewed + public data | **A** | ~96% in-scope accuracy but 40–59% OOS recall | L2, L3, L8 |
| [use-hint3-real-chatbot-oos](use-hint3-real-chatbot-oos.md) | paper + public data (vendor authors) | **A**− | Real traffic: NLU platforms give OOS high confidence | L2, Q7 |
| [use-injecguard-overdefense](use-injecguard-overdefense.md) | paper + released data | B | Trigger-word shortcut: PromptGuard 86M flags benign text | L4 analogue |
| [use-intent-router-banking77](use-intent-router-banking77.md) | single-author eval, scripts | B | Fine-tuned XLM-R beats Claude on closed set; negatives generalise poorly to unseen off-topic types | L2, L3, Q3, Q5 |
| [use-laya-intent-router](use-laya-intent-router.md) | author eval | C | Training on episodes with the correct option removed: OOS recall 0.68 → 0.99 (same-process test data) | L2, L3, Q3, Q6 |
| [use-zeroshot-llm-41-models](use-zeroshot-llm-41-models.md) | preprint | B | Instruction tuning > scale for intent; none > 80% on real sets | Q1, Q4 |
| [use-nemo-guardrails-topical](use-nemo-guardrails-topical.md) | vendor paper | C | In-scope intent only; example-count sensitive | L1, Q4 |
| [use-setfit-fewshot](use-setfit-fewshot.md) | author paper | C | Small fine-tuned encoders competitive on closed sets; no OOS | Q3 |
| [scale-kev-size-ladder](scale-kev-size-ladder.md) | author eval, frozen suites | B | Same recipe 0.8/4/9B: big 0.8 → 4B gain, small 4 → 9B; injection-source 0.55 → 0.75 (Jev 0.89) | Q1, Q8 |
| [scale-decider-size-ladder-and-stock-readout](scale-decider-size-ladder-and-stock-readout.md) | author eval | B | Size helps modestly; stock Gemma-4-12B via the same readout ≥ trained models | Q1, Q3, Q4 |
| [scale-jevbench-cross-model-and-jeff-hard-tier](scale-jevbench-cross-model-and-jeff-hard-tier.md) | benchmark artifacts | B | Encoders 35–39% hard tier; abstain items: jeff 0/7, stock Gemma-12B 13/14 | Q1, Q4 |
| [scale-semif-minijev-jevmlx-llm-readers](scale-semif-minijev-jevmlx-llm-readers.md) | author evals | C | Reader accuracy rises with size (0.44 → 0.96) with quantization confounds; letters vs names swings 10–50 points | Q4, Q8 |
| [scale-anyjev-qwen3-label-heads](scale-anyjev-qwen3-label-heads.md) | author eval | C | Zero-label 0.49 (1.7B) → 0.70 (32B); a fitted head closes most of the gap | Q1, Q3 |
| [scale-gliformer-base-vs-large](scale-gliformer-base-vs-large.md) | model cards + jeff probe | B | Only base (264M) and large (576M) exist; no larger GLiFormer | Q1 |
| [scale-trained-encoders-zero-shot-gap](scale-trained-encoders-zero-shot-gap.md) | mixed author audits | C | In encoders, training data > size (GLiNER2.5-Decide 1B ≤ 340M) | Q3 |

## Coverage summary
- **Similar to local L2/L3** (non-orders accepted, missing option replaced): many independent reports across encoders, hosted Jev without a `none` option, classic NLU, and LLMs.
- **Similar to local L4:** instruction-steering is widely reproduced, but the specific *option-key-naming* override has no external report and no published injection test of jeff or GLiFormer.
- **Contradictions recorded rather than resolved:**
  - jeff's README size ("400M") vs the GLiFormer card and local file (575.6M).
  - mini-jev vs jevmlx on letter- vs name-based readout.
  - Laya and jeff show large option-order effects; hosted Jev shows none.
  - Kev injection robustness is non-monotonic between 4B and 9B, while its ability to use a defence grows with size.
