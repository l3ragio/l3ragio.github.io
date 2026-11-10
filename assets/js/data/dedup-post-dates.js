/**
 * When the post header carries both a Posted and an Updated time, hide
 * the Updated span if both timestamps fall on the same calendar day.
 * Chirpy emits both unconditionally; rendering "Posted May 7 | Updated
 * May 7" reads as redundancy.
 */
(function () {
  'use strict';

  function sameDay(ts1, ts2) {
    var a = new Date(ts1 * 1000);
    var b = new Date(ts2 * 1000);
    return a.getFullYear() === b.getFullYear()
        && a.getMonth()    === b.getMonth()
        && a.getDate()     === b.getDate();
  }

  function run() {
    document.querySelectorAll('header .post-meta').forEach(function (meta) {
      var times = meta.querySelectorAll('time[data-ts]');
      if (times.length < 2) return;
      var t1 = parseInt(times[0].getAttribute('data-ts'), 10);
      var t2 = parseInt(times[1].getAttribute('data-ts'), 10);
      if (!isFinite(t1) || !isFinite(t2)) return;
      if (sameDay(t1, t2)) {
        var updatedSpan = times[1].closest('span');
        if (updatedSpan) updatedSpan.style.display = 'none';
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
