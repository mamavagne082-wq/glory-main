def search_string(filename, target):
    data = open(filename, 'rb').read()
    if target.encode() in data:
        print(f"Found in raw bytes of {filename}!")

for f in ['scratch_main_obj.bin', 'scratch_app_obj.bin', r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\app.py']:
    search_string(f, 'accounts.json')
