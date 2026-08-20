import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
GALLERY_DIR = os.path.join(ROOT_DIR, "img gallery")

EXTS = {".webp", ".png", ".jpg", ".jpeg", ".gif"}


def get_numbered_max(folder):
    """Находит максимальный номер среди файлов вида 001.webp, 143.png"""
    max_num = 0
    for f in os.listdir(folder):
        name, ext = os.path.splitext(f)
        if ext.lower() in EXTS and name.isdigit():
            max_num = max(max_num, int(name))
    return max_num


def get_unnumbered(folder):
    """Находит файлы без числового имени (VRChat_2026-..., screenshot_..., и т.д.)"""
    files = []
    for f in os.listdir(folder):
        name, ext = os.path.splitext(f)
        if ext.lower() in EXTS and not name.isdigit():
            files.append(f)
    return files


def extract_sort_key(filename):
    """Извлекает ключ сортировки из имени файла.
    Для VRChat: VRChat_2026-08-13_01-35-10.868_... -> извлекает дату/время.
    Для остальных: сортирует по имени.
    """
    name = os.path.splitext(filename)[0]

    m = re.search(r"(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})", name)
    if m:
        return "".join(m.groups())

    return name


def rename_folder(folder_path, folder_label=None):
    """Переименовывает новые файлы в папке, начиная с последнего номера + 1."""
    if not os.path.isdir(folder_path):
        print(f"  Папка не найдена: {folder_path}")
        return 0

    last_num = get_numbered_max(folder_path)
    unnumbered = get_unnumbered(folder_path)

    if not unnumbered:
        label = folder_label or os.path.basename(folder_path)
        print(f'  {label}: новых файлов нет (последний номер: {last_num})')
        return 0

    unnumbered.sort(key=extract_sort_key)

    renamed = 0
    for f in unnumbered:
        last_num += 1
        ext = os.path.splitext(f)[1].lower()
        new_name = f"{last_num:03d}{ext}"
        src = os.path.join(folder_path, f)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        renamed += 1

    label = folder_label or os.path.basename(folder_path)
    print(f'  {label}: переименовано {renamed} файлов (номера {last_num - renamed + 1:03d}..{last_num:03d})')
    return renamed


FOLDERS = [
    ("VRC/chil", "VRChat Чилл"),
    ("VRC/Metranome fest 2026", "Metranom Fest"),
    ("VRC/Metranome Ivent vcr", "Metranom Ивенты"),
    ("VRC/Metranome school", "Metranom School"),
    ("Art", "Арты"),
    ("3d art-modeling", "3D Арты"),
]

if len(sys.argv) > 1:
    target = sys.argv[1]
    found = False
    for folder, label in FOLDERS:
        if target.lower() in folder.lower() or target.lower() in label.lower():
            rename_folder(os.path.join(GALLERY_DIR, folder), label)
            found = True
    if not found:
        print(f'Папка "{target}" не найдена. Доступные: {", ".join(l for _, l in FOLDERS)}')
else:
    print("Переименование файлов:\n")
    total = 0
    for folder, label in FOLDERS:
        total += rename_folder(os.path.join(GALLERY_DIR, folder), label)
    print(f"\nИтого переименовано: {total} файлов")

    if total > 0:
        print("\nГенерация HTML...")
        gen_path = os.path.join(SCRIPT_DIR, "generate-galleries.py")
        exec(open(gen_path, encoding="utf-8").read())
