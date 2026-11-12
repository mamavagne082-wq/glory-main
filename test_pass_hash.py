import pyzipper

zip_path = r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.user_uploaded/media_1794484834854_0be8b3e1.zip'

cands = [
    '26ef5dbef741f304ee55fd751e78a06b74f56852',
    '133c877dc3ffd9a23008290a53f0a24c',
]

with pyzipper.AESZipFile(zip_path, 'r') as z:
    for pwd in cands:
        try:
            d = z.read('StartMatch_pb2.py', pwd=pwd.encode('utf-8'))
            print(f"SUCCESS with {pwd}")
            break
        except Exception:
            pass
    else:
        print("Still didn't match.")
