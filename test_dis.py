import sys
import traceback

try:
    from reconstruct_both import reconstruct_file
    import dis
    co_main = reconstruct_file('scratch_main_obj.bin')
    print('Disassembling...')
    instructions = list(dis.get_instructions(co_main))
    print('Total instructions:', len(instructions))
    for inst in instructions[:30]:
        print(f'{inst.opname:20} {repr(inst.argval)}')
except Exception as e:
    traceback.print_exc()
