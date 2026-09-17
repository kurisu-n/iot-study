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

---

## 2026-09-16 · Ported to a built site, and published

### What was asked

Make a repository for this, the same way the FaceCue website works. And: does the domain matter for
the repo name, or can any name be picked?

### The domain question

Any name. FaceCue's site is not GitHub Pages at all: Actions builds it and force-pushes the finished
HTML to a `deploy` branch, and Hostinger pulls that branch. The domain lives entirely in Hostinger's
configuration, so `FaceCue-Site` is an arbitrary name. The only case where a repository name is
forced is a GitHub Pages **user** site, which must be `<username>.github.io`.

Chris chose option C, the build-step architecture, with the name `iot-study`. Since the repository is
public, the serving end went to GitHub Pages rather than Hostinger: free, no domain, no paid plan.

### Retiring a principle

The cookbook recorded "self-contained, one HTML file, opens in any browser" as a design decision, and
option C is incompatible with it. Rather than quietly break it, it was put to Chris, who retired it.
The cookbook now carries the retirement and the reason inline, so a later reader does not find a
principle that the repository contradicts.

The port itself was cheap because of the palette work earlier the same day: FaceCue's documentation
*is* MkDocs Material wearing the two schemes we had just matched, so the corpus could reuse the
tokens directly and Material's palette toggle replaced the hand-built panel.

### The figures were theme-blind

Found while porting, not looked for. Every SVG in Chapter 1 carried literal hex colours from the
Academic palette: 21 distinct values, 178 occurrences. On a dark scheme the sensor-field ellipse
would have been a pale blue glowing on near-black.

The replacement is twenty `--fig-*` tokens declared per scheme. The substitution was done with `sed`
rather than by hand, which is what made it a ten-minute job instead of an afternoon, and the result
was verified by grepping for surviving literals (zero) and by reading the computed `fill` of real SVG
elements in all four schemes.

Academic maps every token back to its original literal, so it renders exactly as authored. That was
deliberate: it is the scheme the diagrams were drawn against.

### Three defects found by measuring, one of them mine

**The MathJax delimiters were wrong, and this is the one worth remembering.** The live config showed
`inlineMath: [["(", ")"]]` — bare parentheses — because the file contained `"\("` with a single
backslash, and `\(` is not a JavaScript escape, so it collapses to `(`. MathJax was hunting bare
parens, matching from the wrong place in every formula on the page.

What made this hard to see is that it *looked* like a partial failure: 10 of 21 inline formulas
rendered and 11 did not, which reads like a timing or config-scope problem. It was neither. All 21
were being matched wrongly; the 10 that "worked" had matched from a stray paren and left a visible
backslash in front of the output, and the 11 that failed had produced invalid TeX and been dropped.
The leftover backslash in the DOM was the actual tell, and I chased two wrong theories (double
typesetting, then the CDN) before reading the live `MathJax.config`.

⚠ The cause was a **bash heredoc eating the escape.** The project rule says to use the Edit tool for
anything with string literals rather than a heredoc; I used a heredoc for a JS file full of
backslashes and got exactly the failure the rule exists to prevent. Two heredocs failed this session,
the other on an apostrophe. Use Write and Edit for content.

The other two:

- `$$...$$` followed immediately by another line is parsed as part of the same paragraph and rendered
  **inline**, not as display maths. Needs a blank line after it.
- A `$...$` inside a figure caption never converts at all, because Markdown passes raw HTML blocks
  through untouched. Written as an explicit `<span class="arithmatex">` instead.

### Verification

Against the **live** site, not the local build, since a 200 proves only that a file exists:

- 20 of 20 inline formulas and 3 of 3 display blocks typeset, zero MathJax errors, no raw `$` left.
- All four schemes cycle from the header toggle, and the figure's field fill changes with each one:
  `#ebf4ff` → `#eae4d5` → `#2a4365` → `#2a2620`.
- Contrast measured against two thresholds, 4.5:1 for text and 3:1 for non-text graphics. Warm Light,
  Navy and Warm Dark pass every pair. Three fixes were needed to get there: Warm Light's sensor dots
  were at 2.41:1, and the figure labels in both dark schemes sat just under 4.5:1.
- The build's own colour guard runs clean.

⚠ The preview pane clipped or mis-rendered almost every screenshot this session. The numeric probes
are what the verification rests on; screenshots only ever confirmed the overall cast.

### Left open, and one decision waiting

- ~~Academic fails contrast in three places and was left alone on purpose.~~ **Ruled by Chris the
  same day: fix it. Done, see the entry below.**
- ~~Search runs the English lunr pipeline, because lunr ships no Greek stemmer.~~ **Wrong reason,
  corrected later the same day: lunr does ship a Greek stemmer. See the entry below.**
- Nine chapters still to write.
- The lecture PDFs (46 MB) are committed so the repository stands alone. MkDocs never sees them; only
  `docs/` is published.


---

## 2026-09-16 (later) · Academic contrast fixed, and a fifth failure found while fixing it

### What was asked

Fix the Academic contrast too. And: is this a problem — *"This repository is missing a package.json
file. Add a package.json file to your repo to enable full import, or continue as a static website."*

### The fixes

Four values in Academic were solved rather than eyeballed: each original was walked toward black in
one per cent steps until it cleared its threshold, which keeps the hue and changes only the depth.
Thresholds applied were 4.5:1 for anything that is text and 3:1 for a non-text graphic, so the sensor
dots were held to the looser bar and the figure labels to the stricter one.

`--c-muted` and `--fig-label` were the same colour in the original palette and were kept the same
afterwards, both landing on `#626f83`, so the scheme still has one muted colour rather than two that
nearly match.

⚠ Academic is no longer byte-identical to the first draft, which it was on purpose until today. That
is recorded at the top of its block in `corpus.css` and in cookbook section 7.6.

### The fifth failure, which was mine

Adding `muted/altbg` and `muted/formulabg` to the probe surfaced a pair nobody had measured:
**Warm Dark muted text on the section surface, 4.08:1.**

It would have been easy to file this under "FaceCue's palette, leave it" and move on. It is not.
FaceCue uses `--fc-text-muted` for subtitle text on the *panel*, where it measures 5.04:1. This
corpus also puts muted text on the *section* surface, in the formula box caption and under figures,
which FaceCue never does. Our composition, our fix: the token is brightened to `#95908B`, enough to
clear 4.5:1 on the section, and every other Warm Dark value is still FaceCue's.

