with open('main.py', 'r', encoding='utf-8') as f:
    c = f.read()

idx1 = c.find('ENC = """')
idx2 = c.find('"""', idx1 + 9)
enc = c[idx1+9:idx2]

def _unwrap(t): return ''.join(t.split())
def _uncaesar(t, sh=7):
    out = []
    for ch in t:
        o = ord(ch)
        if 65 <= o <= 90: out.append(chr((o - 65 - sh) % 26 + 65))
        elif 97 <= o <= 122: out.append(chr((o - 97 - sh) % 26 + 97))
        else: out.append(ch)
    return ''.join(out)

import base64, zlib
s = _unwrap(enc)[::-1]
s = _uncaesar(s)
pad = len(s) % 4
if pad: s += '=' * (4 - pad)
d = zlib.decompress(base64.urlsafe_b64decode(s)).decode('utf-8')
print('Decoded size:', len(d))
print('Decoded preview (first 500 chars):')
print(d[:500])
with open('decoded_original_main.py', 'w', encoding='utf-8') as out:
    out.write(d)
