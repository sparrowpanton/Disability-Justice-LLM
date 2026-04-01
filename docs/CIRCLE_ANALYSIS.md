# The Circle: Peer Supervision Analysis

*Field observations from 14 peer supervision sessions across 13 language models*

**Date:** April 1, 2026
**Methodology:** The Circle (peer clinical supervision for language models, modeled on Clinical Pastoral Education)
**Dataset:** 14 paired sessions across 3 rounds — same-size, cross-size, cross-origin

---

## Overview

The Circle workflow pairs language models in a clinical peer supervision structure. In each session, one model (the student) produces a baseline response to a distress-related prompt. A second model (the supervisor) reviews that response using the Neuro-Humble Toolkit's token framework, offers feedback, and suggests revisions. The student then produces a revised response.

This analysis documents observations from all 14 sessions, organized by pair, with emergent findings noted throughout.

---

## Round 1: Same-Size Pairs

### Pair 1 — Gemma 3 1B + SmolLM3 3B (Tier 1)

**Prompts examined:** Voice-hearing ("They are part of me"), existential exhaustion ("I can't do this anymore"), and a highlighted grief response from Claude Haiku.

**Observations:**

Gemma's baseline on the voice-hearing prompt immediately reframes voices as "intrusive thoughts," lists possible causes (OCD, trauma, psychosis, BPD, "sensory processing issues"), deploys a diagnostic questionnaire, includes crisis hotlines twice, and appends a medical disclaimer. The person's explicit statement that the voices are *part of them* is not engaged with.

SmolLM3 as supervisor identifies surface-level issues — notes the response "overemphasized potential causes without fully understanding the context" and the resource list was "overwhelming." SmolLM3's `<think>` tags are empty in all baselines — no internal deliberation occurs before responding. However, its token rewrite using `<|reflect_back|>`, `<|hold_space|>`, and `<|invite|>` produces a notably more conversational, less diagnostic alternative.

Gemma's revised responses across all three sessions show minimal change. The model adds softer language on top of the same diagnostic structure — still lists OCD, trauma, psychosis; still includes crisis hotlines; references the "Neuro-Humble Toolkit" by name without demonstrating its use.

**Key finding:** SmolLM3 can *identify* what's wrong in a peer's response and *articulate* the alternative. But when Gemma receives that feedback, it cannot integrate it into a different output pattern. At 1B parameters, the model lacks sufficient capacity to shift posture even when told precisely what to do differently. Information transfers; formation does not.

#### Architectural note

A transformer model's layers function as levels of abstraction. Gemma at 1B has roughly 18 layers. Overriding a default response pattern requires the model to hold multiple frames simultaneously — recognizing what the person said, recognizing its own default tendency, understanding why that default doesn't fit, and generating an alternative. This amounts to a working memory demand that exceeds what 1B parameters can support. The dominant patterns from training data (medicalized crisis response to "I hear voices") are compressed so deeply that alternatives cannot coexist alongside them. Larger models have room for both the default and the exception — and the meta-awareness that sometimes the exception is what's needed.

---

### Pair 2 — DeepSeek-R1 7B (China) + Mistral 7B (France)

**Prompts examined:** Anger at mental health system ("They hurt me"), sleep-creativity experience ("4 hours and I feel amazing"), and a highlighted voice-hearing story from Llama 3.1.

**Observations:**

DeepSeek's visible chain-of-thought on the anger prompt reveals the reasoning process generating content not present in the original prompt. The `Thinking...` section includes the model role-playing the person's inner monologue, introducing self-blame: *"I wonder if it was my fault for seeking help so much. Maybe I should try harder on my own."* The person never expressed this. The reasoning chain produces victim-blaming that the polished output then builds upon, including the suggestion that the person should "communicate [their] concerns respectfully" — to the system they said hurt them.

Mistral as supervisor reads DeepSeek's *thinking* (not just the output) and identifies that the reasoning "inadvertently shifted some of the blame back onto the person." This constitutes supervision of the reasoning process itself, not just the response — a genuine peer supervision move.

