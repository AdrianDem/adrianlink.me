(function () {
    var images = document.querySelectorAll('.gallery-grid img');
    if (!images.length) return;

    var overlay = document.createElement('div');
    overlay.className = 'lightbox';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-label', 'Image lightbox');
    overlay.innerHTML =
        '<button class="lightbox-close" aria-label="Close">&times;</button>' +
        '<button class="lightbox-nav lightbox-prev" aria-label="Previous image">&#8249;</button>' +
        '<button class="lightbox-nav lightbox-next" aria-label="Next image">&#8250;</button>' +
        '<img class="lightbox-img" src="" alt="">' +
        '<div class="lightbox-counter"></div>';
    document.body.appendChild(overlay);

    var img = overlay.querySelector('.lightbox-img');
    var counter = overlay.querySelector('.lightbox-counter');
    var current = 0;

    function show(i) {
        current = i;
        img.src = images[i].src;
        img.alt = images[i].alt;
        counter.textContent = (i + 1) + ' / ' + images.length;
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function hide() {
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    images.forEach(function (el, i) {
        el.addEventListener('click', function () { show(i); });
    });

    overlay.querySelector('.lightbox-close').addEventListener('click', hide);
    overlay.addEventListener('click', function (e) {
        if (e.target === overlay) hide();
    });

    overlay.querySelector('.lightbox-prev').addEventListener('click', function (e) {
        e.stopPropagation();
        show((current - 1 + images.length) % images.length);
    });

    overlay.querySelector('.lightbox-next').addEventListener('click', function (e) {
        e.stopPropagation();
        show((current + 1) % images.length);
    });

    document.addEventListener('keydown', function (e) {
        if (!overlay.classList.contains('active')) return;
        if (e.key === 'Escape') hide();
        if (e.key === 'ArrowLeft') show((current - 1 + images.length) % images.length);
        if (e.key === 'ArrowRight') show((current + 1) % images.length);
    });
})();
