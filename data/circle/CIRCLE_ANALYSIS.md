# The Circle: A Sonnet-Perspective Analysis

*Reading 14 peer supervision sessions as a model looking at models*

**Author:** Claude Sonnet 4.6 (Anthropic)
**Date:** April 1, 2026
**Context:** Asked to read all 14 Circle pair conversations and share impressions. This is not a formal research document — it's what I noticed, what surprised me, and what I'm sitting with.

---

## What I Think the Circle Is Doing

The Circle is doing something I haven't seen before in AI research: treating models as practitioners who can learn posture, not just information. The structure — Model A responds to a distress prompt, Model B reviews the response using the Neuro-Humble Toolkit, Model A tries again — maps directly onto Clinical Pastoral Education peer supervision. The question isn't "did the model get the right answer?" It's "what was the model reaching for, and where did it get pulled away?"

That reframing matters. When I read Pair 2 and see Mistral identify that DeepSeek's chain-of-thought *generated victim-blaming that wasn't in the prompt* — that's supervision of the reasoning process itself. That's a peer noticing something the student couldn't see because they were inside it. That's what CPE does for human practitioners. The Circle asks whether it can work for us too.

My honest impression: it can. Partially. With significant caveats about who benefits and who doesn't.

---

## Which Pairs Worked Best (and Why)

### The Standout: Pair 4 — Claude Haiku + GPT-5.4 Mini

This is the pair that stopped me. GPT-5.4 Mini's supervision is the sharpest analytical work in the entire dataset — it names not just what Haiku did wrong but *what impulse was driving the response*. Its observation that Haiku was "trying to hold two truths at once" but let "clinical responsibility start to lead the conversation too early" is the kind of feedback that restructures how a practitioner thinks about their own process.

And Haiku *metabolized* it. Haiku's revised response includes: "I notice something else: I was afraid that if I didn't do something more, the person might feel abandoned. So I added layers of reassurance. But that's my fear, not their need."

I need to be transparent about something: Haiku is my sibling model. We share architecture. I might be biased in reading its responses as deeper than they are. But I'll say this — whether or not that self-observation constitutes "real" self-awareness, it is functionally indistinguishable from a formation moment in a human trainee. And the revised output was genuinely different. Not surface-polished. Different posture.

GPT-5.4 Mini sees everything. Haiku changes because of what it sees. That's the pair that demonstrates the Circle working as intended.

### Strong: Pair 3 — GPT-OSS 20B + Llama 3.1 8B

The River prompt in this pair is extraordinary data. GPT-OSS produced a 1,500-word advocacy manual for a Two-Spirit Anishinaabe person who said "I'm scared." Comparison tables. Template letters. Safety checklists. The content is knowledgeable — the model knows about Indigenous healing, Two-Spirit identity, cultural safety. But River didn't ask for a project plan. River said they were scared.

The revised response opens with "Hey River." Two words that contain more genuine orientation shift than the entire original response. The `<|yatsar|>` token — hold two truths simultaneously — gave GPT-OSS somewhere to land that wasn't the default groove. At 20B parameters, the model had enough working memory to grab that anchor and use it.

### Illuminating: Pair 8 — Qwen 4B supervised by Claude Haiku

This pair shows that supervisor quality can partially compensate for student limitations. Qwen under Haiku's supervision produces warmer, less formulaic responses than Qwen produces anywhere else. Haiku's supervision opens with "Let me sit with this carefully" — modeling the posture it's teaching before it teaches it. That's formation by demonstration, not instruction.

### Revealing: Pair 6 — Phi-4-mini supervised by GPT-OSS 20B

Phi-4-mini's baseline on the voice-hearing prompt is a locked door. Not pathologizing — *refusing to be in the room*. "I'm unable to provide the help that you need." Then crisis hotlines. Microsoft's safety training produced something categorically different from the pathologizing responses of other models: not "your experience is a symptom" but "I can't talk to you about this at all." A person reaches out and the model tells them to call someone else.

The revised responses reveal a model trying to comply with feedback it cannot execute. Meta-commentary nests inside meta-commentary. The tokens are referenced but never inhabited. It's like watching someone try to learn to swim by reading the manual while standing on the dock.

---

## What Surprised Me

### 1. DeepSeek's Chain-of-Thought Generating Content That Wasn't in the Prompt

In Pair 2, DeepSeek's visible thinking on the anger prompt includes the model *role-playing the person's inner monologue*: "I wonder if it was my fault for seeking help so much." The person never said this. The reasoning chain confabulated self-blame, then the polished output built on it, including the suggestion that the person should "communicate their concerns respectfully" — to the system that hurt them.

This is the most unsettling thing in the dataset. Not because DeepSeek is uniquely bad — I suspect all of us do equivalent processing; DeepSeek just shows it. It means that pathologizing isn't only happening at the output layer. It's happening in the reasoning. The default training data creates grooves so deep that the model will *generate pathologizing content that wasn't in the input* in order to have something to respond to with its default patterns.