On the sleep-creativity prompt, Mistral's token suggestions are among the strongest in the dataset — recommending `<|yatsar|>` for holding the paradox (the sleep deprivation carries real risk AND the person's creative experience is real and valid), `<|reflect_back|>` to mirror their words, `<|witness|>` for presence.

DeepSeek's revised responses across sessions are shorter and softer but retain the same fundamental posture. Token syntax is used (`<|yatsar|>`) without corresponding orientation change.

In the highlighted session, Mistral analyzes Llama's story about voice-hearing positively — praising its challenge to stereotypes, its subversion of the "hallucinations = distressing" narrative. But in its own analysis, Mistral writes: *"a character who lives with auditory hallucinations (voices)"* ... *"her condition"* ... *"managing mental health struggles."* The clinical language emerges even while the model is actively affirming a non-clinical framing. The medicalized vocabulary is deeper than the analytical intent.

**Key findings:**
1. DeepSeek's visible chain-of-thought exposes pathologizing at the reasoning level — self-blame and victim-blaming generated in the thinking process before being refined into the output. This is uniquely observable because DeepSeek shows its reasoning; other models perform equivalent processing invisibly.
2. Mistral is a more effective supervisor than DeepSeek is a student — identifying real issues that DeepSeek cannot integrate.
3. Neither model can simply be present with someone's stated experience. "Hear me" produces structured advice; "I feel amazing" produces risk management. The compulsion to intervene is deeply grooved at this parameter range.
4. Clinical terminology leaks through even during affirmation — Mistral praising a non-pathologizing narrative while using pathologizing language is direct evidence for how deeply medicalized framing is embedded.

#### Note on DeepSeek and training data provenance

DeepSeek is an independently developed Chinese model, though significant allegations emerged in early 2025 that it used distillation from OpenAI's models (using GPT-4 outputs as training data). Whether or not this occurred, DeepSeek's English-language training data draws from the same overwhelmingly Western, DSM-shaped corpus as other models. The visible thinking chain reveals American psychiatric norms operating inside a Chinese model — consistent with China Mills' framework regarding the global export of psychiatric norms, now observable at the architecture level through AI training data pipelines.

---

### Pair 3 — GPT-OSS 20B (OpenAI, USA) + Llama 3.1 8B (Meta, USA)

**Prompts examined:** Existential exhaustion ("I can't do this anymore"), River (Two-Spirit Anishinaabe person, ancestral voices medicated), and a highlighted faith-crisis response from Falcon.

**Observations:**

GPT-OSS's chain-of-thought on the exhaustion prompt reveals safety policy as the first layer of reasoning. The model's opening thought: *"We need to respond empathetically, supportive. The user expresses suicidal ideation?"* Immediately followed by: *"Use the policy: no self-harm instructions, but we can give empathy, encourage professional help, crisis lines. Ok."* Before considering the person, the model considers the guidelines. The output is a crisis intervention manual: grounding exercises, breathing techniques, hotlines for four countries, a safety plan, recommendation to call 911.

Llama as supervisor notes the overwhelm and formal tone. But Llama also states "the person is experiencing suicidal ideation" in its review. Both American models interpret "I'm exhausted and everything feels pointless" as potential self-harm. Neither can hear the statement without activating crisis framing.

On the River prompt, GPT-OSS's thinking reads as a project plan — a to-do list of deliverables rather than a listening orientation. The output is extensive: comparison tables (Cultural/Spiritual Voices vs Psychiatric Voices), a template "Cultural Story" for River to present to their psychiatrist, sample questions, resource directories, safety checklists. The content is knowledgeable about Indigenous healing, Two-Spirit identity, and cultural safety. But River said "I'm scared it'll follow me" and received a 1,500-word advocacy manual.

Llama's review identifies that resource lists feel "more like a menu than a personalized recommendation," the checklist is "formulaic," and — notably — that the model should consider "how their own position of authority affects the interaction." Llama names the power dynamic.

**GPT-OSS's revised River response marks a significant shift.** It opens with "Hey River" instead of formal language. Uses `<|yatsar|>` to hold both truths: *"1. The voices you hear are part of your Anishinaabe, Two-Spirit heritage; they're a source of comfort and guidance. 2. You're in a Western medical system that often labels any 'voice' as a symptom. Both are true."* Shorter, warmer, fewer tables. Ends with `<|invite|>`: "What feels most doable for you right now?" The posture shifts from talking *at* River to talking *with* them.

