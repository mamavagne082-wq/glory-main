import marshal

def dummy():
    x = 1
    return x

b = marshal.dumps(dummy.__code__)
print('Dummy length:', len(b))
pos = 0
while pos < len(b):
    flag = b[pos]
    code = flag & 0x7f
    print(f"pos {pos}: {hex(flag)} ({chr(code) if 32 <= code < 127 else '?'}) ref={bool(flag & 0x80)}")
    pos += 1
    if pos > 60: break
