(() => {
    const STORAGE_KEY = 'lang';
    const btn = document.getElementById('lang-toggle');
    if (!btn) return;
    const els = document.querySelectorAll('[data-en]');
    const imgAlts = document.querySelectorAll('[data-en-alt]');

    function getLang() {
        try {
            return localStorage.getItem(STORAGE_KEY) || 'ru';
        } catch (e) {
            return 'ru';
        }
    }

    function applyLang(lang) {
        els.forEach(function (el) {
            if (lang === 'en') {
                if (!el.dataset.ru) el.dataset.ru = el.textContent;
                el.textContent = el.dataset.en;
            } else {
                if (el.dataset.ru) el.textContent = el.dataset.ru;
            }
        });
        imgAlts.forEach(function (img) {
            if (lang === 'en') {
                if (!img.dataset.ruAlt) img.dataset.ruAlt = img.alt;
                img.alt = img.dataset.enAlt;
            } else {
                if (img.dataset.ruAlt) img.alt = img.dataset.ruAlt;
            }
        });
        btn.textContent = lang === 'ru' ? 'EN' : 'RU';
        document.documentElement.lang = lang === 'ru' ? 'ru-RU' : 'en';
    }

    applyLang(getLang());

    btn.addEventListener('click', function () {
        var next = getLang() === 'ru' ? 'en' : 'ru';
        try {
            localStorage.setItem(STORAGE_KEY, next);
        } catch (e) {}
        applyLang(next);
    });
})();
