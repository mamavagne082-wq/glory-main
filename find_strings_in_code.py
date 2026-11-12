import marshal

def search_in_code(co, target):
    found = []
    for c in co.co_consts:
        if isinstance(c, (str, bytes)):
            s = c if isinstance(c, str) else str(c)
            if target.lower() in s.lower():
                found.append((co.co_name, s))
        elif hasattr(c, 'co_consts'):
            found.extend(search_in_code(c, target))
    return found

co_main = marshal.loads(open('scratch_main_obj.bin', 'rb').read())
co_app = marshal.loads(open('scratch_app_obj.bin', 'rb').read())

print("Searching 'accounts' in main:", search_in_code(co_main, 'accounts'))
print("Searching 'not found' in main:", search_in_code(co_main, 'not found'))
print("Searching 'Enter to exit' in main:", search_in_code(co_main, 'Enter to exit'))

print("Searching 'accounts' in app:", search_in_code(co_app, 'accounts'))
print("Searching 'not found' in app:", search_in_code(co_app, 'not found'))
print("Searching 'Enter to exit' in app:", search_in_code(co_app, 'Enter to exit'))
