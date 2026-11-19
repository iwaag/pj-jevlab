# Decider 0.8B/2B/4B/35B-A3B plus stock instruct models read through the same logit readout

- **Sources:** https://github.com/Mapika/decider `README.md` (sections "JevBench", "Decision Index", "Where Jev leads", "Models" table, "Runs on"); HF API `https://huggingface.co/api/models/Mapika/decider-{0.8b,2b,4b,12b,35b-a3b}` (accessed 2026-10-02). Third-party leaderboard figures are quoted by the author from Benchmark Heaven JevBench v1.5.2 and the Decision Index v0.2.1; not re-checked at the leaderboards.
- **Evidence type:** author/vendor evaluation (own runner plus leaderboard rows). Author independence: no. Leaderboard rows are produced by third-party harnesses but were relayed by the author.
- **Model / base / checkpoint:** `Mapika/decider-0.8b` (Qwen3.5-0.8B-Base; 752,393,024 params BF16), `decider-2b` (Qwen3.5-2B-Base; 1,881,825,088), `decider-4b` (Qwen3.5-4B-Base; 4,205,751,296), `decider-35b-a3b` (Qwen3.5-35B-A3B-Base; 34,660,610,688 total), `decider-12b` (stock Gemma-4-12B-it in v1, v2 adds a merged state-tracking LoRA; 11,959,730,224), `decider-chat-gemma4-31b` and `decider-chat-qwen3.6-27b` (stock instruct models, fitted temperatures). All Apache-2.0; last modified 2026-09-22 to 2026-09-29.
- **Architecture / readout:** hidden state at each answer slot projected to one label token per option (letters), softmax at fitted temperature, one pass. Trained models use CE fine-tuning (full/partial) on ~1.47M examples (about 95 public datasets plus Qwen3.5-27B teacher labels); 35B uses frozen-expert Muon training that the author flags as possibly harmful.
- **Task / language:** typed decisions, English. **Rejection mechanism:** none specific.
- **Data provenance:** JevBench public items and sealed set, Decision Index panels, author regression set. **n:** JevBench public hard tier 111; others not recorded here.
- **Relevant local classes:** Q1, Q3, Q4, Q8, L5 (order)

## What the source reports
- JevBench public hard tier (111 items): decider-2b v11 0.577, decider-4b v2.1 0.649, decider-35b-a3b 0.676, stock Gemma-4-12B-it read with the Decider readout 0.730 (v2 with LoRA 0.712), Jev 0.730. Capacity helps, but the 35B MoE barely beats the 4B, and a stock 12B instruct model with no decision training equals Jev.
- JevBench v1.5.2 composite: Cygnet (stock Gemma-4-12B-it) 73.7 #1, Jev 72.1 #3, decider-4b v2 71.3 #7, decider-2b 45.1 #28, decider-35b-a3b 27.5 #41 (35B penalised for cost, not accuracy). Intelligence axis: 4b 55.8, 2b 42.3, 35b 60.5, Cygnet 71.1, Jev 72.0.
- Decision Index (chance-corrected): stock Gemma-4-31B-it via Decider chat readout 57.33 (#2, ECE 0.047), Jev 57.91; trained 35B (NVFP4) 47.11, 4B 40.70, 2B 28.97. Author's conclusion: the base model sets most of the score; stock instruct models read through the readout beat Decider's own trained 35B/4B/2B.
- Sealed yes/no (noul) items hold decider-4b v2 back (43 open vs 19 sealed, chance-corrected). Hard-item ECE 0.10-0.31 is stated as the weak axis.
- Apple Silicon: dense models 0.8B/2B(/2B vision) have a documented MPS path (PR #2): M1 Pro float16 median 133 ms vs 171 ms; MASSIVE Scenario accuracy 0.7553 / ECE 0.0438 vs published bf16 0.756 / 0.041. The 4B and 2B GGUF (Q4_K_M 2.7 GB / 1.3 GB, Q8_0, BF16) run via llama-cpp-python (Metal build mentioned); the HTTP server does not serve GGUF; optional `decider-ai[metal]` MLX kernel. Whether the 4B, 12B, 35B run on MPS is not stated in the README (unknown). `/v1/systemone` served by `decider.serve`.

## Strength and caveats
- Strongest single piece of evidence that, at fixed readout, a stock 12B-31B instruct model reads decisions better than small trained models, i.e. base-model capacity beats decision-specific training at these scales. Confounds: different bases (Qwen3.5 vs Gemma-4), different training stages per size, 35B MoE training flagged as suspect, leaderboard scores include cost/speed axes.
- No rejection/injection subset by size; the JevBench hard tier mixes abstain, long-policy, arithmetic and trap items.
