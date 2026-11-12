import marshal

def inspect_code(co, depth=0):
    indent = "  " * depth
    print(f"{indent}Code: {co.co_name}, file: {co.co_filename}, consts: {len(co.co_consts)}, names: {len(co.co_names)}")
    strings = []
    for c in co.co_consts:
        if isinstance(c, str):
            if any(k in c.lower() for k in ['zip', 'pass', 'ariyan', 'glory', 'port', 'http', 'host', 'key', 'token']):
                strings.append(c)
        elif hasattr(c, 'co_code'):
            inspect_code(c, depth + 1)
    if strings:
        print(f"{indent}Interesting strings ({len(strings)}):")
        for s in strings[:20]:
            print(f"{indent}  {repr(s[:100])}")

print("=== MAIN OBJ ===")
m_co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
inspect_code(m_co)
print("Main names:", [n for n in m_co.co_names if any(k in n.lower() for k in ['zip', 'file', 'app', 'run', 'start', 'pass'])])

print("\n=== APP OBJ ===")
a_co = marshal.loads(open('scratch_app_obj.bin', 'rb').read())
inspect_code(a_co)
