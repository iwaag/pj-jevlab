# Ideas for the lab from the 2026-10-08 to 10-16 papers

Proposals, not results. "Offline" = computable from probabilities the lab has already logged. Numbering continues [../recent_study/ideas.md](../recent_study/ideas.md) as P-ideas.

| # | Idea | Source and evidence | Applies to | Cost |
|---|---|---|---|---|
| P1 | **Runoff re-reading for order**: score each option alone, keep the top few, compare them in listings where each candidate takes every position | 2610.18233 (open models and hosted Jev; ≈0 flips, accuracy within about a point of rotation averaging, 2.1× faster) | J, G, K27, W12, A27 | Two forward passes; replay on benchmark p3 reversal items |
| P2 | **Flip-instability gate**: defer when the pointwise top-1 probability is below ≈0.9 or when two listings disagree | 2610.18233 (over 90% of flips involve a top-3 option), 2610.19536 (flip AUROC 0.81–0.93; error AUROC 0.59–0.84) | Cascades in set4 | **Offline** if per-option probabilities were logged |
| P3 | **Fallback 2×2**: wording (Union vs Complement) by position of the fallback, on gold-fallback inputs | 2610.19856 (up to 39.8% change; position flips sign) | Every system with a "none/escalate" option | One short run on the W2 fallback items |
| P4 | **Finite-sample threshold selection (Learn Then Test)** with a "non-deployment" outcome when nothing certifies | 2610.19811 (7.8% budget violations vs 42–52%) | Replaces point-estimate τ of ideas A1/A2 | Offline on set3/p3/set4 logs |
| P5 | **Shadow-run threshold fitting** per decision type on the agent's own trajectories; report accuracy on "must-ask" states separately | 2610.21412 (fixed 0.5 −19.0 pt; fitted: 14.2% cost saved, no loss; 58.3% of must-ask correct) | game_test, set4 | Needs trajectories; the game_test logs may do |
| P6 | **Irrelevant-added-option probe** and a duplicate-question retest floor | 2610.22066 (10.9% vs 5.1% floor), 2610.16655 (0.20–0.52 nats) | All; qualifies set5 renormalisation | Small: add one off-domain option, re-ask |
| P7 | **Translate-to-pivot arm** for the Japanese collapse | 2610.14112 (+up to 37.2 pt on distant languages) | J, G, K27 on game_test p2 Japanese items | Machine translation plus one run |
| P8 | **Letter-logit baseline with temperature scaling**, raw and scaled, against the lab's pointer-head systems | 2610.17205 (raw 72.9, scaled 79.6 vs Jev 80.1) | Class D baseline | One local model run |
| P9 | **Label-channel check** (rename only the permissive option) for each system; check whether the release code feeds the key to the network | 2610.12292 (fail-open 93–100% where it does; VON/RLCD exactly unaffected) | Extends the two-call test of ideas B1 | Two calls per item |
| P10 | **Sampled decisions in populations** (draw from probabilities rather than argmax) in the school and survey-like settings | 2610.14912 (abstract-level) | set6 follow-ups | Offline |

What an experiment could settle: whether Runoff helps pointer-head 27B models (P1); whether the lab's fallback class design is wording-sensitive (P3); whether state-text key naming survives opaque keys on non-label-rendering models (P9 plus the original attack).
