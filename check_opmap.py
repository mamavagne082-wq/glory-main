import sys
import dis

print("Python version:", sys.version)
for name, op in dis.opmap.items():
    if op in (0x80, 0x90, 0x97, 0x52):
        print(f"op {hex(op)} ({op}): {name}")
