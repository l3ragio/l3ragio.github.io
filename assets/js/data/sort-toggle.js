/**
 * Home sort toggle.
 *
 * Two capsules in #sort-toggle swap which list is visible:
 *   - "Recent"   → #post-list (reverse-chronological, paginated)
 *   - "Selected" → #post-list-curated (author-ranked, asc by rank)
 *
 * State persists in localStorage so the user's choice survives
 * navigation and reload. The toggle is only emitted on page 1; on
 * other paginator pages this script no-ops.
 *
 * Plays nicely with category-filter.js: both targets share the
 * .card-wrapper class, so filtering applies regardless of which
 * list is currently visible.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'dragetti_sort_mode';
  var DEFAULT_MODE = 'recent';
  var VALID_MODES = { recent: true, curated: true };

  function readMode() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return VALID_MODES[raw] ? raw : DEFAULT_MODE;
    } catch (e) {
      return DEFAULT_MODE;
    }
  }

  function writeMode(mode) {
    try {
      localStorage.setItem(STORAGE_KEY, mode);
    } catch (e) { /* swallow */ }
  }

  function applyMode(mode) {
    var listRecent = document.getElementById('post-list');
    var listCurated = document.getElementById('post-list-curated');
    if (!listRecent || !listCurated) return;

    if (mode === 'curated') {
      listRecent.hidden = true;
      listCurated.hidden = false;
    } else {
      listRecent.hidden = false;
      listCurated.hidden = true;
    }
  }

  function syncCapsulesUI(mode) {
    var capsules = document.querySelectorAll('#sort-toggle .sort-capsule');
    capsules.forEach(function (cap) {
      var capMode = cap.getAttribute('data-sort');
      var active = capMode === mode;
      cap.classList.toggle('is-active', active);
      cap.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
  }

  function bindCapsules() {
    var capsules = document.querySelectorAll('#sort-toggle .sort-capsule');
    capsules.forEach(function (cap) {
      cap.addEventListener('click', function () {
        var mode = cap.getAttribute('data-sort');
        if (!VALID_MODES[mode]) return;
        writeMode(mode);
        syncCapsulesUI(mode);
        applyMode(mode);
      });
    });
  }

  function run() {
    if (!document.getElementById('sort-toggle')) return;
    var mode = readMode();
    syncCapsulesUI(mode);
    applyMode(mode);
    bindCapsules();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
