dir_data = (
    "_file1.doc\n"
    "file2.pdf\n"
    "file222_.docx\n"
    "cmd.exe\n"
    "sys.dll\n"
    "FiLe7_5.txt\n"
    "foto1.jpg\n"
    "song1.mp3\n"
    "!!!song2.mp3\n"
    "video.avi\n"
    "file9.txt\n"
    "file_3_document.docx\n"
    "my_document!!!.ppt\n"
    "main.c\n"
    "lab3.py\n"
    "lookup.xml\n"
    "pic1.png\n"
    "pic2.bmp\n"
)

# Очищення від порожніх рядків
files = list(filter(None, dir_data.split("\n")))

print("Початковий вміст каталогу:")
print("\n".join(files))
print("-" * 40)

# Загальна кількість файлів
print(f"У каталозі є {len(files)} файлів")

# Підрахунок файлів з розширеннями ppt та txt (A)
ppt_count = sum(map(lambda f: f.endswith(".ppt"), files))
txt_count = sum(map(lambda f: f.endswith(".txt"), files))
print(f"Файлів з розширенням ppt: {ppt_count}")
print(f"Файлів з розширенням txt: {txt_count}")
print("-" * 40)

# Перейменування bmp -> jpg (B)
files_b = list(map(lambda f: f[:-4] + ".jpg" if f.endswith(".bmp") else f, files))
print("Каталог після заміни розширення .bmp на .jpg:")
print("\n".join(files_b))
print("-" * 40)

# Приведення до верхнього регістру (C)
files_c = list(map(str.upper, files_b))
print("Каталог після приведення імен файлів до верхнього регістру:")
print("\n".join(files_c))
print("-" * 40)

# Видалення файлів з розширенням .jpg / .JPG (D)
files_d = list(filter(lambda f: not f.endswith(".JPG"), files_c))
print("Каталог після видалення файлів з розширенням JPG:")
print("\n".join(files_d))