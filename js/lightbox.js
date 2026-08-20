(function () {
    const images = document.querySelectorAll('.gallery-grid img');
    if (!images.length) return;

    const overlay = document.createElement('div');
    overlay.className = 'lightbox';
    overlay.innerHTML = `
        <span class="lightbox-close">&times;</span>
        <span class="lightbox-nav lightbox-prev">&#8249;</span>
        <span class="lightbox-nav lightbox-next">&#8250;</span>
        <img class="lightbox-img" src="" alt="">
        <div class="lightbox-counter"></div>
    `;
    document.body.appendChild(overlay);

    const img = overlay.querySelector('.lightbox-img');
    const counter = overlay.querySelector('.lightbox-counter');
    let current = 0;

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
