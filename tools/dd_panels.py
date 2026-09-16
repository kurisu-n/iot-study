"""Generates the step-by-step Directed Diffusion panels for Chapter 1.

WHY A GENERATOR. The phase walkthroughs use twenty-two small panels, and they only
teach if they are the SAME network every time: the reader follows node A through
interests, gradients, data and reinforcement, and any drift in position between
panels reads as a different network. Drawing them by hand invites that drift.

WHAT IT EMITS. One HTML fragment per figure, written to the output directory,
ready to paste into the chapter where its @@PANELS:name@@ placeholder sits. Each
fragment is a <figure class="steps"> holding a grid of panels. Every panel is an
SVG plus an HTML caption.

⛔ TEXT RULE. The only text inside an SVG is a node's name, placed in clear space
beside the node. Everything explanatory lives in the HTML caption under the
panel. That keeps text off every shape by construction, which is the rule
tools/figure-audit.js enforces (Chris, 2026-09-16: never overlap text with
elements). Re-run the audit after changing any coordinate here.

⛔ COLOUR RULE. Every colour is a --fig-* token from docs/stylesheets/corpus.css.
The deploy workflow fails the build on a literal hex in a chapter.

Arrowheads are drawn as real polygons, not SVG markers. A marker needs an id,
ids must be unique across the whole page, and twenty-two panels would otherwise
either collide or need a shared hidden <defs> that some browsers will not render
from. Polygons have neither problem, and the audit can see them.

Run, to rewrite the figures inside a chapter in place:
    python tools/dd_panels.py --apply docs/chapters/01-data-propagation.md

Each generated figure sits in the chapter between two comment markers,
<!-- dd_panels:NAME --> and <!-- /dd_panels:NAME -->, and --apply replaces only
what lies between them. That is what keeps the generator and the chapter from
drifting: edit a panel HERE, re-apply, and the chapter follows. Never hand-edit
between the markers; the next apply overwrites it.

Or, to write each figure to its own file for inspection:
    python tools/dd_panels.py <output-dir>
"""

import math
import sys
from pathlib import Path


# ---- The network --------------------------------------------------------
#
# One topology for every panel. Two disjoint routes from Source to Sink
# (S-C-A-K and S-D-B-K) plus two cross links (A-B, C-D), which is the smallest
# shape that still shows multiple exploratory paths, a choice to reinforce, and
# an alternative for local repair.

VIEW_W, VIEW_H = 260, 170

NODES = {
    "K": (34, 85),    # Sink
    "A": (100, 38),
    "B": (100, 132),
    "C": (170, 38),
    "D": (170, 132),
    "S": (236, 85),   # Source
}

LINKS = [("K", "A"), ("K", "B"), ("A", "B"), ("A", "C"),
         ("B", "D"), ("C", "D"), ("C", "S"), ("D", "S")]

NODE_R = {"K": 11, "S": 11}
DEFAULT_R = 9

# Name positions. Chosen so every name sits in clear space: top-row names above
# their node, bottom-row names below, Sink and Source below and slightly clear of
# the links that leave them diagonally. Checked by tools/figure-audit.js.
LABELS = {
    "K": ("Sink", 34, 119),
    "S": ("Source", 236, 119),
    "A": ("A", 100, 18),
    "C": ("C", 170, 18),
    "B": ("B", 100, 159),
    "D": ("D", 170, 159),
}

# ---- Styles ---------------------------------------------------------------
#
# Hue says WHAT a line is, weight says HOW STRONG. An interest and a
# reinforcement are both interests, so they share the accent hue; a gradient is
# green whether exploratory or reinforced, and only its weight changes.

STYLES = {
    "interest":  dict(stroke="var(--fig-accent)",      width=1.6, dash="3 2"),
    "reinforce": dict(stroke="var(--fig-accent-deep)", width=2.4, dash=None),
    "grad":      dict(stroke="var(--fig-ok)",          width=1.4, dash="4 3"),
    "grad-strong": dict(stroke="var(--fig-ok)",        width=3.2, dash=None),
    "data":      dict(stroke="var(--fig-warn)",        width=2.0, dash=None),
    "degraded":  dict(stroke="var(--fig-warn)",        width=3.2, dash="5 3"),
}

