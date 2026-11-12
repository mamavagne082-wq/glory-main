with open('scratch_main_obj.bin', 'rb') as f:
    b = f.read()

# Let's inspect the last fields of the top-level code object!
# In trace_311.py:
# co_names was at pos 25002? No, co_consts was at 25002.
# Let's see what pos each field is at for the top-level code object!

import struct

pos = 26 + 24976 # after co_code
print('pos of co_consts:', pos, hex(b[pos]))
# co_consts starts at 25002
# Let's find where co_consts ends and co_names, localsplusnames start!
