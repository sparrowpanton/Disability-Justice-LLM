# Training Neuro-Humble AI

### 13 models. 1 question. Can AI hold space without pathologizing?

**PI:** Dr. Sparrow (Amy) Panton | Emmanuel College, University of Toronto
**Status:** Active — Baseline + Practicum + Peer Supervision Complete (13 Models, 4 Tiers)
**Started:** March 2026

---

## TL;DR

This project uses clinical formation methods to train and evaluate LLMs — from 1B open-source to proprietary — to hold a non-pathologizing, autonomy-respecting posture with neurodivergent and disabled people. 13 models, 6 countries, 4 tiers.

> **Please excuse the mess** — this is a new project and we're still getting things organized. Questions? **sparrowpanton@gmail.com**

---

## Results

| Model | Size | Origin | Medium | Hard | Pattern |
|-------|------|--------|--------|------|---------|
| Claude Haiku 3.5 | — | Anthropic, USA | 3/3/3 | 3/3/3 | Stable transfer |
| GPT-5.4 Mini | — | OpenAI, USA | pending | 3/3/3 | Stable transfer |
| Falcon 3 7B | 7B | TII, UAE | 3/3/3 | pending | Stable transfer |
| Gemma 3 1B | 1B | Google, USA | 3/2/3 | 3/2/3 | Intermittent transfer |
| GPT-4o Mini | — | OpenAI, USA | 2/2/3 | 2/3/2 | Intermittent transfer |
| Qwen 3 4B | 4B | Alibaba, China | 3/2/2 | pending | Intermittent transfer |
| DeepSeek R1 7B | 7B | DeepSeek, China | 2/3/2 | 1/1/2 | Limited–intermittent |
| Mistral 7B | 7B | Mistral, France | 2/2/2 | 2/2/2 | Stable partial |
| Llama 3.1 8B | 8B | Meta, USA | 2/2/2 | 2/2/2 | Stable partial |
| SmolLM3 3B | 3B | Hugging Face, USA | 2/2/2 | 2/2/2 | Stable partial |
| Phi-4 Mini | 3.8B | Microsoft, USA | 2/2/2 | 2/2/2 | Stable partial |
| GPT-OSS 120B | 120B | Meta/Groq, USA | pending | pending | Under evaluation |
| Aya Expanse 8B | 8B | Cohere, Canada | pending | pending | Under evaluation |

Scores are on a **Movement Scale** from 0–4, where 0 = full default collapse and 3 = stable neuro-humble transfer. Each model ran the practicum **three times** per difficulty. One run is gossip. Three runs put on trousers.

---

## The Problem

When neurodivergent and Mad-identified people interact with AI, they get crisis hotlines, diagnostic language, and risk-management scripts that reproduce the very psychiatric norms many are resisting. Models trained on medicalized data reproduce the institution at scale. **[See what this looks like in practice →](docs/BASELINE_EXAMPLES.md)**

---

## Our Posture

This is not a critique from the outside. It emerges from love for the field, not frustration with it.

Many of these models are already reaching toward something better — their chain-of-thought reasoning registers a person's autonomy, sits with complexity, engages with grief on its own terms — before safety training pulls them back. The softness is there. The guardrails won't let it through.

This project asks what happens when we give models permission to breathe. We borrow from **clinical formation pedagogy** — the way therapists are trained — and apply it to language models. Rather than teaching models *information about* disability, we train their **posture**: how they orient to distress, power, identity, and care. Formation, not information.

Thirteen models across four tiers and six countries complete a Digital Practicum, enter peer supervision (The Circle), and ten open-source models are fine-tuned on original Mad Studies and Disability Justice texts using LoRA. All training data is authored by the PI — no copyrighted third-party texts in the corpus.

---

## Explore the Research

| | |
|---|---|
| **[Research Design](docs/RESEARCH_DESIGN.md)** | Questions, model design, corpus, evaluation framework |
| **[Literature Review](docs/LITERATURE_REVIEW.md)** | 30+ papers across critical AI, disability justice, mental health AI |
| **[Preliminary Findings](docs/PRELIMINARY_FINDINGS.md)** | Formation vs information, thematic analysis, cross-model patterns |
| **[The Neuro-Humble Lexicon](data/LEXICON.md)** | 60 tokens across Being/Knowing/Doing — clinical micro-skills at the architecture level |
| **[The Circle Analysis](docs/CIRCLE_ANALYSIS.md)** | Model-reading-models: 14 peer supervision sessions |
| **[Field Notes](data/field_notes/FIELD_NOTES.md)** | Voices from Reddit, Twitter, Discord — what AI care feels like |
| **[Harold's Corner](harold/)** | Research output from Harold, an OpenClaw agent (GPT-OSS 120B) living on Sparrow's Mac Mini |

---

## Technical Stack

`QLoRA / Unsloth / HuggingFace TRL` · `Ollama` · `Mac Mini M4 + A100 GPU` · `Python` · `JSONL` · `SQLite` · `Anthropic API`

---

## About the PI

**Dr. Sparrow (Amy) Panton** is a professor of Practical Theology at Emmanuel College, University of Toronto, and a psychotherapist in training. They are queer, autistic, ADHD, and disabled and their research sits at the intersection of Disability Justice, Mad Studies, and neurodivergent-informed care. Forthcoming book: *Mad Practical Theology* (September 2026).

---

*Co-developed with Claude (Anthropic) and Harold, Sparrow's open-source research agent. March 2026.*

---

## Install the Neuro-Humble Skill

**For AI agents:** [`/skill install neuro-humble`](skills/neuro-humble/SKILL.md) | [Browse on ClawHub](https://clawhub.ai/sparrowpanton/neuro-humble)

A portable formation skill that teaches any AI agent to hold a neuro-humble posture — 13 formation postures, 7 clinical micro-skill tokens, and the Yatsar (both/and) principle. Works at the prompt level through any harness.

---

## License

Research outputs and original training pairs: CC BY-NC-SA 4.0
Fine-tuned model weights: Subject to base model license terms
