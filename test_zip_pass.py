import zipfile

zip_path = r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.user_uploaded/media_1794484834854_0be8b3e1.zip'

candidates = [
    'ARIYAN', 'ariyan', 'Ariyan', 'ARIYAN_A9X_BD', 'ariyan_a9x_bd',
    'glory', 'GLORY', 'Glory', 'ARIYAN_GLORY', 'ariyan_glory',
    '1234', '12345', '123456', '12345678', 'admin', 'root',
    'ALAMIN', 'alamin', 'Alamin', 'mamavagne082-wq',
    'A9X', 'a9x', 'A9X_BD', 'a9x_bd', 'AriyanPrime', 'ariyanprime',
    'AriyanPrime_A9x', '@AriyanPrime_A9x'
]

# Also extract potential password strings from decoded_original_main.py and main.py:
with open('main.py', 'r', encoding='utf-8', errors='ignore') as f:
    words = f.read().split()
    for w in words:
        if len(w) > 4 and w.isascii() and len(w) < 30:
            candidates.append(w)

with open('decoded_original_main.py', 'r', encoding='utf-8', errors='ignore') as f:
    words = f.read().split()
    for w in words:
        if len(w) > 4 and w.isascii() and len(w) < 30:
            candidates.append(w)

candidates = list(dict.fromkeys(candidates))
print(f"Testing {len(candidates)} candidate passwords...")

with zipfile.ZipFile(zip_path, 'r') as z:
    first_file = z.namelist()[0]
    for pwd in candidates:
        try:
            data = z.read(first_file, pwd=pwd.encode('utf-8'))
            print(f"FOUND PASSWORD: {repr(pwd)}!")
            break
        except (RuntimeError, zipfile.BadZipFile):
            continue
    else:
        print("None of the candidates worked.")
