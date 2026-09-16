/* Turns Material's palette cycler into a dropdown.
 *
 * Material ships a one-button cycler: each click advances to the next scheme,
 * so reaching the fourth from the first takes three clicks and you cannot see
 * what you are choosing. With four schemes that is a poor way to pick one.
 *
 * ⭐ This does NOT replace Material's palette machinery, it drives it. Material
 * renders a radio per scheme (`input#__palette_N[data-md-color-scheme]`) and
 * listens for changes on them, writing the scheme onto <body> and remembering
 * the choice in localStorage. The menu below simply clicks the right radio, so
 * persistence, the scheme attribute and the instant-navigation handling all
 * stay Material's problem rather than becoming ours.
 *
 * The markup it reads, confirmed against Material 9.7.7:
 *
 *   form[data-md-component="palette"]
 *     input#__palette_0[data-md-color-scheme="..."]   scheme 0
 *     label[for="__palette_1"]                        scheme 0's icon and name
 *     input#__palette_1[data-md-color-scheme="..."]   scheme 1
 *     label[for="__palette_2"]                        scheme 1's icon and name
 *     ...
 *
 * ⚠ Note the offset: label N carries scheme N's icon and title, but its `for`
 * points at scheme N+1, because in the cycler the label IS the "go to next"
 * button. So inputs and labels are paired by INDEX, never by the `for`
 * attribute. Pairing by `for` gives every entry the wrong icon, off by one,
 * which looks plausible enough to ship.
 */

(function () {
  "use strict";

  var OPEN_CLASS = "is-open";

  function buildMenu(form) {
    var inputs = Array.prototype.slice.call(
      form.querySelectorAll("input.md-option[data-md-color-scheme]")
    );
    var labels = Array.prototype.slice.call(form.querySelectorAll("label"));
    if (inputs.length < 2) {
      return; // One scheme, or markup we do not recognise. Leave Material alone.
    }

    // Each scheme's icon and name come from the label at the SAME index.
    var schemes = inputs.map(function (input, i) {
      var label = labels[i];
      return {
        input: input,
        scheme: input.getAttribute("data-md-color-scheme"),
        name: (label && label.getAttribute("title")) || input.getAttribute("aria-label") || "",
        icon: (label && label.innerHTML) || ""
      };
    });

    // Material's own labels are the cycler. Hide them rather than remove them,
    // so nothing Material does later trips over a missing node.
    labels.forEach(function (label) {
      label.setAttribute("hidden", "");
      label.setAttribute("aria-hidden", "true");
    });

    var wrap = document.createElement("div");
    wrap.className = "theme-menu";

    var button = document.createElement("button");
    button.type = "button";
    button.className = "theme-menu__button md-header__button";
    button.setAttribute("aria-haspopup", "true");
    button.setAttribute("aria-expanded", "false");
    button.setAttribute("title", "Θέμα εμφάνισης");

    var buttonIcon = document.createElement("span");
    buttonIcon.className = "theme-menu__button-icon";
    button.appendChild(buttonIcon);

    var list = document.createElement("div");
    list.className = "theme-menu__list";
    list.setAttribute("role", "menu");

    var items = schemes.map(function (entry, i) {
      var item = document.createElement("button");
      item.type = "button";
      item.className = "theme-menu__item";
      item.setAttribute("role", "menuitemradio");
      item.setAttribute("aria-checked", "false");
      item.dataset.index = String(i);

      var icon = document.createElement("span");
      icon.className = "theme-menu__icon";
      icon.innerHTML = entry.icon;

      var name = document.createElement("span");
      name.className = "theme-menu__name";
      name.textContent = entry.name;

      /* The swatch is painted by the scheme itself. Every scheme is declared in
       * corpus.css as an attribute selector, not as a rule on <body>, so giving
       * this span the attribute resolves that scheme's own tokens inside it
       * while the rest of the page keeps the active one. */
      var swatch = document.createElement("span");
      swatch.className = "theme-menu__swatch";
      swatch.setAttribute("data-md-color-scheme", entry.scheme);
      swatch.appendChild(document.createElement("i"));

      item.appendChild(icon);
      item.appendChild(name);
      item.appendChild(swatch);

      item.addEventListener("click", function () {
        entry.input.click();
        close();
        button.focus();
      });

      list.appendChild(item);
      return item;
    });

    wrap.appendChild(button);
    wrap.appendChild(list);
    form.appendChild(wrap);

    /* Which scheme is live, according to the page itself.
     *
     * ⚠ Deliberately NOT `input.checked`. Material restores a remembered scheme
     * after this menu is built, so at build time no radio is checked yet and
     * reading them puts the tick on the first entry. That is invisible while
     * the first entry is also the default, which is exactly the case here, so
     * the bug only shows for a reader who has chosen something else and comes
     * back. The attribute on <body> is the thing Material actually maintains.
     */
    function activeScheme() {
      return document.body.getAttribute("data-md-color-scheme");
    }

    function sync() {
      var live = activeScheme();
      var activeIndex = -1;
      schemes.forEach(function (entry, i) {
        if (entry.scheme === live) {
          activeIndex = i;
        }
      });
      if (activeIndex < 0) {
        schemes.forEach(function (entry, i) {
          if (entry.input.checked) {
            activeIndex = i;
          }
        });
      }
      if (activeIndex < 0) {
        activeIndex = 0;
      }
      buttonIcon.innerHTML = schemes[activeIndex].icon;
      button.setAttribute(
        "aria-label",
        "Θέμα εμφάνισης: " + schemes[activeIndex].name
      );
      items.forEach(function (item, i) {
        var on = i === activeIndex;
        item.setAttribute("aria-checked", on ? "true" : "false");
        item.classList.toggle("is-active", on);
      });
    }

    function open() {
      wrap.classList.add(OPEN_CLASS);
      button.setAttribute("aria-expanded", "true");
      document.addEventListener("click", onDocumentClick, true);
      document.addEventListener("keydown", onKeydown, true);
    }

    function close() {
      wrap.classList.remove(OPEN_CLASS);
      button.setAttribute("aria-expanded", "false");
      document.removeEventListener("click", onDocumentClick, true);
      document.removeEventListener("keydown", onKeydown, true);
    }

    function onDocumentClick(event) {
      if (!wrap.contains(event.target)) {
        close();
      }
    }

    function onKeydown(event) {
      if (event.key === "Escape") {
        close();
        button.focus();
      }
    }

    button.addEventListener("click", function (event) {
      event.stopPropagation();
      if (wrap.classList.contains(OPEN_CLASS)) {
        close();
      } else {
        open();
      }
    });

    /* Material writes the scheme on a change event, so this keeps the button
     * and the tick in step whether the change came from this menu or not. */
    form.addEventListener("change", sync);

    /* And this catches the writes that are not a change event: the remembered
     * scheme Material applies on load, after this menu has already been built.
     * Watching the attribute rather than racing it means the tick is right
     * whenever Material gets round to setting it. */
    if (typeof MutationObserver !== "undefined") {
      new MutationObserver(sync).observe(document.body, {
        attributes: true,
        attributeFilter: ["data-md-color-scheme"]
      });
    }

    sync();
  }

  function init() {
    var form = document.querySelector('form[data-md-component="palette"]');
    if (!form) {
      return;
    }
    /* With navigation.instant the header is not re-rendered between pages, so
     * the menu built on the first page is still there on the second. Building
     * it again would stack a second copy in the header. */
    if (form.dataset.themeMenu === "ready") {
      return;
    }
    form.dataset.themeMenu = "ready";
    buildMenu(form);
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(init);
  } else if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
