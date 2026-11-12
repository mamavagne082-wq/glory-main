import pyzipper, os

zip_path = r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\ARIYAN_GLORY.zip'
out_dir = r'c:\Users\Al Amin\Desktop\New folder (3)\Glory-main\Glory-main\unpacked_100_fix'
os.makedirs(out_dir, exist_ok=True)

with pyzipper.AESZipFile(zip_path, 'r') as z:
    z.extractall(out_dir, pwd=b'Nobita@#$321')

print('Extracted successfully! Files:')
for f in os.listdir(out_dir):
    print(f, os.path.getsize(os.path.join(out_dir, f)))
