import marshal

with open('scratch_main_obj.bin', 'rb') as f:
    data = f.read()

# Let's see: in Python 3.12, why does marshal.loads fail?
# Could it be marshal version?
# In Python 3.12, marshal.version is 4!
print("marshal.version:", marshal.version)
try:
    marshal.loads(data)
    print("Direct loads SUCCEEDED!")
except Exception as e:
    print("Direct loads failed:", type(e), e)
