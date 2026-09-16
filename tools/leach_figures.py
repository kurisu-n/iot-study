"""Generates the step-by-step figures for Chapter 2, LEACH.

Same rules as tools/dd_panels.py, and for the same reasons:
  - One fixed node layout reused across panels, so rounds and phases read as the
    same network.
  - No text inside any SVG. Every explanation is HTML beneath the panel, which is
    what keeps text off shapes (tools/figure-audit.js) and lets the shorthand
    hook check it.
  - Every colour is a --fig-* token.

Colour meanings match Chapter 1, so they hold across the corpus:
  blue   control messages (the advertisement, the join request, the schedule)
  orange data (members to their head, the head to the base station)
  red    the node in the special role, here a cluster head
  dotted neutral ring  the node a step is about

The node picks are pseudo-random from a fixed seed, so the pictures look like a
random election but come out the same on every run.

Run:  python tools/leach_figures.py --apply docs/chapters/02-leach.md
"""

import math
import random
import re
import sys
from pathlib import Path

VIEW_W, VIEW_H = 260, 200
BS = (26, 26)          # the base station, outside the field, top left
BS_HALF = 11


# ---- The field ----------------------------------------------------------------

def field_nodes(count, seed, x0=70, x1=246, y0=28, y1=186, min_gap=24):
    rng = random.Random(seed)
    nodes = []
    tries = 0
    while len(nodes) < count and tries < 20000:
        tries += 1
        p = (rng.uniform(x0, x1), rng.uniform(y0, y1))
        if all(math.dist(p, q) >= min_gap for q in nodes):
            nodes.append(p)
    return nodes


NODES = field_nodes(22, seed=7)
R_NODE, R_HEAD = 6.5, 9

# Two rounds' worth of heads, chosen spread out and disjoint, so the second round
# visibly hands the role to other nodes.
HEADS_A = [1, 8, 14, 19]
HEADS_B = [4, 11, 16, 21]


def nearest(i, heads):
    return min(heads, key=lambda h: math.dist(NODES[i], NODES[h]))


# ---- Drawing -----------------------------------------------------------------

def arrow(p, q, stroke, width, r_from, r_to, dash=None, gap=3):
    (x1, y1), (x2, y2) = p, q
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    px, py = -uy, ux
    sx, sy = x1 + ux * (r_from + gap), y1 + uy * (r_from + gap)
    tx, ty = x2 - ux * (r_to + gap), y2 - uy * (r_to + gap)
    head_len, head_half = 6, 3.2
    lx, ly = tx - ux * head_len * 0.8, ty - uy * head_len * 0.8
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    hx, hy = tx - ux * head_len, ty - uy * head_len
    return (f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{stroke}" '
            f'stroke-width="{width}"{dash_attr} stroke-linecap="round"/>'
            f'<polygon points="{tx:.1f},{ty:.1f} {hx + px * head_half:.1f},{hy + py * head_half:.1f} '
            f'{hx - px * head_half:.1f},{hy - py * head_half:.1f}" fill="{stroke}"/>')


def line(p, q, stroke, width, dash=None):
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" '
            f'stroke="{stroke}" stroke-width="{width}"{dash_attr}/>')


def base_station():
    x, y = BS
    return (f'<rect x="{x - BS_HALF}" y="{y - BS_HALF}" width="{2 * BS_HALF}" height="{2 * BS_HALF}" rx="2" '
            f'fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.8"/>')


def node(p, head=False):
    if head:
        return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_HEAD}" fill="var(--fig-event)" '
                f'stroke="var(--fig-event-deep)" stroke-width="1.8"/>')
    return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_NODE}" fill="var(--fig-node)" '
            f'stroke="var(--fig-line)" stroke-width="1.4"/>')


def halo(p, r):
    return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r + 5}" fill="none" stroke="var(--fig-line)" '
            f'stroke-width="2" stroke-dasharray="2.5 2"/>')


def svg(parts):
    return (f'<svg viewBox="0 0 {VIEW_W} {VIEW_H}" xmlns="http://www.w3.org/2000/svg" role="img">'
            + "".join(parts) + "</svg>")


