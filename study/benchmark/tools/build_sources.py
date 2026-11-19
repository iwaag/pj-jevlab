"""Build study/benchmark/evidence/*.md, sources.md tables and search-log appendix
from the step2 cluster notes. Run once in step2; kept for traceability."""
import re, sys, pathlib

SRC = pathlib.Path(sys.argv[1])          # directory with the raw cluster notes
OUT = pathlib.Path(__file__).resolve().parent.parent
CLUSTERS = {
    "A": ("A-metrics.md", "Classification, detection, multilabel, ranking and ordinal metrics"),
    "B": ("B-probability-abstention.md", "Probabilities, calibration, abstention, OOD and cost-sensitive decisions"),
    "C": ("C-judging-structured.md", "Annotation agreement, human/model judging, generated and structured outputs"),
    "D": ("D-data-validity.md", "Validity, datasets, negatives, splits and contamination"),
    "E": ("E-statistics-aggregation.md", "Intervals, paired tests, power, multiplicity and aggregation"),
    "F": ("F-robustness-frameworks-perf.md", "Robustness, harnesses, benchmark suites, performance and cost"),
}

def split_sections(text):
    parts = re.split(r"(?m)^## ", text)
    head, secs = parts[0], {}
    for p in parts[1:]:
        title, _, body = p.partition("\n")
        secs[title.strip()] = body
    return head, secs

def field(block, name):
    m = re.search(r"(?m)^- " + re.escape(name) + r"[^:]*:\s*(.*)$", block)
    return m.group(1).strip() if m else ""

rows, logs = {}, {}
for key, (fname, label) in CLUSTERS.items():
    text = (SRC / fname).read_text()
    head, secs = split_sections(text)
    srclist = next(v for k, v in secs.items() if k.startswith("Source list"))
    entries = []
    for blk in re.split(r"(?m)^### ", srclist)[1:]:
        heading, _, body = blk.partition("\n")
        if "- Title:" not in body:
            print("skip", key, heading.strip()[:60]); continue
        sid = heading.strip().split()[0]
        url = field(body, "URL") or field(body, "DOI")
        ver = field(body, "Verification").replace("*", "").strip()
        v = ver.lower()
        level = ("partial" if v.startswith("full") and ("abstract-level" in v or "findings list only" in v) else
                 "mixed: book unverified, chapter full text" if v.startswith("the book is unverified") else
                 "full text" if v.startswith("full") else
                 "partial" if ver.lower().startswith("partial") else
                 "abstract" if ver.lower().startswith("abstract") else
                 "unverified" if ver.lower().startswith("unverified") else ver.split(" ")[0])
        entries.append(dict(id=sid, heading=heading.strip(), title=field(body, "Title"),
                            authors=field(body, "Authors"), date=field(body, "Date"),
                            url=url, type=field(body, "Type"), level=level))
    rows[key] = entries
    logs[key] = (secs.get("Search log", ""), secs.get("Gaps and unavailable sources", ""))
    keep = {k: v for k, v in secs.items() if k not in ("Search log", "Gaps and unavailable sources")}
    body = head.rstrip() + "\n\n" + (
        f"> Evidence notes for cluster {key} of [study/benchmark](../README.md), compiled 2026-10-02 in step2 of "
        "benchmark/p1 by a research subagent and reviewed by the lead session. The search log and gaps for this "
        "cluster are in [search-log.md](../search-log.md). Verification levels are per entry; claims beyond the "
        "stated level must not be attributed to a source.\n\n")
    body += "".join(f"## {k}\n{v}" for k, v in keep.items())
    (OUT / "evidence" / fname).write_text(body.rstrip() + "\n")

def anchor(h):
    a = h.lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")

def short(s, n=90):
    s = s.replace("|", "/")
    return s if len(s) <= n else s[: n - 1] + "…"

out = []
for key, (fname, label) in CLUSTERS.items():
    es = rows[key]
    cnt = {}
    for e in es:
        cnt[e["level"]] = cnt.get(e["level"], 0) + 1
    out.append(f"## {key}. {label}\n")
    out.append(f"Evidence file: [evidence/{fname}](evidence/{fname}). Entries: {len(es)} "
               f"({', '.join(f'{v} {k}' for k, v in sorted(cnt.items()))}).\n")
    out.append("| ID | Title | Authors / org | Date | Type | Read to | Link |")
    out.append("|---|---|---|---|---|---|---|")
    for e in es:
        link = e["url"]
        m = re.search(r"https?://\S+", link)
        if m:
            link = f"[link]({m.group(0).rstrip(';,)')})"
        else:
            m = re.search(r"arXiv:?\s*(\d{4}\.\d{4,5})", link)
            d = re.search(r"(10\.\d{4,9}/[^\s;,]+)", link)
            link = (f"[arXiv {m.group(1)}](https://arxiv.org/abs/{m.group(1)})" if m else
                    f"[doi](https://doi.org/{d.group(1)})" if d else short(link, 40))
        out.append(f"| [{e['id']}](evidence/{fname}#{anchor(e['heading'])}) | {short(e['title'])} | "
                   f"{short(e['authors'], 50)} | {short(e['date'], 40)} | {short(e['type'], 40)} | {e['level']} | {link} |")
    out.append("")
(OUT / "tools" / "_sources_tables.md").write_text("\n".join(out))

lg = []
for key, (fname, label) in CLUSTERS.items():
    log, gaps = logs[key]
    lg.append(f"### Cluster {key}: {label}\n\n#### Queries\n{log.strip()}\n\n#### Gaps and unavailable sources\n{gaps.strip()}\n")
(OUT / "tools" / "_search_tables.md").write_text("\n".join(lg))

ids = {k: {e["id"]: anchor(e["heading"]) for e in v} for k, v in rows.items()}
import json
(OUT / "tools" / "source_ids.json").write_text(json.dumps({k: {"file": CLUSTERS[k][0], "ids": v} for k, v in ids.items()}, indent=1))
print({k: len(v) for k, v in rows.items()})
