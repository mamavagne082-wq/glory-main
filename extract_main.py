import marshal
import os

with open(r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.user_uploaded/media_1794484834870_282d43fc.py', 'r', encoding='utf-8') as f:
    code_text = f.read()

target = "exec(gNWcT.loads(AI99O))"
replacement = "open('scratch_main_obj.bin', 'wb').write(AI99O)"
code_text = code_text.replace(target, replacement)
globs = {'__name__': '__verify__'}
exec(code_text, globs)
print('Saved scratch_main_obj.bin, size:', os.path.getsize('scratch_main_obj.bin'))
