import os, marshal, builtins
from pathlib import Path

orig_exists = os.path.exists
def hooked_exists(p):
    res = orig_exists(p)
    print(f"[EXISTS] {p} -> {res}")
    return res
os.path.exists = hooked_exists

orig_isfile = os.path.isfile
def hooked_isfile(p):
    res = orig_isfile(p)
    print(f"[ISFILE] {p} -> {res}")
    return res
os.path.isfile = hooked_isfile

orig_p_exists = Path.exists
def hooked_p_exists(self):
    res = orig_p_exists(self)
    print(f"[PATH.EXISTS] {self} -> {res}")
    return res
Path.exists = hooked_p_exists

builtins.input = lambda prompt='': ""

co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
os.chdir(r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY')

exec(co, {'__name__': '__main__', '__file__': r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\main.py'})
