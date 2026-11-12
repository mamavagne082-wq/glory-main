import marshal

co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())

# In Python 3.14, let's execute scratch_main_obj.bin until it defines the decryptor functions, or let's inspect the first few lines of the bytecode!
import dis
lines = []
for instr in dis.get_instructions(co):
    lines.append(f"{instr.opname:25} {instr.argrepr}")
    if len(lines) > 100: break

print('\n'.join(lines))
