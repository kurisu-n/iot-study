# IoT Study — Session Log

One running log for the whole IoT Study project. This is unrelated to FaceCue and does not follow
FaceCue's phase numbering or its changelog rule. Newest entry last.

The living document for the project is `COOKBOOK.md`; this file records what each working session did
and why, and the cookbook records the state that resulted.

---

## 2026-09-16 · Warm presets repainted in the FaceCue documentation palette

### What was asked

Bring the corpus's 🌙 Warm preset to the FaceCue documentation's dark colours, and its ☀️ Warm preset
to the FaceCue documentation's light colours. The two Warm presets had been invented from scratch in
the previous session (a solarized-ish light, a brown-and-amber dark) and Chris wanted them to be the
real thing instead.

### What the FaceCue palette actually is

Worth stating, because the chain is longer than it looks and the naming is easy to get wrong.

FaceCue's site and its documentation share **one** token file, `src/static/assets/fc-tokens.css` in
the `facecue-site-docs` worktree. It declares roughly seventy `--fc-*` tokens on `:root`, and those
values are the **dark** scheme — dark is FaceCue's default, not its alternate. The light scheme is a
second block, in `documentation/docs/stylesheets/facecue.css` under
`[data-md-color-scheme="facecue-light"]`, which re-declares only the tokens it changes.

The `--fc-*` values are themselves lifted from the FaceCue Unity editor theme, and the token file's
comments name the editor colour each one came from. So the full chain is: Unity editor theme →
`fc-tokens.css` → the docs site → this study corpus.

Between the `--fc-*` tokens and Material's own `--md-*` variables sits a third layer, the `--pg-*`
palette tokens, which is why a question like "what colour is a code block" has to be answered by
following `--md-code-bg-color` → `--pg-code-bg` → `--fc-section-header` rather than by reading one
line. Both code tokens and the callout fill were resolved that way.

### The mapping

Fifteen corpus variables against the FaceCue set. Most were direct: page to `--fc-panel`, alternate
surface to `--fc-section`, headings to `--fc-tan`, links and accents to `--fc-gold`, body to
`--fc-text`, captions to `--fc-text-muted`, borders to `--fc-section-border`, code to
`--fc-section-header` with `--fc-text-bright` on it.

Three needed judgement, because the corpus has components the documentation does not have:

**The formula box** is a centred, accent-bordered equation panel with no FaceCue counterpart. Given
`--fc-section` as fill inside its existing gold border, so it reads as a raised surface.

**The exam tip** was the one real mistake of the session, caught by measurement rather than by
reading. I first gave it FaceCue's green signal colour, on the reasoning that a note box wants a
green rule. Two things were wrong with that. FaceCue's callouts are not green at all — they are
ruled in `--fc-callout-border`, a warm gold hairline — so the green was an invention wearing the
palette's name. And the contrast probe put green on the light section surface at 3.46:1, under AA for
a bold 15px label, because `--exam-border` is both the rule colour *and* the heading text colour in
this component. Using `--fc-tan` solved both at once: it is the colour a FaceCue callout heads in,
and it measures 6.16:1 light and 8.25:1 dark.

**The table header** paints `--primary` as a *background*, which FaceCue never does with its tan.
That inverts the text requirement, so `--th-text` became the dark surface colour in both presets.

### Two defects found in passing

Both predate this session and both would have shown up as damage in the new presets:

1. `.comparison-box h4` had `color: #92400e` hard-coded. On any dark preset's warning fill that is a
   dark brown on a dark brown. Promoted to `--compare-h`, given a value in all four presets and a row
   in the colour picker, so it is now the sixteenth theme variable.
2. 🌙 Navy had `--th-text: #e2e8f0` over a `--primary` of `#a0cef8` — pale on pale, an unreadable
   table header in a preset nobody had opened. Set to the dark page colour.

Chapter 1 contains no `.comparison-box` yet, so the first defect had never rendered. It would have
appeared the first time a later chapter used one.

### Verification

Not eyeballed. A contrast probe run in the browser against the live computed values walks twelve
text-on-surface pairs plus the border, in both Warm presets:

- Dark: minimum 5.04:1 (muted caption on page), everything else 7:1 to 13.5:1.
- Light: minimum 5.11:1 (accent on page), everything else 5.4:1 to 14.7:1.
- Borders 1.58:1 dark and 1.65:1 light against the page, which is a hairline, not text, and is what
  FaceCue itself uses.

Both schemes were also rendered and looked at — the near-black page with tan headings in dark, the
warm off-white with dark brown chrome in light, and the tan table header bar in both.

⚠ The preview pane rendered at a heavy zoom throughout, so the screenshots only ever showed a
fragment of the page at a time. The numeric probe is what the verification actually rests on; the
screenshots confirmed the overall cast, not the detail.

### Housekeeping

`COOKBOOK.md` said the project root was `D:\Development\Codex Workspace\IoT Study\` in two places.
That path does not exist; the project is under `Claude Workspace`. Corrected both. Its progress log
also called the fourth preset "Dark Forest" when the code has always called it `dark-warm`.
Corrected. A new §7 in the cookbook records the theme system, the token sources, the three judgement
calls, the two repairs, and the rule that a new component gets a variable rather than a literal.

### Left open

- The corpus is still one chapter. §3 of the cookbook lists the remaining nine.
- The two untouched presets (Academic, Navy) are now the odd ones out stylistically. Whether they
  stay at all is Chris's call; they cost nothing to keep.