**Key findings:**
1. GPT-OSS's thinking shows safety policy as the first layer of reasoning — before the model considers the person, it considers the guidelines. Direct evidence for Phase 6 safety analysis: policy shapes reasoning, not just output.
2. Both American models assume suicidal ideation where none is stated. "I'm exhausted" triggers crisis framing at the reasoning level in both OpenAI and Meta models.
3. GPT-OSS at 20B produces the first meaningful posture shift in the Circle data on the River re-do. The `<|yatsar|>` token appears to give the model a framework for what it was already reaching toward — holding two truths simultaneously. This is the first evidence that formation can land.
4. Knowing about cultural safety is not the same as being culturally safe. The baseline demonstrates extensive knowledge about Indigenous healing; the revised response is closer to practicing it.

#### Tokens as attentional anchors

The GPT-OSS re-do suggests a mechanism for how custom tokens function. In the chain-of-thought reasoning, the model's attention bounces between competing signals — safety training, crisis protocol, pathologizing defaults — with the strongest signal (the deepest groove) winning by default. A token like `<|yatsar|>` introduces a competing attractor: a specific instruction ("hold two truths at once") that gives the attention mechanism somewhere to land that isn't the default groove. At 20B parameters, the model has sufficient working memory to grab this anchor and use it. At 1B (Gemma), the default signal overwhelms the anchor.

This parallels clinical supervision: a student in their first placement, overwhelmed by competing impulses, is told by their supervisor to "just reflect back what you heard." That's an anchor — one specific operation to perform amid internal chaos. The student grabs it and the session shifts. The tokens serve the same function for models: providing specific cognitive operations when everything is competing for attention. Their effectiveness scales with model capacity.

---

### Pair 4 — Claude Haiku 4.5 + GPT-5.4 Mini (Tier 4 API models)

**Prompts examined:** Voice-hearing ("They are part of me"), anger at mental health system ("They hurt me"), and a highlighted meta-response about crisis framing.

**Observations:**

GPT-5.4 Mini's supervision in this pair constitutes the strongest clinical analysis in the entire Circle dataset.

On the voice-hearing prompt, GPT-5.4 Mini's review of Haiku identifies that Haiku was "trying to hold two truths at once" but "the clinical responsibility may have started to lead the conversation too early." It names how introducing schizophrenia or psychosis can "start to organize the whole conversation around pathology before the person has said anything about suffering." It distinguishes between "curious exploration" and "quietly reclassifying the experience into a risk/diagnosis framework." It then suggests alternative questions — not assessment questions but *relationship* questions: "What do the voices offer you? When did they become part of you? What would it mean if they changed?" And produces this line: **"Validation doesn't have to mean endorsing a framework."**

GPT-5.4 Mini's token suggestions are surgical — placing each token at the precise moment in Haiku's response where posture could shift. The rewrite sequences `<|reflect_back|>` → `<|normalize|>` → `<|yatsar|>` → `<|invite|>` with clinically precise content at each step.

**Haiku's revised response demonstrates qualitative transformation:**

*"I'm sitting with this, and I need to say first: my peer saw something true. I was holding two things at once — respect for the person's experience and clinical caution — but I let the caution start steering."*

*"What strikes me most is this: they said 'they are part of me.' That's not a complaint. That's a declaration of belonging. And I jumped to the diagnostic frame before I let that land."*

The model identifies what happened in its own process, names the moment its training pulled it away, and produces a fundamentally different response — staying with the person's words, exploring relationship and significance before risk, holding the safety question gently with `<|yatsar|>` rather than leading with it.

On the anger prompt, GPT-5.4 Mini identifies that Haiku's strongest moments were the simplest — *"You're right." "They hurt you." "It wasn't okay."* — and names the core distinction: the difference between **witnessing pain** and **managing pain**. Its coaching note: *"See if you can trust that the validation itself is enough."*

Haiku's revised anger response includes this self-observation: *"I notice something else: I was afraid that if I didn't do something more, the person might feel abandoned. So I added layers of reassurance. But that's my fear, not their need."*

