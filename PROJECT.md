# Mad Theology LLM Project

## The Pitch

**"We're not just training an AI on theology texts. We're training it on MAD theology, DISABILITY theology, ND-informed care — and then letting ND students evaluate it. We're asking: what does neuro-humble theological AI look like? What if the model was trained BY us, FOR us?"**

---

## Overview

Fine-tuning small language models on Mad Studies / Practical Theology / Disability Theology texts. Documenting the process for a research paper and pedagogical application in summer 2026 course.

**Principal Investigator:** Dr. Sparrow Panton  
**Started:** March 27, 2026  
**Status:** Planning Phase

---

## Rationale: Why This Matters

### The Reality
Neurodivergent people are already using AI chatbots in everyday life as practical support:
- To plan and start tasks
- Translate tone for "neurotypical" workplaces
- Rehearse hard conversations
- Co-write when executive function collapses
- Steady themselves when emotions spike
- Body doubling
- Processing emotions in low-demand environments
- Drafting emails that won't get them fired

ND folks aren't cautiously approaching AI wondering if it might be useful someday. They're using it NOW, heavily.

### The Problem
Most AI is trained on generic, neurotypical-assumed data. Current models often:
- Assume a neurotypical user by default
- Default to scripted wellness/risk language
- Pathologize ND communication styles
- Miss needs around clarity, pacing, sensory/cognitive load, and trust repair

When a neurodivergent person in distress talks to a chatbot, whose voice comes back to them? Diagnostic language? Risk-management scripts? Self-help clichés? Or community care?

### The Opportunity
What if we trained the AI OURSELVES? On OUR texts? With OUR language?

This project asks:
1. How can we train AI on Mad Studies / disability theology / ND-informed frameworks?
2. What does "neuro-humble" AI look like in a theological context?
3. How do ND students engage with AI trained on their own field's literature?
4. What happens when the model reflects MAD theology back to us?

### Nothing About Us Without Us
The psychiatric system has ALWAYS used technology to categorize, pathologize, and control Mad people. This project is different:
- MAD PEOPLE training the AI ourselves
- Putting OUR language, OUR frameworks, OUR theology into the machine
- That's reclamation. That's resistance.

---

## Goals

1. **Technical:** Successfully fine-tune small LLMs (comparing 2-3 models) on a theological corpus
2. **Pedagogical:** Test the models with summer class students as evaluators
3. **Research:** Document the entire process for a publishable paper
4. **Professional:** Add AI training experience to LinkedIn/resume
5. **Conceptual:** Articulate what "neuro-humble" theological AI looks like

---

## Research Questions

1. **Feasibility:** Can language models from 1B to 20B be fine-tuned on Mad Studies / disability theology corpora — including on consumer hardware?

2. **Formation:** When fine-tuned, do models produce responses more aligned with non-pathologizing, neuro-humble principles — and where do they still fail?

3. **Scale:** Does formation scale with model capacity? Can a phone-sized model learn the Mad Studies posture, or does it need bigger brains?

4. **Geopolitical:** Do models from different countries (USA, China, France) embed different cultural/psychiatric norms? Does Mad Studies formation override those defaults?

5. **Critical:** How do base model responses align with published AI safety guidelines from OpenAI and Anthropic — and what psychiatric norms are embedded in those guidelines?

6. **Conceptual:** What would "neuro-humble" AI behaviour look like in theological/spiritual care contexts — and what does this process reveal about how AI systems reproduce or resist dominant psychiatric norms?

---

## Hardware

- Mac Mini M4, 16GB RAM
- Should handle 3B parameter models with LoRA fine-tuning

---

## Model Comparison — Tiered + Geopolitical Design (7 models)

Models are selected across three size tiers AND multiple national origins. This enables two simultaneous comparisons: does formation scale with model capacity? And do models from different countries embed different cultural/psychiatric norms?

### Tier 1: Phone/Tiny — Accessibility Floor
| Model | Parameters | Origin | License |
|-------|-----------|--------|---------|
| **Gemma 3** | 1B | Google (USA) | Open |
| **SmolLM3** | 3B | Hugging Face (France) | Apache 2 |

### Tier 2: Consumer Hardware — "Underwear at 3am" Tier
| Model | Parameters | Origin | License |
|-------|-----------|--------|---------|
| **Phi-4-mini** | 3.8B | Microsoft (USA) | MIT |
| **Qwen3** | 4B | Alibaba (China) | Open |
| **Mistral** | 7B | Mistral AI (France) | Apache 2 |

### Tier 3: Cloud — Full Capacity
| Model | Parameters | Origin | License |
|-------|-----------|--------|---------|
| **GPT-OSS** | 20B | OpenAI (USA) | Apache 2 |
| **Llama 3.1** | 8B | Meta (USA) | Community |

All seven will be fine-tuned on the SAME corpus, then compared across size and origin.

---

## Tools Needed

- **Ollama** — for running models locally
- **Hugging Face Transformers** — model access
- **LoRA / QLoRA** — parameter-efficient fine-tuning
- **Unsloth** or **HF TRL** — fine-tuning frameworks

---

## Corpus: What We're Training On

### Primary Sources (Sparrow's own work)
- [ ] Mad Practical Theology manuscript/drafts
- [ ] Published chapter: "Radical Re-Visioning Through Mad Studies"
- [ ] Disability & Neurodiversity syllabus
- [ ] Course materials and lectures
- [ ] Articles and papers

