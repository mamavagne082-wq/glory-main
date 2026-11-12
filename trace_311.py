import io
import struct

with open('scratch_main_obj.bin', 'rb') as f:
    full_data = f.read()

p = io.BytesIO(full_data)
refs = []

def r_byte():
    b = p.read(1)
    if not b: raise EOFError
    return b[0]

def r_long():
    b = p.read(4)
    if len(b) < 4: raise EOFError
    return struct.unpack('<i', b)[0]

def r_object(depth=0):
    start_pos = p.tell()
    flag = r_byte()
    code = flag & 0x7f
    flag_ref = bool(flag & 0x80)
    type_char = chr(code)
    
    idx = None
    if flag_ref:
        idx = len(refs)
        refs.append(None)
        
    if type_char == 'c':
        argcount = r_long()
        posonly = r_long()
        kwonly = r_long()
        stacksize = r_long()
        flags = r_long()
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
        return 'code'
    elif type_char == 's':
        n = r_long()
        return p.read(n)
    elif type_char == '(':
        n = r_long()
        return [r_object(depth+1) for _ in range(n)]
    elif type_char == ')':
        n = r_byte()
        return [r_object(depth+1) for _ in range(n)]
    elif type_char == 'N':
        return None
    elif type_char == 'T':
        return True
    elif type_char == 'F':
        return False
    elif type_char == 'i':
        return r_long()
    elif type_char == 'l': # TYPE_LONG
        n = r_long() # number of 16-bit digits
        p.read(abs(n) * 2)
        return 'long'
    elif type_char in ('z', 'Z', 'u'):
        n = r_byte()
        return p.read(n)
    elif type_char in ('a', 'A'):
        n = r_long()
        return p.read(n)
    elif type_char == 'r':
        ref_id = r_long()
        return f"ref({ref_id})"
    else:
        raise ValueError(f"Unknown type code {hex(flag)} ({type_char}) at pos {start_pos}")

try:
    r_object()
    print("FINISHED PARSING ALL BYTES! Current pos:", p.tell(), "Total len:", len(full_data))
except Exception as e:
    print("FAILED AT POS", p.tell(), ":", e)
