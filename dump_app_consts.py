from reconstruct_both import reconstruct_file

co_app = reconstruct_file('scratch_app_obj.bin')

def dump_consts(c, path=""):
    for idx, item in enumerate(c.co_consts):
        if isinstance(item, (str, bytes)):
            s = item if isinstance(item, str) else repr(item)
            if len(s) > 0 and len(s) < 200:
                print(f"{path}[{idx}] ({type(item).__name__}): {repr(s)}")
        elif hasattr(item, 'co_consts'):
            dump_consts(item, f"{path}[{idx}].{item.co_name}")

print("=== CO_APP NAMES ===")
print(co_app.co_names)

print("\n=== CO_APP CONSTS (STRINGS/BYTES) ===")
dump_consts(co_app)