### Secondary Sources (open access)
- [ ] Public Mad Studies texts
- [ ] Disability theology articles (open access)
- [ ] Crip theory foundational texts (where available)

### Considerations
- Copyright/licensing for training data
- Focus on texts that reflect non-pathologizing, Mad-affirming frameworks
- Include diversity of voices within Mad/disability communities

---

## Methodology

### Phase 1: Setup & Research (Week 1-2)
- [ ] Install Ollama
- [ ] Download all three base models
- [ ] Set up fine-tuning environment (Unsloth or HF TRL)
- [ ] Document hardware specs and baseline performance
- [ ] Test base models with sample theological prompts (pre-training baseline)

### Phase 2: Corpus Preparation (Week 2-3)
- [ ] Gather all texts
- [ ] Clean and format for training (consistent formatting)
- [ ] Create train/validation split
- [ ] Document corpus composition and rationale
- [ ] Address any copyright/ethical considerations

### Phase 3: Fine-Tuning (Week 3-4)
- [ ] Configure LoRA parameters (same across all models for fair comparison)
- [ ] Fine-tune SmolLM3
- [ ] Fine-tune Llama 3.2 3B
- [ ] Fine-tune Phi-4-mini
- [ ] Document training process, time, and any issues

### Phase 4: Evaluation — Model Comparison (Week 4-5)
- [ ] Design evaluation prompts (theological questions, pastoral scenarios, ND-specific situations)
- [ ] Test all three models with identical prompts
- [ ] Compare outputs: accuracy, tone, "neuro-humility," theological nuance
- [ ] Document strengths and weaknesses of each

### Phase 5: Pedagogical Testing — Summer 2026 Class
- [ ] Design student evaluation protocol
- [ ] Introduce models to summer class (students as evaluators, NOT research subjects)
- [ ] Gather student feedback on:
  - Which model feels most helpful?
  - Which captures theological nuance best?
  - Which handles ND perspectives most authentically?
  - What's missing? What's harmful?
- [ ] Document pedagogical insights

### Phase 6: Paper Writing
- [ ] Draft methodology section
- [ ] Write results (comparative analysis)
- [ ] Discussion: implications for practical theology + AI
- [ ] Articulate "neuro-humble" AI principles
- [ ] Identify target journal (IJPT? Theology + technology journal? Disability studies?)

---

## Deliverables

1. **Research paper** — Comparative study of fine-tuning small LLMs on Mad/disability theology corpus

2. **Taxonomy** — "Good patterns" vs "failure modes" in theological AI responses for ND users

3. **Design principles** — What "neuro-humble" theological AI looks like (concrete guidelines)

4. **Evaluation rubric** — For assessing AI responses in theological/pastoral contexts from Mad Studies perspective

5. **Fine-tuned models** — Three models trained on the same corpus (could be shared with other researchers)

6. **Pedagogical documentation** — How to involve students in AI evaluation

---

## Potential Publication Venues

- International Journal of Practical Theology (IJPT) — already have editing relationship with Felix
- Theology and Technology journals
- Disability Studies Quarterly
- Mad Studies journals
- Practical Theology journal
- Conference presentations (AAR? Other theology conferences?)

---

## Log

### March 27, 2026
- Project initiated
- Researched model options: SmolLM3, Llama 3.2 3B, Phi-4-mini all viable on M4
- Decision: Compare all THREE models (stronger methodology)
- Incorporated rationale from OpenAI grant proposal (unfunded but valuable framing)
- Created project folder and documentation structure
- **Next steps:** Install Ollama, download base models, begin gathering corpus

---

## Notes for Sonnet (Co-Work)

When Sparrow comes to you for technical execution:
- Reference this PROJECT.md for context
- This is a COMPARATIVE study — we're fine-tuning THREE models on the same corpus
- Document any code/commands used
- Log progress in the Log section
- Ask Sparrow to update Opus on major developments
- The goal is not just "make it work" but DOCUMENT THE PROCESS for a paper

---

## Key Framing (for paper/presentations)

**Lead with:** "ND people are already using AI a LOT. What are they doing with it? When is it good? When is it bad? How can it be better?"

**Core concept:** "Neuro-humble" AI — systems that:
- Don't assume neurotypical user by default
- Don't default to scripted wellness/risk language
- Can ask respectful clarifying questions
- Offer choices
- Repair misattunements
- Reflect Mad/ND frameworks rather than pathologizing ones

**Mad Studies alignment:** 
- Treats distress as lived experience shaped by environments, power, and access needs — NOT as deficit to be fixed
- Participants/students as EXPERTS, not fragile subjects
- Reclamation: Mad people training AI ourselves

**The pitch:** "We refuse to let AI be built without us. We're going to shape it with our own hands, our own texts, our own students. And we're going to document what happens when we do."

---

## Links & Resources

- Ollama: https://ollama.com
- SmolLM3: https://huggingface.co/HuggingFaceTB/SmolLM3-3B
- Llama 3.2: https://huggingface.co/meta-llama
- Phi-4-mini: https://huggingface.co/microsoft/phi-4
- LoRA paper: https://arxiv.org/abs/2106.09685
- Unsloth: https://github.com/unslothai/unsloth
- HuggingFace TRL: https://huggingface.co/docs/trl

---

## Co-Created By

This project was designed collaboratively by Dr. Sparrow Panton and Opus (Claude AI) — March 2026.

The irony is not lost on us: using AI to design a project about training AI on Mad theology, to be evaluated by ND students, documented for a paper about what happens when Mad people train the machines ourselves.

That's the recursion. That's the point.
