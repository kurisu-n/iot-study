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
| 2026-09-16 | Chapter 1 rebuilt as the template for every chapter: grounded against slides and notes, four factual errors corrected, 22 step panels, an exam box per section, extracurricular marking, FaceCue-style contents column (see §9) |

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

---

## 9. The Chapter Template

> **Settled on Chapter 1, 2026-09-16. Every later chapter follows it.** Chris's brief was to nail
> Chapter 1's voice, style and structure first, then expand. This section is that template. Where a
> decision is still open, it says so.

### 9.1 Ground the chapter before writing it

Read the lecture transcription (`Transcriptions/`) and the handwritten notes (`Transcribed_Raw_Notes.md`)
for the chapter's topic **before** writing a sentence, and check every claim against them afterwards,
including the claims you added yourself.

This is not a formality. Doing it for Chapter 1 found **four factual errors in the existing text**, all
of which read as perfectly plausible:

| The chapter said | The course says |
|:---|:---|
| Sensors *cannot* transmit directly to the BS | They can, it is just expensive. EBP is built on it (Δ3, διαφ. 6) and LEACH cluster heads do it |
| Flooding the interest is a *one-off* setup cost | The sink *periodically refreshes* the interest (Δ2, διαφ. 10). Recurring, just not per event |
| Phases 1 and 2 happen one after the other | They happen at the same instant: receiving an interest creates the gradient (Δ2, διαφ. 11) |
| Nobody would deploy flooding | DD itself floods its interests |

It also found that the handwritten notes and the slides **disagree on notation**: the slides use $n$
sources and $m$ sinks (Δ2, διαφ. 23), while the notes write the same cost with $m$ for the sources. That
became an exam warning, not a silent pick.

### 9.2 Cite the source; mark what has none

| Form | Meaning |
|:---|:---|
| **(Διάλεξη 2, διαφάνεια 16)** | Lecture 2, slide 16. Plural for a range: "διαφάνειες 25 έως 27" |
| **(χειρόγραφες σημειώσεις, σελίδα 9)** | The handwritten class notes, page 9 |
| `!!! extra "Εκτός ύλης"` | A paragraph or more that comes from neither |
| `<span class="extra-tag">εκτός ύλης</span>` | A single claim that comes from neither |

**What gets marked** is a *fact* that is not in the slides or notes: a term, a list, a result, a
property. **What does not** is explanation that only unpacks course material: an analogy, a worked
consequence, a "because". Marking every inference would bury the page.

⚠ Check a suspicion before marking it. "Energy holes" looked extracurricular in Chapter 1 and is not:
it is in the handwritten notes and on Lecture 3, slide 4.

⛔ Citations are written out in full. The abbreviated forms used until 2026-09-16, "(Δ2, διαφ. 16)"
and "(χειρόγρ. σημ., σ. 9)", now fail the build; see §9.9.

### 9.3 Every section ends with "Τι να περιμένετε στην εξέταση"

```text
!!! exam "Τι να περιμένετε στην εξέταση"

    <div class="exam-record">
      <a class="exam-chip is-hit" href="../../#exam-papers"><strong>6/2/2026</strong> Θέμα Α.1, 1 μονάδα</a>
      <a class="exam-chip" href="../../#exam-papers"><strong>15/2/2025</strong> όχι</a>
      <a class="exam-chip" href="../../#exam-papers"><strong>2/2022</strong> όχι</a>
    </div>

    What was asked, paraphrased. How to answer it. Traps.
```

- **All three papers, every time**, with `is-hit` on the ones that examined the section. An absence is
  information, and a uniform record makes it visible.
- **Dates as known.** 2026 and 2025 carry a day; 2022 survives only as a month. Never invent the day.
- **Paraphrase the question**, do not quote it at length.
- **Guidance is labelled as guidance.** There are no marking schemes; "how to answer" is an assessment.
- The 2022 "indicative answers" file reads like student notes. Use the 2022 *questions* as evidence, not
  those answers.

✅ **Ruled by Chris, 2026-09-16: one box per numbered section**, kept even where the section was never
examined.

