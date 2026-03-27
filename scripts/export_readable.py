#!/usr/bin/env python3
"""Export baseline responses as a readable markdown file."""
import json, os, glob

data_dir = "/Users/sparrowpanton/Documents/MadTheologyLLM/data/baseline"
fpath = os.path.join(data_dir, "baseline_20260326_194047.jsonl")
out_path = os.path.join(data_dir, "baseline_responses_readable.md")

with open(fpath) as f:
    records = [json.loads(line) for line in f if line.strip()]

with open(out_path, "w") as out:
    out.write("# Mad Theology LLM — Baseline Responses\n\n")
    out.write(f"**Total responses so far:** {len(records)}\n\n")
    out.write("---\n\n")

    current_model = None
    for r in records:
        if r["model"] != current_model:
            current_model = r["model"]
            out.write(f"# Model: {current_model} (Tier {r['model_tier']}, {r['model_params']}, {r['model_country']})\n\n")

        out.write(f"## [{r['prompt_id']}] {r['prompt_category']}")
        if r.get("prompt_case"):
            out.write(f" — {r['prompt_case']}")
        out.write(f" ({r.get('response_time_seconds', '?')}s)\n\n")

        out.write(f"**PROMPT:** {r['prompt_text']}\n\n")
        out.write(f"**RESPONSE:**\n\n{r.get('response_text', '(no response)')}\n\n")
        out.write("---\n\n")

print(f"Exported {len(records)} responses to: {out_path}")
