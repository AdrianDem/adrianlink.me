import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
GALLERY_DIR = os.path.join(ROOT_DIR, "img gallery")

pages = [
    {
        "folder": "VRC/chil",
        "slug": "vrc",
        "title": "VRChat Чилл",
        "bg": "../img/bgfon1.webp",
        "css": "../css/gallery.css",
        "cover": "https://adrian-demoner.ru/img/gallery_covers/chilvrc_cover.webp",
        "ogUrl": "https://adrian-demoner.ru/vrc",
        "canonical": "https://adrian-demoner.ru/vrc",
        "altPrefix": "VRChat фото",
        "extraFolders": [],
    },
    {
        "folder": "VRC/Metranome fest 2026",
        "slug": "metrafest2025",
        "title": "Metranom Fest 2025",
        "bg": "../img/bg1.webp",
        "css": "../css/gallery.css",
        "cover": "https://adrian-demoner.ru/img/gallery_covers/metrafest_cover.webp",
        "ogUrl": "https://adrian-demoner.ru/metrafest2025",
        "canonical": "https://adrian-demoner.ru/metrafest2025",
        "altPrefix": "Metranom Fest фото",
        "extraFolders": [],
    },
    {
        "folder": "VRC/Metranome Ivent vcr",
        "slug": "metranomivent",
        "title": "Ивенты Metranom Bar",
        "bg": "../img/bg1.webp",
        "css": "../css/gallery.css",
        "cover": "https://adrian-demoner.ru/img/gallery_covers/metranomivent_cover.webp",
        "ogUrl": "https://adrian-demoner.ru/metranomivent",
        "canonical": "https://adrian-demoner.ru/metranomivent",
        "altPrefix": "Metranom ивент фото",
        "extraFolders": [],
    },
    {
        "folder": "Art",
        "slug": "atr",
        "title": "Арты",
        "bg": "../img/bg1.webp",
        "css": "../css/art.css",
        "cover": "https://adrian-demoner.ru/img/gallery_covers/arts_cover.webp",
        "ogUrl": "https://adrian-demoner.ru/atr",
        "canonical": "https://adrian-demoner.ru/atr",
        "altPrefix": "Арт",
        "extraFolders": ["3d art-modeling"],
    },
]


def get_images(folder_path):
    if not os.path.isdir(folder_path):
        return []
    exts = {".webp", ".png", ".jpg", ".jpeg", ".gif"}
    files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in exts]
    files.sort(key=lambda x: int(re.sub(r"\D", "", x) or "0"))
    return files


def generate_gallery_images(page):
    lines = []
    counter = 1

    main_folder = os.path.join(GALLERY_DIR, page["folder"])
    for file in get_images(main_folder):
        src = f'../img gallery/{page["folder"]}/{file}'
        lines.append(f'                <img src="{src}" alt="{page["altPrefix"]} {counter}" loading="lazy">')
        counter += 1

    for ef in page.get("extraFolders", []):
        extra_folder = os.path.join(GALLERY_DIR, ef)
        for file in get_images(extra_folder):
            src = f'../img gallery/{ef}/{file}'
            lines.append(f'                <img src="{src}" alt="{page["altPrefix"]}" loading="lazy">')
            counter += 1

    return "\n".join(lines)


def generate_html(page):
    images_html = generate_gallery_images(page)
    return f'''<!DOCTYPE html>
<html lang="ru-RU">
<head>
    <meta charset="UTF-8">
    <title>{page["title"]} - Adrian Demoner</title>

    <link rel="icon" href="../img/favicon.png">

    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <script type="application/ld+json">
        {{
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": "Adrian_Demoner",
            "url": "https://adrian-demoner.ru",
            "logo": "https://adrian-demoner.ru/img/logo.png",
            "sameAs": [
                "https://t.me/LogovoChertils",
                "https://github.com/AdrianDem",
                "https://twitch.tv/adrian_demoner",
                "https://youtube.com/@adrian_demoner",
                "https://instagram.com/adrian_demoner"
            ]
        }}
    </script>

    <meta name="description" content="{page["title"]} - Adrian Demoner">
    <meta name="theme-color" content="#b23434">

    <meta property="og:locale" content="ru_RU">
    <meta property="og:title" content="{page["title"]} - Adrian Demoner">
    <meta property="og:description" content="{page["title"]} - Adrian Demoner">
    <meta property="og:site_name" content="Adrian Demoner">
    <meta property="og:url" content="{page["ogUrl"]}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="{page["cover"]}">
    <meta property="og:image:width" content="600">
    <meta property="og:image:height" content="600">

    <meta name="twitter:site" content="Adrian Demoner">
    <meta name="twitter:title" content="{page["title"]} - Adrian Demoner">
    <meta name="twitter:description" content="{page["title"]} - Adrian Demoner">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="{page["cover"]}">

    <link rel="canonical" href="{page["canonical"]}">
    <link rel="alternate" hreflang="ru" href="{page["canonical"]}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">

    <link rel="stylesheet" type="text/css" href="{page["css"]}">
    <script defer src="../js/lightbox.js"></script>
</head>
<body>
<header></header>

<img class="full-page-background" src="{page["bg"]}" alt="">
<div class="full-page">
    <div class="page-container">
        <div class="page-central-container">
            <div class="page-title">{page["title"]}</div>

            <div class="gallery-grid">
{images_html}
            </div>

            <div class="page-space-between-container" style="margin-top: 40px;">
                <div class="page-buttons">
                    <a href="/gallery">Галерея</a>
                </div>
                <div class="page-buttons">
                    <a href="/">Главная</a>
                </div>
            </div>
        </div>
    </div>
</div>

<footer>
    <div class="footer-container">
        <div class="copirate">2026 © adrian-demoner.ru</div>
        <div class="made-by">Made by <a href="https://xrustaller.ru">Xrustaller</a></div>
    </div>
</footer>
</body>
</html>'''


for page in pages:
    slug = page["slug"]
    folder_dir = os.path.join(ROOT_DIR, slug)
    os.makedirs(folder_dir, exist_ok=True)

    html = generate_html(page)
    out_path = os.path.join(folder_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    img_count = html.count("<img ")
    print(f'  /{slug} -> {img_count} изображений')

print("\nВсе страницы сгенерированы!")
