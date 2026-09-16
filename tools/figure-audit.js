/* Figure audit: text overlap and text contrast for the corpus's inline SVGs.
 *
 * WHY THIS EXISTS. Chapter 1's flooding figure put its "SRC" label across the
 * edge of a 16px node, in the colour meant for text ON a filled accent. Most of
 * the lettering actually sat on the page, so on the light schemes it was white
 * on near-white and invisible. A colour-pair contrast sweep had passed it,
 * because the sweep checked the pair the label was DESIGNED for, not the pair it
 * actually landed on. This checks what is really behind each label.
 *
 * RULE BEING ENFORCED (Chris, 2026-09-16): text never overlaps other elements.
 * A label either sits clear on the page, or wholly inside one filled shape that
 * serves as its background, like a name inside a box. Anything else is a defect.
 *
 * HOW. Every SVG shape implements isPointInFill / isPointInStroke. For each
 * <text>, a grid of points across its bounding box is mapped into each other
 * shape's own coordinate space and tested, so transforms and curved paths are
 * handled exactly rather than by bounding-box guesswork.
 *
 * NOT A BUILD STEP. It needs a real browser layout, so it is run by hand against
 * a served page, under each colour scheme, and is kept here rather than in
 * docs/ so it never ships. To run it: open a chapter, paste this whole file into
 * the console, and call  auditFigures()  or  auditFiguresAllSchemes().
 *
 * Limits, stated so a clean report is read correctly:
 *  - Shapes with an <animate> child are skipped. They sweep across everything by
 *    design (the flooding ripples), so a static overlap test is meaningless.
 *  - Marker arrowheads are not tested; they are drawn from <defs>, not placed.
 *  - Contrast is text fill against the innermost filled shape wholly containing
 *    the label, else the page background. Stroke-only outlines are ignored for
 *    that purpose, since they draw nothing behind the text.
 */

