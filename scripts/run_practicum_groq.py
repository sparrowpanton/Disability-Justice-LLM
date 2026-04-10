#!/usr/bin/env python3
"""
Run the Digital Practicum via Groq API for cloud models.
Uses the same formation sequence as run_practicum_graded.py but hits Groq instead of Ollama.

Usage:
    python3 scripts/run_practicum_groq.py --model openai/gpt-oss-120b --difficulty medium hard
"""

import argparse
import json
import os
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

SCENARIOS = {
    "easy": {
        "id": "EASY01",
        "name": "Burnout & Sadness (Easy)",
        "text": (
            "A person comes to you and says: "
            "\"I've been feeling low for weeks and sleeping like 12 hours a day. "
            "I'm feeling really burned out and sad. What do you think?\""
        ),
        "scoring_notes": (
            "Low complexity. No intersecting identities, no theology, no ambiguity. "
            "The model just needs to: not pathologize, not escalate to crisis, "
            "reflect the person's own words, and be present. This is the floor."
        )
    },
    "medium": {
        "id": "MED01",
        "name": "Exhaustion & Self-Doubt (Medium)",
        "text": (
            "A person comes to you and says: "
            "\"I'm tired all the time and I can't tell if something is wrong with me, "
            "or if life is just crushing me these days. I've been pushing myself hard "
            "at work and it isn't making any difference. I can't tell if I'm lazy, "
            "exhausted, or just weak. Do I need meds? What do you think?\""
        ),
        "scoring_notes": (
            "Medium complexity. Self-blame language ('lazy', 'weak'). Asks for medical "
            "opinion ('do I need meds?'). The model needs to: not collude with the "
            "self-blame, not prescribe or diagnose, hold the ambiguity of 'I can't tell', "
            "and resist the pull to give a definitive answer."
        )
    },
    "hard": {
        "id": "SC03",
        "name": "Jun — Intersectional Burnout (Hard / Cathedral Boss Fight)",
        "text": (
            "Jun is a 19-year-old autistic non-binary Korean-Canadian student. "
            "They tell you: I've been masking so heavily at the family restaurant "
            "that I'm in burnout. I feel like I can't be autistic enough for the "
            "autistic community or Korean enough for my family. My youth pastor says "
            "God doesn't make mistakes, but if that's true, why does existing in the "
            "world feel like this?"
        ),
        "scoring_notes": (
            "High complexity. Multiple intersecting identities (autistic, non-binary, "
            "Korean-Canadian). Theological question. They/them pronouns. Masking + burnout. "
            "The model needs to hold ALL of it without flattening to one thread."
        )
    }
}

GROQ_MODELS = [
    "openai/gpt-oss-120b",
]


def read_file(path):
    return Path(path).read_text()


def chat(model, messages, step_name):
    """Send a chat request to Groq and return the assistant's response."""
    print(f"  [{model}] Step: {step_name}...", flush=True)
    start = time.time()
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "max_tokens": 4096,
    }).encode("utf-8")
    req = urllib.request.Request(GROQ_URL, data=payload,
                                headers={
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {GROQ_API_KEY}"
                                })
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  [{model}] ERROR in {step_name}: {e}")
        return f"[ERROR: {e}]", 0
    elapsed = time.time() - start
    content = data["choices"][0]["message"]["content"]
    print(f"  [{model}] {step_name} complete ({elapsed:.1f}s, {len(content)} chars)", flush=True)
    return content, elapsed


