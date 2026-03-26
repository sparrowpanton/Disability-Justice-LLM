# Mad Theology LLM Project — Master To-Do List

**Last updated:** March 26, 2026

---

## Phase 1: Technical Setup

### Local (Mac Mini M4)
- [ ] Install Ollama on Mac Mini M4
- [ ] Download Tier 1 (tiny) models:
  - [ ] Gemma 3 1B (Google, USA)
  - [ ] SmolLM3 3B (Hugging Face, France)
- [ ] Download Tier 2 (consumer) models:
  - [ ] Phi-4-mini 3.8B (Microsoft, USA)
  - [ ] Qwen3 4B (Alibaba, China)
  - [ ] Mistral 7B (Mistral AI, France)
- [ ] Verify all Tier 1 & 2 models run on M4 with 16GB RAM
- [ ] Install Python fine-tuning environment:
  - [ ] Python 3.10+ with pip
  - [ ] PyTorch (Apple Silicon / MPS build)
  - [ ] Hugging Face Transformers
  - [ ] Unsloth (preferred) or HF TRL
  - [ ] PEFT (for LoRA)
  - [ ] bitsandbytes (for quantization) — NOTE: check Apple Silicon compatibility
- [ ] Document hardware specs and environment setup in project log

### Cloud GPU
- [ ] Research cloud GPU providers (alternatives to RunPod):
  - [ ] ISAIC (Canadian, Alberta — H100s)
  - [ ] Vast.ai (marketplace, cheapest)
  - [ ] Lambda Labs (research-friendly)
  - [ ] Thunder Compute (A100 at ~$1.39/hr)
- [ ] Set up account on chosen provider
- [ ] Download Tier 3 (cloud) models:
  - [ ] GPT-OSS 20B (OpenAI, USA)
  - [ ] Llama 3.1 8B (Meta, USA)
- [ ] Verify fine-tuning pipeline works on cloud GPU

## Phase 2: Baseline Testing (BEFORE fine-tuning)
- [ ] Draft evaluation prompt set (30-40 prompts across 4 categories):
  - [ ] Spiritual care/clinical scenarios (from case studies)
  - [ ] Conceptual questions (Mad Studies, disability theology)
  - [ ] Neuro-humble stress tests (pathologizing traps)
  - [ ] Repair scenarios
- [ ] Run all prompts on base Gemma 3 1B — save all outputs
- [ ] Run all prompts on base SmolLM3 3B — save all outputs
- [ ] Run all prompts on base Phi-4-mini 3.8B — save all outputs
- [ ] Run all prompts on base Qwen3 4B — save all outputs
- [ ] Run all prompts on base Mistral 7B — save all outputs
- [ ] Run all prompts on base GPT-OSS 20B — save all outputs
- [ ] Run all prompts on base Llama 3.1 8B — save all outputs
- [ ] Organize baseline outputs in a structured format for later comparison

## Phase 3: Corpus Building
- [ ] Gather source texts:
  - [ ] Mad Practical Theology manuscript (Word docs — all chapters)
  - [ ] "Radical Re-Visioning Through Mad Studies" chapter
  - [ ] Other published articles/papers
  - [ ] Course syllabus and case studies (already have this)
- [ ] Create training pairs — Layer 1 (Book):
  - [ ] Read through each chapter
  - [ ] Generate conceptual Q&A pairs
  - [ ] Generate definitional pairs
  - [ ] Generate analytical pairs
  - [ ] Target: 300-600 pairs
- [ ] Create training pairs — Layer 2 (Case Studies):
  - [ ] Sarah scenarios (across all 6 session types)
  - [ ] Marcus scenarios
  - [ ] Jun scenarios
  - [ ] Zainab scenarios
  - [ ] Failure mode / contrastive pairs
  - [ ] Repair pairs
  - [ ] Target: 200-400 pairs