function auditFigures(opts) {
  opts = opts || {};
  var SAMPLES = opts.samples || 7;      // grid resolution per axis over each label
  var PAD = opts.pad == null ? 1.5 : opts.pad;  // clearance required, in SVG units
  var TEXT_MIN = 4.5;                   // WCAG AA for text

  function lum(rgb) {
    var c = rgb.match(/\d+(\.\d+)?/g).slice(0, 3).map(Number).map(function (v) {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  function contrast(a, b) {
    var L1 = lum(a), L2 = lum(b);
    return +((Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05)).toFixed(2);
  }
  function paints(v) {
    return v && v !== "none" && !/rgba\(\s*\d+,\s*\d+,\s*\d+,\s*0\s*\)/.test(v);
  }
  function describe(el) {
    var s = el.tagName;
    ["cx", "cy", "x", "y", "x1", "y1"].forEach(function (a) {
      if (el.hasAttribute(a)) s += " " + a + "=" + el.getAttribute(a);
    });
    return s;
  }

  var pageBg = getComputedStyle(document.body).backgroundColor;
  var report = { scheme: document.body.getAttribute("data-md-color-scheme"), figures: [] };

  Array.prototype.forEach.call(document.querySelectorAll(".md-typeset figure svg"), function (svg, fi) {
    var svgInv = svg.getScreenCTM().inverse();
    var texts = Array.prototype.slice.call(svg.querySelectorAll("text"));
    var shapes = Array.prototype.slice.call(
      svg.querySelectorAll("circle, ellipse, rect, line, polyline, polygon, path")
    ).filter(function (el) {
      if (el.closest("defs, marker, clipPath, mask, pattern")) return false;
      if (el.querySelector("animate, animateTransform, animateMotion")) return false;
      return true;
    });

    var fig = { figure: fi + 1, labels: texts.length, defects: [] };

    // Label box in SVG root units, and a function to sample points across it.
    function boxOf(el) {
      var b = el.getBBox();
      var m = svgInv.multiply(el.getScreenCTM());
      var pts = [[b.x, b.y], [b.x + b.width, b.y], [b.x, b.y + b.height], [b.x + b.width, b.y + b.height]]
        .map(function (p) { var q = new DOMPoint(p[0], p[1]).matrixTransform(m); return [q.x, q.y]; });
      var xs = pts.map(function (p) { return p[0]; }), ys = pts.map(function (p) { return p[1]; });
      return {
        x0: Math.min.apply(null, xs) - PAD, x1: Math.max.apply(null, xs) + PAD,
        y0: Math.min.apply(null, ys) - PAD, y1: Math.max.apply(null, ys) + PAD
      };
    }
    function grid(bx) {
      var out = [];
      for (var i = 0; i < SAMPLES; i++) {
        for (var j = 0; j < SAMPLES; j++) {
          out.push([bx.x0 + (bx.x1 - bx.x0) * i / (SAMPLES - 1), bx.y0 + (bx.y1 - bx.y0) * j / (SAMPLES - 1)]);
        }
      }
      return out;
    }

    texts.forEach(function (t, ti) {
      var bx = boxOf(t);
      var pts = grid(bx);
      var label = (t.textContent || "").trim();
      var containers = [];

      shapes.forEach(function (sh) {
        var cs = getComputedStyle(sh);
        var fillOn = paints(cs.fill) && sh.tagName !== "line" && sh.tagName !== "polyline";
        var strokeOn = paints(cs.stroke) && parseFloat(cs.strokeWidth) > 0;
        // Map SVG-root points into this shape's own user space.
        var toLocal = sh.getScreenCTM().inverse().multiply(svg.getScreenCTM());
        var inFill = 0, inStroke = 0;
        pts.forEach(function (p) {
          var q = new DOMPoint(p[0], p[1]).matrixTransform(toLocal);
          var sp = svg.createSVGPoint(); sp.x = q.x; sp.y = q.y;
          if (fillOn && sh.isPointInFill(sp)) inFill++;
          if (strokeOn && sh.isPointInStroke(sp)) inStroke++;
        });
        var total = pts.length;
        if (inFill === total && inStroke === 0) {
          containers.push(sh);                       // wholly inside: a background
        } else if (inFill > 0 || inStroke > 0) {
          fig.defects.push({
            type: "overlap",
            label: label,
            with: describe(sh),
            detail: (inFill ? inFill + "/" + total + " points on its fill" : "") +
                    (inFill && inStroke ? ", " : "") +
                    (inStroke ? inStroke + "/" + total + " on its stroke" : "")
          });
        }
      });

      // Text against text.
      texts.forEach(function (o, oi) {
        if (oi <= ti) return;
        var ob = boxOf(o);
        if (bx.x0 < ob.x1 && ob.x0 < bx.x1 && bx.y0 < ob.y1 && ob.y0 < bx.y1) {
          fig.defects.push({ type: "overlap", label: label, with: 'text "' + (o.textContent || "").trim() + '"', detail: "label boxes intersect" });
        }
      });

      // Contrast against what is actually behind the label: the LAST (topmost)
      // wholly containing filled shape in document order, else the page.
      var behind = pageBg, behindWhat = "page";
      if (containers.length) {
        var top = containers[containers.length - 1];
        behind = getComputedStyle(top).fill;
        behindWhat = describe(top);
      }
      var ratio = contrast(getComputedStyle(t).fill, behind);
      if (ratio < TEXT_MIN) {
        fig.defects.push({ type: "contrast", label: label, on: behindWhat, ratio: ratio, need: TEXT_MIN });
      }
    });

    report.figures.push(fig);
  });

  report.defectCount = report.figures.reduce(function (n, f) { return n + f.defects.length; }, 0);
  return report;
}

/* Runs the audit under every scheme and restores the one that was active. */
function auditFiguresAllSchemes(schemes, opts) {
  schemes = schemes || ["warm-light", "warm-dark", "academic", "navy"];
  var prev = document.body.getAttribute("data-md-color-scheme");
  var out = {};
  schemes.forEach(function (s) {
    document.body.setAttribute("data-md-color-scheme", s);
    out[s] = auditFigures(opts);
  });
  document.body.setAttribute("data-md-color-scheme", prev);
  return out;
}
