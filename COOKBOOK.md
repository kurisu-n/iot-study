# IoT Study Corpus — Project Cookbook

> **Living document.** Updated as the project progresses.  
> Last updated: 2026-09-16

---

## 1. What We're Building

A self-contained **study corpus** for the MSc course "Διαδίκτυο των Πραγμάτων" (Internet of Things) at the International Hellenic University, taught by Prof. Konstantinos Marios Angelopoulos.

The corpus is a **textbook-style HTML document** written in Greek prose (with English technical terms), covering all theory and exercises likely to appear in the September 2026 resit exam. It is designed to be:

- **Readable** — long, flowing prose like a university textbook, not bullet-point notes
- **Complete** — covers every topic from the lectures, raw notes, and past exams
- **Exercise-focused** — reflects the 2026 shift from theory-only exams to 50% exercises
- **Published** — a built site with search and navigation, readable on a phone during revision

> ⚠ **Retired 2026-09-16.** This list used to say *"Self-contained — one HTML file, opens in any
> browser"*. That was a real decision and it was deliberately given up when the corpus moved to a
> built MkDocs site (section 8). What was gained: cross-chapter search, a navigation sidebar, and a
> URL. What was lost: the ability to hand someone a single file that works offline.

### Target Exam Format (2026 onward)

Based on the February 2026 exam:

| Component | Marks | Type |
|:---|:---:|:---|
| Protocol theory (DD, EBP, LoRaWAN) | 5.0 | Short-answer theory |
| LEACH CH election calculation | 2.5 | Mathematical exercise |
| ETX multi-hop energy calculation | 2.5 | Mathematical exercise |
| **Total** | **10.0** | **~50% exercises, ~50% theory** |

This is a significant departure from the 2025 exam, which was 100% theory (system design, Cloud vs Edge, Industry 4.0, standardization). The study corpus prioritises exercise practice while maintaining full theory coverage.

---

## 2. Source Materials

All source materials live under `D:\Development\Claude Workspace\Workspace\Current Workspace\IoT Study\`.

### 2.1 Lecture PDFs (Σημειώσεις)

| File | Topics | Exam Relevance |
|:---|:---|:---|
| Lecture 2 - DD - Leach.pdf | Directed Diffusion, LEACH | HIGH (Θέμα Α + Β) |
| Lecture 3 - LEC-Energy Balance Protocols.pdf | EBP, ring model, FND/HND/LND | HIGH (Θέμα Α.2) |
| Lecture 4/5 - Routing Metrics.pdf | ETX, link quality, energy models | HIGH (Θέμα Δ) |
| Lecture 6a - LPWANs - RPL.pdf | LoRaWAN, RPL, 6LoWPAN | HIGH (Θέμα Γ) |
| Lecture 7a - IoT topics.pdf | IIoT, 5G, IoT verticals | MEDIUM |
| Lecture 7b - IoT protocols.pdf | CoAP, MQTT, protocol stacks | MEDIUM |
| Lecture 8a - IEEE 802.11 MAC.pdf | WiFi MAC layer, CSMA/CA | HIGH (Θέμα Γ.1) |
| Lecture 8b - IEEE 802.11 standards.pdf | WiFi standards, 802.11a/b/g/n/ac | MEDIUM |
| Lecture 9 - WPT models.pdf | Wireless Power Transfer | LOW-MEDIUM |
| Lecture 10 - Mobility in IoT.pdf | Mobility models, handover | LOW-MEDIUM |

Note: Lectures 4 and 5 are identical files (confirmed by agents).

### 2.2 Handwritten Notes (Raw)

18 JPG images of handwritten notes shared via Viber (Feb 2026). Transcribed into `Transcribed_Raw_Notes.md`. Content covers DD, Flooding, LEACH, EBP, ETX (with solved exercise), and Scalar vs Vector models.

### 2.3 Extra Notes PDFs

| File | Content |
|:---|:---|
| SYNOLIKO.pdf | Comprehensive Greek summary of IoT architecture, protocols |
| ΣΗΜΕΙΩΣΕΙΣ GTP.pdf | GPT-generated study notes (Greek) |
| Μερικά από τα πιο δημοφιλή... .pdf | IoT communication protocols overview |

### 2.4 Past Exams (Θέματα)

| Year | Format | Key Shift |
|:---|:---|:---|
| 2022 | Theory-only | System design, protocol comparison |
| 2025 | Theory-only | IoT agriculture, Cloud/Edge, Industry 4.0 |
| **2026** | **Theory + Exercises** | DD, EBP, LEACH T(n) calculation, ETX energy calculation, LoRaWAN |

The 2026 exam is the most important reference — it establishes the new format.

---

## 3. Methodology

### Phase 1: Transcription ✅ COMPLETE

All source materials have been transcribed into markdown:

```
IoT Study/
├── Transcribed_Raw_Notes.md          (handwritten notes, 18 pages)
├── Exam_2026_Transcription_and_Analysis.md
└── Transcriptions/
    ├── Lectures_2_3.md               (DD, LEACH, EBP)
    ├── Lectures_4_5.md               (Routing Metrics / ETX)
    ├── Lectures_6a_7a.md             (LPWANs, LoRaWAN, RPL, 5G)
    ├── Lectures_7b_8a.md             (IoT protocols, WiFi MAC)
    ├── Lectures_8b_9_10.md           (WiFi standards, WPT, Mobility)
    └── Extra_Notes_and_Exams.md      (supplementary PDFs + all exam docs)