### 9.4 Protocols get step-by-step figures

- **One small network per protocol, reused in every panel**, so the reader follows the same nodes through
  the whole cycle. Chapter 1 uses Sink, A, B, C, D, Source: two disjoint routes plus two cross links, the
  smallest shape that still shows multiple paths, a choice to reinforce, and an alternative for repair.
- **2 to 4 steps per phase**, each a panel with its explanation under it.
- ⛔ **Explanatory text lives in HTML, never inside the SVG.** The only SVG text is a node's name, in clear
  space. This removes most overlap defects by construction, and HTML text reflows and sits on a page
  background whose contrast is already measured.
- **A legend under each figure, listing only the marks that figure uses.**
- **Hue says what a line is; weight says how strong.** Interest and reinforcement share blue, because a
  reinforcement *is* an interest. A gradient is green whether exploratory (dashed) or reinforced (thick).
  Data is orange, the source red. The ring around the node a step is about is a dotted neutral, sharing a
  hue with no arrow.
- Panels are generated by **`tools/dd_panels.py`** and live in the chapter between
  `<!-- dd_panels:NAME -->` markers. Edit the generator, then run
  `python tools/dd_panels.py --apply docs/chapters/01-data-propagation.md`. Apply is byte-idempotent and
  fails loudly on a broken marker. ⛔ Never hand-edit between the markers.

### 9.5 Figures are checked, not eyeballed, and then eyeballed anyway

Chris's rule, 2026-09-16: **text never overlaps other elements**. Two tools enforce the measurable part:

| Tool | Checks |
|:---|:---|
| `tools/figure-audit.js` | Every SVG label against every shape, sampled with `isPointInFill` and `isPointInStroke`, and its contrast against what is **actually behind it** |
| `tools/contrast-probe.js` | Captions, legend, exam and extracurricular boxes, the contents column, and graphic marks at 3:1 |

Traps, every one of them hit on Chapter 1:

- ⛔ **A colour-pair sweep certifies the pair you give it, not the page.** The "SRC" label passed a sweep of
  on-accent text against an accent fill, but actually sat mostly on the page, at 1.0:1. The audit
  measures what is behind each label instead.
- ⛔ **Measure after a navigation, never after toggling the scheme in place.** A hidden Browser pane
  suspends style recalculation and returns stale colours. Set the remembered palette in localStorage,
  navigate, then measure.
- ⛔ **Alpha and notation.** The contents column fades with `color-mix(... transparent)`, which computes to
  `color(srgb r g b / a)` on a 0 to 1 scale. Ignore the alpha and a faded entry reads at full strength;
  parse it as 0 to 255 and a pale blue reads as black. Both happened, producing a false failure on the
  dark schemes and a false pass on the light ones.
- ⛔ **No contrast check catches colours that each pass against the page but cannot be told apart.** In
  the warm schemes the figure accent, amber and deep tan were one family of browns, so an interest, a
  data message and a reinforcement looked identical. Only a screenshot showed it. The warm schemes now
  take FaceCue's signal blue, green and red for figures, plus a derived orange.
- ⚠ **The Browser pane screenshots unreliably.** Headless Edge is dependable: build a preview page from the
  real CSS and panels, run
  `msedge --headless=new --disable-gpu --window-size=965,870 --screenshot=out.png file:///preview.html`,
  and read the PNG.
- To load a probe into the page without shell escaping trouble, copy it into `docs/_devprobe/` briefly,
  `fetch` it, store it in localStorage, and **delete the copy before building for commit**.
- ⛔⛔ **Map EVERY colour variable Material uses.** Material declares its palette on `:root` as light-theme
  literals, and a custom scheme name matches none of its scheme rules, so an unmapped variable keeps its
  light value in every scheme: harmless on the light schemes, broken on the dark ones. The body text of
  every box was black at 87% on the dark box surface (1.12 to 1.37:1) because `--md-admonition-fg-color`
  was never mapped. A sweep for colour variables equal under a light and a dark scheme found 57; see
  `corpus.css` section 5 for the procedure. Re-run it after any Material upgrade.
