# Voices from the Field: A Working Literature Review

### Situating the Disability Justice LLM Project Within Existing Scholarship

This is a living document cataloguing the research conversations this project is joining. It is organized into three broad areas — not because scholarship is ever this tidy, but because these groupings help make visible a gap that this project occupies.

We are not the first to notice that AI mental health tools have problems. We are not the first to apply Disability Justice to technology. We are not the first to say that psychiatric institutions cause harm. What is unique about our project is we are bringing all three of these conversations together empirically — to *measure* the pathologizing defaults in language models and then *train models to do something different*, using a formation pedagogy rooted in Mad Studies, Disability Justice, and neurodiversity-affirming clinical practice.

---

## 1. The Establishment: AI in Mental Health

These are the papers that document what exists — the landscape of AI mental health tools, their methods, and their outcomes. This work is valuable for establishing baselines, but it largely operates within the medical model, treating diagnostic frameworks as given rather than contested.

### Shatte, A. B. R., Hutchinson, D. M., & Teague, S. J. (2019). Machine learning in mental health: A scoping review of methods and applications. *Psychological Medicine, 49*(9), 1426–1448.

A comprehensive scoping review of ML applications in mental health as of 2019. Useful for understanding the field's trajectory: diagnosis prediction, treatment outcome forecasting, natural language processing for mental health screening. The review maps the technical landscape without questioning whether the diagnostic categories being predicted are themselves the problem. **Relevance to our project:** Establishes the "before" picture. This is what the field looks like when nobody asks whether the categories are right.

### Fitzpatrick, K. K., Darcy, A., & Vierhile, M. (2017). Delivering cognitive behavior therapy to young adults with symptoms of depression via a fully automated conversational agent (Woebot). *JMIR Mental Health, 4*(2), e19.

The original Woebot paper — one of the earliest fully automated AI therapy tools. Reports positive outcomes using CBT-based chatbot interventions for depression in young adults. Important as a landmark in the field, but the framing is entirely within the medical model: depression is the problem, CBT is the solution, automation is the delivery mechanism. No engagement with whether the diagnostic framework itself might be part of the distress. **Relevance to our project:** The establishment baseline for what "AI therapy" looks like when built uncritically within psychiatric norms.

### Fiske, A., Henningsen, P., & Buyx, A. (2019). Your robot therapist will see you now: Ethical implications of embodied artificial intelligence in psychiatry, psychology, and psychotherapy. *Journal of Medical Internet Research, 21*(5), e13216.

An early and influential ethics review raising concerns about AI in therapeutic contexts — questions about the therapeutic relationship, informed consent, privacy, and the limits of machine empathy. Gets closer to our concerns than most establishment papers, but still frames the question as "how do we deploy AI ethically within existing mental health frameworks" rather than "what if the frameworks are the problem." **Relevance to our project:** Shows that even within the mainstream, people were worried — they just weren't worried about the right thing.

### Sedlakova, J., & Trachsel, M. (2023). Conversational artificial intelligence in psychotherapy: A new therapeutic tool or agent? *American Journal of Bioethics, 23*(5), 4–13.

Asks a genuinely important question: is conversational AI a *tool* that therapists use, or an *agent* that does therapy? This maps directly onto our formation vs. information framing — if AI is an agent, then its *posture* matters, not just its knowledge. The paper raises the question but doesn't go where we go: it doesn't ask what happens when the agent's posture is inherently pathologizing. **Relevance to our project:** Provides the philosophical bridge between "AI as tool" and our argument that if AI is functioning as an agent, it needs formation, not just information.

### Albert, B., et al. (Eds.). (2021). *Bridging Human Intelligence and Artificial Intelligence.* Springer.

Multi-author volume exploring intersections of human and artificial intelligence. The chapter on "Supporting Social and Emotional Well-Being with Artificial Intelligence" is particularly relevant — it uses the word "sane" uncritically and frames emotional wellbeing through a neurotypical lens. **Relevance to our project:** An example of how even well-intentioned interdisciplinary work reproduces sanism when disability justice frameworks are absent.

---