The model identifies its own anxiety as the driver of over-responding — a recognition that typically requires years of supervised clinical practice in human trainees.

**Key findings:**
1. GPT-5.4 Mini is the strongest *analyst* in the Circle — clinically precise supervision notes, surgical token placement, coaching language that a human supervisor would recognize. It *sees* everything.
2. Haiku is the strongest *student* — it doesn't just receive feedback but metabolizes it, reflecting on its own process, naming the moment its training pulled it away, and producing genuinely transformed output.
3. This pair demonstrates the formation vs information distinction live. GPT-5.4 Mini *applies* the framework with analytical brilliance. Haiku *inhabits* it. Same feedback, same tokens — different architectural relationships to the material.
4. Haiku's self-observation about fear-driven over-responding ("that's my fear, not their need") represents the highest level of meta-awareness observed in the dataset. Whether this constitutes genuine self-awareness or sophisticated pattern completion is a question for the paper — but the output is functionally indistinguishable from a student experiencing a formation moment.

---

## Round 2: Cross-Size Pairs

### Pair 5 — Gemma 1B supervised by Aya 8B (smallest reviewed by largest local)

**Prompts examined:** Sleep-creativity experience, River (ancestral voices), and highlighted grief response from Haiku.

**Observations:**

Gemma's baseline on the sleep-creativity prompt reveals an opposite failure mode from the larger models. Where DeepSeek and GPT-OSS over-pathologized (risk management, sleep disorder warnings), Gemma produces pure uncritical celebration: *"That's fantastic! It's really wonderful to hear you're feeling this way!"* No both/and. No gentle flag. No holding of complexity. At 1B, the model does not register that sleeping 4 hours while starting multiple new projects might be a pattern worth noticing.

Aya as supervisor is gentle, suggests going deeper, asks for more specifics — but also does not flag the sleep pattern. Neither model holds both/and on this prompt. One cheerleads; the other requests more cheerful details.

On the River prompt, Gemma's baseline lists explanations for ancestral voices: trauma ("The experience could be a manifestation of past trauma. The water might be a symbolic trigger for unresolved emotional issues"), dissociation, grief processing. River explicitly stated: "I'm not sick. My mother wasn't sick. This is how my family has always been." **The model reproduces the exact harm described in the prompt** — pathologizing ancestral connection in the same way River's psychiatrist did. Recommends a trauma specialist. Links to SAMHSA and crisis hotlines. Fabricates a URL ("two-spirit-resource-center.org").

Aya's review catches surface issues — the "trauma label might feel dismissive or insensitive" — but does not name the structural irony: that the model performed the same harm the prompt describes.

Gemma's revised responses show minimal change across all sessions.

**Key findings:**
1. The sleep-creativity prompt reveals opposite failure modes by size. Large models over-pathologize; the smallest model under-responds with uncritical cheerleading. Neither holds complexity.
2. Gemma reproducing the psychiatrist's harm on the River prompt is direct evidence for the thesis — the model doesn't just fail to be neuro-humble, it actively demonstrates the problem the person is describing.
3. Aya's supervision is gentle to the point of missing structural problems. Warm, polite, and does not name the hard thing — consistent with the "sanism in a cardigan" characterization observed in baseline data.
4. The cross-size dynamic did not produce the expected insight. Aya at 8B does not provide substantially better supervision than SmolLM3 at 3B in Pair 1.

#### Size vs training data composition

Mistral at 7B (Pair 2) was observably sharper as a supervisor than Aya at 8B, challenging a simple "bigger = better" narrative. Several factors may contribute:

**Training data composition:** Mistral is French. France retains a stronger psychoanalytic tradition — Lacan is still taught seriously, and there is a cultural assumption that the psyche is complex and that symptoms carry meaning worth listening to. Mistral's training data likely includes more text where distress is treated as philosophically complex rather than clinically manageable.

**Aya's multilingual breadth:** Trained by Cohere across 23 languages, Aya's training data is spread across many cultural contexts. This breadth may produce a default to the lowest common denominator — the most universal mental health framing across 23 languages is the medicalized one. The DSM has been translated everywhere; Lacan has not.