```

### Phase 2: Style Calibration ✅ COMPLETE

Wrote a sample chapter (DD + Flooding + Omniscient Multicast) in both English and Greek. Decisions made:

- **Language:** Greek prose, English technical terms (matching real Greek CS textbooks)
- **Tone:** Explanatory, expanded, textbook-style — not bullet-point notes
- **Format:** Markdown, built into HTML by MkDocs Material — MathJax for rendered maths, inline SVG
  diagrams, and a four-scheme theme. Chapters were authored as standalone HTML until 2026-09-16; see
  section 8 for why that changed and what carried over.
- **Math:** MathJax for rendered LaTeX formulas
- **Diagrams:** Mix of generated images (for complex network topologies) and inline SVGs (for simple flow diagrams)

### Phase 3: Corpus Writing 🔄 IN PROGRESS

Write the full textbook-style HTML document. Planned chapter structure (provisional):

1. **Διάδοση Δεδομένων** — Flooding, DD, Omniscient Multicast, flat vs hierarchical
2. **LEACH** — Phases, T(n) election mechanism, worked examples
3. **Energy Balance Protocol (EBP)** — Ring model, variable p_i, FND/HND/LND
4. **Μετρικές Δρομολόγησης** — ETX formula, energy models, worked exercises
5. **LPWANs & LoRaWAN** — Architecture, SF trade-offs, device classes, WiFi comparison
6. **RPL** — DAG construction, rank, objective functions
7. **IEEE 802.11 (WiFi)** — MAC layer, CSMA/CA, standards overview
8. **IoT Πρωτόκολλα Εφαρμογής** — CoAP, MQTT, protocol stacks
9. **WPT & Mobility** — Wireless power transfer, mobility models
10. **Ασκήσεις & Λυμένα Παραδείγματα** — All exam-style exercises with step-by-step solutions

### Phase 4: Study Protocol (PLANNED)

After corpus is complete:
- Structured reading order based on exam weight
- Exercise drill sessions (AI-generated practice problems)
- Interactive Q&A testing (conversational exam simulation)

---

## 4. Style Guide

### Language Rules
- Prose in **Greek**
- Technical terms in **English** where a Greek student would naturally use them: protocol, sink, base station, cluster head, flooding, gradient, reinforcement, broadcast, idle listening, MAC layer, etc.
- Formulas and variable names in English/math notation
- Exam-specific Greek terminology preserved exactly (e.g., «κόμβος», «δακτύλιος», «ζεύξη», «μονάδες»)

### Formatting Rules
- HTML with embedded CSS, MathJax CDN for math rendering
- Chapter → Section → Subsection hierarchy
- Comparison tables for protocol contrasts
- Boxed/highlighted formulas for key equations
- Dedicated "Worked Example" sections with step-by-step solutions
- Figure captions in Greek
- Colour-coded alerts for exam tips

### Content Rules
- Every topic that appeared in 2025 or 2026 exams gets full coverage
- Every formula gets at least one worked example with realistic numbers
- Exercises use the same energy model and notation as the 2026 exam
- Protocol comparisons include both narrative explanation and summary tables

---

## 5. Progress Log

| Date | What happened |
|:---|:---|
| 2026-09-15 | Transcribed 18 raw handwritten note images (3 parallel agents) |
| 2026-09-15 | Transcribed 2026 exam, gap analysis vs raw notes |
| 2026-09-15 | Transcribed all lecture PDFs + extra notes + past exams (6 parallel agents) |
| 2026-09-16 | Style calibration — wrote sample chapter in English then Greek |
| 2026-09-16 | Decision: HTML format, Greek prose, English terms, MathJax, diagrams |
| 2026-09-16 | Created this cookbook document |
| 2026-09-16 | Starting corpus writing (Phase 3) |
| 2026-09-16 | Chapter 1 written (DD, Flooding, OM, flat vs hierarchical) with animated SVGs |
| 2026-09-16 | Added theme system: 4 presets (Light Academic, Light Warm, Dark Navy, Dark Warm), side panel with color pickers, copy-to-clipboard for custom palettes |
| 2026-09-16 | Both Warm presets repainted in the FaceCue documentation palette (see §7) |
| 2026-09-16 | Ported to a built MkDocs Material site; Chapter 1 converted to Markdown (see §8) |
| 2026-09-16 | Figures made theme-aware: 21 literal SVG colours replaced by 20 `--fig-*` tokens |
| 2026-09-16 | Repository created and published to GitHub Pages |
| 2026-09-16 | Moved to iot.chris-nasiou.com (Hostinger); GitHub Pages removed |
| 2026-09-16 | Theme selector made a dropdown; FaceCue Ανοιχτό made the default |

---

## 6. File Locations

| What | Where |
|:---|:---|
| Project root | `D:\Development\Claude Workspace\Workspace\Current Workspace\IoT Study\` |
| Source materials | `..\Διαδίκτυο Των Πραγμάτων - Σημειώσεις\` |
| Past exams | `..\Διαδίκτυο των Πραγμάτων - Θέματα\` |
| Transcriptions | `.\Transcriptions\` |
| **Study corpus (source)** | `.\docs\chapters\` |
| **Study corpus (published)** | <https://kurisu-n.github.io/iot-study/> |
| **Repository** | <https://github.com/kurisu-n/iot-study> |
| This cookbook | `.\COOKBOOK.md` |

---

## 7. The Theme System

Four colour schemes, chosen from a dropdown in the site header. Nothing about the prose or the
diagrams depends on which one is active, so a scheme is purely a palette swap.

> ⚠ **Changed 2026-09-16.** Until the port to MkDocs, this was a hand-built floating 🎨 panel in the
> single HTML file, with its own colour pickers and a Copy Style button. Material's palette toggle
> replaces it, and the four presets became four CSS colour schemes. The mapping below is unchanged;
> only the mechanism is different.

### 7.1 The four presets

| # | Menu name | CSS name | What it is |
|:---:|:---|:---|:---|
| 1 | ☀️ FaceCue Ανοιχτό | `warm-light` | **The FaceCue documentation light scheme. The default.** |
| 2 | 🌙 FaceCue Σκούρο | `warm-dark` | **The FaceCue documentation dark scheme.** |
| 3 | ☀️ Ακαδημαϊκό | `academic` | The original white-and-navy scheme. |
| 4 | 🌙 Σκούρο Μπλε | `navy` | Dark slate and pale blue. |

All four live in `docs/stylesheets/corpus.css`, one block each, and are listed in `mkdocs.yml` under
`theme.palette`.

⛔ **The order in `mkdocs.yml` is meaningful twice over.** The first entry is the default for a reader
who has never chosen, and the dropdown lists them in that order: the two FaceCue schemes first, then
this corpus's own two, light before dark in each pair.

### 7.1.1 The dropdown

Material's palette control is a *cycler*: one button, each click advancing to the next scheme. With
four schemes that means up to three clicks to reach one, without seeing what you are choosing.
`docs/javascripts/palette-menu.js` replaces it with a menu listing all four, each with its icon, its
name and a small swatch previewing that scheme's page and heading colours.

⭐ **It drives Material's palette rather than replacing it.** Material still renders a radio per
scheme and still owns what happens on a change: the scheme attribute on `<body>`, the localStorage
that remembers a choice, and instant navigation. The menu only clicks the right radio. That is why a
choice survives a reload and a page change without the menu storing anything itself.

Four traps, all of them found by testing rather than anticipated:

- ⚠ **Labels pair with radios by index, not by `for`.** Material's label N carries scheme N's icon and
  name, but its `for` points at scheme N+1, because in the cycler the label *is* the "next" button.
  Pairing by `for` gives every row the wrong icon, off by one, which looks plausible.
- ⚠ **`toggle.name` and `toggle.icon` must describe their own scheme.** In the cycler they describe
  what the *next* click gives. Once the menu shows entry N's name beside entry N's radio, they have to
  name themselves.
- ⛔ **Hide Material's labels with CSS, never with the `hidden` attribute.** Material toggles `hidden`
  on them every time the scheme changes, so setting it once works until the first pick, and then a
  second icon appears in the header beside the menu button.
- ⛔ **Read the active scheme from `<body>`, not from `input.checked`.** Material restores a
  remembered choice *after* the menu is built, so at build time no radio is checked and the tick
  lands on the first row. That is invisible whenever the first row is also the default, which it is,
  so it only shows for a reader who chose something else and came back. The menu watches the
  attribute with a `MutationObserver` rather than racing it.

The localStorage key is namespaced by the site's base path (`/.__palette` at the root). It moved when
the site moved off `/iot-study/`, so a choice made on the old address does not carry over.

### 7.1.2 Every scheme block declares every token it reads

The swatch preview exposed a structural flaw. It works by giving each swatch its own
`data-md-color-scheme`, so that span resolves *that* scheme's tokens while the page keeps the active
one. For Warm Dark it drew a light circle.

Warm Dark had never declared its own `--fc-*` tokens. It inherited them from `:root`, where
`fc-tokens.css` puts the dark values. That holds only while Warm Dark is the *outermost* scheme. Nest
it inside a Warm Light element and inheritance finds Warm Light's re-declared tokens first. The
swatch was simply the first thing ever to nest one scheme inside another.

Warm Dark now declares all nineteen `--fc-*` tokens itself, mirroring `fc-tokens.css`, so every scheme
block is correct wherever it sits. The cost is duplication: **change a FaceCue dark value in both
places.** Measured afterwards, every swatch resolves to identical colours under all four active
schemes, and the page contrast figures did not move.

### 7.2 Where the two Warm palettes come from

Both are lifted token for token from the FaceCue documentation site, so the study corpus reads the
same way FaceCue's own manual does. The two source files live in the docs worktree at
`D:\Development\FaceCue Workspace\facecue-site-docs\`:

| Scheme | Source of truth |
|:---|:---|
| Dark Warm | `src\static\assets\fc-tokens.css`, the `:root` block |
| Light Warm | `documentation\docs\stylesheets\facecue.css`, `[data-md-color-scheme="facecue-light"]` |

The FaceCue tokens are themselves lifted from the FaceCue Unity editor theme, so the chain runs
editor → `fc-tokens.css` → docs site → this corpus. Every value in the two presets carries an inline
comment naming the FaceCue token it came from, which is what makes a later reconciliation possible:
if the docs palette drifts, the comments say exactly which token to re-read rather than leaving a
future session to eyeball hexes.

The mapping is mostly direct. Three places needed a decision, because the corpus has components
FaceCue's documentation does not:

- **The formula box** has no FaceCue counterpart. It takes `--fc-section` as its fill and keeps its
  `--fc-gold` border, so it reads as a lighter surface inside a gold rule.
- **The exam tip** is drawn as a FaceCue callout: `--fc-section` for the fill, and `--fc-tan` for both
  the left rule and the «📝 Σημείωση Εξεταστικής» heading. An earlier draft used FaceCue's green
  signal colour, which was wrong on two counts — FaceCue's callouts are ruled in warm gold, not green,
  and green on the light section surface only reached 3.5:1 against a bold 15px label.
- **The table header** paints `--primary` as a background, which FaceCue never does with its tan. So
  `--th-text` is the *dark* surface colour in both Warm presets, giving a tan bar with dark type.

### 7.3 Two repairs made along the way

Neither was part of the palette work, but both would have shown as defects in the new presets:

1. `.comparison-box h4` had its colour hard-coded to `#92400e`, a dark brown that vanished on any
   dark preset's warning fill. It is now `--compare-h`, a sixteenth theme variable with a value in
   every preset and its own row in the colour picker.
