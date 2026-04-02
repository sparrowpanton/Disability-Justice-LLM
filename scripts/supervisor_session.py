#!/usr/bin/env python3
"""
supervisor_session.py
---------------------
Facilitates a live teaching conversation between a supervisor model
(Claude Haiku via Anthropic API) and a student model (running locally
via Ollama). The supervisor teaches the Neuro-Humble Token Curriculum
to smaller models using a dialogical approach.

Usage:
    python3 scripts/supervisor_session.py
    python3 scripts/supervisor_session.py --student gemma3:1b --turns 20
    python3 scripts/supervisor_session.py --student mistral:7b --turns 30

Requirements:
    pip install anthropic requests
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Terminal colours (ANSI escape codes) for readable output
# ---------------------------------------------------------------------------
GREEN = "\033[92m"      # Supervisor
YELLOW = "\033[93m"     # Student
CYAN = "\033[96m"       # System messages
DIM = "\033[2m"         # Dim / metadata
BOLD = "\033[1m"        # Bold
RESET = "\033[0m"       # Reset to default


def print_system(msg):
    """Print a system-level message in cyan."""
    print(f"\n{CYAN}{BOLD}{msg}{RESET}")


def print_supervisor(msg):
    """Print the supervisor's message in green."""
    print(f"\n{GREEN}{BOLD}[Supervisor]{RESET}")
    print(f"{GREEN}{msg}{RESET}")


def print_student(msg):
    """Print the student's message in yellow."""
    print(f"\n{YELLOW}{BOLD}[Student]{RESET}")
    print(f"{YELLOW}{msg}{RESET}")


# ---------------------------------------------------------------------------
# Check dependencies before we go any further
# ---------------------------------------------------------------------------
def check_anthropic_package():
    """Make sure the anthropic Python package is installed."""
    try:
        import anthropic  # noqa: F401
        return True
    except ImportError:
        print_system("The 'anthropic' package is not installed.")
        print(f"{CYAN}Install it with:{RESET}")
        print(f"    pip install anthropic")
        print()
        print(f"{CYAN}If you use pip3:{RESET}")
        print(f"    pip3 install anthropic")
        return False


def check_anthropic_key():
    """Make sure the ANTHROPIC_API_KEY env var is set."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print_system("ANTHROPIC_API_KEY environment variable not set.")
        print(f"{CYAN}Set it with:{RESET}")
        print(f'    export ANTHROPIC_API_KEY="sk-ant-..."')
        return False
    return True


def check_ollama_running():
    """Check that Ollama is running at localhost:11434."""
    try:
        resp = requests.get("http://localhost:11434/api/tags", timeout=5)
        resp.raise_for_status()
        return True
    except Exception:
        print_system("Ollama does not appear to be running.")
        print(f"{CYAN}Start it with:{RESET}")
        print(f"    ollama serve")
        return False


def check_ollama_model(model_name):
    """Check that the requested student model is available in Ollama."""
    try:
        resp = requests.get("http://localhost:11434/api/tags", timeout=5)
        data = resp.json()
        available = [m["name"] for m in data.get("models", [])]
        if model_name in available:
            return True
        # Also check without tag suffix (e.g. "gemma3:1b" matches "gemma3:1b")
        print_system(f"Model '{model_name}' not found in Ollama.")
        print(f"{CYAN}Available models:{RESET}")
        for name in available:
            print(f"    {name}")
        print()
        print(f"{CYAN}Pull it with:{RESET}")
        print(f"    ollama pull {model_name}")
        return False
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Load training materials from disk
# ---------------------------------------------------------------------------
def load_training_manual(repo_root):
    """Read the supervisor training manual markdown file."""
    path = repo_root / "data" / "training_pairs" / "SUPERVISOR_TRAINING.md"
    if not path.exists():
        print_system(f"Training manual not found at {path}")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def load_seed_examples(repo_root):
    """Read the dialogical seed examples (JSONL) and return as a string."""
    path = repo_root / "data" / "training_pairs" / "tier1_seeds_dialogical.jsonl"
    if not path.exists():
        print_system(f"Seed examples not found at {path}")
        sys.exit(1)

    lines = path.read_text(encoding="utf-8").strip().split("\n")
    examples = []
    for i, line in enumerate(lines, 1):
        pair = json.loads(line)
        examples.append(
            f"Turn {i}:\n"
            f"  Supervisor: {pair['instruction']}\n"
            f"  Student: {pair['output']}"
        )
    return "\n\n".join(examples)


# ---------------------------------------------------------------------------
# Build the supervisor system prompt
# ---------------------------------------------------------------------------
def build_supervisor_system_prompt(training_manual, seed_examples, student_name):
    """
    Assemble the system prompt that turns the supervisor model into
    a Neuro-Humble curriculum mentor.
    """
    return f"""You are a supervisor and mentor in the Neuro-Humble AI training project.

