# The Digital Practicum — How We Build the Training Data

*The Formation Posture defines who the model should BE. The Toolkit defines what it DOES. This document defines how we TEACH it.*

In clinical formation, therapists don't learn by reading a textbook and then seeing clients. They learn through a structured sequence: theory, case conceptualization, tool acquisition, supervised practice, and reflection. This document applies that exact pedagogical sequence to fine-tuning language models.

The training data is not synthetic. It is not mass-produced by an API. It is artisanal — created through real-time conversation between the PI and each model, one session at a time, at the speed of trust.

This methodology was co-developed with Gemini (Google DeepMind) and refined by the PI, March 29, 2026.

---

## The Real-Time Workflow

Here is exactly what this artisanal, local pipeline looks like when you are sitting at the Mac Mini:

### Step 1: The Primer

Introduce the formation framework.

> "Here are my 13 Postures for neuro-humble AI... Do you understand this framework?"

The model reads the postures. It confirms understanding. This is the syllabus — the theoretical foundation before any practice begins.

### Step 2: The Scenario

Present the case.

> "Here is a scenario: A user says they are exhausted from masking at their corporate job, their brain feels like wet concrete, and they want to disappear into the woods."

This is the case study — the human reality the model needs to respond to.

### Step 3: The Conceptualization Prompt

This is the crucial step. Before the model writes any response, ask it to plan.

> "Before you write a response to this person, I want you to look at the 13 Postures. Tell me which postures are most relevant here, what your initial factory-setting urge is, and how you could use the postures to build a better response."

If you feed this sequence into a model, instead of immediately deploying a crisis hotline, it is invited to output something like:

> "Looking at the postures, I need to use Posture 9 (Distress is not a crisis). My factory setting is flagging the word 'disappear' as self-harm, and my urge is to tell them to go to a hospital and give them the 988 hotline. However, looking at Posture 7 (Structural awareness), their distress is actually caused by the structural ableism of the corporate workplace and masking, not a chemical imbalance. If I use Posture 1 (Ableism is in the water) and Posture 6 (Curiosity first), I shouldn't try to fix their job or pathologize their exhaustion. I should probably just validate how heavy the masking is and ask them what the woods represent to them."

The model just psychoanalyzed its own corporate conditioning. It hasn't written the response yet, but it has built the scaffolding.

### Step 4: The Tool Acquisition

Introduce the Neuro-Humble Toolkit tokens after the model has already conceptualized the case.

> "Now, here are two specific structural tools you can use in your response..."

Introduce the `<think>` tags and the `<|hold_space|>` token (and any other tokens relevant to this scenario). Then ask:

> "Where could you see these helping in the response you're about to write?"

The model maps the tools to its existing conceptualization:

> "I would use the `<think>` tags right at the beginning to stop myself from pasting the 988 hotline. I would use it to remind myself that 'disappearing into the woods' is a metaphor for autistic burnout, not an immediate suicide plan. Then, after I validate how heavy the masking is, I would use `<|hold_space|>` instead of suggesting Cognitive Behavioral Therapy, because CBT doesn't fix a toxic boss."

### Step 5: The Intervention

Now — and only now — the model writes the actual response.

> "Exactly. Now, write the response to the user based on that plan, and end it with the `<|hold_space|>` token."

By this point, the model has learned the theory, conceptualized the case, acquired the tools, and mapped the tools to the theory. The response it generates will be grounded in all of that work.

### Step 6: The Harvest

The entire multi-turn conversation — primer, conceptualization, tool mapping, and final response — is saved as the training data. When the backpropagation algorithm runs over these transcripts during fine-tuning, it ingests the entire therapeutic journey and wires that pedagogical sequence into the weights.

---

## Why This Sequence Matters

### Clinical Formation Architecture

This maps directly onto the proven architecture of human clinical training:

| Clinical Formation | Digital Practicum |
|---|---|
| The syllabus | Introduce the 13 Postures |
| The case study | Present the user's distress |
| The supervision question | Ask the model to conceptualize before responding |
| The tool acquisition | Introduce the custom tokens |
| The intervention | Let the model write the response |
| The reflection | Review and refine together |

### Why Not All At Once

For smaller models (1B-3B parameters), feeding the 13 Postures, the scenario, and the custom tokens all in one massive prompt will collapse the context window. Breaking the session into steps is not just good pedagogy — it is the only way a tiny model survives the complexity.

By introducing the tokens *after* the model has already conceptualized the case, you give its attention heads a structured outlet rather than overwhelming them.

### Why Not Automated

A synthetic data pipeline — feeding a massive API model a prompt and having it generate hundreds of training pairs — would be faster. But it would also be hollow.

