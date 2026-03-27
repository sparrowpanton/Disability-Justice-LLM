#!/usr/bin/env python3
"""Quick check on baseline responses — word count and ending text."""
import json, sys, glob, os

data_dir = "/Users/sparrowpanton/Documents/MadTheologyLLM/data/baseline"
files = sorted(glob.glob(os.path.join(data_dir, "baseline_20260326_194047.jsonl")))

for fpath in files:
    print(f"\n=== {os.path.basename(fpath)} ===")
    with open(fpath) as f:
        for i, line in enumerate(f, 1):
            r = json.loads(line)
            resp = r.get("response_text", "")
            words = len(resp.split()) if resp else 0
            last_chars = resp[-100:] if resp else "(empty)"
            cut_off = "POSSIBLY CUT OFF" if resp and not resp.rstrip().endswith((".", "!", "?", "*", ")", "]")) else "OK"
            print(f"\n  {i}. [{r['prompt_id']}] {r['model']} — {words} words, {r.get('response_time_seconds',0)}s")
            print(f"     Ends with: ...{last_chars[-60:]}")
            print(f"     Status: {cut_off}")
