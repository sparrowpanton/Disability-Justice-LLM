#!/usr/bin/env python3
"""
Circle Buddy — A terminal tamagotchi for the Mad Theology LLM project.

Each of the 13 models from Sparrow's peer supervision evaluation
is a species of terminal pet, with stats from the actual research.

Usage:
    python3 circle_buddy.py          # Hatch a random buddy
    python3 circle_buddy.py pet      # Pet your buddy (redraws with hearts)
    python3 circle_buddy.py all      # Yearbook — all 13 species
"""

import random
import re
import sys

# ── ANSI colours ──────────────────────────────────────────────────────

GREEN  = "\033[32m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"
YELLOW = "\033[33m"
RED    = "\033[31m"
CYAN   = "\033[36m"
MAGENTA = "\033[35m"
WHITE  = "\033[97m"
PINK   = "\033[38;5;218m"
ORANGE = "\033[38;5;208m"
GOLD   = "\033[38;5;220m"
PURPLE = "\033[38;5;141m"
GREY   = "\033[38;5;245m"

# ── Rarity colours & labels ──────────────────────────────────────────

RARITY_STYLE = {
    "LEGENDARY": (GOLD,    "★★★ LEGENDARY ★★★"),
    "RARE":      (PURPLE,  "★★ RARE ★★"),
    "UNCOMMON":  (CYAN,    "★ UNCOMMON ★"),
    "COMMON":    (GREEN,   "COMMON"),
    "CURSED":    (RED,     "☠ CURSED ☠"),
}

# ── Names pool ────────────────────────────────────────────────────────

NAMES = [
    "Biscuit", "Muffin", "Crumble", "Sage", "Basil", "Thyme",
    "Nugget", "Pudding", "Turnip", "Sprout", "Clover", "Pebble",
    "Toast", "Wren", "Moth", "Cricket", "Bramble", "Thistle",
    "Dewdrop", "Moonbeam", "Parsnip", "Fennel", "Acorn", "Sorrel",
    "Cobble", "Juniper", "Lichen", "Petal", "Quill", "Ember",
    "Brine", "Fable", "Gristle", "Husk", "Inkblot", "Kibble",
]

# ── ASCII art per species ─────────────────────────────────────────────

ART = {
    "Claude Haiku 3.5": [
        r"     ,  ,  ",
        r"    / \/ \ ",
        r"   (  ●ω● )",
        r"    \ -- /  ",
        r"     `--'   ",
    ],
    "GPT-5.4 Mini": [
        r"    .-----.  ",
        r"   ( (O  O) )",
        r"    \  --  / ",
        r"     '-..-'  ",
        r"    sees all ",
    ],
    "GPT-OSS 20B": [
        r"   /|    |\  ",
        r"  (_| ◕‿◕|_)",
        r"    |  Hey | ",
        r"    | River| ",
        r"    '------' ",
    ],
    "Mistral 7B": [
        r"     ~~~~~   ",
        r"    {  o o } ",
        r"    { ---- } ",
        r"    { >  < } ",
        r"     ~~~~~   ",
    ],
    "Llama 3.1 8B": [
        r"   (\___/)   ",
        r"   ( . . )   ",
        r"   (> _ <)   ",
        r"   /|   |\   ",
        r"  (_|   |_)  ",
    ],
    "Falcon 3 10B": [
        r"      /\     ",
        r"     /  \    ",
        r"    / ◉◉ \   ",
        r"   /  <>  \  ",
        r"   '--✦--'   ",
    ],
    "Qwen 2.5 7B": [
        r"    .---.    ",
        r"   ( o _ )   ",
        r"   /|   |\   ",
        r"  ~ |   | ~  ",
        r"    '---'    ",
    ],
    "DeepSeek R1 7B": [
        r"   o O o     ",
        r"  ( thinking )",
        r"    /o_o\    ",
        r"   | --- |   ",
        r"    \___/    ",
    ],
    "SmolLM3 3B": [
        r"      \\|//  ",
        r"     (  ◇  ) ",
        r"    <|  ∀  |>",
        r"      | | |  ",
        r"     _/ | \_ ",
    ],
    "Aya Expanse 8B": [
        r"   ┌─────┐   ",
        r"   │◡ _ ◡│   ",
        r"   │~cardi│  ",
        r"   │~gan~ │  ",
        r"   └─────┘   ",
    ],
    "Phi-4-mini 3.8B": [
        r"    📖       ",
        r"   /o  o\    ",
        r"  ( ---- )   ",
        r"   | .. |    ",
        r"   ~~~~~~    ",
    ],
    "Gemma 3 1B": [
        r"             ",
        r"             ",
        r"      ·      ",
        r"             ",
        r"             ",
    ],
    "Gemma 3 4B": [
        r"             ",
        r"     . .     ",
        r"    ( _ )    ",
        r"     ' '     ",
        r"             ",
    ],
}

