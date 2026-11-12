import marshal, io

with open('scratch_main_obj.bin', 'rb') as f:
    b = f.read()

# Let's see: in Python 3.12, can marshal.loads load slice?
s = slice(None, 256, None)
dumped_s = marshal.dumps(s)
print('Dumped slice:', [hex(x) for x in dumped_s])
loaded_s = marshal.loads(dumped_s)
print('Loaded slice:', loaded_s)
