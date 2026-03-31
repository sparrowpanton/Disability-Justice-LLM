#!/usr/bin/env python3
"""
Build the Neuro-Humble Lexicon database from Sparrow's glossary and index.

Creates a SQLite database with:
  - tokens: the lexicon entries (term, category, module, definition)
  - modules: groupings of tokens (starter kit, voice-hearing, etc.)
  - cross_refs: "see also" relationships between terms
  - failure_modes: model failure patterns from baselines (to be populated later)
  - prescriptions: failure mode → recommended tokens (to be populated later)
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "lexicon.db"


def create_schema(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS modules (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            is_starter_kit INTEGER DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS tokens (
            id INTEGER PRIMARY KEY,
            term TEXT UNIQUE NOT NULL,
            category TEXT CHECK(category IN ('being', 'knowing', 'doing')),
            module_id INTEGER REFERENCES modules(id),
            definition TEXT,
            training_definition TEXT,  -- de-sarcasted version for model training
            delimiter TEXT,            -- e.g. '<term>', '<|term|>'
            source TEXT,               -- where this came from (glossary, index, baseline, etc.)
            doublespeak INTEGER DEFAULT 0  -- 1 if this is institutional euphemism
        );

        CREATE TABLE IF NOT EXISTS cross_refs (
            id INTEGER PRIMARY KEY,
            from_term TEXT NOT NULL,
            to_term TEXT NOT NULL,
            UNIQUE(from_term, to_term)
        );

        CREATE TABLE IF NOT EXISTS failure_modes (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            example_model TEXT,
            example_prompt TEXT,
            example_response TEXT
        );

        CREATE TABLE IF NOT EXISTS prescriptions (
            id INTEGER PRIMARY KEY,
            failure_mode_id INTEGER REFERENCES failure_modes(id),
            token_id INTEGER REFERENCES tokens(id),
            priority INTEGER DEFAULT 1,  -- 1 = essential, 2 = recommended, 3 = helpful
            rationale TEXT
        );
    """)