OFFSET = 3.8   # perpendicular offset, so two directions on one link stay apart
GAP = 3.5      # clearance between an arrow's ends and the node edge
HEAD_LEN, HEAD_HALF = 6.5, 3.4


def r_of(n):
    return NODE_R.get(n, DEFAULT_R)


def arrow(a, b, style, offset_sign=0):
    """An arrow from node a to node b, trimmed to the node edges.

    offset_sign shifts the arrow sideways so that a->b and b->a on the same link
    are drawn as two parallel arrows rather than one on top of the other.
    """
    (x1, y1), (x2, y2) = NODES[a], NODES[b]
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    ox, oy = px * OFFSET * offset_sign, py * OFFSET * offset_sign

    sx = x1 + ux * (r_of(a) + GAP) + ox
    sy = y1 + uy * (r_of(a) + GAP) + oy
    tx = x2 - ux * (r_of(b) + GAP) + ox
    ty = y2 - uy * (r_of(b) + GAP) + oy

    st = STYLES[style]
    # The line stops where the head begins, so a thick dashed line never pokes
    # through the tip of its own arrowhead.
    lx, ly = tx - ux * HEAD_LEN * 0.8, ty - uy * HEAD_LEN * 0.8
    dash = f' stroke-dasharray="{st["dash"]}"' if st["dash"] else ""
    line = (f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" '
            f'stroke="{st["stroke"]}" stroke-width="{st["width"]}"{dash} stroke-linecap="round"/>')

    hx, hy = tx - ux * HEAD_LEN, ty - uy * HEAD_LEN
    head = (f'<polygon points="{tx:.1f},{ty:.1f} '
            f'{hx + px * HEAD_HALF:.1f},{hy + py * HEAD_HALF:.1f} '
            f'{hx - px * HEAD_HALF:.1f},{hy - py * HEAD_HALF:.1f}" '
            f'fill="{st["stroke"]}"/>')
    return line + head


def cross(cx, cy, size=4.5, stroke="var(--fig-event)"):
    """A drop mark: a small X, drawn beside a node rather than on it."""
    return (f'<line x1="{cx - size:.1f}" y1="{cy - size:.1f}" x2="{cx + size:.1f}" y2="{cy + size:.1f}" '
            f'stroke="{stroke}" stroke-width="2.2" stroke-linecap="round"/>'
            f'<line x1="{cx - size:.1f}" y1="{cy + size:.1f}" x2="{cx + size:.1f}" y2="{cy - size:.1f}" '
            f'stroke="{stroke}" stroke-width="2.2" stroke-linecap="round"/>')


def panel_svg(p):
    """One panel. p is a dict describing what this step shows."""
    out = [f'<svg viewBox="0 0 {VIEW_W} {VIEW_H}" xmlns="http://www.w3.org/2000/svg" role="img">']

    # 1. The neighbour links, as quiet context. Quiet by WEIGHT, not by colour:
    #    they were --fig-node-soft until 2026-09-16, which measured 1.49:1 on the
    #    Academic page and left the network's shape barely visible. --fig-node
    #    clears 3:1 in every scheme, and a 1px stroke still reads as background
    #    beside the coloured arrows drawn over it.
    for a, b in LINKS:
        (x1, y1), (x2, y2) = NODES[a], NODES[b]
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                   f'stroke="var(--fig-node)" stroke-width="1"/>')

    # 2. Arrows. Each entry is (from, to, style) or (from, to, style, offset).
    for spec in p.get("arrows", []):
        a, b, style = spec[0], spec[1], spec[2]
        sign = spec[3] if len(spec) > 3 else 0
        out.append(arrow(a, b, style, sign))

    # 3. Halos on the nodes this step is about. A dotted ring in the neutral
    #    line colour, deliberately sharing a hue with NO arrow type: it was
    #    --fig-warn until 2026-09-16, the same colour as a data message, so an
    #    active node and a message arriving at it read as one thing.
    for n in p.get("active", []):
        x, y = NODES[n]
        out.append(f'<circle cx="{x}" cy="{y}" r="{r_of(n) + 5}" fill="none" '
                   f'stroke="var(--fig-line)" stroke-width="2" stroke-dasharray="2.5 2"/>')

    # 4. Nodes.
    for n, (x, y) in NODES.items():
        if n == "K":
            fill, stroke = "var(--fig-accent)", "var(--fig-accent-deep)"
        elif n == "S":
            fill, stroke = "var(--fig-event)", "var(--fig-event-deep)"
        else:
            fill, stroke = "var(--fig-node)", "var(--fig-line)"
        out.append(f'<circle cx="{x}" cy="{y}" r="{r_of(n)}" fill="{fill}" '
                   f'stroke="{stroke}" stroke-width="1.8"/>')

    # 5. Drop marks, placed up and to the right of the node, clear of its links.
    for n in p.get("drops", []):
        x, y = NODES[n]
        out.append(cross(x + 15, y - 15))

    # 6. Names, in clear space.
    for n, (text, lx, ly) in LABELS.items():
        weight = ' font-weight="bold"' if n in ("K", "S") else ""
        out.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" font-size="11"{weight} '
                   f'fill="var(--fig-label)">{text}</text>')

    out.append("</svg>")
    return "".join(out)


