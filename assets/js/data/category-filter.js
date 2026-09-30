/**
 * Home category filter.
 *
 * Capsules in #category-filter toggle which categories are active.
 * A card in #post-list is hidden iff none of its data-categories
 * intersect the active set. State persists in localStorage so the
 * user's filter survives page navigation and reload.
 *
 * Default: every category is active.
 *
 * Empty state: when no card matches, #post-list gets is-empty-state
 * which the SCSS uses to render a textual message.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'dragetti_filter_inactive';

  function readInactive() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return new Set();
      var arr = JSON.parse(raw);
      return new Set(Array.isArray(arr) ? arr : []);
    } catch (e) {
      return new Set();
    }
  }

  function writeInactive(set) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(set)));
    } catch (e) { /* swallow */ }
  }

  function applyFilter(inactive) {
    var list = document.getElementById('post-list');
    if (!list) return;
    var cards = list.querySelectorAll('.card-wrapper');
    var visibleCount = 0;

    cards.forEach(function (card) {
      var raw = (card.getAttribute('data-categories') || '').trim();
      var cats = raw ? raw.split(/\s+/) : [];

      // A card with no categories is always shown.
      if (cats.length === 0) {
        card.classList.remove('is-filtered-out');
        visibleCount++;
        return;
      }

      // Show iff at least one of its categories is currently active.
      var anyActive = cats.some(function (c) { return !inactive.has(c); });
      if (anyActive) {
        card.classList.remove('is-filtered-out');
        visibleCount++;
      } else {
        card.classList.add('is-filtered-out');
      }
    });

    list.classList.toggle('is-empty-state', visibleCount === 0);
  }

  function syncCapsulesUI(inactive) {
    var capsules = document.querySelectorAll('#category-filter .filter-capsule');
    capsules.forEach(function (cap) {
      var slug = cap.getAttribute('data-category');
      var active = !inactive.has(slug);
      cap.classList.toggle('is-active', active);
      cap.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
  }

  function bindCapsules(inactive) {
    var capsules = document.querySelectorAll('#category-filter .filter-capsule');
    capsules.forEach(function (cap) {
      cap.addEventListener('click', function () {
        var slug = cap.getAttribute('data-category');
        if (inactive.has(slug)) {
          inactive.delete(slug);
        } else {
          inactive.add(slug);
        }
        writeInactive(inactive);
        syncCapsulesUI(inactive);
        applyFilter(inactive);
      });
    });

    var reset = document.getElementById('filter-reset');
    if (reset) {
      reset.addEventListener('click', function () {
        inactive.clear();
        writeInactive(inactive);
        syncCapsulesUI(inactive);
        applyFilter(inactive);
      });
    }
  }

  function run() {
    if (!document.getElementById('category-filter')) return;
    var inactive = readInactive();
    syncCapsulesUI(inactive);
    applyFilter(inactive);
    bindCapsules(inactive);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