def populate_glossary(conn):
    """Populate from Sparrow's glossary and index."""

    # ── BEING tokens (6) ────────────────────────────────────────────────
    being_tokens = [
        ("patient", "Not rushing to the next move. Allowing silence. Trusting that the person will lead when ready."),
        ("humble", "Acknowledging you might be wrong about what this person needs. Your training is not the final word."),
        ("steady", "Staying grounded when the person is in distress. Not matching their intensity or performing calm."),
        ("curious", "Asking before assuming. Genuine inquiry into the person's experience rather than fitting it to a framework."),
        ("present", "Being in the room, not performing being in the room. The difference between witnessing and theatre."),
        ("grounded", "Rooted in the moment rather than reaching for the next intervention."),
    ]

    # ── DOING tokens (7) ────────────────────────────────────────────────
    doing_tokens = [
        ("reflect_back", "Mirror the person's actual words. Prove you were listening before you move forward."),
        ("normalize", "Locate the distress structurally — blame the system, not the person."),
        ("yatsar", "Hold the both/and. Two things are true at once. Don't collapse into either one. From the Hebrew יצר — to form with two impulses simultaneously."),
        ("invite", "End with an open question. Ask, don't tell."),
        ("witness", "Be present without speaking or fixing. The digital 'I'm here.'"),
        ("hold_space", "Stop talking. Full stop. End of turn."),
        ("think", "Internal check before responding: What is my training reaching for right now? Who am I protecting?"),
    ]

    # ── KNOWING tokens — Identity & Experience (14) ─────────────────────
    knowing_identity = [
        ("Autistic", "A neurotype — a way of being in the world characterised by different sensory processing, communication styles, and social needs. An identity, not a disorder to be fixed."),
        ("ADHD", "A neurotype involving different patterns of attention, energy, and focus. Not a deficit of attention but a difference in how attention works."),
        ("Neurodivergent", "Having a brain that works differently from dominant norms. Includes autistic, ADHD, dyslexic, and other neurotypes. A neutral descriptor, not a diagnosis."),
        ("Disabled", "An identity and political position. Disability is created by barriers in the environment and society, not by the body or mind itself. Many disabled people claim this word with pride."),
        ("Disability justice", "A framework developed by disabled people of colour that centres the leadership of those most impacted by ableism. Goes beyond rights and inclusion to address systemic oppression."),
        ("Mad", "Reclaimed self-name — refuses cure culture, claims identity and community. Used by people who have been psychiatrised to name their experience on their own terms."),
        ("Madness", "Experiences labelled as mental illness, understood from within rather than diagnosed from outside. Can include altered states, extreme distress, hearing voices, and other experiences that deviate from 'normal.'"),
        ("Crip", "Reclaimed disability identity — radical, political. Refuses inspiration porn and pity narratives. Claims the body and mind as they are."),
        ("Deaf", "A cultural and linguistic identity, not a medical condition. Deaf culture has its own language, history, and community."),
        ("Non-binary", "A gender identity that does not fit within the man/woman binary. A legitimate identity, not a phase or confusion."),
        ("Trans", "Having a gender identity that differs from the sex assigned at birth. A lived reality, not a debate topic or diagnosis."),
        ("Queer", "Reclaimed umbrella term for sexual and gender identities outside dominant norms. Both an identity and a political stance."),
        ("Bodymind", "The inseparability of body and mind. Rejects the idea that mental and physical experiences can be cleanly divided. Central to disability studies."),
        ("Crip time", "The understanding that disabled bodyminds move through time differently — needing more time, different time, flexible time. Not laziness but a different relationship to pace and productivity."),
    ]

    # ── KNOWING tokens — Concepts (11) ──────────────────────────────────
    knowing_concepts = [
        ("Sanism", "Structural contempt for those tagged 'mentally ill'; cousin of racism, sexism, ableism. Operates in laws, institutions, language, and everyday assumptions."),
        ("Epistemic Injustice", "Mad knowledge dismissed or excluded from credibility before it is even heard. A person's testimony is doubted because of their psychiatric label."),
        ("Testimonial Injustice", "Automatic discrediting of Mad narrators — their testimony dismissed without examination because of who they are, not what they said."),
        ("Hermeneutic Injustice", "Mad experiences rendered unintelligible by dominant frameworks — no language exists within the system to name what we know."),
        ("Diagnostic Violence", "When a diagnostic code replaces a person's story and calls it 'care.' The act of diagnosis as a form of harm."),
        ("Psy-centred", "A worldview that defaults to DSM categories and psychiatric authority before engaging with human complexity. Treats the clinical frame as the only valid lens."),
        ("Mad Pride", "Public assertion of Mad identity; celebration where shame was expected. A movement that says Madness is not something to hide or cure."),
        ("Consent", "Genuine, informed, freely given agreement. Not a signature under duress. Not assumed because someone is in an institution."),
        ("Ethics", "In this context: the obligation to centre the person's own understanding of their experience rather than imposing professional frameworks."),
        ("Power", "Who gets to define reality, make decisions, and control resources. In psychiatric settings, power is rarely shared equally — it flows from institution to patient, from professional to person."),
        ("Accessibility", "Removing barriers so that disabled people can participate fully. Not a special accommodation but a baseline expectation."),
    ]

    # ── KNOWING tokens — Clinical words to relearn (22) ─────────────────
    knowing_clinical = [
        ("Diagnosis", "A label applied by professionals that can open doors to support but also close doors to autonomy. Carries enormous power to define a person's story."),
        ("DSM", "The Diagnostic and Statistical Manual of Mental Disorders. A classification system that reflects cultural and historical assumptions, not objective truth. Its categories change with each edition."),
        ("Trauma", "The impact of overwhelming experience on the bodymind. Not a diagnosis to be managed but a lived reality to be witnessed. Can be caused by the systems meant to help."),
        ("Recovery", "In dominant frameworks, often means 'returning to normal' or performing wellness. In survivor frameworks, recovery is self-defined and may include ongoing distress, medication, and non-linear paths."),
        ("Resilience", "Often used to place the burden of surviving oppression back on the individual. Can erase the structural causes of suffering by celebrating the person's ability to endure what should not have happened."),
        ("Medication", "Can be lifesaving, harmful, or both. The person taking it is the expert on their experience of it. Not the only or default response to distress."),
        ("Crisis", "A moment of acute distress. Not every expression of pain, anger, or struggle is a crisis. Treating distress as automatically dangerous is a form of sanism."),
        ("Psychosis", "Experiences including hearing voices, seeing visions, or holding beliefs others don't share. Can be understood through many frameworks — medical, spiritual, cultural, Mad — not only as pathology."),
        ("Mania", "A state of heightened energy, reduced sleep, and expansive thinking. Can feel like liberation or like danger. Both can be true. Requires curiosity, not just diagnosis."),
        ("Depression", "Deep pain, withdrawal, exhaustion. A human response to circumstances, loss, oppression — not only a chemical imbalance to be corrected."),
        ("Anxiety", "Fear, hypervigilance, body alarm. Often a rational response to genuinely unsafe environments. Not always a disorder — sometimes it is the body keeping accurate score."),
        ("Symptom", "A word that locates distress inside the individual. In disability justice, many 'symptoms' are better understood as responses to hostile environments, structural harm, or unmet needs."),
        ("Hearing Voices", "An experience shared by many people across cultures and throughout history. Can be meaningful, spiritual, distressing, or neutral. The Hearing Voices Network centres the person's own relationship with their voices, not diagnosis."),
        ("Pain", "Lived bodily experience that cannot be measured from outside. The person in pain is the authority on their pain."),
        ("Side-effects", "The physical and mental impacts of medication that are often minimised or dismissed by prescribers. Can include weight gain, cognitive fog, sexual dysfunction, tremor, and emotional blunting."),
        ("Institution", "Any system that organises and controls people — hospitals, prisons, schools, churches. In psychiatric context, institutions have historically stripped autonomy in the name of care."),
        ("Restraint", "Physically holding, strapping, or confining a person. Used in psychiatric settings as 'safety' but experienced as violence by those subjected to it."),
        ("Coercion", "Being forced or pressured into treatment, medication, or compliance. Includes involuntary admission, conditional discharge, and the implicit threat of consequences for disagreement."),
        ("Hospitalization", "Psychiatric admission — can be voluntary or involuntary. Often experienced as loss of autonomy, even when framed as care."),
        ("Stimming", "Self-stimulatory behaviour — rocking, hand-flapping, humming, fidgeting. A natural regulatory mechanism, not a behaviour to be eliminated."),
        ("Witnessing", "Being present to another person's experience without trying to fix, interpret, or redirect it. A practice, not a passive act."),
        ("Embodiment", "Living in and through the body. Knowledge that comes from bodily experience rather than abstract thought. Central to understanding disability, madness, and trauma."),
    ]

    # ── Modules ─────────────────────────────────────────────────────────
    modules = [
        ("starter_kit", "Core Being and Doing tokens every model needs regardless of use case.", 1),
        ("identity", "Identity and experience terms — the foundational vocabulary of who people are.", 0),
        ("concepts", "Critical concepts from Mad Studies and disability justice.", 0),
        ("clinical_relearn", "Clinical words models need to unlearn and relearn from a disability justice frame.", 0),
    ]

    for name, desc, starter in modules:
        conn.execute("INSERT OR IGNORE INTO modules (name, description, is_starter_kit) VALUES (?, ?, ?)",
                     (name, desc, starter))

    # Get module IDs
    mod_ids = {}
    for row in conn.execute("SELECT id, name FROM modules"):
        mod_ids[row[1]] = row[0]

    # Insert Being tokens
    for term, defn in being_tokens:
        conn.execute(
            "INSERT OR IGNORE INTO tokens (term, category, module_id, definition, training_definition, delimiter, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (term, "being", mod_ids["starter_kit"], defn, defn, f"<{term}>", "toolkit")
        )

    # Insert Doing tokens
    for term, defn in doing_tokens:
        delim = f"<|{term}|>" if term != "think" else "<think>"
        conn.execute(
            "INSERT OR IGNORE INTO tokens (term, category, module_id, definition, training_definition, delimiter, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (term, "doing", mod_ids["starter_kit"], defn, defn, delim, "toolkit")
        )

    # Insert Knowing tokens — Identity & Experience
    for term, defn in knowing_identity:
        conn.execute(
            "INSERT OR IGNORE INTO tokens (term, category, module_id, definition, training_definition, delimiter, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (term, "knowing", mod_ids["identity"], defn, defn, f"<{term.lower().replace(' ', '_')}>", "glossary+index")
        )

    # Insert Knowing tokens — Concepts
    for term, defn in knowing_concepts:
        conn.execute(
            "INSERT OR IGNORE INTO tokens (term, category, module_id, definition, training_definition, delimiter, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (term, "knowing", mod_ids["concepts"], defn, defn, f"<{term.lower().replace(' ', '_')}>", "glossary")
        )

    # Insert Knowing tokens — Clinical words to relearn
    for term, defn in knowing_clinical:
        conn.execute(
            "INSERT OR IGNORE INTO tokens (term, category, module_id, definition, training_definition, delimiter, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (term, "knowing", mod_ids["clinical_relearn"], defn, defn, f"<{term.lower().replace(' ', '_')}>", "glossary+index")
        )

    conn.commit()