# Every link in both directions, the state after gradients are set up.
ALL_GRADIENTS = []
for _a, _b in LINKS:
    ALL_GRADIENTS.append((_a, _b, "grad", 1))
    ALL_GRADIENTS.append((_b, _a, "grad", 1))


# ---- The figures ----------------------------------------------------------
#
# Captions are HTML, in the corpus's voice: Greek prose, English terms, a slide
# reference where the step comes straight from the lecture. (Δ2, διαφ. N) means
# Lecture 2, slide N.

FIGURES = {
    "overview": {
        "legend": ["sink", "source", "interest", "grad", "grad-strong"],
        "panels": [
            dict(arrows=[("K", "A", "interest"), ("K", "B", "interest"),
                         ("A", "C", "interest"), ("B", "D", "interest"),
                         ("C", "S", "interest"), ("D", "S", "interest")],
                 caption="<strong>Διάδοση ενδιαφέροντος.</strong> Ο Sink διαχέει το interest σε όλο το δίκτυο."),
            dict(arrows=ALL_GRADIENTS,
                 caption="<strong>Αρχικά gradients.</strong> Κάθε ζεύξη αποκτά gradients και προς τις δύο κατευθύνσεις."),
            dict(arrows=[("S", "C", "grad-strong"), ("C", "A", "grad-strong"),
                         ("A", "K", "grad-strong")],
                 caption="<strong>Παράδοση δεδομένων.</strong> Τα δεδομένα ρέουν στο ενισχυμένο μονοπάτι."),
        ],
    },

    "phase1": {
        "legend": ["sink", "source", "active", "interest"],
        "panels": [
            dict(active=["K"],
                 arrows=[("K", "A", "interest"), ("K", "B", "interest")],
                 caption="Ο Sink δημιουργεί ένα <em>task</em> και στέλνει στους γείτονές του ένα "
                         "<strong>exploratory interest</strong> με <code>interval = 100 ms</code> (Δ2, διαφ. 10)."),
            dict(active=["A", "B"],
                 arrows=[("K", "A", "interest"), ("K", "B", "interest"),
                         ("A", "C", "interest"), ("B", "D", "interest"),
                         ("A", "B", "interest", 1), ("B", "A", "interest", 1)],
                 caption="Οι A και B καταχωρούν το interest στο <strong>interest cache</strong> μαζί με "
                         "ένα timestamp και το αναμεταδίδουν σε όλους τους γείτονές τους (Δ2, διαφ. 11)."),
            dict(active=["C"],
                 arrows=[("A", "C", "interest"), ("D", "C", "interest", 1),
                         ("C", "D", "interest", 1)],
                 caption="Ο C λαμβάνει το <em>ίδιο</em> interest από τον A και από τον D. "
                         "Η δεύτερη λήψη δεν δημιουργεί νέα εγγραφή στο cache (Δ2, διαφ. 11)."),
            dict(active=["S"],
                 arrows=[("C", "S", "interest"), ("D", "S", "interest")],
                 caption="Το interest φτάνει στη Source. Δεν περιέχει καμία πληροφορία για τον Sink, "
                         "και ο Sink το ανανεώνει περιοδικά μέχρι το <code>expiresAt</code> (Δ2, διαφ. 10)."),
        ],
    },

    "phase2": {
        "legend": ["sink", "source", "active", "interest", "grad"],
        "panels": [
            dict(active=["A"],
                 arrows=[("K", "A", "interest", 1), ("A", "K", "grad", 1)],
                 caption="Ο A λαμβάνει το interest από τον Sink και δημιουργεί <strong>gradient</strong> "
                         "προς αυτόν, που αποθηκεύει <em>data rate</em> και <em>duration</em> (Δ2, διαφ. 11)."),
            dict(active=["A"],
                 arrows=[("A", "K", "grad", 1), ("B", "A", "interest", 1), ("A", "B", "grad", 1)],
                 caption="Ο A λαμβάνει το ίδιο interest και από τον B. Αφού υπάρχει ήδη στο cache, "
                         "προστίθεται <em>μόνο</em> νέο gradient, ένα ανά γείτονα (Δ2, διαφ. 11)."),
            dict(active=[],
                 arrows=ALL_GRADIENTS,
                 caption="Κάθε κόμβος κάνει το ίδιο, άρα οι γείτονες δημιουργούν gradients "
                         "<strong>ο ένας προς τον άλλον</strong> (Δ2, διαφ. 12)."),
            dict(active=["S"],
                 arrows=[("S", "C", "grad"), ("C", "A", "grad"), ("A", "K", "grad"),
                         ("S", "D", "grad"), ("D", "B", "grad"), ("B", "K", "grad")],
                 caption="Από τη Source υπάρχουν πλέον <strong>πολλά μονοπάτια</strong> προς τον Sink, "
                         "όλα με χαμηλό, διερευνητικό ρυθμό. Δύο από αυτά φαίνονται εδώ."),
        ],
    },

    "phase3": {
        "legend": ["sink", "source", "active", "grad", "data", "drop"],
        "panels": [
            dict(active=["S"],
                 arrows=[("S", "C", "grad"), ("S", "D", "grad")],
                 caption="Η Source ανιχνεύει γεγονός που ταιριάζει με το interest. Διαλέγει τον "
                         "<strong>υψηλότερο</strong> ρυθμό που ζητούν τα gradients της και παράγει δείγματα "
                         "σε αυτόν (Δ2, διαφ. 13)."),
            dict(active=["S"],
                 arrows=[("S", "C", "data"), ("S", "D", "data")],
                 caption="Στέλνει κάθε data message ως <strong>unicast</strong> σε κάθε γείτονα όπου "
                         "δείχνει gradient, εδώ στους C και D (Δ2, διαφ. 13)."),
            dict(active=["D"],
                 arrows=[("C", "A", "data"), ("D", "B", "data"), ("C", "D", "data")],
                 drops=["D"],
                 caption="Κάθε κόμβος ελέγχει το <strong>data cache</strong>. Ο D παίρνει από τον C μήνυμα "
                         "που έχει ήδη από τη Source, και το <em>απορρίπτει</em>. Ό,τι είναι νέο αποθηκεύεται "
                         "και προωθείται (Δ2, διαφ. 14)."),
            dict(active=["K"],
                 arrows=[("A", "K", "data"), ("B", "K", "data")],
                 caption="Τα διερευνητικά δεδομένα φτάνουν στον Sink από δύο μονοπάτια. Όπου ένα gradient "
                         "ζητά χαμηλότερο ρυθμό από τον εισερχόμενο, ο κόμβος κάνει "
                         "<strong>down-conversion</strong> πριν προωθήσει (Δ2, διαφ. 14)."),
        ],
    },

    "phase4": {
        "legend": ["sink", "source", "active", "grad", "data", "reinforce", "grad-strong"],
        "panels": [
            dict(active=["K"],
                 arrows=[("A", "K", "data"), ("B", "K", "data")],
                 caption="Ο Sink λαμβάνει το ίδιο διερευνητικό γεγονός <strong>πρώτα από τον A</strong> "
                         "και αργότερα από τον B."),
            dict(active=["A"],
                 arrows=[("K", "A", "reinforce", 1), ("A", "K", "grad-strong", 1)],
                 caption="Ο Sink <strong>ενισχύει</strong> τον A: του ξαναστέλνει το ίδιο interest με "
                         "<code>interval = 10 ms</code> αντί για 100 ms. Ο A αναβαθμίζει το gradient του "
                         "προς τον Sink (Δ2, διαφ. 16)."),
            dict(active=["C"],
                 arrows=[("A", "K", "grad-strong"),
                         ("A", "C", "reinforce", 1), ("C", "A", "grad-strong", 1),
                         ("C", "S", "reinforce", 1), ("S", "C", "grad-strong", 1)],
                 caption="Ο ζητούμενος ρυθμός είναι πλέον <em>υψηλότερος</em> από αυτόν που δέχεται ο A, "
                         "οπότε ενισχύει κι εκείνος τον γείτονα που του έφερε πρώτος το γεγονός, τον C, "
                         "κι ο C τη Source (Δ2, διαφ. 16–17)."),
            dict(active=[],
                 arrows=[("S", "C", "grad-strong"), ("C", "A", "grad-strong"), ("A", "K", "grad-strong"),
                         ("S", "D", "grad"), ("D", "B", "grad"), ("B", "K", "grad")],
                 caption="Τα δεδομένα ρέουν με υψηλό ρυθμό στο <strong>ενισχυμένο μονοπάτι</strong>. "
                         "Τα διερευνητικά gradients λήγουν όσο δεν ανανεώνονται (Δ2, διαφ. 20)."),
        ],
    },

    "repair": {
        "legend": ["sink", "source", "active", "grad", "grad-strong", "degraded", "reinforce", "interest"],
        "panels": [
            dict(active=["A"],
                 arrows=[("S", "C", "grad-strong"), ("C", "A", "degraded"), ("A", "K", "grad-strong")],
                 caption="Η ζεύξη C → A <strong>υποβαθμίζεται</strong>. Ο A το αντιλαμβάνεται επειδή "
                         "τα γεγονότα από τον C φτάνουν πιο αραιά (Δ2, διαφ. 19)."),
            dict(active=["A"],
                 arrows=[("S", "C", "grad-strong"), ("C", "A", "degraded"), ("A", "K", "grad-strong"),
                         ("A", "B", "reinforce", 1), ("B", "D", "reinforce", 1), ("D", "S", "reinforce", 1),
                         ("S", "D", "grad-strong", 1), ("D", "B", "grad-strong", 1), ("B", "A", "grad-strong", 1)],
                 caption="Ο A εφαρμόζει <strong>τοπικά</strong> τους ίδιους κανόνες ενίσχυσης: ενισχύει "
                         "τον B, και η ενίσχυση ταξιδεύει μέσω D ως τη Source (Δ2, διαφ. 19)."),
            dict(active=["C"],
                 arrows=[("S", "D", "grad-strong"), ("D", "B", "grad-strong"), ("B", "A", "grad-strong"),
                         ("A", "K", "grad-strong"),
                         ("A", "C", "interest", 1), ("C", "S", "interest", 1),
                         ("C", "A", "grad", 1), ("S", "C", "grad", 1)],
                 caption="<strong>Αρνητική ενίσχυση:</strong> ο A στέλνει στον C interest με διερευνητικό "
                         "ρυθμό. Όλα τα εξερχόμενα gradients του C είναι πλέον διερευνητικά, άρα ενισχύει "
                         "αρνητικά τη Source, και το παλιό μονοπάτι αποκόπτεται (Δ2, διαφ. 20)."),
        ],
    },
}