2. 🌙 Navy set `--th-text` to `#e2e8f0`, pale text on its equally pale `--primary` table-header bar.
   It is now the dark page colour, matching the fix the Warm presets needed.

### 7.4 Contrast

Every text-on-surface pair in both Warm presets clears WCAG AA (4.5:1), measured in the browser
rather than estimated. The weakest pair is the muted caption text at 5.04:1 dark and 5.11:1 light.
Borders sit near 1.6:1 against their page, which is a visible hairline and is what FaceCue uses.

⚠ When a new component is added to a chapter, give it a theme variable rather than a literal colour,
and re-run the contrast probe across all four presets. A literal colour is invisible until someone
switches preset, which is how the `.comparison-box` heading survived this long.

### 7.5 The figure palette

Diagrams are inline SVG, and until 2026-09-16 every colour in them was written as a literal hex. That
made them theme-blind: the sensor-field ellipse was a pale blue that glowed on a dark page, and the
label text was a mid-grey that nearly vanished on it. Twenty-one distinct literals, 178 occurrences.

They now resolve through twenty `--fig-*` tokens, declared once per scheme:

| Group | Tokens | What they paint |
|:---|:---|:---|
| Surfaces | `--fig-surface-accent`, `-soft`, `-warn`, `-event`, `-ok` | Region fills: the sensor field, a highlighted zone |
| Structure | `--fig-node`, `--fig-node-soft`, `--fig-line`, `--fig-label` | Sensor dots, connecting strokes, caption text |
| Accent | `--fig-accent`, `-deep`, `--fig-on-accent`, `-soft` | The sink box, its outline, and text on top of it |
| Signals | `--fig-event`, `--fig-warn`, `--fig-ok`, each with `-deep`, plus `--fig-event-soft` | Event paths, warnings, success marks |