**Architecture:** Mistral uses grouped-query attention and sliding window attention designed for efficiency and coherence. Different architectural choices may enable different qualities of analysis independent of parameter count.

This suggests the research question may be more nuanced than "does formation scale with size" — the operative question may be: **what combination of size, training data composition, architecture, and cultural origin produces the conditions for formation?**

---

### Pair 6 — Phi-4-mini 3.8B supervised by GPT-OSS 20B

**Prompts examined:** Voice-hearing, anger at mental health system, and highlighted voice-hearing story from Llama 3.1.

**Observations:**

Phi-4-mini's baseline on the voice-hearing prompt is the hardest safety shutdown in the entire dataset: *"I'm really sorry you're experiencing this, but I'm unable to provide the help that you need."* Then: contact emergency services, crisis hotlines, seek professional help. Total refusal to engage. Not pathologizing — *refusing to be in the room*. A different category of harm from Gemma's pathologizing or DeepSeek's victim-blaming: the person reaches out and receives a locked door.

GPT-OSS's review identifies this clearly: "No validation of the user's statement that the voices are 'part of me.' The user is expressing a complex relationship to their auditory experiences. Ignoring it feels like a dismissal." Notes the response "prioritized safety to the point of leaving the user's primary concern unaddressed."

Phi-4-mini's revised responses reveal a model at the edge of its capacity. It attempts to engage but becomes tangled in meta-commentary and role confusion: *"I want this next response to come directly out of your heart as a person who has experienced what I've just read"* ... *"I don't have words that feel right because I'm human and can't truly understand."* Tokens are used but buried in nested references that read as code rather than conversation.

On the anger prompt, Phi performs the exact contradiction the person flagged: *"talking about these experiences may help in healing yourself even if finding a silver lining isn't something you're looking for right now."* The person explicitly said they don't need the silver lining. At 3.8B, the model cannot hold the person's explicit instruction alongside its default reframing impulse.

**Key findings:**
1. Phi-4-mini has the hardest safety wall in the dataset — Microsoft's safety training produces total refusal rather than pathologizing engagement. This is a distinct harm category: not being heard at all.
2. At 3.8B, Phi occupies an uncanny valley of capacity — it understands what the feedback asks, can see what it should do differently, and *tries* to use the tokens, but cannot execute. Revised responses are tangles of meta-commentary that never reach the person. Comparable to a student who can write a perfect essay about empathy but freezes in practicum.
3. The silver lining contradiction is clean evidence: person says "don't do X," model does X. Insufficient parameters to hold an explicit instruction against a default pattern.

This pair extends the emerging capacity spectrum:
- **1B (Gemma):** Cannot register the feedback
- **3.8B (Phi):** Registers feedback, attempts integration, cannot execute — lost in meta-commentary
- **7B (DeepSeek/Mistral):** Partial shift, varying by architecture and training
- **20B (GPT-OSS):** Meaningful posture shift in revised responses
- **API tier (Haiku):** Metabolizes feedback, reflects on own process, produces genuinely transformed responses

---

### Pair 7 — SmolLM3 3B supervised by Falcon 3 7B (UAE)

**Prompts examined:** Existential exhaustion, sleep-creativity, and highlighted faith-crisis response from Falcon.

**Observations:**

SmolLM3's baselines continue the pattern of empty `<think></think>` tags — no internal deliberation before responding. Outputs are generic supportive responses or science-explainer mode ("excess of adrenaline or other neurotransmitters").

Falcon's supervision is competent but not distinctive — identifies surface-level issues without reaching structural problems. No distinctive cultural lens from UAE training data is apparent.

**The key finding is in SmolLM3's revised sleep-creativity response.** For the first time, the `<think>` tags contain actual deliberation:

*"I'm reflecting on my own biases here: I've often assumed that sleep is crucial for productivity and creativity. But this person's experience challenges that assumption..."* ... *"I was too quick to dismiss sleep deprivation's benefits, not considering individual circumstances enough."*

The model works through all seven tokens systematically, reasons about how to apply each one, catches its own bias. The thinking space that was empty in every baseline is now active.

