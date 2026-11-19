# AnyJev: Qwen3 1.7B/4B/8B/30B-A3B/32B on typed-decisions with a zero-label vs label-fitted readout

- **Sources:** https://github.com/nokia-applied-research/AnyJev `README.md` (table following "Qwen3-8B, BANKING77 20-way" and the typed-decisions table, "Limitations"); repo metadata via gh api (accessed 2026-10-02)
- **Evidence type:** author evaluation. Author independence: no. Gold is a teacher LLM (mean of three samples), teacher self-agreement 0.735 per README.
- **Model / checkpoint:** Qwen3-1.7B, 4B, 8B, 30B-A3B, 32B (base models keep their own licences; heads for all five ship in-repo as 1.8-4.4 MB files). Repo Apache-2.0, pushed 2026-09-28, ~998 stars.
- **Task:** `LocalLLaMA/typed-decisions` (20 questions x 300 labels, 2,000 held-out decisions) and BANKING77-20. **Readout:** next-token option letters (raw), L0 rotation-averaged zero-label, L1 temperature, L2 closed-form head on a mid-depth hidden state (needs 100-300 labels per question).
- **Rejection mechanism:** none; abstention only via confidence ("auto-decidable at 5% risk").
- **Raw cases available:** committed JSON per README claim.
- **Relevant local classes:** L5 (order), Q1, Q8

## What the source reports
- typed-decisions accuracy, L0 -> L2: 1.7B 0.494 -> 0.730; 4B 0.564 -> 0.786; 8B 0.647 -> 0.771; 30B-A3B 0.630 -> 0.799; 32B 0.700 -> 0.798. Scale helps the zero-label readout markedly (0.49 -> 0.70) but a label-fitted head erases most of the gap (0.73-0.80) and the 4B/8B order inverts.
- BANKING77-20 on Qwen3-8B: order-flip rate raw 0.230 -> L0 0.073 (rotation averaging); accuracy 0.747 -> 0.803. Order bias is a readout property reducible without a larger model.
- Supported backends: transformers and vLLM; the README does not mention Apple Silicon/MPS or MLX (unknown), no `/v1/systemone` server.

## Strength and caveats
- Useful for Q1/Q8: the scale effect depends strongly on whether labelled fitting is allowed; L2 is per question and per model and needs labels. Teacher-LLM gold means "accuracy" is agreement with a teacher.
- Not tested on rejection or injection; the data are 4-workflow typed-decisions plus Banking77.
