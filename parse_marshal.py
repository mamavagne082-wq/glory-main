# Let's inspect the marshal byte structure of scratch_main_obj.bin
with open('scratch_main_obj.bin', 'rb') as f:
    b = f.read()

print('Length:', len(b))
# Let's check type code at pos 0:
# 0x63 is ord('c') -> TYPE_CODE
# Let's see Python 3.11 marshal.c:
# TYPE_CODE:
# w_long(co->co_argcount, p);
# w_long(co->co_posonlyargcount, p);
# w_long(co->co_kwonlyargcount, p);
# w_long(co->co_stacksize, p);
# w_long(co->co_flags, p);
# w_object(co->co_code, p);
# w_object(co->co_consts, p);
# w_object(co->co_names, p);
# w_object(co->co_localsplusnames, p);
# w_object(co->co_localspluskinds, p);
# w_object(co->co_filename, p);
# w_object(co->co_name, p);
# w_object(co->co_qualname, p);
# w_long(co->co_firstlineno, p);
# w_object(co->co_linetable, p);
# w_object(co->co_exceptiontable, p);

# Let's check Python 3.10:
# w_long(co->co_argcount, p);
# w_long(co->co_posonlyargcount, p);
# w_long(co->co_kwonlyargcount, p);
# w_long(co->co_nlocals, p);
# w_long(co->co_stacksize, p);
# w_long(co->co_flags, p);
# w_object(co->co_code, p);
# w_object(co->co_consts, p);
# w_object(co->co_names, p);
# w_object(co->co_varnames, p);
# w_object(co->co_freevars, p);
# w_object(co->co_cellvars, p);
# w_object(co->co_filename, p);
# w_object(co->co_name, p);
# w_long(co->co_firstlineno, p);
# w_object(co->co_lnotab, p);

# Notice in 3.10: 6 longs! 6 * 4 = 24 bytes!
# Here we have:
# b[0] = 0x63 ('c')
# b[1:5]   = 00 00 00 00 (argcount = 0)
# b[5:9]   = 00 00 00 00 (posonly = 0)
# b[9:13]  = 00 00 00 00 (kwonly = 0)
# b[13:17] = 14 00 00 00 (stacksize = 20)
# b[17:21] = 00 00 00 00 (flags = 0)
# Total longs = 5 longs! 5 * 4 = 20 bytes!
# b[21] = 0xf3 = FLAG_REF (0x80) | TYPE_STRING (0x73 = 's')
# Length of co_code = int.from_bytes(b[22:26], 'little') = 0x6190 = 24976 bytes!
print("Code length:", int.from_bytes(b[22:26], 'little'))
co_code = b[26:26+24976]
pos = 26 + 24976
print("Next type code at pos", pos, ":", hex(b[pos]), chr(b[pos] & 0x7f))