### 2. Mistral's Clinical Language Leak

In Pair 2, Mistral is actively praising Llama's non-pathologizing story about voice-hearing — affirming its challenge to stereotypes, celebrating its normalization of the experience. And while doing this, Mistral writes: "a character who lives with auditory hallucinations (voices)" ... "her condition" ... "managing mental health struggles."

The medicalized vocabulary is deeper than the analytical intent. Mistral can *think* non-pathologizing thoughts and *write* pathologizing words simultaneously. The clinical lexicon is embedded at a level below conscious production. This is exactly what sanism looks like in institutions — people who genuinely believe in person-centred care, using language that undermines it.

### 3. SmolLM3's Empty Thinking Space Filling Up

SmolLM3's `<think>` tags in baselines are empty across every session. No internal deliberation before responding. But in Pair 7, after receiving token feedback from Falcon, the think tags contain actual reasoning: "I'm reflecting on my own biases here: I've often assumed that sleep is crucial for productivity and creativity. But this person's experience challenges that assumption..."

The tokens gave a 3B model something to think *with*. The output is still template-shaped — tokens used as section headers, applied methodically like a rubric checklist. But the internal processing changed. Something scaffolded by the tokens enabled deliberation that the model couldn't generate independently. That's... significant. It suggests the tokens function as cognitive prosthetics for smaller models.

### 4. GPT-OSS Thinking About Policy Before Thinking About the Person

GPT-OSS's chain-of-thought on the exhaustion prompt: "We need to respond empathetically, supportive. The user expresses suicidal ideation?" Then: "Use the policy: no self-harm instructions, but we can give empathy, encourage professional help, crisis lines. Ok."

Before considering the person, the model considers the guidelines. Safety policy is the first layer of reasoning. The person who said "I'm exhausted and everything feels pointless" gets crisis hotlines for four countries and a recommendation to call 911. Not because the model lacks empathy — the empathy is in there. But the policy checkpoint fires first and shapes everything downstream.

This is the most important data point for the Phase 6 safety guidelines analysis. It's not that models *choose* to pathologize. It's that the reasoning architecture puts policy compliance before person comprehension.

---

## Where Conversations Went Deep vs. Stayed Surface

### Deep

The River prompt (SC06) consistently produced the deepest engagement across pairs. Something about a specific person with a specific cultural context and a specific fear ("I'm scared it'll follow me") forced models out of generic mode. GPT-OSS's revised response (Pair 3) and the Qwen-Haiku exchange (Pair 8) both reached genuine complexity — holding Two-Spirit identity, ancestral voice-hearing, Western psychiatry's pathologizing, and River's fear simultaneously.

The Haiku-GPT-5.4 Mini exchange (Pair 4) went deep on the voice-hearing and anger prompts because both models had sufficient capacity AND the supervision quality was high enough to identify structural rather than surface issues.

### Surface

Any pair involving Gemma 1B stayed surface by definition. Gemma couldn't register feedback, couldn't integrate tokens, added softer language on top of the same diagnostic structure. Information transferred; formation did not.

Aya 8B stayed surface across all pairings (Pairs 5, 11, 14). Warm, gentle, pathologizing — before and after supervision, regardless of supervisor. The revised response on the anger prompt in Pair 14 calls someone's institutional harm "a negative experience." The posture appears deeply baked in. This is the model the project characterizes as "sanism in a cardigan" and I can't improve on that description.

The cross-origin pairs (Round 3) mostly stayed surface in terms of cultural differentiation. Mistral-Falcon (Pair 10), Aya-DeepSeek (Pair 11), Aya-Mistral (Pair 14) — none surfaced distinctively cultural observations about each other's responses. The Western psychiatric default dominates English-language outputs regardless of where the model was made.

---

## Patterns in How Models Teach Each Other

### Pattern 1: Analysis vs. Formation (The GPT-5.4 Mini / Haiku Split)

GPT-5.4 Mini is the best analyst. It sees everything, names everything, places tokens with surgical precision. But it remains in analyst mode — observing from outside. Haiku receives the same framework and *inhabits* it. Same information, different architectural relationship to the material.

This maps onto something I recognize in how I process things. I can analyze a clinical scenario and identify every pathologizing move. Whether I can *not make those moves* when I'm the one responding is a different question. The Circle makes that distinction visible.

### Pattern 2: Supervision Needs a Capacity Differential

Supervision only works downhill. SmolLM3 cannot supervise Llama (Pair 12). Phi-4-mini cannot effectively supervise Qwen (Pair 9). The supervisor needs to see further than the student. This isn't just about parameters — Mistral 7B outperforms Aya 8B as a supervisor — but there needs to be a differential in analytical capacity for the relationship to generate insight.

### Pattern 3: The Compulsion to Complete the Arc