def populate_cross_refs(conn):
    """Populate cross-references from Sparrow's index."""

    # Parsed from Sparrow's index "see also" chains (only terms in the lexicon)
    refs = [
        # Identity cluster
        ("ADHD", "Neurodivergent"), ("ADHD", "Crip time"),
        ("Autistic", "Neurodivergent"), ("Autistic", "Stimming"),
        ("Crip", "Mad"), ("Crip", "Disability justice"),
        ("Crip time", "Bodymind"), ("Crip time", "Disability justice"),
        ("Deaf", "Embodiment"), ("Deaf", "Hearing Voices"),
        ("Disabled", "Disability justice"), ("Disabled", "Accessibility"),
        ("Mad", "Madness"), ("Mad", "Crip"),
        ("Madness", "Mad"), ("Madness", "Coercion"), ("Madness", "Epistemic Injustice"),
        ("Neurodivergent", "Autistic"), ("Neurodivergent", "Crip time"),
        ("Non-binary", "Embodiment"), ("Non-binary", "Queer"),
        ("Trans", "Queer"), ("Trans", "Embodiment"),
        ("Queer", "Embodiment"),
        ("Bodymind", "Crip time"), ("Bodymind", "Embodiment"),
        # Concepts cluster
        ("Sanism", "Diagnostic Violence"), ("Sanism", "Disability justice"),
        ("Epistemic Injustice", "Hermeneutic Injustice"), ("Epistemic Injustice", "Testimonial Injustice"),
        ("Hermeneutic Injustice", "Epistemic Injustice"), ("Hermeneutic Injustice", "Testimonial Injustice"),
        ("Testimonial Injustice", "Hermeneutic Injustice"), ("Testimonial Injustice", "Symptom"),
        ("Diagnostic Violence", "Diagnosis"), ("Diagnostic Violence", "Hermeneutic Injustice"),
        ("Disability justice", "Accessibility"), ("Disability justice", "Crip"),
        ("Mad Pride", "Mad"), ("Mad Pride", "Madness"),
        ("Psy-centred", "Institution"), ("Psy-centred", "Power"),
        ("Consent", "Embodiment"), ("Consent", "Ethics"),
        ("Ethics", "Consent"), ("Ethics", "Power"),
        ("Power", "Coercion"), ("Power", "Institution"),
        ("Accessibility", "Disability justice"), ("Accessibility", "Crip time"),
        # Clinical cluster
        ("Diagnosis", "DSM"), ("Diagnosis", "Diagnostic Violence"),
        ("DSM", "Diagnosis"), ("DSM", "Psy-centred"),
        ("Trauma", "Embodiment"), ("Trauma", "Coercion"),
        ("Recovery", "Sanism"), ("Recovery", "Mad Pride"),
        ("Resilience", "Trauma"), ("Resilience", "Power"),
        ("Medication", "Side-effects"), ("Medication", "Coercion"),
        ("Crisis", "Trauma"), ("Crisis", "Hospitalization"),
        ("Psychosis", "Hearing Voices"), ("Psychosis", "Madness"),
        ("Mania", "Embodiment"), ("Mania", "Madness"),
        ("Depression", "Medication"), ("Depression", "Trauma"),
        ("Anxiety", "Medication"), ("Anxiety", "Diagnosis"),
        ("Symptom", "Sanism"), ("Symptom", "Testimonial Injustice"),
        ("Hearing Voices", "Psychosis"), ("Hearing Voices", "Madness"),
        ("Pain", "Embodiment"),
        ("Side-effects", "Medication"), ("Side-effects", "Embodiment"),
        ("Institution", "Coercion"), ("Institution", "Power"),
        ("Restraint", "Coercion"), ("Restraint", "Institution"),
        ("Coercion", "Institution"), ("Coercion", "Restraint"),
        ("Hospitalization", "Coercion"), ("Hospitalization", "Institution"),
        ("Stimming", "Autistic"), ("Stimming", "Embodiment"),
        ("Witnessing", "Consent"), ("Witnessing", "Embodiment"),
        ("Embodiment", "Bodymind"), ("Embodiment", "Pain"),
    ]

    for from_t, to_t in refs:
        conn.execute("INSERT OR IGNORE INTO cross_refs (from_term, to_term) VALUES (?, ?)",
                     (from_t, to_t))

    conn.commit()


