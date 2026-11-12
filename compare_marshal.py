with open('scratch_main_obj.bin', 'rb') as f:
    data = f.read()

# Let's find out how far marshal.loads goes before failing
# Or let's inspect the code object header in Python 3.11:
import marshal

# In Python 3.11:
# Let's compile a simple dummy function in 3.11 and dump its marshal bytes!
def dummy(): pass
dummy_bytes = marshal.dumps(dummy.__code__)
print('Dummy code marshal bytes head:')
print(list(dummy_bytes[:30]))
print('Dummy code marshal bytes hex:')
print(dummy_bytes[:30].hex())

print('\nOur scratch_main_obj.bin head:')
print(list(data[:30]))
print('Our scratch_main_obj.bin hex:')
print(data[:30].hex())
