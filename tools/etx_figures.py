"""Figures for Chapter 4, routing metrics and the Expected Transmission Count.

Same rules as the other generators (tools/ebp_figures.py, tools/leach_figures.py):
one fixed layout, no text inside any SVG (labels are HTML beneath the panel),
every colour a --fig-* token, and figures rewritten in place between markers.

The traveling-packet animation (fig-packet, an offset-path circle) is shared with
the other chapters through corpus.css section 19.

Run:  python tools/etx_figures.py --apply docs/chapters/04-routing-metrics.md
"""

import math
import re
import sys
from pathlib import Path

VIEW_W, VIEW_H = 260, 180
R_NODE = 6.5
SINK_HALF = 10


def node(p, kind="live"):
    if kind == "source":
        return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_NODE + 1}" fill="var(--fig-event)" '
                f'stroke="var(--fig-event-deep)" stroke-width="1.8"/>')
    return (f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{R_NODE}" fill="var(--fig-node)" '
            f'stroke="var(--fig-line)" stroke-width="1.4"/>')


def sink(p):
    x, y = p
    return (f'<rect x="{x - SINK_HALF:.1f}" y="{y - SINK_HALF:.1f}" width="{2 * SINK_HALF}" '
            f'height="{2 * SINK_HALF}" rx="2" fill="var(--fig-accent)" '
            f'stroke="var(--fig-accent-deep)" stroke-width="1.8"/>')


def link(p, q, stroke, width, r_from, r_to, dash=None):
    (x1, y1), (x2, y2) = p, q
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    sx, sy = x1 + ux * r_from, y1 + uy * r_from
    tx, ty = x2 - ux * r_to, y2 - uy * r_to
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" stroke="{stroke}" '
            f'stroke-width="{width}"{dash_attr} stroke-linecap="round"/>')


def arrowhead(p, q, stroke, r_to):
    (x1, y1), (x2, y2) = p, q
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    px, py = -uy, ux
    tx, ty = x2 - ux * r_to, y2 - uy * r_to
    hx, hy = tx - ux * 6, ty - uy * 6
    return (f'<polygon points="{tx:.1f},{ty:.1f} {hx + px * 3.2:.1f},{hy + py * 3.2:.1f} '
            f'{hx - px * 3.2:.1f},{hy - py * 3.2:.1f}" fill="{stroke}"/>')


def packet(pts, delay=0.0):
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    style = f"offset-path: path('{d}'); offset-rotate: 0deg;"
    if delay:
        style += f" animation-delay: {delay:.2f}s;"
    return (f'<circle r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1" '
            f'class="fig-packet" style="{style}"/>')


def svg(parts):
    return (f'<svg viewBox="0 0 {VIEW_W} {VIEW_H}" xmlns="http://www.w3.org/2000/svg" role="img">'
            + "".join(parts) + "</svg>")


# ---- The three-route example (Lecture 4, slide 9) --------------------------------

A, B = (30, 90), (230, 90)
C, D, E = (78, 44), (130, 36), (182, 44)
F = (130, 148)


def route_panel(which):
    parts = []
    if which == "direct":
        pts = [A, B]
        parts.append(link(A, B, "var(--fig-warn)", 2, R_NODE, SINK_HALF, dash="5 4"))
        parts.append(arrowhead(A, B, "var(--fig-warn)", SINK_HALF))
    elif which == "cde":
        chain = [A, C, D, E, B]
        pts = chain
        for i in range(len(chain) - 1):
            r_to = SINK_HALF if i == len(chain) - 2 else R_NODE
            parts.append(link(chain[i], chain[i + 1], "var(--fig-warn)", 1.6, R_NODE, r_to))
            parts.append(arrowhead(chain[i], chain[i + 1], "var(--fig-warn)", r_to))
    else:  # f, the winner
        chain = [A, F, B]
        pts = chain
        for i in range(len(chain) - 1):
            r_to = SINK_HALF if i == len(chain) - 2 else R_NODE
            parts.append(link(chain[i], chain[i + 1], "var(--fig-ok)", 2.6, R_NODE, r_to))
            parts.append(arrowhead(chain[i], chain[i + 1], "var(--fig-ok)", r_to))
    # all intermediate nodes drawn faint so every panel shares the same map
    for q in (C, D, E, F):
        parts.append(node(q))
    parts.append(node(A, "source"))
    parts.append(sink(B))
    parts.append(packet(pts))
    return svg(parts)


# ---- The two-hop topology of exam Theme D.1 -------------------------------------

HA, HB, HC = (34, 90), (130, 90), (226, 90)


