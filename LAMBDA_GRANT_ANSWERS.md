# Lambda Research Grant — Short Answers

## Related Publications
https://github.com/sparrowpanton/MadTheologyLLM

---

## Research Problem
AI systems pathologize neurodivergent users. When Mad-identified or autistic people interact with language models during distress, they get crisis hotline scripts and diagnostic language that reproduce dominant psychiatric norms. This is embedded in AI safety guidelines themselves, which assume neurotypical users. No one has tested whether fine-tuning can change this. We fine-tune 7 open-source LLMs (1B-20B) on Mad Studies and disability theology texts, evaluating whether models shift toward "neuro-humble" responses. Success: measurable improvement on a novel evaluation rubric, critical analysis of AI safety norms, a published paper, and 7 fine-tuned models available to researchers.

---

## Relevance and Novelty
Growing work on AI bias in mental health and culturally responsive AI, but no one has fine-tuned LLMs on Mad Studies or disability theology texts, tested a "neuro-humble" AI framework empirically, used clinical formation pedagogy as a fine-tuning methodology, or critically analyzed AI safety guidelines through a disability justice lens with empirical evidence. Our novel concept of "formation not information" trains a model's posture rather than its knowledge, borrowing from how therapists are formed in clinical training. We also compare models from 4 countries (USA, China, France) to test how cultural psychiatric norms are exported through AI, extending critical scholarship on global mental health into AI for the first time.

---

## Challenges
Technical: Memory constraints on consumer hardware (mitigated with QLoRA and cloud GPUs for larger models). Corpus quality over quantity with ~1000 hand-authored training pairs. No existing benchmark for neuro-humble AI, so we build the rubric as part of the study. Cross-architecture comparability across 7 models from different developers. Non-technical: Critiquing AI safety guidelines is inherently political; we approach it as rigorous scholarship with empirical evidence. The PI is Mad, autistic, and disabled, researching AI responses to neurodivergent distress. We treat this as methodological strength consistent with Mad Studies epistemology.

---

## GPU Compute Needs
100

---

## Notable Achievements
SSHRC Doctoral Fellowship recipient. Author of Mad Practical Theology (forthcoming September 2026). Professor of Practical Theology at Emmanuel College, University of Toronto. Psychotherapist in training at CAMH (Centre for Addiction and Mental Health). Published scholarship on Mad Studies, disability theology, and neurodivergent-informed spiritual care.

---

## Partnerships and Support
Research situated at Emmanuel College, University of Toronto. Concurrent clinical training at CAMH, Canada's largest mental health research hospital. Published and forthcoming work developed with academic publishers and interdisciplinary colleagues across practical theology, disability studies, and Mad Studies. Current project co-developed with Claude (Anthropic AI) as research design and technical partner.

---

## Roadmap
April 2026: Baseline testing of all 7 models with 40 standardized prompts, initial rubric scoring. Late April: Corpus complete, 700-1400 training pairs in JSONL format. May: All 7 models fine-tuned with QLoRA, Tier 3 on Lambda cloud GPU. Late May: Post-training evaluation complete with comparative scoring. June: Safety guidelines critical analysis mapping base model responses against OpenAI and Anthropic documentation. July: Paper submitted to target journal, models and methodology published on GitHub.

---

## Publishing Plan
Paper submitted to journals including AI and Ethics, Disability and Society, and Practical Theology by July 2026. Open-source repository already live at github.com/sparrowpanton/MadTheologyLLM with research design and evaluation rubric. Fine-tuned model weights to be released on HuggingFace. Neuro-Humble AI Rubric published as standalone reusable tool. Conference submissions to AAR. PI's book Mad Practical Theology (September 2026) provides theoretical companion. Design principles for neuro-humble AI safety guidelines shared publicly.
