# Kev 0.8B / 4B / 9B / 27B: the cleanest same-recipe size ladder, with rejection-adjacent subsets

- **Sources:** https://github.com/jaredpalmer/kev `README.md` (sections "Models", accuracy table, "What to Expect", "Limits"); model cards `docs/model-cards/kev-0.8b.md`, `kev-4b.md`, `kev-9b.md`, `kev-27b.md` (tables "Other results", "Out-of-domain", "Unanswerable items answered with p >= 0.9"); HF API `https://huggingface.co/api/models/jaredpalmer/kev-{0.8b,4b,9b,27b}` (all accessed 2026-10-02)
- **Evidence type:** author/vendor evaluation (paired-bootstrap tooling, frozen suites, claims CI). Author independence: no.
- **Model / base / checkpoint:** `jaredpalmer/kev-0.8b` (base Qwen3.5-0.8B-Base, LoRA r16 + pointer head), `kev-4b` (Qwen3.5-4B-Base, adapter ~130 MB per tree listing), `kev-9b` (Qwen3.5-9B-Base, adapter ~173 MB), `kev-27b` (Qwen3.8-27B post-trained, full weights, HF safetensors 25,624,600,064 params BF16, tree total about 51.3 GB). All Apache-2.0; HF last modified 2026-10-01. Adapters need the Qwen base downloaded separately (Qwen3.5-0.8B-Base 873M, 4B-Base 4.66B, 9B-Base 9.65B params).
- **Architecture / readout:** pointer head over `</opt>` hidden states vs `<decide>` hidden state, softmax over options, fitted temperature. Same CE recipe and data (`decision-v7` plus follow-up stages) for 0.8B/4B/9B; 27B is full fine-tune on a different 145,840-record corpus from a post-trained base (confound).
- **Task / language:** typed decisions (choice/noul/score), English. **Rejection mechanism:** "none of the above" options and minimal pairs with the correct option removed are inserted in training; there is no separate abstain head.
- **Data provenance:** held-out public datasets (transfer-v4, breadth-v1), generated suites, evaluation-only sources (When2Call, a prompt-injection source, JevBench public items). **n:** transfer-v4 656; devtools-v1 prompt-injection and When2Call dev sets (n per set is in the cards, not recorded here); JevBench public 231 / hard 111.
- **Configuration:** fp32 evaluation path; bf16 serving differs by up to ~0.03 probability (GPU) / 0.05 (Mac) and changes the top answer on about 1 in 300 questions.
- **Raw cases available:** partial (frozen suites at HF dataset `jaredpalmer/kev-suites`, updated 2026-09-30; `runs/` in repo).
- **Fixed / mitigated?** n/a
- **Relevant local classes:** L2, L3, L4 (via prompt-injection/When2Call/unknowable sets), Q1, Q3, Q8

## What the source reports
- New-source accuracy (dev / test): 0.8B 0.648/0.697, 4B 0.817/0.838, 9B 0.820/0.852, 27B 0.851/0.889; Jev (dev only, author-run via Vercel AI Gateway) 0.857. Going 0.8B -> 4B gives about +17 points; 4B -> 9B about +0.3 dev / +1.4 test (diminishing); 9B -> 27B about +3 dev, but the 27B has a different base and corpus.
- Decision Index (chance-corrected, breadth-v1 test): 0.8B 23.3, 4B 38.0, 9B 41.0, 27B 52.3, Jev 54.0.
- JevBench public items (4B card): all 231 = 0.758, hard tier 111 = 0.541 (ECE 0.112); 0.8B card: 0.636 and 0.360 (ECE 0.181). The 0.8B card says the documents-and-skills stage moved its hard tier +2.7 pp with an interval spanning zero.
- Rejection-adjacent subsets (evaluation-only sources): prompt-injection dev accuracy 0.8B 0.547, 4B 0.753, Jev 0.893 (the 9B and 27B cards, as read, do not list this row). When2Call (tool-call routing incl. decline): 0.8B 0.167 dev / 0.133 test (below the 1-in-4 chance; the card says "do not use for tool-call routing"), 4B 0.660 dev.
- "Unanswerable items answered with p >= 0.9" is 0.00 for all four sizes vs Jev 0.09 (transfer-v9 development, deciding evidence removed). README: Kev-9B 0%, Jev 9%.
- Weak at every size: date arithmetic `deadline` policy 0.8B 0.35, 4B 0.65, 9B 0.725 vs Jev 0.95; MMLU-Pro 0.8B 0.230, 4B 0.565, 9B 0.590, 27B 0.675 vs Jev 0.840 ("knowledge is set by the base"). So larger Kev models still fail on knowledge and arithmetic items.
- Apple Silicon: README documents MLX backend (auto on Mac); five questions over a ~270-token text on an M5 (32 GB): 0.8B 149 ms (28 ms cached), 4B 721 ms (136 ms cached) in bf16. 27B on Mac is "expected, not measured" (a user ran the earlier adapter version on a 128 GB M5 Max, PR #175). 9B "expected, not measured".

## Strength and caveats
- Best available evidence that capacity helps out-of-domain accuracy and that the 4B->9B step is small, on identical recipe/readout. The injection and abstention numbers are the closest published analogue of L2/L4, but they come from a different task (developer-tool / security text), different option sets, not from a "key named in the text" attack.
- Numbers are author-measured against author-run Jev; Kev was trained with abstention twins so the zero unanswerable-confident rate is partly in-distribution behaviour.
- Does not show that a bigger Kev rejects small talk or unavailable-job requests: neither was measured.
