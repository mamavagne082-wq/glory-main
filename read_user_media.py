import json

with open(r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.system_generated/logs/transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx == 684:
            data = json.loads(line)
            print("Media:", data.get('media'))
            print("Keys:", data.keys())
