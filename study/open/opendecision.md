# OpenDecision

- **Category**: open
- **Owner / org**: deepanwadhwa (individual)
- **URLs**: https://github.com/deepanwadhwa/OpenDecision ; docs https://deepanwadhwa.github.io/OpenDecision/ ; PyPI `OpenDecision`
- **License** (code / weights): Apache-2.0 / uses third-party weights (MoritzLaurer zero-shot models; their licenses not checked here)
- **First release / last update**: created 2026-09-17, last push 2026-09-25; v0.1.2 "developer preview".
- **Popularity signals**: 57 GitHub stars.

## Summary
A Python library and FastAPI server that wraps existing zero-shot NLI-style classifiers into Jev-shaped primitives (Choice, Noul, Score) plus extras: `Relation` (supports/contradicts/unknown/conflicted) and a document pipeline with retrieval and evidence passages. No custom model training; its value is the decision/evidence layer.

## Approach / architecture
Default backend `MoritzLaurer/ModernBERT-large-zeroshot-v2.0`; optional `MoritzLaurer/deberta-v3-large-zeroshot-v2.0`. Zero-shot entailment scoring for each option/statement, no text generation. For documents: split, retrieve relevant passages, answer per question, return passages; Noul modes `binary`, `three_way`, `both` (confirmed / tentative / conflicted). README: "Treat the model scores as uncalibrated."

## Interface
Python `OpenDecisionEngine`; `opendecision serve` exposes `GET /health`, `POST /v1/systemone` (core TypeSafe request shape, usable as `base_url` for compatible clients), `POST /v1/documents/decide`, `/docs`. Requires Python >=3.13.

## Training & data
None (off-the-shelf zero-shot models).

## Reported performance
No latency/accuracy comparison vs Jev in README. Illustrative author experiments: synthetic insurance claim (17/17 facts retrieved, 10/10 composed decisions on one dev case); GDPR doc 9/10 objective questions correct (54k chars, 31 sections); Doom demo with fixed-seed recordings and "no win rate has been measured". Not independently verified; small, single-case examples.

## Self-hosting notes
`pip install OpenDecision`; model downloads from HF on first use; a large (395M) ModernBERT or DeBERTa-large encoder - CPU feasible, GPU faster.

## Assessment
Strengths: document-level evidence trail and conflict-aware Noul are conceptually interesting; permissive license. Weaknesses: no calibration (explicitly), no benchmark vs Jev, Python 3.13 requirement, NLI-based so scaling to many options costs one pass per option (inferred from zero-shot NLI design; not stated). Useful as a design reference for evidence-backed decisions, not as a calibrated Jev replacement.

## Sources
- https://github.com/deepanwadhwa/OpenDecision (README via gh api)
