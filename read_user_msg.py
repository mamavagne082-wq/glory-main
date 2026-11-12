import json

with open(r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.system_generated/logs/transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in (684, 685, 686):
            data = json.loads(line)
            print(f"=== STEP {idx} ===")
            print("source:", data.get('source'))
            print("content preview:", repr(data.get('content', '')[:1000]))