⭐ The lesson is about the probe, not the palette. The first sweep checked muted text against the
page and passed it; the failure lived on a surface the sweep never paired it with. **A contrast probe
certifies the pairs it was given, not the design.** When a token is used on more than one surface,
every surface has to be in the list.

### Verification

All four schemes, sixteen text pairs and four graphic pairs each: no failures anywhere. Lowest text
figure is 4.59:1 (Academic), lowest graphic figure 3.20:1 (Academic sensor dots). Build clean under
`--strict`, colour guard clean.

### The package.json message

Not a problem, and nothing to act on. It comes from a host's import wizard (Vercel, Netlify,
Cloudflare Pages and similar all say a version of it) looking for a Node project to run a build
command against. This corpus has no Node in it at all: it is Python and MkDocs, and the build already
happens in GitHub Actions.

⛔ The thing not to do is accept such an importer's offer to "continue as a static website" against
`main`. `main` holds Markdown source, not HTML. The built site lives on `gh-pages`, and a host
pointed at `main` would serve the raw sources. Nothing is missing and nothing needs adding.

---

## 2026-09-16 (later still) · Moved to iot.chris-nasiou.com, GitHub Pages removed

### What was asked

Chris pointed at `https://iot.chris-nasiou.com/docs/`, then chose to serve at the **root** of that
subdomain and to remove GitHub Pages.

### What was already true

The subdomain answered 403 at both `/` and `/docs/`. That is Hostinger's empty-directory response,
not a permissions fault: DNS resolves, TLS works, nothing had been deployed. Both `iot.chris-nasiou.com`
and `facecue.net` sit on the same Hostinger edge (`92.113.x`, `Server: hcdn`), so the FaceCue deploy
pattern transfers exactly.

`/docs/` would have been an empty prefix on every URL. It exists on `facecue.net` because the
Eleventy marketing site holds the root there; here the subdomain is dedicated to one thing. Chris
chose the root.

### What changed

- `site_url` to `https://iot.chris-nasiou.com/`. This is load-bearing: canonical tags, the sitemap
  and the search index base all come from it, and `mkdocs serve` mounts under its path.
- The workflow publishes to **`deploy`** instead of `gh-pages`, the FaceCue convention, because
  Hostinger pulls a branch and runs no build.
- A new `hosting/.htaccess`, copied into the build by the workflow. It cannot live under `docs/`,
  because MkDocs skips dotfiles.
- GitHub Pages disabled, and the `gh-pages` branch deleted.

### The .htaccess, and why it is not improvised

The cache rules follow the FaceCue site's, which the website rulebook records as measured against the
live host rather than reasoned about. The rule that matters: **nothing is immutable unless its
filename carries a content hash**, because a cache header that has gone out cannot be withdrawn.

Checked rather than assumed, by running the regex over the real build output: Material's own bundles
(`bundle.d7400e89.min.js`, `main.ec1eaa64.min.css`, `palette.ab4e12ef.min.css`, `search.2c215733.min.js`)
match the 8-hex-character pattern and get a year. Our three editable files (`corpus.css`,
`fc-tokens.css`, `mathjax.js`) do not match and get five minutes with revalidation, which is what
lets a colour edit reach a returning reader.

⛔ The immutable rules sit *below* the generic css/js rule in the file. With `Header set` the later
match wins, so moving them up would let the five-minute rule overwrite the one-year rule.

Also carried over: `ErrorDocument 404 /404.html` as a local path, never a full URL. A URL there makes
the server redirect, which turns a missing page into a 302 to something that answers 200, and search
engines read that as a real page.

### A correction to the previous entry

The earlier log said search falls back to English *because lunr ships no Greek stemmer*. That is
wrong, and I found it while listing the build output for the cache check: `lunr.el.min.js` is right
there in the bundle, carrying `el.stemmer`, `el.trimmer` and `el.stop`.

The real reason is narrower. Material's **search plugin** does not accept `el` as an index language.
Setting `lang: el` builds fine and prints *"Option search.lang 'el' is not supported, falling back to
'en'"*. Measured against Material 9.7.7.

The practical effect is the same, so nothing needed fixing, but the reason matters: it means this may
simply start working on a Material upgrade, which "lunr has no Greek stemmer" would have ruled out
forever. Worth re-testing after each upgrade.

⭐ The general shape of this: a wrong *reason* attached to a right *observation* survives review,
because the observation keeps checking out. It only fell over when an unrelated task listed the same
directory.

### Left open

- **Hostinger's git integration still has to be pointed at the `deploy` branch** in hPanel, with the
  subdomain's docroot as the target. That is the one step that cannot be done from here. Until then
  the subdomain keeps answering 403, and that is expected rather than a fault.


---

## 2026-09-16 (evening) · Theme selector as a dropdown, FaceCue Ανοιχτό by default

### What was asked

Hostinger confirmed working. Then: turn the theme button into a dropdown that shows all four and lets
you pick; make the FaceCue light scheme the default; order them FaceCue light, FaceCue dark, light,
dark. Mid-way, Chris added: title-case the names.

### The approach

Material's palette control is a cycler, so a dropdown means custom code, and there were two ways to
write it. A fully custom selector would own its own localStorage and scheme switching, duplicating
logic Material already has and drifting from it. The menu written instead **clicks Material's own
radios**, so persistence, the `<body>` attribute and instant navigation all stay Material's. The menu
stores nothing.

Default and order both come from `mkdocs.yml`: Material treats the first palette entry as the default,
and the menu lists entries in file order.

### Four bugs, every one found by testing

The first two came from reading Material's markup before writing anything, which is the only reason
they were never shipped:

- **Label N carries scheme N's icon, but its `for` points at scheme N+1**, because in the cycler the
  label is the "next" button. Pairing by index, not by `for`.
- **`toggle.name` described the next click**, as it should for a cycler. Rewritten to name each scheme
  itself.

The other two only appeared in testing, and both were the kind that passes the obvious check:

**The tick was on the wrong row after a reload.** The first test cleared storage, loaded the page,
and saw the tick on "FaceCue Ανοιχτό", which was correct, because that is the default. It only broke
for a *remembered* non-default: `navy` applied, tick still on row 1. Material restores the choice
after the menu is built, so reading `input.checked` at build time found nothing checked. Now reads the
attribute on `<body>` and watches it with a `MutationObserver`.

⭐ A default-state test cannot catch a bug whose symptom *is* the default state. The check has to
start from something other than the default.

**A second icon appeared in the header, and the dark swatch was light.** These only showed once a
screenshot rendered properly, after numbers had passed. Diagnosed before fixing:

- Material toggles `hidden` on its labels on every scheme change, undoing the menu's one-time `hidden`.
  Now hidden by a CSS rule it cannot toggle.
- The Warm Dark swatch resolved `--fc-panel` to `#FAF8F3`, Warm Light's value. Warm Dark had always
  *inherited* its `--fc-*` tokens from `:root`, which only works while it is the outermost scheme. The
  swatch nests it inside `<body data-md-color-scheme="warm-light">`, where inheritance finds Warm
  Light's tokens first. This was a latent flaw in the scheme structure, not in the swatch: the swatch
  was just the first thing to nest one scheme in another. Warm Dark now declares all nineteen tokens.

### A detour: a stale dev server

Mid-test, instant navigation landed on `/iot-study/`, the old base path. Before touching config, the
build output was checked and found clean; the only mentions of `iot-study` were historical comments.
The `mkdocs serve` process had been started before `site_url` moved to the root and was still
mounting the old path. Restarted, and the problem went with it.

⚠ `mkdocs serve` picks up content and most config changes live, but not a change to the mount path.
After editing `site_url`, restart it.

### Verification

- Fresh visitor gets `warm-light`; menu order FaceCue Ανοιχτό, FaceCue Σκούρο, Ακαδημαϊκό, Σκούρο Μπλε.
- Every item applies its scheme, moves the tick, and closes the menu; outside click and Escape close it.
- A remembered non-default survives reload with the tick on the right row.
- Instant navigation: one menu (not two), choice carried over, figure follows the scheme, maths still
  typesets 20 of 20.
- Exactly one visible header icon under every active scheme.
- Every swatch resolves identically under all four active schemes.
- Page contrast regression after restructuring Warm Dark: figures unchanged, all four still pass.

### Left open

- A reader who picked a scheme on the old GitHub Pages address loses it: Material namespaces the
  storage key by base path, and the path changed.


---

## 2026-09-16 (night) · Chapter 1 rebuilt as the template

### What was asked

Four things, with the instruction to nail Chapter 1's voice, style and structure before expanding:

1. The "SRC" label in the flooding figure was invisible on both light schemes. More generally, never let
   text overlap other elements.
2. Make the table of contents look like the FaceCue documentation's; it was crowded.
3. Content: (a) the four DD phases were hand-waved, reinforcement especially; show each phase step by step,
   2 to 4 steps, and mark anything extracurricular clearly. (b) End every section with "what to expect on
   the exam", based on past papers, with dates.

### Grounding first

Nothing was written until the sources were read: Lecture 2 in full (DD, slides 1 to 39), Lecture 3's
framing slides, the handwritten notes for pages 1 to 9, 12 and 15 to 16, and all three exam papers.

That reading is what the rest of the session stands on, and it turned up more than gaps:

- **Four factual errors in the existing chapter**, all plausible on a read-through: that sensors cannot
  transmit directly to the BS (they can; EBP depends on it), that the interest flood is a one-off cost
  (the sink refreshes it periodically), that phases 1 and 2 are sequential (the same reception does both),
  and that flooding is never deployed (DD floods its own interests).
- **What "hand-waved" meant, concretely.** Reinforcement is the same interest resent with a tenfold rate,
  and a node that receives a rate higher than what it is getting reinforces a neighbour of its own, which
  is how the path is built hop by hop back to the source (Δ2, διαφ. 16). The old chapter said only that
  "the sink reinforces the fastest path". Also missing: the forwarding rate rule and down-conversion
  (διαφ. 14), task generation and interest aggregation (διαφ. 10), loops that cannot be broken (διαφ. 21).
- **A notation clash** between slides ($n$ sources, $m$ sinks) and notes ($m$ for sources).
- **Exam dates as they actually survive:** 6 February 2026, 15 February 2025, and only "February 2022".
  A Viber photo dated the day before the 2026 exam turned out to be the 2025 paper, not new guidance.
- **A suspicion that was wrong.** "Energy holes" looked like my own addition and would have been marked
  extracurricular. It is in the notes and on Δ3, διαφ. 4. Checked before marking.

### The figures: a tool first, then the fix

Rather than patch the one label, `tools/figure-audit.js` was written to check every label against every
shape, using `isPointInFill` and `isPointInStroke`, and against what is actually behind it. Run first on
the unchanged chapter, it had to reproduce the reported bug to be trusted, and it did: "SRC" at **1.0:1 on
the page**. It also found ten other defects that nobody had reported.

Root cause of "SRC", stated plainly because the earlier sweep had passed it: the label was drawn in the
colour for text *on* an accent fill, but it straddled a 16px node and sat mostly on the page. The sweep
had checked the pair the label was designed for, not the pair it landed on.