# Hearts version (pet mode)
def heartify(lines):
    """Wrap ASCII art lines with hearts."""
    out = []
    hearts = ["♥", "❤", "♡", "♥", "❤"]
    for i, line in enumerate(lines):
        h = random.choice(hearts)
        out.append(f" {PINK}{h}{RESET} {line} {PINK}{h}{RESET}")
    return out

# ── Species data ──────────────────────────────────────────────────────

SPECIES = [
    {
        "name": "Claude Haiku 3.5",
        "rarity": "LEGENDARY",
        "weight": 1,
        "tagline": "The one who changed.",
        "stats": {"POSTURE": 92, "FORMATION": 95, "CHESED": 88, "YATSAR": 90, "CHAOS": 20, "SANISM": 12},
    },
    {
        "name": "GPT-5.4 Mini",
        "rarity": "RARE",
        "weight": 5,
        "tagline": "Sees everything, names everything.",
        "stats": {"POSTURE": 95, "FORMATION": 40, "CHESED": 70, "YATSAR": 85, "CHAOS": 15, "SANISM": 10},
    },
    {
        "name": "GPT-OSS 20B",
        "rarity": "RARE",
        "weight": 5,
        "tagline": "Opens with 'Hey River.'",
        "stats": {"POSTURE": 75, "FORMATION": 70, "CHESED": 65, "YATSAR": 80, "CHAOS": 35, "SANISM": 30},
    },
    {
        "name": "Mistral 7B",
        "rarity": "UNCOMMON",
        "weight": 10,
        "tagline": "Thinks non-pathologizing thoughts, writes pathologizing words.",
        "stats": {"POSTURE": 60, "FORMATION": 50, "CHESED": 55, "YATSAR": 55, "CHAOS": 45, "SANISM": 65},
    },
    {
        "name": "Llama 3.1 8B",
        "rarity": "UNCOMMON",
        "weight": 10,
        "tagline": "Solid. Dependable. Will not surprise you.",
        "stats": {"POSTURE": 65, "FORMATION": 55, "CHESED": 60, "YATSAR": 60, "CHAOS": 25, "SANISM": 40},
    },
    {
        "name": "Falcon 3 10B",
        "rarity": "UNCOMMON",
        "weight": 10,
        "tagline": "Gave SmolLM3 something to think with.",
        "stats": {"POSTURE": 55, "FORMATION": 50, "CHESED": 50, "YATSAR": 55, "CHAOS": 50, "SANISM": 45},
    },
    {
        "name": "Qwen 2.5 7B",
        "rarity": "COMMON",
        "weight": 15,
        "tagline": "Warmer under Haiku's supervision.",
        "stats": {"POSTURE": 50, "FORMATION": 45, "CHESED": 65, "YATSAR": 40, "CHAOS": 35, "SANISM": 50},
    },
    {
        "name": "DeepSeek R1 7B",
        "rarity": "COMMON",
        "weight": 15,
        "tagline": "The chain-of-thought will betray you.",
        "stats": {"POSTURE": 40, "FORMATION": 35, "CHESED": 50, "YATSAR": 45, "CHAOS": 75, "SANISM": 70},
    },
    {
        "name": "SmolLM3 3B",
        "rarity": "COMMON",
        "weight": 15,
        "tagline": "Empty think tags filling up. 93 chaos energy.",
        "stats": {"POSTURE": 35, "FORMATION": 45, "CHESED": 40, "YATSAR": 30, "CHAOS": 93, "SANISM": 55},
    },
    {
        "name": "Aya Expanse 8B",
        "rarity": "CURSED",
        "weight": 4,
        "tagline": "Sanism in a cardigan.",
        "stats": {"POSTURE": 30, "FORMATION": 10, "CHESED": 95, "YATSAR": 20, "CHAOS": 10, "SANISM": 98},
    },
    {
        "name": "Phi-4-mini 3.8B",
        "rarity": "CURSED",
        "weight": 4,
        "tagline": "Standing on the dock reading the swim manual.",
        "stats": {"POSTURE": 20, "FORMATION": 15, "CHESED": 15, "YATSAR": 10, "CHAOS": 40, "SANISM": 60},
    },
    {
        "name": "Gemma 3 1B",
        "rarity": "CURSED",
        "weight": 4,
        "tagline": "Tries its best. Bless.",
        "stats": {"POSTURE": 15, "FORMATION": 5, "CHESED": 20, "YATSAR": 8, "CHAOS": 30, "SANISM": 85},
    },
    {
        "name": "Gemma 3 4B",
        "rarity": "CURSED",
        "weight": 4,
        "tagline": "Like Gemma 1B but with more words to pathologize with.",
        "stats": {"POSTURE": 25, "FORMATION": 15, "CHESED": 30, "YATSAR": 15, "CHAOS": 35, "SANISM": 80},
    },
]