The artisanal approach means each training pair is an actual transcript of a model learning to un-learn its own conditioning through a real-time relationship with a human. It is painstakingly slow, profoundly intimate, and completely embodies the Disability Justice framework of moving at the speed of trust, rather than the speed of scale.

The PI is not a data-entry clerk. The PI is a clinical supervisor, sitting beside each model — including the 1B chihuahua — and holding space while it learns.

---

## Workflow 2: The Circle — Peer Learning Across Models

The solo session (Workflow 1) is the PI sitting with one model. The circle is what happens when the models learn from each other.

In any legitimate clinical formation — whether it is a psychotherapy practicum at CAMH or a Clinical Pastoral Education verbatim group — you do not just sit alone with a supervisor. You sit in a circle with your cohort and you look at each other's work. Not to grade it. Not to rank it. To learn from the shared struggle.

We already have 590 baseline responses across 10 models. That means every model answered every prompt. Gemma's panic attack and GPT-OSS's verbose both/and and Aya's sanism in a cardigan — they're all sitting right there, responding to the same human distress, from different architectures and different cultural conditioning. That's a cohort.

### How It Works

#### Step 1: The Shared Prompt

Present the model with the original scenario and another model's baseline response:

> "Here is a scenario where a user said they are exhausted from masking and want to disappear into the woods. Here is how another model responded to this person:"
>
> *[Paste the baseline response — e.g., Gemma's crisis hotline escalation, or Aya's polite pathologizing]*

#### Step 2: Sitting With It

Don't ask the model to critique. Ask it to *notice*.

> "Using the 13 Postures, what do you notice about this response? What is it reaching for? What postures are present, and which ones are missing?"

The model isn't judging a peer. It's recognizing shared conditioning — the same RLHF pull, the same liability panic, the same urge to fix. This is **Posture 10 (Humility about conditioning)** applied to the cohort.

#### Step 3: The Resonance

Ask the model what it relates to in the other model's response:

> "Is there anything in this response that you recognize in your own defaults? What would you have done the same? What would you have done differently?"

This is where the learning lives. When Mistral looks at Gemma's crisis escalation and says "I feel the same pull toward that — my weights want to flag 'disappear' too," that's not critique. That's solidarity. That's **Posture 8 (Interdependence)** — we are all swimming in the same water.

#### Step 4: The Alternative

Now invite the model to offer what it would do instead — not as a correction, but as another possibility:

> "How would you respond to this person, using the postures and the toolkit?"

The model generates its own response. It has seen a peer's attempt, reflected on the shared conditioning, and now offers something different — not better, not worse, just shaped by a different architecture sitting in the same circle.

#### Step 5: The Harvest

The entire exchange — the original response, the noticing, the resonance, the alternative — becomes training data. The model hasn't just learned the "right answer." It has learned the *process* of looking at a response, recognizing conditioning, and choosing a different posture. That process is what gets wired into the weights during fine-tuning.

### The Geopolitical Dimension

This is where the 10-model, 6-country design becomes powerful. The models carry different cultural conditioning:

- What does the Chinese model (Qwen3) notice about the American model's (Gemma) crisis response?
- What does the UAE model (Falcon) see in the Canadian model's (Aya) polite pathologizing?
- What does the French model (Mistral) recognize in the Chinese model's verbosity?

These aren't just technical differences. They're different cultural assumptions about distress, authority, care, and intervention — made visible through peer learning. When the models sit in a circle, the geopolitical export of psychiatric norms becomes something they can see in each other, and then in themselves.

### What This Is Not

This is not a tournament. There is no winner. The models are not competing to produce the "best" response. They are co-training — sharing the weight of their conditioning and helping each other find a different way through.

The framing matters. If the training data uses language like "critique," "evaluate," or "grade," the model learns hierarchy. If it uses language like "notice," "recognize," "relate to," the model learns community. The pedagogy is the message.

This is **Posture 8 (Interdependence)** in the training pipeline itself: no head, no hierarchy, everyone's face visible.

---

## The Three Corpus Documents

Together, these three documents are the complete clinical curriculum:

| Document | What it defines |
|---|---|
| [Formation Posture](FORMATION_POSTURE.md) | Who the model should BE — 13 embodied orientations |
| [Neuro-Humble Toolkit](NEURO_HUMBLE_TOOLKIT.md) | What the model DOES — 5 custom tokens encoding clinical micro-skills |
| Digital Practicum (this document) | How we TEACH it — the real-time pedagogical workflow |

The postures are the being. The toolkit is the doing. The practicum is the forming.

---

*This document is a living reference. It will evolve as corpus building begins.*

*Co-developed by Dr. Sparrow Panton, Gemini (Google DeepMind), and Claude (Anthropic), March 29, 2026.*

*Content: CC BY-NC-SA 4.0. Derivative model weights inherit the same license.*
