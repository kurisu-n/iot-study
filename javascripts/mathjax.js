/* MathJax, wired for Material's instant navigation.
 *
 * With navigation.instant on, a page change does not reload the document, so
 * MathJax never re-runs and formulas on the second page you visit stay as raw
 * LaTeX. Material publishes document$ for exactly this: it fires on every page
 * load, instant ones included.
 *
 * The delimiters match pymdownx.arithmatex's `generic: true` output. That
 * extension rewrites $...$ and $$...$$ in the Markdown into \( \) and \[ \],
 * so the source stays comfortable to write while MathJax sees unambiguous
 * delimiters that a stray dollar sign in prose cannot trigger.
 */
window.MathJax = {
  /* Do NOT typeset on load. MathJax normally typesets the page itself as soon
   * as it starts, and the document$ handler below typesets it again, so every
   * formula is processed twice. The second pass walks spans that already hold
   * a rendered mjx-container, finds the \( \) delimiters gone, and leaves them
   * alone: measured on this chapter, 10 of 21 inline formulas survived and the
   * rest stayed as raw LaTeX, with a stray backslash left in front of the ones
   * that did render. Handing the single typeset pass to document$ fixes both,
   * and is what makes instant navigation work at the same time.
   */
  startup: {
    typeset: false
  },

  tex: {
    /* Doubled backslashes on purpose: these are JavaScript string literals, so
     * "\\(" is the two characters \( that arithmatex emits. Written with single
     * backslashes, "\(" collapses to "(" and MathJax hunts bare parentheses
     * instead, matching from the wrong place in every formula on the page. */
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
