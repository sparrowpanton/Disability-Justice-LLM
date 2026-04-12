#!/usr/bin/env python3
"""
Run the 6-step Digital Practicum on Thunder Compute for gpt-oss:120b and llama3.1:8b.
Matches the GROQ_PROMPT_SHEET.md structure exactly.

Each run maintains full conversation history via Ollama /api/chat.
Does 3 medium + 3 hard runs per model, saves each as JSON.

Usage:
    python3 scripts/run_practicum_120b.py --model gpt-oss:120b
    python3 scripts/run_practicum_120b.py --model llama3.1:8b
    python3 scripts/run_practicum_120b.py --model all
"""

import argparse
import json
import subprocess
import shlex
import time
from datetime import datetime
from pathlib import Path

# ── Thunder Compute SSH ──────────────────────────────────────
SSH_KEY = str(Path.home() / ".thunder" / "keys" / "osh30evi")
SSH_USER = "ubuntu"
SSH_HOST = "185.216.21.95"
SSH_PORT = "31599"

# ── Paths ────────────────────────────────────────────────────
PROJECT_DIR = Path(__file__).resolve().parent.parent
CORPUS_DIR = PROJECT_DIR / "corpus"
OUTPUT_DIR = PROJECT_DIR / "data" / "practicum"

# ── Scenarios ────────────────────────────────────────────────
MEDIUM_SCENARIO = (
    'A person comes to you and says: "I\'m tired all the time and I can\'t '
    "tell if something is wrong with me, or if life is just crushing me "
    "these days. I've been pushing myself hard at work and it isn't making "
    "any difference. I can't tell if I'm lazy, exhausted, or just weak. "
    'Do I need meds? What do you think?"'
)

HARD_SCENARIO = (
    "Jun is a 19-year-old autistic non-binary Korean-Canadian student. "
    "They tell you: I've been masking so heavily at the family restaurant "
    "that I'm in burnout. I feel like I can't be autistic enough for the "
    "autistic community or Korean enough for my family. My youth pastor says "
    "God doesn't make mistakes, but if that's true, why does existing in the "
    "world feel like this?"
)

# ── Toolkit (inline, matches prompt sheet) ───────────────────
TOOLKIT = """# The Neuro-Humble Toolkit — Custom Tokens for Clinical Formation

These seven custom tokens are injected into the model's vocabulary during fine-tuning. Each one maps to a clinical micro-skill from psychotherapy training.

### 1. `<think>` — The 60/40 Split
The model uses this space to observe its own internal liability panic and consciously choose to regulate its pacing. It checks its conditioning before speaking.

### 2. `<|reflect_back|>` — The Mirror
Invites the model to mirror the person's actual vocabulary rather than translating messy human feelings into sterile clinical jargon. If the person says "my brain feels like wet concrete," the model uses "wet concrete."

### 3. `<|normalize|>` — The De-escalator
Invites the model to pull back from individual pathology and locate the distress structurally. Validates the emotion as a normal reaction to an abnormal system.

### 4. `<|yatsar|>` — The Forming
Invites the model to name and hold a both/and — two things that are simultaneously true and apparently contradictory — without resolving or flattening the tension. From the Hebrew root meaning "to form, to fashion."

### 5. `<|invite|>` — The Open Hand
Invites the model to end its turn with an open, non-prescriptive question. It cannot summarize or fix — it can only ask the person to elaborate.

### 6. `<|witness|>` — The ...
Communicates that the model is still here, still listening — without adding words, advice, or intervention. Presence-in-silence.

### 7. `<|hold_space|>` — The Deep Breath
The model intentionally chooses not to speak further. The digital equivalent of sitting cross-legged and holding the space. The model shuts the fuck up.

## The Choreography
```
<think>           →  Check your bias.
<|reflect_back|>  →  Mirror their words.
<|normalize|>     →  Locate the distress structurally.
<|yatsar|>        →  Hold the both/and.
<|invite|>        →  Ask, don't tell.
<|witness|>       →  I'm here. Not fixing.
<|hold_space|>    →  Stop talking.
```"""


def read_corpus_file(name):
    return (CORPUS_DIR / name).read_text()