def round_panel(heads, stage):
    """stage: 'clusters', 'elect', 'advertise', 'join', 'steady'."""
    parts = [base_station()]
    members = [i for i in range(len(NODES)) if i not in heads]

    if stage == "advertise":
        for h in heads:
            x, y = NODES[h]
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="34" fill="none" stroke="var(--fig-accent)" '
                         f'stroke-width="1.5" stroke-dasharray="4 3"/>')

    if stage in ("clusters", "steady"):
        for i in members:
            h = nearest(i, heads)
            if stage == "clusters":
                parts.append(line(NODES[i], NODES[h], "var(--fig-node)", 1.1))
            else:
                parts.append(arrow(NODES[i], NODES[h], "var(--fig-warn)", 1.6, R_NODE, R_HEAD, gap=2))

    if stage == "join":
        for i in members:
            h = nearest(i, heads)
            parts.append(arrow(NODES[i], NODES[h], "var(--fig-accent)", 1.4, R_NODE, R_HEAD, dash="3 2", gap=2))

    if stage in ("clusters", "steady"):
        for h in heads:
            parts.append(arrow(NODES[h], BS, "var(--fig-warn)", 2.6, R_HEAD, BS_HALF + 2, gap=2))

    for i, p in enumerate(NODES):
        parts.append(node(p, head=(i in heads and stage != "elect")))

    if stage == "elect":
        for h in heads:
            parts.append(halo(NODES[h], R_NODE))

    return svg(parts)


# ---- The era, N = 70, P = 1/7 --------------------------------------------------

ERA_COLS, ERA_ROWS, ERA_GAP = 10, 7, 20
ERA_W, ERA_H = 20 + ERA_COLS * ERA_GAP, 20 + ERA_ROWS * ERA_GAP
_perm = list(range(70))
random.Random(21).shuffle(_perm)
ERA_HEADS = [_perm[10 * r: 10 * r + 10] for r in range(7)]
_next = list(range(70))
random.Random(99).shuffle(_next)
ERA_NEXT = _next[:10]


def era_panel(r):
    parts = []
    served = set(sum(ERA_HEADS[:r], [])) if r < 7 else set()
    now = set(ERA_HEADS[r]) if r < 7 else set(ERA_NEXT)
    for idx in range(70):
        cx = 20 + (idx % ERA_COLS) * ERA_GAP
        cy = 20 + (idx // ERA_COLS) * ERA_GAP
        if idx in now:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="6.5" fill="var(--fig-event)" '
                         f'stroke="var(--fig-event-deep)" stroke-width="1.6"/>')
        elif idx in served:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="none" stroke="var(--fig-node)" stroke-width="1.6"/>')
        else:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="5.5" fill="var(--fig-node)" '
                         f'stroke="var(--fig-line)" stroke-width="1.2"/>')
    return (f'<svg viewBox="0 0 {ERA_W} {ERA_H}" xmlns="http://www.w3.org/2000/svg" role="img">'
            + "".join(parts) + "</svg>")


def era_caption(r):
    if r == 7:
        return ("<strong>Γύρος 7: νέα περίοδος.</strong> Επειδή 7 mod 7 = 0, όλοι οι κόμβοι ξαναμπαίνουν στο "
                "σύνολο G και ο κύκλος αρχίζει από την αρχή, με "
                r'<span class="arithmatex">\(T(n) = \tfrac{1}{7}\)</span>.')
    eligible = 70 - 10 * r
    frac = "1" if r == 6 else rf"\tfrac{{1}}{{{7 - r}}}"
    return (f"<strong>Γύρος {r}.</strong> Στο G μένουν {eligible} κόμβοι, "
            rf'<span class="arithmatex">\(T(n) = {frac}\)</span>'
            f", άρα κατά μέσο όρο γίνονται cluster heads {eligible} × "
            + ("1" if r == 6 else f"1/{7 - r}") + " = 10.")


# ---- Where nodes die: a schematic of Lecture 2, slides 61 to 63 -------------------

DEAD_NODES = field_nodes(34, seed=3, x0=48, x1=246, y0=46, y1=188, min_gap=26)


def dead_panel(kind):
    by_distance = sorted(range(len(DEAD_NODES)), key=lambda i: math.dist(DEAD_NODES[i], BS))
    k = len(DEAD_NODES) // 3
    if kind == "mte":
        dead = set(by_distance[:k])
    elif kind == "direct":
        dead = set(by_distance[-k:])
    else:
        dead = set(by_distance[1::3][:k])
    parts = [base_station()]
    for i, p in enumerate(DEAD_NODES):
        if i in dead:
            parts.append(f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="6" fill="none" '
                         f'stroke="var(--fig-line)" stroke-width="1.8"/>')
        else:
            parts.append(node(p))
    return svg(parts)


