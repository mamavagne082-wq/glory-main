with open('scratch_main_obj.bin', 'rb') as f:
    b = f.read()

import struct

for p in (165379, 165384, 165389, 165404):
    ref_id = struct.unpack('<i', b[p+1:p+5])[0]
    print(f"pos {p}: ref to {ref_id}")
