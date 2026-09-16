"""No shorthand anywhere: every abbreviation is defined before use, and linked back.

The rule (Chris, 2026-09-16). An abbreviation may appear on a page only after its
full name has been written out on that same page, immediately followed by the
abbreviation in parentheses: "Directed Diffusion (DD)". That first mention is the
definition. Every later use on the page links back to it, with the full name as
its tooltip. Greek abbreviations ("π.χ.", "διαφ.", "Δ2") are never allowed, and
neither are acronyms missing from terms.yml.

WHY PER PAGE. Readers open a chapter directly, from search or a link, so a term
defined in Chapter 1 would be undefined for someone who starts at Chapter 5. Each
page therefore defines what it uses, and every chapter reads on its own.

WHY A BUILD HOOK. A rule kept by hand across ten chapters drifts. This fails the
build on any violation, locally and in the deploy workflow alike, and it does the
linking itself so the Markdown stays readable: authors write "DD", not a link.

HOW. Works on the rendered HTML of each page (on_page_content), walking text nodes
in reading order and skipping the places shorthand cannot be judged or linked:
code, maths, SVG figures, existing links. Headings may not contain shorthand at
all, because a link inside a heading also lands in the contents column.
"""

import html
import re
from html.parser import HTMLParser
from pathlib import Path

import yaml
from mkdocs.exceptions import PluginError

TERMS_FILE = Path(__file__).resolve().parent.parent / "terms.yml"

# Text inside these is never checked or linked.
SKIP_TAGS = {"code", "pre", "script", "style", "svg", "math", "kbd", "samp", "a", "abbr", "dfn", "textarea"}
SKIP_CLASSES = {"arithmatex"}
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

# How much text before a first use is searched for the full name.
DEFINITION_WINDOW = 160

# Greek abbreviations, as a closed list: a generic "word followed by a full stop"
# pattern would match the end of every sentence.
GREEK_ABBREVIATIONS = re.compile(
    r"(?<![\wά-ώΆ-Ώ])"
    r"(π\.χ\.|κ\.λπ\.|κλπ\.?|δηλ\.|διαφ\.|σελ\.|χειρόγρ\.|σημ\.|βλ\.|μον\.|αρ\.|κ\.ά\.|σ\.\s*\d|Δ\d+)"
)
# Latin acronyms in capitals (DD, WSNs), and words with an inner capital (IoT).
ALLCAPS = re.compile(r"(?<![\w-])([A-Z][A-Z0-9]+)(s?)(?![\w-])")
INNER_CAP = re.compile(r"(?<![\w-])([A-Za-z]*[a-z][A-Z][A-Za-z]*)(?![\w-])")


def load_terms():
    data = yaml.safe_load(TERMS_FILE.read_text(encoding="utf-8"))
    terms = {key: list(names) for key, names in (data.get("terms") or {}).items()}
    proper = set(data.get("proper_names") or [])
    return terms, proper


def slug(key):
    return "abbr-" + re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")


class Walker(HTMLParser):
    """Re-emits the HTML exactly, handing each text run to a callback with its context."""

    def __init__(self, on_text):
        super().__init__(convert_charrefs=False)
        self.out = []
        self.stack = []
        self.on_text = on_text

    def _context(self):
        skip = False
        heading = False
        for tag, classes in self.stack:
            if tag in SKIP_TAGS or classes & SKIP_CLASSES:
                skip = True
            if tag in HEADINGS:
                heading = True
        return skip, heading

    def handle_starttag(self, tag, attrs):
        self.out.append(self.get_starttag_text())
        if tag not in VOID:
            classes = set((dict(attrs).get("class") or "").split())
            self.stack.append((tag, classes))

    def handle_startendtag(self, tag, attrs):
        self.out.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.out.append(f"</{tag}>")
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        skip, heading = self._context()
        self.out.append(self.on_text(data, skip, heading))

    def handle_entityref(self, name):
        self.out.append(f"&{name};")
        self.on_text_plain(html.unescape(f"&{name};"))

    def handle_charref(self, name):
        self.out.append(f"&#{name};")
        self.on_text_plain(html.unescape(f"&#{name};"))

    def handle_comment(self, data):
        self.out.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        self.out.append(f"<!{decl}>")

    def handle_pi(self, data):
        self.out.append(f"<?{data}>")

    def unknown_decl(self, data):
        self.out.append(f"<![{data}]>")

    # Replaced by the page processor so entity text still counts as "preceding text".
    def on_text_plain(self, text):
        pass


