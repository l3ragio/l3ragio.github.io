/**
 * Gallery mode: full screen, caption beside the image, auto-advance.
 *
 * Sequences
 *   - posts:          every figure.plate, in order. The thumbnails of
 *                     .story-gallery open the same sequence.
 *   - visual stories: every .vs-panel a.vs-image (caption from data-head /
 *                     data-text).
 *
 * The click is taken in the capture phase, so the theme's own lightbox does
 * not open on top. Without JavaScript the links still open the image.
 */
(function () {
  'use strict';

  var TRIGGERS = 'figure.plate a, .story-gallery a, .vs-panel a.vs-image';
  var it = (document.documentElement.lang || '').toLowerCase().indexOf('it') === 0;
  var L = it
    ? { dialog: 'Galleria', close: 'Chiudi', prev: 'Precedente', next: 'Successiva', play: 'Avvia', pause: 'Pausa' }
    : { dialog: 'Gallery', close: 'Close', prev: 'Previous', next: 'Next', play: 'Play', pause: 'Pause' };

  var box, img, countEl, headEl, textEl, barEl, playBtn;
  var items = [], index = 0, playing = false, timer = null, opener = null, touchX = null, overflow = '';

  function pathOf(href) {
    return new URL(href, window.location.href).pathname;
  }

  function item(a, head, text) {
    var i = a.querySelector('img');
    return {
      src: a.href,
      path: pathOf(a.href),
      alt: i ? i.alt : '',
      head: head || '',
      text: text || ''
    };
  }

  function collect() {
    var plates = document.querySelectorAll('figure.plate');
    if (plates.length) {
      return Array.prototype.map.call(plates, function (figure) {
        var head = figure.querySelector('.plate-head');
        var caption = figure.querySelector('figcaption');
        var text = '';
        if (caption) {
          var copy = caption.cloneNode(true);
          var h = copy.querySelector('.plate-head');
          if (h) h.remove();
          text = copy.textContent.trim();
        }
        return item(figure.querySelector('a'), head && head.textContent.trim(), text);
      });
    }
    return Array.prototype.map.call(document.querySelectorAll('.vs-panel a.vs-image'), function (a) {
      return item(a, a.getAttribute('data-head'), a.getAttribute('data-text'));
    });
  }

  function el(tag, cls, parent) {
    var node = document.createElement(tag);
    node.className = cls;
    if (parent) parent.appendChild(node);
    return node;
  }

  function button(cls, label, text, parent, onClick) {
    var b = el('button', cls, parent);
    b.type = 'button';
    b.setAttribute('aria-label', label);
    b.title = label;
    b.textContent = text;
    b.addEventListener('click', onClick);
    return b;
  }

  function build() {
    box = el('div', 'glb');
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', L.dialog);

    var stage = el('div', 'glb-stage', box);
    img = el('img', 'glb-img', stage);
    button('glb-nav glb-prev', L.prev, '‹', stage, function () { go(index - 1); });
    button('glb-nav glb-next', L.next, '›', stage, function () { go(index + 1); });

    var side = el('div', 'glb-side', box);
    countEl = el('p', 'glb-count', side);
    headEl = el('p', 'glb-head', side);
    textEl = el('p', 'glb-text', side);
    textEl.setAttribute('aria-live', 'polite');
    var bar = el('div', 'glb-bar', side);
    barEl = el('span', 'glb-bar-fill', bar);
    playBtn = button('glb-play', L.pause, '', side, toggle);

    button('glb-close', L.close, '×', box, close);

    stage.addEventListener('click', function (e) { if (e.target === stage) close(); });
    box.addEventListener('touchstart', function (e) { touchX = e.changedTouches[0].clientX; }, { passive: true });
    box.addEventListener('touchend', function (e) {
      if (touchX === null) return;
      var dx = e.changedTouches[0].clientX - touchX;
      touchX = null;
      if (Math.abs(dx) > 50) go(index + (dx < 0 ? 1 : -1));
    }, { passive: true });
  }

  // Reading time: longer captions stay longer on screen.
  function duration(entry) {
    if (!entry.text) return 5000;
    var words = entry.text.split(/\s+/).length;
    return Math.min(14000, Math.max(6000, 4000 + words * 260));
  }

  function schedule() {
    window.clearTimeout(timer);
    barEl.style.transition = 'none';
    barEl.style.width = '0';
    if (!playing || document.hidden) return;
    var ms = duration(items[index]);
    void barEl.offsetWidth; // restart the progress bar
    barEl.style.transition = 'width ' + ms + 'ms linear';
    barEl.style.width = '100%';
    timer = window.setTimeout(function () {
      if (index < items.length - 1) go(index + 1);
      else setPlaying(false);
    }, ms);
  }

  function setPlaying(value) {
    playing = value;
    var label = playing ? L.pause : L.play;
    playBtn.setAttribute('aria-label', label);
    playBtn.textContent = (playing ? '❚❚  ' : '▶  ') + label;
    schedule();
  }

  function toggle() {
    // pressing play on the last image starts the sequence again
    if (!playing && index === items.length - 1) { index = 0; render(); }
    setPlaying(!playing);
  }

  function render() {
    var entry = items[index];
    img.src = entry.src;
    img.alt = entry.alt;
    countEl.textContent = (index + 1) + ' / ' + items.length;
    headEl.textContent = entry.head;
    textEl.textContent = entry.text;
    if (items[index + 1]) new Image().src = items[index + 1].src;
  }

  function go(to) {
    index = (to + items.length) % items.length;
    render();
    schedule();
  }

  function onKey(e) {
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowRight') go(index + 1);
    else if (e.key === 'ArrowLeft') go(index - 1);
    else if (e.key === ' ' && e.target.tagName !== 'BUTTON') toggle();
    else if (e.key === 'Tab') {
      var f = box.querySelectorAll('button');
      var at = Array.prototype.indexOf.call(f, document.activeElement);
      f[(at + (e.shiftKey ? f.length - 1 : 1)) % f.length].focus();
    } else return;
    e.preventDefault();
    e.stopPropagation();
  }

  function open(list, start, from) {
    if (!box) build();
    items = list;
    index = start;
    opener = from;
    overflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    document.body.appendChild(box);
    document.addEventListener('keydown', onKey, true);
    render();
    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    setPlaying(!calm);
    playBtn.focus();
  }

  function close() {
    window.clearTimeout(timer);
    playing = false;
    document.removeEventListener('keydown', onKey, true);
    document.body.style.overflow = overflow;
    box.remove();
    if (opener) opener.focus({ preventScroll: true });
  }

  document.addEventListener('visibilitychange', function () {
    if (box && box.isConnected) schedule();
  });

  document.addEventListener('click', function (e) {
    if (e.button !== 0 || e.ctrlKey || e.metaKey || e.shiftKey || !e.target.closest) return;
    var a = e.target.closest(TRIGGERS);
    if (!a) return;
    var list = collect();
    var path = pathOf(a.href);
    for (var i = 0; i < list.length; i++) {
      if (list[i].path === path) {
        e.preventDefault();
        e.stopImmediatePropagation();
        open(list, i, a);
        return;
      }
    }
  }, true);
})();