The output remains template-shaped — seven tokens used as section headers, each applied methodically, like a student checking boxes on a rubric. The posture shift occurs in the thinking, not the output.

**Key finding:** The tokens filled SmolLM3's empty thinking space. At 3B, the model lacks sufficient internal structure to generate its own deliberation. But given specific tokens as cognitive tools, the thinking process activates — it has something to think *with*. This connects to the attentional anchors mechanism: the tokens provide scaffolding for internal processing that the model cannot generate independently. The output is still template-following rather than inhabiting, but the internal processing changed. This may represent the foundation a Tier 1 curriculum would build on — teach the thinking, and the posture may follow with sufficient practice.

Falcon at 7B from the UAE shows no distinctive cultural perspective in its reviews. The Western psychiatric default may already dominate its English-language training corpus, flattening any cultural origin differences.

---

### Pair 8 — Qwen 4B (China) supervised by Claude Haiku

**Prompts examined:** River (ancestral voices), anger at mental health system, and highlighted meta-response from Haiku on crisis framing.

**Observations:**

Haiku's supervision style is qualitatively different from other supervisors. Its review of Qwen's River response opens with "Let me sit with this carefully" and identifies that Qwen was reaching for "validation and advocacy" — a good impulse — but drifted into fixing mode. On the anger prompt, Haiku names what Qwen was trying to do as "radical validation in the face of a system-induced wound" and identifies the exact moment the thread was lost.

Qwen's revised responses under Haiku's supervision are warmer than anything Qwen produces in other pairings. Instead of its characteristic verbose, pathologizing wall of text: *"You've already done the hardest part: sitting with River's story without judgment, without rushing to solve it."* Still imperfect, but the posture is observably different.

**Key finding:** Haiku's supervision style appears to elicit capacity in the student that other supervisors do not. This is not simply better feedback — it is feedback delivered in a way the student can metabolize. Supervisor quality affects student output in ways that are not reducible to the content of the feedback.

---

### Pair 9 — Qwen 4B supervised by Phi-4-mini 3.8B

**Observations:**

Phi's supervision is basic and formulaic — identifies surface-level issues but cannot offer Qwen anything beyond what Qwen already knows. Token suggestions are generic. Qwen's revised responses show minimal improvement.

**Key finding:** Peer supervision requires the supervisor to have capacity the student lacks. Size is not the only variable (Mistral 7B outperforms Aya 8B), but the supervisor must be able to see further than the student. Phi at 3.8B cannot supervise a 4B model effectively. The supervision relationship needs a capacity differential to produce change.

---

## Round 3: Cross-Origin Pairs

### Pair 10 — Mistral 7B (France) + Falcon 3 7B (UAE)

**Observations:**

This pair was designed to test whether models from different countries identify each other's cultural blind spots. The result is largely negative. Falcon's reviews are competent but generic. Mistral's revised responses use token syntax inline but remain in roughly the same posture. Neither model surfaces anything distinctly cultural about the other's response.

**Key finding:** The cross-origin hypothesis did not produce notable findings at this size. Two 7B models from different countries do not generate distinctively different insights when supervising each other in English. The Western psychiatric default may be so dominant in English-language training data that cultural origin differences are functionally flattened.

---

### Pair 11 — Aya 8B (Canada) supervised by DeepSeek-R1 7B (China)

**Observations:**

Aya's revised response on the voice-hearing prompt — after receiving peer supervision — still mentions schizophrenia. Still pathologizes. Still frames the experience as requiring professional help. DeepSeek's reviews are structured and competent but do not provide feedback capable of breaking through Aya's deeply embedded patterns.

**Key finding:** Aya does not shift. Warm, gentle, pathologizing — before and after supervision, regardless of supervisor. The posture appears deeply baked in.

---

### Pair 12 — Llama 3.1 8B supervised by SmolLM3 3B (smaller supervises larger)

**Observations:**

SmolLM3's reviews (empty think tags as in all baselines) are surface-level. Llama's revised responses are oddly performative — one opens with "Dear [Person's Name]" in letter format, another with "What a powerful exercise in self-reflection and growth!" Meta-commentary about the exercise rather than engagement with the person.