def process(page_html, page_name, terms, proper):
    errors = []
    defined = {}           # key -> tooltip text, once defined on this page
    recent = []            # the last stretch of plain text, for the definition check

    keys = sorted(terms, key=len, reverse=True)
    variants = "|".join(re.escape(k) for k in keys)
    term_re = re.compile(r"(?<![\w-])(" + variants + r")(s?)(?![\w-])")

    def remember(text):
        recent.append(text)
        joined = "".join(recent)
        if len(joined) > DEFINITION_WINDOW * 2:
            recent[:] = [joined[-DEFINITION_WINDOW * 2:]]

    def where(text, start):
        snippet = text[max(0, start - 30): start + 30].replace("\n", " ")
        return f"{page_name}: …{snippet}…"

    def on_text(raw, skip, heading):
        text = html.unescape(raw)
        if skip:
            remember(text)
            return raw

        for m in GREEK_ABBREVIATIONS.finditer(text):
            errors.append(f"Greek abbreviation {m.group(1)!r}, write it out. {where(text, m.start())}")

        for m in ALLCAPS.finditer(text):
            if m.group(1) not in terms:
                errors.append(f"Acronym {m.group(1)!r} is not in terms.yml. {where(text, m.start())}")
        for m in INNER_CAP.finditer(text):
            word = m.group(1)
            if word not in terms and word not in proper:
                errors.append(f"{word!r} looks like shorthand and is not in terms.yml or proper_names. "
                              f"{where(text, m.start())}")

        pieces = []
        last = 0
        for m in term_re.finditer(text):
            key = m.group(1)
            before_text = "".join(recent) + text[:m.start()]
            before = before_text[-DEFINITION_WINDOW:]
            pieces.append(html.escape(text[last:m.start()], quote=False))
            word = html.escape(m.group(0), quote=False)

            if heading:
                errors.append(f"Shorthand {key!r} in a heading; headings use the full name. {where(text, m.start())}")
                pieces.append(word)
            elif key not in defined:
                lower = before.lower()
                named = [n for n in terms[key] if n.lower() in lower]
                open_paren = lower.rfind("(") > lower.rfind(")")
                if named and open_paren:
                    defined[key] = terms[key][0]
                    pieces.append(f'<dfn class="abbr-def" id="{slug(key)}" title="{html.escape(terms[key][0])}">{word}</dfn>')
                else:
                    errors.append(
                        f"{key!r} is used before it is defined on this page. Its first use must follow "
                        f"its full name, e.g. \"{terms[key][0]} ({key})\". {where(text, m.start())}")
                    pieces.append(word)
            else:
                pieces.append(f'<a class="abbr-link" href="#{slug(key)}" title="{html.escape(defined[key])}">{word}</a>')
            last = m.end()

        remember(text)
        if not pieces:
            return raw
        pieces.append(html.escape(text[last:], quote=False))
        return "".join(pieces)

    walker = Walker(on_text)
    walker.on_text_plain = remember
    walker.feed(page_html)
    walker.close()
    return "".join(walker.out), errors


# Problems are collected across every page and reported once at the end, so a
# single build lists everything to fix rather than stopping at the first page.
_problems = []


def on_pre_build(config):
    _problems.clear()


def on_page_content(html_text, page, config, files):
    terms, proper = load_terms()
    result, errors = process(html_text, page.file.src_uri, terms, proper)
    _problems.extend(errors)
    return result


def on_post_build(config):
    if not _problems:
        return
    # Written as UTF-8 beside the build, because a Windows console prints the
    # Greek in these messages as \u escapes.
    report = Path(config["config_file_path"]).resolve().parent / "shorthand-report.txt"
    report.write_text("\n".join(_problems) + "\n", encoding="utf-8")
    listing = "\n  - ".join(_problems)
    raise PluginError(f"Shorthand rule, {len(_problems)} problem(s), also in {report.name}:\n  - {listing}")