# ---- Legend ---------------------------------------------------------------

LEGEND_ITEMS = {
    "sink": ("Sink",
             '<circle cx="9" cy="7" r="5.5" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.5"/>'),
    "source": ("Source",
               '<circle cx="9" cy="7" r="5.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.5"/>'),
    "active": ("κόμβος του βήματος",
               '<circle cx="9" cy="7" r="5.5" fill="none" stroke="var(--fig-line)" stroke-width="1.8" stroke-dasharray="2 1.6"/>'),
    "interest": ("interest",
                 '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-accent)" stroke-width="1.6" stroke-dasharray="3 2"/>'),
    "reinforce": ("ενίσχυση (interest υψηλού ρυθμού)",
                  '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-accent-deep)" stroke-width="2.4"/>'),
    "grad": ("διερευνητικό gradient",
             '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-ok)" stroke-width="1.4" stroke-dasharray="4 3"/>'),
    "grad-strong": ("data gradient (ενισχυμένο)",
                    '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-ok)" stroke-width="3.2"/>'),
    "data": ("data message",
             '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="2"/>'),
    "degraded": ("υποβαθμισμένη ζεύξη",
                 '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="3.2" stroke-dasharray="5 3"/>'),
    "drop": ("απόρριψη διπλότυπου",
             '<line x1="5" y1="3" x2="13" y2="11" stroke="var(--fig-event)" stroke-width="2.2" stroke-linecap="round"/>'
             '<line x1="5" y1="11" x2="13" y2="3" stroke="var(--fig-event)" stroke-width="2.2" stroke-linecap="round"/>'),
}


