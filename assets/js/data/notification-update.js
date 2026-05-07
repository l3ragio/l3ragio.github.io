/**
 * PWA "new version" notification handling.
 *
 * Two responsibilities:
 *
 * 1. Make the Update button actually update - unregister all service
 *    workers, clear Cache Storage, then replace location with a
 *    cache-busting query. Default Chirpy mechanism left users on the
 *    cached page after clicking Update.
 *
 * 2. Suppress the toast for 30s after an Update click. Without this,
 *    Chirpy's SW reasserts "new version" detection on the very next
 *    page load and the toast pops back up immediately. The 30-second
 *    window covers reload + reinstall + first paint.
 */
(function () {
  'use strict';

  var FLAG_KEY = 'dragetti_update_done';
  var SUPPRESS_MS = 30000;

  function hideToast(el) {
    if (!el) return;
    el.style.display = 'none';
    el.classList.remove('show');
  }

  function maybeSuppressOnLoad() {
    var raw = sessionStorage.getItem(FLAG_KEY);
    if (!raw) return;
    var ts = parseInt(raw, 10);
    if (!isFinite(ts)) {
      sessionStorage.removeItem(FLAG_KEY);
      return;
    }
    var age = Date.now() - ts;
    if (age >= SUPPRESS_MS) {
      sessionStorage.removeItem(FLAG_KEY);
      return;
    }

    // Within the suppression window - hide the toast now and keep
    // hiding it if Chirpy tries to show it again via .show class.
    var notif = document.getElementById('notification');
    hideToast(notif);

    if (!notif || typeof MutationObserver !== 'function') return;
    var obs = new MutationObserver(function () {
      hideToast(notif);
    });
    obs.observe(notif, {
      attributes: true,
      attributeFilter: ['class', 'style']
    });

    var remaining = Math.max(0, SUPPRESS_MS - age);
    setTimeout(function () {
      obs.disconnect();
      sessionStorage.removeItem(FLAG_KEY);
    }, remaining);
  }

  function bindUpdate() {
    var btn = document.querySelector('#notification button[aria-label="Update"]');
    if (!btn) return;
    if (btn.dataset.dragettiBound === '1') return;
    btn.dataset.dragettiBound = '1';

    btn.addEventListener('click', function () {
      // Mark the suppression window before any async work so a
      // synchronous reload still finds the flag on the next load.
      sessionStorage.setItem(FLAG_KEY, Date.now().toString());

      var tasks = [];

      if ('serviceWorker' in navigator) {
        tasks.push(
          navigator.serviceWorker.getRegistrations().then(function (regs) {
            return Promise.all(regs.map(function (r) { return r.unregister(); }));
          }).catch(function () { /* swallow */ })
        );
      }

      if ('caches' in window) {
        tasks.push(
          caches.keys().then(function (names) {
            return Promise.all(names.map(function (n) { return caches.delete(n); }));
          }).catch(function () { /* swallow */ })
        );
      }

      Promise.all(tasks).then(function () {
        var u = new URL(window.location.href);
        u.searchParams.set('_v', Date.now().toString());
        window.location.replace(u.toString());
      }).catch(function () {
        window.location.reload();
      });
    });
  }

  function run() {
    maybeSuppressOnLoad();
    bindUpdate();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