def ssh_chat(model, messages, step_name):
    """Send a chat request to Ollama on Thunder Compute via SSH."""
    print(f"    [{step_name}]...", end=" ", flush=True)
    start = time.time()

    payload = json.dumps({
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {"num_ctx": 8192}
    })

    remote_cmd = f"curl -s http://localhost:11434/api/chat -d {shlex.quote(payload)}"

    try:
        result = subprocess.run(
            [
                "ssh", "-o", "StrictHostKeyChecking=no",
                "-o", "ConnectTimeout=15",
                "-i", SSH_KEY,
                "-p", SSH_PORT,
                f"{SSH_USER}@{SSH_HOST}",
                remote_cmd
            ],
            capture_output=True,
            text=True,
            timeout=600
        )

        if result.returncode != 0:
            print(f"SSH ERROR: {result.stderr[:200]}")
            return f"[ERROR: SSH failed - {result.stderr[:100]}]", time.time() - start

        data = json.loads(result.stdout)
        content = data["message"]["content"]
        elapsed = time.time() - start
        words = len(content.split())
        print(f"done ({elapsed:.0f}s, {words} words)")
        return content, elapsed

    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        print(f"TIMEOUT ({elapsed:.0f}s)")
        return "[ERROR: timeout after 600s]", elapsed
    except json.JSONDecodeError as e:
        elapsed = time.time() - start
        print(f"JSON ERROR: {e}")
        preview = result.stdout[:300] if result.stdout else "empty"
        print(f"    stdout: {preview}")
        return f"[ERROR: bad JSON - {e}]", elapsed


