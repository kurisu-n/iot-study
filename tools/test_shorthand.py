"""Tests for hooks/shorthand.py: it must FAIL on each kind of shorthand, not only pass clean pages.

A checker that only ever sees correct pages proves nothing, so most cases here are
deliberately broken input. Run by the deploy workflow before the build.

    python tools/test_shorthand.py
"""
import importlib.util
import sys

from pathlib import Path
HOOK = Path(__file__).resolve().parent.parent / "hooks" / "shorthand.py"
spec = importlib.util.spec_from_file_location("shorthand", HOOK)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
terms, proper = mod.load_terms()

cases = [
    # (name, html, expect_errors, must_contain)
    ("use before definition fails",
     "<p>Το WSN είναι δίκτυο.</p>", 1, None),
    ("definition then link",
     "<p>Ένα ασύρματο δίκτυο αισθητήρων (Wireless Sensor Network, WSN) μετρά.</p><p>Κάθε WSN έχει κόμβους.</p>",
     0, ['<dfn class="abbr-def" id="abbr-wsn"', '<a class="abbr-link" href="#abbr-wsn"']),
    ("shorthand in a heading fails",
     "<p>Directed Diffusion (DD) είναι πρωτόκολλο.</p><h2>Τα όρια του DD</h2>", 1, None),
    ("Greek abbreviation fails",
     "<p>Όπως στη διαφάνεια (Δ2, διαφ. 16).</p>", 2, None),
    ("unregistered acronym fails",
     "<p>Η κεφαλή CH εκλέγεται.</p>", 1, None),
    ("inner-capital shorthand fails",
     "<p>Το WiFi είναι γνωστό.</p>", 1, None),
    ("proper name passes",
     "<p>Η παλέτα του FaceCue.</p>", 0, None),
    ("code, maths and svg are ignored",
     '<p><code>WSN</code> <span class="arithmatex">\\(DD\\)</span></p><svg><text>(BS)</text></svg>', 0, None),
    ("plural definition and use",
     "<p>Wireless Sensor Networks (WSNs) και WSNs.</p>", 0, ['id="abbr-wsn"', 'href="#abbr-wsn"']),
    ("expansion far away does not count as definition",
     "<p>Directed Diffusion" + " κείμενο" * 40 + ". Το DD λειτουργεί.</p>", 1, None),
]

failed = 0
for name, html_in, expect, must in cases:
    out, errors = mod.process(html_in, "test.md", terms, proper)
    ok = len(errors) == expect and all(m in out for m in (must or []))
    failed += not ok
    print(("PASS " if ok else "FAIL ") + name + (f"  (errors={len(errors)}, expected {expect})" if not ok else ""))
    if not ok:
        for e in errors:
            print("     ", e)
        print("      out:", out[:300])

print(f"\n{len(cases) - failed}/{len(cases)} passed")
sys.exit(1 if failed else 0)
