import marshal, io, struct

def dummy(a, b=1):
    c = a + b
    return c

b = marshal.dumps(dummy.__code__)
p = io.BytesIO(b)

def parse_312_code():
    flag = p.read(1)[0]
    print('top flag:', hex(flag))
    argcount = struct.unpack('<i', p.read(4))[0]
    posonly = struct.unpack('<i', p.read(4))[0]
    kwonly = struct.unpack('<i', p.read(4))[0]
    stacksize = struct.unpack('<i', p.read(4))[0]
    flags = struct.unpack('<i', p.read(4))[0]
    print(f'args={argcount}, posonly={posonly}, kwonly={kwonly}, stack={stacksize}, flags={flags}')
    
    # Let's read objects in order
    idx = 0
    while p.tell() < len(b):
        start = p.tell()
        ch = p.read(1)
        if not ch: break
        t = ch[0]
        p.seek(start)
        obj = marshal.load(p)
        print(f'field {idx} at {start}: {type(obj)} -> {repr(obj)[:50]}')
        idx += 1

parse_312_code()
