import zipfile

zip_path = r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.user_uploaded/media_1794484834854_0be8b3e1.zip'

with zipfile.ZipFile(zip_path, 'r') as z:
    for info in z.infolist():
        print(f"File: {info.filename}")
        print(f"  flag_bits: {bin(info.flag_bits)}")
        print(f"  compress_type: {info.compress_type}")
        print(f"  extra: {repr(info.extra)}")
        print(f"  comment: {repr(info.comment)}")
        print(f"  CRC: {hex(info.CRC)}")
        print(f"  compress_size: {info.compress_size}")
        print(f"  file_size: {info.file_size}")
        break
