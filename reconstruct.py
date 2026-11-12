import io
import struct
import types

with open('scratch_main_obj.bin', 'rb') as f:
    full_data = f.read()

p = io.BytesIO(full_data)
refs = []

def r_byte():
    b = p.read(1)
    if not b: raise EOFError
    return b[0]

def r_long():
    return struct.unpack('<i', p.read(4))[0]

def r_object():
    start_pos = p.tell()
    flag = r_byte()
    code = flag & 0x7f
    flag_ref = bool(flag & 0x80)
    type_char = chr(code)
    
    ref_idx = None
    if flag_ref:
        ref_idx = len(refs)
        refs.append(None)
        
    result = None
    if type_char == 'c':
        argcount = r_long()
        posonly = r_long()
        kwonly = r_long()
        stacksize = r_long()
        flags = r_long()
        co_code = r_object()
        co_consts = r_object()
        co_names = r_object()
        co_localsplusnames = r_object()
        co_localspluskinds = r_object()
        co_filename = r_object()
        co_name = r_object()
        co_qualname = r_object()
        co_firstlineno = r_long()
        co_linetable = r_object()
        co_exceptiontable = r_object()
        
        varnames = []
        cellvars = []
        freevars = []
        for name, kind in zip(co_localsplusnames, co_localspluskinds):
            if kind & 0x20:
                varnames.append(name)
            elif kind & 0x40:
                cellvars.append(name)
            elif kind & 0x80:
                freevars.append(name)
            else:
                varnames.append(name)
                
        co = types.CodeType(
            argcount,
            posonly,
            kwonly,
            len(varnames),
            stacksize,
            flags,
            co_code,
            tuple(co_consts),
            tuple(co_names),
            tuple(varnames),
            co_filename,
            co_name,
            co_qualname,
            co_firstlineno,
            co_linetable,
            co_exceptiontable,
            tuple(freevars),
            tuple(cellvars)
        )
        result = co
    elif type_char == 's':
        n = r_long()
        result = p.read(n)
    elif type_char == '(':
        n = r_long()
        result = [r_object() for _ in range(n)]
    elif type_char == ')':
        n = r_byte()
        result = [r_object() for _ in range(n)]
    elif type_char == 'N':
        result = None
    elif type_char == 'T':
        result = True
    elif type_char == 'F':
        result = False
    elif type_char == 'i':
        result = r_long()
    elif type_char == 'l':
        n = r_long()
        digits = p.read(abs(n) * 2)
        val = 0
        for i in range(abs(n)):
            d = struct.unpack('<H', digits[i*2:i*2+2])[0]
            val += d * (1 << (15 * i))
        if n < 0: val = -val
        result = val
    elif type_char == ':':
        start = r_object()
        stop = r_object()
        step = r_object()
        result = slice(start, stop, step)
    elif type_char in ('z', 'Z', 'u'):
        n = r_byte()
        result = p.read(n).decode('utf-8', 'surrogateescape')
    elif type_char in ('a', 'A'):
        n = r_long()
        result = p.read(n).decode('utf-8', 'surrogateescape')
    elif type_char == 'r':
        ref_id = r_long()
        result = refs[ref_id]
    else:
        raise ValueError(f"Unknown type code {hex(flag)} ({type_char}) at pos {start_pos}")
        
    if flag_ref and ref_idx is not None:
        refs[ref_idx] = result
        
    return result

co = r_object()
print("Reconstructed top-level code object!")
print("Name:", co.co_name)
print("Filename:", co.co_filename)
print("Consts count:", len(co.co_consts))
print("Names count:", len(co.co_names))
print("Names:", co.co_names[:30])
