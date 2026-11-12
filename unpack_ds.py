with open('dashboard_server.py', 'rb') as f:
    c = f.read()

import zlib, base64

idx1 = c.find(b"b'")
idx2 = c.rfind(b"'")
payload = c[idx1+2:idx2]
unpacked = zlib.decompress(base64.b64decode(payload[::-1])).decode('utf-8', errors='replace')

print("Unpacked dashboard_server.py size:", len(unpacked))
print("Unpacked preview (first 500 chars):")
print(unpacked[:500])

with open('unpacked_dashboard_server.py', 'w', encoding='utf-8') as out:
    out.write(unpacked)
