import builtins
import os
import marshal

orig_open = builtins.open
def hooked_open(file, *args, **kwargs):
    s = str(file)
    if any(k in s for k in ['zip', '.py', 'account', 'temp', 'Ariyan', 'json']):
        print(f"[OPEN] {s} mode={args[:1]}")
    return orig_open(file, *args, **kwargs)
builtins.open = hooked_open

orig_mkdir = os.mkdir
def hooked_mkdir(path, *args, **kwargs):
    print(f"[MKDIR] {path}")
    return orig_mkdir(path, *args, **kwargs)
os.mkdir = hooked_mkdir

orig_makedirs = os.makedirs
def hooked_makedirs(path, *args, **kwargs):
    print(f"[MAKEDIRS] {path}")
    return orig_makedirs(path, *args, **kwargs)
os.makedirs = hooked_makedirs

import subprocess
orig_sp_run = subprocess.run
def hooked_sp_run(cmd, *args, **kwargs):
    print(f"[SUBPROCESS.RUN] {cmd}")
    return orig_sp_run(cmd, *args, **kwargs)
subprocess.run = hooked_sp_run

import sys
orig_input = builtins.input
def hooked_input(prompt=''):
    print(f"[INPUT PROMPT] {prompt}")
    return ""
builtins.input = hooked_input

co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
os.chdir(r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY')

# Let's create a dummy accounts.json so it doesn't fail!
if not os.path.exists('accounts.json'):
    with orig_open('accounts.json', 'w') as f:
        f.write('[]')

ns = {'__name__': '__main__', '__file__': r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\main.py'}
try:
    exec(co, ns)
except SystemExit as e:
    print("[SYSTEM EXIT]:", e)
except Exception as e:
    print("[EXCEPTION]:", e)
