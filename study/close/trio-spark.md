# Trio-Spark v1.0 (MachineFi)

- **Category**: close
- **Owner / org**: MachineFi
- **URLs**: https://github.com/machinefi/trio-spark ; https://platform.machinefi.com/spark ; https://huggingface.co/MachineFi/Trio-Spark-v1.0 (model card)
- **License** (code / weights): client code Apache-2.0; "model weights and training code are not publicly released"
- **First release / last update** (as seen 2026-10-01): ~2026-09-30
- **Popularity signals**: evaluation requests filed on jevbench, S1MB, jevfish; 100 free decisions for new accounts

## Summary
Hosted "Situated World Model": takes environment state and 2-8 candidate moves, returns the best move plus a probability for each, in one pass. Targeted at agents/robots; Choice is native, Noul/Score are described as projections.

## Approach / architecture
Undisclosed. Single pass, no free text.

## Interface
Hosted API, model id `trio-spark-preview`. Python client: `decide(task=..., state={...}, choices={"continue": "...", "slow": "...", "stop": "..."})`. Limits: 1,024 input tokens, one question per request, 2-8 choices, no silent truncation. $0.042/MTok input, no output charge.

## Training & data
Not disclosed.

## Reported performance
Vendor demos: drone 25 calls/65 s/0 collisions, browser agent 3 calls/4 s, robot arm 13 calls/13.7 s. Third-party preflight (jevbench issue, 120 items): 96.67% accuracy, ~0.51 s median; long-policy items returned 503. Small and not independently confirmed.

## Self-hosting notes
None.

## Assessment
Narrow (single question, 1K tokens) so not a Jev drop-in; useful as an example of a constrained hosted variant. Pricing mirrors Jev's.

## Sources
- https://github.com/machinefi/trio-spark
- https://github.com/fstandhartinger/jevbench/issues/166
- https://systemonemodels.tech/system-one-models
