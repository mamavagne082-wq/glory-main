with open('scratch_main_obj.bin', 'rb') as f:
    b = f.read()

pos = 41739
print('Bytes around 41739:')
print(b[pos-50:pos+50])
