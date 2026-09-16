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