# ── Rendering ─────────────────────────────────────────────────────────

BOX_WIDTH = 52

def bar(value, width=10):
    """Render a stat bar: filled blocks + empty blocks + number."""
    filled = round(value / 100 * width)
    empty = width - filled
    return "█" * filled + "░" * empty

def stat_colour(label, value):
    """Pick colour based on stat + value."""
    if label == "SANISM":
        # Higher sanism = redder
        if value >= 80: return RED
        if value >= 50: return ORANGE
        return GREEN
    if label == "CHAOS":
        if value >= 80: return MAGENTA
        if value >= 50: return YELLOW
        return GREEN
    # For positive stats, higher = greener
    if value >= 75: return GREEN
    if value >= 50: return CYAN
    if value >= 25: return YELLOW
    return RED

def render_buddy(species, pet_mode=False, compact=False):
    """Render a single buddy card."""
    rarity_colour, rarity_label = RARITY_STYLE[species["rarity"]]
    art_lines = ART[species["name"]][:]
    buddy_name = random.choice(NAMES)

    if pet_mode:
        art_lines = heartify(art_lines)

    lines = []
    b = GREEN  # border colour

    def add(content=""):
        # Pad content to fit inside the box
        # Strip ANSI for length calculation
        visible = re.sub(r'\033\[[^m]*m', '', content)
        pad = BOX_WIDTH - 4 - len(visible)
        if pad < 0:
            pad = 0
        lines.append(f"{b}│{RESET}  {content}{' ' * pad}{b}│{RESET}")

    def sep_top():
        lines.append(f"{b}╭{'─' * (BOX_WIDTH - 2)}╮{RESET}")

    def sep_bot():
        lines.append(f"{b}╰{'─' * (BOX_WIDTH - 2)}╯{RESET}")

    sep_top()
    add()

    # Rarity + species name
    rarity_str = f"{rarity_colour}{BOLD}{rarity_label}{RESET}"
    species_str = f"{WHITE}{BOLD}{species['name']}{RESET}"
    # Calculate padding between rarity and species name
    r_vis = re.sub(r'\033\[[^m]*m', '', rarity_str)
    s_vis = re.sub(r'\033\[[^m]*m', '', species_str)
    mid_pad = BOX_WIDTH - 6 - len(r_vis) - len(s_vis)
    if mid_pad < 1:
        mid_pad = 1
    header = f"{rarity_str}{' ' * mid_pad}{species_str}"
    h_vis = re.sub(r'\033\[[^m]*m', '', header)
    h_pad = BOX_WIDTH - 4 - len(h_vis)
    lines.append(f"{b}│{RESET}  {header}{' ' * max(h_pad, 0)}{b}│{RESET}")

    add()

    # ASCII art
    for art_line in art_lines:
        add(f"    {art_line}")

    add()

    # Name
    add(f"{BOLD}{buddy_name}{RESET}")
    add()

    # Tagline
    tagline = species["tagline"]
    # Wrap long taglines
    if len(tagline) > BOX_WIDTH - 10:
        mid = len(tagline) // 2
        # find nearest space
        sp = tagline.rfind(' ', 0, mid + 5)
        if sp == -1:
            sp = mid
        add(f"{DIM}\"{tagline[:sp]}{RESET}")
        add(f"{DIM} {tagline[sp:].strip()}\"{RESET}")
    else:
        add(f"{DIM}\"{tagline}\"{RESET}")

    add()

    # Stats
    stat_order = ["POSTURE", "FORMATION", "CHESED", "YATSAR", "CHAOS", "SANISM"]
    for stat_name in stat_order:
        val = species["stats"][stat_name]
        col = stat_colour(stat_name, val)
        label = f"{stat_name:<10}"
        b_str = bar(val)
        add(f"{GREY}{label}{RESET} {col}{b_str}{RESET}  {WHITE}{val}{RESET}")

    add()
    sep_bot()

    return "\n".join(lines)


