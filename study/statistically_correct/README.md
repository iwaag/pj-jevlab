# Useful systems from imperfect decisions: a cross-disciplinary literature survey

Compiled 2026-10-06 (episode `study/statistically_correct`). A literature survey: no model was run, and no simulator or experiment was designed. The 80–90% accuracy range comes from the [brief](../../devdocs/episodes/study/statistically_correct/braindump.md) as a design scenario; no source establishes it as a threshold. Sources were read by parallel searchers, some at abstract level only (each card says how much was read); I spot-checked three 2025–2026 papers against their arXiv abstracts. Recent AI work is searched up to 2026-10-06.

## Files

| File | Contents |
|---|---|
| [plan.md](../../devdocs/episodes/study/statistically_correct/plan.md), [braindump.md](../../devdocs/episodes/study/statistically_correct/braindump.md) | Plan and the unchanged brief |
| [framing.md](framing.md) | Definitions, local evidence inventory, unresolved assumptions A1–A8 |
| [search-log.md](search-log.md) | Queries, candidates, inclusion reasons, inaccessible sources, gaps |
| [evidence/](evidence) | 55 case cards (54 distinct cases) in four files: [stats and reliable computation](evidence/stats-and-reliable-computation.md), [control and collective behaviour](evidence/control-and-collective-behaviour.md), [game theory and stochastic optimisation](evidence/game-theory-and-stochastic-optimisation.md), [modern AI and games](evidence/modern-ai-and-games.md) |
| [catalog.md](catalog.md) | All cases with mechanism, evidence type, limitation and Jev relevance |
| [mechanisms.md](mechanisms.md) | Mechanism-by-error-structure matrix, conditions, failure boundaries |
| [synthesis.md](synthesis.md) | Cross-disciplinary reading: established, conditional, speculative |
| report1–6.md, [report.md](../../devdocs/episodes/study/statistically_correct/report.md) | Step reports and the final report |

## Short answers

- **Q1. What is an "error" without a unique correct action?** Five categories: task error, preference difference, uncertainty, deliberate randomisation, invalid action ([framing](framing.md)). The sources use "error" for different things: departure from truth (S-01, G-05), a faulty component (S-08, C-01), a human-likeness failure (M-13 to M-15), or a mismatch with a human distribution (M-05 to M-08). Quantal response (G-01) treats noisy choice as a model of behaviour, not as a fault.
- **Q2. When do many imperfect decisions give a satisfactory whole?** When errors are independent, or at least differ (S-03), when interaction keeps independent information alive (C-08), and the task has a truth or verifier. Shared and state-dependent errors defeat it (S-01 Theorem 3, G-06, S-04 to S-06, S-11). Effective sample size, not head count, matters (S-05).
- **Q3. Which mechanisms absorb or correct errors without improving the model?** Voting and averaging (absorb); coding, hierarchy and Byzantine protocols (correct, with explicit error models); constraints and feedback (thin evidence: M-09, M-12, M-13, M-15). Costs: extra decisions (5–40x for self-consistency, S-07), communication, supervision. Escalation has no card; only local leads.
- **Q4. When does variability help?** In structured, narrow settings with a no-noise comparison: scheduled annealing (G-08), uncertainty-driven exploration (G-09), partly correlated cues in small groups (C-09), cohesion in a flocking model (C-11), threshold systems (G-10). Nulls: G-11, M-17. No adequately sized player study shows entertainment gains from deliberate mistakes.
- **Q5. Can a modest statistical preference steer a population?** In models, yes, with thresholds: mild preferences give strong segregation (C-10), an informed minority leads (C-05), uninformed members can dilute a strong minority (C-06). Limits: sharp transitions and capture by a strongly opinionated minority. Mapping model scores to action probabilities is untested; reported confidence can be far sharper than human frequencies (M-07).
- **Q6. What makes the same system fail?** Correlated or state-dependent mistakes (S-04, S-05, S-06, S-11), cascades (G-03, G-04), amplified early noise (G-07), thresholds (C-04, S-08), homogenised or prompt-fragile populations (M-06, M-11), scale-dependent herding (M-10). Rare irreversible failures and distribution shift are not measured in any card.
- **Q7. What follows for Jev-style decision systems?** Nothing is demonstrated for Jev's own readouts in a population. Directly demonstrated (for generative LLMs) are correlation, homogenisation, over-sharp probabilities and prompt sensitivity; plausible transfers are effective-vote measurement, cascade risk, structured randomisation and steering by weak bias; reliability thresholds, resonance and "noise is entertaining" are speculative ([synthesis §5](synthesis.md)).

## Strongest supported mechanisms

1. Aggregation under diversity, and its failure under shared error (theorem plus several LLM measurements).
2. Interaction can absorb or amplify, and independence of information is the hinge (C-08, G-03, S-02).
3. Weak local bias steering with thresholds (C-10, C-05).
4. Structured, scheduled randomisation versus greedy or constant noise (G-08, G-09).

## Unresolved questions

- Error dependence of label-scoring and encoder readouts across states and agents.
- Sampling versus argmax in an interactive population; calibration for sampling.
- Whether deliberate mistakes improve player experience (only one weak null).
- Preference aggregation by model agents (only M-08).
- Escalation costs and benefits.
- Independent replication of most 2025–2026 preprints.

## Limits

Coverage target: 20–30 cases across at least six areas; reached 54 cases in eight areas, with weak items labelled. Not retrievable: primary W-MSR paper, Hingston 2009, Hajek's INFORMS copy (OCR copy used), Science/PNAS/Nature papers (403 or paywall; PMC or preprints used). Not searched or not opened: correlated-voter theorems (Ladha, Boland), Boids, self-stabilisation, gossip, stochastic-control stability, Costikyan and Lantz, evolutionary-algorithm mutation rates, Bishop 1995. No Japanese-language source was used. Missing evidence is a gap, not evidence of absence.
