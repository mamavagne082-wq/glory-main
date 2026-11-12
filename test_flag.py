import marshal

with open('scratch_main_obj.bin', 'rb') as f:
    b = f.read()

# Let's find out what part of `b` marshal.loads in Python 3.12 can load.
# Byte 0 is 0x63 ('c' without FLAG_REF).
# In Python 3.12, can marshal.loads load a code object?
# Let's see: what if the top flag was 0xe3 (c with FLAG_REF)?
b_with_flag = bytearray(b)
b_with_flag[0] = 0xe3 # set FLAG_REF
try:
    marshal.loads(b_with_flag)
    print("Loads with FLAG_REF succeeded!")
except Exception as e:
    print("Loads with FLAG_REF failed:", e)

# What if b is loaded directly?
try:
    marshal.loads(b)
    print("Loads b succeeded!")
except Exception as e:
    print("Loads b failed:", e)