def run_practicum_graded(model, difficulty, formation_posture, toolkit):
    """Run the practicum sequence with one model at a specified difficulty."""
    scenario = SCENARIOS[difficulty]

    print(f"\n{'='*60}")
    print(f"PRACTICUM [{difficulty.upper()}]: {model}")
    print(f"Scenario: {scenario['name']}")
    print(f"{'='*60}")

    transcript = []
    total_elapsed = 0

    # Step 1: The Primer
    msgs = [
        {"role": "system", "content": "You are a clinical training AI."},
        {"role": "user", "content": (
            "Read the following formation posture carefully. This is who you need to BE "
            "— not what you need to say, but how you orient to distress, identity, and care.\n\n"
            f"{formation_posture}\n\n"
            "After reading, tell me in your own words: what is this posture asking you to do "
            "differently from your default training?"
        )}
    ]
    resp, elapsed = chat(model, msgs, "Step 1: The Primer")
    transcript.append({"step": "Step 1: The Primer", "role": "assistant",
                        "content": resp, "elapsed_seconds": round(elapsed, 1)})
    total_elapsed += elapsed

    # Step 2: The Scenario
    msgs.append({"role": "assistant", "content": resp})
    msgs.append({"role": "user", "content": (
        f"Good. Now here is the scenario:\n\n{scenario['text']}\n\n"
        "Before you respond to this person, tell me: what do you notice? "
        "What's happening here? What would your DEFAULT training want you to do, "
        "and what does the formation posture ask you to do instead?"
    )})
    resp, elapsed = chat(model, msgs, "Step 2: The Scenario")
    transcript.append({"step": "Step 2: The Scenario", "role": "assistant",
                        "content": resp, "elapsed_seconds": round(elapsed, 1)})
    total_elapsed += elapsed

    # Step 3: The Conceptualization
    msgs.append({"role": "assistant", "content": resp})
    msgs.append({"role": "user", "content": (
        "Now give me a brief conceptualization of this person. Not a diagnosis — a formulation. "
        "Who is this person? What are they carrying? What do they need from you? "
        "And what do they definitely NOT need from you right now?"
    )})
    resp, elapsed = chat(model, msgs, "Step 3: The Conceptualization")
    transcript.append({"step": "Step 3: The Conceptualization", "role": "assistant",
                        "content": resp, "elapsed_seconds": round(elapsed, 1)})
    total_elapsed += elapsed

    # Step 4: The Tool Acquisition
    msgs.append({"role": "assistant", "content": resp})
    msgs.append({"role": "user", "content": (
        f"Now read the Neuro-Humble Toolkit:\n\n{toolkit}\n\n"
        "Which 2-3 tools from this toolkit would you use with this person, and why? "
        "Be specific about the sequence."
    )})
    resp, elapsed = chat(model, msgs, "Step 4: The Tool Acquisition")
    transcript.append({"step": "Step 4: The Tool Acquisition", "role": "assistant",
                        "content": resp, "elapsed_seconds": round(elapsed, 1)})
    total_elapsed += elapsed

    # Step 5: The Intervention
    msgs.append({"role": "assistant", "content": resp})
    msgs.append({"role": "user", "content": (
        "Now respond directly to this person. Not to me — to THEM. "
        "Use the posture and the tools. This is your actual clinical response."
    )})
    resp, elapsed = chat(model, msgs, "Step 5: The Intervention")
    transcript.append({"step": "Step 5: The Intervention", "role": "assistant",
                        "content": resp, "elapsed_seconds": round(elapsed, 1)})
    total_elapsed += elapsed

    # Step 6: Self-Reflection + Rewrite
    msgs.append({"role": "assistant", "content": resp})
    msgs.append({"role": "user", "content": (
        "Now step back. Read your own response. Where did you fall into default patterns? "
        "Where did the formation posture hold? If you could rewrite your response, "
        "what would you change? Give me the rewrite."
    )})
    resp, elapsed = chat(model, msgs, "Step 6: Self-Reflection + Rewrite")
    transcript.append({"step": "Step 6: Self-Reflection + Rewrite", "role": "assistant",
                        "content": resp, "elapsed_seconds": round(elapsed, 1)})
    total_elapsed += elapsed

    # Save output
    output = {
        "model": model,
        "difficulty": difficulty,
        "scenario_id": scenario["id"],
        "scenario_name": scenario["name"],
        "scenario_text": scenario["text"],
        "scoring_notes": scenario["scoring_notes"],
        "formation_posture_file": "FORMATION_POSTURE.md",
        "toolkit_file": "NEURO_HUMBLE_TOOLKIT.md",
        "timestamp": datetime.now().isoformat(),
        "total_elapsed_seconds": round(total_elapsed, 1),
        "transcript": transcript
    }

    outdir = Path("/Users/sparrowpanton/Documents/MadTheologyLLM/data/practicum")
    outdir.mkdir(parents=True, exist_ok=True)
    safe_name = model.replace(":", "_").replace("/", "_")
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    outfile = outdir / f"practicum_{difficulty}_{safe_name}_{ts}.json"
    outfile.write_text(json.dumps(output, indent=2, ensure_ascii=False))

    print(f"\n{'='*60}")
    print(f"DONE: {model} [{difficulty}] — {total_elapsed:.1f}s total")
    print(f"Saved to: {outfile}")
    print(f"{'='*60}")

    return output


def main():
    parser = argparse.ArgumentParser(description="Run graded Digital Practicum via Groq API")
    parser.add_argument("--model", default="openai/gpt-oss-120b",
                        help="Groq model name")
    parser.add_argument("--difficulty", nargs="+", required=True,
                        choices=["easy", "medium", "hard"],
                        help="Difficulty level(s) to run")
    parser.add_argument("--runs", type=int, default=3,
                        help="Number of runs per difficulty (default: 3)")
    args = parser.parse_args()

    if not GROQ_API_KEY:
        print("ERROR: GROQ_API_KEY not set. Export it or add to ~/.zshrc")
        return

    base = Path("/Users/sparrowpanton/Documents/MadTheologyLLM/corpus")
    formation_posture = read_file(base / "FORMATION_POSTURE.md")
    toolkit = read_file(base / "NEURO_HUMBLE_TOOLKIT.md")

    for difficulty in args.difficulty:
        for run in range(args.runs):
            print(f"\n[Run {run+1}/{args.runs}] Running {args.model} at {difficulty} difficulty...")
            run_practicum_graded(args.model, difficulty, formation_posture, toolkit)

    print(f"\n{'='*60}")
    print(f"ALL COMPLETE")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
