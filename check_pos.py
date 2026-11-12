with open('scratch_main_obj.bin', 'rb') as f:
    b = f.read()

pos = 25002
for i in range(pos, min(pos+100, len(b))):
    flag = b[i]
    code = flag & 0x7f
    ch = chr(code) if 32 <= code < 127 else '?'
    print(f"pos {i}: {hex(flag)} ({ch}) ref={bool(flag & 0x80)}")
