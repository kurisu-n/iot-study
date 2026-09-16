"""Figures for Chapter 3, the Energy Balance Protocol.

Same rules as tools/leach_figures.py and tools/dd_panels.py:
  - One fixed layout reused across panels.
  - No text inside any SVG; every label is HTML beneath the panel.
  - Every colour is a --fig-* token.

Colour meanings continue the corpus:
  blue square   the sink / Base Station
  grey circle   a live node
  red circle    an overused node (draining fast) or, in the energy figure, a dead one
  orange arrow  a data transmission (thin = one hop, thick = direct to the sink)

The network is drawn as vertical slices ("δακτύλιοι") of width R, the sink on
the left. Distance from the sink grows with the slice index i, so a direct
transmission from slice i costs about (iR)^2 while one hop costs about R^2, which
is exactly the energy model the chapter uses.

Run:  python tools/ebp_figures.py --apply docs/chapters/03-energy-balance.md
"""

import math
import random
import re
import sys
from pathlib import Path

VIEW_W, VIEW_H = 260, 190
SINK = (24, 95)
SINK_HALF = 11

# Five slices of width R, the sink just left of the first.
N_SLICES = 5
X0, SLICE_W = 60, 38
Y0, Y1 = 24, 170


def slice_of(x):
    return min(N_SLICES, max(1, int((x - X0) // SLICE_W) + 1))


def field_nodes(seed, count=26):
    rng = random.Random(seed)
    nodes, tries = [], 0
    x_max = X0 + N_SLICES * SLICE_W
    while len(nodes) < count and tries < 20000:
        tries += 1
        p = (rng.uniform(X0 + 4, x_max - 4), rng.uniform(Y0 + 6, Y1 - 6))
        if all(math.dist(p, q) >= 17 for q in nodes):
            nodes.append(p)
    return nodes


NODES = field_nodes(seed=11)
R_NODE = 6


# ---- Drawing --------------------------------------------------------------------

def slices_bg():
    parts = []
    for i in range(N_SLICES):
        x = X0 + i * SLICE_W
        fill = "var(--fig-surface-accent)" if i % 2 == 0 else "none"
        parts.append(f'<rect x="{x}" y="{Y0}" width="{SLICE_W}" height="{Y1 - Y0}" '
                     f'fill="{fill}" stroke="var(--fig-line)" stroke-width="0.8" '
                     f'stroke-dasharray="2 2"/>')
    return "".join(parts)


def sink():
    x, y = SINK
    return (f'<rect x="{x - SINK_HALF}" y="{y - SINK_HALF}" width="{2 * SINK_HALF}" '
            f'height="{2 * SINK_HALF}" rx="2" fill="var(--fig-accent)" '
            f'stroke="var(--fig-accent-deep)" stroke-width="1.8"/>')


def node(p, kind="live", cls="", style=""):
    attr = (f' class="{cls}"' if cls else "") + (f' style="{style}"' if style else "")
    if kind == "hot":
        return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_NODE + 0.5}" fill="var(--fig-event)" '
                f'stroke="var(--fig-event-deep)" stroke-width="1.6"{attr}/>')
    if kind == "dead":
        return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_NODE}" fill="none" '
                f'stroke="var(--fig-line)" stroke-width="1.6"{attr}/>')
    if kind == "dying":
        # Looks dead at rest (nearly hollow); the fig-die animation makes it fade
        # from full to this state, so with motion off it reads as a dead node.
        return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_NODE}" fill="var(--fig-node)" '
                f'fill-opacity="0.05" stroke="var(--fig-line)" stroke-width="1.6"{attr}/>')
    return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_NODE}" fill="var(--fig-node)" '
            f'stroke="var(--fig-line)" stroke-width="1.3"{attr}/>')


def arrow(p, q, stroke, width, r_from, r_to, dash=None, gap=3, cls=""):
    (x1, y1), (x2, y2) = p, q
    d = math.hypot(x2 - x1, y2 - y1)
    if d == 0:
        return ""
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    px, py = -uy, ux
    sx, sy = x1 + ux * (r_from + gap), y1 + uy * (r_from + gap)
    tx, ty = x2 - ux * (r_to + gap), y2 - uy * (r_to + gap)
    head, half = 6, 3.2
    hx, hy = tx - ux * head, ty - uy * head
    lx, ly = tx - ux * head * 0.8, ty - uy * head * 0.8
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    cls_attr = f' class="{cls}"' if cls else ""
    return (f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{lx:.1f}" y2="{ly:.1f}" stroke="{stroke}" '
            f'stroke-width="{width}"{dash_attr}{cls_attr} stroke-linecap="round"/>'
            f'<polygon points="{tx:.1f},{ty:.1f} {hx + px * half:.1f},{hy + py * half:.1f} '
            f'{hx - px * half:.1f},{hy - py * half:.1f}" fill="{stroke}"/>')


