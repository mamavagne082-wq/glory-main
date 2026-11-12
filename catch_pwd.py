import pyzipper
import zipfile

# Hook pyzipper and zipfile to catch the password!
orig_read = pyzipper.AESZipFile.read
def hooked_read(self, name, pwd=None):
    if pwd:
        print(f"!!! CAUGHT PWD IN AESZipFile.read: {pwd} !!!")
    return orig_read(self, name, pwd)
pyzipper.AESZipFile.read = hooked_read

orig_extract = pyzipper.AESZipFile.extractall
def hooked_extract(self, path=None, members=None, pwd=None):
    if pwd:
        print(f"!!! CAUGHT PWD IN AESZipFile.extractall: {pwd} !!!")
    return orig_extract(self, path, members, pwd)
pyzipper.AESZipFile.extractall = hooked_extract

orig_z_read = zipfile.ZipFile.read
def hooked_z_read(self, name, pwd=None):
    if pwd:
        print(f"!!! CAUGHT PWD IN ZipFile.read: {pwd} !!!")
    return orig_z_read(self, name, pwd)
zipfile.ZipFile.read = hooked_z_read

orig_z_extract = zipfile.ZipFile.extractall
def hooked_z_extract(self, path=None, members=None, pwd=None):
    if pwd:
        print(f"!!! CAUGHT PWD IN ZipFile.extractall: {pwd} !!!")
    return orig_z_extract(self, path, members, pwd)
zipfile.ZipFile.extractall = hooked_z_extract

# Now run the code of scratch_main_obj.bin
import marshal
co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
import os
os.chdir(r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY')

# Run in custom namespace
ns = {'__name__': '__main__', '__file__': r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\main.py'}
try:
    exec(co, ns)
except Exception as e:
    print("Execution finished or exited:", e)
