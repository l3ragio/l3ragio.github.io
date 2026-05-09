// Dynamic TOC collapse: replace the internal scrollbar with a smart
// "first 2 + active context + last 1" view. Items outside that window
// collapse and are represented by a vertical ellipsis (⋮) so the
// reader still perceives the structural depth of the post without an
// internal scroll affordance redundant with the browser scrollbar.
//
// As the reader scrolls the page, the active link changes (set by
// Chirpy's tocbot at xl+ or by our inline-toc.js IntersectionObserver
// at lg-only). A MutationObserver on #toc reacts to that class change
// and re-runs the windowing logic, so the visible slice tracks the
// reading position.
//
// Operates only on top-level li (H2 sections). Nested H3 lis ride
// along with their parent H2 - we do not split a nested group.

(function () {
  'use strict';

  var MQ_DESKTOP = '(min-width: 992px)';

  // Slot budget. Keep small so the TOC reads as a curated overview.
  var FIRST_KEEP = 2;
  var LAST_KEEP = 1;
  var WINDOW_BEFORE = 1;
  var WINDOW_AFTER = 1;

  // Re-entry guard: our own DOM mutations (adding/removing ellipses,
  // toggling .is-collapsed) trigger MutationObserver. Without a guard
  // we would loop forever.
  var updating = false;

  function getRootList() {
    var toc = document.getElementById('toc');
    if (!toc) return null;
    return toc.querySelector('ul');
  }

  function getTopLevelItems() {
    var root = getRootList();
    if (!root) return [];
    var out = [];
    for (var i = 0; i < root.children.length; i++) {
      var el = root.children[i];
      if (el.tagName === 'LI' && !el.classList.contains('toc-ellipsis')) {
        out.push(el);
      }
    }
    return out;
  }

  function findActiveIndex(items) {
    var toc = document.getElementById('toc');
    if (!toc) return -1;
    var activeLink = toc.querySelector('a.is-active-link');
    if (!activeLink) return -1;
    for (var i = 0; i < items.length; i++) {
      if (items[i].contains(activeLink)) return i;
    }
    return -1;
  }

  function clearEllipses() {
    var root = getRootList();
    if (!root) return;
    var nodes = root.querySelectorAll(':scope > li.toc-ellipsis');
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].parentNode.removeChild(nodes[i]);
    }
  }

  function insertEllipsisAfter(li) {
    var ell = document.createElement('li');
    ell.className = 'toc-ellipsis';
    ell.setAttribute('aria-hidden', 'true');
    ell.title = 'Sezioni omesse - scrolla per vederle';
    if (li.nextSibling) {
      li.parentNode.insertBefore(ell, li.nextSibling);
    } else {
      li.parentNode.appendChild(ell);
    }
  }

  function update() {
    if (updating) return;
    if (!window.matchMedia(MQ_DESKTOP).matches) return;

    updating = true;
    try {
      clearEllipses();

      var items = getTopLevelItems();
      var TOTAL = items.length;
      if (TOTAL === 0) return;

      // Slot budget. With first+last+window the natural cap is
      // FIRST_KEEP + LAST_KEEP + WINDOW_BEFORE + 1 + WINDOW_AFTER = 6.
      // If the whole list is small we just show everything.
      var ALWAYS_VISIBLE = FIRST_KEEP + LAST_KEEP + WINDOW_BEFORE + 1 + WINDOW_AFTER;
      if (TOTAL <= ALWAYS_VISIBLE) {
        for (var x = 0; x < items.length; x++) items[x].classList.remove('is-collapsed');
        return;
      }

      var activeIdx = findActiveIndex(items);

      var visible = {};
      function add(i) { if (i >= 0 && i < TOTAL) visible[i] = true; }

      // First N
      for (var i = 0; i < Math.min(FIRST_KEEP, TOTAL); i++) add(i);
      // Last M
      for (var j = Math.max(0, TOTAL - LAST_KEEP); j < TOTAL; j++) add(j);

      if (activeIdx === -1) {
        // No active section yet (top of post, before reader scrolls
        // into any section). Show a generous opening band so the TOC
        // does not look starved on first paint.
        for (var s = 0; s < Math.min(FIRST_KEEP + WINDOW_AFTER + 2, TOTAL); s++) add(s);
      } else {
        for (var k = activeIdx - WINDOW_BEFORE; k <= activeIdx + WINDOW_AFTER; k++) add(k);
      }

      // Apply visibility
      for (var m = 0; m < items.length; m++) {
        if (visible[m]) {
          items[m].classList.remove('is-collapsed');
        } else {
          items[m].classList.add('is-collapsed');
        }
      }

      // Insert ⋮ at every gap between visible indices.
      var sorted = [];
      for (var key in visible) {
        if (Object.prototype.hasOwnProperty.call(visible, key)) sorted.push(Number(key));
      }
      sorted.sort(function (a, b) { return a - b; });

      for (var n = 0; n < sorted.length - 1; n++) {
        if (sorted[n + 1] - sorted[n] > 1) {
          insertEllipsisAfter(items[sorted[n]]);
        }
      }
    } finally {
      updating = false;
    }
  }

  var scrollTimer = null;
  function scheduleUpdate() {
    if (scrollTimer) clearTimeout(scrollTimer);
    scrollTimer = setTimeout(update, 60);
  }

  function init() {
    update();

    window.addEventListener('scroll', scheduleUpdate, { passive: true });
    window.addEventListener('resize', scheduleUpdate, { passive: true });

    var toc = document.getElementById('toc');
    if (toc && window.MutationObserver) {
      var obs = new MutationObserver(function (mutations) {
        if (updating) return;
        for (var i = 0; i < mutations.length; i++) {
          var m = mutations[i];
          // childList: tocbot or inline-toc just populated/refreshed.
          // attributes (class): active link moved.
          if (m.type === 'childList' || m.attributeName === 'class') {
            scheduleUpdate();
            return;
          }
        }
      });
      obs.observe(toc, {
        subtree: true,
        childList: true,
        attributes: true,
        attributeFilter: ['class']
      });
    }
  }

  // Wait until at least one toc-link exists in #toc before the first
  // pass — otherwise we run on an empty list and bail without setting
  // up observers.
  function waitAndInit(attempts) {
    attempts = attempts || 0;
    var toc = document.getElementById('toc');
    if (toc && toc.querySelector('a.toc-link')) {
      init();
      return;
    }
    if (attempts > 30) return; // give up after ~3s
    setTimeout(function () { waitAndInit(attempts + 1); }, 100);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { waitAndInit(0); });
  } else {
    waitAndInit(0);
  }
})();