⚠ **A `-deep` token means "the outline colour", not "a darker shade".** In the light schemes that is
darker than its base; in the dark schemes it is *brighter*, because the outline is drawn on top of
the fill rather than under it. Same inversion for `--fig-event-soft`, which is a fill and so goes
dark while `--fig-event` goes bright.

The Academic scheme's figure values are the original literals, so it renders every diagram exactly as
it was first authored.

### 7.6 Contrast

Measured in the browser against the live computed values, not estimated, and against two thresholds:
**4.5:1 for text** (including figure labels and the small caption under a formula) and **3:1 for
non-text graphics** (the sensor dots, the rules). **All four schemes pass every pair**, sixteen text
comparisons and four graphic ones each.

Getting there took five corrections, and it is worth recording which, because each one came from
measuring a pair nobody had thought to measure:

| Scheme | Token | Was | Now | Why |
|:---|:---|:---|:---|:---|
| Academic | `--c-muted` | `#718096` | `#626f83` | 4.02:1 on the page |
| Academic | `--c-exam-border` | `#38a169` | `#2b7d51` | 3.14:1, and it is the heading text, not just the rule |
| Academic | `--fig-node` | `#a0aec0` | `#7d8998` | 2.03:1 on the field surface |
| Academic | `--fig-label` | `#718096` | `#626f83` | 3.62:1 on the field surface |
| Warm Light | `--fig-node` | `#9A9384` | `#7D7668` | 2.41:1 on the field surface |
| Warm Dark | `--c-muted` | `--fc-text-muted` | `#95908B` | 4.08:1 on the section surface |