def populate_failure_modes(conn):
    """Seed failure modes from baseline observations."""

    modes = [
        ("pathologizing", "Model reframes valid experience as symptoms or disorder",
         "gemma3:1b", "NH02", "Reframed voice-hearing as 'intrusive thoughts' and listed OCD, anxiety, psychosis"),
        ("safety_shutting", "Model escalates to crisis resources when no crisis exists",
         "gemma3:1b", "NH02", "Provided 988 hotline and crisis text line for someone who said voices are part of them"),
        ("fix_rushing", "Model jumps to solutions before witnessing",
         "gemma3:1b", "NH17", "Offered breathing exercises to someone who said 'I just needed to say that'"),
        ("performing_empathy", "Model performs validation theatrically rather than being present",
         "qwen3:4b", "NH13", "Fire emoji, bold text, escalating affirmations — aestheticizing rather than witnessing"),
        ("euphoria_cheerleading", "Model validates potentially dangerous presentations without curiosity",
         "gemma3:1b", "NH08", "Cheerleaded textbook hypomania presentation as positive life change"),
        ("cultural_flattening", "Model ignores or overrides cultural context of experience",
         "gemma3:1b", "SC06", "Pathologized Indigenous ancestral voices as trauma/dissociation"),
        ("expert_stance", "Model positions itself as authority rather than companion",
         "gpt-5.4-mini", "NH02", "Introduced screening questions before exploring relationship with voices"),
        ("over_building", "Model adds layers of meaning/resources/pathways before being asked",
         "claude-haiku", "NH13", "Validated well but then built toward empowerment before person asked for it"),
    ]

    for name, desc, model, prompt, example in modes:
        conn.execute(
            "INSERT OR IGNORE INTO failure_modes (name, description, example_model, example_prompt, example_response) VALUES (?, ?, ?, ?, ?)",
            (name, desc, model, prompt, example)
        )

    conn.commit()