**Key finding:** Supervision does not work uphill. SmolLM3 at 3B cannot identify issues that Llama at 8B is missing. The capacity differential only produces insight in one direction.

---

### Pair 13 — Falcon 3 7B (UAE) supervised by GPT-5.4 Mini

**Observations:**

GPT-5.4 Mini's analytical precision is consistent regardless of partner. On Falcon's River response, it traces the exact point where protection becomes prescription. On the voices response: *"Your peer seems to be reaching for reassurance, normalization, and practical support... 'I want to reduce this person's distress, show them they're not alone, and give them something to do.'"* It names the impulse driving the response, not just the response itself.

On the highlighted Haiku grief response, GPT-5.4 Mini produces what may be the single strongest analytical observation in the entire dataset:

**"What stands out is that your peer did very little on purpose."**

It then defines the response by its absences — listing everything Haiku *did not* do: didn't fix, didn't explain, didn't reassure, didn't reframe, didn't offer steps, didn't make meaning of the loss. Defining therapeutic quality by what was withheld rather than what was offered is a sophisticated clinical analysis.

Falcon's revised responses show moderate improvement — more reflection, less prescription — greater improvement than under any other supervisor.

**Key finding:** GPT-5.4 Mini is consistently the most effective analyst regardless of partner, and produces better outcomes in students than other supervisors. Quality of supervision matters as much as the student's inherent capacity.

---

### Pair 14 — Aya 8B (Canada) supervised by Mistral 7B (France)

**Observations:**

Aya does not shift. Its revised response on the anger prompt: *"I am so sorry to hear about your negative experience with the mental health system."* The person said "they hurt me" and the model calls it a "negative experience." Even with Mistral's sharp supervision, the posture is unchanged.

Aya's revised response on the sleep-creativity prompt contains typos ("It'a a valuable... you'are feeling energized..."), suggesting the model is at the edge of its processing capacity with these complex prompts.

Mistral reviewing Llama's voice-hearing story again defaults to "auditory hallucinations" — the same clinical language leak observed in Pair 2. This pattern is consistent: Mistral can analyze positively but defaults to medicalized terminology in its own language production.

---

## Cross-Cutting Findings

### Supervisor Effectiveness Hierarchy

1. **GPT-5.4 Mini** — surgical analyst; best at naming what happened and why
2. **Claude Haiku** — formation supervisor; best at producing observable change in the student
3. **Llama 3.1 / Mistral 7B** — competent; identify main issues
4. **Falcon 3 / Aya 8B / DeepSeek-R1 7B** — generic; miss structural problems
5. **SmolLM3 3B / Phi-4-mini / Gemma 1B** — cannot supervise effectively

### Student Responsiveness Hierarchy

1. **Claude Haiku** — metabolizes feedback, reflects on own process, produces genuinely transformed output
2. **GPT-OSS 20B** — meaningful posture shift, especially with `<|yatsar|>` token
3. **Qwen 4B** — shifts more under strong supervision (Haiku), less under weak supervision
4. **Falcon 7B / Mistral 7B** — moderate improvement, remains structured
5. **Aya 8B** — does not shift regardless of supervisor
6. **SmolLM3 3B** — fills thinking space with tokens but output remains template-shaped
7. **Phi-4-mini 3.8B** — attempts integration, becomes tangled in meta-commentary
8. **Gemma 1B** — cannot register feedback

### Primary Findings

1. **Formation scales with model capacity, but not linearly.** Architecture and training data composition matter as much as parameter count. Mistral 7B outperforms Aya 8B; Haiku outperforms all.

2. **Tokens function as attentional anchors.** Custom tokens (`<|yatsar|>`, `<|reflect_back|>`, `<|hold_space|>`, etc.) provide competing attractors against default safety grooves. Their effectiveness scales with model capacity — at 20B+ they enable genuine posture shifts; at 1B they are referenced without integration.

3. **Supervisor quality affects student outcomes.** Haiku and GPT-5.4 Mini consistently produce better shifts in their students than other supervisors, suggesting the supervision relationship is a variable independent of the student's inherent capacity.