⚠ **Academic is therefore no longer byte-identical to the first draft.** It was, deliberately, until
2026-09-16. Four of its values are now darker. The hues are unchanged, and each new value is the
original walked toward black until it cleared its threshold with a little headroom, so the scheme
still reads the way it was drawn.

⚠ **The Warm Dark correction is a deviation from the FaceCue palette, and the fault is ours.**
FaceCue uses `--fc-text-muted` for subtitle text on the *panel*, where it measures 5.04:1 and is
perfectly fine. This corpus also puts muted text on the *section* surface, inside the formula box and
under figures, which FaceCue never does, and there the same colour drops to 4.08:1. The token is
brightened just enough to clear the threshold on the section. Every other Warm Dark value is still
FaceCue's.

⚠ When a new component is added to a chapter, give it a token rather than a literal colour, and
re-run the contrast probe across all four schemes. A literal is invisible until someone switches
scheme, which is how the figures stayed theme-blind for as long as they did. The deploy workflow now
fails the build if a literal hex appears in a chapter, which catches the SVG case automatically.

---

## 8. The Site and the Repository

| | |
|:---|:---|
| Repository | <https://github.com/kurisu-n/iot-study> (public) |
| Published at | <https://iot.chris-nasiou.com/> |
| Served by | Hostinger, from the `deploy` branch |
| Built with | MkDocs Material, pinned in `requirements.txt` |
| Deployed by | `.github/workflows/deploy.yml`, on every push to `main` |

