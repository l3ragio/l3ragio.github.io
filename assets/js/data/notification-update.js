/**
 * PWA cleanup + permanent toast suppression.
 *
 * Original purpose was to make the Update button work. We have since
 * disabled PWA entirely (pwa.enabled: false in _config.yml), but this
 * script still runs because users who visited while PWA was on may
 * have an active service worker and a populated Cache Storage that
 * keep generating spurious "new version" toasts.
 *
 * On every page load this script:
 *
 *   1. Unregisters every service worker registered for the origin.
 *   2. Clears every entry in Cache Storage.
 *   3. Hides the #notification toast immediately.
 *   4. Installs a MutationObserver that re-hides the toast if any
 *      remaining script tries to add the .show class later in the
 *      page lifecycle.
 *
 * Result: the toast cannot persist after one page load, regardless
 * of which prior PWA state the browser was in. After the SW is
 * unregistered once, future visits will not see the toast at all.
 */
(function () {
  'use strict';

  function hideToast() {
    var notif = document.getElementById('notification');
    if (!notif) return;
    notif.style.display = 'none';
    notif.classList.remove('show');
  }

  function unregisterAllServiceWorkers() {
    if (!('serviceWorker' in navigator)) return Promise.resolve();
    return navigator.serviceWorker.getRegistrations()
      .then(function (regs) {
        return Promise.all(regs.map(function (r) {
          return r.unregister();
        }));
      })
      .catch(function () { /* swallow */ });
  }

  function clearAllCaches() {
    if (!('caches' in window)) return Promise.resolve();
    return caches.keys()
      .then(function (names) {
        return Promise.all(names.map(function (n) {
          return caches.delete(n);
        }));
      })
      .catch(function () { /* swallow */ });
  }

  function watchAndHide() {
    var notif = document.getElementById('notification');
    if (!notif || typeof MutationObserver !== 'function') return;
    var obs = new MutationObserver(hideToast);
    obs.observe(notif, {
      attributes: true,
      attributeFilter: ['class', 'style']
    });
  }

  function run() {
    hideToast();
    watchAndHide();
    unregisterAllServiceWorkers();
    clearAllCaches();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
