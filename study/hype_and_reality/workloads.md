# Which workloads succeed, under what conditions, and where they fail

Written 2026-10-02. It is based on the graded [evidence index](evidence/README.md) and the [local failure taxonomy](local-failures.md). Each row is labelled as follows:
- **Source:** what a cited source reports, with its grade.
- **Local:** what we measured.
- **Inference:** our reading.

Where no concrete evidence exists, the cell says so.

## Dimensions that matter
| Dimension | Easier end | Harder end | Evidence |
|---|---|---|---|
| Label set | Closed, in-distribution labels with many training examples | Open world: inputs may belong to none of the labels | CLINC150 (A): ~96% in-scope vs 40–59% OOS recall. HINT3 (A−). Banking77 router (B) |
| "None" representation | Trained abstention or negative episodes, explicit `none` option the model was trained to use | `none`/`clarify` as just another zero-shot label, or no such option | laya-intent-router (C): 0.68 → 0.99 OOS after removed-gold training. Hosted Jev (B): 0.950 → 0.000 when `unknown` removed. Tam et al. (A): 30–50% drop when NOTA is correct, regardless of scale. Laya issues (B): `none` present but ignored |
| Distance of the negative | Far off-topic (recipes, gibberish) | Adjacent: requests for a near-neighbour action, domain neighbours | Banking77 router (B): insurance 75% and held-out neighbours don't transfer. Local L3 (9/24). Von #21 (B) |
| Text-to-label relation | Semantic match is the task (spam, topic, intent paraphrase) | The input mentions a label word but means something else (negation, override, quotation) | Laya #377 (B): "do NOT cancel" → cancel. Local L4 (13/14). InjecGuard (B): trigger-word over-defense |
| Input trust | Inputs written by cooperative users or internal systems | Attacker- or player-controlled text | cwhy bench (A): flip rates span 0.09% to 63% across models |
| Context length / extra text | Short, focused `state` | Long state, irrelevant lines, multiple questions per pass | Local L6 (visible state: 23 new failures), L7. Laya controls in cwhy (A): "any added text" flips ~50%. GSM-IC (B) |
| Reasoning requirement | Similarity / paraphrase | Prerequisites, arithmetic, dates, multi-hop, policy application | JevBench hard tier (B): encoders 35–39%, 4B LLM reader 61%, Jev 73%. Kev (B): date arithmetic weak at every size |
| Consequence of error | Advisory, reversible, or confirmed by a human; low-confidence escalation | Automatic irreversible execution | Entagl/Arize (C): gated use with escalation. jev-engineering (B): regex rules first, fails open to prompt |

## Workload comparison
| Workload | Observed outcome | Evidence strength | Conditions that made it work | What remained | Implication for Blackout Dispatch |
|---|---|---|---|---|---|
| **Closed-set routing / intent classification, in-distribution** | Works well. Fine-tuned XLM-R 94.2% beats Claude Sonnet 85.3% on Banking77; hosted Jev 98.5% on labelled routing tests; SetFit competitive with few labels | B/C (single-author and commercial; SetFit author paper) | Task-specific training data, or a strong hosted model; in-scope inputs only | OOS not measured in most reports | Our real-order accuracy (88–92% fresh, 0–1 wrong job) is this regime and is acceptable |
| **Out-of-scope rejection with a threshold** | Partial. Banking77 router 86.7% unseen-OOS recall at 6.6% false rejection; CLINC150 BERT 40–59%; threshold behaviour erratic across models | A/B | Threshold tuned against an explicit false-rejection budget; negatives of varied kinds | Adjacent-domain inputs pass; confidence on OOS can be high (HINT3, Laya ≥ 0.9) | Local margin AUC 0.73; a threshold cannot remove key-naming overrides (margins 0.36–0.62) |
| **OOS rejection with trained abstention / negative episodes** | Large gains reported: laya-intent-router 0.68 → 0.99; hosted Jev uses an `unknown` option at 0.95 | C (author, same-process test) / B | Training episodes with the correct option *removed* (exactly our L3); explicit abstain label | Small menus (2 options) still map filler to an option; unseen adjacent negatives transfer poorly | Most direct candidate fix for L2/L3, but needs a model trained this way (jeff/GLiFormer is not) |
| **Moderation / spam with a human band** | Works as a product. Arize: uncertain 0.3–0.7 band to a person, rest at 99.5% | C | Human review of the uncertain band; in-distribution data | No adversarial input tested | Analogous to our confirmation step: product tolerates errors, model not improved |
| **Gated cascade (small model → large model / human)** | Entagl: 88% coverage at 99.75% accuracy; but system1-system2 found injections *lowered* Jev confidence and the hybrid got worse | C / B | Errors must have low confidence to be escalated | Adversarial errors with high confidence pass, or the gate escalates much normal traffic (jev-engineering: a 0.8 floor escalated 58%) | Our key-naming overrides have high margins, so a cascade on margin would not catch them |
| **Injection / instruction-steering resistance** | Strongly model-dependent: hosted Jev 0.09%, Winnow-12B 3.0%, SemIf-4B 27.4%, Laya 49–63% | A | Large or well-trained models; for Jev, a policy line saying embedded commands are content | Plausible false facts still work on Jev (96.5% → 26.5%); defences hurt Kev-0.8B | Player text is untrusted by design; small encoders should not be assumed robust |
| **Prompt-injection detection classifiers** | Trigger-word shortcuts: PromptGuard 86M flags almost all benign trigger-word texts; Llama-Guard-3 misses most attacks | B | De-biased training (InjecGuard) | Size alone or an LLM alone did not fix it | Mirror image of our L4: lexical-match errors are a classifier-class property |
| **Reasoning-heavy decisions** (prerequisites, multi-hop, long policy, arithmetic) | Encoders fail (35–39% hard tier), 4B LLM readers mid (61%), stock 12B instruct ≈ Jev (73%) | B | Base-model capacity | Date arithmetic and knowledge remain weak even at 27B (Kev) | Our game keeps prerequisites in code. That is correct and should stay |
| **Non-English** | Laya Romanian 50–55%, Chinese 60–70% (n = 20); Entagl Jev Turkish/Arabic 96–98%; English hypotheses beat target-language ones in NLI | B/C | Multilingual training (Jev, Malkuth) | Small English-centric encoders degrade | Local L9 matches; Japanese needs a separately chosen model |
| **Game NLU with confirmation / rejection** | **No inspectable report with measured rejection or confirmation outcomes was found** | — | — | — | Our ex1 result (0 state changes in 1,307 submissions; 38–44% wrong proposals on non-orders) is itself the best available data point |

