import os, marshal, builtins
from pathlib import Path

orig_exists = os.path.exists
def hooked_exists(p):
    res = orig_exists(p)
    print(f"[EXISTS] {p} -> {res}")
    return res
os.path.exists = hooked_exists

import pyzipper, zipfile
def hook_zip(cls):
    for method in ['read', 'extract', 'extractall']:
        orig = getattr(cls, method, None)
        if orig:
            def make_wrapper(m, name):
                def wrapper(self, *args, **kwargs):
                    pwd = kwargs.get('pwd') or (args[1] if len(args) > 1 and name == 'read' else None)
                    print(f"[{cls.__name__}.{name}] args={args[:2]} kwargs={kwargs} PWD={pwd}")
                    return m(self, *args, **kwargs)
                return wrapper
            setattr(cls, method, make_wrapper(orig, method))

hook_zip(pyzipper.AESZipFile)
hook_zip(zipfile.ZipFile)

builtins.input = lambda prompt='': ""

co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
os.chdir(r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY')

# Create a sample accounts.json
with open('accounts.json', 'w', encoding='utf-8') as f:
    f.write('[{"token": "test_token"}]')

try:
    exec(co, {'__name__': '__main__', '__file__': r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\main.py'})
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    if os.path.exists('accounts.json'):
        os.remove('accounts.json')
