import struct

with open('scratch_main_obj.bin', 'rb') as f:
    buf = f.read()

pos = 0

def read_obj(depth=0):
    global pos
    flag = buf[pos]
    pos += 1
    real_type = chr(flag & 0x7f)
    has_ref = bool(flag & 0x80)
    
    # print('  '*depth, f'pos={pos-1} type={real_type} ({hex(flag)})')
    
    if real_type == 'c':
        argcount = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        posonly = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        kwonly = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        stacksize = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        flags = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        code = read_obj(depth+1)
        consts = read_obj(depth+1)
        names = read_obj(depth+1)
        varnames = read_obj(depth+1) # in 3.11: localsplusnames
        # let's see what comes next
        return ('code', consts, names)
    elif real_type == 's': # string/bytes
        l = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        s = buf[pos:pos+l]; pos += l
        return s
    elif real_type == '(': # tuple
        n = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        items = [read_obj(depth+1) for _ in range(n)]
        return tuple(items)
    elif real_type == 'z': # short ascii
        l = buf[pos]; pos += 1
        s = buf[pos:pos+l].decode('utf-8', 'replace'); pos += l
        return s
    elif real_type == 'a': # ascii
        l = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        s = buf[pos:pos+l].decode('utf-8', 'replace'); pos += l
        return s
    elif real_type == 'u': # short ascii interned
        l = buf[pos]; pos += 1
        s = buf[pos:pos+l].decode('utf-8', 'replace'); pos += l
        return s
    elif real_type == 'A': # ascii interned
        l = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        s = buf[pos:pos+l].decode('utf-8', 'replace'); pos += l
        return s
    elif real_type == 'i': # int
        v = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        return v
    elif real_type == 'N': # None
        return None
    elif real_type == 'T': # True
        return True
    elif real_type == 'F': # False
        return False
    elif real_type == 'r': # ref
        idx = struct.unpack('<i', buf[pos:pos+4])[0]; pos += 4
        return f'<ref {idx}>'
    else:
        print(f"UNKNOWN TYPE: {hex(flag)} ({chr(flag & 0x7f)}) at pos {pos-1}")
        return None

res = read_obj()
print("Top consts count:", len(res[1]))
for i, c in enumerate(res[1]):
    if isinstance(c, str) and len(c) < 200:
        print(f"const {i}: {c}")
    elif isinstance(c, tuple):
        print(f"const {i}: tuple len {len(c)}")
    elif isinstance(c, tuple) and len(c) > 0 and c[0] == 'code':
        print(f"const {i}: sub-code object")