def hops_panel():
    parts = []
    parts.append(link(HA, HB, "var(--fig-warn)", 2, R_NODE, R_NODE))
    parts.append(arrowhead(HA, HB, "var(--fig-warn)", R_NODE))
    parts.append(link(HB, HC, "var(--fig-warn)", 2, R_NODE, SINK_HALF))
    parts.append(arrowhead(HB, HC, "var(--fig-warn)", SINK_HALF))
    parts.append(node(HA, "source"))
    parts.append(node(HB))
    parts.append(sink(HC))
    parts.append(packet([HA, HB, HC]))
    return svg(parts)


LEGEND = {
    "source": ("κόμβος-πηγή", '<circle cx="9" cy="7" r="5.5" fill="var(--fig-event)" stroke="var(--fig-event-deep)" stroke-width="1.5"/>'),
    "node": ("ενδιάμεσος κόμβος", '<circle cx="9" cy="7" r="5" fill="var(--fig-node)" stroke="var(--fig-line)" stroke-width="1.2"/>'),
    "dest": ("προορισμός", '<rect x="3" y="1" width="12" height="12" rx="1.5" fill="var(--fig-accent)" stroke="var(--fig-accent-deep)" stroke-width="1.5"/>'),
    "route": ("ζεύξη της διαδρομής", '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="1.8"/>'),
    "win": ("η διαδρομή που διαλέγει το ETX", '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-ok)" stroke-width="2.6"/>'),
    "bad": ("ζεύξη χαμηλής ποιότητας", '<line x1="1" y1="7" x2="17" y2="7" stroke="var(--fig-warn)" stroke-width="2" stroke-dasharray="5 4"/>'),
    "packet": ("πακέτο", '<circle cx="9" cy="7" r="3.4" fill="var(--fig-warn)" stroke="var(--fig-node)" stroke-width="1"/>'),
}

FIGURES = {
    "routes": {
        "caption": "Σχήμα 4.1 · Τρεις διαδρομές από το A στο B, και ποια διαλέγει το Expected Transmission Count (ETX). Διάλεξη 4, διαφάνεια 9.",
        "legend": ["source", "node", "dest", "bad", "route", "win", "packet"],
        "cols": 3,
        "panels": [
            (route_panel("direct"),
             "<strong>Απευθείας.</strong> Μία μόνο ζεύξη, αλλά χαμηλής ποιότητας 0.1. Χρειάζονται κατά μέσο "
             "όρο 1 / 0.1 = <strong>10</strong> μεταδόσεις."),
            (route_panel("cde"),
             "<strong>Μέσω C, D, E.</strong> Τέσσερις σύντομες ζεύξεις καλής ποιότητας 0.9. Συνολικά "
             "4 × (1 / 0.9) ≈ <strong>4.44</strong> μεταδόσεις."),
            (route_panel("f"),
             "<strong>Μέσω F.</strong> Δύο ζεύξεις μέτριας ποιότητας 0.8: 2 × (1 / 0.8) = <strong>2.5</strong> "
             "μεταδόσεις. Το μικρότερο άθροισμα, άρα τη διαλέγει το ETX."),
        ],
    },
    "hops": {
        "caption": "Σχήμα 4.2 · Η τοπολογία του Θέματος Δ.1 (2026): το πακέτο ταξιδεύει από το A στο C μέσω του B, σε δύο ζεύξεις.",
        "legend": ["source", "node", "dest", "route", "packet"],
        "cols": 1,
        "panels": [
            (hops_panel(),
             "Κάθε ζεύξη έχει το δικό της ETX (πόσες μεταδόσεις χρειάζονται κατά μέσο όρο) και το δικό της "
             "μήκος (πόσο κοστίζει η κάθε μετάδοση). Το συνολικό κόστος είναι το άθροισμα των δύο ζεύξεων."),
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
        num = f'<span class="step__num">{i}</span>' if len(spec["panels"]) > 1 else ""
        cells.append('<div class="step">' + panel + f'<p class="step__text">{num}{text}</p></div>')
    cols = {1: "", 2: "", 3: " steps--three"}[spec["cols"]]
    number = re.search(r"Σχήμα (\d+)\.(\d+)", spec["caption"])
    fig_id = f' id="fig-{number.group(1)}-{number.group(2)}"' if number else ""
    grid = f'<div class="steps__grid">{"".join(cells)}</div>' if len(spec["panels"]) > 1 else cells[0]
    return (f'<figure class="steps{cols}"{fig_id}>\n{grid}\n{legend_html(spec["legend"])}\n'
            f'<figcaption>{spec["caption"]}</figcaption>\n</figure>')


def marked(name):
    return "\n".join([f"<!-- etx_figures:{name} -->", figure_html(name), f"<!-- /etx_figures:{name} -->"])


def apply(chapter_path):
    path = Path(chapter_path)
    text = path.read_text(encoding="utf-8")
    for name in FIGURES:
        pattern = re.compile(r"<!-- etx_figures:" + re.escape(name) + r" -->.*?<!-- /etx_figures:"
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
        print("usage: python tools/etx_figures.py --apply docs/chapters/04-routing-metrics.md")
