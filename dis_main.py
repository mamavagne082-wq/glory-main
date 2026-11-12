from reconstruct_both import reconstruct_file
import sys

co_main = reconstruct_file('scratch_main_obj.bin')

# Let's inspect what modules co_main imports or what functions it calls
# Let's run it with a tracer or inspect its bytecode
import dis

print("=== DISASSEMBLY (FIRST 80 INSTRUCTIONS) ===")
dis.dis(co_main, depth=1)
