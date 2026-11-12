import io, struct

with open('scratch_main_obj.bin', 'rb') as f:
    full_data = f.read()

p = io.BytesIO(full_data)
refs = []

def r_byte(): return p.read(1)[0]
def r_long(): return struct.unpack('<i', p.read(4))[0]

def r_object(path=''):
    start = p.tell()
    flag = r_byte()
    code = flag & 0x7f
    flag_ref = bool(flag & 0x80)
    type_char = chr(code)
    
    if start <= 41739 <= p.tell():
        print(f"FOUND 41739 at path: {path}, start: {start}")
        
    ref_idx = len(refs) if flag_ref else None
    if flag_ref: refs.append(None)
    
    res = None
    if type_char == 'c':
        r_long(); r_long(); r_long(); r_long(); r_long()
        co_code = r_object(path + '/code')
        co_consts = r_object(path + '/consts')
        co_names = r_object(path + '/names')
        co_localsplusnames = r_object(path + '/localsplusnames')
        co_localspluskinds = r_object(path + '/localspluskinds')
        co_filename = r_object(path + '/filename')
        co_name = r_object(path + '/name')
        co_qualname = r_object(path + '/qualname')
        r_long()
        co_linetable = r_object(path + '/linetable')
        co_exceptiontable = r_object(path + '/exceptiontable')
        res = 'code'
    elif type_char == 's':
        n = r_long(); res = p.read(n)
    elif type_char == '(':
        n = r_long()
        for i in range(n):
            if p.tell() <= 41739:
                # print before
                pass
            r_object(f"{path}/tuple[{i}]")
    elif type_char == ')':
        n = r_byte()
        for i in range(n):
            r_object(f"{path}/smalltuple[{i}]")
    elif type_char in ('N', 'T', 'F'): pass
    elif type_char == 'i': r_long()
    elif type_char == 'l':
        n = r_long(); p.read(abs(n)*2)
    elif type_char == ':':
        print(f"COLON at pos {start}, path={path}")
        r_object(path + '/slice_start')
        r_object(path + '/slice_stop')
        r_object(path + '/slice_step')
    elif type_char in ('z', 'Z', 'u'):
        n = r_byte(); p.read(n)
    elif type_char in ('a', 'A'):
        n = r_long(); p.read(n)
    elif type_char == 'r':
        r_long()

r_object('root')