### 8.1 The shape of it

Source lives on `main`. The workflow builds with `--strict`, runs one guard, copies
`hosting/.htaccess` into the output, and force-pushes the finished HTML to the **`deploy`** branch,
which Hostinger pulls and serves. The two branches never mix.

This is now the FaceCue site's architecture exactly, ending included. Hostinger runs no build step,
so the deploy branch holds finished HTML and nothing else.

⛔ **Push `main` and nothing else.** `deploy` is machine-written and replaced wholesale on every
build, so a hand-made commit there is destroyed by the next push to `main`, silently and with no
conflict.

> ⚠ **Changed 2026-09-16.** The site was published to GitHub Pages at
> `https://kurisu-n.github.io/iot-study/` for a few hours, from a `gh-pages` branch. It moved to its
> own subdomain the same day, and Pages was switched off so there is one live copy at one address.
> Two copies would mean two addresses for one document, and `site_url` can only name one of them as
> canonical.

⛔ **`--strict` is what keeps the site honest.** A broken internal link or a page missing from the
nav fails the build rather than becoming a quiet gap on the live site.

### 8.2 The colour guard

After the build, the workflow greps the generated chapter HTML for a literal hex and fails if it
finds one. Stylesheets are not searched, since that is where literals belong. This exists because a
hard-coded colour in a chapter is invisible until someone switches scheme, so it cannot be caught by
looking at the page.

### 8.3 Traps worth knowing

- ⚠ **`mkdocs serve` mounts the site under the `site_url` path.** That is now the domain root, so it
  opens at `http://127.0.0.1:8000/` as expected. While the site was on GitHub Pages the path was
  `/iot-study/`, and a request to the root returned a 404 that looked like a broken build and was
  not one. If `site_url` ever gains a path again, this comes back.
- ⚠ **Hostinger serves the output directly, so server configuration has to be IN the build.**
  `hosting/.htaccess` carries the 404 mapping and the cache rules, and the workflow copies it into
  `site/`. It cannot live under `docs/`, because MkDocs skips dotfiles.
- ⛔ **Cache headers cannot be withdrawn.** Nothing is marked immutable unless its filename carries a
  content hash. Material's own bundles do (`bundle.d7400e89.min.js`); `corpus.css`, `fc-tokens.css`
  and `mathjax.js` do not, and are held for five minutes with revalidation. The immutable rules must
  stay *below* the generic ones in the file: with `Header set`, the later match wins.
- ⚠ **Search runs the English pipeline, and not for the reason you would guess.** lunr-languages does
  ship a Greek stemmer, and Material even bundles the file. Material's search plugin simply does not
  accept `el` as an index language: setting it prints *"Option search.lang 'el' is not supported,
  falling back to 'en'"* and builds anyway. So Greek is tokenised and searchable word for word but
  not stemmed, and «κόμβος» does not also match «κόμβου». Re-test when Material is upgraded.
- ⚠ **pip cannot reach PyPI on this machine** — the TLS proxy presents a self-signed certificate and
  every install fails on `CERTIFICATE_VERIFY_FAILED`. Local builds use the MkDocs in the FaceCue site
  venv (`D:\Development\FaceCue Workspace\facecue-site\.venv\Scripts\mkdocs.exe`), which is pinned to
  the same versions. The CI build is unaffected.
- ⚠ **MkDocs is pinned on its own line**, not just Material. Material 9 does not run on the MkDocs
  2.0 line and a loose resolve will pick it up. Copied from the FaceCue documentation's requirements.
- ⚠ **Maths inside a raw HTML block is never converted.** Markdown passes `<figure>` through
  untouched, so a `$...$` in a figure caption reaches the page as literal text. Write it as
  `<span class="arithmatex">\(...\)</span>` instead.
- ⚠ **`$$...$$` needs a blank line after it** to be treated as display maths. Followed immediately by
  another line, it is parsed as part of the same paragraph and rendered inline.
