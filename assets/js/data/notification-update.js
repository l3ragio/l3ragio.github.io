/**
 * Make the PWA "Update" button actually update the site.
 *
 * Default Chirpy mechanism leaves the user on the cached page after
 * clicking Update. Override: unregister all service workers, clear
 * the Cache Storage, then hard-reload bypassing the HTTP cache.
 */
(function () {
  'use strict';

  function bind() {
    var btn = document.querySelector('#notification button[aria-label="Update"]');
    if (!btn) return;
    if (btn.dataset.dragettiBound === '1') return;
    btn.dataset.dragettiBound = '1';

    btn.addEventListener('click', function () {
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
        // Bypass HTTP cache on the reload itself.
        var u = new URL(window.location.href);
        u.searchParams.set('_v', Date.now().toString());
        window.location.replace(u.toString());
      }).catch(function () {
        window.location.reload();
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bind);
  } else {
    bind();
  }
})();