# ---- Figures ---------------------------------------------------------------------

LEGEND = {
    "bs": ("Base Station",
           '<rect x="3" y="1" width="12" height="12" rx="1.5" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.5"/>'),
    "head": ("cluster head",
             '<circle cx="9" cy="7" r="5.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.5"/>'),
    "member": ("μέλος συστάδας",
               '<circle cx="9" cy="7" r="4.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.2"/>'),
    "eligible": ("κόμβος στο G",
                 '<circle cx="9" cy="7" r="4.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.2"/>'),
    "served": ("έγινε ήδη cluster head σε αυτή την περίοδο",
               '<circle cx="9" cy="7" r="4.2" fill="none" stroke="var(--fig-node)" stroke-width="1.6"/>'),
    "active": ("κόμβος που εκλέγει τον εαυτό του",
               '<circle cx="9" cy="7" r="5.5" fill="none" stroke="var(--fig-line)" stroke-width="1.8" stroke-dasharray="2 1.6"/>'),
    "membership": ("ανήκει στη συστάδα",
                   '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-node)" stroke-width="1.2"/>'),
    "advert": ("advertisement",
               '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-accent)" stroke-width="1.5" stroke-dasharray="4 3"/>'),
    "join": ("αίτηση ένταξης",
             '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-accent)" stroke-width="1.4" stroke-dasharray="3 2"/>'),
    "data": ("δεδομένα",
             '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="1.8"/>'),
    "fused": ("συμπιεσμένα δεδομένα προς τη Base Station",
              '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="2.8"/>'),
    "alive": ("ζωντανός κόμβος",
              '<circle cx="9" cy="7" r="4.5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.2"/>'),
    "dead": ("κόμβος που εξαντλήθηκε",
             '<circle cx="9" cy="7" r="4.5" fill="none" stroke="var(--fig-line)" stroke-width="1.6"/>'),
}

