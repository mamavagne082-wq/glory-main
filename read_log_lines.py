import json

with open(r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.system_generated/logs/transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx in [106, 108, 112, 124, 136, 142]:
    if idx < len(lines):
        data = json.loads(lines[idx])
        print(f"=== LINE {idx} ===")
        print(data.get('content', '')[:300])
        print("tool calls:", data.get('tool_calls', ''))
