import io
import struct

with open('scratch_main_obj.bin', 'rb') as f:
    full_data = f.read()

p = io.BytesIO(full_data)
seen = set()

def r_byte():
    b = p.read(1)
    if not b: raise EOFError
    return b[0]

def r_long():
    return struct.unpack('<i', p.read(4))[0]

def r_object():
    flag = r_byte()
    code = flag & 0x7f
    flag_ref = bool(flag & 0x80)
    type_char = chr(code)
    seen.add((hex(flag), type_char, flag_ref))
    
    if type_char == 'c':
        r_long(); r_long(); r_long(); r_long(); r_long()
        for _ in range(10): r_object()
        r_long() # firstlineno
        r_object()
    elif type_char == 's':
        n = r_long()
        p.read(n)
    elif type_char == '(':
        n = r_long()
        for _ in range(n): r_object()
    elif type_char == ')':
        n = r_byte()
        for _ in range(n): r_object()
    elif type_char in ('N', 'T', 'F'):
        pass
    elif type_char == 'i':
        r_long()
    elif type_char == 'l':
        n = r_long()
        p.read(abs(n) * 2)
    elif type_char == ':':
        r_object(); r_object(); r_object()
    elif type_char in ('z', 'Z', 'u'):
        n = r_byte()
        p.read(n)
    elif type_char in ('a', 'A'):
        n = r_long()
        p.read(n)
    elif type_char == 'r':
        r_long()

r_object()
print('All (flag, type, has_ref):')
for item in sorted(seen):
    print(item)