## 2. The Diagnostic Gaze: Critical Disability Perspectives on AI

These are the scholars asking harder questions — not "how do we make AI mental health tools less biased" but "what assumptions are baked into these systems at the level of design, data, and discourse?"

### Keyes, O. (2020). Automating autism: Disability, discourse, and artificial intelligence. *Journal of Sociotechnical Critique, 1*(1), 8.

A landmark paper in critical disability studies of AI. Keyes argues that conventional AI ethics frameworks are "actively invisible" to discursive harms — the way AI *talks about* and *categorizes* disabled people is itself the violence, not just algorithmic bias. Demonstrates how autism detection AI reproduces a specific medical model of autism that erases autistic self-understanding and agency. **Relevance to our project:** Keyes is doing the critical theory that our project measures empirically. They show *that* the harm exists at the level of discourse; we show *how much* of it exists across eight models, fifty-nine prompts, and seven hundred markers. Essential citation.

### El Morr, C., El-Lahib, Y., & da Silveira Gorman, R. (Eds.). (2025). *Beyond Tech Fixes: AI and Disability Justice.* Springer.

Possibly the most directly relevant book to our project. Argues that technological "fixes" for disability are a form of technoableism — the assumption that technology will "solve" disability rather than addressing structural oppression. Calls for Disability Justice frameworks in AI development, data sovereignty for disabled communities, and participatory design that centers disabled people as experts.

Key chapters include:

- **El-Lahib, Y., da Silveira Gorman, R., & El Morr, C. (2025).** "AI and Disability Justice: Why Beyond Tech Fixes?" — The introductory framework rejecting technoableist approaches to disability and AI.

- **Fernandes, J., Rahman, T., & da Silveira Gorman, R. (2025).** "A Framework for Social Justice-Oriented Practices for Accessible and Inclusive AI" — Lays out concrete principles for justice-oriented AI, including data sovereignty and participatory design.

**Relevance to our project:** They're theorizing what we're building. Their Disability Justice framework for AI is the theoretical house; our fine-tuned models are an empirical proof of concept that lives inside it. This book validates the *approach* while our project provides the *evidence*.

### Timmons, A. C., et al. (2023). A call to action on assessing and mitigating bias in artificial intelligence applications for mental health. *Perspectives on Psychological Science, 18*(5), 1062–1078.

A mainstream call to action reviewing health equity implications of AI in mental health. Important for establishing that even within psychology's establishment, there is growing concern about bias. However, the paper stays within the medical model — it wants to *fix bias* within existing diagnostic frameworks rather than questioning whether those frameworks are the source of the harm. **Relevance to our project:** Useful as a "even the mainstream is worried" citation, but demonstrates the limits of reform-from-within approaches. Our project goes further: we don't just identify bias, we name the *framework* as the problem and train an alternative.

### Saeidnia, H. R., et al. (2024). Ethical considerations in artificial intelligence interventions for mental health and well-being: Ensuring responsible implementation. *Social Sciences & Humanities Open.*

Reviews ethical dimensions of AI mental health interventions including privacy, informed consent, and the digital divide. Approaches the question from a responsible implementation lens. **Relevance to our project:** Part of the growing chorus saying "we need ethical guardrails" — our project asks what those guardrails look like when designed *by and for* disabled and Mad communities rather than imposed from above.

---

## 3. The Longer Lineage: Mad Studies, Anti-Psychiatry, and Disability Justice

These are the intellectual foundations. The critique of institutional psychiatry did not begin with AI — it began with people locked inside the institutions, and with practitioners who chose to listen to them.

### Laing, R. D. (1960). *The Divided Self.* Tavistock.

### Laing, R. D. (1967). *The Politics of Experience.* Penguin.

Laing argued that the clinical gaze itself could be pathogenic — that what people in extreme states needed was not containment but community, not diagnosis but presence. His work is foundational to the anti-psychiatry movement and remains relevant because the pathologizing gaze he described in 1960 is now automated at scale. **Relevance to our project:** Laing's critique is the intellectual ancestor of our empirical findings. When we measure 623 pathologizing markers across Qwen3's baseline responses, we are documenting exactly what Laing warned about — the clinical gaze, now running on GPUs.

