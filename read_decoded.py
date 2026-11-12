with open('decoded_original_main.py', 'r', encoding='utf-8') as f:
    text = f.read()

# In decoded_original_main.py:
# llIlIlIIIl(x1, x2, ...) is x ^ 131!
import re

def de_xor(match):
    nums = [int(n.strip()) for n in match.group(1).split(',')]
    s = ''.join(chr(n ^ 131) for n in nums)
    return repr(s)

# Let's find how strings are encoded
# Let's print occurrences of lambda *a: ''.join(map(chr, [x ^ ...
for line in text.splitlines()[:20]:
    print(line)
