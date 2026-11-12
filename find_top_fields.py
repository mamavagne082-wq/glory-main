import io, struct

with open('scratch_main_obj.bin', 'rb') as f:
    full_data = f.read()

p = io.BytesIO(full_data)
refs = []

def r_byte(): return p.read(1)[0]
def r_long(): return struct.unpack('<i', p.read(4))[0]

def r_object(depth=0):
    start = p.tell()
    flag = r_byte()
    code = flag & 0x7f
    flag_ref = bool(flag & 0x80)
    type_char = chr(code)
    
    ref_idx = len(refs) if flag_ref else None
    if flag_ref: refs.append(None)
    
    if depth == 1:
        print(f"Top-level field at pos {start}: flag={hex(flag)} ({type_char}), ref={flag_ref}")
        
    res = None
    if type_char == 'c':
        argcount = r_long(); posonly = r_long(); kwonly = r_long(); stacksize = r_long(); flags = r_long()
        co_code = r_object(depth+1)
        co_consts = r_object(depth+1)
        co_names = r_object(depth+1)
        co_localsplusnames = r_object(depth+1)
        co_localspluskinds = r_object(depth+1)
        co_filename = r_object(depth+1)
        co_name = r_object(depth+1)
        co_qualname = r_object(depth+1)
        firstlineno_pos = p.tell()
        co_firstlineno = r_long()
        if depth == 0:
            print(f"Top-level firstlineno at pos {firstlineno_pos}: {co_firstlineno}")
        co_linetable = r_object(depth+1)
        co_exceptiontable = r_object(depth+1)
    elif type_char == 's':
        n = r_long(); p.read(n)
    elif type_char == '(':
        n = r_long(); [r_object(depth+1) for _ in range(n)]
    elif type_char == ')':
        n = r_byte(); [r_object(depth+1) for _ in range(n)]
    elif type_char in ('N', 'T', 'F'): pass
    elif type_char == 'i': r_long()
    elif type_char == 'l':
        n = r_long(); p.read(abs(n)*2)
    elif type_char == ':':
        r_object(depth+1); r_object(depth+1); r_object(depth+1)
    elif type_char in ('z', 'Z', 'u'):
        n = r_byte(); p.read(n)
    elif type_char in ('a', 'A'):
        n = r_long(); p.read(n)
    elif type_char == 'r':
        r_long()

r_object(0)
