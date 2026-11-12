import pyzipper

zip_path = r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.user_uploaded/media_1794484834854_0be8b3e1.zip'

with pyzipper.AESZipFile(zip_path, 'r') as z:
    for info in z.infolist():
        print(f"{info.filename}: flag={bin(info.flag_bits)}, comp={info.compress_type}, size={info.file_size}")
