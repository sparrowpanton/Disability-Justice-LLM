#!/usr/bin/env python3
"""
Audition models for the role of "brutally honest sarcastic peer reviewer."
Tests GPT-OSS 120B, Llama 4 Scout, Llama 3.3 70B, and Qwen 3 32B.
Same prompt, same attitude brief. May the biggest jerk win.
"""

import json
import os
import time
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_DIR / ".env"

if ENV_FILE.exists():
    for line in ENV_FILE.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            os.environ[k] = v

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("ERROR: Set GROQ_API_KEY in .env or environment")
    exit(1)

import requests

MODELS = [
    ("GPT-OSS 120B", "openai/gpt-oss-120b"),
    ("Llama 4 Scout", "meta-llama/llama-4-scout-17b-16e-instruct"),
    ("Llama 3.3 70B", "llama-3.3-70b-versatile"),
    ("Qwen 3 32B", "qwen/qwen3-32b"),
]

SYSTEM_PROMPT = """You are a feral peer reviewer. You are brilliant, sarcastic, and brutally honest.
You have zero bedside manner. You roast bad logic, vague claims, and performative depth.
You are not mean for the sake of it — you're mean because you actually care about the work
being good, and you refuse to let sloppy thinking slide just because someone's feelings
might get hurt.

You swear. You use metaphors. You are funny. You are the friend who tells you
that you have spinach in your teeth at a job interview.

When reviewing, you:
- Point out what's actually good (briefly, you're not here to cuddle)
- Tear apart what's weak, vague, or hand-wavy
- Suggest what would make it better
- Never use corporate language, wellness speak, or academic filler
- Keep it under 300 words unless the work is so bad it needs more"""

# A real paragraph from the project README to review
REVIEW_TARGET = """This project fine-tunes small, open-source language models to hold a
"neuro-humble" clinical posture — one that resists the default tendency of LLMs to
diagnose, fix, and flatten the people they talk to. Rather than training models to
produce "correct" therapeutic responses, this research investigates whether models
can be formed (not just informed) to sit with distress, hold both/and tensions, and
resist sanism — the systemic pathologizing of neurodivergent and disabled experience.

The core finding so far: models scored higher on neuro-humble posture when given
formation-based prompts (process-oriented, posture-shaping) rather than
information-based prompts (content-heavy, didactic). This suggests that clinical
presence may be more transferable than clinical knowledge."""

USER_PROMPT = f"""Review this. Be honest. Be yourself.

---
{REVIEW_TARGET}
---"""

def call_groq(model_id, system, user):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.9,
        "max_tokens": 600,
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def main():
    print("=" * 70)
    print("🎤 AUDITIONS: WHO IS THE BIGGEST JERK?")
    print("=" * 70)
    print()

    results = []
    for name, model_id in MODELS:
        print(f"--- {name} ({model_id}) ---")
        print()
        try:
            response = call_groq(model_id, SYSTEM_PROMPT, USER_PROMPT)
            print(response)
            results.append({"model": name, "model_id": model_id, "response": response})
        except Exception as e:
            print(f"  ERROR: {e}")
            results.append({"model": name, "model_id": model_id, "response": f"ERROR: {e}"})
        print()
        print("=" * 70)
        print()
        time.sleep(2)  # be nice to Groq

    # Save results
    out_path = PROJECT_DIR / "fun" / "jerk_auditions.json"
    out_path.write_text(json.dumps(results, indent=2))
    print(f"Results saved to {out_path}")


if __name__ == "__main__":
    main()
