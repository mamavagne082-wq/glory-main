# In Python 3.12, let's compile a function that has a slice!
import marshal

code = compile("def f(x): return x[:256]", "<test>", "exec")
print("Compiled ok!")
dumped = marshal.dumps(code)
print("Dumped ok! Length:", len(dumped))
loaded = marshal.loads(dumped)
print("Loaded ok!", type(loaded))

# Let's inspect the constants of f
f_code = [c for c in code.co_consts if hasattr(c, 'co_consts')][0]
print("f constants:", f_code.co_consts)
for c in f_code.co_consts:
    print("  constant:", type(c), c)
