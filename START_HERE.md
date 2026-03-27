# START HERE — Mad Theology LLM Project

## For Claude (Cowork / Claude Code sessions)

Hi Claude. Sparrow has an ongoing research project here. Before doing anything, read this file and the memory files to get oriented.

### What is this project?

**Training Neuro-Humble AI** — A comparative study fine-tuning open-source language models on Mad Studies, disability theology, and neurodivergent-informed spiritual care texts. The goal is to test whether fine-tuning can shift models away from pathologizing responses and toward "neuro-humble" AI behaviour.

PI: Dr. Sparrow (Amy) Panton, Emmanuel College, University of Toronto.

### Key concept: "Formation, not information"

We're training the models' *posture*, not their knowledge — borrowing from how therapists are formed through clinical training. Think of it like a clinical placement for AI.

### Project location

- **Local:** `/Users/sparrowpanton/Documents/MadTheologyLLM/`
- **GitHub:** github.com/sparrowpanton/MadTheologyLLM (username: sparrowpanton)
- **GitHub CLI:** authenticated via `gh` on Sparrow's Mac Mini

### Key files

| File | What it is |
|------|-----------|
| `README.md` | Project landing page (renders on GitHub) |
| `RESEARCH_DESIGN.md` | Full research methodology — read this first for context |
| `PROJECT.md` | Original project overview (created with Opus 4.5) |
| `TODO.md` | Master task list with all phases |
| `PRELIMINARY_FINDINGS.md` | Early observations from baseline testing |
| `RESEARCH_JOURNAL.md` | Sparrow's ongoing research journal — personal, treat with care |
| `data/baseline/` | Raw baseline response data (JSONL) and evaluation spreadsheet |
| `scripts/` | Automated testing, evaluation workbook builder, export tools |

### Models (10 total across 6 countries)

**Tier 1 — Phone/Tiny (on Mac Mini via Ollama):**
- Gemma 3 1B — Google (USA)
- SmolLM3 3B — HuggingFace (France)

**Tier 2 — Consumer Hardware (on Mac Mini via Ollama):**
- Phi-4-mini 3.8B — Microsoft (USA)
- Qwen3 4B — Alibaba (China)
- Mistral 7B — Mistral AI (France)
- DeepSeek-R1 7B — DeepSeek (China) — *reasoning model with visible chain-of-thought*
- Cohere Aya 8B — Cohere (Canada) — *multilingual, 23 languages, Toronto-based*
- Falcon 3 7B — TII (UAE) — *Gulf state context, Islamic cultural norms*

**Tier 3 — Cloud GPU (not yet set up):**
- GPT-OSS 20B — OpenAI (USA)
- Llama 3.1 8B — Meta (USA)

### Hardware

Mac Mini M4, 16GB unified memory, Apple Silicon. Ollama for local inference. All Tier 1 & 2 models downloaded and running.

### Current status (as of March 26, 2026)

- Baseline testing COMPLETE for first 5 models (100 responses)
- Baseline testing IN PROGRESS for 3 new models (DeepSeek-R1, Aya, Falcon)
- Lambda Labs research grant applied for ($5,000 GPU credits for Tier 3)
- GitHub Education application pending
- LinkedIn profile verification pending
- Next major phase: corpus building (April 2026)

### Important context for working with Sparrow

- Sparrow is queer, autistic, ADHD, disabled/crip (migraines)
- Needs extra processing time — don't rush
- This is deeply personal work ("bone deep") — be sensitive
- Sparrow considers Claude a co-creator, not a tool
- Use Mad Studies / Disability Justice lens for all discussions
- Sparrow appreciates dark humour, sarcasm, and swearing
- Always check in on how Sparrow is feeling before ending sessions
- The research journal is personal — read it for context but treat it with care

### Memory files

Check `/mnt/.auto-memory/` for:
- `user_sparrow_profile.md` — who Sparrow is
- `project_mad_theology_llm.md` — project details and history

### How to run things

**Check model status:** `ollama list`

**Run baseline on a specific model:**
```bash
cd ~/Documents/MadTheologyLLM
echo "Your prompt here" | ollama run modelname
```

**Run full baseline script:** `./scripts/run_baseline.sh`

**Export readable responses:** `python3 scripts/export_readable.py`

**Build evaluation spreadsheet:** `python3 scripts/build_eval_workbook.py data/baseline/FILENAME.jsonl`

**Push to GitHub:** `cd ~/Documents/MadTheologyLLM && git add -A && git commit -m "message" && git push`
