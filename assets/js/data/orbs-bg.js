/**
 * Background orbs: floating, pulsing soft circles at watermark opacity.
 * Subtle scroll parallax. Theme-reactive via --orb-rgb CSS variable.
 * Respects prefers-reduced-motion. Pauses when tab is hidden.
 */
(function () {
  'use strict';

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var canvas = document.createElement('canvas');
  canvas.id = 'orbs-bg';
  canvas.setAttribute('aria-hidden', 'true');

  var ctx = null;
  var orbs = [];
  var ORB_COUNT = 14;
  var rafId = null;
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var scrollY = 0;
  var smoothScroll = 0;

  function rand(a, b) { return Math.random() * (b - a) + a; }

  function getAccent() {
    var v = getComputedStyle(document.documentElement)
              .getPropertyValue('--orb-rgb');
    return v && v.trim() ? v.trim() : '0, 255, 198';
  }

  function resize() {
    var w = window.innerWidth;
    var h = window.innerHeight;
    canvas.width  = Math.floor(w * dpr);
    canvas.height = Math.floor(h * dpr);
    canvas.style.width  = w + 'px';
    canvas.style.height = h + 'px';
    if (ctx) ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function init() {
    var w = window.innerWidth;
    var h = window.innerHeight;
    orbs = [];
    for (var i = 0; i < ORB_COUNT; i++) {
      var br = rand(20, 70);
      orbs.push({
        x: Math.random() * w,
        y: Math.random() * h,
        vx: rand(-0.18, 0.18),
        vy: rand(-0.14, 0.14),
        baseR: br,
        phase: Math.random() * Math.PI * 2,
        phaseSpeed: rand(0.004, 0.010),
        amp: rand(0.18, 0.36),
        parallax: rand(0.02, 0.10),
        // Organic floating perturbation: independent sin-wave offset
        // per orb so each drifts on its own rhythm.
        wobblePhaseX: Math.random() * Math.PI * 2,
        wobblePhaseY: Math.random() * Math.PI * 2,
        wobbleSpeedX: rand(0.003, 0.008),
        wobbleSpeedY: rand(0.0025, 0.007),
        wobbleAmpX: rand(0.15, 0.35),
        wobbleAmpY: rand(0.10, 0.28)
      });
    }
  }

  function draw() {
    var w = window.innerWidth;
    var h = window.innerHeight;
    ctx.clearRect(0, 0, w, h);

    smoothScroll += (scrollY - smoothScroll) * 0.08;

    var accent = getAccent();

    for (var i = 0; i < orbs.length; i++) {
      var o = orbs[i];

      // Organic float: linear drift + per-orb sin perturbation so the
      // motion feels alive instead of mechanically straight-line.
      o.wobblePhaseX += o.wobbleSpeedX;
      o.wobblePhaseY += o.wobbleSpeedY;
      o.x += o.vx + Math.sin(o.wobblePhaseX) * o.wobbleAmpX;
      o.y += o.vy + Math.cos(o.wobblePhaseY) * o.wobbleAmpY;

      var pad = o.baseR * 1.5;
      if (o.x < -pad)        o.x = w + pad;
      if (o.x > w + pad)     o.x = -pad;
      if (o.y < -pad)        o.y = h + pad;
      if (o.y > h + pad)     o.y = -pad;

      o.phase += o.phaseSpeed;
      var r = o.baseR * (1 + Math.sin(o.phase) * o.amp);

      var dy = -smoothScroll * o.parallax;
      var range = h + pad * 2;
      var py = ((o.y + dy) % range + range) % range - pad;

      // Right-bias: rings on the right side of the viewport are
      // brighter so the atmospheric rail zone breathes more.
      var rightBias = 1 + Math.max(0, (o.x / w - 0.5)) * 2;

      // Hollow rings — only the stroke is visible, no fill. Replaces
      // the soft radial-gradient blob look with a quieter outline
      // that reads as a discreet glyph rather than a paint stain.
      ctx.strokeStyle = 'rgba(' + accent + ', ' + (0.30 * rightBias).toFixed(3) + ')';
      ctx.lineWidth = 1.25;
      ctx.beginPath();
      ctx.arc(o.x, py, r, 0, Math.PI * 2);
      ctx.stroke();
    }

    rafId = requestAnimationFrame(draw);
  }

  function start() {
    ctx = canvas.getContext('2d');
    resize();
    init();
    draw();
  }

  function pause() {
    if (rafId) {
      cancelAnimationFrame(rafId);
      rafId = null;
    }
  }

  function inject() {
    if (document.body) {
      document.body.insertBefore(canvas, document.body.firstChild);
      start();
    } else {
      requestAnimationFrame(inject);
    }
  }

  window.addEventListener('scroll', function () {
    scrollY = window.scrollY || window.pageYOffset || 0;
  }, { passive: true });

  window.addEventListener('resize', function () {
    resize();
    init();
  });

  document.addEventListener('visibilitychange', function () {
    if (document.hidden) pause();
    else if (!rafId && ctx) draw();
  });

  inject();
})();
