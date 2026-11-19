# Prompt and option design for Jev-style decision models

Compiled 2026-10-03 (episode `study/prompt_best_practice/p1`). A source-based study: no model was run. Source claims, lab results and inference are kept apart in each file. Every external claim carries the readout it was shown on, because most prompting evidence comes from generative chat LLMs, while the lab's systems read option-letter logits (W12, A27), a pointer head (K27) or an encoder (J, G).

## Files

| File | Contents |
|---|---|
| [guidelines.md](guidelines.md) | 38 recommendations for Q1–Q6, each classed established, plausible or open, with practices to avoid and templates |
| [reinvention-check.md](reinvention-check.md) | Per-experiment verdicts, candidate next experiments, overall answer |
| [lab-evidence.md](lab-evidence.md) | The lab's own measurements by question, with strength labels |
| [search-log.md](search-log.md) | Queries, candidates, inaccessible sources, coverage and gaps |
| [evidence/q1-q2-instruction-and-options.md](evidence/q1-q2-instruction-and-options.md) | Instruction wording, distractors, option keys and descriptions |
| [evidence/q3-order-and-format.md](evidence/q3-order-and-format.md) | Option-order bias, debiasing, calibration, format |
| [evidence/q4-second-passes.md](evidence/q4-second-passes.md) | Self-correction, verification, voting, elimination |
| [evidence/q5-abstention.md](evidence/q5-abstention.md) | Abstention, "none of the above", missing information |
| [evidence/q6-readout-and-vendor.md](evidence/q6-readout-and-vendor.md) | Encoder, scorer and vendor evidence |

Related existing notes: [benchmark/robustness-and-execution.md](../benchmark/robustness-and-execution.md), [landscape/calibration.md](../landscape/calibration.md), [landscape/llm-as-classifier-logits.md](../landscape/llm-as-classifier-logits.md), [landscape/zero-shot-classifiers.md](../landscape/zero-shot-classifiers.md), [close/jev.md](../close/jev.md).

## Short answers

- **Q1 Instructions.** Wording and format sensitivity is well documented, mostly on generative or base models, and is task-dependent. No source compares terse and full instructions on logit, pointer or encoder readouts. Rules placed in the question hurt one small trained model (Decider author probe). Details: [guidelines Q1](guidelines.md).
- **Q2 Options.** Symbol swaps do not remove the option-ID prior for letter-logit readers. Description and elaboration help on some tasks and not on others. A closed list without a fallback option pushes models to answer. Nothing was found for pointer heads or GLiNER2-style label descriptions.
- **Q3 Order.** Selection bias is largely a prior on the option-ID token. Permutation averaging and PriDe-style prior estimation (about 5% of items) are the known countermeasures, and voting over orders gives a few points. Part of the measured bias is a first-token-logit readout artifact. No published precision or recall exists for order disagreement as an error flag.
- **Q4 Second passes.** Intrinsic self-correction and re-asks give no gain or a loss. Gains need an independent signal. Unweighted votes suffer from correlated errors. Option elimination on option-ID logits is the one positive result close to W12 and A27.
- **Q5 Abstention.** Models answer rather than abstain, and missing-information detection is the weakest case. Abstain clauses trade coverage for abstention and are model-dependent. Max-softmax thresholding works on letter-logit readouts. Encoder and span scorers depend heavily on training with negatives.
- **Q6 Readout dependence.** Chain of thought, verbalised confidence and self-reflection are generative-only. No controlled external study covers pointer-head or trained decision models.
- **Q7 Reinvention.** Mostly not reinvention, but not mostly new. The phenomena are known; the readouts are new. Wording vote, shown verification, model vote and the K27 narrowed re-asks were predictable from published work. Missed methods: multi-paraphrase distributions, permutation averaging or PriDe, and a margin baseline for the D2 order flag. See [reinvention-check.md](reinvention-check.md).

## Limits

Many sources were read through a fetch summary or at abstract level, and several are 2026 preprints. Each evidence note marks which. "No source found" is not proof that no work exists.
