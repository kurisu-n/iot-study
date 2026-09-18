/* A chapter group's name in the sidebar opens its first page.
 *
 * Ported from the FaceCue documentation (docs/assets/nav-sections.js), with one
 * change: this site uses Material's instant navigation and FaceCue's does not.
 *
 * Material draws a group with no page of its own ("Κεφάλαια") as one label that
 * folds the group, so the name and the arrow do the same thing and neither opens
 * a page. This finds the group's first page and makes a click on the NAME alone
 * go there, while the rest of the row keeps folding. The stylesheet gives the
 * name its own hover colour and hand cursor off the class set here (corpus.css
 * section 14), so the two behaviours look different before they are tried.
 *
 * ⚠ Instant navigation. FaceCue runs this once per page load. Here a page change
 * does not reload the document, so it runs on every document$ emission instead,
 * and marks each label it has handled so a label that survives a navigation is
 * not given a second click handler.
 */
(function () {
  "use strict";

  var LINKED = "fc-nav-section--linked";

  function firstPage(item) {
    var nav = item.querySelector(":scope > .md-nav");
    if (!nav) return null;
    var first = nav.querySelector(".md-nav__list > .md-nav__item > a.md-nav__link");
    // .href, not getAttribute: the attribute is relative to the page it was
    // rendered on, which instant navigation may already have left.
    return first ? first.href : null;
  }

  function link(item) {
    var label = item.querySelector(":scope > label.md-nav__link");
    var name = label && label.querySelector(":scope > .md-ellipsis");
    if (!label || !name || label.classList.contains(LINKED)) return;
    if (!firstPage(item)) return;

    label.classList.add(LINKED);
    name.setAttribute("role", "link");
    name.setAttribute("title", "Άνοιγμα της πρώτης σελίδας");

    name.addEventListener("click", function (event) {
      // The label would flip the fold checkbox on the same click.
      event.preventDefault();
      event.stopPropagation();
      // Read the target at click time rather than binding it once, so it is
      // right whichever page the reader has navigated to since.
      var href = firstPage(item);
      if (href) window.location.assign(href);
    });
  }

  function run() {
    var items = document.querySelectorAll(".md-sidebar--primary .md-nav__item--nested");
    for (var i = 0; i < items.length; i++) link(items[i]);
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(run);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
