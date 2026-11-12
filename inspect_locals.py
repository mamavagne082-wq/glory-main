from reconstruct_both import reconstruct_file
import struct, io

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
        co_firstlineno = r_long()
        co_linetable = r_object(depth+1)
        co_exceptiontable = r_object(depth+1)
        print(f"[{depth}] co_name={co_name}, qualname={co_qualname}")
        print(f"     localsplusnames={co_localsplusnames}")
        print(f"     localspluskinds={co_localspluskinds}")
        res = ('code', co_name)
    elif type_char == 's':
        n = r_long(); res = p.read(n)
    elif type_char == '(':
        n = r_long(); res = [r_object(depth+1) for _ in range(n)]
    elif type_char == ')':
        n = r_byte(); res = [r_object(depth+1) for _ in range(n)]
    elif type_char == 'N': res = None
    elif type_char == 'T': res = True
    elif type_char == 'F': res = False
    elif type_char == 'i': res = r_long()
    elif type_char == 'l':
        n = r_long(); p.read(abs(n)*2); res = 'long'
    elif type_char == ':':
        res = (r_object(depth+1), r_object(depth+1), r_object(depth+1))
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
