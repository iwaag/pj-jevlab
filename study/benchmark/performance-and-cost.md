# Performance and cost measurement

How to measure latency, throughput, memory and cost so that results are comparable and reproducible. Written 2026-10-02 in step5 of [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md).
- Citations link to [evidence/](evidence/).
- **"(derived here)"** marks arithmetic or synthesis made for this note.
- How quality and cost are combined in a decision is discussed in [metrics.md §10](metrics.md).

## 1. Define the scenario before the metric
A latency number means nothing without the load that produced it. MLPerf Inference defines four scenarios [reddi2020mlperf](evidence/F-robustness-frameworks-perf.md#reddi2020mlperf) [mlperf-rules](evidence/F-robustness-frameworks-perf.md#mlperf-rules):

| Scenario | Load | Metric |
|---|---|---|
| **Single-stream** | One query at a time; the next is sent when the previous completes | Tail latency: 90th percentile, with an early-stopping estimate in the current rules |
| **Multistream** | Fixed-size groups of samples per query | 99th-percentile latency |
| **Server** | Poisson arrivals (open loop) | Maximum arrival rate that meets a tail-latency bound |
| **Offline** | All samples available at once | Throughput (samples/s) |

- **A sequential, single-client run measures only single-stream latency** (derived here). It says nothing about throughput under concurrency or about tail latency at load.
- **Report the load model:** sequential, a fixed concurrency, or open-loop Poisson at rate λ.
- **Batching raises throughput and hardware utilisation but raises per-request latency** [pope2023scaling](evidence/F-robustness-frameworks-perf.md#pope2023scaling) [kwon2023paged](evidence/F-robustness-frameworks-perf.md#kwon2023paged). Compare systems at matched latency, or show the full curve against request rate [kwon2023paged](evidence/F-robustness-frameworks-perf.md#kwon2023paged).

## 2. Latency components for language models
- **Prefill vs decode.** Latency = prefill (process the input tokens) + decode (generate output tokens one at a time) [pope2023scaling](evidence/F-robustness-frameworks-perf.md#pope2023scaling).
- **Serving metrics.** These follow the same split. The definitions differ by tool, so cite the tool and its version [genaiperf-docs](evidence/F-robustness-frameworks-perf.md#genaiperf-docs) [vllm-bench-serve](evidence/F-robustness-frameworks-perf.md#vllm-bench-serve) [mlperf-rules](evidence/F-robustness-frameworks-perf.md#mlperf-rules):

| Metric | Definition | Note |
|---|---|---|
| **TTFT** | Time from sending the request to the first token | Dominated by prefill and queueing |
| **TPOT** | (end-to-end latency − TTFT) / (output tokens − 1) | vLLM's form; MLPerf constrains TTFT and TPOT |
| **ITL** | Time between successive streamed chunks, divided by tokens per chunk | GenAI-Perf's form; differs subtly from TPOT |
| **End-to-end latency** | Request sent → final response | What a caller waits for |
| **Request / token throughput** | Completed requests (or output tokens) / benchmark duration | Depends on the load model |
| **Goodput** | Requests that meet *all* latency targets / duration | vLLM; ties throughput to service-level objectives |
| **Normalised latency** | Mean of (end-to-end latency / output length) | Used to compare serving systems across request rates [kwon2023paged](evidence/F-robustness-frameworks-perf.md#kwon2023paged) |

- **Decision models that return no generated text** (a single forward pass with a readout) have no decode phase. For them, end-to-end latency per request, and per question when several share a request, are the relevant measures (derived here).
- **Input size, output size and question count drive latency.** Report latency as a function of these, on a fixed grid, not as one average over a convenience set (derived here).
- **HELM models runtime** as F(prompt size) + g × (output tokens) [liang2023helm](evidence/F-robustness-frameworks-perf.md#liang2023helm).

## 3. Cold vs warm, caches and measurement overhead
**Cold-start phases** (derived here; measure each separately):
1. process spawn;
2. model load;
3. first valid answer.

The first requests after load may include one-time compilation or allocation.

**Warm-up vs equilibrium:**
- MLPerf requires minimum run durations to reach a steady state: 60 s in the 2020 paper and 600 s for single-stream in the current rules [reddi2020mlperf](evidence/F-robustness-frameworks-perf.md#reddi2020mlperf) [mlperf-rules](evidence/F-robustness-frameworks-perf.md#mlperf-rules).
- A "warm" measurement must say how many requests came before it.

**Caches:**
- Prefix and KV caches make repeated or shared-prefix inputs faster.
- To measure uncached latency, use distinct inputs. To measure the benefit of caching, use deliberately repeated prefixes.
- Either way, state which one was measured (derived here).

**Measurement overhead:**
- Client-side timing includes transport, serialisation and the client's own processing.
- Server-reported timings, where available, separate them.
- Record both and state which clock is used (derived here).
- HELM separates two kinds of runtime because provider APIs mix hardware, software and contention [liang2023helm](evidence/F-robustness-frameworks-perf.md#liang2023helm):
  - **denoised runtime:** the provider's own stack, with noise removed;
  - **idealised runtime:** uniform hardware and software for every model.

**Nondeterministic batching on shared servers changes outputs as well as timings** [he2025nondeterminism](evidence/F-robustness-frameworks-perf.md#he2025nondeterminism).

## 4. Tail percentiles and sample size
**Why tails.** Under fan-out, rare slow requests dominate. If 1% of single-server requests are slow, a request touching 100 servers is slow 63% of the time (1 − 0.99^100) [dean2013tail](evidence/F-robustness-frameworks-perf.md#dean2013tail). Report p50, p90, p95 or p99 with the sample size, not only the mean.

**How many samples a percentile needs.** A distribution-free confidence interval for a quantile is a pair of order statistics [X_(j), X_(k)], chosen from the binomial distribution [leboudec2010perfeval](evidence/F-robustness-frameworks-perf.md#leboudec2010perfeval). Derived from that theorem here:

| Samples n | 95% interval for p50 | p90 | p95 | p99 |
|---|---|---|---|---|
| 40 | ranks 13–26 | ranks 32–40 (upper end = sample max) | **no interval exists** | **no interval exists** |
| 100 | 40–60 | 84–96 | 90–99 | **no interval exists** |
| 300 | 133–167 | 259–280 | 278–293 | 290–300 |

- **Construction:** the table gives the shortest pair of ranks with ≥ 95% coverage, which need not be equal-tailed.
- **Minimum n for any 95% interval,** using [min, max]: 6 (p50), 29 (p90), 59 (p95), 299 (p99). Such intervals put almost all of the 5% miss probability in the upper tail. **For an equal-tailed interval** (2.5% each side): 8 (p50), 36 (p90), 72 (p95), 368 (p99) (derived here).
- **With n = 40, a reported "p95" is about the third-largest value (rank 38).** The true p95 exceeds the sample maximum with probability 0.95^40 ≈ 13%.
- **With n = 100, "p99" is essentially the maximum.** The true p99 exceeds the sample maximum with probability 0.99^100 ≈ 37%.

**MLPerf sample counts:**
- The 2020 paper derives query counts from a normal approximation. At 99% confidence the computed counts are 23,886 for p90 and 262,742 for p99, rounded up to 24,576 and 270,336 queries in use [reddi2020mlperf](evidence/F-robustness-frameworks-perf.md#reddi2020mlperf).
- The current rules use a binomial early-stopping criterion that reports a conservative order statistic [mlperf-rules](evidence/F-robustness-frameworks-perf.md#mlperf-rules).

**The interval assumes independent samples.** Warm-up, caching, frequency scaling and queueing make consecutive latencies dependent. Use separate runs, randomised order and minimum durations [leboudec2010perfeval](evidence/F-robustness-frameworks-perf.md#leboudec2010perfeval) [reddi2020mlperf](evidence/F-robustness-frameworks-perf.md#reddi2020mlperf).

## 5. Throughput, concurrency and batching
- **Report throughput at a stated concurrency** or arrival rate, together with the latency at that load. A throughput number without its latency, or a latency without its load, is incomplete [reddi2020mlperf](evidence/F-robustness-frameworks-perf.md#reddi2020mlperf) [kwon2023paged](evidence/F-robustness-frameworks-perf.md#kwon2023paged).
- **Batching depends on memory.**
  - KV-cache memory limits the batch size.
  - Earlier serving systems used only 20–38% of KV-cache memory for actual token states, which motivated paged allocation [kwon2023paged](evidence/F-robustness-frameworks-perf.md#kwon2023paged).
  - Report the runtime's batching and caching settings.
- **Utilisation.** Model FLOPS utilisation (observed throughput / theoretical peak) shows how far a configuration is from hardware limits. Lower latency needs smaller batches, which lowers utilisation and raises cost [pope2023scaling](evidence/F-robustness-frameworks-perf.md#pope2023scaling).
- **Multi-question amortisation.** When several questions share one request, report latency per request and per question in joint vs separate mode ([robustness-and-execution.md §5](robustness-and-execution.md)).

## 6. Memory
**Memory counters measure different things** (derived here; this is a general systems point, not from a source in this review):
- **Resident set size (RSS):** the process's resident pages. It can miss GPU or unified-memory allocations made through a driver, and it counts shared file-backed (memory-mapped) weights in a way that varies by OS.
- **Physical footprint / driver-reported GPU memory:** includes accelerator allocations, but can miss memory-mapped weight files.
- **Peak vs steady state:** a value sampled every few seconds is a lower bound on the true peak.

**Report:**
- which counter was used;
- which process tree was measured;
- when it was sampled (after load, during a run, peak of samples);
- the sampling interval.

**Do not compare one system's RSS with another's footprint.** Use the same counter for all systems, or report both.

## 7. Reproducible hardware and runtime configuration
- **What to record per measurement:**
  - hardware: device, memory, accelerator;
  - OS and driver versions;
  - runtime and library versions;
  - model revision and precision;
  - batching and caching settings;
  - power mode;
  - concurrent load on the machine.
- **Sources for this list:**
  - MLPerf "available" submissions must list software versions, hardware, stacks and settings [mlperf-rules](evidence/F-robustness-frameworks-perf.md#mlperf-rules).
  - The experiment-impact-tracker logs a similar list: packages, hardware, power, utilisation, memory, frequency, grid region [henderson2020energy](evidence/F-robustness-frameworks-perf.md#henderson2020energy).
  - In a sample of 100 NeurIPS 2019 papers, only 46 reported their hardware [henderson2020energy](evidence/F-robustness-frameworks-perf.md#henderson2020energy).
- **Energy** can be estimated from measured power and time:
  - Strubell et al.'s formula multiplies average CPU, DRAM and GPU power by time and by a PUE factor (power usage effectiveness: total facility energy / IT energy) [strubell2019energy](evidence/F-robustness-frameworks-perf.md#strubell2019energy).
  - Software power counters are estimates [henderson2020energy](evidence/F-robustness-frameworks-perf.md#henderson2020energy).
  - Report the method if energy is claimed.

## 8. Cost
- **There is no single standard cost metric** [pope2023scaling](evidence/F-robustness-frameworks-perf.md#pope2023scaling) [kurtic2025quant](evidence/F-robustness-frameworks-perf.md#kurtic2025quant). Common forms:
  - price per request or per token (API);
  - accelerator-seconds or chip-hours per request;
  - energy per request;
  - memory footprint as a capacity constraint.
- **Quality and resources together.** Quantization and precision trade accuracy against throughput and memory. One vendor-affiliated study reports about 99% average score recovery at 8-bit [kurtic2025quant](evidence/F-robustness-frameworks-perf.md#kurtic2025quant).
- **Leaderboards that ignore resources** misstate utility for users with budgets [ethayarajh2020utility](evidence/E-statistics-aggregation.md#ethayarajh2020utility).
- **Show a Pareto front.** Without an agreed exchange rate between quality and resources, show the front over quality, latency and memory, rather than one weighted score (derived here).
- **Count retries, repairs and escalations as cost.** A cascade that escalates uncertain cases to a larger system has cost = small-system cost + escalation rate × large-system cost (derived here).

## 9. Measurement checklist
1. **Scenario and load model:** sequential, fixed concurrency or Poisson rate; batching settings.
2. **Input grid:** input length × option or question count × output length, with distinct texts for uncached measurement.
3. **Cold start:** spawn → ready → first valid answer, measured separately from warm latency, with the number of preceding requests.
4. **Percentiles with n and intervals:** n large enough for the reported percentile (≥ 59 for a p95 interval and ≥ 299 for p99 with [min, max]; 72 and 368 for equal-tailed), samples spread over separate runs.
5. **Clocks:** client and server timings, with the clock source.
6. **Memory:** the same counter for all systems, the process tree, sampling interval, and peak vs steady state.
7. **Configuration record:** hardware, OS, runtime, versions, precision, power mode, other load on the machine.
8. **Cost:** expressed in the units the decision needs, with retries and escalations included; a Pareto view against quality.
