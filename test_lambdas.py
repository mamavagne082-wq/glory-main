import marshal

co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())

# Let's execute the setup part of co (until it creates the string decoders)
env = {'__name__': '__verify__', '__file__': 'main.py'}
# Let's inspect the code object constants
# Constant 3 is code object <lambda> line 2
# Constant 6 is code object <lambda> line 6
print("Const 3:", co.co_consts[3])
print("Const 6:", co.co_consts[6])

# Let's execute the two lambdas
l1 = [c for c in co.co_consts if getattr(c, 'co_name', None) == '<lambda>'][0]
l2 = [c for c in co.co_consts if getattr(c, 'co_name', None) == '<lambda>'][1]

# Let's see how l1 is defined
import dis
print("=== l1 disassembly ===")
dis.dis(l1)

print("=== l2 disassembly ===")
dis.dis(l2)
