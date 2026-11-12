import pyzipper

zip_path = r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.user_uploaded/media_1794484834854_0be8b3e1.zip'

cands = [
    'Ariyan H4cks', 'ariyan h4cks', 'AriyanH4cks', 'ariyanh4cks',
    'Ariyan_H4cks', 'ariyan_h4cks', 'Ariyan H4ck', 'ariyan h4ck',
    'AriyanH4ck', 'ariyanh4ck', 'Ariyan_H4ck', 'ariyan_h4ck',
    'Ariyan Hacks', 'ariyan hacks', 'AriyanHacks', 'ariyanhacks',
    'Ariyan_Hacks', 'ariyan_hacks', 'H4cks', 'h4cks', 'Hacks', 'hacks',
    'AriyanPrime_A9x', 'AriyanPrime', 'Ariyan_A9x', 'ariyan_a9x',
    'Ariyan A9X', 'ariyan a9x', 'AriyanA9X', 'ariyana9x',
    'Free Fire Bot Squad Engine v2.0', 'Free Fire Bot Squad Engine',
    'Squad Engine', 'Bot Squad Engine', 'Free Fire', 'FreeFire',
    'free fire', 'freefire', 'FF', 'ff',
    'All Systems Online', 'Auto Create', 'Anti-AFK', 'Team Play',
    'Apex Glory Command', 'Apex Glory', 'apex glory', 'apexglory',
    'APEX GLORY', 'APEX_GLORY', 'apex_core', 'apex core', 'Apex Core',
    'ApexCore', 'APEX CORE', 'APEXCORE', 'ariyan@apex-core',
    'apex-core', 'apex_core', 'apexcore'
]

with pyzipper.AESZipFile(zip_path, 'r') as z:
    for pwd in cands:
        try:
            d = z.read('StartMatch_pb2.py', pwd=pwd.encode('utf-8'))
            print(f"FOUND PASSWORD! {repr(pwd)}")
            break
        except Exception:
            pass
    else:
        print("None worked.")