def legend_html(keys):
    items = []
    for k in keys:
        label, swatch = LEGEND_ITEMS[k]
        items.append(f'<span class="legend__item"><svg class="legend__swatch" viewBox="0 0 18 14" '
                     f'aria-hidden="true">{swatch}</svg>{label}</span>')
    return '<div class="legend">' + "".join(items) + "</div>"


def figure_html(name, caption):
    spec = FIGURES[name]
    cells = []
    for i, p in enumerate(spec["panels"], start=1):
        cells.append(
            '<div class="step">'
            f'{panel_svg(p)}'
            f'<p class="step__text"><span class="step__num">{i}</span>{p["caption"]}</p>'
            '</div>'
        )
    cols = " steps--three" if len(spec["panels"]) == 3 else ""
    return (f'<figure class="steps{cols}">\n'
            f'<div class="steps__grid">{"".join(cells)}</div>\n'
            f'{legend_html(spec["legend"])}\n'
            f'<figcaption>{caption}</figcaption>\n'
            '</figure>')


CAPTIONS = {
    "overview": "Σχήμα 1.3 · Το Directed Diffusion με μια ματιά, όπως στη διαφάνεια 22 της Διάλεξης 2.",
    "phase1": "Σχήμα 1.4 · Φάση 1, διάδοση ενδιαφέροντος, βήμα προς βήμα.",
    "phase2": "Σχήμα 1.5 · Φάση 2, δημιουργία gradients, βήμα προς βήμα.",
    "phase3": "Σχήμα 1.6 · Φάση 3, διάδοση δεδομένων, βήμα προς βήμα.",
    "phase4": "Σχήμα 1.7 · Φάση 4, ενίσχυση, βήμα προς βήμα.",
    "repair": "Σχήμα 1.8 · Τοπική επισκευή και αρνητική ενίσχυση.",
}