def halo(p, r=R_NODE):
    return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r + 5}" fill="none" '
            f'stroke="var(--fig-line)" stroke-width="2" stroke-dasharray="2.5 2"/>')


def svg(parts):
    return (f'<svg viewBox="0 0 {VIEW_W} {VIEW_H}" xmlns="http://www.w3.org/2000/svg" role="img">'
            + "".join(parts) + "</svg>")


# ---- Panels ---------------------------------------------------------------------

def strain_panel(kind):
    """kind: 'hop' overuses the slice nearest the sink; 'direct' overuses the far slice."""
    parts = [slices_bg(), sink()]
    if kind == "hop":
        hot = lambda p: slice_of(p[0]) == 1
    else:
        hot = lambda p: slice_of(p[0]) >= N_SLICES
    # A few representative transmissions, so the reader sees why those nodes drain.
    if kind == "hop":
        for i in [3, 9, 15, 20]:
            p = NODES[i]
            # a chain of one-hop steps leftwards toward the sink
            steps = int(slice_of(p[0]))
            cur = p
            for s in range(steps):
                nxt = (max(X0 + 2, cur[0] - SLICE_W), cur[1])
                tgt = SINK if s == steps - 1 else nxt
                parts.append(arrow(cur, tgt, "var(--fig-warn)", 1.4,
                                    R_NODE, SINK_HALF if tgt is SINK else R_NODE, cls="fig-flow"))
                cur = tgt
    else:
        for i in [6, 12, 18, 23]:
            parts.append(arrow(NODES[i], SINK, "var(--fig-warn)", 1.6, R_NODE, SINK_HALF, cls="fig-flow"))
    for p in NODES:
        parts.append(node(p, "hot" if hot(p) else "live", cls="fig-strain" if hot(p) else ""))
    return svg(parts)


def choice_panel(option):
    """option: 'hop' or 'direct' from one node in a far slice."""
    parts = [slices_bg(), sink()]
    src = NODES[23]  # a node out in slice 4/5
    # the neighbour one slice closer to the sink
    dst = min((q for q in NODES if slice_of(q[0]) == slice_of(src[0]) - 1),
              key=lambda q: abs(q[1] - src[1]), default=None)
    if option == "hop" and dst is not None:
        parts.append(arrow(src, dst, "var(--fig-warn)", 1.8, R_NODE, R_NODE, cls="fig-flow"))
    elif option == "direct":
        parts.append(arrow(src, SINK, "var(--fig-warn)", 3.0, R_NODE, SINK_HALF, cls="fig-flow"))
    for p in NODES:
        parts.append(node(p))
    parts.append(halo(src))
    if option == "hop" and dst is not None:
        parts.append(halo(dst))
    return svg(parts)


def energy_panel(kind):
    """kind: 'holes' drains the near-sink slice first; 'balanced' drains evenly.

    Dead nodes are drawn as "dying": they rest looking dead (nearly hollow), and
    the fig-die animation fades them from full to empty in an order set by their
    animation-delay. In 'holes' the delay grows with distance from the sink, so
    the near-sink nodes die first and the hole visibly opens; in 'balanced' the
    delay is a small jitter, so the scattered deaths happen almost together.
    """
    parts = [slices_bg(), sink()]
    rng = random.Random(3 if kind == "holes" else 7)
    for p in NODES:
        if kind == "holes":
            dead = slice_of(p[0]) == 1 or (slice_of(p[0]) == 2 and rng.random() < 0.4)
            delay = (slice_of(p[0]) - 1) * 0.7
        else:
            dead = rng.random() < 0.25
            delay = rng.uniform(0, 0.7)
        if dead:
            parts.append(node(p, "dying", cls="fig-die", style=f"animation-delay:{delay:.2f}s"))
        else:
            parts.append(node(p, "live"))
    return svg(parts)


# ---- Figures --------------------------------------------------------------------