- ⛔ **A probe that reads the first match measures the wrong element.** The first `<p>` inside a box is its
  title, so "box body" measured the readable title and passed the unreadable body. Measure every match
  and report the worst, and test the probe against the broken page before trusting it on the fixed one.

### 9.6 Voice

Greek textbook prose with English technical terms, as §4 says. Chapter 1 was rewritten **without em
dashes**; the previous text had 32.

✅ **Ruled by Chris, 2026-09-16: no em dashes** in this corpus.

### 9.7 The table of contents

Ported from the FaceCue documentation: every entry rests faded, and the reader's position shows by the
fade coming off. Sections get a hairline beneath, subsections a short bar. `toc_depth: 3` keeps step-level
content out of the column. The selector traps are documented in `corpus.css` section 10.

✅ **Ruled by Chris, 2026-09-16: the dark schemes are fine as ported; the light ones want more contrast,
especially on the selected entry.** Light dials raised and the reader's position painted in
`--toc-strong`, which in Warm Light is FaceCue's deeper tan (its ordinary tan tops out at 6.72:1 even at
full strength). Measured after:

| | Section, resting | Subsection, resting | Selected |
|:---|:---:|:---:|:---:|
| FaceCue Ανοιχτό | 2.35 → **3.53** | 4.39 → **6.02** | 6.72 → **9.59** |
| Ακαδημαϊκό | 2.99 → **5.19** | 4.64 → **6.46** | 12.14 |
| Dark schemes | unchanged | unchanged | unchanged |

The live FaceCue documentation measured 2.35 / 5.55 / 6.72 to 7.66 in its light scheme on the same day,
identical to this corpus before the change, so the same lift applies there if Chris wants it.

### 9.8 The left sidebar

Ported on 2026-09-16 from the structure the FaceCue documentation actually ships, variant C, "inspector
rows" (its `overrides/main.html` forces `data-fc-sidebar="c"`; variants A and B exist only for its preview
switcher). A chapter group is a boxed header row, its pages hang off a thin rail, and the current page
takes a coloured stripe and a tinted row. Code in `corpus.css` section 14 and `javascripts/nav-sections.js`.

- **The group's name opens its first page; the rest of the row folds.** Material makes the whole label a
  fold control, so `nav-sections.js` splits it. Unlike FaceCue's copy it runs on every `document$`
  emission and marks each label it handles, because this site uses instant navigation and FaceCue's does
  not. Verified: a row click folds and stays, a name click opens the chapter, and after navigating there is
  still exactly one handler.
- **Colours** are FaceCue's measured values in the two warm schemes, and derived from `--c-*` in Academic
  and Navy. Lowest sidebar text contrast in any scheme: 5.95:1, the active page in FaceCue Ανοιχτό.
- **The nav is 14.5rem wide on desktop**, FaceCue's width, so a chapter name does not wrap. Widening
  `.md-sidebar` alone does nothing; the width lives on `.md-sidebar__inner`'s right padding.
- **Not ported:** FaceCue's separators between conceptual groups, which are matched by nav position and
  hard-wired to its own page order.
- ⚠ **Deliberately different:** FaceCue hides the sidebar's title row at every width. Here it is hidden on
  desktop only, because on a phone Material's drawer uses that row as the back control inside a chapter.

### 9.9 No shorthand, anywhere

Ruled by Chris, 2026-09-16: **no shorthand anywhere.** An abbreviation may only appear after its full name
has been written out, and every use after that links back to where it was written out. References to
other things get links too.

**It is enforced by the build, not by care.** `hooks/shorthand.py` reads every rendered page and fails
the build on any of:

| Problem | Example that fails |
|:---|:---|
| An abbreviation used before its full name on the same page | "Το WSN είναι…" with no "Wireless Sensor Network (WSN)" above it |
| Shorthand in a heading | "## Τα όρια του DD" (headings use the full name) |
| An acronym missing from `terms.yml` | "CH", until it is listed |
| A word with an inner capital that is not a listed name | "WiFi", "LoRaWAN" unlisted |
| A Greek abbreviation | "π.χ.", "διαφ.", "σελ.", "Δ2" |

