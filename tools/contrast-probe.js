/* Contrast probe: measures real rendered colour pairs on a chapter page.
 *
 * Companion to figure-audit.js, which checks text INSIDE figures. This checks
 * everything around them: step captions, the legend, the exam and extracurricular
 * boxes, and the table of contents.
 *
 * Two traps it exists to get right, both measured on 2026-09-16:
 *
 *  1. ALPHA. The table of contents fades with color-mix(... transparent), so its
 *     colours carry an alpha channel. Contrast is meaningless until the
 *     foreground is composited over what is actually behind it. Ignoring alpha
 *     reports a faded entry at full strength.
 *
 *  2. NOTATION. A color-mix() result computes to color(srgb r g b / a) with
 *     channels on a 0 to 1 scale, not rgba() on 0 to 255. Parsing it as rgba
 *     reads a pale blue as near black: it reported the dark-scheme contents at
 *     1.06:1 and the light-scheme contents as passing at 4.2:1, both false.
 *
 * Run it only right after a navigation. A hidden Browser pane suspends style
 * recalculation, so toggling the scheme in place returns stale colours.
 * To run: paste into the console, then  contrastProbe()
 */

function parseColor(c) {
  var n = c.match(/[0-9.]+/g).map(Number);
  if (/^color\(srgb/.test(c)) {
    return { r: n[0] * 255, g: n[1] * 255, b: n[2] * 255, a: n.length > 3 ? n[3] : 1 };
  }
  return { r: n[0], g: n[1], b: n[2], a: n.length > 3 ? n[3] : 1 };
}

function composite(fg, bg) {
  var f = parseColor(fg), k = parseColor(bg);
  return { r: f.r * f.a + k.r * (1 - f.a), g: f.g * f.a + k.g * (1 - f.a), b: f.b * f.a + k.b * (1 - f.a) };
}

function luminance(o) {
  return [o.r, o.g, o.b].map(function (v) {
    v /= 255;
    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
  }).reduce(function (sum, v, i) { return sum + v * [0.2126, 0.7152, 0.0722][i]; }, 0);
}

function contrastRatio(fg, bg) {
  var L1 = luminance(composite(fg, bg));
  var L2 = luminance(parseColor(bg));
  return +((Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05)).toFixed(2);
}

/* The first ancestor that actually paints a background. */
function paintedBackground(el) {
  while (el) {
    var b = getComputedStyle(el).backgroundColor;
    if (b && !/rgba\(0, 0, 0, 0\)|transparent/.test(b)) return b;
    el = el.parentElement;
  }
  return getComputedStyle(document.body).backgroundColor;
}

/* Resolves a custom property to a colour by letting the browser compute it. */
function tokenColor(name) {
  var probe = document.createElement("span");
  probe.style.color = "var(" + name + ")";
  document.body.appendChild(probe);
  var c = getComputedStyle(probe).color;
  probe.remove();
  return c;
}

function contrastProbe() {
  var body = document.body;
  var page = getComputedStyle(body).backgroundColor;
  var out = { scheme: body.getAttribute("data-md-color-scheme"), page: page, text: {}, graphics: {}, toc: {} };

  // Non-text marks inside the step panels, against the page. Need 3:1.
  ["--fig-node-soft", "--fig-node", "--fig-accent", "--fig-accent-deep",
   "--fig-ok", "--fig-warn", "--fig-event"].forEach(function (t) {
    out.graphics[t] = contrastRatio(tokenColor(t), page);
  });

  // Text components, each against whatever paints behind it. Need 4.5:1.
  //
  // ⛔ EVERY match is measured and the WORST is reported. This used to take the
  // first match only, and the first <p> inside an admonition is its title. So
  // "exam body" measured the tan title twice and never the body, and passed
  // while the body text was black at 87% on the dark box (2026-09-16). The
  // body selectors also exclude the title explicitly now.
  var sel = {
    "step caption": ".step__text",
    "step number": ".step__num",
    "legend": ".legend__item",
    "exam chip": ".exam-chip",
    "exam chip date": ".exam-chip strong",
    "extra tag": ".extra-tag",
    "extra title": ".admonition.extra > .admonition-title",
    "extra body": ".admonition.extra > p:not(.admonition-title), .admonition.extra li",
    "exam title": ".admonition.exam > .admonition-title",
    "exam body": ".admonition.exam > p:not(.admonition-title), .admonition.exam li, .admonition.exam strong",
    "table header": ".md-typeset table th",
    "table cell": ".md-typeset table td",
    "body text": ".md-typeset > p"
  };
  Object.keys(sel).forEach(function (k) {
    var worst = null;
    Array.prototype.forEach.call(document.querySelectorAll(sel[k]), function (e) {
      var r = contrastRatio(getComputedStyle(e).color, paintedBackground(e));
      if (worst === null || r < worst) worst = r;
    });
    if (worst !== null) out.text[k] = worst;
  });

  // Table of contents. Resting colours are read from the DOM; the "on" state is
  // scroll-driven and never fires in a hidden pane, so it is computed from the
  // same custom properties the stylesheet mixes, which is the same arithmetic.
  var nav = document.querySelector(".md-sidebar--secondary .md-nav--secondary");
  var h2 = document.querySelector(".md-sidebar--secondary .md-nav--secondary > .md-nav__list > .md-nav__item > .md-nav__link");
  var h3 = document.querySelector(".md-sidebar--secondary .md-nav--secondary > .md-nav__list > .md-nav__item > .md-nav > .md-nav__list > .md-nav__item > .md-nav__link");
  if (nav && h2) {
    var bg = paintedBackground(h2);
    var cs = getComputedStyle(nav);
    // The reader's position is painted in --toc-strong, which is not always
    // --c-primary (Warm Light uses a deeper tan). Resolve it ON the nav, where
    // it is declared, rather than assuming.
    var strongProbe = document.createElement("span");
    strongProbe.style.color = "var(--toc-strong)";
    nav.appendChild(strongProbe);
    var strongColor = getComputedStyle(strongProbe).color;
    strongProbe.remove();
    var strong = parseColor(strongColor);
    var mixed = function (pct) {
      return "rgba(" + strong.r + ", " + strong.g + ", " + strong.b + ", " + (parseFloat(pct) / 100) + ")";
    };
    out.toc["section, resting"] = contrastRatio(getComputedStyle(h2).color, bg);
    out.toc["section, reader is in it"] = contrastRatio(mixed(cs.getPropertyValue("--toc-fade-head-on")), bg);
    if (h3) out.toc["subsection, resting"] = contrastRatio(getComputedStyle(h3).color, bg);
    out.toc["active entry (--toc-strong)"] = contrastRatio(strongColor, bg);
  }

  out.textFailures = Object.keys(out.text).filter(function (k) { return out.text[k] < 4.5; });
  out.graphicFailures = Object.keys(out.graphics).filter(function (k) { return out.graphics[k] < 3; });
  return out;
}
