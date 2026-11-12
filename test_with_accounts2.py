import os, marshal, builtins
from pathlib import Path

orig_exists = os.path.exists
def hooked_exists(p):
    res = orig_exists(p)
    print(f"[EXISTS] {p} -> {res}")
    return res
os.path.exists = hooked_exists

builtins.input = lambda prompt='': ""

co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
target_dir = r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY'
os.chdir(target_dir)

# Create accounts.json in target_dir
with open(os.path.join(target_dir, 'accounts.json'), 'w', encoding='utf-8') as f:
    f.write('[{"token": "test_token"}]')

try:
    exec(co, {'__name__': '__main__', '__file__': os.path.join(target_dir, 'main.py')})
except Exception as e:
    import traceback
    traceback.print_exc()
