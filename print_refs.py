import io, struct

with open('scratch_main_obj.bin', 'rb') as f:
    full_data = f.read()

p = io.BytesIO(full_data)
refs = []

def r_byte(): return p.read(1)[0]
def r_long(): return struct.unpack('<i', p.read(4))[0]

def r_object():
    flag = r_byte()
    code = flag & 0x7f
    flag_ref = bool(flag & 0x80)
    type_char = chr(code)
    
    ref_idx = None
    if flag_ref:
        ref_idx = len(refs)
        refs.append(None)
        
    res = None
    if type_char == 'c':
        r_long(); r_long(); r_long(); r_long(); r_long()
        co_code = r_object()
        co_consts = r_object()
        co_names = r_object()
        co_localsplusnames = r_object()
        co_localspluskinds = r_object()
        co_filename = r_object()
        co_name = r_object()
        co_qualname = r_object()
        r_long()
        co_linetable = r_object()
        co_exceptiontable = r_object()
        res = 'code'
    elif type_char == 's':
        n = r_long(); res = p.read(n)
    elif type_char == '(':
        n = r_long(); res = tuple(r_object() for _ in range(n))
    elif type_char == ')':
        n = r_byte(); res = tuple(r_object() for _ in range(n))
    elif type_char in ('N', 'T', 'F'): res = None
    elif type_char == 'i': res = r_long()
    elif type_char == 'l':
        n = r_long(); p.read(abs(n)*2); res = 0
    elif type_char == ':':
        res = slice(r_object(), r_object(), r_object())
    elif type_char in ('z', 'Z', 'u'):
        n = r_byte(); res = p.read(n).decode('utf-8', 'surrogateescape')
    elif type_char in ('a', 'A'):
        n = r_long(); res = p.read(n).decode('utf-8', 'surrogateescape')
    elif type_char == 'r':
        ref_id = r_long(); res = refs[ref_id]
        
    if flag_ref and ref_idx is not None:
        refs[ref_idx] = res
    return res

r_object()
print("Total refs:", len(refs))
print("ref 10:", repr(refs[10]))
print("ref 24:", repr(refs[24]))
print("ref 60:", repr(refs[60]))
print("ref 302:", repr(refs[302]))