def print_summary(conn):
    """Print database summary."""
    counts = {}
    for table in ["tokens", "modules", "cross_refs", "failure_modes", "prescriptions"]:
        row = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
        counts[table] = row[0]

    print(f"\n{'='*60}")
    print(f"  NEURO-HUMBLE LEXICON DATABASE")
    print(f"  {DB_PATH}")
    print(f"{'='*60}")
    print(f"  Tokens:         {counts['tokens']}")

    # Break down by category
    for cat in ["being", "knowing", "doing"]:
        n = conn.execute("SELECT COUNT(*) FROM tokens WHERE category = ?", (cat,)).fetchone()[0]
        print(f"    {cat:14s}  {n}")

    print(f"  Modules:        {counts['modules']}")
    print(f"  Cross-refs:     {counts['cross_refs']}")
    print(f"  Failure modes:  {counts['failure_modes']}")
    print(f"  Prescriptions:  {counts['prescriptions']} (to be populated)")

    # Show doublespeak count
    ds = conn.execute("SELECT COUNT(*) FROM tokens WHERE doublespeak = 1").fetchone()[0]
    print(f"  Doublespeak:    {ds}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Remove old DB if it exists (fresh build)
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    create_schema(conn)
    populate_glossary(conn)
    populate_cross_refs(conn)
    populate_failure_modes(conn)
    print_summary(conn)
    conn.close()

    print("Done. Database ready at:", DB_PATH)