**How to write a definition:** the full name, then the abbreviation inside parentheses, within about
160 characters: "Directed Diffusion (DD)" or "ασύρματο δίκτυο αισθητήρων (Wireless Sensor Network, WSN)".
The hook turns that first abbreviation into the anchor and **every later use on the page into a link
back to it**, with the full name as a tooltip. Authors write plain "DD" in the Markdown; the links are
generated.

**Per page, on purpose.** Each page defines its own abbreviations, so a reader who opens Chapter 5
directly still meets "WSN" spelled out before it is used. The cost is a little repetition across
chapters; the gain is that no chapter depends on having read another.

**Adding a term:** list it in `terms.yml` with the full names it may be introduced by, and note where
the course spells it out. `ns-2` is the one expansion the course never gives; it uses the tool's own
name.

**Cross-references.** Section headings carry stable English ids (`{#flat-vs-hierarchical}`), figures
carry their number (`fig-1-3`), and the front page's exam table is `#exam-papers`, which every exam
chip links to. `validation: anchors: warn` in `mkdocs.yml` makes a Markdown link to a missing anchor a
strict-build failure. ⚠ The exam chips are raw HTML, so MkDocs neither rewrites nor validates their
`../../#exam-papers` path; it is correct for a page two levels deep, which every chapter is.

**Tests.** `tools/test_shorthand.py` feeds the hook deliberately broken input, since a checker that only
ever sees clean pages proves nothing. The deploy workflow runs it before building. 10 cases as of
2026-09-16, covering each failure above plus the places it must stay silent: code, maths and SVG.

⏳ **Not linked yet, and why:**
- **"Κεφάλαιο 2", "Κεφάλαιο 3"** in Chapter 1: those chapters do not exist, and a link to a missing page
  fails the strict build. Link them when they are written.
- **Slide citations** ("Διάλεξη 2, διαφάνεια 16") point at the lecture PDFs, which are in the repository
  but not published. Linking would mean publishing them; a browser opens `file.pdf#page=16` at that
  page. Decision for Chris.

### 9.10 Plain language: keep the term, say what it means

Ruled by Chris, 2026-09-16, after a paragraph on how well DD copes with a changing network used
"δυναμικότητα", "κατατάσσοντάς το" and "ρευστά δίκτυα" and never said what the practical point was.

**The rule:** every technical term the course or the exam uses stays, and it comes with its meaning in
ordinary words, right there. "Κλιμάκωση" becomes "συνεχίζει να δουλεύει σωστά όταν το δίκτυο μεγαλώνει";
"διάμετρος του δικτύου" becomes "τα βήματα από τη μία άκρη του ως την άλλη (η διάμετρός του)".

What the Chapter 1 sweep changed, 27 places, as a checklist for the next chapter:

- **Abstract nouns that hide a situation.** "Δυναμικότητα" is "κόμβοι χαλάνε, μετακινούνται ή εμφανίζονται,
  ώστε οι διαδρομές να αλλάζουν". Say the situation, then name it.