LEGEND = {
    "sink": ("σταθμός βάσης (Base Station)",
             '<rect x="3" y="1" width="12" height="12" rx="1.5" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.5"/>'),
    "live": ("ζωντανός κόμβος",
             '<circle cx="9" cy="7" r="5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.2"/>'),
    "hot": ("κόμβος που αδειάζει γρήγορα",
            '<circle cx="9" cy="7" r="5.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.5"/>'),
    "dead": ("κόμβος που εξαντλήθηκε",
             '<circle cx="9" cy="7" r="5" fill="none" stroke="var(--fig-line)" stroke-width="1.6"/>'),
    "data": ("μία μετάδοση (ένα βήμα)",
             '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="1.6"/>'),
    "direct": ("απευθείας μετάδοση στη Base Station",
               '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="3"/>'),
    "slice": ("δακτύλιος πλάτους R",
              '<rect x="2" y="1" width="14" height="12" fill="var(--fig-surface-accent)" stroke="var(--fig-line)" stroke-width="0.8" stroke-dasharray="2 2"/>'),
    "active": ("ο κόμβος που αποφασίζει",
               '<circle cx="9" cy="7" r="5.5" fill="none" stroke="var(--fig-line)" stroke-width="1.8" stroke-dasharray="2 1.6"/>'),
}

FIGURES = {
    "strain": {
        "caption": "Σχήμα 3.1 · Κάθε απλό σχήμα στραγγίζει κάποιους κόμβους. Σχηματική απεικόνιση της Διάλεξης 3, διαφάνεια 4.",
        "legend": ["sink", "live", "hot", "data", "direct"],
        "cols": 2,
        "panels": [
            (strain_panel("hop"),
             "<strong>Βήμα προς βήμα.</strong> Όλα τα μηνύματα περνούν από τους κόμβους κοντά στη Base "
             "Station, οπότε αυτοί αδειάζουν πρώτοι, ακόμη κι αν κάθε βήμα είναι φθηνό."),
            (strain_panel("direct"),
             "<strong>Απευθείας.</strong> Κάθε κόμβος στέλνει μόνος του ως τη Base Station. Οι μακρινοί "
             "κόμβοι πληρώνουν το ακριβό κόστος της απόστασης και αδειάζουν πρώτοι."),
        ],
    },
    "choice": {
        "caption": "Σχήμα 3.2 · Η επιλογή κάθε κόμβου στο Energy Balance Protocol (Διάλεξη 3, διαφάνειες 7 έως 9).",
        "legend": ["sink", "slice", "active", "live", "data", "direct"],
        "cols": 2,
        "panels": [
            (choice_panel("hop"),
             "<strong>Με πιθανότητα p<sub>i</sub>:</strong> ο κόμβος περνά το μήνυμα έναν δακτύλιο πιο "
             "κοντά στη Base Station. Ένα φθηνό βήμα μήκους R."),
            (choice_panel("direct"),
             "<strong>Με πιθανότητα 1 − p<sub>i</sub>:</strong> ο κόμβος στέλνει το μήνυμα απευθείας στη "
             "Base Station, πληρώνοντας το ακριβό κόστος της απόστασης, αλλά ξεφορτώνοντας τους κόμβους "
             "μπροστά του."),
        ],
    },
    "energy": {
        "caption": "Σχήμα 3.3 · Πού τελειώνει πρώτα η ενέργεια. Σχηματική σύγκριση, όχι πραγματικά δεδομένα μέτρησης.",
        "legend": ["sink", "live", "dead", "slice"],
        "cols": 2,
        "panels": [
            (energy_panel("holes"),
             "<strong>Παραδοσιακό σχήμα.</strong> Οι κόμβοι κοντά στη Base Station εξαντλούνται πρώτοι και "
             "ανοίγει μια «ενεργειακή τρύπα»: το δίκτυο αποκόπτεται ενώ οι μακρινοί κόμβοι έχουν ακόμη "
             "μπαταρία (χειρόγραφες σημειώσεις, σελίδες 15 έως 16)."),
            (energy_panel("balanced"),
             "<strong>Energy Balance Protocol.</strong> Η ενέργεια πέφτει ομοιόμορφα σε όλο το πεδίο, ώστε "
             "το δίκτυο να αξιοποιεί σχεδόν όλη τη διαθέσιμη ενέργεια πριν σταματήσει να λειτουργεί."),
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
    return "\n".join([f"<!-- ebp_figures:{name} -->", figure_html(name), f"<!-- /ebp_figures:{name} -->"])


def apply(chapter_path):
    path = Path(chapter_path)
    text = path.read_text(encoding="utf-8")
    for name in FIGURES:
        pattern = re.compile(r"<!-- ebp_figures:" + re.escape(name) + r" -->.*?<!-- /ebp_figures:"
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
        print("usage: python tools/ebp_figures.py --apply docs/chapters/03-energy-balance.md")
