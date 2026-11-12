import json

with open(r'C:/Users/Al Amin/.gemini/antigravity/brain/1a4f9ac8-9c9e-43c3-b3dc-0a47d27cffea/.system_generated/logs/transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in range(75, 95):
            data = json.loads(line)
            tool_calls = data.get('tool_calls', [])
            for tc in tool_calls:
                args = tc.get('args') or tc.get('parameters') or tc.get('function', {}).get('arguments')
                print(f"Line {idx} {tc.get('name')}: {repr(args)[:200]}")
