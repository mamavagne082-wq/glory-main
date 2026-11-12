import marshal

def dummy(a, b=1):
    c = a + b
    return c

b = marshal.dumps(dummy.__code__)
print('3.12 dummy length:', len(b))
print('3.12 dummy head bytes:')
print([hex(x) for x in b[:35]])
