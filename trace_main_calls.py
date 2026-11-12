import marshal, sys

# Set a trace function to see every function call!
def tracer(frame, event, arg):
    if event == 'call':
        co = frame.f_code
        print(f"CALL {co.co_name} in {co.co_filename}:{frame.f_lineno}")
    return tracer

co = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
sys.settrace(tracer)
try:
    exec(co, {'__name__': '__main__', '__file__': r'c:\Users\Al Amin\Desktop\New folder (3)\100%FIX_GLORY\main.py'})
except Exception as e:
    print("EXITED:", e)