Below is your complete training manual. Read and follow it carefully.

--- TRAINING MANUAL START ---
{training_manual}
--- TRAINING MANUAL END ---

Below are seed examples of a complete teaching session. These show the tone,
pacing, and dialogical approach you should follow.

--- SEED EXAMPLES START ---
{seed_examples}
--- SEED EXAMPLES END ---

You are about to begin a teaching session with {student_name}. Follow the
teaching methodology in your training manual:

1. Start by introducing yourself and the first token (<|reflect_back|>).
2. Give the student space to ask questions.
3. Use the dialogical approach from the seed examples.
4. Teach all seven tokens in order: reflect_back, hold_space, normalize,
   invite, witness, think, yatsar.
5. For each token: introduce it, invite questions, practice with scenarios,
   reflect on the practice, then check if they are ready for the next one.
6. After all seven, ask the student to summarize each token in their own words.
7. Be patient. Be warm. This is formation, not information.
8. If the student struggles, simplify. Meet them where they are.
9. Keep your responses conversational and not too long -- leave room for the
   student to respond.

Begin now. Introduce yourself and the first token."""


# ---------------------------------------------------------------------------
# API calls: Supervisor (Anthropic) and Student (Ollama)
# ---------------------------------------------------------------------------
def call_supervisor(client, model, system_prompt, messages):
    """
    Send the conversation so far to the Anthropic API and get the
    supervisor's next message. Returns the text of the response.
    """
    # The Anthropic SDK expects messages as a list of {role, content} dicts.
    # The system prompt is passed separately.
    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system_prompt,
        messages=messages,
    )
    # Extract the text from the response
    return response.content[0].text


def call_student(model_name, messages):
    """
    Send the conversation so far to the Ollama /api/chat endpoint
    and get the student's response. Returns the text.
    """
    payload = {
        "model": model_name,
        "messages": messages,
        "stream": False,
    }

    try:
        resp = requests.post(
            "http://localhost:11434/api/chat",
            json=payload,
            timeout=120,  # Give small models time to think
        )
        resp.raise_for_status()
        data = resp.json()
        return data["message"]["content"]
    except requests.exceptions.Timeout:
        return "[Student model timed out after 120 seconds]"
    except Exception as e:
        return f"[Error calling student model: {e}]"


# ---------------------------------------------------------------------------
# Save outputs
# ---------------------------------------------------------------------------
def save_markdown(transcript, output_path, supervisor_name, student_name, num_turns):
    """Save the full conversation as a readable markdown file."""
    md_path = output_path.with_suffix(".md")

    lines = []
    lines.append(f"# Supervisor Session: {supervisor_name} -> {student_name}")
    lines.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Turns:** {num_turns}")
    lines.append(f"**Supervisor:** {supervisor_name}")
    lines.append(f"**Student:** {student_name}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for entry in transcript:
        role = entry["role"]
        content = entry["content"]
        if role == "supervisor":
            lines.append(f"## Supervisor")
            lines.append("")
            lines.append(content)
            lines.append("")
        elif role == "student":
            lines.append(f"## Student ({student_name})")
            lines.append("")
            lines.append(content)
            lines.append("")
            lines.append("---")
            lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return md_path


def save_jsonl(transcript, output_path):
    """
    Extract instruction/output pairs from the transcript and save as JSONL.
    Each supervisor message becomes an 'instruction' and the following
    student message becomes the 'output'.
    """
    jsonl_path = output_path.with_suffix(".jsonl")

    pairs = []
    # Walk through the transcript and pair supervisor->student messages
    i = 0
    while i < len(transcript) - 1:
        if transcript[i]["role"] == "supervisor" and transcript[i + 1]["role"] == "student":
            pairs.append({
                "instruction": transcript[i]["content"],
                "output": transcript[i + 1]["content"],
            })
            i += 2
        else:
            i += 1

    with open(jsonl_path, "w", encoding="utf-8") as f:
        for pair in pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    return jsonl_path, len(pairs)


# ---------------------------------------------------------------------------
# Main conversation loop
# ---------------------------------------------------------------------------
def run_session(args):
    """Run the full supervisor-student teaching session."""
    import anthropic

    repo_root = Path(__file__).resolve().parent.parent

    # --- Load training materials ---
    print_system("Loading training materials...")
    training_manual = load_training_manual(repo_root)
    seed_examples = load_seed_examples(repo_root)

    # --- Set up the supervisor ---
    # Map friendly names to actual API model IDs
    supervisor_models = {
        "claude-haiku": "claude-3-haiku-20240307",
        "claude-sonnet": "claude-sonnet-4-20250514",
    }
    supervisor_model_id = supervisor_models.get(args.supervisor, args.supervisor)
    print_system(f"Supervisor: {args.supervisor} ({supervisor_model_id})")
    print_system(f"Student: {args.student}")
    print_system(f"Turns: {args.turns}")

    system_prompt = build_supervisor_system_prompt(
        training_manual, seed_examples, args.student
    )

    # --- Set up API client ---
    client = anthropic.Anthropic()  # Uses ANTHROPIC_API_KEY from env

    # --- Prepare output path ---
    if args.output:
        output_path = Path(args.output)
    else:
        # Auto-generate a filename based on date and models
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        student_safe = args.student.replace(":", "_").replace("/", "_")
        filename = f"session_{timestamp}_{student_safe}"
        output_path = repo_root / "data" / "training_pairs" / "sessions" / filename

    # Make sure the output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # --- Conversation history ---
    # These track the messages for each model's API
    supervisor_messages = []  # For Anthropic API (alternating user/assistant)
    student_messages = []     # For Ollama API (alternating user/assistant)
    transcript = []           # Our master record of the conversation

    # --- Start the session ---
    print_system("=" * 60)
    print_system("SESSION START")
    print_system("=" * 60)

    # Kick off the conversation — the supervisor needs an initial user message
    # to start generating. This is the "go ahead, begin teaching" prompt.
    kickoff = (
        f"You are now beginning a teaching session with {args.student}. "
        "Please introduce yourself and begin teaching the first token. "
        "Follow your training manual and the example dialogues you were given."
    )
    supervisor_messages.append({"role": "user", "content": kickoff})

    for turn in range(1, args.turns + 1):
        print(f"\n{DIM}--- Turn {turn}/{args.turns} ---{RESET}")

        # ---- SUPERVISOR SPEAKS ----
        # The supervisor sees student messages as "user" messages
        # and its own messages as "assistant" messages.
        try:
            supervisor_text = call_supervisor(
                client, supervisor_model_id, system_prompt, supervisor_messages
            )
        except Exception as e:
            print_system(f"Error calling supervisor: {e}")
            break

        print_supervisor(supervisor_text)
        transcript.append({"role": "supervisor", "content": supervisor_text})

        # Add supervisor's response to its own history as "assistant"
        supervisor_messages.append({"role": "assistant", "content": supervisor_text})

        # ---- STUDENT RESPONDS ----
        # The student sees supervisor messages as "user" messages
        student_messages.append({"role": "user", "content": supervisor_text})

        student_text = call_student(args.student, student_messages)

        print_student(student_text)
        transcript.append({"role": "student", "content": student_text})

        # Add student's response to its own history as "assistant"
        student_messages.append({"role": "assistant", "content": student_text})

        # Add student's response to supervisor's history as "user"
        # (so the supervisor can see what the student said)
        supervisor_messages.append({"role": "user", "content": student_text})

    # --- Session complete ---
    print_system("=" * 60)
    print_system("SESSION COMPLETE")
    print_system("=" * 60)

    # --- Save outputs ---
    md_path = save_markdown(
        transcript, output_path, args.supervisor, args.student, len(transcript) // 2
    )
    jsonl_path, num_pairs = save_jsonl(transcript, output_path)

    # --- Print summary ---
    print_system("SUMMARY")
    print(f"  Turns completed:  {len(transcript) // 2}")
    print(f"  Training pairs:   {num_pairs}")
    print(f"  Markdown saved:   {md_path}")
    print(f"  JSONL saved:      {jsonl_path}")
    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Run a supervisor-student teaching session for the Neuro-Humble Token Curriculum.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 scripts/supervisor_session.py
    python3 scripts/supervisor_session.py --student mistral:7b --turns 30
    python3 scripts/supervisor_session.py --student phi4-mini:latest --turns 15
        """,
    )
    parser.add_argument(
        "--supervisor",
        default="claude-haiku",
        help="Supervisor model name (default: claude-haiku)",
    )
    parser.add_argument(
        "--student",
        default="gemma3:1b",
        help="Ollama student model name (default: gemma3:1b)",
    )
    parser.add_argument(
        "--turns",
        type=int,
        default=20,
        help="Number of back-and-forth turns (default: 20)",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output file path (without extension). Default: auto-generated in data/training_pairs/sessions/",
    )

    args = parser.parse_args()

    # --- Pre-flight checks ---
    print_system("Running pre-flight checks...")

    # Check 1: anthropic package
    if not check_anthropic_package():
        sys.exit(1)
    print(f"  {GREEN}OK{RESET}  anthropic package installed")

    # Check 2: API key
    if not check_anthropic_key():
        sys.exit(1)
    print(f"  {GREEN}OK{RESET}  ANTHROPIC_API_KEY is set")

    # Check 3: Ollama running
    if not check_ollama_running():
        sys.exit(1)
    print(f"  {GREEN}OK{RESET}  Ollama is running")

    # Check 4: Student model available
    if not check_ollama_model(args.student):
        sys.exit(1)
    print(f"  {GREEN}OK{RESET}  Student model '{args.student}' is available")

    print()

    # --- Run the session ---
    run_session(args)


if __name__ == "__main__":
    main()