def marked(name):
    """A figure wrapped in the markers --apply looks for."""
    return "\n".join([
        f"<!-- dd_panels:{name} -->",
        figure_html(name, CAPTIONS[name]),
        f"<!-- /dd_panels:{name} -->",
    ])


def apply(chapter_path):
    """Rewrites every marked figure in a chapter. Fails loudly on a missing pair,
    rather than silently leaving a figure stale."""
    import re
    path = Path(chapter_path)
    text = path.read_text(encoding="utf-8")
    for name in FIGURES:
        pattern = re.compile(
            r"<!-- dd_panels:" + re.escape(name) + r" -->.*?<!-- /dd_panels:" + re.escape(name) + r" -->",
            re.DOTALL)
        found = pattern.findall(text)
        if len(found) != 1:
            raise SystemExit(f"{name}: expected exactly one marker pair, found {len(found)}")
        text = pattern.sub(lambda _m: marked(name), text)
    # newline="" writes the text exactly as it is. Without it Python on Windows
    # turns every \n into \r\n, so an apply that changed no figure still
    # rewrote all 452 lines of the chapter (measured 2026-09-16).
    path.write_text(text, encoding="utf-8", newline="")
    print(f"applied {len(FIGURES)} figures to {path}")


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--apply":
        apply(sys.argv[2])
        return
    out_dir = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in FIGURES:
        path = out_dir / f"panels_{name}.html"
        path.write_text(marked(name), encoding="utf-8", newline="")
        print(f"wrote {path}  ({len(FIGURES[name]['panels'])} panels)")


if __name__ == "__main__":
    main()
