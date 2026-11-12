import io

data = open('scratch_main_obj.bin', 'rb').read()
print('Length of data:', len(data))

# Let's inspect where Python 3.12 fails
import marshal
try:
    marshal.loads(data)
except Exception as e:
    import traceback
    traceback.print_exc()

# Let's see Python 3.11 vs 3.12 code object fields:
# In 3.11:
# argcount (4), posonlyargcount (4), kwonlyargcount (4), stacksize (4), flags (4), code, consts, names, localsplusnames, localspluskinds, filename, name, qualname, firstlineno, linetable, exceptiontable
# In 3.12:
# 3.12 changed code objects! In 3.12:
# co_argcount, co_posonlyargcount, co_kwonlyargcount, co_stacksize, co_flags, co_code, co_consts, co_names, co_localsplusnames, co_localspluskinds, co_filename, co_name, co_qualname, co_firstlineno, co_linetable, co_exceptiontable
# BUT wait! Python 3.11 has co_qualname after co_name. Python 3.10 does not have co_qualname or exceptiontable.
# Python 3.11 is the EXACT version that has this!