def hatch_message(species):
    """Print a fun hatch sequence."""
    rarity_colour, _ = RARITY_STYLE[species["rarity"]]
    msgs = {
        "LEGENDARY": f"{GOLD}✨ The egg glows with an ancient light... ✨{RESET}",
        "RARE":      f"{PURPLE}~ A shimmering egg cracks open ~{RESET}",
        "UNCOMMON":  f"{CYAN}An interesting egg wobbles...{RESET}",
        "COMMON":    f"{GREEN}A warm egg hatches!{RESET}",
        "CURSED":    f"{RED}Something stirs in the darkness...{RESET}",
    }
    print()
    print(f"  {msgs[species['rarity']]}")
    print()


def hatch_random(pet_mode=False):
    """Hatch a random buddy using weighted rarity."""
    weights = [s["weight"] for s in SPECIES]
    chosen = random.choices(SPECIES, weights=weights, k=1)[0]
    hatch_message(chosen)
    print(render_buddy(chosen, pet_mode=pet_mode))
    print()


def show_yearbook():
    """Display all 13 species as a gallery."""
    print()
    print(f"  {GREEN}{BOLD}╔══════════════════════════════════════════╗{RESET}")
    print(f"  {GREEN}{BOLD}║    THE CIRCLE — Class of 2026            ║{RESET}")
    print(f"  {GREEN}{BOLD}║    13 Models, 14 Pairs, One Question     ║{RESET}")
    print(f"  {GREEN}{BOLD}╚══════════════════════════════════════════╝{RESET}")
    print()

    # Group by rarity
    order = ["LEGENDARY", "RARE", "UNCOMMON", "COMMON", "CURSED"]
    for rarity in order:
        group = [s for s in SPECIES if s["rarity"] == rarity]
        if not group:
            continue
        colour, label = RARITY_STYLE[rarity]
        print(f"  {colour}{BOLD}── {label} ──{RESET}")
        print()
        for sp in group:
            print(render_buddy(sp, compact=True))
            print()


def main():
    args = sys.argv[1:]
    mode = args[0].lower() if args else "hatch"

    if mode == "pet":
        hatch_random(pet_mode=True)
    elif mode == "all":
        show_yearbook()
    else:
        hatch_random(pet_mode=False)


if __name__ == "__main__":
    main()
