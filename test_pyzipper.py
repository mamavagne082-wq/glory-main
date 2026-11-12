import pyzipper

zip_path = r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.user_uploaded/media_1794484834854_0be8b3e1.zip'

# Let's test with empty password or no password first!
try:
    with pyzipper.AESZipFile(zip_path, 'r') as z:
        for name in z.namelist():
            data = z.read(name)
            print(f"NO PASSWORD NEEDED! {name}: {len(data)} bytes")
            break
except Exception as e:
    print("Without password failed:", e)

# Now test candidates
candidates = [
    'ARIYAN', 'ariyan', 'Ariyan', 'ARIYAN_A9X_BD', 'ariyan_a9x_bd',
    'glory', 'GLORY', 'Glory', 'ARIYAN_GLORY', 'ariyan_glory',
    '1234', '12345', '123456', '12345678', 'admin', 'root',
    'ALAMIN', 'alamin', 'Alamin', 'mamavagne082-wq',
    'A9X', 'a9x', 'A9X_BD', 'a9x_bd', 'AriyanPrime', 'ariyanprime',
    'AriyanPrime_A9x', '@AriyanPrime_A9x', 'bd', 'BD', 'bangladesh',
    'ff', 'freefire', 'FreeFire', 'apex', 'APEX', 'Apex',
    'apexcore', 'ApexCore', 'APEX_CORE', 'apex_core',
    '25567', '7069712'
]

with pyzipper.AESZipFile(zip_path, 'r') as z:
    for pwd in candidates:
        try:
            d = z.read('StartMatch_pb2.py', pwd=pwd.encode('utf-8'))
            print(f"SUCCESS! PASSWORD IS: {repr(pwd)}")
            print("Preview of StartMatch_pb2.py:")
            print(d[:200].decode('utf-8', errors='replace'))
            break
        except Exception:
            continue
    else:
        print("None of the common passwords worked.")
