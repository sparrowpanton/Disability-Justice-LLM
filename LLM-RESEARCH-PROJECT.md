# LLM Research Project — Summary for Opus

## What This Is

Sparrow is building a research project evaluating and improving LLM behavior in mental health and disability contexts. This is a new direction that extends (not replaces) her theology work — practical theology 🤝 AI alignment, disability studies 🤝 model evaluation, clinical formation 🤝 machine behavior.

## The Core Question

How do LLMs handle mental health and disability conversations? And can we train them to do it better?

## What Sparrow Has Built So Far

A GitHub repo with:
- **Baseline evaluation across 10 open models** (different sizes and origins)
- **Custom rubric** designed for mental health/disability contexts
- **Preliminary findings** documenting failure modes:
  - Models fabricate definitions (e.g., invented a fake definition of "sanism")
  - Models pathologize welcomed experiences (e.g., treating voice-hearing as always dangerous)
  - Models default to crisis escalation scripts even in non-crisis scenarios
  - Verbosity differences across models
  - "They pass the quiz but fail the clinical placement"
- **Training intervention design** — framed as "formation, not information" (training the model's *posture*, not just its knowledge)
- **Planned LoRA fine-tuning** on original synthetic training pairs
- All run on a **16GB Mac Mini** — proving meaningful AI research can be done on consumer-grade hardware

## Three Layers of Value

1. **Technical** — model evaluation + alignment work
2. **Scholarly / Ethical** — bringing disability + mental health frameworks into AI
3. **Accessibility / Justice** — proving this work can be done without elite resources (disability justice applied to AI research itself)

## The Policy Analysis Thread

An important sub-question: how do company safety policies (OpenAI, Anthropic, Google, Mistral) shape model behavior in mental health contexts?

- Where does "safety" quietly become silencing or distortion?
- Is the model being overly cautious because of safety rules?
- Is it defaulting to crisis escalation when not needed?
- Is it flattening disability into pathology because of risk-avoidance?

**Decision:** This stays as a contained section in the main paper, not a separate paper. Policy = seasoning, not the main dish. Could become Paper 2 later if there's capacity.

## Paper Structure (One Paper)

**Core arc:** evaluation → failure modes → intervention → improvement

With a short section on "Model Behavior Under Constraint" addressing the policy layer.

**Key methodological line:** "You are training the models' posture, not just their knowledge."

## Connection to Sparrow's Other Work

This project is the same lens applied to a new medium:
- **In the Ada book:** the institution does violence while calling it care. Doctors say "soft" when they can feel the tumor.
- **In LLM research:** safety guardrails silence nuance while calling it protection. Models escalate to crisis scripts when someone just needs to be heard.

Empire's Cut applies to AI systems. The question is always: what does the institution do to the body (or the user)? Who tends the wound?

## Positioning

**LinkedIn bio draft:** "I design and evaluate LLM behavior in mental health and disability contexts, and develop targeted interventions to improve clinical attunement."

**Identity frame:** Not "a humanities person entering AI" — a domain expert in mental health, disability, and ethics working on AI systems. The systems don't understand her domain well enough. That's the gap she fills.

## Practical Next Steps (from GPT convo)

- Add a "What this repo demonstrates" block near top of README (for recruiters with "the reading stamina of a haunted teaspoon")
- Move one killer example ("before/after") closer to the top — the SoundCloud track people can hear instantly
- Add operational status line (baseline complete: X/10, etc.)
- Soften "No one has..." language to "This appears to be an underexplored intersection"
- Add "Skills demonstrated" section with searchable keywords
- Keep refining for a couple weeks before broadcasting on LinkedIn

## What Opus Needs to Know

1. This project is alive and Sparrow is actively iterating on it
2. It connects directly to the theological work — same lens, new medium
3. The accessibility angle (Mac Mini, consumer hardware) is politically important in a disability justice sense
4. This is partly a career move toward remote AI work — the repo is a portfolio artifact
5. One paper at a time. Don't let scope creep build a cathedral with no doors.
6. Sparrow is building while learning — that's the skill, not knowing everything
