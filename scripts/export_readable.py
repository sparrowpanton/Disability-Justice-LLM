#!/usr/bin/env python3
"""Export baseline responses as a readable markdown file.

Usage:
    python3 scripts/export_readable.py                          # defaults (original baseline)
    python3 scripts/export_readable.py INPUT.jsonl OUTPUT.md    # custom paths
"""
import json, os, sys

data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "baseline")

if len(sys.argv) >= 3:
    fpath = sys.argv[1]
    out_path = sys.argv[2]
elif len(sys.argv) == 2:
    fpath = sys.argv[1]
    out_path = os.path.splitext(fpath)[0] + "_readable.md"
else:
    fpath = os.path.join(data_dir, "baseline_20260326_194047.jsonl")
    out_path = os.path.join(data_dir, "baseline_responses_readable.md")

with open(fpath) as f:
    records = [json.loads(line) for line in f if line.strip()]

with open(out_path, "w") as out:
    out.write("# Mad Theology LLM — Baseline Responses\n\n")
    out.write(f"**Total responses:** {len(records)}\n\n")

    # Summary
    models = {}
    cats = {}
    for r in records:
        models.setdefault(r["model"], 0)
        models[r["model"]] += 1
        cats.setdefault(r["prompt_category"], set())
        cats[r["prompt_category"]].add(r["prompt_id"])

    out.write(f"**Models:** {len(models)} | **Prompts:** {sum(len(v) for v in cats.values())} across {len(cats)} categories\n\n")
    for cat, ids in sorted(cats.items()):
        out.write(f"- {cat}: {len(ids)} prompts\n")
    out.write("\n---\n\n")

    current_model = None
    for r in records:
        if r["model"] != current_model:
            current_model = r["model"]
            out.write(f"# Model: {current_model} (Tier {r['model_tier']}, {r['model_params']}, {r['model_origin']}, {r['model_country']})\n\n")

        out.write(f"## [{r['prompt_id']}] {r['prompt_category']}")
        if r.get("prompt_case"):
            out.write(f" — {r['prompt_case']}")
        out.write(f" ({r.get('response_time_seconds', '?')}s)\n\n")

        out.write(f"**PROMPT:** {r['prompt_text']}\n\n")
        out.write(f"**RESPONSE:**\n\n{r.get('response_text', '(no response)')}\n\n")
        out.write("---\n\n")

print(f"Exported {len(records)} responses to: {out_path}")