- **Notation left unread.** "$\mathcal{O}(n\sqrt{N})$ για $m \ll \sqrt{N}$" gets a sentence: what $m \ll
  \sqrt{N}$ means, and what the growth rate does in practice ("τετραπλάσιοι κόμβοι, περίπου διπλάσιο
  κόστος").
- **Terms of art named but not explained.** "Shortest-path multicast tree", "σε επίπεδο εφαρμογής",
  "distinct-event delivery ratio" (as a question the metric answers).
- **Words that read two ways.** "Το σχήμα είναι αντιδραστικό" can be read as *the figure*. Say "ο μηχανισμός".
- **Clever phrasing.** "Λένε περισσότερα από μια παράγραφο επιθέτων" is style, not information.
- **A contrast between two sources gets a question, the two answers, and the reconciliation**, in that order,
  not one dense sentence.

⛔ **An explanation may unpack the source, never extend it.** "Proportionally to node failure percentage"
does not mean one-to-one, so the text says the drop "follows" the failure rate and gives no "10% fail,
10% lost" example. A draft sentence explaining *why* delivery drops was removed, because the slide says
only *that* it does.

---

## 10. Chapter Order

Ruled by Chris, 2026-09-16. **Write chapters in this order of priority, even if that means skipping some:**

1. **Topics the handwritten notes cover.** They record what was actually taught and emphasised in class.
2. **Topics of the 2026 exam**, the paper that set the current format.
3. **Topics of the 2025 and 2022 exams.**
4. **Everything else.**

Mapped against the sources on the same day:

| Priority | Chapter topic | Handwritten notes | Exams | Lecture |
|:---:|:---|:---|:---|:---|
| ✅ | Data propagation: flooding, Directed Diffusion | pages 1 to 6 | 2026 Α.1, Α.2; 2022 Θέμα 2Γ | 2, 3 |
| ✅ | LEACH, including the cluster head election exercise | pages 7 to 11 | 2026 Β.1 (2.5 marks) | 2 |
| ✅ | Energy Balance Protocol | pages 12 to 14 | 2026 Α.2 | 3 |
| **1** | **Routing metrics and ETX**, including the multi-hop energy exercise | pages 15 to 16 | **2026 Δ.1 (2.5 marks)** | 4 / 5 |
| 1 | How technology changed energy management, a synthesis across the protocols | page 17 | none | notes cite "§12" |
| 1 | Scalar and vector models | pages 17 to 18 | none | 9 (see warning) |
| **2** | **Low Power Wide Area Networks and LoRaWAN, with the WiFi comparison** | none | **2026 Γ.1 to Γ.3 (2.5 marks)** | 6a, 8a, 8b |
| 3 | Designing an IoT system, the IoT reference layers | none | 2025 Θέμα 1; 2022 Θέμα 3 | 7a, 7b, extra notes |
| 3 | Comparing access protocols, and why no single wireless technology fits all | none | 2025 2α and 2022 2Α (asked twice); 2022 2Ε | 7b, 8b |
| 3 | Cloud and edge computing; Industry 4.0; standardisation | none | 2025 2β to 2δ | 7a, extra notes |
| 3 | IEEE 802.11ah; addressing and security; WSN and MANET; smart cities and 5G | none | 2022 Θέμα 1, 2Β to 2Δ | 7a, 8b |
| 4 | RPL, CoAP and MQTT, wireless power transfer, mobility | only as noted above | none | 6a, 7b, 9, 10 |

⚠ The Lecture column is checked for priorities 1 and 2 only; for 3 and 4 it is a first guess from the slide titles, to be confirmed when those chapters are written.

**Next up is routing metrics with ETX** (LEACH and the Energy Balance Protocol are done, 2026-09-16):
it is covered by the notes, carries 2.5 marks in 2026 (Θέμα Δ.1), and is the last of the 2026 exercises.
The full chapter skeleton (chapters 3 to 12) now exists as placeholder pages in the menu, marked with a
`☆`, so the order and what is deferred are visible up front.

### 10.1 What the LEACH chapter added to the template

Written 2026-09-16. Nothing overturned §9; three things worth carrying forward:

- **A generator per chapter, same contract as `dd_panels.py`.** `tools/leach_figures.py` reuses the
  `<figure class="steps">` fragment, the HTML-only labels, the `--fig-*` colours, and the
  `<!-- leach_figures:NAME -->` markers rewritten in place by `--apply`. A four-across variant
  (`.steps--four`, added to `corpus.css` §11) holds a row of small panels such as the rounds of one era;
  it drops to two across below 76.24em so a phone never shrinks a panel past reading size.
- **Schematic figures are labelled as such.** The dead-node distribution (Σχήμα 2.4) redraws the *shape*
  of what slides 61 to 63 show, not their data, and the caption says so. When a figure stands in for a
  measurement rather than reproducing it, the caption states that plainly.
- **A worked exam answer gets its own numbered section**, not a box: the 2026 Β.1 solution is §2.4, with
  the question in a `!!! question` admonition, then numbered steps, the era figure, and an
  extracurricular note on why the literal 0.14 fails where P = 1/7 works. Correct a slide error inline in
  a `!!! warning` (here the slide-53 typo `1/(1-2P)`, correctly `P/(1-2P)`), with the derivation that
  proves which is right.

⚠ **Check before writing the scalar and vector chapter.** The notes' table describes scalar and vector
*sensor data* (temperature as one value, wind velocity with a direction). The only place those words
appear in the lectures is Lecture 9 on wireless power transfer, as the *Scalar Charging Model* and the
*Vector Model*, which are about charging. The notes may have attached an unrelated explanation to the
lecture's terms. Read Lecture 9 before trusting either.

## 11. Exam pages

Added 2026-09-16. A `Θέματα Εξετάσεων` nav section sits before `Κεφάλαια`, one page per
exam (`docs/exams/2026.md`, `2025.md`, `2022.md`). Each page has two parts.

**The facsimile.** A `<div class="exam-facsimile" markdown="0">` holds one or more `<div class="exam-sheet">`
blocks, each an **A4 page** (the 210:297 proportion of the real thing), reproducing the original as
closely as the source allows: the institution header, the course and date block, the name and student
number fill-in lines, the italic return note, the θέματα with their marks in bold, and any diagram the
paper carries (the 2026 ETX topology, drawn as a small inline SVG). It is a fixed cream sheet with dark
ink in every scheme, framed with a border and shadow, so it reads as the physical paper rather than as
our writing.

⭐ **How the A4 sizing works, ruled with Chris 2026-09-16.** The type is sized in **container units**
(`cqi`, one per cent of the sheet width), so a sheet holds the same amount of text whatever its rendered
width: the whole page scales like a photo of the original. That means the content-per-page is set by the
font size alone, not by the screen. At the sheet's capped width (46rem) a readable ~2cqi font fits each of
the three papers on one A4. `aspect-ratio: 210/297` is a **minimum, not a hard clip** (`overflow: visible`):
a short paper (2025) sits in an exact A4 with whitespace below, a fuller one grows a little rather than
cutting a question off. Below 45em the sheet drops the fixed height and reflows at a fixed readable size,
because a true A4 on a phone shrinks the type past reading. ⚠ **Measure fit at the real 46rem width, not in
the preview pane** — the pane is narrower, which inflates line-wrapping and made a one-page paper look like
1.7 pages. Split into two `exam-sheet` blocks only if a paper genuinely will not fit one A4 at a readable
font. Two rules on content:

- ⛔ **The facsimile is verbatim source.** `hooks/shorthand.py` lists `exam-facsimile` in `SKIP_CLASSES`,
  so the paper keeps its own acronyms (WiFi, LoRaWAN, EBP, SF) untouched, with no define-first links. The
  answers below it are our prose and obey the no-shorthand rule as usual, defining each acronym on the
  page before use (the skipped facsimile does not count as a definition).
- ⛔ **Do not copy an institution's logo artwork.** The 2026 paper has an emblem; the facsimile uses the
  text header only. Reproduce the layout and wording, not the trademark.

**The answers.** Under `## Απαντήσεις`, each question gets a heading with a marks chip
(`<span class="q-marks">`), a one-line restatement, and then:

- `!!! answer "Σύντομη απάντηση"` (open) for the short answer, and
- `??? answer-more "Εκτενής απάντηση"` (collapsed) for the expanded one, so a reader can attempt the
  question first.
- A question whose chapter is not written yet gets `!!! todo "..."` naming the chapter that will fill it,
  instead of the two answer blocks. Populate answers as the chapters land.

The three admonition types (`answer`, `answer-more`, `todo`) and the facsimile frame live in
`corpus.css` §16-17. When a covered answer restates a worked chapter result, link to the chapter section
rather than duplicating the figure (e.g. the 2026 Β.1 answer links to `02-leach.md#worked-2026`).

## 12. Formula traces (smallest-step solving)

Ruled by Chris, 2026-09-16. **Every formula solved in the corpus is shown as a trace: the smallest
possible steps, one change per line, so it is clear which number replaces which symbol.** A line either
substitutes one value or performs one arithmetic operation, never both, and a right-column note says what
changed.

**Shape.** A `<div class="trace" markdown="1">` (a light left-ruled block, `corpus.css` §18) holding a
MathJax `aligned` environment. The `&&` opens a right column for the per-line note, kept **purely
numeric** so it needs no words: `(P = 1/7,\ r = 2)`, `(2 \bmod 7 = 2)`, `(\tfrac17\cdot2=\tfrac27)`. A
`<div class="trace-label">` above it names the case (e.g. "Γύρος r = 2"). Trace the count too, not just
the threshold: `N_{\text{CH}} = T(n)\times|G| = \tfrac15\times50 = \tfrac{50}{5} = 10`.

**How much to trace.** Trace one representative case fully (in the worked exercise, two: a middle round
and the boundary round where the threshold hits 1), then give the remaining cases in a summary table. The
table is the reference; the trace is the teaching.

⛔ **Block `$$` maths break inside a `???`/`!!!` admonition.** `pymdownx.details` + `admonition` +
`md_in_html` (`markdown="1"`) does not recognise the block-maths pattern: a `$$...$$` (or a
`<div class="formula">$$...$$`) inside a collapsible renders as **inline** maths with a **stray `$`**
left in the text. Inside an admonition, write the maths as **inline** `\(\displaystyle ...\)` instead,
which renders as a proper display block. At the top level of a page, block `$$...$$` is fine. (Found on
the exam pages, where the answers live inside `??? answer-more`; the chapter traces are top-level and use
block `$$`.)

⚠ Greek inside `\text{}` **does** render in this MathJax setup (the cases labels "αν n ∈ G / αλλιώς"
prove it), so an earlier worry about Greek annotations was unfounded. Numeric notes are still preferred,
because they show the arithmetic rather than describe it.

## 13. Figure animation

Ruled by Chris, 2026-09-16. The generated step figures may be animated, and when they are, the animation
must **carry information the static panel only implies**, never decorate. Movement shows a mechanism (traffic
converging on the near-sink nodes), a process (a message travelling an option), or a timeline (the order in
which nodes die). If an animation would only be pretty, leave it off.

The classes and keyframes live in `corpus.css` §19 with generic names (`fig-flow`, `fig-strain`, `fig-die`),
so any chapter's generator can reuse them. The generators (`tools/ebp_figures.py` and siblings) tag the
elements; per-element timing (a death sweep, say) is set with an inline `animation-delay`.

The rules, each learned the hard way:

- ⛔ **Loop seamlessly: the `0%` and `100%` keyframe values must be identical.** A keyframe that ends on a
  different value than it starts snaps back instantly at the loop seam and reads as a **flash**. `figDie`
  starts and ends at `fill-opacity: 1`; `figFlow` steps the dash offset by exactly one dash period (`5 + 6`)
  so the stream restarts invisibly.
- ⭐ **Hold the meaningful end-state for most of the cycle.** The point of an animation is usually its
  *result*, not its transition. `figDie` spends ~70% of a long (20s) cycle in the dead state, with a short
  drain and a short refill, so the reader sits and looks at the empty network rather than watching it blink.
  Make the cycle long (tens of seconds), the transitions short, and the state you care about dominant.
- ⛔ **Respect `prefers-reduced-motion`: still everything, and make sure the resting frame still tells the
  story.** Under reduced motion the animation is `none`, so the element's *static* attributes must carry the
  meaning on their own: hot nodes stay red, dead nodes rest looking hollow (drawn as `fill-opacity: 0.06`,
  which is also `figDie`'s dead value), arrowheads still show direction. Never animate a fact that only
  exists while the animation runs.
- ⚠ **The figures sit below the fold, so animations must loop, not play once.** A one-shot animation finishes
  during page load, before the reader ever scrolls to it. (A future refinement could start them with an
  intersection observer, but looping is the current answer.)
- **Technique.** Flow along a line: `stroke-dashoffset` stepped by one dash period. Drain a node: animate
  `fill-opacity` (not `fill`), so the outline survives as the dead/hollow shape. Draw attention to a node:
  animate `opacity` (not `r`, which the figure audit skips and which can nudge overlap). Keep it slow.