FIGURES = {
    "clusters": {
        "caption": "Σχήμα 2.1 · Οι ίδιοι κόμβοι σε δύο διαδοχικούς γύρους. Οι συστάδες αλλάζουν επειδή αλλάζουν οι cluster heads.",
        "legend": ["bs", "head", "member", "membership", "fused"],
        "cols": 2,
        "panels": [
            (round_panel(HEADS_A, "clusters"),
             "<strong>Ένας γύρος.</strong> Τέσσερις κόμβοι είναι cluster heads. Κάθε άλλος κόμβος ανήκει στη "
             "συστάδα ενός από αυτούς, και οι κεφαλές στέλνουν απευθείας στη Base Station."),
            (round_panel(HEADS_B, "clusters"),
             "<strong>Ο επόμενος γύρος.</strong> Τον ρόλο παίρνουν άλλοι τέσσερις κόμβοι, και οι συστάδες "
             "σχηματίζονται ξανά γύρω τους (Διάλεξη 2, διαφάνεια 43)."),
        ],
    },
    "round": {
        "caption": "Σχήμα 2.2 · Ένας γύρος του LEACH βήμα προς βήμα.",
        "legend": ["bs", "active", "head", "advert", "join", "data", "fused"],
        "cols": 2,
        "panels": [
            (round_panel(HEADS_A, "elect"),
             "<strong>Εκλογή.</strong> Κάθε κόμβος που μπορεί να γίνει κεφαλή τραβά έναν τυχαίο αριθμό. "
             "Όσοι τραβήξουν αριθμό μικρότερο από το κατώφλι γίνονται cluster heads "
             "(Διάλεξη 2, διαφάνεια 45)."),
            (round_panel(HEADS_A, "advertise"),
             "<strong>Ανακοίνωση.</strong> Κάθε νέα κεφαλή εκπέμπει ένα advertisement σε όλους τους κόμβους "
             "(Διάλεξη 2, διαφάνεια 54)."),
            (round_panel(HEADS_A, "join"),
             "<strong>Σχηματισμός συστάδων.</strong> Κάθε κόμβος διαλέγει την κεφαλή με το ισχυρότερο σήμα και "
             "της ζητά να ενταχθεί. Η κεφαλή φτιάχνει ένα πρόγραμμα με τη σειρά που θα μιλά κάθε μέλος και το "
             "στέλνει πίσω (Διάλεξη 2, διαφάνειες 54 έως 55)."),
            (round_panel(HEADS_A, "steady"),
             "<strong>Μετάδοση.</strong> Κάθε μέλος στέλνει τα δεδομένα του στην κεφαλή, μόνο στη δική του σειρά. "
             "Η κεφαλή τα συμπιέζει και τα στέλνει απευθείας στη Base Station (Διάλεξη 2, διαφάνεια 56)."),
        ],
    },
    "era": {
        "caption": ("Σχήμα 2.3 · Μια ολόκληρη περίοδος με 70 κόμβους και "
                    r'<span class="arithmatex">\(P = \tfrac{1}{7}\)</span>'
                    ". Δείχνει τη μέση περίπτωση: στην πράξη ο αριθμός των κεφαλών κάθε γύρου αλλάζει λίγο, "
                    "επειδή η εκλογή είναι τυχαία."),
        "legend": ["head", "eligible", "served"],
        "cols": 4,
        "panels": [(era_panel(r), era_caption(r)) for r in range(8)],
    },
    "dead": {
        "caption": ("Σχήμα 2.4 · Πού πεθαίνουν οι κόμβοι. Σχηματική απεικόνιση όσων δείχνουν οι διαφάνειες "
                    "61 έως 63 της Διάλεξης 2, όχι τα πραγματικά δεδομένα της μέτρησης."),
        "legend": ["bs", "alive", "dead"],
        "cols": 3,
        "panels": [
            (dead_panel("mte"),
             "<strong>Minimum-Energy-Transmission</strong>, μετά από 180 γύρους: πεθαίνουν πρώτοι οι κόμβοι "
             "<em>κοντά</em> στη Base Station."),
            (dead_panel("direct"),
             "<strong>Direct Transmission</strong>, μετά από 180 γύρους: πεθαίνουν πρώτοι οι κόμβοι "
             "<em>μακριά</em> από τη Base Station."),
            (dead_panel("leach"),
             "<strong>LEACH</strong>, μετά από 1200 γύρους: οι κόμβοι πεθαίνουν ομοιόμορφα σε όλο το πεδίο."),
        ],
    },
}


def legend_html(keys):
    items = []
    for k in keys:
        label, swatch = LEGEND[k]
        items.append(f'<span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" '
                     f'aria-hidden="true">{swatch}</svg>{label}</span>')
    return '<div class="legend">' + "".join(items) + "</div>"


def figure_html(name):
    spec = FIGURES[name]
    cells = []
    for i, (panel, text) in enumerate(spec["panels"], start=1):
        cells.append('<div class="step">' + panel +
                     f'<p class="step__text"><span class="step__num">{i}</span>{text}</p></div>')
    cols = {2: "", 3: " steps--three", 4: " steps--four"}[spec["cols"]]
    number = re.search(r"Σχήμα (\d+)\.(\d+)", spec["caption"])
    fig_id = f' id="fig-{number.group(1)}-{number.group(2)}"' if number else ""
    return (f'<figure class="steps{cols}"{fig_id}>\n'
            f'<div class="steps__grid">{"".join(cells)}</div>\n'
            f'{legend_html(spec["legend"])}\n'
            f'<figcaption>{spec["caption"]}</figcaption>\n'
            '</figure>')


def marked(name):
    return "\n".join([f"<!-- leach_figures:{name} -->", figure_html(name), f"<!-- /leach_figures:{name} -->"])


def apply(chapter_path):
    path = Path(chapter_path)
    text = path.read_text(encoding="utf-8")
    for name in FIGURES:
        pattern = re.compile(r"<!-- leach_figures:" + re.escape(name) + r" -->.*?<!-- /leach_figures:"
                             + re.escape(name) + r" -->", re.DOTALL)
        found = pattern.findall(text)
        if len(found) != 1:
            raise SystemExit(f"{name}: expected exactly one marker pair, found {len(found)}")
        text = pattern.sub(lambda _m: marked(name), text)
    path.write_text(text, encoding="utf-8", newline="")
    print(f"applied {len(FIGURES)} figures to {path}")


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--apply":
        apply(sys.argv[2])
    else:
        print("usage: python tools/leach_figures.py --apply docs/chapters/02-leach.md")