## "The classifier works" vs "the product tolerates its errors"
| System | Model quality evidence | Product-side safeguard | Which one carries the result |
|---|---|---|---|
| Entagl routing | 98.5% labelled, 84–91% agent selection on real traffic | Confidence gate + escalation to larger models | Mostly the safeguard on hard traffic |
| Arize spam | 98.3% (≈ TF-IDF baseline) | Human band 0.3–0.7 | Both; the model is not better than a trained baseline |
| jev-engineering shell gate | Blunt overrides 0/30, authority claims 3/30 | Regex hard rules first; fails open to normal permission prompt | Safeguard |
| Banking77 router | 94.2% in-domain; 86.7% OOS at 6.6% FRR | LLM escalation below threshold | Both |
| **Blackout Dispatch ex1** | 88.9–91.7% clear intent; 56–63% non-orders rejected | Legal-option filtering, margin gate, confirmation | **Safeguard** for cost; the classifier is unchanged |

## Where the evidence cannot support a conclusion
- **Scale and the specific local failures:** no source measures greetings accepted as an action (L2), unavailable-action substitution (L3), or key-naming overrides (L4) as a function of model size within one family. Kev's injection subset (0.8B 0.55 → 4B 0.75) and malkuth's abstain items (2B 4/14 → 4B 8/14) are the nearest analogues, on different tasks.
- **Why** zero-shot encoders accept off-topic text: the lexical-overlap literature (graded C here) is consistent with L4, but no source dissects GLiFormer.
- **Human vs authored inputs:** HINT3 shows real traffic is harder than curated sets. Whether players phrase orders more or less adversarially than our authored cases is unknown.
- **Confirmation in games:** no measured precedent. Whether players notice wrong proposals remains a playtest question.
- **Success tendencies in games** cannot be stated from external evidence. The game demos found in [study/game](../game/README.md) did not measure rejection.

## Practical guidance (inference)
1. Use small zero-shot decision models where every input is expected to belong to one of the labels, and where a wrong label is cheap or reviewed.
2. Do not rely on a competing `clarify`/`none` label or a margin threshold to reject untrusted input with a zero-shot encoder. Either train for abstention (removed-gold episodes, varied negatives), or keep rejection in code and interaction (confirmation, explicit job controls).
3. Do not put option identifiers that a user could type into the text the model scores. Treat any classifier that sees user text as injectable unless it was tested otherwise.
4. Keep prerequisites, legality and arithmetic in code. Even large decision models are weak there.
5. When comparing models, report false acceptance on non-orders at a fixed false-rejection budget, not just top-1 accuracy or a shared threshold (the Banking77 author's corrected method).
