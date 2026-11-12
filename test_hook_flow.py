import os, marshal, builtins, io, traceback
import pyzipper

# Hook pyzipper to capture password and extracted files!
orig_setpassword = pyzipper.AESZipFile.setpassword
def hooked_setpassword(self, pwd):
    print(f"\n[PYZIPPER SETPASSWORD] pwd = {pwd!r}")
    return orig_setpassword(self, pwd)
pyzipper.AESZipFile.setpassword = hooked_setpassword

orig_extractall = pyzipper.AESZipFile.extractall
def hooked_extractall(self, path=None, members=None, pwd=None):
    print(f"\n[PYZIPPER EXTRACTALL] path = {path!r}, pwd = {pwd!r}")
    return orig_extractall(self, path=path, members=members, pwd=pwd)
pyzipper.AESZipFile.extractall = hooked_extractall

orig_read = pyzipper.AESZipFile.read
def hooked_read(self, name, pwd=None):
    print(f"\n[PYZIPPER READ] name = {name!r}, pwd = {pwd!r}")
    return orig_read(self, name, pwd=pwd)
pyzipper.AESZipFile.read = hooked_read

orig_open = builtins.open
def hooked_open(file, *args, **kwargs):
    if 'accounts.json' in str(file) and 'r' in str(args):
        print('[OPEN HOOKED accounts.json]')
        return io.StringIO('[{"token": "test_token", "uid": 12345}]')
    return orig_open(file, *args, **kwargs)

builtins.open = hooked_open

orig_exists = os.path.exists
def hooked_exists(p):
    if 'accounts.json' in str(p):
        print(f'[EXISTS HOOKED] {p} -> True')
        return True
    res = orig_exists(p)
    return res
os.path.exists = hooked_exists

builtins.input = lambda prompt='': ''

co = marshal.loads(orig_open('scratch_main_obj.bin', 'rb').read())
os.chdir(r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY')

try:
    exec(co, {'__name__': '__main__', '__file__': r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\main.py'})
except Exception as e:
    traceback.print_exc()

