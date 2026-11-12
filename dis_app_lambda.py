import marshal, dis

co_app = marshal.loads(open('scratch_app_obj.bin', 'rb').read())
lambdas = [c for c in co_app.co_consts if getattr(c, 'co_name', None) == '<lambda>']
print("Number of lambdas in app:", len(lambdas))
for idx, l in enumerate(lambdas[:3]):
    print(f"=== Lambda {idx} ===")
    dis.dis(l)
