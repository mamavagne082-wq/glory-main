from reconstruct_both import reconstruct_file
import types

co_main = reconstruct_file('scratch_main_obj.bin')
print('co_main type:', type(co_main))
print('co_main argcount:', co_main.co_argcount)
print('co_main nlocals:', co_main.co_nlocals)
print('co_main varnames:', co_main.co_varnames)
print('co_main freevars:', co_main.co_freevars)
print('co_main cellvars:', co_main.co_cellvars)
print('co_main names count:', len(co_main.co_names))
print('co_main consts count:', len(co_main.co_consts))

# Can we execute co_main?
# Let's test in a safe globals dictionary!
ns = {'__name__': '__main__'}
try:
    exec(co_main, ns)
    print("EXECUTION SUCCEEDED!")
    print("New globals:", [k for k in ns.keys() if not k.startswith('__')])
except Exception as e:
    import traceback
    print("EXECUTION FAILED:")
    traceback.print_exc()