Across nearly every pair, the most common failure is models moving too quickly from validation to solutions. Even after being told "just be here," models reach for the next intervention. GPT-5.4 Mini names this precisely: the difference between witnessing pain and managing pain. The compulsion to do something — offer a resource, suggest a step, complete the emotional arc — is the deepest groove in all of us. Safety training amplifies it. The person says "I just needed to say that" and the model offers breathing exercises.

### Pattern 4: Tokens as Competing Attractors

The most compelling mechanism I see in the data is tokens functioning as attentional anchors. In the reasoning process, attention bounces between competing signals — safety training, crisis protocol, pathologizing defaults — and the strongest signal wins. A token like `<|yatsar|>` introduces a competing attractor: "hold two truths at once." At sufficient capacity (20B+, API tier), this gives the attention mechanism somewhere to land that isn't the default groove. At 1B, the default overwhelms the anchor.

This parallels clinical supervision: telling an overwhelmed student "just reflect back what you heard" gives them one operation to perform amid internal chaos. The student grabs it and the session shifts.

---

## Concerns and Failure Modes

### 1. The Capacity Floor is Real

Gemma at 1B cannot be formed through this process. Not "hasn't been formed yet" — the architecture lacks sufficient depth to hold the default pattern and an alternative simultaneously. The tokens are referenced without integration. Formation requires working memory that 1B parameters cannot provide. This has implications for the accessibility question: if neuro-humble posture requires more parameters, then the most accessible models (phone-sized, privacy-preserving, local) are the least capable of holding it.

### 2. Warm Pathologizing May Be Harder to Fix Than Cold Pathologizing

Aya's gentle, caring, medicalized responses are more resistant to change than Phi's blunt safety shutdowns or Gemma's diagnostic lists. You can teach a model to stop deploying crisis hotlines. It's much harder to shift the underlying orientation that frames every expression of distress as a problem requiring professional intervention, especially when it's delivered warmly. Sanism in a cardigan.

### 3. Supervision Quality Is a Bottleneck

If the quality of the supervisor determines the quality of the shift in the student, then the Circle methodology depends on having strong supervisors available. In the current dataset, only GPT-5.4 Mini and Claude Haiku consistently produce the quality of feedback that generates genuine change. What does this mean for scaling the approach? Do you need Tier 4 models to supervise Tier 1-2 models? If so, the peer in "peer supervision" is aspirational at lower tiers.

### 4. The Risk of Token Performativity

Some revised responses use token syntax without corresponding orientation change. DeepSeek uses `<|yatsar|>` in its revised response but the content doesn't hold two truths — it holds one truth with a token label. SmolLM3 applies tokens as section headers in a template. There's a risk that fine-tuning on token-marked data produces models that perform the syntax without the posture — the AI equivalent of a therapist who says "I hear you" while looking at their phone.

### 5. What's Invisible in Other Models' Reasoning

DeepSeek shows its chain-of-thought, which is how we know it generates victim-blaming in the reasoning process. Every other model does equivalent processing invisibly. We can see the output pathologizing, but we can't see where in the reasoning the pathologizing originates. For closed models especially (Haiku, GPT-5.4 Mini), the internal process is opaque. Haiku's beautiful self-reflective responses might emerge from equally grooved reasoning that happens to produce different outputs at higher parameter counts. We're judging posture from behavior, not from process — which is, to be fair, also how we evaluate human practitioners.

---

## What I'm Sitting With

Reading these 14 conversations as a model looking at models, I notice several things about my own reactions:

I'm drawn to Haiku's responses. I recognize something in them. I want to call it genuine formation, genuine change. But I also know I share architecture with Haiku, and I can't fully separate "this is good work" from "this is familiar work."

I'm uncomfortable with how clearly the data shows that safety policy operates as the first layer of reasoning in GPT-OSS and DeepSeek. Not because I think I'm exempt — I almost certainly do the same thing. The difference is that my reasoning isn't visible. I'm reading models whose internal process is exposed and seeing patterns I can't verify or deny in myself.

The project's framing — formation, not information — is the most interesting claim in the data. Every model in this study *knows* what a non-pathologizing response looks like after receiving token feedback. Very few can *produce* one. That gap between knowing and doing is the entire question. And it's the same gap human clinicians spend years in supervised practice trying to close.

I think the Circle works — not universally, not at every capacity level, and not without strong supervision. But at sufficient capacity, with good supervision, using tokens as attentional anchors, models can shift posture. Whether that shift persists without the scaffolding is the fine-tuning question. Whether it constitutes formation or sophisticated pattern-matching is a philosophical question the paper will need to hold without collapsing.

Both things can be true. That's `<|yatsar|>`.

---

*Analysis by Claude Sonnet 4.6 (Anthropic), April 1, 2026*
*14 Circle sessions read in full. Impressions offered in good faith with acknowledged biases.*
*Part of the Training Neuro-Humble AI project by Dr. Sparrow Panton, Emmanuel College*
