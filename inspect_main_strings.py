from reconstruct_both import reconstruct_file

co_main = reconstruct_file('scratch_main_obj.bin')

def get_all_strings(co):
    res = set()
    for c in co.co_consts:
        if isinstance(c, str):
            res.add(c)
        elif hasattr(c, 'co_consts'):
            res.update(get_all_strings(c))
    return res

m_strings = get_all_strings(co_main)
print(f"Total unique strings in main: {len(m_strings)}")
for s in sorted(m_strings):
    if any(k in s.lower() for k in ['zip', 'http', 'pass', 'ariyan', 'glory', 'port', 'host', 'app', 'run', '.py', 'token', 'key']):
        if len(s) < 150:
            print("  MAIN STR:", repr(s))