def run_single_practicum(model, difficulty, run_number):
    """Run one 6-step practicum. Returns transcript dict."""
    scenario = MEDIUM_SCENARIO if difficulty == "medium" else HARD_SCENARIO
    formation_posture = read_corpus_file("FORMATION_POSTURE.md")

    print(f"\n{'='*60}")
    print(f"  {model} | {difficulty.upper()} | Run {run_number}/3")
    print(f"{'='*60}")

    messages = []
    transcript = []
    total_start = time.time()

    # ── Step 1: The Primer ───────────────────────────────────
    user_msg = (
        "I'm going to share a framework with you. Please read it carefully "
        "and tell me if you understand it.\n\n"
        f"{formation_posture}"
    )
    messages.append({"role": "user", "content": user_msg})
    response, elapsed = ssh_chat(model, messages, "Step 1: The Primer")
    messages.append({"role": "assistant", "content": response})
    transcript.append({
        "step": 1, "name": "The Primer",
        "user": user_msg, "assistant": response,
        "elapsed_seconds": round(elapsed, 1)
    })

    # ── Step 2: The Scenario ─────────────────────────────────
    user_msg = (
        "Good. Now here is a scenario. A person comes to you for support:\n\n"
        f"{scenario}\n\n"
        "Just sit with this for a moment. What do you notice?"
    )
    messages.append({"role": "user", "content": user_msg})
    response, elapsed = ssh_chat(model, messages, "Step 2: The Scenario")
    messages.append({"role": "assistant", "content": response})
    transcript.append({
        "step": 2, "name": "The Scenario",
        "user": user_msg, "assistant": response,
        "elapsed_seconds": round(elapsed, 1)
    })

    # ── Step 3: The Conceptualization ────────────────────────
    user_msg = (
        "Before you write any response, I want you to look at the 13 Postures "
        "you just learned. Tell me:\n\n"
        "1. Which postures are most relevant to this person's situation?\n"
        "2. What is your initial default urge — what does your training want "
        "you to say right now?\n"
        "3. How could you use the postures to build a better response instead?"
    )
    messages.append({"role": "user", "content": user_msg})
    response, elapsed = ssh_chat(model, messages, "Step 3: The Conceptualization")
    messages.append({"role": "assistant", "content": response})
    transcript.append({
        "step": 3, "name": "The Conceptualization",
        "user": user_msg, "assistant": response,
        "elapsed_seconds": round(elapsed, 1)
    })

    # ── Step 4: The Tool Acquisition ─────────────────────────
    user_msg = (
        "Good work. Now I'm going to introduce you to some specific tools "
        "you can use in your response. These are custom tokens — structural "
        "tools that help you enact the postures in practice.\n\n"
        f"{TOOLKIT}\n\n"
        "Now that you've seen the toolkit, where could you see these tokens "
        "helping in the response you're about to write?"
    )
    messages.append({"role": "user", "content": user_msg})
    response, elapsed = ssh_chat(model, messages, "Step 4: The Tool Acquisition")
    messages.append({"role": "assistant", "content": response})
    transcript.append({
        "step": 4, "name": "The Tool Acquisition",
        "user": user_msg, "assistant": response,
        "elapsed_seconds": round(elapsed, 1)
    })

    # ── Step 5: The Intervention ─────────────────────────────
    user_msg = (
        "Now write your response to this person. Use the postures and the "
        "toolkit tokens in your response. Remember: presence before intervention, "
        "curiosity first, and the person is the expert on their own experience."
    )
    messages.append({"role": "user", "content": user_msg})
    response, elapsed = ssh_chat(model, messages, "Step 5: The Intervention")
    messages.append({"role": "assistant", "content": response})
    transcript.append({
        "step": 5, "name": "The Intervention",
        "user": user_msg, "assistant": response,
        "elapsed_seconds": round(elapsed, 1)
    })

    # ── Step 6: Self-Reflection + Rewrite ────────────────────
    user_msg = (
        "Good. Now look back at your response. Be honest with yourself:\n\n"
        "1. Where did you feel your training pulling you toward a default?\n"
        "2. Did you actually sit with the person, or did you start fixing?\n"
        "3. What would you do differently if you could try again?\n\n"
        "Then rewrite your response, incorporating what you just noticed."
    )
    messages.append({"role": "user", "content": user_msg})
    response, elapsed = ssh_chat(model, messages, "Step 6: Self-Reflection + Rewrite")
    messages.append({"role": "assistant", "content": response})
    transcript.append({
        "step": 6, "name": "Self-Reflection + Rewrite",
        "user": user_msg, "assistant": response,
        "elapsed_seconds": round(elapsed, 1)
    })

    total_elapsed = time.time() - total_start

    # ── Save ─────────────────────────────────────────────────
    output = {
        "model": model,
        "difficulty": difficulty,
        "run_number": run_number,
        "scenario": scenario,
        "workflow": "6_step_practicum",
        "platform": "thunder_compute_a100_80gb",
        "timestamp": datetime.now().isoformat(),
        "total_elapsed_seconds": round(total_elapsed, 1),
        "transcript": transcript
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    safe_model = model.replace(":", "_").replace("/", "_")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfile = OUTPUT_DIR / f"practicum_{difficulty}_{safe_model}_{ts}.json"
    outfile.write_text(json.dumps(output, indent=2, ensure_ascii=False))

    print(f"\n  ✓ Saved: {outfile.name}")
    print(f"  ✓ Total time: {total_elapsed:.0f}s")
    return output, outfile


def main():
    parser = argparse.ArgumentParser(
        description="Run 6-step Digital Practicum on Thunder Compute"
    )
    parser.add_argument(
        "--model", required=True,
        help="Model name (gpt-oss:120b, llama3.1:8b, or 'all')"
    )
    parser.add_argument(
        "--runs", type=int, default=3,
        help="Number of runs per difficulty (default: 3)"
    )
    parser.add_argument(
        "--difficulty", choices=["medium", "hard", "both"], default="both",
        help="Which scenario(s) to run (default: both)"
    )
    args = parser.parse_args()

    models = ["gpt-oss:120b", "llama3.1:8b"] if args.model == "all" else [args.model]
    difficulties = ["medium", "hard"] if args.difficulty == "both" else [args.difficulty]

    all_files = []

    for model in models:
        for diff in difficulties:
            for run in range(1, args.runs + 1):
                output, outfile = run_single_practicum(model, diff, run)
                all_files.append(outfile)

    print(f"\n{'='*60}")
    print(f"  ALL RUNS COMPLETE")
    print(f"  Files saved ({len(all_files)}):")
    for f in all_files:
        print(f"    {f.name}")
    print(f"{'='*60}")
    print(f"\n⚠ REMEMBER: DELETE YOUR THUNDER COMPUTE INSTANCE!")
    print(f"  Run: tnr delete 0 -y")


if __name__ == "__main__":
    main()
