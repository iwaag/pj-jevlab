# modernbert-ja-310m-jev / Jev Local (Argos1111)

- **Category**: open
- **Owner / org**: argos1111 (HF) / Argos1111 (GitHub `jev_local`)
- **URLs**: HF https://huggingface.co/argos1111/modernbert-ja-310m-jev ; code https://github.com/Argos1111/jev_local
- **License** (code / weights): weights CC-BY-SA-4.0 (inherits JGLUE/data share-alike; base sbintuitions/modernbert-ja-310m); repo license not checked
- **First release / last update**: HF created and modified 2026-09-19.
- **Popularity signals**: HF 1,080 downloads, 15 likes. GitHub stars for jev_local not retrieved (API lookup returned a different value on a separate query; unverified).

## Summary
A Japanese ModernBERT-310M cross-encoder fine-tuned as the ModernBERT backend of "Jev Local", a local `/v1/systemone`-compatible server. Included as the only Japanese-language encoder variant found; explicitly unofficial.

## Approach / architecture
`ModernBertForSequenceClassification(num_labels=1)`, CLS pooling; each (question+state, candidate) pair is a separate sequence and the per-candidate logits are softmaxed (listwise CE) into Choice / Score / Noul probabilities (Noul = candidates ["true","false"]). So cost is one sequence per option, not one pass for all options. Rendering format must match training (`質問: ...\n状況: ...`, `label — description`), 512 tokens.

## Interface
Served by Jev Local as a `/v1/systemone`-compatible API (`run_modernbert.sh`, `systemone_client.py`); or direct transformers use.

## Training & data
94,384 questions (~345k pairs) converted from JGLUE (JNLI, JCommonsenseQA), JCoLA, commonsense-moral-ja, MASSIVE etc.; 2 epochs, ~41 min on a single AMD Radeon AI PRO R9700 (ROCm). Test splits not used for training or validation.

## Reported performance
No accuracy, calibration or latency figures in the card text read. Author says it does not reproduce Jev's training or accuracy.

## Self-hosting notes
310M encoder; GPU (ROCm/CUDA) or CPU.

## Assessment
Niche but relevant for Japanese-language experiments; no evaluation evidence and share-alike licence constraint.

## Sources
- https://huggingface.co/argos1111/modernbert-ja-310m-jev (card + API)
