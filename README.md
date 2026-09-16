# IoT Study

A study corpus for the MSc course **«Διαδίκτυο των Πραγμάτων»** (Internet of Things) at the
International Hellenic University.

The corpus is written in Greek prose with English technical terms, in the register of a university
textbook rather than a set of notes. It is built with MkDocs Material and published to:

**<https://iot.chris-nasiou.com/>**

## Repository layout

| Path | What it holds |
|:---|:---|
| `docs/` | The corpus itself. Everything under here is published. |
| `docs/chapters/` | One Markdown file per chapter. |
| `docs/stylesheets/` | The theme: four colour schemes and the diagram palette. |
| `Transcriptions/` | Lecture and exam material transcribed to Markdown. Source, not published. |
| `Corpus/` | The original single-file HTML draft of Chapter 1, kept for reference. |
| `hosting/` | Server configuration that ships with the build (`.htaccess`). |
| `COOKBOOK.md` | The living project document: method, style guide, theme system, progress. |
| `Session_Log.md` | What each working session did, and why. |

Only `docs/` reaches the site. The lecture PDFs, the transcriptions and the notes are carried in the
repository so it stands on its own, but MkDocs never sees them.

## Building it locally

```bash
pip install -r requirements.txt
mkdocs serve
```

The dev server mounts the site under the path in `site_url`. That path is now the domain root, so it
opens at `http://127.0.0.1:8000/` as you would expect. It served under `/iot-study/` while the site
was on GitHub Pages.

## How it deploys

`.github/workflows/deploy.yml` runs on every push to `main`: it builds with `--strict`, checks that
no chapter carries a literal colour, adds `hosting/.htaccess` to the output, and force-pushes the
result to the `deploy` branch. Hostinger's git integration pulls that branch and serves it; it runs
no build of its own, which is why the branch holds finished HTML and nothing else.

Source lives on `main`, built output lives on `deploy`, and the two never mix. **Push `main` and
nothing else** — each deploy replaces the `deploy` branch wholesale, so anything committed there by
hand is destroyed on the next build.

## The theme

Four colour schemes, cycled by the icon in the header: two light, two dark. The two warm ones are the
palette from the [FaceCue](https://facecue.net) documentation, which traces back to the FaceCue Unity
editor theme. `COOKBOOK.md` section 7 records where each value comes from.

Diagrams follow the scheme. Every colour inside a chapter's SVG resolves through a `--fig-*` token
rather than being written as a hex, and the build fails if that stops being true.

## Sources

The course material (lecture slides, past exam papers) belongs to its authors and is included here
for study. The prose, the diagrams and the worked examples are original.