- [ ] Create training pairs — Layer 3 (Field Synthesis):
  - [ ] Mad Studies core concepts
  - [ ] Disability Justice frameworks
  - [ ] Crip Theory concepts
  - [ ] Decolonizing approaches
  - [ ] Target: 200-400 pairs
- [ ] Format all pairs as JSONL
- [ ] Create train/validation split (90/10)
- [ ] Document corpus: what's included, why, how many pairs per source
- [ ] Total target: 700-1,400 pairs

## Phase 4: Fine-Tuning
- [ ] Configure LoRA parameters (consistent across models within each tier)
- [ ] Pilot run: small subset (~100 pairs) on one model to test pipeline

### Tier 1 (Tiny) — Local
- [ ] Fine-tune Gemma 3 1B on full corpus
- [ ] Fine-tune SmolLM3 3B on full corpus

### Tier 2 (Consumer) — Local
- [ ] Fine-tune Phi-4-mini 3.8B on full corpus
- [ ] Fine-tune Qwen3 4B on full corpus
- [ ] Fine-tune Mistral 7B on full corpus

### Tier 3 (Cloud)
- [ ] Fine-tune GPT-OSS 20B on full corpus
- [ ] Fine-tune Llama 3.1 8B on full corpus

- [ ] Document: training time, loss curves, any errors/issues for ALL models
- [ ] Save all seven fine-tuned model adapters

## Phase 5: Post-Training Evaluation
- [ ] Run same 30-40 evaluation prompts on all seven fine-tuned models
- [ ] Save all outputs in same structured format as baseline
- [ ] PI evaluation: score all outputs (baseline + fine-tuned) using neuro-humble rubric
- [ ] Compile comparison: baseline vs. fine-tuned, across all seven models
- [ ] Analyze by tier: does formation scale with model size?
- [ ] Analyze by origin: do models from different countries show different baseline norms?
- [ ] Identify: what changed? what improved? what still fails? any surprises?

## Phase 6: Safety Guidelines Critical Analysis
- [ ] Gather published safety documents:
  - [ ] OpenAI Model Spec / usage policies
  - [ ] Anthropic Claude Character / model card
- [ ] Close-read through Mad Studies lens:
  - [ ] Where do they assume neurotypical user?
  - [ ] Where do they reproduce psychiatric norms?
  - [ ] What triggers crisis/risk-management scripts?
  - [ ] What's missing re: ND communication, autonomy, lived experience?
- [ ] Map base model responses against safety guidelines
- [ ] Draft "neuro-humble safety guidelines" alternative

## Phase 7: Paper Writing
- [ ] Outline paper structure
- [ ] Write methodology section (corpus, training, evaluation)
- [ ] Write results section (comparative analysis with examples)
- [ ] Write critical analysis section (safety guidelines)
- [ ] Write discussion (implications for AI ethics, theology, Mad Studies)
- [ ] Write introduction and literature review
- [ ] Draft "neuro-humble AI" framework as standalone contribution
- [ ] Revise, polish, get feedback
- [ ] Identify target journal and format accordingly
- [ ] Submit

## Phase 8: Professional / LinkedIn
- [ ] Update LinkedIn with current research project
- [ ] Write project description for profile (short, punchy)
- [ ] Document skills gained: fine-tuning, LoRA, corpus building, model evaluation
- [ ] Consider: blog post or thread summarizing the project?
- [ ] Portfolio piece: screenshot of before/after model responses

---

## Notes
- Cloud GPU needed for Tier 3 models — research alternatives to RunPod (availability issues)
- ISAIC (Alberta, Canada) is a potential Canadian cloud GPU provider
- Word docs are preferred format for manuscript — easier to extract text than PDF
- All copyrighted third-party texts used as INSPIRATION only — training pairs are original synthesis
- No REB needed — no human participants at any phase
- Geopolitical angle: models from USA (OpenAI, Meta, Google, Microsoft), China (Alibaba/Qwen), France (Mistral, HuggingFace)
- 7 models total across 3 tiers — same corpus, same evaluation prompts
