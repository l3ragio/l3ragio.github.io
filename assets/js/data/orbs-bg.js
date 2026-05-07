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
        vx: rand(-0.12, 0.12),
        vy: rand(-0.10, 0.10),
        baseR: br,
        phase: Math.random() * Math.PI * 2,
        phaseSpeed: rand(0.005, 0.012),
        amp: rand(0.20, 0.40),
        parallax: rand(0.02, 0.10)
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

      o.x += o.vx;
      o.y += o.vy;

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

      // Bias visibility: orbs get up to 2x intensity on the right
      // side of the viewport so the right rail acts as the
      // atmospheric zone. Alpha at left ~ base, alpha at right ~ 2x.
      var rightBias = 1 + Math.max(0, (o.x / w - 0.5)) * 2;

      var g = ctx.createRadialGradient(o.x, py, 0, o.x, py, r);
      g.addColorStop(0,   'rgba(' + accent + ', ' + (0.13 * rightBias).toFixed(3) + ')');
      g.addColorStop(0.6, 'rgba(' + accent + ', ' + (0.04 * rightBias).toFixed(3) + ')');
      g.addColorStop(1,   'rgba(' + accent + ', 0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(o.x, py, r, 0, Math.PI * 2);
      ctx.fill();
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
