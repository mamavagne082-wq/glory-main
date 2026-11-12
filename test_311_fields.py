import io, struct

with open('scratch_main_obj.bin', 'rb') as f:
    full_data = bytearray(f.read())
full_data[0] = 0xe3

# In Python 3.11, marshal.loads(full_data) raised:
# SystemError: Objects\codeobject.c:250: bad argument to internal function
# Let's see what line 250 in 3.11 codeobject.c checks:
# Let's inspect all sub-objects in scratch_main_obj.bin by dumping them one by one!
import marshal

p = io.BytesIO(full_data)
# Let's skip the top-level code header and test each constant!
flag = p.read(1)[0]
p.read(20) # 5 ints
code_bytes = marshal.load(p) # loads co_code
print('co_code loaded ok, len:', len(code_bytes))

consts = marshal.load(p)
print('consts loaded ok, count:', len(consts))

names = marshal.load(p)
print('names loaded ok, count:', len(names))

localsplusnames = marshal.load(p)
print('localsplusnames loaded ok:', localsplusnames)

localspluskinds = marshal.load(p)
print('localspluskinds loaded ok:', localspluskinds)

filename = marshal.load(p)
print('filename loaded ok:', filename)

name = marshal.load(p)
print('name loaded ok:', name)

qualname = marshal.load(p)
print('qualname loaded ok:', qualname)

firstlineno = struct.unpack('<i', p.read(4))[0]
print('firstlineno:', firstlineno)

linetable = marshal.load(p)
print('linetable loaded ok, len:', len(linetable))

exceptiontable = marshal.load(p)
print('exceptiontable loaded ok, len:', len(exceptiontable))
