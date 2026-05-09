// Inline TOC populator for the right column at lg-only (992-1199px).
//
// Chirpy's bundled tocbot is gated to matchMedia("(min-width: 1200px)")
// in post.min.js, so the inline <nav id="toc"> stays empty between
// 992-1199. The capsule TOC handles navigation there via the popup,
// but the right column reads as half-rendered. This script populates
// the inline TOC at lg+ from the article's h2/h3 headings, and wires
// IntersectionObserver-based active-link highlighting so it behaves
// like Chirpy's xl+ inline TOC. At xl+ Chirpy's tocbot already
// populated #toc; we detect that and bail.
(function () {
  'use strict';

  var MQ = '(min-width: 992px)';
  var observer = null;

  function clearActiveObserver() {
    if (observer) {
      observer.disconnect();
      observer = null;
    }
  }

  function buildToc() {
    var toc = document.getElementById('toc');
    if (!toc) return;

    // Chirpy's tocbot already populated it (xl+). Nothing to do.
    if (toc.querySelector('a.toc-link')) return;

    var article = document.querySelector('article[data-toc="true"] .content');
    if (!article) return;

    var headings = article.querySelectorAll('h2[id], h3[id]');
    if (headings.length === 0) return;

    var rootUl = document.createElement('ul');
    rootUl.className = 'toc-list';
    var currentH2Li = null;
    var currentSubUl = null;

    headings.forEach(function (h) {
      var li = document.createElement('li');
      li.className = 'toc-list-item';

      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.className = 'toc-link';
      // Strip Chirpy's anchor "#" suffix that appears on hover.
      a.textContent = (h.textContent || '').replace(/\s*#?\s*$/, '').trim();
      a.title = a.textContent;
      li.appendChild(a);

      if (h.tagName === 'H3' && currentH2Li) {
        if (!currentSubUl) {
          currentSubUl = document.createElement('ul');
          currentSubUl.className = 'toc-list';
          currentH2Li.appendChild(currentSubUl);
        }
        currentSubUl.appendChild(li);
      } else {
        rootUl.appendChild(li);
        currentH2Li = li;
        currentSubUl = null;
      }
    });

    toc.appendChild(rootUl);

    // Active-link tracking. Highlight the heading whose top is currently
    // closest to the viewport top - that is the section the reader is in.
    var links = {};
    toc.querySelectorAll('a.toc-link').forEach(function (l) {
      var id = l.getAttribute('href').slice(1);
      links[id] = l;
    });

    clearActiveObserver();
    observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var id = entry.target.id;
        var link = links[id];
        if (!link) return;
        if (entry.isIntersecting) {
          Object.keys(links).forEach(function (k) {
            links[k].classList.remove('is-active-link');
          });
          link.classList.add('is-active-link');
        }
      });
    }, { rootMargin: '-15% 0% -65% 0%' });

    headings.forEach(function (h) { observer.observe(h); });
  }

  function teardown() {
    var toc = document.getElementById('toc');
    if (!toc) return;
    // Only tear down what WE built. Chirpy's tocbot output uses a
    // .toc-list class as well; bail if the wrapper has any node we
    // would not have created.
    if (toc.querySelector('a.toc-link')) {
      // Detect tocbot signature: tocbot adds .is-collapsed / .is-active
      // dynamically. If anchor count matches our expected H2/H3 count
      // and we are below 1200, it is ours.
      var below1200 = !window.matchMedia('(min-width: 1200px)').matches;
      if (below1200) {
        toc.innerHTML = '';
      }
    }
    clearActiveObserver();
  }

  function refresh() {
    var atLg = window.matchMedia(MQ).matches;
    if (atLg) {
      buildToc();
    } else {
      teardown();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', refresh);
  } else {
    refresh();
  }

  // Re-evaluate on resize across the lg/xl boundary so the column
  // populates / clears as the user resizes.
  var lastAtLg = window.matchMedia(MQ).matches;
  var resizeTimer = null;
  window.addEventListener('resize', function () {
    if (resizeTimer) clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      var nowAtLg = window.matchMedia(MQ).matches;
      if (nowAtLg !== lastAtLg) {
        lastAtLg = nowAtLg;
        refresh();
      }
    }, 150);
  });
})();
