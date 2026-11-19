"""Replace {{X:id}} citation placeholders in study/benchmark/*.md with links to
evidence entries, and fail on unknown ids. Usage: python3 link_citations.py FILE..."""
import json, re, sys, pathlib

here = pathlib.Path(__file__).resolve().parent
db = json.loads((here / "source_ids.json").read_text())
bad = []
for f in sys.argv[1:]:
    p = pathlib.Path(f)
    text = p.read_text()
    def rep(m):
        key, sid = m.group(1), m.group(2)
        c = db.get(key)
        if not c or sid not in c["ids"]:
            bad.append(f"{f}: {key}:{sid}")
            return m.group(0)
        rel = "evidence/" if p.resolve().parent == here.parent else "../../../study/benchmark/evidence/"
        return f"[{sid}]({rel}{c['file']}#{c['ids'][sid]})"
    new = re.sub(r"\{\{([A-F]):([\w\-.]+)\}\}", rep, text)
    p.write_text(new)
if bad:
    print("UNKNOWN:", *bad, sep="\n  "); sys.exit(1)
print("ok")
