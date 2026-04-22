(function () {
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target && e.target.tagName === 'A') {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Lightly obfuscated email — assembled at runtime
  document.querySelectorAll('.email-link').forEach(function (el) {
    var user = el.getAttribute('data-user');
    var domain = el.getAttribute('data-domain');
    if (!user || !domain) return;
    var address = user + '@' + domain;
    el.setAttribute('href', 'mailto:' + address);
    el.textContent = el.textContent.trim() || address;
  });

  // Active section highlighting in primary nav (IntersectionObserver).
  if ('IntersectionObserver' in window && nav) {
    var navLinks = Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]'));
    var sections = navLinks
      .map(function (a) {
        var id = a.getAttribute('href').slice(1);
        var el = id ? document.getElementById(id) : null;
        return el ? { id: id, el: el, link: a } : null;
      })
      .filter(Boolean);

    var byId = {};
    sections.forEach(function (s) { byId[s.id] = s; });

    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        visible[entry.target.id] = entry.isIntersecting ? entry.intersectionRatio : 0;
      });
      // Pick the section with the highest visibility ratio
      var best = null, bestRatio = 0;
      Object.keys(visible).forEach(function (id) {
        if (visible[id] > bestRatio) { bestRatio = visible[id]; best = id; }
      });
      navLinks.forEach(function (a) { a.classList.remove('is-active'); });
      if (best && byId[best]) byId[best].link.classList.add('is-active');
    }, {
      // Trigger when a section's middle band crosses the viewport
      rootMargin: '-40% 0px -50% 0px',
      threshold: [0, 0.25, 0.5, 0.75, 1]
    });
    sections.forEach(function (s) { io.observe(s.el); });
  }
})();