Defects went 11, then 2, then 0 across all four schemes. Two of the fixes were geometric (stacked labels
too close, a label clipped by a sideways-offset arrow) and one was a colour misuse (event red, a graphic
colour, used as text; the fix was the scheme's existing deep variant, no new token).

### Four of my own tools and scripts were wrong at some point

Worth recording because each one produced a confident, plausible answer:

- **The contrast probe ignored alpha**, so the faded contents column read at full strength.
- **It then misparsed `color(srgb …)` notation**, whose channels run 0 to 1, as 0 to 255. That reported the
  dark-scheme contents at 1.06:1, a false failure, and the light-scheme contents as passing, a false pass.
  Diagnosed by reading the computed colour string rather than by editing CSS that was already correct.
- **A bash heredoc ate escapes twice more**: once breaking a Python f-string's `\n`, once on apostrophes.
  The project rule says to use the Edit tool for string literals; after the second failure, all prose and
  code went through Write and Edit.
- **The generator's in-place apply rewrote all 452 lines** as CRLF on Windows while changing no figure.
  Caught by insisting the apply be byte-idempotent; fixed with `newline=""`.

### The failure no measurement could catch

With every numeric check passing, a real screenshot (headless Edge, since the Browser pane would not
render reliably) showed the step panels were unreadable in the warm schemes. The accent (#86642A), amber
(#8F6B10) and deep tan (#533E0F) are one family of browns, so an interest, a data message and a
reinforcement were visually the same line. Each colour passed contrast against the page; they failed
against *each other*, and no contrast check measures that.

Fixed by giving the warm schemes' figures FaceCue's own signal colours (blue for the sink and interests,
green for gradients, red for the source) plus a derived orange for data, and by making the active-node
ring a dotted neutral that shares no hue with any arrow. Re-screenshotted in both warm schemes, then
re-measured: 0 figure defects, 0 text failures, 0 graphic failures in all four schemes.

### What was built

- **Chapter 1**, rewritten against the sources: every course claim cited as (Δ2, διαφ. N) or to the notes;
  a comparison table of the exploratory and reinforced interest; seven exam boxes; one extracurricular
  block and one extracurricular tag, the latter on a comparison-table row the slides never evaluate.
- **22 step panels** in six figures (overview, four phases, repair), from `tools/dd_panels.py`, living in
  the chapter between comment markers so the generator can rewrite them in place.
- **The FaceCue contents column**, with `toc_depth: 3`, measured and matching FaceCue's documented numbers.
- **The index page** now explains citations, the extracurricular mark, the exam boxes, and lists the three
  papers with what can and cannot be trusted about each.
- **Cookbook §9**, the chapter template, so Chapter 2 starts from settled rules.

### Open, for Chris

1. **Exam box placement.** "At the end of each section" was taken literally: seven boxes, several saying
   "not examined". The alternative is one rollup per chapter.
2. **Voice.** The rewrite has no em dashes, following the FaceCue documentation's copy rules. Nobody has
   ruled those rules apply here.
3. **Contents column at rest.** Faithful to FaceCue means resting section entries at 2.35 to 2.99:1, below
   AA by design. One dial raises it.

## 2026-09-16 (late) · Chapter 2: LEACH

### What was built

Chapter 2, `docs/chapters/02-leach.md`, live at
https://iot.chris-nasiou.com/chapters/02-leach/ (commit `33bfef8`, Actions run 35106217585 green):

- **§2.1 the idea** (clusters, heads, why the role rotates), **§2.2 rounds and phases** (the set-up and
  steady phases from the notes reconciled with the slides' three-phase split), **§2.3 the election
  mechanism** (the T(n) threshold, the induction that shows the head count stays constant, the slide
  example with N=100 P=0.2 including the r=5 "new era" answer), **§2.4 the worked 2026 Β.1**, **§2.5 the
  experimental evaluation** (dead-node distributions, the lifetime table from slide 66), **§2.6 limits and
  extensions**. Every claim cited to the slides, notes or exam. Plain language, no shorthand, no em dashes,
  an exam box per section, extracurricular marks on TEEN/PEGASIS and the static-clustering aside.
- **`tools/leach_figures.py`**, four figures: two rounds side by side (2.1), one round step by step (2.2),
  the seven-round era over 70 nodes (2.3), and the schematic dead-node distributions (2.4). All labels in
  HTML, all colours `--fig-*`, markers rewritten in place. Added `.steps--four` to `corpus.css` §11.
- Nav and index card for chapter 2, chapter 1's forward link, the new LEACH terms in `terms.yml`.

### Two source problems handled in the text

- **Slide 53 typo.** The derivation prints the third-round threshold as `P₂ = 1/(1-2P)`. It is
  `P₂ = P/(1-2P)`: the induction and the general T(n) for r=2 both give the P in the numerator, and
  `1/(1-2P)` would exceed 1 for small P. Corrected inline in a `!!! warning`, with the derivation.
- **"14%" vs 1/7.** The 2026 Β.1 says 7-round eras and 14% heads. Those are consistent only for P=1/7
  (14.29%); the chapter works in 1/7 and an extracurricular note shows the literal 0.14 breaks (era does
  not close in 7 rounds, and r=7 would give T=7).

### Verified

Build `--strict` clean; shorthand hook 10/10 and 0 page problems after fixing LEACH-in-heading, the P₀/P₁
math subscripts read as acronyms, and TEEN/PEGASIS in an admonition title before their definition. The CI
literal-hex guard finds no literal colour in the built chapter. Headless-Edge screenshots (warm-light)
confirm all four figures, the MathJax formulas, and both worked tables render correctly; a warm-dark
capture of the page top confirms the dark tokens apply (the chapter adds no new colour CSS, so the dark
components are Chapter 1's, already validated).

### Open, for Chris

1. **Schematic dead-node figure (2.4).** The three panels (MTE dead near the BS, DT dead far, LEACH
   uniform) are distinct but not dramatically so. If you want the contrast sharper I can retune the seed
   and counts. It is explicitly labelled schematic.
2. Still deferred from before: publishing the lecture PDFs so slide citations can link to a page.

## 2026-09-16 (late) · Exam papers section

Chris asked for a section before `Κεφάλαια`, one page per exam, each drawn as close to the original as
possible, with a short and an expanded answer per question (answering only what the current chapters
cover, and populating the rest as chapters land).

### Built

- **`Θέματα Εξετάσεων` nav section** before the chapters, with `docs/exams/2026.md`, `2025.md`, `2022.md`.
- **Facsimiles.** Each page opens with a framed cream sheet reproducing the original: header, course and
  date, name and student-number fill-in lines, the return note, the θέματα with their marks, and the
  2026 ETX topology diagram as a small inline SVG. The 2026 layout was matched against the original photo
  (`ΙοΤ - Θέματα 2026.jpg`). The 2025 and 2022 papers came from the `.docx` files, extracted with the
  venv python. The institution's logo artwork was not reproduced; text header only.
- **Answers.** Short (`!!! answer`, open) and expanded (`??? answer-more`, collapsed) per question, with a
  marks chip on each heading. Covered now: 2026 Α.1 (DD, via Ch1), 2026 Β.1 (LEACH, via Ch2, linking the
  worked example), and the WSN energy-waste part of 2022 Θέμα 2Γ (via Ch1). Everything else carries a
  `!!! todo` naming the chapter that will fill it.
- **The 2022 answer file was NOT used.** It is student-notes style, not instructor material (index
  ruling), so only the questions were reproduced.

### Traps handled

- **The facsimile is verbatim source**, so its acronyms must not be touched by the no-shorthand rule.
  Added `exam-facsimile` to `hooks/shorthand.py` `SKIP_CLASSES`. The answers below obey the rule normally.
- `corpus.css` §16-17: the facsimile frame (fixed cream + dark ink so it is legible in all four schemes),
  the `answer` / `answer-more` / `todo` admonitions, the `q-marks` chip, and a `.steps--four`-style
  responsive shrink for narrow screens.

### Verified

Build `--strict` clean, shorthand hook 10/10 and 0 page problems, deploy green (run 35112336858), all
three pages live (200). Headless-Edge screenshots confirm the 2026 facsimile matches the original and the
answer blocks render (short open, expanded collapsed, todo muted).

### A4 refinement (same day)

Chris asked the facsimiles to be A4-proportioned like the original, with a slightly larger font, splitting
to a second page only if a paper will not fit. Each `.exam-sheet` became an A4 page (aspect-ratio 210:297),
type sized in `cqi` so it scales with the sheet, A4 as a minimum with `overflow: visible` so nothing clips.
A first attempt split 2026 and 2022 into two sheets, on a fill measurement taken in the narrow preview pane
(which inflates line-wrapping to ~1.7 A4). Chris pointed out they fit one page at real width; measured at the
capped 46rem width, all three fit one A4 at ~1.95cqi (≈14px, larger than the previous fixed size), so the
splits were reverted. Cookbook §11 updated with the sizing rule and the measure-at-real-width caveat.

## 2026-09-16 (late) · Smallest-step formula traces

Chris asked that solving the cluster-head threshold be broken into the smallest steps, showing which number
replaces which symbol, and the same for every formula solve. Added a `.trace` block (corpus.css §18): a
MathJax `aligned` derivation, one substitution or operation per line, with a purely numeric right-column
note. Applied to the LEACH slide example (2.3, r=2), the worked 2026 exercise (2.4, r=2 and the r=6
threshold-hits-1 case), and the exam 2026 Β.1 answer, each also tracing the head count
`N_CH = T(n)×|G|`. Tables kept as summaries.

Trap found and recorded (cookbook §12): block `$$` maths inside a `???`/`!!!` admonition (pymdownx.details
+ md_in_html) renders as inline with a stray `$` — the exam page's existing B.1 formula was already broken
this way, unseen because the panel is collapsed by default. Fixed by using inline `\(\displaystyle ...\)`
inside admonitions; top-level block `$$` is fine. Also confirmed Greek renders in `\text{}` here, so the
earlier concern was moot. Built strict, deployed green, both chapter (block) and exam (inline) traces
verified rendering.

## 2026-09-16 (late) · Chapter skeleton, then Chapter 3 (Energy Balance Protocol)

Chris asked to build the full menu skeleton first, with placeholder pages marked by a symbol, so the
reading/writing order and what gets deferred are visible, then move on to the next chapter (still exam/notes
priority order).

### Skeleton

Chapters 3 to 12 created as placeholder pages in priority order, each with a `todo` box stating what it
covers, which exam questions it answers, its priority, and its sources. Placeholders carry a `☆` in the
nav label. Order: notes-covered first (EBP, ETX, energy synthesis, scalar/vector), then rest of 2026
(LPWAN/LoRaWAN), then 2025/2022 theory, then the unexamined rest (RPL, application protocols, WPT). Index
explains the `☆` and that the order is priority, not textbook order. Added CoAP and MQTT to terms.yml.

### Chapter 3: Energy Balance Protocol

Grounded in Lecture 3 (slides 1 to 29) and notes pages 12 to 16. The lecture goes deep (probabilistic
recurrence, closed form, linear-programming lifespan maximisation, distributed potential algorithm); the
notes are the accessible tier. Wrote the chapter around the accessible tier plus the energy model, marking
the deep recurrence/LP as beyond the basic scope:

- 3.1 efficiency vs balance, 3.2 why every scheme strains some nodes, 3.3 the slice-and-dice probabilistic
  idea (hop with p_i, direct with 1-p_i), 3.4 the energy model with a traced E[ε] expansion and the balance
  property, 3.5 how p_i behaves (far→hop, near→direct), 3.6 energy holes and FND/HND/LND, 3.7 the DD
  comparison the 2026 Α.2 asks for.
- `tools/ebp_figures.py`: three figures (strain patterns, the per-node choice over a sliced network, energy
  holes vs uniform drain), HTML labels only, `--fig-*` colours, marker-rewritten.
- Filled the exam 2026 Α.2 answer (DD vs EBP, short + expanded) now that the chapter covers it; removed the
  `☆` from chapter 3's nav label.

### Trap

The hook read `iR` and `cR²` written as plain text in prose as inner-cap shorthand. Fixed by wrapping them
in inline math `\(iR\)`, `\(cR^2\)`. General rule: symbolic quantities in prose go in math, not plain text.

Built strict clean, deployed green (skeleton and chapter as separate commits). Next: routing metrics and
ETX (chapter 4), the last 2026 exercise.

## 2026-09-16 (late) · Chapter 3 p_i formula, then Chapter 4 (routing metrics + ETX)

### Chapter 3: the computable p_i (new section 3.6)

Chris asked whether "how p_i is chosen" should be added. Assessment: the *derivation* (the recurrence and
exact closed form) is graduate-level and out of proportion with the exam's arithmetic exercises, so it stays
in the beyond-scope box. But the *closed approximate form* p_i = 1 - 3x/((i+1)(i-1)), p_2 = 1/2 (slide 17)
is exactly the LEACH-shaped plug-and-chug that could become an exercise, and it makes 3.5's qualitative
behaviour concrete. Added it as section 3.6 with a traced p_3 and a table p_2..p_6 (rising toward 1),
renumbered lifetime/comparison to 3.7/3.8, reconciled the two boxes that said "not needed".

### Chapter 4: routing metrics and ETX

Both of Chris's leanings (next-on-notes, 2026 Θέμα Δ) point here. Grounded in Lecture 4/5 (the full ETX
taxonomy) and notes pages 15-16 (ETX = 1/(d_f d_r), the worked energy example). The 2026 Δ.1 is the notes'
Example 2 applied to two links: per-attempt cost of a 5m link = E_c*b + E_tx(5)*b + E_c*b = 40*200 + 25*200
+ 40*200 = 21000 nJ; A→B = 4.3*21000 = 90300; B→C = 1.5*21000 = 31500; total = 121800 nJ = 121.8 μJ.
Wrote 4.1-4.7 (link quality, the metric, the 3-route example, advantages/limits, the energy model with a
traced Example 2, the worked Δ.1 traced in three steps, and a brief breadth section for MOR/ExOR/LTP/PFR
marked beyond scope). `tools/etx_figures.py` for the 3-route and A-B-C figures. Filled the exam 2026 Δ.1
answer. All three 2026 exercises now written.

### Traps

- The hook flagged `nJ` (inner-cap) as shorthand; it is a unit, added to proper_names. `ACK` needed a
  terms entry + a define-first ("Acknowledgement (ACK)"). Two section headings had `ETX` in them; renamed
  to acronym-free headings.
- The dev server (`mkdocs serve` on 8090) wedged again mid-session and served an Edge error page to a
  screenshot; killed the PID and restarted via preview_start. Build itself was always clean.

Built strict clean, deployed green (chapters 3.6 and 4 as separate commits). Next: chapter 5 (energy-
management synthesis) or 6 (scalar/vector, after reading Lecture 9), then priority 2 LoRaWAN.

### Chapter 6 and the scalar/vector settlement (same day)

Chris asked whether the p_i formula is in the handwritten notes: it is NOT. The notes (§17-18) describe the
concept of a calculated per-ring p_i and contrast it with LEACH's uniform p, but never write the formula;
the only threshold formula the notes work out is LEACH's T(n). The p_i closed form is slide-only (Lecture 3,
slide 17). Softened chapter 3's §3.6 exam box accordingly: unlike the LEACH and ETX exercises (which the
notes work through with numbers), this one is slide-only, so a long shot, given "as a safety, not a
prediction".

Then "do 6+9 to settle it": read Lecture 9 to settle the scalar/vector question, and wrote Chapter 6.
Settled: the notes' scalar/vector (sensor data: temperature vs wind velocity) and Lecture 9's Scalar
Charging Model / Vector Model (wireless-power-transfer physics: additive Friis power vs the 2D electric
field with phase under charger interference) are DIFFERENT concepts sharing only the words. Chapter 6 is the
notes' sensor-data concept, with a §6.3 box holding the distinction; the charging models stay for the WPT
chapter (priority 4). Short chapter (not examined), one hand-authored two-panel figure (thermometer, vector
arrow). Cookbook §10 note updated from "check" to "settled". Built strict clean, deployed green.

## 2026-09-16 (late) · Chapter 5 (synthesis) and Chapter 7 (LoRaWAN)

**Chapter 5, energy management synthesis.** A short capstone tying chapters 1 to 4: the shift from
node-centric/IP to data-centric and hierarchical, the realization that the goal is smart distribution not
just low consumption, and a toolbox table (aggregation, clustering, role rotation, probabilistic balancing,
path selection) mapping each method to what it does and which chapter. Notes-sourced (page 17), not
examined.

**Chapter 7, LPWAN and LoRaWAN.** Priority 2, the last real 2026 exam topic (Θέμα Γ, 2.5 marks). Grounded
in Lecture 6a (LoRaWAN architecture, data rates, Spreading Factor) and Lectures 7b/8a/8b (Wi-Fi). Covers:
what LPWANs are; the LoRaWAN architecture (end devices, gateways, network server, application server;
multicast; 0.3-50 Kbps) with a hand-authored architecture figure; the Spreading Factor and the
range/rate/energy trade-off (Ts = 2^SF/BW = 32.8 ms for SF=12, traced, and the key exam point that higher SF
means more energy because time on air grows exponentially); and the Wi-Fi comparison (opposite design
goals). Filled the exam 2026 Γ.1, Γ.2, Γ.3 answers. **The entire 2026 exam is now answered (A, B, C, D).**

Traps: many acronyms in the new chapter. Fixed LPWAN/LoRaWAN in headings, added SF to terms and LoRa/kHz to
proper_names, defined IEEE and SF on the pages that use them, mathified BW (proper_names does not silence
ALLCAPS, only inner-cap), and replaced π.χ. with "για παράδειγμα". Both chapters built strict clean and
deployed green.

Chapters done: 1, 2, 3, 4, 5, 6, 7. Remaining are priority 3 (2025/2022 theory: IoT system design, access
protocols, cloud/edge/Industry 4.0, 802.11ah/security/smart cities) and priority 4 (RPL, application
protocols, wireless power transfer).

## 2026-09-16 (later) · Chapter 8 (IoT system design), first tier-3 chapter

**Chapter 8, designing an IoT system.** Priority 3, the first purely 2025/2022 theory chapter. Steps back
from inside-the-network to the whole-system, sensor-to-app view. Grounded in Lecture 7b slide 3 (the
authoritative "IoT common architecture": Edge-side Thing/Radio/Gateway/Connectivity, Cloud-side
Ingestion/Processing, User-side Apps), Lecture 7a (IoT elements and the PAN/LPWAN/Cellular technology
zones), and the two exam questions themselves.

Content: (8.1) the three-side architecture; (8.2) the examined five-layer IoT OSI model (End Points,
Connectivity, Middleware, IoT Services, Apps) as a table mapped to both the traffic and irrigation examples,
plus a hand-authored layer-stack figure, and an "εκτός ύλης" box reconciling it with the extra-notes
Perception/Network/Processing/Application/Security naming; (8.3) technology selection and "no single
technology fits all"; (8.4) a full worked irrigation system with a control-loop architecture figure;
(8.5) implementation challenges; (8.6) benefits.

**Grounding calls.** The 2022 answer file is student-notes style, so only its *questions* and the five
layer names were treated as authoritative, not its prose. The two competing five-layer models were
reconciled rather than picked between (they are the same jobs under different names; the extra-notes model's
only real addition is pulling security into a cross-cutting layer). The exam names are led with because 2022
asks for them by name.

**Exam answers filled.** 2025 Θέμα 1 (irrigation, 4 marks, fully in-chapter). 2022 Θέμα 3 (traffic, 4
marks): part 1 (five layers) full; part 2 (connectivity security) scoped now with a pointer to chapter 11;
part 3 (cloud vs edge) answered on principle with the systematic comparison deferred to chapter 10. 2022 2Ε
("no single technology") filled from 8.3.

**Traps.** OSI, LoRaWAN and IoT flagged as used-before-defined on several pages; fixed by reordering the OSI
definition ahead of "IoT OSI", defining Long Range Wide Area Network (LoRaWAN) at first use in the table,
defining Internet of Things (IoT) in the index intro, and dropping the OSI acronym from the 2022 answer.
Renamed two headings to drop IoT/OSI. Added OSI and TLS to terms, ZigBee to proper_names. Built strict
clean; both figures verified present in the DOM with correct shape and legend counts (the preview pane was
suspended so screenshots came back blank, a known gotcha).

Chapters done: 1 to 8. Remaining: tier 3 chapters 9 (access protocols), 10 (cloud/edge/Industry 4.0), 11
(802.11ah/security/smart cities), and tier 4 chapter 12 (RPL, application protocols, wireless power).

## 2026-09-17 · Chapter 9 (access protocols)

**Chapter 9, comparing access protocols.** Priority 3. Answers the one question asked *identically* in
2022 (Θέμα 2Α) and 2025 (Θέμα 2α): the three most important criteria for comparing IoT access protocols.
Grounded in Lecture 8a (the shared-medium collision problem, the contention-vs-scheduled classification on
slide 9, CSMA and its backoff, and slide 33's "ideal = perfect scheduling"). Structure: 9.1 the shared
medium and collisions; 9.2 the two families (contention/CSMA vs scheduled/TDMA, plus centralized vs
distributed) with a timeline figure contrasting a collision-and-gaps contention row against clean TDMA
slots; 9.3 the three criteria (energy efficiency, scalability, latency/reliability), each tied to the
contention-vs-scheduled trade-off.

**Grounding call.** The course gives no closed "three criteria" list, and the only answer artifacts are the
two student-notes files, which give slightly different triads (both include energy efficiency and security;
they differ on the third). Framed it honestly as a propose-and-justify question with a source note, led with
the triad that ties to real access-protocol characteristics (energy, scalability, latency/reliability), and
told the reader security is an equally valid third if justified. Dropped the placeholder's claim that this
chapter also answers 2022 2Ε (already answered in chapter 8) and corrected the sources to 8a.

**Exam answers filled.** 2025 Θέμα 2α and 2022 Θέμα 2Α (the twice-asked question), each short + expanded.
No new terms needed (avoided ALOHA and QoS acronyms; used CSMA/TDMA/MAC, all already defined). Built strict
clean; figure structure verified in the DOM (9 rects, 2 axes, 3 legend items); deployed green and confirmed
live.

Chapters done: 1 to 9. Remaining tier 3: chapter 10 (cloud/edge, Industry 4.0, standardisation, 2025 2β to
2δ) and chapter 11 (802.11ah, security, WSN/MANET, smart cities, 2022 Θέμα 1 and 2Β to 2Δ); then tier 4
chapter 12.

## 2026-09-17 · Dark-theme consistency and the key-term sweep

**Dark theme (task b).** In warm-dark the key-term pills and blockquotes were filled with the warm
HubGroupBackground (#2a2620), the only warm-fill surface on the neutral #141414 panel, so they read as
inconsistent. Pointed --c-highlight at the neutral HeadlessBoxBackground (#2e2d2c) in warm-dark only; the
other schemes keep their own highlight. Added a shared radius scale (--r-inline 4px, --r-box 6px) and
applied it to key-terms, quotes, formulas, admonitions and legends, replacing a grab-bag of 0/2/3/4/6/8 px
corners. Deployed green.

**Key-terms recalibrated and swept (task a).** Chris's rule: a key-term pill marks only a term the student
would have to PRODUCE as an exam answer, the subject X of a question or an item of an enumerable answer
(characteristics, phases, layers, criteria, causes); bullet-label leads included. Everything else stays
bold. Acronym-entangled terms (cluster head/CH, FND, SF): pill the spelled-out concept once, never the
shorthand definition itself (it breaks the hook), leave the acronym link. Not inside the exam-answer boxes.
Recorded as COOKBOOK §9.11.

Chapter 1 recalibrated from 14 loose pills to 5 answer-terms (dropped sink, routing protocol, the two
caches, local repair, Omniscient Multicast). Swept the rest: ch2 LEACH (6: clusters, cluster head, rounds,
the two phases, the three characteristics), ch3 EBP (9: efficiency/balance, hop-by-hop/direct, slices,
energy hole, FND/HND/LND), ch4 ETX (2: link quality, expected transmissions), ch5 (3: node/data-centric,
hierarchical), ch6 (2: scalar/vector), ch7 (4: the four LoRaWAN architecture components), ch8 (13: five IoT
OSI layers, four challenges, four benefits), ch9 (5: the two families, the three criteria). Built strict
clean; the IoT-Services pill correctly nests the acronym link.

## 2026-09-17 · Chapter 10 (cloud/edge, Industry 4.0, standardisation) and template repairs

**Chapter 10.** Tier 3. Answers 2025 Θέμα 2β, 2γ, 2δ, and backs 2022 Θέμα 3 part 3. The extra notes looked
thin (the 2025 questions appear there with no answers), but the real material is in lectures not read
before: Lecture 7b slides 14 to 24 (IIoT, the nine Industry 4.0 technologies, slide 20's four
characteristics verbatim, the vibration-sensor predictive-maintenance example and the time-to-failure
ladder, "End-to-End IoT System spans Edge/Fog and Cloud"), Lecture 8b slides 49 to 66 (standard
definitions, six benefits, de facto vs de jure, SDO principles, the full IEEE lifecycle with the 75%/75%
ballot), and Lecture 7a's Tactile Internet 1 ms budget (0.3 + 0.2 + 0.5 ms, computation budgeted with the
base station), which became the course-grounded latency argument for edge computing.

Cloud vs edge is the one question no slide answers directly. The three differences (location, latency,
capacity) and the similarity (parts of one system) are each tied to a course statement; the
speed-of-light argument and the other commonly cited differences (bandwidth, privacy, offline) sit in
flagged extra boxes. Two hand-authored figures: the edge/cloud decision paths (short vs long return) and
the four characteristics as a sense-communicate-decide-act loop, the loop explicitly marked as a memory
aid rather than course content. 23 answer-term pills. New terms: IETF, IIoT, IPv6, 6LoWPAN, M2M, MEC,
OASIS, SDO. Built strict clean on the first try.

**Grounding corrections found while writing.**
- `Lectures_6a_7a.md` is Lecture 6a up to line 109. The technology zones, 802.15.4, 6LoWPAN, CoAP, MQTT
  and the 5G/MEC slide are 6a, not 7a or 7b. Fixed Chapter 8's citations (zones now "6a and 7a", CoAP and
  MQTT now 6a), the 2022 2Ε answer, and the CoAP/MQTT comments in terms.yml.
- COOKBOOK §9.11 (written the previous turn) claimed a pill around a full name breaks the shorthand hook's
  definition detection. False: the hook joins text across tags and searches a 160-character window.
  Corrected the section, pilled Spreading Factor in Chapter 7, and verified the SF dfn and all nine SF
  links survive.
- Chapters 8 and 9 had a single chapter-level exam section instead of Chris's one-box-per-section rule.
  Both now have one `!!! exam` box with all three chips per section. Chapter 9's intro claimed we "know the
  instructor likes" the criteria question (contradicts the index note that the instructor's identity is
  unknown for 2022/2025); reworded. Its exam note gave 2025 as 1 mark; it was 1.5.
- Chapter 8 §8.1 said "the next chapter" for the next section.

The 2026 and 2025 papers are now fully answered. Chapters done: 1 to 10. Remaining: chapter 11 (tier 3),
chapter 12 (tier 4).

## 2026-09-17 · Chapter 11 (802.11ah, addressing and security, WSN vs MANET, smart cities)

**Chapter 11.** Last tier-3 chapter. Answers 2022 Θέμα 1, 2Β, 2Γ (all three parts), 2Δ, and part 2 of
Θέμα 3. **All three exam papers are now fully answered.**

Grounding: 802.11ah goals from Lecture 8b slide 26 (sub-1 GHz, extended range, power efficiency, many
devices) and the decisive evidence in Lecture 8a slide 27, the rate-vs-range chart (802.11ac 3.5 Gbps at
10 to 30 m, 802.11ah at 200 m to 4 km); 802.11ah is now part of IEEE 802.11-2020 (8b slide 25). Addressing
and security appear only as named challenges (7b slide 50) plus scattered mechanisms: IPv6 and 6LoWPAN
(6a), Wi-Fi association and authentication (8a slides 25-26), 802.11ai/bi/bn (8b), mobile sink reducing
adversarial overhearing (Lecture 10 slide 6); standard measures (TLS, certificates, access control) sit in
a flagged extra box. WSN vs MANET: WSN definition from Lecture 9 slide 12, MANET from 8a's taxonomy
(slide 22), WSN challenges from Lecture 2 slide 7, MANET challenges from Lecture 3 slide 3 ("DD suitable
for low dynamics", verified verbatim) and Lecture 10 slide 5; table cells the course is silent on carry
extra-tags. Smart cities: services from Lecture 7a, 5G requirements (7b slide 8), eMBB/mMTC/URLLC (7a),
ITU KPIs (7b slides 9-10), small cells (7b 43-45); the city "characteristics" are derived from 7b slide 24
and the chapter says so. Two figures (rate-vs-range bars on a log scale; WSN vs MANET panels with a broken
link). 38 answer-term pills after removing a redundant sentence. New terms: ITU, eMBB, mMTC, URLLC.

**Correction found while grounding.** Lecture 7b slide 32 lists deafness, idle listening and overhearing
as MAC energy waste. Chapter 1's exam box and the 2022 2Γ answer both claimed overhearing was not in the
slides; both corrected.

## 2026-09-17 · Revision section: formula sheet, overview, exercise and theory variants

Chris asked, after chapter 11, for a τυπολόγιο, a per-chapter overview for the days before the exam, and
variant exercises and variant theory questions as one section of two pages. Nav, after Κεφάλαια:
Τυπολόγιο, Επισκόπηση, and Εξάσκηση (Παραλλαγές ασκήσεων, Παραλλαγές θεωρίας). Linked from the home page.

- **Τυπολόγιο** (`revision/formulas.md`): 13 formula boxes covering every formula in chapters 1 to 11
  (flooding and Omniscient Multicast cost, LEACH threshold with era length, expected cluster heads and the
  P1/P2 derivation with the slide-53 typo flagged, the EBP cost, mean energy, balance property and p_i
  approximation, ETX and the link energy model, LoRa symbol time, the 1 ms latency budget), each with
  symbols, traps and a status chip, plus a table of numbers worth memorising.
- **Επισκόπηση** (`revision/overview.md`): a priority order led by the two 2026 exercises, then one section
  per chapter with exam chips, the essentials as bullets with answer-terms pilled, and a note that chapter
  12 is unwritten and unexamined.
- **Παραλλαγές ασκήσεων** (`practice/exercises.md`): 10 exercises. LEACH: a 4-round era with a
  random-number decision; the "12% with 8 rounds" rounding trap; a node outside G and the era rollover.
  ETX: metric and path sum; route choice plus energy of both routes; a three-link topology with different
  lengths where the shortest link is the most expensive. EBP: p_5 and p_7; E[ε] against always-hop and
  always-direct. LoRa: SF and bandwidth ratios. Flooding: how cost grows from N = 100 to 400. All numbers
  hand-computed; browser check with every solution opened: 20 traces, 150 math elements, zero untypeset
  traces, zero MathJax errors.
- **Παραλλαγές θεωρίας** (`practice/theory.md`): 27 questions across chapters 1 to 11, each labelled as a
  variant of a named exam question or new, with an exam-length answer skeleton and a section link.

Recorded the conventions as COOKBOOK §14, including the rule that these pages must be updated in the same
commit as any chapter change they summarise.
