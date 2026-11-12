import marshal, dis

co_app = marshal.loads(open('scratch_app_obj.bin', 'rb').read())

def get_strings_from_code(co, xor_key=210):
    decoded = set()
    instructions = list(dis.get_instructions(co))
    
    # Look for sequences:
    # LOAD_GLOBAL (IllllIlIl)
    # [LOAD_SMALL_INT or LOAD_CONST]*
    # CALL N
    i = 0
    while i < len(instructions):
        inst = instructions[i]
        if inst.opname == 'LOAD_GLOBAL' and inst.argval == 'IllllIlIl':
            args = []
            j = i + 1
            while j < len(instructions) and instructions[j].opname in ('LOAD_SMALL_INT', 'LOAD_CONST', 'EXTENDED_ARG'):
                if instructions[j].opname != 'EXTENDED_ARG':
                    val = instructions[j].argval
                    if isinstance(val, int):
                        args.append(val)
                j += 1
            if j < len(instructions) and instructions[j].opname == 'CALL':
                # Try to decode args with xor_key
                s = ''.join(chr(x ^ xor_key) for x in args)
                if all(32 <= ord(c) < 127 or c in '\r\n\t' for c in s) and len(s) > 0:
                    decoded.add(s)
        i += 1
        
    for c in co.co_consts:
        if hasattr(c, 'co_consts'):
            decoded.update(get_strings_from_code(c, xor_key))
            
    return decoded

all_dec = get_strings_from_code(co_app)
print(f"Total decoded strings in app: {len(all_dec)}")
with open('all_app_strings.txt', 'w', encoding='utf-8') as f:
    for s in sorted(all_dec):
        f.write(s + '\n')
print("Wrote all_app_strings.txt")
