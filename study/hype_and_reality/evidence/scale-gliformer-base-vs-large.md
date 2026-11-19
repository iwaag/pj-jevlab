# GLiFormer base vs large: same family, same card benchmark, plus jeff's own base/large probes

- **Sources:** https://huggingface.co/knowledgator/gliformer-base-v1 and https://huggingface.co/knowledgator/gliformer-large-v1 (model cards, section "Results"/classification table; HF API for sizes and dates); https://github.com/logan-markewich/jeff `bench/RESULTS.md` (sections "Noul context sensitivity" and "CPU arm") and `README.md` ("Model and backend settings") (all accessed 2026-10-02)
- **Evidence type:** author/vendor evaluation (Knowledgator card, same-protocol base/large table); author evaluation (jeff repo, a probe by the jeff author). Author independence: card = no (model author); jeff probe = yes (independent of Knowledgator, but it is the wrapper whose behaviour we are explaining).
- **Model / base / checkpoint:** `knowledgator/gliformer-base-v1` (card: 264.2M params; pytorch_model.bin 1,056,900,463 bytes; HF last modified 2026-09-14) and `knowledgator/gliformer-large-v1` (card: 575.6M params; pytorch_model.bin 2,302,735,855 bytes; HF last modified 2026-09-18). Both Apache-2.0, DeBERTa-based GLiFormer, library `gliformer`. **No small checkpoint exists:** HF API search for author knowledgator + "gliformer" returns only these two (access 2026-10-02); `gliformer-small-v1` returns "Invalid username or password" (not found).
- **Task:** (card) 13-dataset text classification with labels supplied at inference; (jeff) 24 noul questions on support messages.
- **Rejection mechanism:** none evaluated in either source.
- **Data provenance:** public datasets (card); 12 short support messages x 2 yes/no questions written by the jeff author.
- **n / metrics:** card: classification mean macro-F1 over 13 datasets, 79,828 examples. jeff probe n = 24 nouls.
- **Fixed / mitigated?** not applicable.
- **Relevant local classes:** Q1, Q8, L1-L4 (indirect only); L7

## What the source reports
- Same-protocol vendor table, base -> large: mean classification macro-F1 72.36 -> 75.03; banking77 acc 67.21 -> 70.97; sst5 38.05 -> 44.34; 20_newsgroups 48.67 -> 57.94; ag_news 82.59 -> 82.07 (large slightly lower); emotion 53.55 -> 54.75. Large is about 2.2x the parameters for +2.7 macro-F1 points on generic classification.
- The card does not report rejection, out-of-scope, injection or adversarial results for either size.
- jeff author's probe: `gliformer-base-v1` cannot answer yes/no (noul) questions in any variant (best 0.67 accuracy with `single` rendering, 0.38 with default `yes_no`), and the jeff docs recommend base for tests only. Large reaches 0.79-0.83 once questions are isolated.
- jeff docs wrap large as "400M parameters", but the model card says 575.6M; the local 2.2 GB fp32 file matches 575.6M x 4 bytes (arithmetic, not a stated fact in the sources).
- On CPU, jeff's own benchmark lists large with 296 ms (ONNX int8, Modal 8-core) vs base 137 ms; on M2 Max large on torch-mps was 94 ms; base was not run on MPS.

## Strength and caveats
- Supports only: a mid-sized step up inside one family gives a modest generic-classification gain. It says nothing about L2/L3/L4 behaviour, which nobody has measured per size.
- Base vs large differ in whatever training changed between releases; the card does not say they share data/steps (unknown).
- There is no third (small) size and no larger GLiFormer on HF, so a scale ladder for the current wrapper stops at large.
