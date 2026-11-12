def decode_chars(a, offset):
    return ''.join(chr((x - offset) % 1114112) for x in a)

# Let's test offsets for 220, 220, 231, 234, 224, 247, 220, 220 -> '__builtins__'
target = "__builtins__"
nums = [220, 220, 231, 234, 224, 247, 220, 220]
# Wait, '__doc__' or '__name__'?
# '__doc__' is len 7: 220, 220, ..., 220, 220 is len 8?
# Let's find which offset gives valid ascii for all nums:
for off in range(256):
    s = ''.join(chr((x ^ off)) for x in nums)
    if s.startswith('__'):
        print(f"XOR off {off}: {s}")
    s2 = ''.join(chr((x - off) % 256) for x in nums)
    if s2.startswith('__'):
        print(f"SUB off {off}: {s2}")