### LeFrançois, B. A., Menzies, R., & Reaume, G. (Eds.). (2013). *Mad Matters: A Critical Reader in Canadian Mad Studies.* Canadian Scholars' Press.

The foundational Canadian Mad Studies reader. Establishes Mad Studies as an academic and activist discipline that centers the knowledge and experience of people who have been psychiatrized. Argues for Mad identity as a site of political resistance, not a condition to be treated. **Relevance to our project:** Provides the theoretical framework for why we train models on Mad Studies texts rather than clinical psychology texts — because the knowledge we need comes from the people who have been harmed by the institution, not from the institution itself.

### Sins Invalid. (2019). *Skin, Tooth, and Bone: The Basis of Movement is Our People.* 2nd ed.

The foundational Disability Justice primer from Sins Invalid, a disability justice performance project. Establishes the ten principles of Disability Justice, centering intersectionality, interdependence, and the leadership of those most impacted. **Relevance to our project:** The methodological and ethical backbone. "Nothing about us without us" as practiced in this project — research designed and led by a disabled, neurodivergent, Mad-identified PI — is Disability Justice methodology in action.

### Mills, C. (2014). *Decolonizing Global Mental Health: The Psychiatrization of the Majority World.* Routledge.

Critiques the global export of Western psychiatric norms to the Global South, arguing that "global mental health" is a form of colonialism that pathologizes culturally specific expressions of distress. **Relevance to our project:** Our geopolitical analysis dimension — comparing models from the USA, China, France, Canada, and UAE — directly extends Mills' critique to AI systems. If Western psychiatric norms are exported through human institutions, they are now also exported through language models trained on Western data.

### Graichen, R. (2025). Neurodiversity-affirming supervision. In M. Marneau (Ed.), *On Being an Autistic Therapist.* PCCS Books.

Introduces the concept of "neuro-humility" within Neurodiversity-Affirming Supervision (NDASV), describing a clinical posture that "explores beyond a neurotypical perspective" using "an open framework that draws on multiple, diverse ways of explaining/interpreting client behaviours and experiences, as opposed to limiting us to a single neurotypical and pathologising model." **Relevance to our project:** The direct source of our "neuro-humble" evaluation framework. Graichen describes how to train *therapists* to have this posture; we extend her framework to training *language models*. The parallel is methodologically foundational.

---

## 4. The Surveillance Paradigm: When "Care" Becomes Control

A smaller but critical thread in the literature — work that documents what happens when mental health AI crosses from care into surveillance, monitoring, and control.

### Yee, A. Z. H., et al. (2024). Biosensor-enhanced AI for mental health monitoring. *Frontiers in Psychiatry.*

Proposes integrating biosensors with AI for continuous mental health monitoring. Frames constant physiological surveillance as "early intervention." **Relevance to our project:** This is the extreme endpoint of the pathologizing paradigm — not just AI that *responds* to distress with diagnostic language, but AI that *monitors bodies* for signs of deviance. Our project's critique of the diagnostic gaze extends naturally to this surveillance trajectory.

---

## The Gap We Occupy

Three conversations are happening:

**The establishment** is building AI mental health tools and beginning to worry about bias — but stays within the medical model, seeking to fix the tools rather than questioning the frameworks.

**Critical disability scholars** are theorizing what's wrong — showing how AI reproduces ableism, sanism, and the diagnostic gaze — but largely without empirical measurement of LLM behavior or proposed alternatives.

**Mad Studies and Disability Justice** offer a different vision of what care could look like — but have not yet been applied to AI training methodology.

This project sits at the intersection of all three. We take the establishment's tools (LLMs, fine-tuning, evaluation frameworks), apply the critical scholars' analysis (the diagnostic gaze, technoableism, discursive harm), and use Mad Studies and Disability Justice as the foundation for training an alternative.

Nobody else appears to be doing this. That's the gap.

---

*This is a living document. Last updated March 2026.*
*Maintained by Dr. Sparrow Panton and Claude (Anthropic).*