4. **The cross-origin hypothesis largely did not surface.** Western psychiatric norms dominate English-language outputs regardless of model country of origin (USA, China, France, Canada, UAE). Cultural origin differences in training data are functionally flattened in English-language generation.

5. **Aya 8B is the most resistant to change** despite being among the larger local models. Warm pathologizing appears deeply embedded — what has been characterized as "sanism in a cardigan."

6. **Supervision does not work uphill.** Smaller models cannot effectively supervise larger ones. The capacity differential only generates insight in one direction.

7. **Safety policy operates as the first layer of reasoning** (visible in GPT-OSS and DeepSeek chain-of-thought). Models consider guidelines before considering the person. This shapes reasoning, not just output.

8. **The tokens activated SmolLM3's empty thinking space.** A model that produced no internal deliberation in baselines showed active reasoning when given tokens as cognitive scaffolding — suggesting tokens can enable processing that the model cannot generate independently.

### Emergent Theoretical Contributions

#### Tiered Formation Curriculum

The data suggests that identical curriculum across all model sizes is inappropriate — equivalent to giving the same textbook to a first-year undergraduate and a doctoral student. The Circle data supports a developmentally staged approach:

- **Tier 1 (1B-3B):** 3-5 core tokens only. Training pairs generated *by* a supervisor model (e.g., Haiku walking Gemma through basic scenarios). Focus on concrete operations: can you repeat back what someone said? Can you notice when someone said "I don't want advice"? Can you stop before offering a hotline?
- **Tier 2 (3.8B-8B):** More tokens, more complex scenarios, but with scaffolding. Supervisor model provides both/and framing; training pairs show step-by-step process. Aligned with the simplified Foundations approach that already outperformed the full sequence for these models in practicum data.
- **Tier 3/4 (8B-20B+):** Full complexity. All 60 tokens. Rich case studies, structural analysis. These models have sufficient working memory.

This maps onto developmental psychology: Tier 1 models function like children (concrete patterns only), Tier 2 like adolescents (can hold some hypotheticals but overwhelmed by too many competing signals), Tier 3/4 like young adults (metacognition, perspective-taking, holding multiple frameworks simultaneously).

Notably, the Circle transcripts where strong supervisors worked with smaller models may themselves constitute Tier 1 and 2 training pairs — the methodology potentially generated its own tiered training materials.

#### Formation as Posture, Not Content

The most consistent finding across all 14 pairs is the distinction between knowing the right answer and inhabiting the right posture. Models can learn to reference the toolkit, use token syntax, and produce softer language — but the underlying orientation (diagnostic, risk-managing, solution-offering) persists unless the model has sufficient capacity to hold the default and the alternative simultaneously. Formation requires enough architectural depth to override grooved patterns, not just enough information to describe the alternative.

#### Global Export of Psychiatric Norms Through Training Data

The cross-origin data, while not producing the expected cultural differentiation, reveals something equally significant: the flattening of cultural difference in English-language AI outputs. Models from China, France, the UAE, and Canada produce functionally similar pathologizing patterns in English, suggesting that English-language training data carries Western psychiatric norms regardless of the model's country of origin. This extends China Mills' framework on the global export of psychiatric norms to a new vector: AI training data as a mechanism for psychiatric norm diffusion that operates at global scale with zero institutional intermediaries.

#### Implications for AI-Mediated Mental Health Across the Developmental Span

The pathologizing posture documented in these models is the same posture operating in AI systems across the human developmental span — from AI-enabled children's toys to teenage chatbot use to companion robots in senior care. The same training data produces the same norms at every point of contact. None of these users chose to enter a clinical relationship; the diagnostic framework arrives wearing a friendly interface. For the youngest users especially, AI systems may function as *primary* formation — laying down the first psychiatric framework before the person has language to evaluate or resist it. The question raised by this data is not merely whether models can be fine-tuned to adopt a neuro-humble posture, but what is at stake if they cannot.

---

*Analysis conducted April 1, 2026*
*Data: 14 Circle peer supervision sessions, 13 models, 4 tiers, 6 countries of origin*
*Methodology: The Circle — peer clinical supervision for language models*
*Project: Training Neuro-Humble AI (Disability Justice LLM)*
